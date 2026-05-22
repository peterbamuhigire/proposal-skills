---
name: saas-business-case-and-roi-modeling
description: Use when a SaaS implementation or SaaS product-development proposal needs a CFO-grade business case covering TCO vs on-premise, time to value, CAC payback, LTV uplift, retention uplift, ROI, NPV, sensitivity, and (for investor-grade buyers) Rule of 40 and magic number. Drives the Executive Summary's Value at Stake block and the Financial Proposal's price-defence narrative.
---

# SaaS Business Case and ROI Modeling
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The buyer is CFO-aware, board-overseen, donor-funded, or investor-backed.
- The proposal must defend a premium implementation fee against alternatives (cheaper bidder, build-in-house, do-nothing).
- The procurement framework requires a separate business case or financial justification annex.
- The agency proposes a phased engagement where each phase must justify the next.

## Do Not Use When

- The bid is purely price-based with no business-case requirement (use `10-financial-proposal/` only).
- The engagement is non-SaaS and the standard financial proposal applies.

## Required Inputs

- The buyer's segment (internal-use SaaS vs resale SaaS).
- The buyer's vertical and any vertical-specific economics.
- Baseline metrics (cost, time, revenue, quality, adoption, complaints, compliance) — request these in discovery if missing.
- The cost structure of the proposed engagement (implementation fees, subscription fees, ongoing support).
- The comparable alternatives the buyer will evaluate (incumbent renewal, point solution, build-in-house, do-nothing).

## Workflow

1. Decide which flavour applies: Internal-Use SaaS (anchor on TCO + TTV + risk reduction) or Resale SaaS (anchor on unit economics + NRR + Rule of 40).
2. For Internal-Use: populate value-at-stake table, five-year TCO comparison, time-to-value comparison, risk-reduction quantification, payback / NPV table, sensitivity.
3. For Resale: populate commercial model, unit economics plan, GTM investment plan, ARR build, path to profitability, sensitivity.
4. Build comparable engagements table — anonymised where required, named where reference permission exists.
5. Stress-test for buyer's CFO: identify the two or three assumptions that drive most of the NPV and present low / base / high cases.
6. Apply Six-Lens Value Claim to every load-bearing claim (Before / After / Capabilities / Mechanism / Outcome / Proof).
7. Decide which investor-grade vocabulary opt-ins (Rule of 40, magic number, burn multiple) are appropriate; suppress for non-investor buyers.
8. Produce the Executive Summary's Value at Stake paragraph and the Financial Proposal's price-defence narrative.

## Quality Standards

- Every claim has a named baseline, target, value, and source.
- Sensitivity analysis shown for the two or three assumptions that drive most of the NPV.
- No single-point estimates without a confidence statement.
- Internal-control measurement language (A/B, holdout, propensity-matched) instead of industry-benchmark comparisons.
- British English, East African professional tone, currency stated explicitly on every table.

## Anti-Patterns

- "Payback within 12 months" with no mechanism stated.
- LTV quoted without naming gross margin and churn assumptions.
- "Rule of 40" referenced for non-investable buyers.
- TCO comparison that omits operating cost, attrition risk, or continuous-improvement cost on the build side.
- "ARR" used loosely to include one-time and non-recurring revenue.
- Benchmark comparisons used as the sole evidence.

## Outputs

- Value at Stake table (for Executive Summary).
- Five-year TCO comparison (for Internal-Use SaaS bids).
- Unit economics plan (for Resale SaaS bids).
- Payback and NPV table.
- Sensitivity table.
- Comparable engagements table.
- Price-defence narrative for the Financial Proposal section.
- Standalone business-case annex when required.

## AI Value and Cost-of-Tokens Addendum

When the SaaS contains AI features, the business case must add an AI Value Stack (cost-of-poor-quality reduction, productivity uplift with caveats, AI-tier upsell revenue, AI-driven activation / retention) **and** an AI Cost Stack (model and embedding cost, eval cost, AI operations, AI engineering payroll). The eval-margin (annual eval cost ÷ AI-feature gross margin) must be computed and discussed; cost-of-tokens must be presented at P50 / P90 / P99 tenant volume; three scenarios (downside / base / upside) replace any single hero ROI; FX is named where revenue is local and model costs are USD. See `../ai-on-saas-business-case-and-roi/SKILL.md` and `../references/ai-on-saas-business-case-template.md` for the full overlay with worked examples.

## References

- `../references/saas-business-case-and-roi-template.md` — the template this skill operationalises.
- `../references/ai-on-saas-business-case-template.md` — AI value + cost-of-tokens addendum.
- `../ai-on-saas-business-case-and-roi/SKILL.md` — companion skill for AI-on-SaaS engagements.
- `../references/saas-metrics-glossary-for-proposals.md` — vocabulary.
- `../references/saas-pricing-models-reference.md` — commercial models for Resale SaaS.
- `../references/saas-win-themes-and-discriminators.md` — converting business case into win themes.
- `../10-financial-proposal/SKILL.md` — financial proposal section discipline.
- `../premium-pricing-and-value-defense/SKILL.md` — premium fee defence overlay.
- `../critical-analysis-business-logic/SKILL.md` — feasibility and achievability gate.
