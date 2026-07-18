---
name: saas-pricing-and-packaging-proposal
description: Use when a SaaS proposal must choose and defend subscription, usage, hybrid, enterprise, freemium, trial, expansion, or price-review mechanics; use AI-on-SaaS pricing when model usage and provider-cost volatility drive the structure.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Pricing and Packaging Proposal
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The proposal includes the design of the client's resale SaaS commercial model.
- The agency must price its own implementation, customer-success, and managed-service fees in a structurally defensible way.
- The procurement requires a tiering proposal (Starter / Pro / Enterprise) or an expansion-path design.
- The bid competes against cheaper alternatives and the commercial structure must defend the premium.

## Do Not Use When

- The proposal is purely a fixed-fee response to a tightly defined ToR with no commercial-model design.
- The engagement is non-SaaS and the standard financial proposal applies.

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The buyer's segment shape (Enterprise / SMM / B2C). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's vertical and any sector-specific pricing realities. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The pricing model the buyer is currently using (if any) and its known weaknesses. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The competitive set the buyer's commercial model will face. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The expected expansion path (per-seat, per-volume, per-feature). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Select the primary pricing pattern: subscription, usage-based, hybrid, enterprise tier, outcome-based, capacity-based.
2. Design the tier ladder (Starter / Pro / Enterprise) with explicit gating per dimension (users, features, integrations, support, SLA, security, residency).
3. Design the expansion path: name the triggers, the conversation pattern, the owner on the agency side, and the measurable signal.
4. Decide on freemium vs paid trial using the decision matrix; default to paid trial when uncertain.
5. Design the price-increase clause: cadence, cap, communication, grandfathering, operational steps.
6. State currency, withholding tax, VAT, and payment-infrastructure realities for the buyer's jurisdiction.
7. Stress-test the commercial model: what does CAC payback look like? What gross margin does each tier sustain? Where does the model break under realistic adoption scenarios?
8. Produce the commercial-model section for the Methodology and the Financial Proposal.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Every tier has explicit feature, support, and SLA gating — not just a price difference.
- Expansion path is engineered, not optimistic.
- Price-increase clause includes grandfathering policy.
- Currency stated explicitly.
- Investor-grade vocabulary used only where the buyer is investor-aware.

## Anti-Patterns

- Single-tier pricing for a SaaS serving SMB through Enterprise. **Fix:** Segment tiers by buyer, value metric, capability, governance, service level, and expansion path from SMB to enterprise.
- Usage-based pricing without accurate metering or cost-control tools. **Fix:** Implement accurate metering, budgets, alerts, caps, anomaly handling, invoice evidence, and cost-to-serve monitoring before launch.
- Freemium that converts below 3%. **Fix:** Validate acquisition, activation, servicing cost, upgrade path, and conversion economics before choosing freemium; otherwise use a trial.
- Annual price increases above 8% without grandfathering. **Fix:** Use a named index or cost trigger, notice, cap, customer options, renewal treatment, and grandfathering policy.
- Hidden professional-services fees that make the headline misleading. **Fix:** Disclose implementation, migration, integration, training, support, and optional-service fees beside the headline price.
- "Custom enterprise pricing" with no public anchor. **Fix:** Publish a defensible enterprise starting point or pricing logic, included scope, variables, and approval rules.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Pricing-pattern selection with rationale. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Tier-ladder design. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Expansion-path design. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Freemium / paid-trial decision. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Price-increase clause text. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Commercial-model section for Methodology. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Financial Proposal narrative. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## AI Pricing Patterns

When the SaaS contains AI features, layer on the five AI pricing patterns: (a) bundled-in-tier with fair-use, (b) AI-tier-as-upsell (separate premium tier with AI), (c) included-allowance + overage, (d) pure usage credits, (e) hybrid floor + overage. Decide model-by-tier (cost-efficient model standard tier, frontier model in premium, sovereign / region-routed in regulated). Write fair-use with a number (not "reasonable use"), price-increase clause indexed and capped (CPI + 3 pp or model-provider list-price index plus margin floor), and FX clause where revenue is local and model costs are USD. Worked examples at P50 / P90 / P99 tenant volume confirm margin. See `../ai-on-saas-pricing-and-packaging-proposal/SKILL.md` and `../references/ai-on-saas-pricing-models-reference.md`.

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

If usage volume is uncertain, present a bounded base allowance and transparent overage rule with a review point; do not imply a fixed total cost without the buyer's volume evidence.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/saas-pricing-models-reference.md](../../profiles-sectors/references/saas-pricing-models-reference.md) — the reference this skill operationalises.
- [../references/ai-on-saas-pricing-models-reference.md](../../profiles-sectors/references/ai-on-saas-pricing-models-reference.md) — AI pricing patterns with worked examples and clauses.
- [../ai-on-saas-pricing-and-packaging-proposal/SKILL.md](../../ai-on-saas-proposals/ai-on-saas-pricing-and-packaging-proposal/SKILL.md) — companion skill for AI-on-SaaS engagements.
- [../references/saas-business-case-and-roi-template.md](../../profiles-sectors/references/saas-business-case-and-roi-template.md) — Resale SaaS Flavour B.
- [../references/saas-metrics-glossary-for-proposals.md](../../profiles-sectors/references/saas-metrics-glossary-for-proposals.md) — vocabulary.
- [../references/saas-gtm-motion-design-reference.md](../../profiles-sectors/references/saas-gtm-motion-design-reference.md) — pricing-experimentation register.
- [../premium-pricing-and-value-defense/SKILL.md](../../strategy-positioning/premium-pricing-and-value-defense/SKILL.md) — premium fee defence overlay.
- [../10-financial-proposal/SKILL.md](../../pipeline/10-financial-proposal/SKILL.md) — section discipline.
