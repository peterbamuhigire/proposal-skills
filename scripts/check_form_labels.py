#!/usr/bin/env python3
"""Reject stale World Bank form labels in every active skill.

The correct map lives in tests/fixtures/world-bank-form-map.json. This check
looks for the retired pairings recorded there (for example TECH-7 described as a
staffing schedule) and for forms the inspected RFP does not contain (FIN-5).
It is a label check. It does not assess any bid, and the issued RFP still
controls the forms of a real solicitation.

Known limit: a paragraph that carries one of the recorded warning phrases (a
sentence telling the reader not to use the old mapping) is exempt as a whole, so
a stale label hidden inside such a paragraph would pass. Table rows are checked
line by line and are never exempted by a phrase elsewhere.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES_PATH = "tests/fixtures/world-bank-form-map.json"
FORM_ID = re.compile(r"\b(TECH|FIN)-(\d)(?:/(\d))?")


def load_rules(root: Path) -> dict:
    data = json.loads((root / RULES_PATH).read_text(encoding="utf-8"))
    return {
        "stale": {k: [p.lower() for p in v] for k, v in data.get("stale_associations", {}).items()},
        "unsupported": set(data.get("unsupported_forms", [])),
        "warnings": [p.lower() for p in data.get("warning_phrases", [])],
    }


def paragraphs(lines: list[str]) -> list[str]:
    """Context text for each line: its own row for tables, else its paragraph."""
    contexts = [""] * len(lines)
    block: list[int] = []

    def flush() -> None:
        joined = " ".join(lines[i] for i in block).lower()
        for i in block:
            contexts[i] = joined
        block.clear()

    for index, line in enumerate(lines):
        if not line.strip():
            flush()
        elif line.lstrip().startswith("|"):
            flush()
            contexts[index] = line.lower()
        else:
            block.append(index)
    flush()
    return contexts


def scan_text(text: str, rules: dict) -> list[tuple[int, str]]:
    """Return (line number, message) pairs for one document."""
    lines = text.splitlines()
    contexts = paragraphs(lines)
    findings: list[tuple[int, str]] = []
    for number, line in enumerate(lines, start=1):
        matches = list(FORM_ID.finditer(line))
        if not matches or any(w in contexts[number - 1] for w in rules["warnings"]):
            continue
        for position, match in enumerate(matches):
            kind, first, second = match.groups()
            identifiers = [f"{kind}-{first}"] + ([f"{kind}-{second}"] if second else [])
            end = matches[position + 1].start() if position + 1 < len(matches) else len(line)
            following = line[match.end():end].lower()
            preceding = line[:match.start() - 1].lower() if line[match.start() - 1:match.start()] == "(" else ""
            for identifier in identifiers:
                if identifier in rules["unsupported"]:
                    findings.append((number, f"{identifier} is not in the inspected March 2025 RFP"))
                for phrase in rules["stale"].get(identifier, []):
                    if phrase in following or phrase in preceding:
                        findings.append((number, f"{identifier} described as '{phrase}' (retired mapping)"))
    return findings


def validate(root: Path = ROOT) -> list[str]:
    try:
        rules = load_rules(root)
    except (OSError, ValueError) as exc:
        return [f"form-label rules unavailable: {exc}"]
    errors: list[str] = []
    for path in sorted((root / "skills").rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"form-label scan could not read {path.relative_to(root).as_posix()}: {exc}")
            continue
        relative = path.relative_to(root).as_posix()
        for number, message in scan_text(text, rules):
            errors.append(f"stale form label: {relative}:{number}: {message}")
    return errors


if __name__ == "__main__":
    problems = validate()
    print("\n".join(problems) if problems else "form labels: PASS; label check only, the issued RFP controls")
    sys.exit(1 if problems else 0)
