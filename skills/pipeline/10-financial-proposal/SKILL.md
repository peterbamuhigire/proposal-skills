---
name: 10-financial-proposal
description: Use when drafting a bid budget, fee schedule, reimbursables, payment schedule, price form, or commercial assumptions. Unlike accounting-finance-advisory, this skill prices the proposed delivery and preserves any required technical-financial envelope separation.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Financial Proposal
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill to draft or revise the financial proposal narrative, pricing logic, or cost structure.
- Load it when the bid requires a separate commercial response or financial forms.

## Do Not Use When
- The task is unrelated to pricing, costing, or financial proposal content.
- The user only needs supporting domain knowledge rather than the financial response.

## Required Inputs
- The financial-proposal instructions, forms, and commercial assumptions.
- The methodology, work plan, and staffing assumptions that drive the pricing logic.
- Any taxes, reimbursables, validity, and currency rules that apply.

| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Official price form, currency/tax rules, technical scope, work plan, person-days, rates, costs, and approvals | Tender pack and authorised commercial model | required | Stop final pricing and issue a cost/input reconciliation request. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Read the commercial instructions and identify the required pricing structure, forms, and constraints.
2. Load any relevant procurement framework before drafting or structuring the response.
3. Build the budget from delivery drivers: scope, team, level of effort, timing, travel, and approvals.
4. Add premium value, support, maintenance, technical risk, service design, and total-cost-of-ownership drivers where relevant.
5. Test the price for internal consistency against the methodology, staffing plan, and timeline.
6. Stress-test the price with basic cash-flow, scenario, and sustainability checks before finalising.
7. Verify compliance with envelope separation, form rules, and pricing assumptions.

## Quality Standards
- Keep the pricing logic transparent, internally consistent, and format-compliant.
- Use clear professional language and avoid unsupported commercial claims.
- Prefer defensible assumptions, explicit cost drivers, and coherent structure.
- Show that the price is workable operationally, not merely arithmetically.

## Anti-Patterns
- Releasing the section with an unresolved mandatory input. Fix: block release and name the evidence owner.
- Hiding a contradiction with another proposal section. Fix: reconcile the source sections before drafting resumes.
- Treating an unavailable check as passed. Fix: mark it not assessed and return a qualified draft.
- Do not price work that the technical proposal does not actually support.
- Do not ignore donor or client form requirements, currency rules, or tax assumptions.
- Do not mix financial content into the technical proposal where separation is required.
- Do not invent tax treatment or rates. Fix: route to external finance doctrine and verify current authoritative sources.
- Do not force the target total by hiding effort or margin. Fix: show driver changes and obtain an authorised scope/price decision.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Completed financial proposal and assumption schedule | Evaluator, bid lead, finance approver | Arithmetic, forms, scope, days, rates, taxes, currency, cash flow, envelope, and approvals reconcile. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Price reconciliation and finance-doctrine gate | Checked workbook/register | Totals recalculate, technical scope is fully costed, and tax/accounting assumptions show source and reviewer status. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Review is read-only by default. Editing requires commercial authority; changing rates, margins, tax, discounts, payment terms, or submitting the price requires the named approver. Do not certify tax treatment.

## Degraded Mode
Without price forms, verified costs, finance doctrine, spreadsheet execution, or tax evidence, return a driver-based model structure and unassessed checks. Never present unchecked arithmetic or tax as final.

## Decision Rules
| Condition | Action | Risk avoided |
|---|---|---|
| Technical and financial envelopes are separate | Block all price content from technical files | Rejection |
| Tax or accounting treatment is load-bearing | Apply external finance doctrine and current source review | Incorrect statutory price |
| Price fails cash-flow or margin floor | Re-scope, rephase, or seek approval | Unworkable bid |

## Worked Example
For a donor bid, reconcile expert days to the work plan, separate reimbursables, apply the verified tax basis, test payment timing against delivery costs, and scan the technical archive for price leakage.

## AI Commercial Structure Block

When the engagement contains AI features, the financial proposal includes an AI commercial structure block: cost-of-tokens calculation (tokens-in × price + tokens-out × price + embedding cost + ancillary, per call, scaled to projected production volume); AI-tier credits (included allowance per tier + overage rate); fair-use clause (per-tenant call ceiling, abuse trigger, commercial conversation language); FX clause where revenue is local and model costs are USD; price-increase clause indexed to CPI + 3 pp or model-provider list-price index plus a margin floor. Worked examples at P50 / P90 / P99 tenant volume confirm margin under heavy-user economics. See `../ai-on-saas-pricing-and-packaging-proposal/SKILL.md`, `../references/ai-on-saas-pricing-models-reference.md`, and `../references/ai-on-saas-business-case-template.md` for the formulas, clauses, and worked examples.

## AI-Agent Commercial Structure Block

When the engagement delivers AI agents (autonomous LLM systems that act on the buyer's behalf), the financial proposal carries an agent-specific structure: choice of pricing pattern from the six agent patterns (per-resolution / per-outcome / per-step / per-agent / hybrid / success-based); explicit definitions of "resolution / outcome / step / agent"; **intervention credit clause** (buyer receives a credit if intervention rate exceeds the agreed ceiling); **vendor cost pass-through** (agents fan out 10–100 model calls per task — a model-price increase invisible in a copilot can be catastrophic in an agent) with index, cap, and margin floor; fair-use specific to agents (per-tenant action ceiling, anomalous-action trigger, scope-creep change-order trigger); **abort and refund clause** (irreversible-action incident at agency fault; intervention rate beyond ceiling for 60 consecutive days; regulator action); **autonomy ramp clause** (faster ramp triggers re-price); FX clause; supervisor retraining curriculum costed in.

The agent commercial structure is delivered as **drop-in exhibits** in the financial proposal annexes — Pricing Exhibit, SLA Exhibit, Credit and Refund Exhibit, MSA Addendum, Abandonment-and-Refund Policy, Dispute Resolution and Audit Rights Annex, Vendor Cost Pass-Through, Renewal and True-Up Clauses, Outcome-Pricing Clauses (where applicable). The exhibits reference the same numbers, same definitions, and same evidence trail. Assembly is orchestrated by `../ai-agent-contract-language-pack/SKILL.md`.

See:
- [../ai-agent-pricing-and-packaging-proposal/SKILL.md](../../ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md) — six patterns and packaging.
- [../ai-agent-sla-and-credit-schedule/SKILL.md](../../ai-agent-commercial/ai-agent-sla-and-credit-schedule/SKILL.md) — SLA class and credit schedule.
- [../ai-agent-commercial-packaging/SKILL.md](../../ai-agent-commercial/ai-agent-commercial-packaging/SKILL.md) — packaging shape (Included / Add-on / Standalone).
- [../ai-agent-success-fee-and-outcome-pricing/SKILL.md](../../ai-agent-commercial/ai-agent-success-fee-and-outcome-pricing/SKILL.md) — outcome and success-fee structures.
- [../ai-agent-intervention-credit-and-abort-refund/SKILL.md](../../ai-agent-commercial/ai-agent-intervention-credit-and-abort-refund/SKILL.md) — intervention-credit and abort-refund.
- [../ai-agent-msa-and-sla-addendum-templates/SKILL.md](../../ai-agent-commercial/ai-agent-msa-and-sla-addendum-templates/SKILL.md) — MSA / SLA addendum.
- [../ai-agent-renewal-and-true-up/SKILL.md](../../ai-agent-commercial/ai-agent-renewal-and-true-up/SKILL.md) — renewal and true-up.
- [../ai-agent-contract-language-pack/SKILL.md](../../ai-agent-commercial/ai-agent-contract-language-pack/SKILL.md) — exhibit assembly.
- [../references/ai-agent-pricing-models-reference.md](../../profiles-sectors/references/ai-agent-pricing-models-reference.md) — pattern library.
- [../references/ai-agent-pricing-exhibit-template.md](../../profiles-sectors/references/ai-agent-pricing-exhibit-template.md) — drop-in pricing exhibit.
- [../references/ai-agent-sla-exhibit-template.md](../../profiles-sectors/references/ai-agent-sla-exhibit-template.md) — drop-in SLA exhibit.
- [../references/ai-agent-credit-and-refund-clauses.md](../../profiles-sectors/references/ai-agent-credit-and-refund-clauses.md) — credit and refund clauses.
- [../references/ai-agent-msa-addendum-template.md](../../profiles-sectors/references/ai-agent-msa-addendum-template.md) — MSA addendum.
- [../references/ai-agent-business-case-template.md](../../profiles-sectors/references/ai-agent-business-case-template.md) — business case inputs.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- [../sectors/SKILL.md](../../profiles-sectors/sectors/SKILL.md) for procurement routing.
- [../premium-pricing-and-value-defense/SKILL.md](../../strategy-positioning/premium-pricing-and-value-defense/SKILL.md) for premium fee logic, options, and value defence.
- [../sales-discovery-and-objection-handling/SKILL.md](../../strategy-positioning/sales-discovery-and-objection-handling/SKILL.md) for price, risk, timeline, staffing, technology, and local-context objections.
- [../customer-service-and-maintenance-proposals/SKILL.md](../../strategy-positioning/customer-service-and-maintenance-proposals/SKILL.md) for support, maintenance, SLA, and post-launch optimisation pricing.
- [../references/technical-strategy-credibility-checklist.md](../../profiles-sectors/references/technical-strategy-credibility-checklist.md) for SaaS, AI, software, cloud, API, operations, and maintainability cost drivers.
- [../references/ai-on-saas-pricing-models-reference.md](../../profiles-sectors/references/ai-on-saas-pricing-models-reference.md) for AI pricing patterns, fair-use, price-increase, and FX clauses.
- [../references/ai-on-saas-business-case-template.md](../../profiles-sectors/references/ai-on-saas-business-case-template.md) for cost-of-tokens and three-scenario AI ROI.
- [../ai-on-saas-pricing-and-packaging-proposal/SKILL.md](../../ai-on-saas-proposals/ai-on-saas-pricing-and-packaging-proposal/SKILL.md) for the companion pricing skill.
- [../references/ai-agent-pricing-models-reference.md](../../profiles-sectors/references/ai-agent-pricing-models-reference.md) for the six agent pricing patterns, intervention credit, vendor cost pass-through, abort-and-refund, and autonomy-ramp clauses.
- [../references/ai-agent-business-case-template.md](../../profiles-sectors/references/ai-agent-business-case-template.md) for tasks-per-FTE with intervention discount and three-scenario agent ROI.
- [../ai-agent-pricing-and-packaging-proposal/SKILL.md](../../ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md) for the companion agent pricing skill.
- Root and local `references/` files for budgeting, estimation, and commercial framing.
- Relevant proposal sections so pricing remains consistent with delivery assumptions.

The financial proposal is a separate commercial document. It presents the total cost of the assignment, broken down by fees and reimbursable expenses, tied to milestones and payment logic. Strong pricing shows not only what the work costs, but why the cost structure is credible and sustainable.

## What to Gather Before Writing

- The assignment scope and deliverables from the ToR
- Team members, their roles, day rates, and number of days per person
- Reimbursable items such as travel, accommodation, printing, and communications
- Currency to quote in
- VAT treatment and any withholding assumptions
- Payment schedule preferences or mandatory milestones
- Any published rate ceilings or eligible-cost rules
- Internal assumptions on mobilisation, review cycles, and payment lag

## Pricing Model Structure

Build the financial response using three linked layers:

1. **Assumptions layer** — scope drivers, rates, tax rules, travel assumptions, exchange assumptions, and payment terms.
2. **Calculation layer** — fees, reimbursables, overhead allocation, contingency, and totals.
3. **Output layer** — compliant submission sheets, summary tables, milestone payments, and any narrative assumptions.

This separation makes it easier to check logic, revise assumptions, and defend the price during internal review.

## Structure

### Financial Proposal Submission Sheet

```text
FINANCIAL PROPOSAL SUBMISSION SHEET

Total Bid Price: [CURRENCY] [AMOUNT] ([AMOUNT IN WORDS])

[State whether VAT is included or excluded and at what rate]

Authorised By:

Signature: ___________________  Name: [NAME]
Position:  [TITLE]             Date:  [DATE]

For and on behalf of: [FIRM NAME]
```

### Summary of Bid Price

| Component | Amount |
|---|---|
| Professional Fees | [Amount] |
| Reimbursable Expenses | [Amount] |
| Subtotal | [Amount] |
| VAT ([X]%) | [Amount] |
| **Total Bid Price** | **[Amount]** |

### Breakdown of Professional Fees

| Expert | Role | Day Rate | Days | Total |
|---|---|---|---|---|
| [Name] | [Role] | [Rate] | [N] | [Total] |
| **Total Fees** | | | | **[Total]** |

### Breakdown of Reimbursables

| Item | Unit | Quantity | Unit Cost | Total |
|---|---|---|---|---|
| Local transport | Trip | [N] | [Cost] | [Total] |
| Accommodation / Per diem | Night | [N] | [Cost] | [Total] |
| Printing and reproduction | Lump sum | 1 | [Cost] | [Total] |
| Communications | Month | [N] | [Cost] | [Total] |
| **Total Reimbursables** | | | | **[Total]** |

### Payment Schedule

Tie every payment to a deliverable, not a calendar date.

| Payment | Milestone / Deliverable | % | Amount |
|---|---|---|---|
| 1 | Contract signing / Mobilisation | 20% | [Amount] |
| 2 | [Deliverable name] | 30% | [Amount] |
| 3 | [Deliverable name] | 30% | [Amount] |
| 4 | Final report accepted / Project closure | 20% | [Amount] |

### Assumptions and Exclusions

State clearly what is not included in the price and what the client is expected to provide:

- workspace and internet connectivity for on-site work where relevant
- client-side participation costs such as venue or staff travel if excluded
- third-party software licence costs unless explicitly included
- pricing validity period
- payment timing assumptions if these materially affect mobilisation or cash flow

## Day Rate Reference Ranges

Use local market evidence and published ceilings where available. If the client or donor publishes allowable rates, those take precedence over generic market ranges.

## Budget Construction Methodology

State the estimation methodology used. A strong default is:
"Our budget is constructed using a hybrid approach: recurring operational costs are estimated from comparable recent assignments, while specialist and activity-specific costs are built from first principles using the staffing plan and work breakdown."

### Driver-Based Build

Tie costs to the actual delivery model:
- work package or phase
- level of effort
- expertise level
- travel volume
- workshop count
- reporting frequency

Avoid unexplained lump sums unless the form requires them.

### The PCTS Constraint

Cost is a function of performance, time, and scope: `C = f(P, T, S)`.

When clients challenge the price, respond by adjusting scope, sequencing, or timeline rather than compressing costs below sustainable levels.

### Risk-Adjusted Contingency

Where contingency is allowed, calculate it from identified risks rather than adding an arbitrary markup. If the bid rules discourage visible contingency lines, absorb the logic into conservative assumptions and documented pricing buffers.

### Cash-Flow Sufficiency Check

Before finalising, test whether mobilisation and delivery costs can be financed between payment milestones. A technically correct price can still be commercially weak if the payment schedule creates an avoidable cash squeeze.

### Scenario and Sensitivity Check

Run simple tests on the most sensitive assumptions:
- expert days
- travel frequency
- exchange rate
- approval delay
- tax treatment

Use this to identify which assumptions materially affect margin or cash position.

### Contribution Margin and Break-Even Check

Separate fixed and variable cost logic where possible:
- use contribution margin to understand how much each additional work package or deliverable contributes after variable cost
- check the break-even level for effort-intensive assignments

This is useful when presenting optional scope, alternative commercial options, or negotiations around reduced budgets.

## Rules

- Never quote below a sustainable rate.
- State currency explicitly on every table.
- Keep the financial proposal separate from the technical proposal where required.
- For ICT or infrastructure assignments, include life-cycle or total-cost-of-ownership logic when relevant.
- For website design, redesign, SEO-ready website, ecommerce, landing page, portal, or web frontend assignments, run [../website-design-proposal-strategy/SKILL.md](../../strategy-positioning/website-design-proposal-strategy/SKILL.md) before final pricing. Price discovery, UX, content, SEO, design system, development, CMS, integrations, QA, launch, hosting/licences, training, handover, support, and post-launch optimisation explicitly.
- For software, SaaS, AI, website, or digital-service assignments, price operations explicitly: monitoring, backups, updates, incident response, model/prompt evaluation, usage review, analytics review, documentation, handover, support channels, and optimisation backlog.
- For SaaS implementation engagements specifically, price these workstreams as named lines, not bundled inside implementation: control plane (onboarding, identity, billing, observability, cost attribution); application plane build and integration; trust and compliance hardening; customer success engagement (tier-appropriate intensity); lifecycle communications (per program); change management and adoption; ongoing managed service or retainer. Reference [../saas-pricing-and-packaging-proposal/SKILL.md](../../saas-proposals/saas-pricing-and-packaging-proposal/SKILL.md) for client-owned SaaS commercial model design when in scope.
- For resale SaaS bids (where the client owns the SaaS revenue model), include the tier-ladder design, expansion path, freemium / paid-trial decision, and price-increase clause. Reference [../references/saas-pricing-models-reference.md](../../profiles-sectors/references/saas-pricing-models-reference.md).
- Use Professional Services Attach Rate (PSAR) framing to defend the implementation fee against the subscription cost. Reference [../references/saas-metrics-glossary-for-proposals.md](../../profiles-sectors/references/saas-metrics-glossary-for-proposals.md).
- Tie payment milestones to SaaS-relevant value events where possible: contract signature, security review cleared, tenant model decision, first end-to-end integration, UAT entry, pilot go-live, full cutover, 60-day adoption review, first QBR. Reference [../references/saas-mutual-action-plan-template.md](../../profiles-sectors/references/saas-mutual-action-plan-template.md).
- For service design or customer-experience assignments, price research, touchpoint inventory, journey mapping, blueprinting, co-creation, prototyping, frontline validation, implementation planning, training, and measurement separately.
- For accounting, bookkeeping, ERP finance, POS/accounting integration, finance dashboards, Excel model, or management-accounting assignments, price discovery of source documents, chart-of-accounts review, reconciliation sampling, control walkthroughs, data cleanup, model audit, configuration review, and validation workshops explicitly.
- For proposals that include project financial management, donor/grant finance, budget governance, audit evidence, tax/statutory handling, or financial reporting, price finance-management effort explicitly: financial controls setup, report preparation, reconciliations, advance liquidation, audit-file maintenance, finance review meetings, tax verification, and close-out reporting.
- For embedded accounting-engine builds, price posting-rule workshops, accountant validation, chart-of-accounts templates, mapping configuration, opening-balance migration, inventory/payroll/fixed-asset/tax posting tests, reconciliation gates, report testing, parallel run, and first-close support as separate workstreams.
- For finance transformation, accounting cleanup, ERP/POS finance, grant finance, revenue assurance, cost-control, financial-modelling, or management-accounting proposals, run [../accounting-finance-advisory/SKILL.md](../../domain-delivery/accounting-finance-advisory/SKILL.md) before final pricing so scope, methodology, deliverables, risks, and level of effort agree.
- For premium-client, executive, enterprise, luxury/affluent, high-ticket, or strategic transformation proposals, run [../premium-client-proposal-strategy/SKILL.md](../../strategy-positioning/premium-client-proposal-strategy/SKILL.md) before final pricing so fees reflect value, risk, seniority, proof, governance, and service quality rather than low-cost positioning.
- For manufacturing, warehousing, logistics, ERP/MES/WMS/TMS, and industrial operations assignments, price site visits, data extraction, stock sampling, process observation, layout mapping, validation workshops, and specialist modelling effort explicitly.
- For multi-year assignments, include NPV or cash-flow logic where the commercial form allows it.
- Categorise costs clearly as direct, indirect, fixed, variable, or reimbursable where that adds clarity.

## Reference Library

| Reference File | Contents |
|---|---|
| `references/budgeting-and-cost-estimation.md` | Budget methodologies, driver-based modelling, master budget logic, cash budget, capex, sensitivity analysis, contribution margin, break-even, ratios, contingency, forecasting, and cost database practices |
| `../consulting-frameworks/references/financial-analysis.md` | Expected value, breakeven, profitability decomposition, market sizing, pricing toolkit, and related commercial logic |
| `../consulting-frameworks/references/accounting-finance-systems-diagnostics.md` | Accounting/bookkeeping diagnostics, ERP finance controls, reconciliations, management accounting, source-document review, Excel model audit, and finance-system deliverables |
| `../accounting-finance-advisory/references/accounting-finance-proposal-gate.md` | Proposal workstreams, deliverables, pricing drivers, acceptance criteria, and red flags for accounting, ERP finance, financial-modelling, controls, and finance-transformation assignments |
| `../accounting-finance-advisory/references/world-class-finance-accounting-section.md` | Finance/accounting section template, project financial management, donor/grant finance, fiduciary controls, audit evidence, caveats, and acceptance criteria |
| `../premium-client-proposal-strategy/references/premium-proposal-gate.md` | Executive, enterprise, affluent, high-ticket, and premium proposal positioning, methodology, proof, and commercial discipline |
| `../references/premium-rate-justification-framework.md` | Premium value stack, proof ladder, commercial options, discount rules, and price defence |
| `../references/proposal-objection-handling.md` | Ethical objection handling for price, risk, timeline, staffing, technology, AI, local context, support, and procurement |
| `../references/website-software-maintenance-support-language.md` | Support categories, SLA language, client responsibilities, and maintenance pricing notes |
| `../website-design-proposal-strategy/references/website-design-proposal-gate.md` | Website philosophy, UX/content/SEO methodology, stack explanation, deliverables, costing drivers, acceptance criteria, launch, handover, and red flags |
| `../references/world-class-proposal-patterns.md` | Proposal architecture and commercial positioning patterns |
| `../consulting-frameworks/references/industrial-operations-diagnostics.md` | Cost drivers for industrial diagnostics, including site work, data cleansing, material-flow mapping, scheduling analysis, warehouse review, and sustainability measurement |

Read the budgeting reference when constructing budgets that need stronger modelling logic, scenario testing, or financial viability checks.

