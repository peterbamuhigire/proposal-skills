---
name: saas-business-case-and-roi-modeling
description: Use when a SaaS implementation or product-development proposal needs a CFO-grade business case covering TCO, time to value, payback, NPV, retention, or unit economics; use the AI-on-SaaS ROI skill when model and evaluation costs materially affect value.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Business Case and ROI Modeling
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The buyer is CFO-aware, board-overseen, donor-funded, or investor-backed.
- The proposal must defend a premium implementation fee against alternatives (cheaper bidder, build-in-house, do-nothing).
- The procurement framework requires a separate business case or financial justification annex.
- The agency proposes a phased engagement where each phase must justify the next.

## Do Not Use When

- The bid is purely price-based with no business-case requirement (use `10-financial-proposal/` only).
- The engagement is non-SaaS and the standard financial proposal applies.

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The buyer's segment (internal-use SaaS vs resale SaaS). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's vertical and any vertical-specific economics. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Baseline metrics (cost, time, revenue, quality, adoption, complaints, compliance) — request these in discovery if missing. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The cost structure of the proposed engagement (implementation fees, subscription fees, ongoing support). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The comparable alternatives the buyer will evaluate (incumbent renewal, point solution, build-in-house, do-nothing). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Decide which flavour applies: Internal-Use SaaS (anchor on TCO + TTV + risk reduction) or Resale SaaS (anchor on unit economics + NRR + Rule of 40).
2. For Internal-Use: populate value-at-stake table, five-year TCO comparison, time-to-value comparison, risk-reduction quantification, payback / NPV table, sensitivity.
3. For Resale: populate commercial model, unit economics plan, GTM investment plan, ARR build, path to profitability, sensitivity.
4. Build comparable engagements table — anonymised where required, named where reference permission exists.
5. Stress-test for buyer's CFO: identify the two or three assumptions that drive most of the NPV and present low / base / high cases.
6. Apply Six-Lens Value Claim to every load-bearing claim (Before / After / Capabilities / Mechanism / Outcome / Proof).
7. Decide which investor-grade vocabulary opt-ins (Rule of 40, magic number, burn multiple) are appropriate; suppress for non-investor buyers.
8. Produce the Executive Summary's Value at Stake paragraph and the Financial Proposal's price-defence narrative.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Every claim has a named baseline, target, value, and source.
- Sensitivity analysis shown for the two or three assumptions that drive most of the NPV.
- No single-point estimates without a confidence statement.
- Internal-control measurement language (A/B, holdout, propensity-matched) instead of industry-benchmark comparisons.
- British English, East African professional tone, currency stated explicitly on every table.

## Anti-Patterns

- "Payback within 12 months" with no mechanism stated. **Fix:** Show the baseline, benefit mechanism, adoption ramp, cost stack, cash-flow timing, and sensitivity that produce payback.
- LTV quoted without naming gross margin and churn assumptions. **Fix:** State ARPA, gross margin, logo or revenue churn, expansion, cohort period, and formula before using LTV.
- "Rule of 40" referenced for non-investable buyers. **Fix:** Use Rule of 40 only for an investor-grade resale SaaS case and explain the growth and margin inputs.
- TCO comparison that omits operating cost, attrition risk, or continuous-improvement cost on the build side. **Fix:** Include build, run, support, security, compliance, talent attrition, technical debt, and continuous-improvement cost in each alternative.
- "ARR" used loosely to include one-time and non-recurring revenue. **Fix:** Separate recurring subscription revenue from setup, services, hardware, and other one-time revenue.
- Benchmark comparisons used as the sole evidence. **Fix:** Use buyer baselines and controlled measurement as primary evidence; label external benchmarks as contextual.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Value at Stake table (for Executive Summary). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Five-year TCO comparison (for Internal-Use SaaS bids). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Unit economics plan (for Resale SaaS bids). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Payback and NPV table. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Sensitivity table. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Comparable engagements table. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Price-defence narrative for the Financial Proposal section. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Standalone business-case annex when required. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## AI Value and Cost-of-Tokens Addendum

When the SaaS contains AI features, the business case must add an AI Value Stack (cost-of-poor-quality reduction, productivity uplift with caveats, AI-tier upsell revenue, AI-driven activation / retention) **and** an AI Cost Stack (model and embedding cost, eval cost, AI operations, AI engineering payroll). The eval-margin (annual eval cost ÷ AI-feature gross margin) must be computed and discussed; cost-of-tokens must be presented at P50 / P90 / P99 tenant volume; three scenarios (downside / base / upside) replace any single hero ROI; FX is named where revenue is local and model costs are USD. See `../ai-on-saas-business-case-and-roi/SKILL.md` and `../references/ai-on-saas-business-case-template.md` for the full overlay with worked examples.

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
| Baseline evidence | Use ranges and label assumptions; request source data before claiming ROI | False precision and indefensible payback |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

If the buyer supplies transaction volumes but no verified labour-cost baseline, calculate operational volume transparently, leave labour savings unpriced, and show the missing rate and owner in the value-at-stake table.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/saas-business-case-and-roi-template.md](../../profiles-sectors/references/saas-business-case-and-roi-template.md) — the template this skill operationalises.
- [../references/ai-on-saas-business-case-template.md](../../profiles-sectors/references/ai-on-saas-business-case-template.md) — AI value + cost-of-tokens addendum.
- [../ai-on-saas-business-case-and-roi/SKILL.md](../../ai-on-saas-proposals/ai-on-saas-business-case-and-roi/SKILL.md) — companion skill for AI-on-SaaS engagements.
- [../references/saas-metrics-glossary-for-proposals.md](../../profiles-sectors/references/saas-metrics-glossary-for-proposals.md) — vocabulary.
- [../references/saas-pricing-models-reference.md](../../profiles-sectors/references/saas-pricing-models-reference.md) — commercial models for Resale SaaS.
- [../references/saas-win-themes-and-discriminators.md](../../profiles-sectors/references/saas-win-themes-and-discriminators.md) — converting business case into win themes.
- [../10-financial-proposal/SKILL.md](../../pipeline/10-financial-proposal/SKILL.md) — financial proposal section discipline.
- [../premium-pricing-and-value-defense/SKILL.md](../../strategy-positioning/premium-pricing-and-value-defense/SKILL.md) — premium fee defence overlay.
- [../critical-analysis-business-logic/SKILL.md](../../strategy-positioning/critical-analysis-business-logic/SKILL.md) — feasibility and achievability gate.
