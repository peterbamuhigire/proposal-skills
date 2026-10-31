#!/usr/bin/env python3
"""Propose or check a page allocation against a solicitation's cap and weights.

Allocation arithmetic only. It does not predict an evaluator's score, read a real
solicitation or certify compliance: the issued solicitation's caps, weights,
floors and exclusions are the inputs and stay the controlling text.

Input (JSON):
  page_cap            pages available to the scored narrative
  page_unit           allocation step in pages, for example 0.25
  criteria[]          id, points, optional floor_pages, embedded (no pages of its
                      own), evidence_outside_cap, justification
  allocation          optional {criterion id: pages} to check instead of propose
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

DEFAULT_TOLERANCE = 0.4


def _number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def validate_spec(spec) -> list[str]:
    errors: list[str] = []
    if not isinstance(spec, dict):
        return ["specification must be an object"]
    if not _number(spec.get("page_cap")) or spec["page_cap"] <= 0:
        errors.append("page_cap must be a positive number")
    unit = spec.get("page_unit", 0.25)
    if not _number(unit) or unit <= 0:
        errors.append("page_unit must be a positive number")
    elif _number(spec.get("page_cap")) and abs(spec["page_cap"] / unit - round(spec["page_cap"] / unit)) > 1e-9:
        errors.append("page_cap must be a whole multiple of page_unit")
    criteria = spec.get("criteria")
    if not isinstance(criteria, list) or not criteria:
        return errors + ["criteria must be a non-empty list"]
    seen: set[str] = set()
    for row in criteria:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"].strip():
            errors.append("each criterion needs a non-empty id")
            continue
        if row["id"] in seen:
            errors.append(f"duplicate criterion {row['id']}")
        seen.add(row["id"])
        if not _number(row.get("points")) or row["points"] <= 0:
            errors.append(f"{row['id']}: points must be a positive number")
        floor = row.get("floor_pages", 0)
        if not _number(floor) or floor < 0:
            errors.append(f"{row['id']}: floor_pages must be zero or more")
        if row.get("embedded") is not None and not isinstance(row["embedded"], bool):
            errors.append(f"{row['id']}: embedded must be true or false")
    return errors


def propose(spec: dict) -> dict[str, float]:
    """Proportional allocation in whole units with floors, largest remainder."""
    unit = spec.get("page_unit", 0.25)
    total_units = round(spec["page_cap"] / unit)
    live = [row for row in spec["criteria"] if not row.get("embedded")]
    floors = {row["id"]: math.ceil(row.get("floor_pages", 0) / unit - 1e-9) for row in live}
    if sum(floors.values()) > total_units:
        raise ValueError("floors alone exceed the page cap")
    fixed: dict[str, float] = {}
    while True:
        free = [row for row in live if row["id"] not in fixed]
        budget = total_units - sum(fixed.values())
        weight = sum(row["points"] for row in free)
        ideal = {row["id"]: budget * row["points"] / weight for row in free}
        short = [row["id"] for row in free if ideal[row["id"]] < floors[row["id"]]]
        if not short:
            break
        for identifier in short:
            fixed[identifier] = floors[identifier]
    base = {identifier: math.floor(value + 1e-9) for identifier, value in ideal.items()}
    leftover = total_units - sum(fixed.values()) - sum(base.values())
    order = sorted(ideal, key=lambda i: (-(ideal[i] - base[i]), -next(r["points"] for r in live if r["id"] == i), i))
    for identifier in order[:leftover]:
        base[identifier] += 1
    units = {**fixed, **base}
    result = {row["id"]: units.get(row["id"], 0) * unit for row in spec["criteria"]}
    return result


def check(spec: dict, allocation: dict, tolerance: float = DEFAULT_TOLERANCE) -> list[str]:
    errors: list[str] = []
    criteria = {row["id"]: row for row in spec["criteria"]}
    for identifier in allocation:
        if identifier not in criteria:
            errors.append(f"allocation names unknown criterion {identifier}")
    for identifier in criteria:
        value = allocation.get(identifier)
        if not _number(value) or value < 0:
            errors.append(f"{identifier}: allocation must be a number of pages, zero or more")
    if errors:
        return errors
    if sum(allocation.values()) > spec["page_cap"] + 1e-9:
        errors.append(f"allocation uses {sum(allocation.values()):g} pages; cap is {spec['page_cap']:g}")
    live = {i: row for i, row in criteria.items() if not row.get("embedded")}
    total_points = sum(row["points"] for row in live.values())
    used = sum(allocation[i] for i in live) or 1
    for identifier, row in live.items():
        pages = allocation[identifier]
        if pages == 0:
            errors.append(f"{identifier}: carries {row['points']:g} points but has no pages")
            continue
        if pages + 1e-9 < row.get("floor_pages", 0):
            errors.append(f"{identifier}: {pages:g} pages is below its floor of {row['floor_pages']:g}")
        share_points = row["points"] / total_points
        share_pages = pages / used
        if (
            share_pages < share_points * (1 - tolerance)
            and not row.get("evidence_outside_cap")
            and not str(row.get("justification", "")).strip()
        ):
            errors.append(
                f"{identifier}: {share_pages:.0%} of pages for {share_points:.0%} of points "
                "(add evidence_outside_cap or a justification if intended)"
            )
    ordered = sorted(live.items(), key=lambda item: -item[1]["points"])
    for index, (high_id, high) in enumerate(ordered):
        for low_id, low in ordered[index + 1:]:
            if (
                high["points"] > low["points"]
                and allocation[high_id] < allocation[low_id]
                and not str(high.get("justification", "")).strip()
                and not high.get("evidence_outside_cap")
                and not str(low.get("justification", "")).strip()
            ):
                errors.append(
                    f"{low_id} ({low['points']:g} points) has more pages than {high_id} ({high['points']:g} points)"
                )
    return errors


def render(spec: dict, allocation: dict) -> str:
    live = {row["id"]: row for row in spec["criteria"] if not row.get("embedded")}
    total_points = sum(row["points"] for row in live.values())
    used = sum(allocation[i] for i in live) or 1
    lines = ["| Criterion | Points | Share of points | Pages | Share of pages |", "|---|---:|---:|---:|---:|"]
    for row in spec["criteria"]:
        identifier = row["id"]
        if row.get("embedded"):
            lines.append(f"| {identifier} | {row['points']:g} | embedded | 0 | embedded |")
        else:
            lines.append(
                f"| {identifier} | {row['points']:g} | {row['points'] / total_points:.1%} | "
                f"{allocation[identifier]:g} | {allocation[identifier] / used:.1%} |"
            )
    lines.append(f"| Total | | | {sum(allocation.values()):g} of {spec['page_cap']:g} | |")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", type=Path, help="JSON specification")
    parser.add_argument("--propose", action="store_true", help="print a proportional allocation and exit")
    parser.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE)
    args = parser.parse_args(argv)
    spec = json.loads(args.input.read_text(encoding="utf-8"))
    problems = validate_spec(spec)
    if problems:
        print("\n".join(f"[ERROR] {item}" for item in problems))
        return 1
    if args.propose or "allocation" not in spec:
        try:
            allocation = propose(spec)
        except ValueError as exc:
            print(f"[ERROR] {exc}")
            return 1
        print(render(spec, allocation))
        print("scope: allocation arithmetic only; not a prediction of evaluator scores")
        return 0
    errors = check(spec, spec["allocation"], args.tolerance)
    print(render(spec, spec["allocation"]))
    print(f"page-budget-check: {'PASS' if not errors else 'FAIL'}")
    for item in errors:
        print(f"[ERROR] {item}")
    print("scope: allocation arithmetic only; not a prediction of evaluator scores")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
