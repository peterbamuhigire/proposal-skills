---
name: ai-agent-business-case-and-roi
description: Use when the AI-agent proposal must present an ROI that survives a sceptical CFO and a sceptical head of operations. Provides task-based ROI (tasks-per-FTE-saved with intervention discount; AHT reduction with quality cap; deflection rate; time-to-resolution), agent cost stack (model calls per task × tasks; oversight cost; eval and red-team; integration and ops), three-scenario model accounting for autonomy-level, downside scenarios (regulator action, irreversible-incident cost, intervention overhead, scope-creep cost), and payback with autonomy ramp. Extends `ai-on-saas-business-case-and-roi` with the agent overlay; replaces it when the engagement is stand-alone agentic.
---

# AI-Agent Business Case and ROI
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The proposal must justify the price of an agent or a multi-agent system to a CFO, head of operations, or investment committee.
- The buyer has been promised "AI does the work" and the CFO now wants the numbers.
- The pricing rests on per-resolution, per-outcome, per-step, or success-based commercials and the case must show that the model can pay for itself at the proposed rate.
- The buyer's CFO will challenge: intervention overhead, irreversibility cost, scope-creep cost, model-call cost per task, supervisor cost, escalation cost, and the cost of being wrong.

## Do Not Use When

- The case is for a non-agent AI feature (use `ai-on-saas-business-case-and-roi`).
- The case is for generic AI strategy with no measurable outcome workflow (use `ai-transformation-proposal`).

## Required Inputs

- Baseline cost per outcome today (cost per resolved ticket, per triaged claim, per reconciled batch, per drafted document).
- Volume per month per tenant.
- Headcount cost (loaded), ramp curve, attrition.
- Average handling time (AHT) and time-to-resolution baseline, with P50 / P95 distribution.
- Model-call cost per task at the candidate provider(s) — agents make many calls per task, not one.
- Target autonomy level by quarter, and the **intervention rate** at each level.
- Supervisor cost (oversight queue staffing, on-call, escalation engineer).
- Eval, red-team, drift-watch cost.
- Insurance / liability cost differential for agentic actions.
- Buyer regulator exposure (downside).
- FX assumptions (USD model costs, local revenue).

## Workflow

1. Build the **Agent Value Stack** for each agent or use case: cost per outcome saved (volume × baseline cost − agent cost), AHT reduction monetised, deflection-rate monetised (work that never reached a human), time-to-resolution monetised (revenue cycle effect or SLA-breach avoidance), capacity unlock (volume the buyer can now handle without hiring), revenue from agent-tier upsell where the agent is a product feature.
2. Build the **Agent Cost Stack**: model calls per task × tasks per month (this is the biggest line and the most overlooked), embedding cost, tool-call cost (search, third-party API), oversight cost (supervisor headcount or on-call), eval cost (golden set + LLM-as-judge + human review), red-team cost, drift-watch cost, engineering cost, integration cost, vendor liability / insurance differential, cloud compute, vector store / memory.
3. Compute **Tasks-per-FTE-Saved with Intervention Discount**:

       FTE saved = (tasks completed by agent × (1 − intervention rate)) / (FTE annual task capacity)

   Intervention rate must come from the pilot, not from the brochure. An agent with 60 % autonomy at go-live saves less than half what a 90 % autonomy agent saves — and supervisor cost rises with intervention rate.

4. Compute **Cost per Outcome at three intervention rates** (P50 / P90 / P99 pessimistic), so the proposal is honest about the curve as autonomy improves over time.
5. Compute **Three Scenarios** by autonomy ramp (downside, base, upside):
   - Downside — autonomy ramp stalls; intervention rate stays high; one minor irreversible incident; one model-price increase.
   - Base — autonomy ramp tracks the pilot; intervention rate falls month over month within plan; zero irreversible incidents.
   - Upside — autonomy ramp accelerates; intervention rate halves at month six; volume expansion across tenants.
6. Compute **Payback in months**, accounting for model-call cost per task, supervisor cost, and the autonomy ramp. Payback that ignores model-call cost is fiction.
7. Compute **NPV** over 36 months with the buyer's discount rate and sensitivity on (a) model-call price (±30 %), (b) intervention rate (±10 percentage points), (c) volume (±20 %).
8. Write the **Downside Scenarios**:
   - (a) **Irreversible-action incident** — one wrong agent action sized at the buyer's worst-case (refund, fine, public statement, lost customer). Mitigation links to L1 / L2 gating and Responsible-AI commitment.
   - (b) **Regulator action on agentic system** — pause, conformity assessment, ban in market. Mitigation links to compliance and procurement.
   - (c) **Intervention overhead overshoots** — supervisor headcount exceeds plan; net savings collapse. Mitigation links to eval and prompt regression cadence.
   - (d) **Scope-creep cost** — buyer adds use cases without adding pricing; engineering and ops drown. Mitigation links to the action catalogue gate and change-control clause.
   - (e) **Model-price shock** — provider raises prices or restricts use. Mitigation links to model-gateway and fallback.
   - (f) **Adoption stall** — staff resist; volume routed to agent stays low; payback delays. Mitigation links to change management.
   - (g) **Liability event** — a court / regulator / contract holds the buyer or agency liable. Mitigation links to insurance, contract, audit log.
   - (h) **Service-credit cost** — credits issued under the SLA Class credit schedule and intervention-credit clause reduce realised revenue. Model the worst-credit-month at P90 / P99 intervention, P90 / P99 task-success miss, and a kill-switch breach. Stress-test margin floor against the aggregate credit cap. See `../ai-agent-sla-and-credit-schedule/SKILL.md` and `../ai-agent-intervention-credit-and-abort-refund/SKILL.md`.
   - (i) **Refund-trigger event** — model the engagement-level loss if an Abort-and-Refund trigger fires (Irreversible-Action Incident at agency fault; intervention overshoot for 60 consecutive days; regulator action). The contingency reserve should cover at least the worst single-trigger refund scenario.
9. Output the **Agent Business Case Memo** in the buyer's shape (CFO one-pager, board memo, investment-committee deck).

## The Tasks-per-FTE-Saved Formula (worked illustration)

Assume:
- Volume: 100,000 tickets / month
- Baseline AHT: 12 minutes; FTE handles 8,000 / month
- Baseline FTE need: 12.5
- Pilot intervention rate: 25 % at month 1; target 10 % at month 6
- Tickets the agent attempts: 80 % of volume = 80,000

At month 1:
- Agent-completed (no intervention) = 80,000 × (1 − 0.25) = 60,000
- FTE saved = 60,000 / 8,000 = **7.5 FTE**

At month 6:
- Agent-completed = 80,000 × (1 − 0.10) = 72,000
- FTE saved = 72,000 / 8,000 = **9.0 FTE**

The CFO is buying a curve, not a step change. The proposal commits to the curve.

## Quality Standards

- Value stack and cost stack are presented side by side; intervention rate is named.
- Model-call cost per task is computed, not omitted as "cloud cost".
- Supervisor cost is computed; the agent does not get free oversight in the model.
- Cost per outcome is given at three intervention rates.
- Three scenarios reflect autonomy ramp, not just demand variation.
- Downside scenarios include an irreversible-incident dollar figure.
- FX is named where revenue is local and model costs are USD.
- The discount rate is the buyer's stated rate.
- The proposal does not quote tasks-per-FTE without subtracting intervention.

## Anti-Patterns

- "The agent saves 10 FTE" with no intervention rate.
- "Cost per ticket falls 80 %" with no model-call cost subtracted.
- Three scenarios that vary only volume, not autonomy.
- Irreversible-action incident treated as "we will be careful".
- Supervisor cost zeroed because "the agent runs itself".
- Payback computed at month 1 autonomy assumed to last forever.
- Scope-creep cost ignored; the case assumes the catalogue does not grow.
- Liability event excluded because "the buyer accepts the risk".

## Outputs

- Agent Value Stack table.
- Agent Cost Stack table.
- Tasks-per-FTE-Saved with Intervention Discount (worked at month 1 and month 6).
- Cost per Outcome at P50 / P90 / P99 intervention.
- Three-Scenario ROI (downside / base / upside) keyed to autonomy ramp.
- Payback in months and NPV at 36 months.
- Sensitivity on model-call price, intervention rate, volume.
- Downside Scenarios with mitigations.
- Agent Business Case Memo in the buyer's preferred shape.

## References

- `../references/ai-agent-business-case-template.md` — formulas, worked examples, FX handling.
- `../references/ai-agent-metrics-glossary.md` — definitions used in the case.
- `../references/ai-agent-pricing-models-reference.md` — pricing patterns that change the revenue / cost split.
- `../references/ai-agent-sla-class-table.md` — SLA class credit schedule (downside modelling).
- `../references/ai-agent-credit-and-refund-clauses.md` — credit and refund clauses (worst-credit-month inputs).
- `../ai-agent-pricing-and-packaging-proposal/SKILL.md` — pricing inputs.
- `../ai-agent-sla-and-credit-schedule/SKILL.md` — credit-cost into downside.
- `../ai-agent-intervention-credit-and-abort-refund/SKILL.md` — intervention-credit exposure.
- `../ai-on-saas-business-case-and-roi/SKILL.md` — AI-on-SaaS business case when the agent lives inside a SaaS product.
- `../ai-agent-risk-and-responsible-ai/SKILL.md` — downside scenarios.
- `../10-financial-proposal/SKILL.md` — financial proposal placement.
- `../premium-pricing-and-value-defense/SKILL.md` — fee defence at the close.
