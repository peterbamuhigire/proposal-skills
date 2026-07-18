---
name: accounting-finance-advisory
description: Use when a proposal covers accounting, finance operations, controls, ERP or POS finance, grants, tax, audit readiness, modelling, or financial transformation. Route pure bid pricing to 10-financial-proposal; this skill governs finance doctrine and delivery credibility.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Accounting Finance Advisory
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- A proposal includes finance-system design, accounting cleanup, ERP/POS implementation, bookkeeping improvement, financial modelling, budget review, revenue assurance, cost controls, grant finance, or management reporting.
- The bid requires credible financial methodology, staffing, deliverables, evidence, or pricing.
- The client is a CEO, board, investor, donor, public entity, school, healthcare provider, SME, manufacturer, retailer, or project owner with money-control risk.
- The proposal must show how assignment funds, project accounts, budgets, advances, reimbursements, taxes, procurement, audit evidence, donor reporting, or client financial data will be handled.
- The proposal has a finance/accounting section, financial management section, project budget management section, grant-management section, audit/readiness section, or fiduciary-risk section.

## Do Not Use When

- The task only prices a bid; use [../../pipeline/10-financial-proposal/SKILL.md](../../pipeline/10-financial-proposal/SKILL.md).
- The task requests an audit opinion, tax filing, statutory certification, valuation, or legal conclusion without the authorised professional and evidence.

## Required Inputs

| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Finance scope, entities, periods, systems, transactions, and reporting needs | ToR and client finance owner | required | Stop detailed design and issue a finance evidence request. |
| Applicable accounting framework, tax jurisdiction, donor rules, and source records | Canonical finance doctrine and authoritative current sources | required for compliance claims | Mark treatment unresolved and route for doctrine review. |

## Canonical Finance Doctrine Route

For every finance-triggered task, resolve and read the external `chwezi-accounting-doctrine` engine from the global routing table: `README.md`, `doctrine/accounting-finance-doctrine.md`, the matched `skills/**/SKILL.md`, and `governance/finance-accounting-quality-gate.md`. For any software with a finance element, also run its `finance-module-audit` skill. Record the gate result in the deliverable evidence; this local skill never replaces doctrine.

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.

1. Diagnose the financial problem: record quality, source documents, systems, controls, reconciliations, tax, reporting, budgeting, and decision usefulness.
2. Define workstreams: current-state review, transaction walkthroughs, data extraction, chart-of-accounts review, reconciliation sampling, controls testing, model audit, dashboard design, implementation roadmap.
3. Specify accounting depth: financial accounting, management accounting, cost accounting, IFRS/local GAAP, tax, grant accounting, consolidation, or valuation as relevant.
4. Tie methodology to evidence: document samples, ledger exports, bank/mobile money statements, inventory records, payroll, tax returns, contracts, reports, user roles, and system screenshots.
5. Define outputs: diagnostic report, controls matrix, finance process map, chart of accounts, posting rules, reconciliation pack, management accounts, financial model, dashboard spec, training, and SOPs.
6. Price the work from drivers: source-system complexity, transaction volume, sample size, number of entities/branches, data cleanup, workshops, onsite visits, validation cycles, and reporting forms.
7. If the proposal must describe project/assignment financial management, write a dedicated finance-accounting section covering budget governance, funds flow, approval controls, procurement/payment controls, accounting basis, source-document evidence, bank/mobile-money handling, tax treatment, reporting cadence, audit file, and close-out.
8. Add caveats where law or standards require professional sign-off: statutory audit, tax filing, fair value, impairment, deferred tax, donor-specific eligibility rulings, or legal interpretation.

## Quality Standards

- The proposal shows how money will be traced from source document to report.
- Deliverables are specific enough to price and manage.
- Controls and reconciliations are treated as core scope, not optional garnish.
- Financial modelling distinguishes assumptions, calculations, outputs, and checks.
- The technical proposal and financial proposal agree on scope, level of effort, and validation.
- The finance/accounting section is specific enough that a CFO, donor finance officer, accountant, auditor, or procurement evaluator can see how money will be authorised, recorded, reconciled, reported, and evidenced.
- The proposal separates bookkeeping execution, management accounting, statutory/tax compliance, audit support, and professional judgement instead of collapsing them into vague "financial management".

## Anti-Patterns

- Treating “financial management” as one vague workstream. Fix: separate records, controls, reporting, tax, audit support, and judgement.
- Proposing postings without source-to-ledger rules. Fix: define evidence, recognition, accounts, dimensions, reversals, and reconciliation.
- Quoting tax or statutory rules from memory. Fix: verify the dated source register and reviewer status.
- Calling a balanced spreadsheet reconciled. Fix: reconcile independent source, subledger, control account, and exception evidence.
- Promising audit, tax, valuation, or IFRS sign-off. Fix: state the authorised-professional boundary and review dependency.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Finance methodology, scope, deliverables, controls, assumptions, and acceptance schedule | Evaluator, CFO/controller, delivery team | Traces each material money flow from source evidence through authorisation, posting, reconciliation, reporting, and review. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Finance doctrine gate and transaction-to-report trace | Completed gate plus control matrix | Names doctrine skill used, unassessed items, reviewer boundary, and evidence for each material flow. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.

Default to read-only review. Editing proposals requires authority; posting, filing, paying, changing masters, opening periods, certifying compliance, or issuing an opinion requires explicit client authority and the responsible finance professional.

## Degraded Mode

When ledgers, source records, systems, doctrine, current statutory sources, or reviewer access are unavailable or missing, return the narrowest qualified diagnostic and evidence gaps. Mark reconciliation, compliance, and audit procedures not assessed.

## Decision Rules

| Condition | Action | Risk avoided |
|---|---|---|
| Money flow or accounting treatment is in scope | Load matched external doctrine skill and quality gate | Local invention of accounting rules |
| Current tax or statutory fact is load-bearing | Verify dated authoritative source and reviewer status | Stale compliance claim |
| Evidence is insufficient for assurance | Qualify conclusion and require professional review | Unauthorised certification |

## Worked Example

For a retailer's POS-to-ledger proposal, trace cash, card, mobile money, VAT, inventory, refunds, and settlements through control accounts and reconciliations; route treatment to the retail/POS doctrine pack and keep tax filing and audit sign-off outside the consultant's unverified promise.

## Output Checks

- Does the methodology cover AR, AP, cash/bank, inventory, payroll, tax, fixed assets, loans, grants, revenue, expenses, journals, close, and reports where relevant?
- Are IFRS/local GAAP and tax assumptions explicit enough for the assignment?
- Are management accounting needs covered: cost centers, project costs, branch P&L, budgets, variance, contribution margin, and KPIs?
- Are high-risk controls covered: supplier changes, refunds, write-offs, stock adjustments, payroll changes, manual journals, and period reopening?
- Are acceptance criteria defined for reconciliation, reporting accuracy, training completion, and handover?
- If the proposal manages project funds, does it cover budget lines, approval thresholds, segregation of duties, supporting documents, bank/mobile-money controls, tax withholding, reporting cadence, audit trail, and close-out?
- If donor/grant funds are involved, does it cover fund restrictions, eligible/ineligible costs, budget reallocations, exchange-rate treatment, advance liquidation, procurement evidence, and donor financial reporting?
- If the proposal makes accounting or compliance claims, are caveats included for statutory audit, tax filing sign-off, and complex accounting judgement?

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.

- [references/accounting-finance-proposal-gate.md](references/accounting-finance-proposal-gate.md) - detailed methodology, deliverables, scope/pricing drivers, and red flags.
- [references/world-class-finance-accounting-section.md](references/world-class-finance-accounting-section.md) - reusable finance/accounting section templates, quality gate, and caveat language.
- [../consulting-frameworks/references/accounting-finance-systems-diagnostics.md](../consulting-frameworks/references/accounting-finance-systems-diagnostics.md) - existing diagnostic reference.
- [../10-financial-proposal/SKILL.md](../../pipeline/10-financial-proposal/SKILL.md) - pricing and commercial structure.
