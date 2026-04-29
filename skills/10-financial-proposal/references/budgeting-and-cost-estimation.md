# Budgeting and Cost Estimation Reference

This reference supports two closely related uses:
1. writing financial proposals with disciplined pricing logic
2. advising clients on budgeting, fiscal administration, and cost management

Synthesised from budgeting and fiscal-management sources already used in the repository, plus Proctor's *Building Financial Models with Microsoft Excel*.

---

## 1. Build the Model in Layers

Use a three-layer model structure:

- **Assumptions layer**: rates, quantities, tax rules, exchange assumptions, timing, and payment terms
- **Calculation layer**: fees, reimbursables, overheads, contingency, capex, and totals
- **Output layer**: proposal tables, dashboards, milestone schedules, and summary notes

This separation makes the budget easier to audit, revise, and defend.

### Assumptions Dashboard

For larger or more complex bids, maintain a compact assumptions dashboard covering:
- staffing assumptions
- travel assumptions
- tax and currency assumptions
- payment timing
- inflation or escalation where relevant
- scenario flags for best case, base case, and stress case

---

## 2. Budget Allocation Methodologies

### Zero-Based Budgeting

Every budget line starts at zero and must be justified from scratch.

Use when:
- the assignment is novel
- the client expects full transparency
- historical benchmarks are weak or misleading

### Incremental Budgeting

Start from historical cost patterns and adjust for known changes.

Use when:
- the assignment resembles prior work
- cost drivers are stable
- reliable internal benchmark data exists

### Hybrid Approach

Recommended default:
- use incremental logic for predictable recurring costs
- use zero-based logic for specialist tasks, workshops, travel bursts, or unusual deliverables

---

## 3. Master Budget Logic for Proposals

Even short consulting bids benefit from a simplified master budget structure.

### Operating Budget Components

- professional fees
- reimbursable field costs
- operating expenses linked to delivery
- overhead allocation where needed

### Financial Budget Components

- capital expenditure or equipment purchases, if allowed
- cash budget by milestone or month
- working-capital implications of payment lag

This prevents budgets that look balanced on paper but fail operationally during delivery.

---

## 4. Driver-Based Cost Build

Build the price from the actual delivery drivers:

| Driver | Typical Use |
|---|---|
| Expert days | Professional fee build-up |
| Number of workshops | Venue, travel, facilitation, materials |
| Number of field sites | Transport, accommodation, per diem |
| Reporting frequency | Editorial, QA, production effort |
| Deliverable count | Packaging and review effort |
| Duration | Overhead exposure and cash timing |

Avoid unexplained lump sums where driver-based build-up is possible.

---

## 5. Cost Classification Framework

| Type | Definition | Proposal Example |
|---|---|---|
| **Direct Cost** | Traceable to a specific deliverable | Consultant fees for a diagnostic phase |
| **Indirect Cost** | Supports delivery but not tied to one deliverable | PM overhead, back-office support |
| **Variable Cost** | Changes with workload or volume | Per diem for additional field visits |
| **Fixed Cost** | Does not change with activity in the short run | Software licence, mobilisation setup |
| **Semi-Variable Cost** | Contains fixed and variable elements | Communications, vehicle usage |
| **Marginal Cost** | Cost of one additional unit | Adding one extra workshop day |
| **Average Cost** | Total cost divided by units served | Cost per trainee or beneficiary |

This structure is useful when presenting optional scope or explaining why some budget lines are flexible and others are not.

---

## 6. Progressive Cost Estimation

### Level 1: Parametric / Unit-Based Estimate

Use rough cost-per-unit logic early:
- cost per beneficiary
- cost per district
- cost per workshop
- cost per field site

Always present a range, not a false single-point estimate.

### Level 2: Component Estimate

Estimate by phase or deliverable.

### Level 3: Activity-Based Estimate

Estimate by specific activity and role.

### Level 4: Unit Price Estimate

Use historical internal cost data, published ceilings, or supplier quotes.

### Level 5: Bottom-Up Work Specification

Use when requirements, quantities, and quality expectations are already stable.

For proposal work, combine methods rather than forcing one method across every line.

---

## 7. Pricing Build-Up and Sustainable Day Rates

Use a first-principles pricing structure:

```text
individual service cost
+ assignment overhead
+ general business overhead
+ risk allowance
+ profit margin
= net fee
+ VAT / applicable taxes
= gross fee
```

Rate justification should be available internally even if the client only sees a summary table.

---

## 8. PCTS Constraint and Time-Cost Trade-Off

Use the relationship `C = f(P, T, S)`:
- **P** = performance
- **T** = time
- **S** = scope
- **C** = cost

When budget pressure arises, adjust scope or schedule consciously rather than pretending all four constraints can remain fixed.

Compression below the practical optimum raises cost through overtime, coordination overhead, and rework.

---

## 9. Cash Budget and Payment Timing

A financially sound proposal should include a simple cash budget when milestone payments are stretched or the assignment is long.

### Cash Budget Questions

- when will mobilisation costs be incurred
- when will major travel or workshop costs hit
- when will invoices be submitted
- when is payment realistically expected
- can the firm carry the working-capital burden between milestones

For larger bids, map this monthly. For smaller bids, map it by milestone.

---

## 10. Contingency, Reserve, and Margin

Distinguish clearly between:

| Component | Purpose |
|---|---|
| **Work Budget** | Planned cost of defined work |
| **Management Reserve** | Cost of newly identified scope or change |
| **Margin** | Profit buffer and commercial return |

Do not use reserve to hide poor estimating.

### Risk-Adjusted Contingency

Calculate contingency from identified risks where visible contingency is allowed. If the procurement format discourages explicit contingency, protect the price through conservative assumptions and realistic quantities.

---

## 11. Sensitivity Analysis

Sensitivity analysis shows how much the output changes when one key assumption moves.

Test variables such as:
- total expert days
- travel volume
- average day rate
- VAT treatment
- exchange rate
- payment lag

Use this to identify the assumptions that deserve management attention and tighter review.

---

## 12. Scenario Analysis

Scenario analysis changes several assumptions together to test commercial resilience.

Typical scenarios:
- **Base case**: expected delivery conditions
- **Lean case**: reduced travel or lower volume
- **Stress case**: delayed approvals, more field days, weaker exchange rate

This is especially useful when deciding whether to present optional scope, alternative pricing packages, or a walk-away threshold.

---

## 13. Contribution Margin and Break-Even

### Contribution Margin

Contribution margin shows how much a work package contributes after variable cost is covered.

Use it when:
- comparing optional scope items
- deciding whether to accept reduced volume
- structuring add-ons or phased options

### Break-Even

Break-even analysis shows the volume or effort level at which revenue covers fixed and variable cost.

Use it to test whether a sharply discounted proposal is still commercially viable.

---

## 14. Ratios and Viability Checks

Use simple ratio checks where the bid is large enough to justify them:

| Check | Purpose |
|---|---|
| Fee share by seniority | Detect top-heavy or underpowered staffing |
| Reimbursables as % of total | Detect unusual travel or logistics exposure |
| Mobilisation cash coverage | Test whether first payment supports early delivery |
| Overhead as % of fees | Test whether the proposal carries enough support cost |
| Contribution margin % | Check sustainability of discounted offers |

These do not replace judgment, but they help catch distorted pricing structures before submission.

---

## 15. Life-Cycle and Long-Horizon Costing

For ICT, infrastructure, or service-platform assignments, move beyond the bid price and show life-cycle thinking:
- initial implementation
- licences and hosting
- maintenance and support
- training and change costs
- upgrade or decommissioning costs

This strengthens advisory credibility and discourages false economy.

---

## 16. Time Value of Money

Use present value and NPV logic for multi-year assignments, investment appraisals, or options analysis.

Decision rule:
- negative NPV signals a weak financial case for purely commercial decisions
- public-interest assignments may still proceed, but the rationale must be explicit

State the discount rate and why it is appropriate.

---

## 17. Forecasting and Volume Assumptions

When pricing depends on demand or volume assumptions, be explicit about the method:
- moving average for stable series
- weighted moving average where recent values matter more
- exponential smoothing for rolling updates
- regression only where data quality supports it

Weak forecasting assumptions are a common source of bid underpricing.

---

## 18. Cost Database Discipline

Maintain internal benchmarks from completed assignments:

```text
cost figure = invoiced sum / quantity delivered
```

Best practices:
- store values net of VAT
- record year and market
- keep notes on scope and exclusions
- distinguish between efficient delivery and distress delivery

This is one of the strongest ways to improve future proposal accuracy.

---

## 19. Common Proposal Uses

### When Writing a Budget Narrative

State:
- how the budget was built
- which assumptions drive the cost
- how risk and change will be handled
- why the payment schedule is workable

### When Preparing Optional Commercial Options

Use:
- contribution margin logic
- scenario analysis
- direct versus variable cost separation

### When Testing Bid Sustainability

Review:
- cash budget
- break-even point
- sensitivity to day counts, rates, and payment lag
- alignment between staffing schedule and commercial totals
