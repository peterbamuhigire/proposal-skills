---
name: ai-on-saas-pricing-and-packaging-proposal
description: Use when the AI-on-SaaS proposal must price and package AI features inside a SaaS product. Provides usage-based AI credits, included-allowance + overage, AI-tier-as-upsell, model-selection-by-tier, fair-use language, and protection against tenant abuse and model-price volatility. Extends `saas-pricing-and-packaging-proposal` with the AI overlay.
---

# AI-on-SaaS Pricing and Packaging Proposal
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The AI-on-SaaS product is being priced for the first time, repriced, or repackaged.
- The buyer expects a defensible pricing structure that survives CFO and CISO scrutiny.
- The proposal must address AI-credit packaging, fair-use, model-by-tier, and token-cost pass-through.
- The buyer faces volatile model prices and needs price-increase clauses with a real basis.
- The competitive set includes vendors who bundle AI for free (loss-leader) or meter aggressively (rent-extraction).

## Do Not Use When

- The pricing is for a non-AI SaaS engagement (use `saas-pricing-and-packaging-proposal`).
- The engagement is fee-for-service AI consulting with no recurring SaaS revenue.

## Required Inputs

- The AI Value Stack and AI Cost Stack from `ai-on-saas-business-case-and-roi`.
- The buyer's pricing instinct (subscription, usage, hybrid, value-based).
- The competitive pricing reference points (named competitors, prices).
- Cost-of-tokens at P50 / P90 / P99 by tenant.
- The buyer's tolerance for variable bills.
- The buyer's tier strategy (good / better / best, or persona-based).

## Workflow

1. Decide the **AI pricing pattern** from the patterns library: (a) bundled-in-tier (AI as part of base licence), (b) AI-tier-as-upsell (separate premium tier with AI), (c) included-allowance + overage (X credits / month then $Y per K tokens), (d) pure usage credits (pay per use), (e) hybrid floor + overage.
2. Map the pattern to the buyer's tolerance and the AI Cost Stack. Bundled-in-tier is dangerous if cost-of-tokens at P99 swamps the licence fee.
3. Decide **model-by-tier**: standard tier locked to a cost-efficient model, premium tier picks model (frontier model available), regulated tier locked to sovereign / region-routed model. State the model-gateway architecture that enables this.
4. Write the **fair-use clause**: per-tenant call ceiling per month, abuse-detection trigger, escalation to commercial conversation. Fair-use is not a punishment; it is a price-stability mechanism for both sides.
5. Write the **price-increase clause** with a real basis: model-provider price index, FX index, annual cap (e.g. CPI + 3 %), or a pass-through with a margin floor. Vague "we may increase prices" is rejected by procurement.
6. Write the **rollover / forfeit** policy for AI credits (rollover one month, forfeit thereafter, or no rollover with discount).
7. Write the **tenant-tier-switch** language: how a tenant moves from standard to premium (no migration, instant model upgrade) and back (drained credits, downgrade at renewal).
8. Show **worked examples**: small tenant (P50 usage), medium tenant (P90), heavy tenant (P99); for each, bill at the proposed pricing and compare to the buyer's cost-of-tokens.
9. Output the **AI Pricing Proposal** subsection of the financial proposal.

## Quality Standards

- The pricing pattern is named and justified by the cost stack and the buyer's tolerance.
- Cost-of-tokens at P99 is below the licence-fee plus overage, with margin, in every worked example.
- Model-by-tier is technically deliverable (the model gateway exists in the methodology).
- Fair-use is defined with a number, not a vague clause.
- Price-increase clause has a real index, an annual cap, or a margin-floor pass-through.
- FX is named where revenue is local and model costs are USD.
- The pricing protects the agency against model-price volatility and the buyer against runaway bills.

## Anti-Patterns

- AI bundled into the base tier at no marginal price with no fair-use.
- "Usage-based credits" with no per-credit price and no overage rate.
- "Premium AI tier" with no defined model difference.
- Fair-use as a vague "reasonable use" clause.
- Price-increase as a one-line "subject to change with 30 days' notice" with no index or cap.
- Worked examples that hide P99 behaviour behind P50 averages.
- FX risk left on the agency side without a clause.

## Outputs

- AI Pricing Proposal subsection of the financial proposal.
- AI Pricing Pattern Decision Memo (for the win-room file).
- Model-by-Tier Matrix.
- Fair-Use Clause language.
- Price-Increase Clause language.
- Worked examples for P50 / P90 / P99 tenants.

## Agent Overlay

For agentic engagements, the pattern library expands from five to **six agent-specific patterns**: per-resolution, per-outcome, per-step, per-agent, hybrid (base + usage), and success-based (outcome-linked bonus). Two clauses become essential: **intervention credit** (if intervention rate exceeds the agreed ceiling, the buyer receives a credit) and **vendor cost pass-through** (agents fan out 10–100 model calls per task; a model-price increase invisible in a copilot can be catastrophic in an agent). Load `../ai-agent-pricing-and-packaging-proposal/SKILL.md` for the agent pricing patterns and clauses.

## References

- `../references/ai-on-saas-pricing-models-reference.md` — pattern library, worked examples, clauses.
- `../references/saas-pricing-models-reference.md` — base SaaS pricing patterns.
- `../saas-pricing-and-packaging-proposal/SKILL.md` — base SaaS pricing skill.
- `../ai-on-saas-business-case-and-roi/SKILL.md` — cost stack input.
- `../10-financial-proposal/SKILL.md` — financial proposal placement.
- `../premium-pricing-and-value-defense/SKILL.md` — premium-fee defence.
