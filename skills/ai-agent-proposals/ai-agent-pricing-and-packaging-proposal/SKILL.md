---
name: ai-agent-pricing-and-packaging-proposal
description: Use when the AI-agent proposal must price and package agent capability. Provides the six agent pricing patterns (per-resolution / per-outcome / per-step / per-agent / hybrid / success-based) with worked examples, intervention-credit reductions, vendor-cost-pass-through clauses, fair-use specific to agentic actions, model-price-volatility protection, abort and refund triggers, and FX clauses. Extends `ai-on-saas-pricing-and-packaging-proposal` with the agent overlay; replaces it when the engagement is stand-alone agentic.
---

# AI-Agent Pricing and Packaging Proposal
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The AI-agent product or service is being priced for the first time, repriced, or repackaged.
- The buyer expects a defensible pricing structure that survives CFO and procurement scrutiny.
- The proposal must address per-resolution, per-outcome, per-step, per-agent, hybrid, or success-based pricing.
- Vendor model-call cost behaviour is volatile and the agency needs cost-pass-through with a margin floor.
- The competitive set includes vendors who quote "per resolution" without defining what a resolution is, or quote a per-seat licence as if the agent did not consume tokens.

## Do Not Use When

- The pricing is for a non-agent SaaS or AI feature (use `saas-pricing-and-packaging-proposal` or `ai-on-saas-pricing-and-packaging-proposal`).
- The engagement is fee-for-service AI consulting with no recurring agentic operations.

## Required Inputs

- The Agent Value Stack and Agent Cost Stack from `ai-agent-business-case-and-roi`.
- The buyer's commercial instinct (subscription, usage, outcome, hybrid).
- The competitive pricing reference points (named competitors, prices, definitions of "resolution").
- Model-call cost per task at P50 / P90 / P99 per use case.
- Buyer's tolerance for variable bills and for outcome-based risk-sharing.
- Buyer's tier strategy (good / better / best, or persona-based, or sovereign / on-prem).
- The intervention-rate target curve from the pilot.
- The reversibility classification of each action class.

## Workflow

1. Decide the **agent pricing pattern** from the six patterns (below).
2. Map the pattern to the buyer's tolerance, the cost stack, and the intervention-rate target. Per-resolution looks attractive but is dangerous if intervention rate stays high. Per-step is conservative for the agency but invites scope-creep games.
3. Decide **what counts** (definition of a resolution, an outcome, a step, an agent). Procurement will exploit any ambiguity.
4. Write the **intervention-credit clause** — if intervention rate exceeds the agreed ceiling, the buyer receives a credit, calibrated to the intervention overhead the buyer carried.
5. Write the **vendor-cost-pass-through clause** — provider model-price index, FX index, annual cap, margin floor. Agents fan out model calls; a model-price increase that is invisible in a copilot can be catastrophic in an agent.
6. Write the **fair-use clause** specific to agents — per-tenant action ceiling per day, anomalous-action ceiling, scope-creep trigger (a new action class added by the buyer requires a change order).
7. Write the **abort and refund clause** — what triggers a refund (irreversible-action incident at the agency's fault; intervention rate beyond ceiling for 60 consecutive days; regulator action against the agentic system).
8. Write the **autonomy-ramp clause** — pricing assumes a stated autonomy ramp; if the buyer demands a higher autonomy level than the methodology supports, the buyer accepts the resulting risk and the price changes.
9. Show **worked examples** — small tenant, medium tenant, heavy tenant — for each pattern.
10. Output the **Agent Pricing Proposal** subsection of the financial proposal.

## The Six Agent Pricing Patterns

### Pattern A — Per-Resolution (Outcome Unit)
- The agency charges $X per resolved ticket / triaged claim / reconciled batch / drafted document.
- "Resolution" is defined narrowly (the agent did the work; the human did not have to redo it; the outcome held for N days).
- Best for: high-volume, well-defined outcome workflows (support, claims acknowledgement, low-stakes operations).
- Risk to agency: intervention rate exceeds plan and the price-per-resolution does not cover model and supervision cost.
- Mitigation: floor price, intervention-credit ceiling, model-cost-pass-through clause.

### Pattern B — Per-Outcome (Business Result Unit)
- The agency charges per business outcome, not per agent action. Example: per recovered debt, per renewed policy, per closed bug.
- Best for: workflows where the buyer can attribute outcome cleanly to the agent.
- Risk to agency: attribution disputes; outcome timing exceeds agency control.
- Mitigation: outcome definition with cooling-off period and dispute clause; minimum-fee floor.

### Pattern C — Per-Step (Action Unit)
- The agency charges per agent action (tool call, system write, message sent), or per task step.
- Best for: workflows where the buyer wants visibility and refuses to pay for outcomes the agent does not control end-to-end.
- Risk to agency: incentive for the agent to over-call tools.
- Mitigation: step budget per task; anomaly alerting; quarterly review.

### Pattern D — Per-Agent (Seat / Persona Unit)
- The agency charges per agent persona (e.g. "1 support agent — 24x7 — handling up to N tickets / month").
- Best for: buyers who think in headcount terms and want a clean comparison ("this agent costs the equivalent of 0.3 FTE").
- Risk to agency: heavy users overrun the included volume; light users under-utilise.
- Mitigation: included-volume cap and overage rate; volume-floor for the buyer.

### Pattern E — Hybrid (Base + Usage)
- A base fee covers platform, oversight queue, eval and red-team, plus a per-resolution / per-step rate above an included allowance.
- Best for: enterprise buyers who want budget predictability with a usage tail.
- Risk to agency: complex bills, hard to explain.
- Mitigation: clear allowance, overage rate, monthly statement, quarterly review.

### Pattern F — Success-Based (Outcome-Linked Bonus)
- A base fee at a lower rate plus a bonus on achieving an agreed outcome threshold (e.g. 80 % autonomy at month 6 → bonus; intervention rate below 10 % → bonus).
- Best for: trust-building engagements where the agency has confidence in the methodology and the buyer wants skin-in-the-game.
- Risk to agency: outcome shortfall destroys margin.
- Mitigation: bonus is genuinely a bonus, not buried as risk; base fee covers cost; cap on bonus.

## Worked Pattern Map by Use Case

| Use case | Recommended pattern | Why |
|---|---|---|
| Customer support resolution | A or E | Volume is high; resolution is defined; both sides care about per-ticket economics |
| Insurance claims triage | C or D | Outcome attribution is messy; per-step or per-agent is cleaner |
| Financial reconciliation | B or D | Outcome is clean (reconciled batch); per-agent works for in-house ops |
| Legal drafting / review | C or D | Outcome is the human's; per-step or per-agent fits |
| Citizen-service (public-sector) | D | Outcome-based pricing is politically inappropriate; per-agent gives transparency |
| Healthcare admin | D | Outcome attribution is sensitive; per-agent gives clarity |
| Coding / ops triage | C or E | Step count and base + usage suit engineering ops |

## Clauses the Procurement Team Will Read First

- **Definition of unit** — every pricing unit (resolution, outcome, step, agent) defined in one paragraph with examples and counter-examples.
- **Intervention credit** — if intervention rate exceeds X % for the month, the buyer receives a Y % credit on units billed.
- **Vendor cost pass-through** — model-call cost indexed to provider price; annual cap (e.g. CPI + 3 % or model-price-index + N %); margin floor; notice before increase.
- **Fair-use** — per-tenant action ceiling per day; anomalous-action ceiling (e.g. agent attempts more than 3× P95 daily action volume); scope-creep trigger (new action class requires change order).
- **Abort and refund** — irreversible-action incident at agency fault → defined refund; intervention rate beyond ceiling for 60 days → buyer may exit with pro-rata refund; regulator action → joint review.
- **Autonomy ramp** — pricing assumes ramp curve; demand for faster ramp invokes a re-price.
- **FX** — model costs in USD; revenue in local currency; FX index or annual reset.

## Quality Standards

- The pricing pattern is named and justified by the cost stack and the buyer's tolerance.
- Cost-of-model-calls at P99 per task is below the priced unit, with margin, in every worked example.
- Definitions of "resolution / outcome / step / agent" are explicit.
- Intervention credit and abort-and-refund clauses are present.
- Vendor cost pass-through has an index, cap, and margin floor.
- Fair-use is defined numerically.
- FX is named.
- The pricing protects both sides against model-price volatility and against intervention overshoot.

## Anti-Patterns

- Per-resolution pricing with "resolution" undefined.
- "Outcome-based pricing" with no attribution clause.
- Per-step pricing with no step budget.
- Per-agent pricing with no included-volume cap.
- Hybrid pricing with the allowance hidden in an appendix.
- Success bonus written as risk dressed up as bonus.
- Model-cost pass-through as "subject to change".
- No intervention credit (buyer carries all the supervisor cost).
- Scope-creep ignored — buyer adds use cases at no extra price and the agency drowns.

## Outputs

- Agent Pricing Proposal subsection of the financial proposal.
- Agent Pricing Pattern Decision Memo (win-room file).
- Unit Definitions (resolution / outcome / step / agent) one-paragraph each.
- Intervention Credit Clause.
- Vendor Cost Pass-Through Clause.
- Fair-Use Clause.
- Abort-and-Refund Clause.
- Autonomy-Ramp Clause.
- Worked examples for small / medium / heavy tenants.

## Packaging-Pattern Decision Matrix

The pricing pattern is paired with a **packaging shape** — Included in Pro, Add-on, or Standalone — that constrains the SLA class achievable, the credit cap, the renewal posture, and the cost recovery shape. Use `../ai-agent-commercial-packaging/SKILL.md` to choose the shape before finalising the pattern. The reference matrix `../references/ai-agent-packaging-pattern-decision-matrix.md` shows pattern × shape combinations with worked examples.

| Shape | Recommended patterns | Default SLA class | Credit cap |
|---|---|---|---|
| Included in Pro | D, E | Bronze / Silver | ≤ 25 % |
| Add-on | A, C, D, E | Silver / Gold | 25–50 % |
| Standalone | B, F, E (high-base) | Gold / Platinum | 50–100 % |

## SLA-Tier Alignment with Pricing Tier

Every pricing pattern attaches to an SLA Class. The SLA Class drives the metric thresholds, the credit schedule, the kill-switch and audit-log SLAs, and the credit cap. The pricing exhibit and the SLA exhibit must reference the same numbers, same definitions, and same evidence trail. Load `../ai-agent-sla-and-credit-schedule/SKILL.md` after choosing the pattern.

## Commercial Layer Cross-Links

The pricing pattern is one of nine commercial artefacts the proposal carries. The others are produced by the dedicated commercial-layer skills:

- `../ai-agent-sla-and-credit-schedule/SKILL.md` — SLA class and credit schedule.
- `../ai-agent-commercial-packaging/SKILL.md` — packaging shape decision.
- `../ai-agent-contract-language-pack/SKILL.md` — drop-in exhibit assembly.
- `../ai-agent-success-fee-and-outcome-pricing/SKILL.md` — outcome and success-fee structures (Patterns B, F, E with success component).
- `../ai-agent-intervention-credit-and-abort-refund/SKILL.md` — intervention-credit formula and abort-refund triggers.
- `../ai-agent-msa-and-sla-addendum-templates/SKILL.md` — MSA / SLA addendum.
- `../ai-agent-procurement-objections-on-commercials/SKILL.md` — commercial objection handling.
- `../ai-agent-renewal-and-true-up/SKILL.md` — renewal, true-up, autonomy price-step.
- `../references/ai-agent-pricing-exhibit-template.md` — drop-in pricing exhibit.

## References

- `../references/ai-agent-pricing-models-reference.md` — pattern library with worked examples and clauses.
- `../references/ai-agent-pricing-exhibit-template.md` — drop-in pricing exhibit.
- `../references/ai-agent-packaging-pattern-decision-matrix.md` — packaging decision matrix.
- `../references/ai-agent-sla-class-table.md` — SLA class thresholds and credit schedule.
- `../references/ai-on-saas-pricing-models-reference.md` — AI-on-SaaS pricing patterns.
- `../ai-on-saas-pricing-and-packaging-proposal/SKILL.md` — AI-on-SaaS pricing when the agent lives inside a SaaS product.
- `../ai-agent-business-case-and-roi/SKILL.md` — cost stack input.
- `../ai-agent-sla-and-credit-schedule/SKILL.md` — SLA class and credit schedule.
- `../ai-agent-commercial-packaging/SKILL.md` — packaging shape.
- `../10-financial-proposal/SKILL.md` — financial proposal placement.
- `../premium-pricing-and-value-defense/SKILL.md` — premium-fee defence.
