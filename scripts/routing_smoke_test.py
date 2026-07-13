#!/usr/bin/env python3
"""Rank live skill descriptions against representative routing prompts."""

from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "routing-fixtures.json"
STOP = {"a", "an", "and", "as", "at", "be", "by", "for", "from", "in", "is", "it", "of", "on", "or", "that", "the", "this", "to", "use", "when", "with"}


def tokens(text: str) -> list[str]:
    return [token for token in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text.lower()) if token not in STOP and len(token) > 2]


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    return yaml.safe_load(match.group(1)) if match else {}


def main() -> int:
    fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))["fixtures"]
    catalogue: dict[str, str] = {}
    for path in sorted((ROOT / "skills").rglob("SKILL.md")):
        fm = frontmatter(path)
        catalogue[path.relative_to(ROOT).as_posix().removesuffix("/SKILL.md")] = str(fm.get("description", ""))

    document_frequency: Counter[str] = Counter()
    description_tokens: dict[str, Counter[str]] = {}
    for skill, description in catalogue.items():
        counts = Counter(tokens(f"{skill.replace('/', ' ')} {description}"))
        description_tokens[skill] = counts
        document_frequency.update(counts.keys())

    failures: list[dict] = []
    for fixture in fixtures:
        prompt_tokens = Counter(tokens(fixture["prompt"]))
        ranked: list[tuple[float, str]] = []
        for skill, counts in description_tokens.items():
            score = sum(
                min(amount, counts[token]) * (1.0 + math.log((1 + len(catalogue)) / (1 + document_frequency[token])))
                for token, amount in prompt_tokens.items()
            )
            ranked.append((score, skill))
        top_three = [skill for _, skill in sorted(ranked, key=lambda item: (-item[0], item[1]))[:3]]
        passed = fixture["expected"] in top_three
        if not passed:
            failures.append({"id": fixture["id"], "expected": fixture["expected"], "top_three": top_three})
        print(f"{'PASS' if passed else 'FAIL'} {fixture['id']}: {fixture['expected']} | top3={', '.join(top_three)}")

    precision = (len(fixtures) - len(failures)) / len(fixtures) if fixtures else 0.0
    print(f"routing fixtures: {len(fixtures)}; top-three precision: {precision:.1%}; threshold: 100.0%")
    return 1 if failures or precision < 1.0 else 0


if __name__ == "__main__":
    sys.exit(main())
