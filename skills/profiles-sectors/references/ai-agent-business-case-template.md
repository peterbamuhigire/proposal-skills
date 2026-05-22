# AI-Agent Business Case Template

Reusable template, formulas, and worked examples for the AI-agent business case. Pairs with `ai-agent-business-case-and-roi`.

## Core Formula Set

### Tasks-per-FTE-Saved with Intervention Discount

       FTE saved = (tasks_attempted × (1 − intervention_rate)) / annual_FTE_task_capacity

where:
- `tasks_attempted` is the share of total volume routed to the agent (rarely 100 %; pick a sustainable share based on the action catalogue scope).
- `intervention_rate` is the share of attempted tasks that the human supervisor had to step in on (correction, override, completion).
- `annual_FTE_task_capacity` is the loaded annual task throughput of one human FTE in the same workflow.

### Cost per Outcome

       cost_per_outcome = (model_calls_per_task × model_call_price)
                        + (oversight_cost_per_task)
                        + (eval_and_redteam_cost_amortised_per_task)
                        + (engineering_amortised_per_task)
                        + (compute_and_vector_store_per_task)

Compare against baseline. Watch the model-calls-per-task line; agents fan out, often 10–100 calls per task.

### Three Scenarios Keyed to Autonomy Ramp

| Scenario | Autonomy at month 6 | Intervention rate | Volume | Irreversible incidents | Model price |
|---|---|---|---|---|---|
| Downside | L2 | 35 % | Plan − 20 % | 1 minor | +30 % |
| Base | L3 | 12 % | Plan | 0 | 0 |
| Upside | L3+ | 6 % | Plan + 20 % | 0 | −10 % |

### Payback

       payback_months = total_engagement_cost / monthly_net_savings

`monthly_net_savings` already subtracts agent operating cost (models, oversight, eval, drift, compute) and does not assume month-1 intervention rate for month-12.

### NPV with Sensitivity

- Discount rate: buyer's stated rate.
- Sensitivity dimensions: model-call price (±30 %), intervention rate (±10 pp), volume (±20 %), autonomy-ramp slip (delay base case by 1, 3, 6 months).

## Worked Example — Customer Support Resolution Agent

Buyer: regional bank's customer-support operations.

Inputs:
- Volume: 100,000 tickets / month
- Baseline cost per ticket (loaded): $4.50
- Baseline AHT: 12 minutes; FTE task capacity: 8,000 / month
- Baseline FTE: 12.5
- Agent attempts 80 % of volume; 20 % routed straight to human (sensitive, complex)
- Model calls per task at P95: 18
- Model call price: $0.012
- Oversight cost (queue staffing): $0.45 per attempted task at month 1, falling to $0.15 by month 6
- Eval + red-team + drift: $0.05 per task amortised
- Engineering amortised over 36 months: $0.08 per task
- Compute + vector store: $0.02 per task
- Pilot intervention rate: 25 % at month 1; target 10 % at month 6

Tasks-per-FTE Saved:
- Month 1: 80,000 × (1 − 0.25) / 8,000 = **7.5 FTE saved**
- Month 6: 80,000 × (1 − 0.10) / 8,000 = **9.0 FTE saved**

Cost per Outcome at Month 6:
- Model calls: 18 × $0.012 = $0.216
- Oversight: $0.15
- Eval + red-team: $0.05
- Engineering: $0.08
- Compute: $0.02
- Total: **$0.516 per attempted task**

Net Saving per Attempted Task at Month 6:
- Baseline $4.50 − agent cost $0.516 − residual human handling on intervention (0.10 × $4.50 = $0.45) = **$3.53 per task**
- Monthly: 80,000 × $3.53 = **$282,400**

Payback:
- Engagement cost (design + build + pilot): $1.6 M
- Payback: $1.6 M / $282 K = ~5.7 months from month 6 (effective ~9 months from start)

Three Scenarios (illustrative monthly savings at month 12):

| Scenario | Intervention | Volume | Monthly net savings |
|---|---|---|---|
| Downside | 25 % | 80,000 | $190K |
| Base | 10 % | 100,000 | $353K |
| Upside | 6 % | 120,000 | $447K |

Downside scenarios:
- Irreversible-action incident (wrong refund authorised, public statement issued in error): sized at $50K legal + $200K reputational worst case.
- Regulator action: pause for conformity assessment costs four weeks of agent operation and consultant fees.
- Intervention overshoots: supervisor headcount above plan adds $80K / month.
- Scope creep: action catalogue grows; engineering and ops absorb cost; net savings reduced by 15 %.

## Worked Example — Insurance Claims Triage Agent

Buyer: mid-sized insurer.

Inputs:
- Volume: 8,000 claims / month
- Baseline cost per triaged claim (loaded): $22
- Agent triages and assembles; humans decide payout / declinature
- Agent attempts 90 % of volume
- Model calls per task at P95: 25 (includes document parsing across multi-page claims)
- Model call price: $0.012
- Oversight: $1.10 per task at month 1; $0.40 at month 6
- Pilot intervention rate: 30 % at month 1; target 12 % at month 6
- Irreversible-action risk: declinature wrongly accelerated → conduct-of-business complaint; cost $20K average per incident

Tasks-per-FTE Saved (FTE capacity 1,000 triaged claims / month):
- Month 6: 7,200 × (1 − 0.12) / 1,000 = **6.3 FTE saved**

Cost per Outcome (month 6): $0.30 + $0.40 + $0.10 + $0.12 = **$0.92 per task**

Net Saving per Task: $22 − $0.92 − (0.12 × $22) = **$18.44 per task**, monthly $132K

Downside:
- Conduct-of-business complaint cluster — three incidents in a quarter sized at $60K plus regulator engagement.
- Adverse fairness finding — pause and re-train, $300K.

## Worked Example — Financial-Services Reconciliation Agent

Buyer: payments processor.

Inputs:
- Volume: 50,000 reconciliation cases / month
- Baseline cost: $1.80 per case (loaded)
- Agent assembles reconciliation; finance ops confirms; the agent never posts to ledger autonomously (L1 on ledger writes)
- Model calls per task at P95: 8
- Net saving target: 60 %

This example pairs with a per-agent pricing pattern (Pattern D) — the buyer pays for a defined "reconciliation agent" with included throughput, plus overage. The CFO compares the per-agent fee to the FTE equivalent.

## FX Handling

Where revenue is in local currency (KES, NGN, UGX, RWF, ZAR) and model costs are USD-denominated:
- State the FX assumption in the case.
- Use a six-month or twelve-month rolling average for forward planning.
- Include an FX clause in the contract (`ai-agent-pricing-models-reference.md`).
- Sensitivity: ±15 % FX move tested in the downside.

## Africa-Context Notes

- Local FTE costs are lower than US/EU benchmarks; the payback maths shifts.
- Sovereign-AI options add cost in the cost stack but unlock public-sector and bank tenants.
- Mobile-money workflows (M-Pesa, MTN MoMo, Airtel Money) are a common reconciliation use case and reward replay-deterministic agents with full audit.
- Volume from CBA-style consolidation across SACCOs or MFIs can dwarf baseline assumptions.

## CFO One-Pager Shape

1. Outcome owned by the agent (one line).
2. Baseline cost per outcome and monthly volume.
3. Tasks-per-FTE saved at month 1 and month 6 (curve).
4. Cost per outcome at month 6 with the cost stack.
5. Three-scenario monthly savings.
6. Payback in months.
7. Downside scenarios summarised with mitigation.
8. The ask: engagement cost and pricing pattern.

## Board / Investment-Committee Shape

Add to the CFO one-pager:
- NPV over 36 months with sensitivity table.
- Capacity unlock — work the buyer can now do without hiring.
- Strategic value — competitive position, customer experience, regulator stance.
- Optionality — what other agents become viable once the platform exists.
