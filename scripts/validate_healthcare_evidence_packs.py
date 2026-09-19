#!/usr/bin/env python3
"""Validate synthetic proposal evidence contracts for the Phase 1 health slice."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_STATES = {
    "supported",
    "partial",
    "inference",
    "unsupported",
    "no-source",
    "NOT_ASSESSED",
    "DENIED",
}
REQUIRED_SOURCE_FIELDS = {
    "claim",
    "source_scope",
    "source_version",
    "publication_or_revision_date",
    "access_date",
    "verification_date",
    "freshness_class",
    "review_date",
    "uncertainty",
    "owner",
}


def _nonblank(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _ids(value: Any) -> bool:
    """Require a non-empty list of nonblank identifiers."""
    return isinstance(value, list) and bool(value) and all(_nonblank(item) for item in value)


def _string_list(value: Any) -> bool:
    """Allow an explicitly empty list for the no-source state."""
    return isinstance(value, list) and all(_nonblank(item) for item in value)


def _validate_sources(data: dict[str, Any], errors: list[str]) -> set[str]:
    records = data.get("evidence_records")
    if not isinstance(records, list) or not records:
        errors.append("evidence_records must be a non-empty list")
        return set()
    seen: set[str] = set()
    for record in records:
        if not isinstance(record, dict) or not _nonblank(record.get("evidence_id")):
            errors.append("each evidence record requires a nonblank evidence_id")
            continue
        evidence_id = record["evidence_id"]
        if evidence_id in seen:
            errors.append(f"duplicate evidence_id: {evidence_id}")
        seen.add(evidence_id)
        for field in REQUIRED_SOURCE_FIELDS:
            if not _nonblank(record.get(field)):
                errors.append(f"evidence {evidence_id} requires nonblank {field}")
        review = record.get("support_review")
        if not isinstance(review, dict):
            errors.append(f"evidence {evidence_id} requires support_review")
            continue
        state = review.get("state")
        source_ids = review.get("source_ids")
        if state not in ALLOWED_STATES:
            errors.append(f"evidence {evidence_id} has invalid support state")
        if not _string_list(source_ids):
            errors.append(f"evidence {evidence_id} source_ids must be a list of strings")
        elif state == "no-source" and source_ids:
            errors.append(f"evidence {evidence_id} no-source must use an empty source_ids list")
        elif state != "no-source" and not source_ids:
            errors.append(f"evidence {evidence_id} non-no-source state needs a source_id")
        for field in ("reviewer", "basis", "review_date"):
            if not _nonblank(review.get(field)):
                errors.append(f"evidence {evidence_id} support_review requires {field}")
    return seen


def _known_evidence(
    evidence_ids: Any, known: set[str], label: str, errors: list[str], required: bool = True
) -> None:
    if not _ids(evidence_ids):
        if required:
            errors.append(f"{label} evidence_ids must be a non-empty list")
        return
    for evidence_id in evidence_ids:
        if evidence_id not in known:
            errors.append(f"{label} cites unknown evidence {evidence_id}")


def _validate_integration(data: dict[str, Any], known: set[str], errors: list[str]) -> None:
    pack = data.get("integration_tenant_checks")
    if not isinstance(pack, dict):
        errors.append("integration_tenant_checks must be an object")
        return
    cases = pack.get("cases")
    if not isinstance(cases, list):
        errors.append("integration cases must be a list")
        return
    required = {"wrong-tenant-read", "wrong-tenant-write", "duplicate-event", "interrupted-transfer"}
    found: set[str] = set()
    for case in cases:
        case_id = case.get("case_id") if isinstance(case, dict) else None
        if not _nonblank(case_id):
            errors.append("integration case requires case_id")
            continue
        if case_id in found:
            errors.append(f"duplicate integration case_id: {case_id}")
        found.add(case_id)
        for field in ("expected", "observed", "state", "reviewer", "review_date"):
            if not _nonblank(case.get(field)):
                errors.append(f"integration case {case_id} requires {field}")
        _known_evidence(case.get("evidence_ids"), known, f"integration case {case_id}", errors)
        expected = case.get("expected")
        observed = case.get("observed")
        if expected != observed:
            errors.append(f"integration case {case_id} observed result does not meet expected result")
        if case_id.startswith("wrong-tenant-") and observed != "deny":
            errors.append(f"integration case {case_id} must deny cross-tenant access")
        if case_id == "duplicate-event" and observed != "idempotent-or-held":
            errors.append("duplicate-event must be idempotent-or-held")
        if case_id == "interrupted-transfer" and observed != "resume-or-reconcile":
            errors.append("interrupted-transfer must resume-or-reconcile")
    missing = required - found
    for case_id in sorted(missing):
        errors.append(f"missing required integration case: {case_id}")


def _validate_governance_budget(data: dict[str, Any], known: set[str], errors: list[str]) -> None:
    pack = data.get("governance_budget")
    if not isinstance(pack, dict):
        errors.append("governance_budget must be an object")
        return
    options = pack.get("decisions")
    if not isinstance(options, list) or not options:
        errors.append("governance decisions must be a non-empty list")
    else:
        for option in options:
            decision_id = option.get("decision_id") if isinstance(option, dict) else None
            if not _nonblank(decision_id):
                errors.append("decision requires decision_id")
                continue
            _known_evidence(option.get("evidence_ids"), known, f"decision {decision_id}", errors)
            if option.get("status") == "approved":
                for field in ("authority", "approval_reference", "review_date"):
                    if not _nonblank(option.get(field)):
                        errors.append(f"approved decision {decision_id} requires {field}")
    lines = pack.get("budget_lines")
    if not isinstance(lines, list) or not lines:
        errors.append("budget_lines must be a non-empty list")
    else:
        for line in lines:
            line_id = line.get("line_id") if isinstance(line, dict) else None
            if not _nonblank(line_id):
                errors.append("budget line requires line_id")
                continue
            _known_evidence(line.get("evidence_ids"), known, f"budget line {line_id}", errors)
            if line.get("material") is True:
                for field in ("basis_type", "basis_source_id", "period", "reviewer"):
                    if not _nonblank(line.get(field)):
                        errors.append(f"material budget line {line_id} requires {field}")
                if str(line.get("basis_type", "")).lower() in {"book", "textbook", "generic-benchmark"}:
                    errors.append(f"material budget line {line_id} uses an impermissible textbook basis")
    links = pack.get("links")
    if not isinstance(links, dict):
        errors.append("governance budget links must be an object")
    else:
        for field in ("service", "staffing", "cash", "risks", "milestones"):
            if not _ids(links.get(field)):
                errors.append(f"governance budget links require {field}")


def _validate_hr(data: dict[str, Any], known: set[str], errors: list[str]) -> None:
    pack = data.get("hr_safety_metrics")
    if not isinstance(pack, dict):
        errors.append("hr_safety_metrics must be an object")
        return
    for case in pack.get("conduct_cases", []):
        case_id = case.get("case_id") if isinstance(case, dict) else None
        if not _nonblank(case_id):
            errors.append("conduct case requires case_id")
            continue
        _known_evidence(case.get("evidence_ids"), known, f"conduct case {case_id}", errors)
        if case.get("status") == "closed":
            for field in ("disposition", "staff_response", "reviewer", "closed_at", "evidence_hold_decision"):
                if not _nonblank(case.get(field)):
                    errors.append(f"closed conduct case {case_id} requires {field}")
    competencies = pack.get("competencies", [])
    for item in competencies:
        competency_id = item.get("competency_id") if isinstance(item, dict) else None
        if not _nonblank(competency_id):
            errors.append("competency record requires competency_id")
            continue
        _known_evidence(item.get("evidence_ids"), known, f"competency {competency_id}", errors)
        if item.get("safety_critical") is True and item.get("gap_status") != "cleared":
            errors.append(f"safety-critical competency {competency_id} is not cleared")
    for metric in pack.get("metrics", []):
        metric_id = metric.get("metric_id") if isinstance(metric, dict) else None
        if not _nonblank(metric_id):
            errors.append("metric requires metric_id")
            continue
        _known_evidence(metric.get("evidence_ids"), known, f"metric {metric_id}", errors)
        for field in ("definition", "source_system", "period_start", "period_end", "calculation", "second_reviewer", "reproduction_inputs_or_hash"):
            if not _nonblank(metric.get(field)):
                errors.append(f"metric {metric_id} requires {field}")


def validate(data: Any) -> list[str]:
    if not isinstance(data, dict):
        return ["fixture must be an object"]
    errors: list[str] = []
    if data.get("fixture_label") != "FICTIONAL TEST DATA":
        errors.append("fixture_label must be FICTIONAL TEST DATA")
    known = _validate_sources(data, errors)
    _validate_integration(data, known, errors)
    _validate_governance_budget(data, known, errors)
    _validate_hr(data, known, errors)
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_healthcare_evidence_packs.py <fixture.json>")
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        return 1
    errors = validate(data)
    print("PASS" if not errors else "FAIL")
    for error in errors:
        print(f"[ERROR] {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
