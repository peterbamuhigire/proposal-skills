---
name: ai-agent-commercial-packaging
description: Use when choosing whether an AI agent is included, sold as an add-on, or sold standalone; use the pricing skill for rate mechanics and the SLA skill for service commitments.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent Commercial Packaging
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The agency must decide whether the agent is bundled into a SaaS tier, sold as an add-on, or sold standalone.
- The buyer's commercial conversation has multiple shapes (some tenants want the agent included; others want to buy it separately; others want only the agent).
- The packaging decision changes which SLA class is available, which credit schedule applies, and which renewal posture works.
- A SaaS-embedded agent must be priced without cannibalising the core subscription or breaking the existing renewal economics.

## Do Not Use When

- The engagement is a one-off agent build with no recurring commercial model.
- The pricing pattern has not yet been chosen — choose the pattern with `ai-agent-pricing-and-packaging-proposal` first, then return.

## Domain Inputs

- Existing SaaS pricing and packaging (if any).
- Buyer's tier strategy (good / better / best, persona, sovereign).
- Buyer's procurement instinct on whether the agent is "part of the product" or "a separate purchase".
- Agent cost stack (per `ai-agent-business-case-and-roi`).
- Forecast adoption per tier (what percentage of customers will actually use the agent).
- The SLA class the buyer expects (Bronze / Silver / Gold / Platinum) and whether that SLA can survive in a bundled shape.
- The eval, red-team, drift-watch cost the agency must recover (these are real costs that do not disappear just because the agent is bundled).

## Domain Method

1. Read the **three packaging shapes** below and select the candidate(s) by buyer fit and economic fit.
2. For each candidate, compute the **economic effect** on margin: at forecast adoption, does the package pay for the agent cost stack, the eval / red-team cost, the supervisor cost, and the credit-schedule exposure?
3. Decide the **SLA class** that survives in the chosen shape — Bronze and Silver are bundleable; Gold and Platinum usually break the bundle and require a Standalone or Add-on shape.
4. Decide the **renewal posture** — bundled agents renew with the SaaS; standalone agents renew on their own clock with separate true-up; add-on agents can be moved to standalone at renewal.
5. Write the **packaging exhibit** — table of what the buyer gets at each shape, with included volumes, overage rates, SLA class, credit schedule, support model, eval reporting, kill-switch availability.
6. Stress-test the package against three customer profiles (light / medium / heavy) and confirm margin and SLA viability at each.
7. Output the **Packaging Decision Memo** (win-room file) and the **Packaging Exhibit** (proposal artefact).

## The Three Packaging Shapes

### Shape 1 — Agent Included in Pro (Bundled)

- The agent is included in the existing Pro tier (or equivalent), with an included volume and overage.
- **Strengths**: lowest friction; fastest adoption; agent becomes a default product feature; competitive against "AI-included" pitches.
- **Weaknesses**: hard to recover real agent cost from light users; the cost stack is real (model calls, supervisor cost, eval, red-team) and the average tenant may not justify it; SLA must be modest (Bronze / Silver) because bundled support cannot absorb a Platinum credit schedule; renewal pressure if buyers churn on tier price.
- **Best for**: high-volume, low-stakes agents (customer-support resolution, simple drafting, basic triage) where included volume is generous and intervention rate is low after stabilisation.
- **Required guardrails**: included-volume cap; overage rate; fair-use; sovereign-AI premium variant if needed; right to move heavy users to Standalone at renewal.

### Shape 2 — Agent Add-on (Modular)

- The agent is an optional add-on to any tier, with its own price, included volume, SLA class, and credit schedule.
- **Strengths**: cleanest economics — adoption is opt-in, every paying customer chose the agent; SLA class can be raised (Gold available); cost recovery is transparent; can be priced under any of the six patterns (per-resolution, per-outcome, per-step, per-agent, hybrid, success-based).
- **Weaknesses**: requires a separate sales motion; some buyers see add-ons as nickel-and-diming; the add-on must be defensible against "why isn't this just in the product?" — answer with the eval, red-team, supervisor, and audit-log cost stack.
- **Best for**: regulated verticals; mid-stakes and higher-stakes agents; engagements where the agent's autonomy curve is still maturing.
- **Required guardrails**: explicit included volume; overage; SLA class named (Silver or Gold default); credit schedule; intervention-credit explicit; renewal mechanics independent of base tier.

### Shape 3 — Agent Standalone (Headline)

- The agent is sold on its own, with no SaaS base required. The buyer subscribes to the agent for its outcomes (resolutions, claims triaged, debt recovered, ops alerts triaged).
- **Strengths**: highest possible SLA class (Platinum available); highest possible price discipline (no need to bundle a tier price); cleanest outcome-pricing or success-fee structure; strongest premium positioning.
- **Weaknesses**: highest commercial expectation; buyer will scrutinise every clause; floor pricing must protect against light months; vendor-cost-pass-through becomes critical because there is no SaaS base to absorb a model-price shock.
- **Best for**: mission-critical agents; high-stakes regulated verticals; outcome-based commercials; gain-share.
- **Required guardrails**: floor price; vendor pass-through with cap and margin floor; FX corridor; SLA Platinum with full credit schedule; abort-and-refund clause; autonomy-ramp clause; quarterly SLA review with the buyer's operations and legal.

## Packaging × Pricing × SLA Decision Matrix

| Shape | Recommended pricing patterns | Default SLA class | Credit posture | Renewal |
|---|---|---|---|---|
| Included in Pro | D (per-agent included volume), E (hybrid) | Bronze or Silver | Modest credits (≤ 25 % cap) | Renews with SaaS |
| Add-on | A (per-resolution), C (per-step), D (per-agent), E (hybrid) | Silver or Gold | 25–50 % cap | Independent clock; can be elevated to Standalone at renewal |
| Standalone | B (per-outcome), F (success-based), E (hybrid with high base) | Gold or Platinum | 50–100 % cap; abort-and-refund | Standalone clock; autonomy-progression price-step at renewal |

See [ai-agent-packaging-pattern-decision-matrix](../../profiles-sectors/references/ai-agent-packaging-pattern-decision-matrix.md) for the worked decision matrix.

## Bundling Logic — When to Move the Agent Up or Down

- **Move up (Included → Add-on)** when adoption is concentrated in a small share of tenants, when intervention rate is not falling, or when the SLA class the buyer demands does not survive the bundled shape.
- **Move down (Add-on → Included)** when adoption is broad, intervention rate is below the floor, and the agent has become a default expectation that competitors are bundling.
- **Move out (Add-on → Standalone)** when the buyer is buying outcomes, not licences; when the regulator treats the agent as a distinct product; when the buyer's CFO wants the agent on its own P&L line.

## Effect on Underlying SaaS Pricing

- Bundling the agent into Pro typically requires either a Pro price increase or a modest reduction in Pro margin during the autonomy ramp. The proposal must be honest about which.
- Add-on packaging protects Pro margin and gives a clean upsell narrative for CSMs.
- Standalone packaging can co-exist with a SaaS base or replace it; the proposal must say which.
- Across all three shapes, the agent's eval / red-team / supervisor / audit-log costs are real and recurring; the proposal must show how each shape recovers them.

## Quality Standards

- The chosen shape is justified by buyer fit and by economic fit at forecast adoption.
- The SLA class is consistent with the shape (no Platinum SLA on an Included-in-Pro bundle without explicit Pro price uplift).
- Included volume, overage, and credit schedule are explicit at every shape.
- Renewal posture is explicit and tested against autonomy-progression and model-price volatility.
- The packaging exhibit is drop-in.

## Domain Risks

- Promising Platinum SLA on a bundled agent without restructuring the bundle price.
- Bundling the agent into a tier without modelling adoption-weighted cost recovery — the agency loses money on heavy users.
- Add-on packaging without an independent renewal clock — the agent renews automatically with a tier the buyer is already trying to leave.
- Standalone packaging without an explicit floor — light months blow margin.
- Treating packaging as a marketing decision; it is a commercial-engineering decision that changes the SLA, the credit schedule, the renewal mechanics, and the cost recovery.

## Domain Outputs

- Packaging Decision Memo (win-room file).
- Packaging Exhibit (proposal artefact).
- Margin sensitivity at three adoption profiles.
- Confirmation that the chosen SLA class survives in the chosen shape.

## Anti-Patterns

- Quoting an unverified commercial term. Fix: trace it to the approved brief or contract record and label any unresolved variable.
- Billing an attempted task as a completed outcome. Fix: define the eligible event, exclusions, reversal window, and evidence source.
- Leaving credits, refunds, or liability uncapped. Fix: state the eligible fee base, cap, trigger, exclusions, and approval owner.
- Updating one exhibit while dependent terms still conflict. Fix: reconcile pricing, SLA, credit, refund, renewal, and liability provisions together.
- Removing a legal placeholder without authority. Fix: retain the marker, name the decision owner, and require qualified review before issue.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| commercial brief and adoption forecast | Buyer, proposal owner, approved contract record, or measured operating evidence | Yes | Stop before making a commitment; list the missing evidence and provide only a qualified option set. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Packaging decision memo and exhibit | Proposal lead and finance reviewer | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| packaging decision memo and exhibit | Proposal lead and finance reviewer | Assumptions, measures, authority, exclusions, and acceptance tests are explicit and traceable to the supplied evidence. |

## Capability Contract

Minimum capability is read access to the approved commercial record and calculation support for any stated formula. Drafting authority permits edits only inside the requested proposal or contract working copy. Do not sign, publish, spend, change production configuration, concede liability, or represent legal approval without explicit authority. Legal and tax conclusions require qualified review.

## Degraded Mode

Fallback when tools are unavailable: use the qualified path below.

If source terms, telemetry, calculation tools, or legal review are unavailable, return the narrowest useful marked draft: identify unverified variables, preserve placeholders, show the calculation method where possible, and mark each unavailable check as not assessed. Never convert missing evidence into approval.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Choose included, add-on, or standalone | Match buyer adoption, cost recovery, and SLA economics. | Margin loss or an unsellable bundle. |
| Evidence is incomplete or positions conflict | Stop commitment drafting, record the conflict, and request the named owner’s decision. | Invented terms, double recovery, or an unauthorised concession. |
| Evidence and authority are complete | Draft, cross-check dependent exhibits, and retain the calculation or clause trace. | An internally inconsistent commercial package. |

## Workflow

1. Confirm the consumer, authority, controlling commercial record, and required inputs; stop when a baseline or accountable owner is missing.
2. Reproduce relevant calculations and identify conflicts across pricing, SLA, credit, refund, renewal, liability, and scope; stop when a formula cannot be reproduced.
3. Apply the domain method and decision rules within delegated authority, recording assumptions and exclusions.
4. Draft the contracted output and cross-check every dependent exhibit; recover by reconciling the controlling term with its owner and rerunning the calculation.
5. Verify acceptance conditions, evidence trace, legal-review markers, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

A buyer forecasts 20% tenant adoption and needs a separately renewable Gold SLA. Select an add-on, show included volume and overage, and test margin at low, base, and high adoption.

<!-- dual-compat-end -->

## References

- [ai-agent-packaging-pattern-decision-matrix](../../profiles-sectors/references/ai-agent-packaging-pattern-decision-matrix.md) — worked decision matrix.
- [ai-agent-pricing-exhibit-template](../../profiles-sectors/references/ai-agent-pricing-exhibit-template.md) — drop-in pricing exhibit.
- [ai-agent-sla-class-table](../../profiles-sectors/references/ai-agent-sla-class-table.md) — SLA class thresholds.
- [ai-agent-pricing-and-packaging-proposal](../../ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md) — the six pricing patterns.
- [ai-agent-sla-and-credit-schedule](../ai-agent-sla-and-credit-schedule/SKILL.md) — the SLA the package will carry.
- [ai-agent-renewal-and-true-up](../ai-agent-renewal-and-true-up/SKILL.md) — renewal mechanics.
- [saas-pricing-and-packaging-proposal](../../saas-proposals/saas-pricing-and-packaging-proposal/SKILL.md) — SaaS packaging context.
- [premium-pricing-and-value-defense](../../strategy-positioning/premium-pricing-and-value-defense/SKILL.md) — premium fee defence.
