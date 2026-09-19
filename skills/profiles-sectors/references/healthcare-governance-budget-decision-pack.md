# Healthcare Governance and Budget Decision Pack

Use this reference when a healthcare proposal must show who decides, what evidence supports the choice, how the budget follows the service model, and how approvals and changes are retained. It is a proposal evidence contract. It is not an accounting opinion, a statutory approval, or a substitute for the finance engine's current doctrine.

## Outcome and boundary

The evaluator should be able to trace:

`service need -> option -> decision authority -> evidence -> staffing and cash requirement -> risk and milestone effect -> approval or deferral`.

Separate an option recommendation from an approval. A proposal may recommend an option when its evidence and assumptions are visible; only the named authority may approve it.

## Required inputs

| Input | Minimum fields | If missing |
|---|---|---|
| Decision brief | problem, options, criteria, affected service, decision date | Return a decision gap; do not fill in a preferred option. |
| Authority map | decision right, named role or body, delegation, conflict declaration | An option cannot be marked approved. |
| Evidence register | source ID, scope, version, dates, support state, owner and reviewer | Mark the option or budget line `NOT_ASSESSED`. |
| Service and delivery model | outputs, staffing, milestones, dependencies, risks and client inputs | Stop the affected cost or feasibility claim. |
| Reporting basis | currency, unit, period, cash or accrual basis where relevant, and current finance guidance | Route to the finance reviewer and keep the calculation provisional. |

## Decision record

Record at least:

`decision_id`, `decision_question`, `options`, `criteria`, `recommended_option`, `decision_right`, `authority`, `conflict_status`, `evidence_ids`, `assumptions`, `risks`, `status`, `approval_reference`, `changed_at`, `change_reason`, `review_trigger`, `reviewer`, and `support_status`.

Allowed statuses are `proposed`, `approved`, `rejected`, `deferred`, and `NOT_ASSESSED`. An `approved` status requires a named authority, a non-empty evidence list, a review date, and an approval record. If the authority or evidence is absent, the status remains `proposed`, `deferred`, or `NOT_ASSESSED`.

## Budget evidence map

Every material budget line should contain:

`line_id`, `service_or_deliverable`, `staffing_or_driver`, `quantity`, `unit`, `rate_or_basis`, `basis_source_id`, `period`, `currency`, `cash_or_accrual_basis`, `dependency`, `risk_link`, `milestone_link`, `assumption`, `reviewer`, `evidence_ids`, and `status`.

Use a named basis: approved client data, measured driver, supplier quotation, approved assumption, or an explicit scenario. A textbook, book extract, generic benchmark, or unverified remembered figure is not a current budget basis. If the only basis is a book-derived concept, classify the line `NOT_ASSESSED` until a current, scope-matched source or approved assumption exists.

The budget map must link material lines to all applicable dimensions:

- service and deliverable: what the spend enables;
- staffing: role, effort, availability, and competency;
- cash: timing, payment dependency, and working-capital effect;
- risk: exposure, treatment, and contingency owner; and
- milestone: gate, acceptance evidence, and timing.

## Failure gates

| Finding | Result |
|---|---|
| Option has no decision authority | Cannot pass; retain as proposed or `NOT_ASSESSED`. |
| Option has no source evidence or explicit assumption | Cannot pass; identify the evidence owner. |
| Material line lacks basis, period, or reviewer | Budget evidence is incomplete. |
| A book or generic figure is used as the current budget basis | Quarantine the line and re-source it. |
| Price, staffing, milestones, or risks disagree | Stop the affected commercial claim and reconcile the delivery story. |
| Approval is changed | Retain old and new values, authority, reason, timestamp, and re-review trigger. |

## Independent acceptance oracle

The independent oracle is a finance reviewer who did not originate the line or option recommendation. The reviewer checks the source, period, unit, arithmetic, basis, cash timing, linkage to service and staffing, risk treatment, and approval state. A proposal writer may assemble the pack but may not approve a budget, certify value for money, or alter an immutable client financial record.

## Currentness and reviewer boundary

This reference makes `NO_TIME_SENSITIVE_CLAIMS`: it defines a trace structure and review questions. Currency rules, reporting bases, tax treatments, donor conditions, procurement thresholds, and accounting conclusions require the current finance/accounting engine and the controlling solicitation. Record publication or revision date, access date, verification date, freshness class, review date, support status, uncertainty, confidence, and owner for each current claim. Missing finance evidence is `NOT_ASSESSED`.

Required human review:

- service or clinical operations owner: service need, outputs, milestones and dependencies;
- finance reviewer: basis, period, arithmetic, cash and reporting treatment; and
- authorised governance body: decision right, approval, conflict disposition and material changes.

## Synthetic example

For a fixture only, a line may use `basis_type: measured_driver`, cite `SRC-SYNTH-BUDGET-01`, carry period `2026-Q4`, and remain subject to finance review. Label it `FICTIONAL TEST DATA`; it is not a price recommendation or approved budget.

