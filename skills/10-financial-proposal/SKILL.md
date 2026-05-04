---
name: proposal-writing-10-financial-proposal
description: Write the financial proposal for a consulting bid. Use when the user asks to draft a financial proposal, budget, cost breakdown, fee schedule, or pricing for a consulting assignment.
---

# Financial Proposal
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

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

## Workflow
1. Read the commercial instructions and identify the required pricing structure, forms, and constraints.
2. Load any relevant procurement framework before drafting or structuring the response.
3. Build the budget from delivery drivers: scope, team, level of effort, timing, travel, and approvals.
4. Test the price for internal consistency against the methodology, staffing plan, and timeline.
5. Stress-test the price with basic cash-flow, scenario, and sustainability checks before finalising.
6. Verify compliance with envelope separation, form rules, and pricing assumptions.

## Quality Standards
- Keep the pricing logic transparent, internally consistent, and format-compliant.
- Use clear professional language and avoid unsupported commercial claims.
- Prefer defensible assumptions, explicit cost drivers, and coherent structure.
- Show that the price is workable operationally, not merely arithmetically.

## Anti-Patterns
- Do not price work that the technical proposal does not actually support.
- Do not ignore donor or client form requirements, currency rules, or tax assumptions.
- Do not mix financial content into the technical proposal where separation is required.

## Outputs
- A financial proposal narrative or pricing structure aligned to the bid instructions.

## References
- `../sectors/SKILL.md` for procurement routing.
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
- For website design, redesign, SEO-ready website, ecommerce, landing page, portal, or web frontend assignments, run `../website-design-proposal-strategy/SKILL.md` before final pricing. Price discovery, UX, content, SEO, design system, development, CMS, integrations, QA, launch, hosting/licences, training, handover, support, and post-launch optimisation explicitly.
- For accounting, bookkeeping, ERP finance, POS/accounting integration, finance dashboards, Excel model, or management-accounting assignments, price discovery of source documents, chart-of-accounts review, reconciliation sampling, control walkthroughs, data cleanup, model audit, configuration review, and validation workshops explicitly.
- For finance transformation, accounting cleanup, ERP/POS finance, grant finance, revenue assurance, cost-control, financial-modelling, or management-accounting proposals, run `../accounting-finance-advisory/SKILL.md` before final pricing so scope, methodology, deliverables, risks, and level of effort agree.
- For premium-client, executive, enterprise, luxury/affluent, high-ticket, or strategic transformation proposals, run `../premium-client-proposal-strategy/SKILL.md` before final pricing so fees reflect value, risk, seniority, proof, governance, and service quality rather than low-cost positioning.
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
| `../premium-client-proposal-strategy/references/premium-proposal-gate.md` | Executive, enterprise, affluent, high-ticket, and premium proposal positioning, methodology, proof, and commercial discipline |
| `../website-design-proposal-strategy/references/website-design-proposal-gate.md` | Website philosophy, UX/content/SEO methodology, stack explanation, deliverables, costing drivers, acceptance criteria, launch, handover, and red flags |
| `../references/world-class-proposal-patterns.md` | Proposal architecture and commercial positioning patterns |
| `../consulting-frameworks/references/industrial-operations-diagnostics.md` | Cost drivers for industrial diagnostics, including site work, data cleansing, material-flow mapping, scheduling analysis, warehouse review, and sustainability measurement |

Read the budgeting reference when constructing budgets that need stronger modelling logic, scenario testing, or financial viability checks.

