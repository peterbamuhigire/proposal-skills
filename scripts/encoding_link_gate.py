#!/usr/bin/env python3
"""Check repository text encoding, Markdown links, and portable engine routes."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".json", ".py", ".txt", ".yaml", ".yml"}
MARKDOWN_SUFFIXES = {".md"}
EXCLUDED_PARTS = {".git", ".venv", "__pycache__", "node_modules", "proposals"}
MOJIBAKE_MARKERS = ("\u00c3", "\u00c2", "\u00e2\u20ac", "\u00e2\u2020", "\u00f0\u0178", "\ufffd")
STALE_DEVICE_ROUTE = re.compile(
    r"C:\\Users\\[^\s|)]+\\source\\repos\\(?:social-media-skills|business-plan-skills)",
    re.IGNORECASE,
)
PORTABLE_ROUTES = {
    "social-media-skills": "https://github.com/peterbamuhigire/social-media-skills",
    "business-plan-skills": "https://github.com/peterbamuhigire/business-plan-skills",
}


def repository_files(root: Path, suffixes: set[str]):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        if any(part in EXCLUDED_PARTS for part in path.relative_to(root).parts):
            continue
        yield path


def resolve_markdown_target(path: Path, target: str, root: Path) -> Path | None:
    clean = target.split("#", 1)[0].strip()
    if not clean or clean.startswith(("#", "mailto:")) or "://" in clean:
        return None
    if clean.startswith("/") and re.match(r"^/[A-Za-z]:/", clean):
        return Path(clean[1:])
    if clean.startswith("/"):
        return None
    return path.parent / clean


def check(root: Path) -> list[str]:
    findings: list[str] = []
    decoded: dict[Path, str] = {}
    route_surfaces = {
        root / "README.md",
        root / "AGENTS.md",
        root / "CLAUDE.md",
        root / "skills" / "SKILL.md",
    }

    for path in repository_files(root, TEXT_SUFFIXES):
        relative = path.relative_to(root).as_posix()
        try:
            text = path.read_bytes().decode("utf-8")
        except UnicodeDecodeError as error:
            findings.append(f"invalid UTF-8: {relative}: {error}")
            continue
        decoded[path] = text
        if path.suffix.lower() in MARKDOWN_SUFFIXES:
            for marker in MOJIBAKE_MARKERS:
                if marker in text:
                    escaped = marker.encode("unicode_escape").decode()
                    findings.append(f"mojibake marker {escaped}: {relative}")
            if path in route_surfaces or "skills" in path.relative_to(root).parts:
                stale_route = STALE_DEVICE_ROUTE.search(text)
            else:
                stale_route = None
            if stale_route:
                findings.append(f"stale device-specific sibling route: {relative}")

    for path, text in decoded.items():
        if path.suffix.lower() not in MARKDOWN_SUFFIXES:
            continue
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            candidate = resolve_markdown_target(path, target, root)
            if candidate is not None and not candidate.resolve().exists():
                findings.append(
                    f"broken local Markdown link: {path.relative_to(root).as_posix()} -> {target}"
                )

    readme = root / "README.md"
    readme_text = decoded.get(readme, "")
    for route_key, canonical_url in PORTABLE_ROUTES.items():
        if canonical_url not in readme_text:
            findings.append(f"missing canonical route for {route_key}: {canonical_url}")

    return findings


def main() -> int:
    findings = check(ROOT)
    print(f"encoding-link-gate: {ROOT}")
    print(f"findings: {len(findings)}")
    for finding in findings:
        print(f"[ERROR] {finding}")
    if not findings:
        print("encoding: PASS; local Markdown links: PASS; portable sibling routes: PASS")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
