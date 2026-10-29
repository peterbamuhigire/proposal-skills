#!/usr/bin/env python3
"""Read-only package parity and immutable full-checkout capacity gate."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIMIT = 5000
EXCLUDED = {'.git', '.cache', 'cache', '__pycache__', 'node_modules', '.venv', 'venv'}


def inventory(root):
    full = package = 0
    def refuse(error):
        raise error
    for current, dirs, files in os.walk(root, followlinks=False, onerror=refuse):
        base = Path(current)
        links = [name for name in dirs if (base / name).is_symlink()]
        dirs[:] = [name for name in dirs if name not in links]
        for name in files + links:
            full += 1
            if not EXCLUDED.intersection((base / name).relative_to(root).parts):
                package += 1
    return full, package


def validate(root=ROOT):
    root = Path(root).resolve()
    errors = []
    try:
        full, package = inventory(root)
        if max(full, package) > LIMIT:
            errors.append('hard 5000 file limit exceeded')
        print(f'checkout_files={full} package_files={package} hard_limit={LIMIT}')
        plugin = json.loads((root / '.claude-plugin/plugin.json').read_text())
        market = json.loads((root / '.claude-plugin/marketplace.json').read_text())
        entries = market['plugins']
        if len(entries) != 1 or entries[0]['name'] != plugin['name'] or entries[0]['version'] != plugin['version'] or entries[0]['source'] != './':
            errors.append('marketplace identity/version/local source mismatch')
        configured = plugin['skills']
        if not isinstance(configured, list) or not configured:
            raise ValueError('skills must be a nonempty list')
        actual = {p.parent.relative_to(root).as_posix() for p in (root / 'skills').rglob('SKILL.md')}
        selected = []
        for entry in configured:
            if not isinstance(entry, str) or not entry.startswith('./') or '..' in Path(entry).parts or '\\' in entry:
                raise ValueError('invalid relative skill path')
            path = root / entry
            if not path.resolve().is_relative_to(root) or any(part.is_symlink() for part in [path, *path.parents] if part != root):
                raise ValueError('skill path escape or symlink')
            if not (path / 'SKILL.md').is_file():
                raise ValueError('missing skill')
            selected.append(path.relative_to(root).as_posix())
        if len(selected) != len(set(selected)) or set(selected) != actual:
            errors.append('manifest skill path set differs from canonical catalogue')
        for name in ('AGENTS.md', 'README.md'):
            text = (root / name).read_text()
            if 'C:\\wamp64' in text or '/home/' in text or '/Users/' in text:
                errors.append(f'machine binding in {name}')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'incomplete or invalid package: {exc}')
    return errors


if __name__ == '__main__':
    findings = validate()
    print('\n'.join(findings) if findings else 'marketplace: PASS')
    raise SystemExit(bool(findings))
