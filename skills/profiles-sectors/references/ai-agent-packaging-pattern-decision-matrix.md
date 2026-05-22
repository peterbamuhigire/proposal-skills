# AI-Agent Packaging Pattern Decision Matrix

Worked decision matrix for choosing between Agent Included in Pro, Agent Add-on, and Agent Standalone. Pairs with `../ai-agent-commercial-packaging/SKILL.md`.

## The Three Packaging Shapes — Side by Side

| Dimension | Included in Pro | Add-on | Standalone |
|---|---|---|---|
| Adoption friction | Lowest | Medium | Highest |
| Effective SLA class possible | Bronze / Silver | Silver / Gold | Gold / Platinum |
| Credit cap | ≤ 25 % | 25–50 % | 50–100 % |
| Default pricing patterns | D (per-agent included), E (hybrid) | A, C, D, E | B (outcome), F (success), E (high-base hybrid) |
| Renewal posture | Renews with SaaS | Independent clock | Independent clock + autonomy price-step |
| Refund triggers active | Force-majeure only | + Intervention overshoot | Full Abort-and-Refund |
| Pass-through | Limited (absorbed in tier price); annual review | Standard pass-through | Full pass-through with margin floor |
| Cost recovery for eval / red-team | From tier price aggregate | From add-on price directly | From base fee directly |
| Sales motion | Marketing-led | Solution-sales | Strategic sales |
| Best for | High-volume low-stakes agents | Mid-stakes regulated and unregulated | Mission-critical and regulated |

## Decision Tree

```
Q1: Is the agent's outcome attributable cleanly to the agent?
   No → Add-on or Included
   Yes ↓

Q2: Is the buyer comfortable buying an outcome (not a licence)?
   No → Add-on or Included
   Yes ↓

Q3: Is the SLA class required Gold or Platinum?
   No (Bronze / Silver OK) → Included (if also high-volume low-stakes) or Add-on
   Yes ↓

Q4: Is the autonomy ramp proven in pilot (intervention rate predictable)?
   No → Add-on with hybrid; promote to Standalone after autonomy stabilises
   Yes ↓

Q5: Is the regulator treating the agent as a distinct product?
   Yes → Standalone (regulator-aware SLA variant)
   No ↓

Q6: Does the buyer's CFO want the agent on its own P&L line?
   Yes → Standalone
   No → Add-on (with explicit upsell-to-Standalone path)
```

## Three Worked Decisions

### Worked Decision 1 — Customer-Support Resolution Agent (Included in Pro)

**Context.** A mid-market SaaS vendor sells a support platform with Starter / Pro / Enterprise tiers. They want to add a resolution agent. 80 % of their customers are in Pro. Average tenant volume is 50,000 tickets / month. Stakes are low (consumer support, no regulator).

**Decision.** Included in Pro, with a 30,000-resolution included volume and a $0.40 overage rate. SLA class Silver. Credit cap 25 %.

**Why.** Adoption needs to be broad; the agent's commercial story is "Pro now includes the AI Agent". Resolution is well-defined and attribution is clean. Stakes are low so Gold/Platinum is not required. The tier price is raised by 12 % to recover the cost stack at expected adoption.

**Risks managed.** Heavy users (above 30,000) are routed to Standalone at renewal. Light users do not generate enough volume to justify the tier uplift; the proposal models adoption-weighted economics and confirms the 12 % uplift is recovered at 60 % activation in the Pro base.

### Worked Decision 2 — Insurance Claims Triage Agent (Add-on)

**Context.** A mid-sized insurer wants to triage claims with an agent. The buyer's compliance team requires a regulator-aware SLA. The buyer has a CRM, a claims system, and a payments system. Volume is uncertain (forecast 5,000–12,000 claims / month). The buyer's CFO has signalled they will pay outcome-based pricing.

**Decision.** Add-on. Pattern E (hybrid base-plus-usage with success bonus on intervention rate ≤ 12 %). SLA class Gold. Credit cap 50 %. Base fee $32k/month including 5,000 claims; overage $0.60/claim; bonus $0.10/claim above 5,000 in months where intervention rate ≤ 12 %. Independent renewal clock.

**Why.** Buyer requires Gold SLA, which does not survive in an Included shape. Volume uncertainty is absorbed by the hybrid. The buyer's outcome appetite is captured through the bonus, not through a pure outcome pattern (Pattern B), because attribution disputes in insurance are messy.

**Risks managed.** Bonus capped at 10 % of base fees per quarter. Floor is the base fee. Pass-through is full. Renewal is independent so the agent can be elevated to Standalone if it matures into a Platinum-class deployment.

### Worked Decision 3 — Debt-Recovery Agent for SACCO Group (Standalone)

**Context.** A regional SACCO group wants an agent that handles debt-recovery outreach (calls, SMS, email, payment-plan negotiation within bounds). The group's regulator has issued guidance on automated customer interaction. The CFO wants a P&L line per group institution. The volume is high (~100k accounts in arrears across the group).

**Decision.** Standalone. Pattern B (gain-share at 8 % of recovered value above baseline) + monthly floor of $40k per institution. SLA class Gold (Platinum reserved for the group-wide control plane). Credit cap 50 %. Full Abort-and-Refund schedule. Autonomy-progression price-step at renewal.

**Why.** Buyer wants outcome pricing; attribution is clean (recovered value is a number). Regulator requires gold-class SLA with named accountability. The CFO wants the line item.

**Risks managed.** 30-day cooling-off on recoveries. Counter-example rule applied (chargeback within 60 days excluded). Floor protects against quiet months. FX corridor on the model-cost denomination. Sovereign-AI option offered at a premium for the regulator's data-residency concerns.

## Bundling Logic — When to Move

- **Move up (Included → Add-on)** when:
  - The cost stack is not recovered at observed adoption.
  - The buyer's SLA expectation has elevated.
  - Heavy users dominate volume and need a different tier of treatment.
  - The autonomy ramp has stalled and the credit schedule is biting into tier margin.

- **Move down (Add-on → Included)** when:
  - Adoption is broad and the add-on is becoming a default expectation.
  - Competitors are bundling and pricing power is shifting.
  - Intervention rate is below the floor consistently and supervisor cost has dropped.
  - Eval / red-team cost has moved into baseline ops cost.

- **Move out (Add-on → Standalone)** when:
  - Buyer is procuring outcomes, not licences.
  - Regulator treats the agent as a distinct product.
  - CFO wants the agent on its own P&L line.
  - Buyer wants Platinum SLA.
  - Outcome pricing is the right structure and the bundle blocks it.

## Adoption-Weighted Economics Stress Test

Every packaging decision must survive the adoption-weighted economics stress test. Compute:

```
Tier-aggregate cost recovery
  = Σ over tiers (tier_price × tier_subs × activation_rate)
  - Σ over tiers (agent_cost_per_tenant × tier_subs × activation_rate)
```

If the result is below the engineering, eval, red-team, and supervisor cost the Agency must cover, the package fails. Move up the matrix (Add-on or Standalone).

## Africa-Context Notes

- For SACCO and MFI customers in fragmented markets, Add-on is typically the right shape — outcome pricing works, but volume is variable enough that a pure Standalone with floor is too rich for some institutions.
- For public-sector buyers in EAC and SADC, Standalone with Pattern D (per-agent) is the default — outcome pricing is politically inappropriate; inclusion-in-tier rarely fits because there is no SaaS tier to bundle into.
- For FS group structures (regional banks, group SACCOs), packaging may differ by institution — a Standalone deployment to one CEO and an Add-on to the group's shared platform.
