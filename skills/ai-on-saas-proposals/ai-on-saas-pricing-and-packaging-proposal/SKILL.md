---
name: ai-on-saas-pricing-and-packaging-proposal
description: Use when pricing AI features within SaaS through credits, allowances, overages, model tiers, or fair-use controls while protecting margin from usage and provider-cost volatility; use SaaS pricing when AI economics do not apply.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI-on-SaaS Pricing and Packaging Proposal
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
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

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The AI Value Stack and AI Cost Stack from `ai-on-saas-business-case-and-roi`. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's pricing instinct (subscription, usage, hybrid, value-based). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The competitive pricing reference points (named competitors, prices). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Cost-of-tokens at P50 / P90 / P99 by tenant. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's tolerance for variable bills. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's tier strategy (good / better / best, or persona-based). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

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


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- The pricing pattern is named and justified by the cost stack and the buyer's tolerance.
- Cost-of-tokens at P99 is below the licence-fee plus overage, with margin, in every worked example.
- Model-by-tier is technically deliverable (the model gateway exists in the methodology).
- Fair-use is defined with a number, not a vague clause.
- Price-increase clause has a real index, an annual cap, or a margin-floor pass-through.
- FX is named where revenue is local and model costs are USD.
- The pricing protects the agency against model-price volatility and the buyer against runaway bills.

## Anti-Patterns

- AI bundled into the base tier at no marginal price with no fair-use. **Fix:** Set an included allowance from measured usage, publish overage and fair-use rules, and protect access with budgets and alerts.
- "Usage-based credits" with no per-credit price and no overage rate. **Fix:** Define the credit unit, conversion by model or action, included volume, expiry, overage price, and worked invoice.
- "Premium AI tier" with no defined model difference. **Fix:** State the models, quality, latency, governance, support, and usage allowance that distinguish each tier.
- Fair-use as a vague "reasonable use" clause. **Fix:** Translate fair use into measurable limits, monitoring, notification, throttling, appeal, and restoration rules.
- Price-increase as a one-line "subject to change with 30 days' notice" with no index or cap. **Fix:** Use a named index or provider-cost trigger, notice period, cap, customer options, and renewal treatment.
- Worked examples that hide P99 behaviour behind P50 averages. **Fix:** Show P50, P90, and P99 usage, including heavy-tenant and abuse cases, in buyer-visible invoice examples.
- FX risk left on the agency side without a clause. **Fix:** State billing currency, FX source and observation date, adjustment band, review cadence, and allocation of FX risk.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Pricing Proposal subsection of the financial proposal. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| AI Pricing Pattern Decision Memo (for the win-room file). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Model-by-Tier Matrix. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Fair-Use Clause language. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Price-Increase Clause language. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Worked examples for P50 / P90 / P99 tenants. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## Agent Overlay

For agentic engagements, the pattern library expands from five to **six agent-specific patterns**: per-resolution, per-outcome, per-step, per-agent, hybrid (base + usage), and success-based (outcome-linked bonus). Two clauses become essential: **intervention credit** (if intervention rate exceeds the agreed ceiling, the buyer receives a credit) and **vendor cost pass-through** (agents fan out 10–100 model calls per task; a model-price increase invisible in a copilot can be catastrophic in an agent). Load `../ai-agent-pricing-and-packaging-proposal/SKILL.md` for the agent pricing patterns and clauses.

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Input-and-assumption record | Proposal lead and reviewer | Every load-bearing claim maps to a source, approved assumption, or explicit gap. |
| Decision and review record | Buyer owner and delivery lead | The selected option, rationale, owner, stop condition, and approval status are visible. |
| Section acceptance check | Evaluator-readiness reviewer | Each output meets its stated acceptance condition and unresolved checks are not presented as passed. |

## Capability and Permission Boundaries

This skill may read supplied tender, discovery, architecture, commercial, security, and operating evidence and draft proposal artefacts within the authorised workspace. It must not publish, send, certify compliance, accept contractual terms, change production systems, spend funds, or disclose confidential evidence without explicit authority. Review and analysis remain read-only by default.

## Degraded Mode

If files, current legal or technical evidence, calculation tools, network access, or reviewers are unavailable, produce the narrowest useful qualified draft. Label assumptions and checks as **not assessed**, omit unsupported assurances or figures, and state the exact evidence and owner needed to complete the work. An unavailable check never becomes a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Usage variability | Model P50, P90, and abuse cases before fixing allowance and overage terms | Negative gross margin or buyer bill shock |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

When inference cost and usage distribution are uncertain, price a bounded allowance with measured true-up and model-tier rules; do not offer an unlimited fixed fee without cost evidence.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/ai-on-saas-pricing-models-reference.md](../../profiles-sectors/references/ai-on-saas-pricing-models-reference.md) — pattern library, worked examples, clauses.
- [../references/saas-pricing-models-reference.md](../../profiles-sectors/references/saas-pricing-models-reference.md) — base SaaS pricing patterns.
- [../saas-pricing-and-packaging-proposal/SKILL.md](../../saas-proposals/saas-pricing-and-packaging-proposal/SKILL.md) — base SaaS pricing skill.
- [../ai-on-saas-business-case-and-roi/SKILL.md](../ai-on-saas-business-case-and-roi/SKILL.md) — cost stack input.
- [../10-financial-proposal/SKILL.md](../../pipeline/10-financial-proposal/SKILL.md) — financial proposal placement.
- [../premium-pricing-and-value-defense/SKILL.md](../../strategy-positioning/premium-pricing-and-value-defense/SKILL.md) — premium-fee defence.
