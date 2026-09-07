#!/usr/bin/env python3
"""Validate the deterministic fictional proposal evidence fixture."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


FIXTURE = Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "fictional-bid-package.json"


def has_parent_traversal(path: str) -> bool:
    """Check fixture path segments without accessing the filesystem."""
    return '..' in path.replace('\\', '/').split('/')


def validate_bid_package(package: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(package, dict):
        return ['package must be an object']
    # Validate identities before dict construction can silently overwrite them.
    for collection, identity in (('requirements', 'id'), ('evidence', 'id'),
                                 ('responses', 'requirement_id')):
        rows = package.get(collection)
        if not isinstance(rows, list):
            errors.append(f'{collection} must be a list')
            continue
        seen = set()
        for row in rows:
            value = row.get(identity) if isinstance(row, dict) else None
            if not isinstance(value, str) or not value.strip():
                errors.append(f'{collection} requires object rows with non-empty {identity}')
            elif value in seen:
                errors.append(f'{collection} has duplicate {identity}: {value}')
            else:
                seen.add(value)
            if not isinstance(row, dict):
                continue
            if collection == 'requirements' and not isinstance(row.get('mandatory'), bool):
                errors.append(f'requirement {value} mandatory must be boolean')
            if collection in ('requirements', 'evidence'):
                owner_field = 'evidence_owner' if collection == 'requirements' else 'owner'
                owner = row.get(owner_field)
                if not isinstance(owner, str) or not owner.strip():
                    label = 'requirement' if collection == 'requirements' else 'evidence'
                    errors.append(f'{label} {value} {owner_field} must be a nonblank string')
            if collection in ('requirements', 'responses'):
                for field in ('envelope', 'response_location'):
                    if not isinstance(row.get(field), str):
                        errors.append(f'{collection} {value} requires string {field}')
                    elif field == 'response_location' and has_parent_traversal(row[field]):
                        errors.append(f'{collection} {value} response_location must not contain parent traversal')
            if collection == 'responses':
                ids = row.get('evidence_ids')
                if not isinstance(ids, list) or any(not isinstance(i, str) or not i.strip() for i in ids):
                    errors.append(f'response {value} evidence_ids must be a list of strings')
    envelope_records = package.get('envelopes')
    if not isinstance(envelope_records, dict):
        errors.append('envelopes must be an object')
    else:
        for name, record in envelope_records.items():
            files = record.get('files') if isinstance(record, dict) else None
            if not isinstance(files, list) or any(not isinstance(f, str) or not f.strip() for f in files):
                errors.append(f'envelope {name} files must be a list of strings')
            elif any(has_parent_traversal(f) for f in files):
                errors.append(f'envelope {name} files must not contain parent traversal')
    approval_records = package.get('approvals')
    if not isinstance(approval_records, list) or any(
        not isinstance(r, dict) or not isinstance(r.get('envelope'), str)
        for r in approval_records
    ):
        errors.append('approvals must contain objects with an envelope')
    if errors:
        return errors
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
            elif item.get('status') != 'available':
                errors.append(f'requirement {requirement_id} evidence {evidence_id} is not available')

    unknown_responses = set(response_by_requirement) - requirement_ids
    for requirement_id in sorted(unknown_responses):
        errors.append(f"response cites unknown requirement {requirement_id}")

    approved_envelopes = {
        item.get("envelope") for item in approvals if item.get("status") == "approved"
        and isinstance(item.get('owner'), str) and item['owner'].strip()
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
