# AI-Agent Pricing Models Reference

Pattern library, worked examples, and contractual clauses for AI-agent pricing. Pairs with `ai-agent-pricing-and-packaging-proposal`.

## The Six Patterns at a Glance

| Pattern | Unit | Best for | Risk to agency | Mitigation |
|---|---|---|---|---|
| A — Per-Resolution | Resolved outcome | High-volume defined-outcome workflows | Intervention overshoot | Floor price; intervention credit |
| B — Per-Outcome | Business outcome | Workflows with clean outcome attribution | Attribution disputes | Outcome definition + cooling-off |
| C — Per-Step | Action / step | Buyers wanting visibility | Tool over-call | Step budget per task |
| D — Per-Agent | Agent persona / seat | Buyers thinking in FTE terms | Mismatch with usage | Included volume + overage |
| E — Hybrid | Base + usage | Enterprise predictability | Bill complexity | Statement + quarterly review |
| F — Success-Based | Outcome-linked bonus | Trust-building | Bonus shortfall | Base covers cost; cap on bonus |

## Pattern A — Per-Resolution

### Definition
- A resolution is a unit of work completed by the agent that **the human did not have to redo for N days**. Define N (commonly 7–30 days, sector-specific).
- The agent's action chain must be documented; partial attempts are not billable resolutions.

### Worked Example
- Customer-support resolution agent.
- Price: $0.85 per resolution; floor of $25,000 / month per tenant; intervention credit if intervention rate exceeds 15 % for the month.
- At 80,000 resolutions / month: $68,000 base.
- Tenant economics: baseline cost per ticket $4.50; agent at $0.85 with $3.65 saved per resolution; tenant approves the swap.

### Sample Clause
> The Agency shall charge $0.85 per Resolution where a Resolution is the closure of a Buyer ticket by the Agent without subsequent reopen or human re-work for thirty (30) calendar days. The Agency shall maintain a Resolution log auditable by the Buyer. If the Intervention Rate (defined as the percentage of attempted tasks requiring human correction, override, or completion) exceeds 15 % in any calendar month, the Buyer shall receive a credit equal to 1 % of monthly Resolution fees for every percentage point above 15 %, up to a maximum credit of 25 %.

## Pattern B — Per-Outcome

### Definition
- A business outcome attributable to the agent, with attribution rules and a cooling-off period before billing.

### Worked Example
- Debt-recovery agent in financial services.
- Price: 8 % of recovered value above baseline recovery rate, with a 30-day cooling-off (the debt stays recovered).
- Floor of $40,000 / month per tenant covers platform and oversight.

### Sample Clause
> The Agency shall be paid 8 % of Recovered Value above the agreed Baseline Recovery Rate, calculated thirty (30) calendar days after the recovery event, provided no Reversal has occurred. Attribution disputes shall be resolved by reference to the Action Audit Log and shall be raised within sixty (60) days of the recovery event.

## Pattern C — Per-Step

### Definition
- Per agent action — tool call, system write, message sent. Step budget per task to prevent over-call.

### Worked Example
- Operations agent — incident triage and runbook execution.
- Price: $0.04 per step with a step budget of 25 per incident; steps beyond budget billed at $0.02; anomaly alerting on more than 50 steps in an incident.

### Sample Clause
> The Agency shall charge $0.04 per Step (defined as a tool invocation, system write, or outbound communication initiated by the Agent). The Step Budget per Task shall be twenty-five (25); Steps within budget billed at the full rate, Steps above budget billed at $0.02. The Agency shall alert the Buyer if any single Task exceeds fifty (50) Steps and shall pause the Agent pending Buyer review.

## Pattern D — Per-Agent (Seat / Persona)

### Definition
- Agent persona priced as a unit — "1 Support Agent — 24x7 — up to N resolutions / month — premium model".
- Included throughput with overage rate.

### Worked Example
- Public-sector citizen-service agent.
- Price: $18,000 / month per "Citizen-Service Agent" — up to 30,000 cases routed and assembled; overage at $0.40 per case; sovereign-AI deployment available at a premium of 35 %.
- Buyer comparison: equivalent FTE cost (loaded, in market) approximately $24,000 / month for partial coverage — agent is on call 24x7.

### Sample Clause
> The Buyer shall pay $18,000 per calendar month per Citizen-Service Agent. Each Citizen-Service Agent includes up to thirty thousand (30,000) Cases per month, where a Case is a citizen request triaged and assembled to the Named Officer's review queue. Cases above thirty thousand (30,000) shall be billed at $0.40 per Case. The Agent shall not make Decisions on citizen status, benefit, or entitlement; Decisions are made by the Named Officer at the Buyer.

## Pattern E — Hybrid (Base + Usage)

### Definition
- Base fee covers platform, oversight queue, eval and red-team, plus a per-resolution / per-step rate above an included allowance.

### Worked Example
- Insurance claims triage agent for a mid-sized insurer.
- Base: $32,000 / month covers platform, eval, red-team, drift watch, kill-switch operations, supervisor retraining curriculum.
- Included: 5,000 triaged claims.
- Overage: $0.60 per claim above 5,000.

### Sample Clause
> The Buyer shall pay a Base Fee of $32,000 per calendar month covering Platform Operations, Eval and Red-Team, Drift Watch, Kill-Switch Drills, and Supervisor Retraining. The Base Fee includes up to five thousand (5,000) Triaged Claims per month. Triaged Claims above five thousand shall be billed at $0.60 per Claim. The monthly statement shall itemise base and overage.

## Pattern F — Success-Based (Outcome-Linked Bonus)

### Definition
- Base fee at a discounted rate plus a bonus on achieving an agreed outcome threshold (autonomy, intervention rate, deflection, customer-satisfaction).

### Worked Example
- Customer-support resolution agent (return engagement).
- Base: 70 % of standard per-resolution rate.
- Bonus: additional 15 % on resolutions in any month where intervention rate is at or below 10 % and CSAT is at or above 4.3 / 5.
- Bonus cap: 30 % above base in any quarter.

### Sample Clause
> The Buyer shall pay seventy per cent (70 %) of the Standard Resolution Rate as Base Fee. In any calendar month in which the Intervention Rate is at or below 10 % and the CSAT is at or above 4.3 / 5, the Buyer shall pay an Outcome Bonus of fifteen per cent (15 %) of the Standard Resolution Rate on Resolutions completed in that month. The aggregate Outcome Bonus shall not exceed thirty per cent (30 %) of Base Fees in any calendar quarter.

## Cross-Pattern Clauses

### Vendor Cost Pass-Through

> Where the unit cost of model inference, tool-call API access, or compute services charged to the Agency by a named Sub-Processor (the Sub-Processor list is set out in Annex X) increases by more than ten per cent (10 %) on a rolling twelve-month basis, the Agency may pass through the increase to the Buyer with sixty (60) days' notice, capped at the verified increase. The Agency shall maintain a margin floor and shall provide reasonable evidence of Sub-Processor price changes on request.

### Fair-Use

> The Agent shall operate within the Action Catalogue published in Annex Y. The Action Catalogue may be amended only by written change order. The Agent's daily Action volume per Tenant shall not exceed three (3) times the trailing thirty-day P95 daily Action volume; the Agency shall alert the Buyer and pause the relevant Tenant pending review where this threshold is breached.

### Abort and Refund

> The Buyer may exit with pro-rata refund of unused fees in any of: (a) an Irreversible-Action Incident determined to be at the Agency's fault; (b) Intervention Rate above the agreed ceiling for sixty (60) consecutive days; (c) Regulator Action against the Agentic System that the Agency cannot remedy within ninety (90) days.

### Autonomy Ramp

> The Pricing in this Schedule assumes the Autonomy Ramp set out in Annex Z. A Buyer-initiated request to accelerate the Autonomy Ramp shall trigger a re-price reflecting additional risk and additional oversight. A Buyer-initiated request to decelerate the Autonomy Ramp shall not reduce the Base Fee; the Agency shall continue to operate Oversight at the originally planned cadence.

### FX

> Model-Call and Tool-Call costs are denominated in United States Dollars. Where the Buyer's Fees are denominated in local currency, the exchange rate applicable for each invoice shall be the [Reference Rate] on the last business day of the month preceding the invoice month. Where the exchange rate moves by more than fifteen per cent (15 %) against the rate at the Effective Date over any rolling twelve-month period, either party may request a commercial review.

## Pattern Choice Decision Memo (Win-Room File)

1. Buyer's pricing instinct — what they said in discovery.
2. Buyer's tolerance for variable bills.
3. Agent Cost Stack and Cost per Outcome at P50 / P90 / P99.
4. Intervention rate target curve.
5. Reversibility classification per action class.
6. Competitive pricing reference points.
7. Recommended pattern with rationale.
8. Fallback pattern if buyer rejects.

## Africa-Context Notes

- Public-sector buyers prefer Pattern D (per-agent) — outcome pricing on citizen services is politically inappropriate.
- Financial-services buyers in regulated markets prefer Pattern E (hybrid) — predictable base plus a usage tail.
- SACCO / MFI buyers may need Pattern D scaled to small per-agent fees.
- FX clauses are essential when model costs are USD-denominated; the FX shock of 2022–2024 in several markets justified explicit clauses.
