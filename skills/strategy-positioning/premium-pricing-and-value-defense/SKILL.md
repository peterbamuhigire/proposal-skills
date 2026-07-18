---
name: premium-pricing-and-value-defense
description: Use when pricing or defending premium consulting, software, AI, website, transformation, support, or service-design proposals where fees must be tied to value, risk reduction, seniority, assurance, and measurable outcomes.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Premium Pricing and Value Defense
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The bid should not compete on the cheapest compliant price.
- The proposal needs value-based commercial logic, options, assumptions, or negotiation language.
- A client may challenge price, compare against low-cost alternatives, or ask for discounts.
- The financial proposal must reflect senior expertise, quality gates, delivery risk, support, or total cost of ownership.

## Domain Method

1. Identify the economic value at stake: revenue, cost, time, compliance, service quality, risk, reputation, continuity, or capability.
2. Build the value stack before the price: outcomes, avoided cost, speed, assurance, seniority, quality, adoption, and sustainability.
3. Price from delivery drivers: effort, seniority, risk, client review cycles, complexity, tools, licences, support, and governance.
4. Create options where useful: essential, recommended, and enhanced, with clear trade-offs and acceptance criteria.
5. Defend fees by explaining what lower-cost approaches remove: discovery, QA, senior review, adoption, support, documentation, or risk controls.
6. Handle price objections by comparing price with total cost, cost of delay, rework risk, adoption failure, and long-term ownership.
7. Use premium commercial writing standards when fee logic must appear in cover letters, summaries, case studies, commercial documents, or public positioning.

## Quality Standards

- Premium value must be evidenced, not asserted.
- Do not bury material work inside vague lump sums.
- Do not discount without changing scope, payment terms, timeline, or assurance level.
- Keep commercial language factual and evaluator-friendly.

## Existing Deliverables

- Premium fee rationale.
- Commercial options and trade-off language.
- Price-objection response.
- Financial proposal assumptions and exclusions.

## SaaS Lens

For SaaS implementation and SaaS product-development engagements, the value defence anchors on different commercial logic:

- **Internal-Use SaaS** (client adopts SaaS to run operations): defend with five-year TCO comparison vs on-premise / legacy, time-to-value reduction, and risk-reduction quantification (compliance, outage, breach, audit, key-person).
- **Resale SaaS** (client builds or implements SaaS to sell to its own customers): defend with unit economics — CAC payback, LTV:CAC, gross margin, net dollar retention, Rule of 40 (investor-grade buyers only), magic number, professional services attach rate (PSAR).
- **Commercial options**: subscription, usage-based, hybrid, enterprise tiering, outcome-based, capacity-based. Each option carries different risk-and-cost shape for the agency.
- **Pricing structure inside the financial proposal**: never bundle customer success, lifecycle communications, or trust-and-compliance work invisibly inside the implementation fee — they are named workstreams that defend the premium.
- **Trade discipline**: in BAFO, trade scope, term, payment milestones, or assurance level — never pure discount on a properly priced SaaS engagement.

## AI-Agent Lens

When the engagement is agentic, the value defence has agent-specific levers that do not exist in generic consulting or SaaS:

- **Outcome pricing as premium defence** — gain-share (Pattern B) or success-fee (Pattern F) demonstrates skin-in-the-game and defends a premium because the agency carries the autonomy-ramp risk. Outcome pricing is not a discount; it is the agency saying "we will earn our fee against your business result". Use [ai-agent-success-fee-and-outcome-pricing](../../ai-agent-commercial/ai-agent-success-fee-and-outcome-pricing/SKILL.md).
- **Service credits as real value** — the SLA Class credit schedule (Bronze / Silver / Gold / Platinum) is not boilerplate; it is the agency's commitment to give the buyer money back if it misses. Credits visible on the Monthly Statement defend the premium because the buyer can see, every month, the SLA being honoured. Use [ai-agent-sla-and-credit-schedule](../../ai-agent-commercial/ai-agent-sla-and-credit-schedule/SKILL.md).
- **Intervention credit as fairness** — the buyer does not pay full price when the human did the work. The Intervention Credit Clause translates the autonomy ramp into a fair invoice. This is a discriminator against vendors who quote per-resolution with no intervention sensitivity. Use [ai-agent-intervention-credit-and-abort-refund](../../ai-agent-commercial/ai-agent-intervention-credit-and-abort-refund/SKILL.md).
- **Abort-and-refund as honesty** — the agency offers a pro-rata exit if the agent fails the autonomy ramp, an irreversible incident occurs at agency fault, the regulator intervenes, or the model provider sustains outage. This commitment is the agency's most powerful premium defence: it shows the price is for the agent that works, not the agent that tries.
- **Vendor-cost-pass-through as discipline, not a tax** — the pass-through clause exists because agents fan out many model calls per task; an invisible provider hike is catastrophic. The clause is capped, evidenced, and notice-bound. It demonstrates commercial maturity, not nickel-and-diming. Use [ai-agent-vendor-cost-pass-through](../../profiles-sectors/references/ai-agent-vendor-cost-pass-through.md).
- **Autonomy-progression price-step** — the price falls as the agent matures. The buyer is not locked into immature-agent prices forever. This defends the premium at signature by promising better unit economics as autonomy proves out. Use [ai-agent-renewal-and-true-up](../../ai-agent-commercial/ai-agent-renewal-and-true-up/SKILL.md).
- **Premium SLA Class** (Gold / Platinum) — Platinum SLA is not a slide; it is kill-switch ≤ 30 seconds, audit-log completeness ≥ 99.9 %, intervention SLA ≤ 60 seconds 24x7, full Abort-and-Refund. The premium price recovers the cost of operating to that standard. Vendors who quote Platinum at Silver prices are not telling the truth.

In every agent commercial conversation, the premium is defended by **moving the buyer up the commercial-maturity stack** — from "per resolution, undefined" to a SLA-class, packaging-shape, credit-schedule, intervention-credit, abort-refund, pass-through, FX-corridor, renewal-mechanics conversation. The conversation is itself the differentiator.

## Do Not Use When

- Do not use this skill when a neighbouring specialist named in the description owns the primary decision; route there first and use this skill only as a supporting layer.
- Do not use it to invent buyer facts, evidence, legal positions, statutory rules, delivery capacity, or current external claims.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| scope, cost floor, buyer value, risk allocation, options, proof, and negotiation authority | Buyer, ToR, approved project record, accountable owner, or verified evidence source | Yes | Stop the affected decision, name the missing source, and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| pricing rationale, options, and concession guardrails | Buyer CFO, procurement, and commercial lead | Claims trace to supplied evidence; assumptions, owners, exclusions, decisions, and observable acceptance tests are explicit. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Decision and source trace for the output | Reviewer and release owner | Each load-bearing choice identifies its source, rationale, accountable owner, and any unassessed check. |

## Capability Contract

Default to read-only for analysis, critique, discovery, and review. Minimum capability is access to the supplied artefacts and permission to inspect or calculate relevant evidence. Edit only the requested working copy. Do not publish, send, spend, change production systems, certify compliance, make a statutory claim, or approve a commercial concession without explicit authority.

## Degraded Mode

If required files, interviews, finance doctrine, search evidence, calculation tools, network access, or specialist review are unavailable, return the narrowest useful qualified result. Mark unavailable checks as not assessed, separate facts from assumptions, and state what is needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Set price, option, or concession | Tie price to scope, seniority, assurance, measurable value, and reciprocal trade. | Discounting without changing value, scope, or risk. |
| Evidence conflicts or authority is absent | Stop the affected recommendation, record the conflict, and seek the named owner’s decision. | Invented facts or unauthorised commitments. |
| Evidence and approval are complete | Proceed within scope and retain the decision trace. | Irreproducible approval or scope drift. |

## Workflow

1. Confirm the consumer, decision, neighbouring-skill route, authority, and required inputs; stop if the primary route or accountable owner is unknown.
2. Inspect supplied evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a load-bearing contradiction.
3. Apply the domain method and decision rules, preserving the repository’s proposal voice and specialist constraints.
4. Draft the contracted output with observable acceptance conditions and an evidence trace.
5. Review alignment with scope, work plan, team, pricing, risk, and dependent proposal sections; recover by revising the affected choice and rerunning the check.
6. Run the critical-analysis and anti-slop gates; block release on unsupported claims, failed safety or finance gates, or an F slop grade.

## Quality Standards

- Every load-bearing claim is verified or explicitly qualified, and the output distinguishes fact, assumption, recommendation, and commitment.
- Scope, method, work plan, staffing, pricing, risks, dependencies, and acceptance conditions remain mutually consistent.
- The output preserves domain constraints, names accountable owners, covers failure paths, and blocks unsupported or unauthorised promises.
- British English and the repository’s East African professional tone are used unless the buyer requires another standard.
- The critical-analysis and anti-slop gates pass before release, with no unassessed check represented as passed.

## Anti-Patterns

- Inventing a buyer fact or proof point. Fix: cite the supplied source or mark the statement as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and name the evidence needed to resume.
- Copying a neighbouring skill’s method without routing. Fix: use the specialist for the primary decision and retain only the supporting layer here.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: state an observable measure, evidence record, and decision owner.
- Adding premium or technical claims without delivery capacity. Fix: reconcile the claim with named people, time, budget, dependencies, and authority.

## Worked Example

Procurement asks for 15% off. Offer the reduction only with a narrower workshop count or longer commitment, and show the retained assurance obligations.

<!-- dual-compat-end -->

## References

- [premium-rate-justification-framework](../../profiles-sectors/references/premium-rate-justification-framework.md) - premium fee proof ladder and commercial options.
- [ai-agent-pricing-exhibit-template](../../profiles-sectors/references/ai-agent-pricing-exhibit-template.md) - agent pricing exhibit (premium structure).
- [ai-agent-sla-class-table](../../profiles-sectors/references/ai-agent-sla-class-table.md) - agent SLA class table.
- [ai-agent-outcome-pricing-clauses](../../profiles-sectors/references/ai-agent-outcome-pricing-clauses.md) - outcome-pricing structures.
- [ai-agent-pricing-and-packaging-proposal](../../ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md) - agent pricing patterns.
- [ai-agent-sla-and-credit-schedule](../../ai-agent-commercial/ai-agent-sla-and-credit-schedule/SKILL.md) - agent SLA class.
- [ai-agent-success-fee-and-outcome-pricing](../../ai-agent-commercial/ai-agent-success-fee-and-outcome-pricing/SKILL.md) - agent outcome-pricing.
- [ai-agent-intervention-credit-and-abort-refund](../../ai-agent-commercial/ai-agent-intervention-credit-and-abort-refund/SKILL.md) - intervention credit.
- [ai-agent-renewal-and-true-up](../../ai-agent-commercial/ai-agent-renewal-and-true-up/SKILL.md) - agent renewal mechanics.
- [proposal-objection-handling](../../profiles-sectors/references/proposal-objection-handling.md) - ethical responses to pricing and risk objections.
- [saas-pricing-models-reference](../../profiles-sectors/references/saas-pricing-models-reference.md) - subscription, usage, hybrid, tiering, expansion, freemium, paid trial, price-increase clauses.
- [saas-business-case-and-roi-template](../../profiles-sectors/references/saas-business-case-and-roi-template.md) - TCO vs on-prem (Flavour A) and unit economics (Flavour B).
- [saas-metrics-glossary-for-proposals](../../profiles-sectors/references/saas-metrics-glossary-for-proposals.md) - vocabulary for investor-grade conversations.
- [saas-objection-handling-playbook](../../profiles-sectors/references/saas-objection-handling-playbook.md) - price, risk, timeline, vendor lock-in, build-in-house responses.
- [premium-commercial-writing](../../writing-content/premium-commercial-writing/SKILL.md) - turns value defence into clear, proof-led, premium-fee-worthy prose.
- [10-financial-proposal](../../pipeline/10-financial-proposal/SKILL.md) - financial proposal owner and costing discipline.
- [premium-client-proposal-strategy](../premium-client-proposal-strategy/SKILL.md) - executive and premium-buyer proposal positioning.
- [saas-pricing-and-packaging-proposal](../../saas-proposals/saas-pricing-and-packaging-proposal/SKILL.md) - SaaS pricing and packaging skill.
- [saas-business-case-and-roi-modeling](../../saas-proposals/saas-business-case-and-roi-modeling/SKILL.md) - SaaS business case skill.
