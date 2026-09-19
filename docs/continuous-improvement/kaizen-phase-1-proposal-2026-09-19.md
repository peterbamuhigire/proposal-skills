# Proposal Engine Phase 1 Kaizen Record - 19 September 2026

## Scope decision

This bounded implementation covers B24-A02, B32-A03, and B25-A03 in proposal-skills. The engine owns proposal evidence mapping, procurement questions, evaluator-facing acceptance gates, and handoff boundaries. It does not own production integration controls, accounting doctrine, HR case management, clinical governance, or statutory certification.

B08-A03 is deferred. The action card assigns its proposed canonical reference to SRS and the accounting/control engine, and this repository has no denial/compliance-review route that would make a proposal-local implementation coherent. A future proposal route may link the receiving-engine contract after that owner publishes it.

## Baseline and root cause

The existing SaaS procurement route asked for tenant isolation, subprocessors, audit and exit evidence, but did not give a compact health-specific question set with negative cases and source-state semantics. The general risk route did not make governance authority, budget basis, conduct closure, competency evidence, or metric reproduction machine-checkable. This left an evaluator-facing evidence gap and made `NOT_ASSESSED` handling dependent on prose.

## Experiment

Hypothesis: one shared, synthetic evidence contract plus three focused references will reduce unsupported health-sector assurances while giving a second reviewer observable failure paths.

Changed surfaces:

- `skills/profiles-sectors/references/health-it-integration-and-tenant-evidence.md`
- `skills/profiles-sectors/references/healthcare-governance-budget-decision-pack.md`
- `skills/profiles-sectors/references/healthcare-hr-safety-and-metric-evidence.md`
- `scripts/validate_healthcare_evidence_packs.py`
- `tests/fixtures/healthcare-evidence-packs.json`
- `tests/test_healthcare_evidence_packs.py`
- SaaS procurement routing, `README.md`, and this record

The fixture is synthetic and labelled `FICTIONAL TEST DATA`. It contains no client, vendor, patient, employee, price, legal, or standards claim.

## Contract and acceptance evidence

The validator requires:

- tenant cases for wrong-tenant read/write, duplicate events, and interrupted transfer, with expected and observed outcomes aligned;
- evidence IDs with source scope, version, dates, freshness class, support state, reviewer and uncertainty;
- approved governance options with a named authority, evidence and review date;
- material budget lines with basis, period, source and reviewer, while rejecting textbook or generic-benchmark bases;
- closed conduct cases with disposition, staff response, evidence-hold decision, reviewer and closure date;
- cleared safety-critical competency records; and
- metrics with source, period, calculation, second reviewer and reproducible input reference.

## Currentness and human review

Preflight result: `NO_TIME_SENSITIVE_CLAIMS` in the new references and fixture. The references deliberately do not assert a current FHIR/PACS version, law, procurement rule, privacy requirement, accounting treatment, HR rule, clinical standard, vendor feature, or security certification. Such claims must be routed to Digital Research and the relevant sibling engine, with source scope, publication or revision date, access date, verification date, freshness class, review date, support state, uncertainty, confidence, owner, and reviewer. Missing evidence remains `NOT_ASSESSED`.

Human reviewers remain required: security/architecture for integration; privacy/legal for data and contract scope; finance for budget basis and reporting treatment; HR/safeguarding for conduct; clinical/patient-safety for competency; and data/M&E for metric reproduction. The proposal engine cannot approve, certify, submit, or alter source records.

## Rollback and next review

The change is reversible by removing the new reference links and validator fixture; it does not change production systems or source records. If a validator false-pass is found, retain the prior route, mark the affected state `NOT_ASSESSED`, fix the smallest contract, and rerun the focused tests.

Re-audit date: 19 October 2026. Owner: proposal-engine maintainer. Required next evidence: one independently reconciled, approved proposal fragment using a real buyer evidence register, with currentness and domain reviewers named before any release claim.

## Validation record

Commands and results are recorded in the handoff:

- `python -X utf8 scripts/validate_healthcare_evidence_packs.py tests/fixtures/healthcare-evidence-packs.json` - PASS.
- `python -m pytest -q tests/test_healthcare_evidence_packs.py` - 8 passed.
- Full native and cross-engine checks remain to be run after documentation links are integrated; see the final task handoff for `NOT_ASSESSED` items.

