---
name: proposal-writing/10-financial-proposal
description: Write the financial proposal for a consulting bid. Use when the user asks to draft a financial proposal, budget, cost breakdown, fee schedule, or pricing for a consulting assignment.
---

# Financial Proposal

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
3. Use the guidance below to build defensible pricing logic tied to the actual delivery model.
4. Cross-check the financial content against the methodology, staffing, and timeline assumptions.
5. Verify compliance with envelope separation, form rules, and pricing assumptions before finalizing.

## Quality Standards
- Keep the pricing logic transparent, internally consistent, and format-compliant.
- Use clear professional language and avoid unsupported commercial claims.
- Prefer defensible assumptions, explicit cost drivers, and coherent structure.

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

The financial proposal is always a separate document — never included in the technical proposal envelope. It presents the total cost of the assignment, broken down by fees and reimbursable expenses, tied to a milestone payment schedule.

## What to Gather Before Writing

- The assignment scope and deliverables (from the ToR)
- Team members, their roles, day rates, and number of days per person
- Reimbursable items: travel, accommodation, printing, communications
- Currency to quote in (UGX, USD, KES, or as specified in the ToR)
- VAT treatment: whether to include or exclude, and the applicable rate
- Payment schedule preferences or any milestones specified in the ToR
- Any rate ceilings published by the client or donor

## Structure

### Financial Proposal Submission Sheet
```
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

Typical splits: 20/30/30/20 for most assignments. For longer multi-phase projects, use more milestones at smaller percentages.

### Assumptions and Exclusions
State clearly what is not included in the price and what the client is expected to provide:

- Client will provide workspace and internet connectivity for on-site work
- Travel costs for client staff attending training are not included
- Third-party software licence costs are not included unless specified
- The quoted price assumes the assignment commences within [30] days of contract signing

## Day Rate Reference Ranges (East African Market, 2025–2026)

| Level | USD/day | UGX/day (approx.) |
|---|---|---|
| Senior Partner / Director | $800–1,500 | UGX 3M–5.5M |
| Senior Consultant / Project Manager | $400–800 | UGX 1.5M–3M |
| Consultant / Analyst | $150–400 | UGX 550K–1.5M |
| Junior Consultant | $80–150 | UGX 300K–550K |
| Technical Specialist (Developer) | $200–600 | UGX 750K–2.2M |

International (non-local) consultant rates are typically 1.5 to 3 times local rates. World Bank and donor-funded projects may publish rate ceilings — check the ToR.

## Budget Construction Methodology

State the estimation methodology used: "Our budget is constructed using a hybrid approach — recurring operational costs are estimated from comparable recent assignments in our cost database, while specialist and activity-specific costs are built from first principles."

### The PCTS Constraint (Lewis)

Cost is a function of Performance, Time, and Scope: `C = f(P, T, S)`. You can fix three constraints; the fourth must be whatever the relationship dictates. When clients challenge the price, respond by adjusting scope or timeline, not by compressing costs below sustainable levels.

### Risk-Adjusted Contingency

Calculate contingency using the square-root-sum-of-squares method rather than a flat percentage:

```
Risk Budget = √(C₁² + C₂² + C₃² + ...)
```

Where C = individual risk cost (effect × probability). This produces a statistically reasonable contingency that can be justified to evaluators. Typically 5-10% of professional fees.

### Buffer Scheduling

Identify cost modules that can be delivered at reduced specification if risks materialise. Present these as a structured contingency plan in the assumptions section — it demonstrates fiscal discipline and gives the client flexibility.

## Rules

- Never quote below a sustainable rate — low pricing signals low quality and creates delivery risk
- State currency explicitly on every table — ambiguity between UGX and USD can disqualify a bid
- Warrant the delivered system or reports for a minimum of three months after final acceptance
- Seal the financial proposal separately — in PPDA and World Bank format, the financial proposal is never in the same envelope as the technical proposal
- Always present life cycle costs for ICT or infrastructure assignments — a 5-year TCO table alongside the project budget demonstrates strategic thinking
- For multi-year assignments, include NPV analysis with a stated discount rate and rationale
- Categorise costs explicitly (direct/indirect, fixed/variable) in the budget narrative

## Reference Library

| Reference File | Contents |
|---|---|
| `references/budgeting-and-cost-estimation.md` | Budget allocation methodologies (ZBB, incremental, hybrid), 5-level progressive cost estimation, PCTS constraints, cost contingency and management reserve, contractor pricing build-up, risk-adjusted budgeting (√ formula), life cycle costs, financial ratio analysis (12+ ratios), fiscal conservatism, TVM (PV/FV/NPV), forecasting methods, budget alignment, variance analysis, 6-stage costing gates, cost databases, wants vs needs prioritisation, "cut back not out" principle |
| `../consulting-frameworks/references/financial-analysis.md` | Expected value, cannibalisation, breakeven, profitability decomposition, market sizing, pricing toolkit, pocket pricing model, CLV, experience curve |
| `../references/world-class-proposal-patterns.md` | Budget proposal architecture (Chereau & Meschi), Sweet Spot positioning |

Read the budgeting reference file when constructing project budgets that need detailed cost estimation frameworks, contingency calculations, or when the assignment involves advising clients on budgeting and fiscal management.
