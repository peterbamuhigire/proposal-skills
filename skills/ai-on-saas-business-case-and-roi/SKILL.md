---
name: ai-on-saas-business-case-and-roi
description: Use when the AI-on-SaaS proposal must present an AI ROI that survives a sceptical CFO. Provides cost-of-poor-quality reduction, agent-productivity uplift with caveats, AI-tier upsell revenue, payback that accounts for token costs, eval-margin, and downside scenarios including regulator and hallucination liability. Extends `saas-business-case-and-roi-modeling` with the AI overlay (cost-of-tokens, eval-margin, AI uplift, payback, downside).
---

# AI-on-SaaS Business Case and ROI
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The proposal must present an AI business case to a CFO, board, or investment committee.
- The buyer has been promised "AI ROI" by previous vendors and is sceptical.
- The pricing rests on AI-tier upsell, AI-credit usage, or AI-driven efficiency.
- The buyer's CFO will challenge token cost, eval cost, hallucination liability, and downside scenarios.
- The investor-grade lens applies (Rule of 40, payback, NPV, sensitivity).

## Do Not Use When

- The business case is for a non-AI SaaS engagement (use `saas-business-case-and-roi-modeling`).
- The buyer is buying AI consulting only, not building AI into a SaaS product (use `ai-transformation-proposal`).

## Required Inputs

- Baseline operating metric per affected workflow (cycle time, error rate, cost per case).
- Volume of the affected workflow per month and per tenant.
- Cost of poor quality today (rework, escalation, refund, fine, churn).
- Headcount cost and ramp curve for the AI-augmented workflow.
- Token / model-call price for the candidate model providers (and the fallback).
- Eval set size, labelling cost, and refresh cadence.
- The AI-tier upsell hypothesis (price, attach rate, churn delta).
- The buyer's regulator exposure (downside).
- FX assumptions where relevant (KES, NGN, ZAR, UGX, RWF, USD billing).

## Workflow

1. Build the **AI Value Stack** for each AI feature: cost-of-poor-quality reduction, agent productivity uplift, revenue from AI-tier upsell, revenue from AI-driven activation / retention. Each component is sized with a baseline, a target, and a confidence band.
2. Build the **AI Cost Stack**: model-call cost (tokens × price), embedding cost, eval cost (labelling + LLM-as-judge calls + human review), red-team cost, drift-watch cost, AI engineering payroll, cloud compute (GPU rental, inference, vector store).
3. Compute the **Eval-Margin** (the cost of running the eval, expressed as a percentage of the AI feature's gross margin contribution). Eval-margin above 15–20 % is a flag; the feature is paying for its own marking.
4. Compute **Cost-of-Tokens per Tenant** at three volume levels (P50, P90, P99) so the proposal is honest about heavy-user economics.
5. Compute **AI Uplift with Caveats**. Never quote a single hero number. Quote three scenarios (downside, base, upside) with the caveats that move the case between scenarios (hallucination rate above ceiling, regulator delay, adoption shortfall, model price increase).
6. Compute **Payback** in months, accounting for token and eval costs (not just licence revenue).
7. Compute **NPV** over 36 months with the buyer's discount rate, and a **sensitivity** on token price (±30 %) and adoption rate (±20 percentage points).
8. Write the **Downside Scenarios**: (a) regulator changes tier classification; (b) hallucination liability event; (c) model-provider price increase or ban; (d) eval drift not caught; (e) AI-tier upsell flops; (f) sovereign-AI mandate. Each has a financial number and a mitigation that ties back to the methodology and Responsible-AI commitment.
9. Output the **AI Business Case Memo** in the buyer's preferred shape (CFO one-pager, board memo, investment-committee deck).

## Quality Standards

- The value stack and the cost stack are presented side by side; the net is computed transparently.
- Eval-margin is calculated and discussed; eval is not pretended to be free.
- Cost-of-tokens is at three volume levels.
- Three scenarios (downside, base, upside) are presented; no hero single-number ROI.
- Downside scenarios are named, sized, and mitigated.
- FX assumption is stated where AI costs are USD-denominated and revenue is local-currency.
- The discount rate used is the buyer's stated rate, not the agency's default.

## Anti-Patterns

- "AI will save you 30 %" with no scenario, no cost stack, no caveat.
- Token cost omitted because "it is a cloud cost."
- Eval cost omitted because "the model will be fine."
- Payback computed without the cost of running the model.
- AI-tier upsell modelled at 100 % attach rate.
- Hallucination liability treated as "we will display a disclaimer," not as a downside dollar figure.
- FX assumption left implicit when revenue is local and costs are USD.

## Outputs

- AI Value Stack table.
- AI Cost Stack table.
- Eval-Margin calculation.
- Cost-of-Tokens per Tenant table (P50, P90, P99).
- Three-scenario ROI table (downside, base, upside) with caveats.
- Payback (months) and NPV (36 months) with sensitivity.
- Downside Scenarios section with mitigations.
- AI Business Case Memo in the buyer's preferred shape.

## References

- `../references/ai-on-saas-business-case-template.md` — formulas, worked examples, FX handling.
- `../references/ai-on-saas-metrics-glossary.md` — definitions used in the case.
- `../references/saas-business-case-and-roi-template.md` — base SaaS business case template.
- `../saas-business-case-and-roi-modeling/SKILL.md` — base SaaS business case skill.
- `../ai-on-saas-pricing-and-packaging-proposal/SKILL.md` — pricing patterns that drive revenue inputs.
- `../ai-on-saas-risk-and-responsible-ai/SKILL.md` — risks that drive downside scenarios.
- `../10-financial-proposal/SKILL.md` — financial proposal placement.
- `../premium-pricing-and-value-defense/SKILL.md` — fee defence at the close.
