---
name: ai-agent-renewal-and-true-up
description: Use when drafting the renewal mechanics for an agentic engagement — auto-renewal, true-up clauses for volume divergence, ramp-down protection, autonomy-progression price-step, and index-linked renewal anchored to model-provider price index and FX. Pairs with `ai-agent-pricing-and-packaging-proposal` and `ai-agent-sla-and-credit-schedule`. Designed for autonomy ramps that change the price as the agent matures.
---

# AI-Agent Renewal and True-Up
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The engagement has a multi-year horizon and the renewal mechanics must be drafted now.
- The agent's autonomy ramp is expected to change the price (price-step at each autonomy level achieved).
- Volume is uncertain and true-up is required.
- The buyer's procurement team has signalled the renewal clause is a deal-blocker if not pre-agreed.
- The model-provider price and FX are volatile and the renewal must index against them.

## Do Not Use When

- The engagement is a one-off fixed-fee build with no recurring component.
- The engagement is month-to-month with no renewal commitment.

## Required Inputs

- The base term, the renewal term, and the notice period.
- The autonomy ramp curve with named milestones and price-steps.
- The volume baseline and the true-up direction (over / under / both).
- The model-provider price-index source and FX reference rate.
- The CPI source (where indexed pricing applies).
- The ramp-down protection the buyer expects.
- The agency's renewal posture (auto vs express).

## Workflow

1. Set the **base term** (typically 12 / 24 / 36 months) and the **renewal term** (typically annual).
2. Decide **auto-renewal vs express-renewal** — auto with 90-day notice is the default; regulated buyers often require express renewal.
3. Write the **true-up clause** for volume — at the end of each quarter or annum, observed volume is reconciled against the included volume; overage is billed; under-use does not refund (the buyer pre-committed to the included volume).
4. Write the **autonomy-progression price-step** — the price changes when the agent crosses a named autonomy threshold (e.g. intervention rate sustained below 8 % for three months → next pricing tier; sustained above 15 % for three months → previous pricing tier).
5. Write the **ramp-down protection** — the buyer's right to reduce included volume by a defined percentage at renewal (typically up to 15 %) without re-priced base.
6. Write the **index-linked renewal** — annual price reset capped at CPI + N % or model-provider-price-index + N %, with a margin floor and a buyer protection floor.
7. Write the **FX corridor** — the price denomination, the reference rate, and the corridor (typically 15 %) outside which a commercial review is triggered.
8. Output the **Renewal Exhibit** for the MSA.

## The Renewal Mechanics

### Auto-Renewal vs Express-Renewal
- **Auto-renewal** with 90-day non-renewal notice is the default for non-regulated buyers; protects revenue continuity.
- **Express renewal** with a 60-day pre-renewal review window is the default for regulated buyers and public sector; protects against governance failures.
- A hybrid is available: auto-renewal with a mandatory pre-renewal review at month 10 (of a 12-month base), with named topics — autonomy progression, SLA performance, credit and refund history, model-provider posture, FX movement, regulatory environment.

### True-Up Clause
At the end of each **True-Up Period** (typically quarterly for high-volume engagements, annual for stable engagements):
- **Overage** — volume above included is billed at the overage rate.
- **Under-use** — volume below included does not refund (the buyer pre-committed); a portion of the under-use (typically up to 25 %) may roll forward into the next period at the agency's discretion.
- **Material divergence** — observed volume diverges from forecast by more than 30 % over two consecutive periods triggers a commercial review.

### Autonomy-Progression Price-Step
The agent's autonomy progression changes the price:
- Crossing the next autonomy tier (e.g. intervention rate sustained ≤ 8 % for three months) → price moves to the next tier (better unit economics for the buyer).
- Slipping below the previous autonomy tier (e.g. intervention rate sustained ≥ 15 % for three months) → price moves to the previous tier (more supervisor cost recovered).
- The price-step protects both sides — the buyer is not paying mature-agent prices for an immature agent, and the agency is not absorbing supervisor cost on a regressing agent.

### Ramp-Down Protection
At renewal, the buyer may reduce included volume by up to **R %** (typically 15 %) without re-priced base. Beyond R %, the agency re-prices the base to reflect the reduced cost recovery. The buyer may not reduce the SLA class without re-priced base.

### Index-Linked Renewal
The annual price reset is capped at the **lower of**:
- CPI + N % (typically CPI + 3 %), and
- Model-provider-price-index + M % (typically model-index + 2 %),
with a **margin floor** for the agency (the agency does not absorb a model-price hike that would breach its floor) and a **buyer protection floor** (the agency does not raise prices in a low-CPI year by stacking indices).

### FX Corridor
Where the buyer's fees are in local currency (KES, NGN, UGX, RWF, ZAR) and the model costs are in USD:
- Reference rate is the named index (central bank reference rate) on the last business day of the month preceding the invoice month.
- A 15 % corridor against the rate at the Effective Date over any rolling 12-month period triggers a commercial review.
- The agency does not absorb sustained FX shocks beyond the corridor.

## Quality Standards

- Auto-renewal posture is explicit (auto vs express vs hybrid).
- True-up direction is named (both over and under).
- Autonomy price-step has named thresholds and a sustained-observation window.
- Ramp-down protection has a named percentage.
- Index-linked renewal names both CPI and model-provider-price-index, with caps and floors.
- FX corridor is named with reference rate and percentage.
- Renewal exhibit is internally consistent with the pricing exhibit and the SLA exhibit.

## Anti-Patterns

- Auto-renewal hidden in fine print at the end of the contract.
- True-up that refunds under-use — the agency absorbs the under-commitment.
- Autonomy price-step undefined — the buyer keeps paying immature-agent prices forever, or vice versa.
- Ramp-down without a percentage — the buyer collapses volume at renewal and the agency cannot recover cost.
- Index-linked renewal with no floor — the agency absorbs FX or model-price shocks.
- FX corridor absent in an Africa-context engagement.
- "Subject to annual review" — procurement reads this as no commitment.

## Outputs

- Renewal Exhibit (drop-in).
- True-Up Schedule.
- Autonomy-Progression Price-Step Schedule.
- Ramp-Down Protection Clause.
- Index-Linked Renewal Clause.
- FX Corridor Clause.

## References

- `../references/ai-agent-renewal-and-true-up-clauses.md` — drop-in language.
- `../references/ai-agent-vendor-cost-pass-through.md` — model-provider price-index handling.
- `../references/ai-agent-pricing-exhibit-template.md` — pricing exhibit consistency.
- `../ai-agent-pricing-and-packaging-proposal/SKILL.md` — pricing patterns.
- `../ai-agent-commercial-packaging/SKILL.md` — packaging-shape renewal posture.
- `../ai-agent-sla-and-credit-schedule/SKILL.md` — SLA-class renewal interaction.
- `../ai-agent-msa-and-sla-addendum-templates/SKILL.md` — MSA addendum.
