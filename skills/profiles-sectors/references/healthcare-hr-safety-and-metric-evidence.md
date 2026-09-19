# Healthcare HR Safety, Conduct and Metric Evidence

Use this reference when a healthcare proposal must show how workforce conduct, competency, supervision, patient-safety evidence, and performance metrics will be controlled. It prepares an evidence request and proposal method. It does not determine employment law, clinical standards, disciplinary findings, or privacy compliance.

## Outcome and boundary

The proposal should make it possible for a second reviewer to determine:

1. whether a conduct case has an access-controlled evidence hold and a documented disposition;
2. whether a safety-critical role has the required competency and supervision evidence; and
3. whether a workforce or safety metric can be reproduced from a named source, period, definition, and calculation.

Protect people and records. Use a case ID or pseudonym in the proposal pack; do not copy personal health, disciplinary, or identifiable staff data into a narrative without an authorised basis.

## Required inputs

| Input | Minimum fields | If missing |
|---|---|---|
| Conduct case record | case ID, allegation, evidence hold, access scope, owner, staff response and disposition | A case cannot be described as closed. |
| Competency and supervision record | role, requirement source, staff or pseudonym ID, evidence, assessor, supervisor, review or expiry date | A safety-critical workflow is blocked or remains `NOT_ASSESSED`. |
| Metric definition and source | definition, numerator, denominator, exclusions, source, period, cohort, calculation and owner | Do not state a measured result. |
| Current HR, privacy and safety basis | jurisdiction, policy or standard version, source ID, dates, reviewer and review trigger | Route to the relevant current reviewer; mark the rule `NOT_ASSESSED`. |

## Conduct and safety case checklist

Record at least:

`case_id`, `case_type`, `reported_at`, `access_scope`, `evidence_hold_id`, `case_owner`, `investigator`, `staff_response`, `disposition`, `remediation_or_follow_up`, `reviewer`, `closed_at`, `status`, `rights_or_authority`, and `evidence_ids`.

The case status cannot be `closed` unless disposition, staff response, reviewer, closure date, and evidence-hold decision are present. A missing response may be recorded as `NOT_RECEIVED` only when the responsible reviewer has documented the permitted next step; it does not silently satisfy the closure gate.

Use separate access for the case owner, investigator, HR or safeguarding lead, and the proposal reviewer. The proposal should describe the role boundary and audit trail without exposing the underlying personal record.

## Competency and supervision gate

For each safety-critical role, record:

`role_id`, `competency_id`, `requirement_source_id`, `staff_pseudonym`, `evidence_ids`, `assessor`, `supervisor`, `supervision_frequency`, `valid_from`, `valid_to_or_review_date`, `gap_status`, and `reviewer`.

Missing, expired, disputed, or inaccessible competency evidence blocks the specified safety-critical workflow until the named owner resolves it. Training attendance alone does not prove competence unless the approved requirement says it does and the assessor records the basis.

## Metric evidence card

Record at least:

`metric_id`, `name`, `definition`, `purpose`, `numerator`, `denominator`, `exclusions`, `source_system`, `source_version_or_as_of`, `period_start`, `period_end`, `cohort`, `calculation`, `data_owner`, `first_reviewer`, `second_reviewer`, `reproduction_inputs_or_hash`, `limitations`, `support_status`, and `evidence_ids`.

The second reviewer must reproduce the calculation from the recorded inputs or an approved extract. If the source, period, definition, cohort, or calculation is unclear, the metric is `NOT_ASSESSED` and cannot support a target, safety claim, staffing decision, or performance conclusion.

## Acceptance and failure gates

| Finding | Result |
|---|---|
| Closed conduct case lacks disposition or staff response | Block closure and retain the evidence hold. |
| Closed conduct case lacks a named reviewer | Block closure. |
| Safety-critical competency or supervision evidence is missing | Block the specified workflow or mark it `NOT_ASSESSED`. |
| Metric has no source, period, definition, or reproducible calculation | Do not publish the result. |
| Second reviewer cannot reproduce the metric | Return to the data owner; no pass. |
| Proposal includes identifiable case or health data without authority | Remove, minimise, or stop the affected content. |

## Currentness and reviewer boundary

This reference makes `NO_TIME_SENSITIVE_CLAIMS`: it supplies a durable evidence pattern. Employment, privacy, safeguarding, occupational-health, patient-safety, and professional requirements vary by jurisdiction and version. Route each current rule to Digital Research and the applicable legal, HR, safeguarding, or clinical reviewer. Record source scope, publication or revision date, access date, verification date, freshness class, review date, support status, uncertainty, confidence, and owner. Missing evidence remains `NOT_ASSESSED`.

Required human review:

- HR or safeguarding lead: conduct case access, response, disposition and retention;
- clinical or patient-safety lead: competency, supervision and safety workflow;
- data or M&E reviewer: metric definition, source, calculation and reproduction; and
- privacy or legal reviewer where personal or regulated data is in scope.

The proposal engine may describe gates and request evidence. It cannot make a disciplinary finding, certify competence, release a patient-safety control, or certify a statutory position.

## Synthetic example

For a fixture only, `CASE-SYNTH-01` is a fictional closed case with a disposition, staff response, evidence hold decision and second review. Use pseudonyms and label all records `FICTIONAL TEST DATA`; a synthetic case is not HR or clinical evidence.

