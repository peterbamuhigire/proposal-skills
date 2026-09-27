#!/usr/bin/env python3
"""Validate the deterministic fictional proposal evidence fixture."""

from __future__ import annotations

import json
from datetime import datetime
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

    # Optional amendment records let the matrix preserve the source of a
    # changed requirement. Existing fixtures without amendments remain valid.
    amendments = package.get("amendments", [])
    if not isinstance(amendments, list):
        errors.append("amendments must be a list")
        amendments = []
    amendments_by_id: dict[str, dict[str, Any]] = {}
    for amendment in amendments:
        if not isinstance(amendment, dict):
            errors.append("amendments must contain objects")
            continue
        amendment_id = amendment.get("id")
        source_clause = amendment.get("source_clause")
        refs = amendment.get("requirement_ids")
        if not isinstance(amendment_id, str) or not amendment_id.strip():
            errors.append("amendment id must be a nonblank string")
            continue
        if amendment_id in amendments_by_id:
            errors.append(f"duplicate amendment id: {amendment_id}")
        amendments_by_id[amendment_id] = amendment
        if not isinstance(source_clause, str) or not source_clause.strip():
            errors.append(f"amendment {amendment_id} source_clause must be nonblank")
        if not isinstance(refs, list) or not refs:
            errors.append(f"amendment {amendment_id} requires requirement_ids")
        elif any(not isinstance(ref, str) or ref not in requirement_ids for ref in refs):
            errors.append(f"amendment {amendment_id} cites an unknown requirement")

    for requirement in requirements:
        source_clause = requirement.get("source_clause")
        if not isinstance(source_clause, str) or not source_clause.strip():
            errors.append(
                f"requirement {requirement.get('id')} requires a source_clause"
            )
        amendment_id = requirement.get("amendment_id")
        if amendment_id is None:
            continue
        amendment = amendments_by_id.get(amendment_id)
        if amendment is None:
            errors.append(
                f"requirement {requirement.get('id')} cites missing amendment {amendment_id}"
            )
        else:
            amendment_requirements = amendment.get("requirement_ids")
            if (
                not isinstance(amendment_requirements, list)
                or requirement.get("id") not in amendment_requirements
            ):
                errors.append(
                    f"amendment {amendment_id} does not map requirement {requirement.get('id')}"
                )

    # A package with unresolved authority or unsupported claims is not ready
    # even when the requirement/evidence rows happen to be structurally valid.
    controls = package.get("submission_controls")
    solicitation = package.get("solicitation")
    if (
        isinstance(solicitation, dict)
        and solicitation.get("type") == "EOI"
        and controls is None
    ):
        errors.append("EOI package requires submission_controls")
    if controls is not None:
        if not isinstance(controls, dict):
            errors.append("submission_controls must be an object")
        else:
            deadline = controls.get("deadline")
            if not isinstance(deadline, dict):
                errors.append("submission deadline must be an object")
            else:
                if not isinstance(deadline.get("source"), str) or not deadline["source"].strip():
                    errors.append("submission deadline requires a source")
                value = deadline.get("value")
                if not isinstance(value, str) or not value.strip():
                    errors.append("submission deadline requires a date-time value")
                else:
                    try:
                        parsed_deadline = datetime.fromisoformat(value)
                        if parsed_deadline.utcoffset() is None:
                            errors.append("submission deadline must include a timezone offset")
                    except ValueError:
                        errors.append("submission deadline must be an ISO date-time")
                if deadline.get("status") != "resolved":
                    errors.append("submission deadline conflict is unresolved")
                conflicts = deadline.get("conflicts", [])
                if not isinstance(conflicts, list):
                    errors.append("deadline conflicts must be a list")
                else:
                    for conflict in conflicts:
                        if (
                            not isinstance(conflict, dict)
                            or not isinstance(conflict.get("value"), str)
                            or not conflict["value"].strip()
                            or not isinstance(conflict.get("source"), str)
                            or not conflict["source"].strip()
                        ):
                            errors.append("deadline conflict requires a value and source")
                    if conflicts and deadline.get("status") == "resolved":
                        resolution = deadline.get("resolution")
                        if (
                            not isinstance(resolution, dict)
                            or not isinstance(resolution.get("source"), str)
                            or not resolution["source"].strip()
                            or not isinstance(resolution.get("owner"), str)
                            or not resolution["owner"].strip()
                        ):
                            errors.append("resolved deadline conflict requires source and owner")
            signatures = controls.get("required_signatures")
            if not isinstance(signatures, list) or not signatures:
                errors.append("required signatures must be a non-empty list")
            else:
                for signature in signatures:
                    if not isinstance(signature, dict):
                        errors.append("required signature records must be objects")
                    else:
                        role = signature.get("role", "?")
                        if (
                            signature.get("status") != "signed"
                            or not isinstance(signature.get("owner"), str)
                            or not signature["owner"].strip()
                        ):
                            errors.append(
                                f"required signature {role} is missing or unowned"
                            )
                        evidence_id = signature.get("evidence_id")
                        evidence_record = (
                            evidence_by_id.get(evidence_id)
                            if isinstance(evidence_id, str)
                            else None
                        )
                        if evidence_record is None or evidence_record.get("status") != "available":
                            errors.append(
                                f"required signature {role} has no available evidence"
                            )
            final_authority = controls.get("final_authority")
            if (
                not isinstance(final_authority, dict)
                or final_authority.get("status") != "approved"
                or not isinstance(final_authority.get("owner"), str)
                or not final_authority["owner"].strip()
            ):
                errors.append("final submission authority is not approved by a named owner")
            elif (
                not isinstance(final_authority.get("evidence_id"), str)
                or final_authority["evidence_id"] not in evidence_by_id
                or evidence_by_id[final_authority["evidence_id"]].get("status") != "available"
            ):
                errors.append("final submission authority has no available evidence")
            claims = controls.get("claims", [])
            if not isinstance(claims, list):
                errors.append("submission claims must be a list")
            else:
                seen_claims: set[str] = set()
                for claim in claims:
                    if not isinstance(claim, dict):
                        errors.append("submission claims must contain objects")
                        continue
                    claim_id = claim.get("id")
                    if not isinstance(claim_id, str) or not claim_id.strip():
                        errors.append("submission claim id must be nonblank")
                    elif claim_id in seen_claims:
                        errors.append(f"duplicate submission claim id: {claim_id}")
                    else:
                        seen_claims.add(claim_id)
                    if claim.get("status") == "unsupported" and claim.get("included") is not False:
                        errors.append(f"unsupported claim {claim_id or '?'} must be excluded")
                    if claim.get("status") not in {"supported", "unsupported"}:
                        errors.append(f"submission claim {claim_id or '?'} has invalid status")
                    if not isinstance(claim.get("included"), bool):
                        errors.append(f"submission claim {claim_id or '?'} included must be boolean")
                    if claim.get("status") == "supported":
                        claim_evidence = claim.get("evidence_ids")
                        if not isinstance(claim_evidence, list) or not claim_evidence:
                            errors.append(f"supported claim {claim_id or '?'} requires evidence")
                        else:
                            for evidence_id in claim_evidence:
                                item = evidence_by_id.get(evidence_id)
                                if item is None or item.get("status") != "available":
                                    errors.append(
                                        f"supported claim {claim_id or '?'} cites unavailable evidence {evidence_id}"
                                    )

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

    approved_envelopes = set()
    for item in approvals:
        if item.get("status") != "approved":
            continue
        owner = item.get("owner")
        if not isinstance(owner, str) or not owner.strip():
            continue
        evidence_id = item.get("evidence_id")
        approval_evidence = (
            evidence_by_id.get(evidence_id)
            if isinstance(evidence_id, str)
            else None
        )
        envelope = item.get("envelope")
        if approval_evidence is None or approval_evidence.get("status") != "available":
            errors.append(f"{envelope or '?'} approval has no available evidence")
            continue
        approved_envelopes.add(envelope)
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
