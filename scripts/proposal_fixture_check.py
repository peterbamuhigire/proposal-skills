#!/usr/bin/env python3
"""Validate the deterministic fictional proposal evidence fixture."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


FIXTURE = Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "fictional-bid-package.json"


def validate_bid_package(package: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not str(package.get("fixture_label", "")).startswith("FICTIONAL TEST DATA"):
        errors.append("fixture must be explicitly labelled fictional test data")

    requirements = package.get("requirements", [])
    evidence = package.get("evidence", [])
    responses = package.get("responses", [])
    envelopes = package.get("envelopes", {})
    approvals = package.get("approvals", [])
    requirement_ids = {item.get("id") for item in requirements}
    evidence_by_id = {item.get("id"): item for item in evidence}
    response_by_requirement = {item.get("requirement_id"): item for item in responses}

    if not requirements:
        errors.append("fixture must declare at least one requirement")

    if set(envelopes) != {"technical", "financial"}:
        errors.append("technical and financial envelopes must both be declared")
    files_by_envelope = {
        name: set(value.get("files", [])) for name, value in envelopes.items()
    }
    if files_by_envelope.get("technical", set()) & files_by_envelope.get("financial", set()):
        errors.append("technical and financial envelope files must not overlap")

    for requirement in requirements:
        requirement_id = requirement.get("id")
        requirement_envelope = requirement.get("envelope")
        expected_location = requirement.get("response_location")
        response = response_by_requirement.get(requirement_id)
        if requirement_envelope not in envelopes:
            errors.append(
                f"requirement {requirement_id} uses undeclared envelope {requirement_envelope}"
            )
        elif expected_location not in files_by_envelope[requirement_envelope]:
            errors.append(
                f"requirement {requirement_id} response location is not in "
                f"the {requirement_envelope} envelope"
            )
        if not requirement.get("evidence_owner"):
            errors.append(f"requirement {requirement_id} has no evidence owner")
        if requirement.get("mandatory") and response is None:
            errors.append(f"mandatory requirement {requirement_id} has no response")
            continue
        if response is None:
            continue
        response_envelope = response.get("envelope")
        response_location = response.get("response_location")
        if response_envelope != requirement_envelope:
            errors.append(f"requirement {requirement_id} crosses envelope boundaries")
        if response_location != expected_location:
            errors.append(f"requirement {requirement_id} response location is not traceable")
            if (
                response_envelope in files_by_envelope
                and response_location not in files_by_envelope[response_envelope]
            ):
                errors.append(
                    f"requirement {requirement_id} response location is outside "
                    f"the {response_envelope} envelope"
                )
        if not response.get("evidence_ids"):
            errors.append(f"requirement {requirement_id} has no evidence")
        expected_owner = requirement.get("evidence_owner")
        for evidence_id in response.get("evidence_ids", []):
            item = evidence_by_id.get(evidence_id)
            if item is None:
                errors.append(f"requirement {requirement_id} cites missing evidence {evidence_id}")
            elif item.get("owner") != expected_owner:
                errors.append(f"requirement {requirement_id} evidence owner is not {expected_owner}")

    unknown_responses = set(response_by_requirement) - requirement_ids
    for requirement_id in sorted(unknown_responses):
        errors.append(f"response cites unknown requirement {requirement_id}")

    approved_envelopes = {
        item.get("envelope") for item in approvals if item.get("status") == "approved"
    }
    for envelope in ("technical", "financial"):
        if envelope not in approved_envelopes:
            errors.append(f"{envelope} envelope has no approved review record")

    return errors


def main() -> int:
    package = json.loads(FIXTURE.read_text(encoding="utf-8"))
    errors = validate_bid_package(package)
    print(f"proposal-fixture-check: {FIXTURE}")
    print(f"result: {'PASS' if not errors else 'FAIL'}")
    for error in errors:
        print(f"[ERROR] {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
