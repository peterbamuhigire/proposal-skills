---
name: embedded-accounting-engine-proposal
description: Use when proposing embedded bookkeeping or accounting functionality inside a SaaS, ERP, POS, sector system, or marketplace; route accounting doctrine and finance-module audit to the canonical finance engine.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Embedded Accounting Engine Proposal
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The proposal includes bookkeeping, financial reporting, finance automation, ERP/POS finance, inventory accounting, payroll accounting, tax/VAT, donor/fund accounting, bank/mobile-money reconciliation, or statutory reports.
- The client wants to avoid separate QuickBooks, Xero, Sage, Pastel, Tally, Zoho Books, Wave, or similar subscriptions for routine books.
- A SaaS build must credibly claim audit-ready financial statements from inside the operating system.

## Do Not Use When

- The engagement is only accounting cleanup or advisory with no software build; use `accounting-finance-advisory`.
- The proposal cannot include accountant validation, posting-rule testing, reconciliation, and first-close support; do not claim automated accounting without those controls.
- The client needs statutory audit, tax filing sign-off, impairment, fair value, deferred tax, or other professional judgement; include caveats and specialist roles.

## Core Positioning

Use client-facing language:

> The system will not treat accounting as a separate module to be reconciled later. Every approved business event will post through a single embedded accounting engine into one controlled ledger. This means sales, stock, payments, payroll, grants, and assets produce audit-ready books from the same operational data the teams use every day.

Verifiable claim:

> For routine bookkeeping and statutory/management reporting of the operating entity, the system is designed to replace separate QuickBooks/Sage/Pastel/Tally-class accounting subscriptions. Statutory audit, tax filing sign-off, and complex accounting judgements remain subject to applicable law and professional review.

## Proposal Sections To Include

1. Why embedded accounting engine.
2. Single-ledger architecture.
3. Financial and operational reports delivered out of the box.
4. Implementation methodology and gates.
5. Accounting validation and reconciliation approach.
6. Caveats and professional judgement boundaries.
7. Team roles and client-side finance owner.
8. Acceptance criteria.

## Deliverables Block

- Chart of accounts template and tenant-specific mapping register.
- Posting-rule matrix for sales, purchases, payments, payroll, inventory, assets, tax, grants, and reversals.
- Embedded `LedgerPostingService` and append-only journal design.
- Financial reports: trial balance, general ledger, income statement, statement of financial position, cash flow statement, statement of changes in equity/net assets.
- Operational reports: AR ageing, AP ageing, inventory valuation, COGS, stock movement, payroll liabilities, VAT/tax schedules, bank/mobile-money reconciliation, fixed asset register, donor/fund reports where relevant.
- Migration pack: opening balances, customer/supplier balances, stock values, fixed assets, unpaid payroll/tax liabilities.
- Reconciliation and first-close support pack.

## Acceptance Criteria

- Every posted journal balances.
- No module writes directly to the ledger tables.
- Reports regenerate from journal lines.
- AR/AP/inventory/fixed assets/payroll/tax control accounts reconcile to subledgers.
- Locked periods reject new postings.
- Duplicate business events do not double-post.
- Posting rules pass accountant-reviewed test scenarios.

## Do Not Use When

- Do not use this skill when a neighbouring specialist named in the description owns the primary decision; route there first and use this skill only as a supporting layer.
- Do not use it to invent buyer facts, evidence, legal positions, statutory rules, delivery capacity, or current external claims.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| finance scope, transactions, statutory context, integrations, controls, and canonical finance-engine findings | Buyer, ToR, approved project record, accountable owner, or verified evidence source | Yes | Stop the affected decision, name the missing source, and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| embedded-accounting proposal scope and acceptance pack | Finance owner, evaluator, and implementation team | Claims trace to supplied evidence; assumptions, owners, exclusions, decisions, and observable acceptance tests are explicit. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Decision and source trace for the output | Reviewer and release owner | Each load-bearing choice identifies its source, rationale, accountable owner, and any unassessed check. |

## Capability Contract

Default to read-only for analysis, critique, discovery, and review. Minimum capability is access to the supplied artefacts and permission to inspect or calculate relevant evidence. Edit only the requested working copy. Do not publish, send, spend, change production systems, certify compliance, make a statutory claim, or approve a commercial concession without explicit authority.

## Degraded Mode

If required files, interviews, finance doctrine, search evidence, calculation tools, network access, or specialist review are unavailable, return the narrowest useful qualified result. Mark unavailable checks as not assessed, separate facts from assumptions, and state what is needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Propose, qualify, or exclude a finance capability | Route doctrine to the finance engine and align the proposal with its finance-module audit findings. | Invented accounting treatment or unsafe ledger replacement. |
| Evidence conflicts or authority is absent | Stop the affected recommendation, record the conflict, and seek the named owner’s decision. | Invented facts or unauthorised commitments. |
| Evidence and approval are complete | Proceed within scope and retain the decision trace. | Irreproducible approval or scope drift. |

## Workflow

1. Confirm the consumer, decision, neighbouring-skill route, authority, and required inputs; stop if the primary route or accountable owner is unknown.
2. Inspect supplied evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a load-bearing contradiction.
3. Apply the domain method and decision rules, preserving the repository’s proposal voice and specialist constraints.
4. Draft the contracted output with observable acceptance conditions and an evidence trace.
5. Review alignment with scope, work plan, team, pricing, risk, and dependent proposal sections; recover by revising the affected choice and rerunning the check.
6. Run the critical-analysis and anti-slop gates; block release on unsupported claims, failed safety or finance gates, or an F slop grade.

## Quality Standards

- Every load-bearing claim is verified or explicitly qualified, and the output distinguishes fact, assumption, recommendation, and commitment.
- Scope, method, work plan, staffing, pricing, risks, dependencies, and acceptance conditions remain mutually consistent.
- The output preserves domain constraints, names accountable owners, covers failure paths, and blocks unsupported or unauthorised promises.
- British English and the repository’s East African professional tone are used unless the buyer requires another standard.
- The critical-analysis and anti-slop gates pass before release, with no unassessed check represented as passed.

## Anti-Patterns

- Inventing a buyer fact or proof point. Fix: cite the supplied source or mark the statement as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and name the evidence needed to resume.
- Copying a neighbouring skill’s method without routing. Fix: use the specialist for the primary decision and retain only the supporting layer here.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: state an observable measure, evidence record, and decision owner.
- Adding premium or technical claims without delivery capacity. Fix: reconcile the claim with named people, time, budget, dependencies, and authority.

## Worked Example

A retail POS replacement includes stock, VAT, mobile money, and refunds. Load the finance doctrine and audit, then scope posting rules, reconciliation, migration, controls, and acceptance evidence without promising unsupported statutory compliance.

<!-- dual-compat-end -->

## References

- [accounting-engine-positioning](references/accounting-engine-positioning.md)
- [accounting-caveats-and-claims](references/accounting-caveats-and-claims.md)
