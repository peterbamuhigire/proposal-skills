---
name: sales-discovery-and-objection-handling
description: Use when a proposal must infer buyer needs, sharpen discovery questions, qualify decision criteria, handle objections, frame commercial concerns, or prepare follow-up language for premium consulting, software, AI, website, support, or transformation offers.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Sales Discovery and Objection Handling
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The brief is incomplete and proposal assumptions must be clarified through discovery questions.
- The evaluator may resist price, timeline, staffing, technology, AI, risk, maintenance, or local-context assumptions.
- The proposal needs a stronger buyer conversation before submission, negotiation, presentation, or BAFO.
- The offer is premium-priced and must defend value without pressure tactics.

## Domain Method

1. Identify the decision path: sponsor, technical evaluator, procurement, finance, legal, users, and approvers.
2. Convert vague requirements into discovery questions about outcomes, current pain, decision criteria, constraints, budget logic, and success measures.
3. Qualify urgency and value: what happens if the client delays, under-scopes, or chooses the cheapest compliant option.
4. Map likely objections before drafting: price, risk, timeline, staffing, technology, data, maintenance, local delivery, or procurement compliance.
5. Answer objections ethically: acknowledge the concern, clarify the basis, reframe around value or risk, provide evidence, and define the practical trade-off.
6. Add follow-up language that makes the next step easy: clarification request, option comparison, presentation agenda, revised scope, or decision memo.

## Quality Standards

- Discovery questions must be useful to the proposal, not generic sales chatter.
- Objection responses must be factual, respectful, and grounded in scope, evidence, and trade-offs.
- Never create false urgency, fake scarcity, exaggerated social proof, or manipulative closing pressure.
- For premium offers, trade price only for scope, timeline, assurance level, payment terms, or included services.

## Existing Deliverables

- Discovery question list for the proposal team or client clarification.
- Objection map and response language.
- Negotiation and follow-up notes.
- Proposal edits that anticipate evaluator concerns.

## SaaS Lens

When the bid is a SaaS implementation or SaaS product-development engagement, layer on the SaaS-specific discovery and objection patterns:

- Articulate ICP, Critical Event, and Pain Chain (surface → operational → financial → strategic).
- Quantify Impact per Role: CEO, CFO, COO, CIO, CISO, sponsor, frontline user, customer/beneficiary, procurement.
- Map the Decision Process as consensus (multiple veto holders) or hierarchy (single owner); name individuals where known.
- Apply the MEDDPICC qualification gate (Metrics, Economic Buyer, Decision Criteria, Decision Process, Paper Process, Identify Pain, Champion, Competition) — never name the mnemonic in the client-facing proposal.
- Use trade discipline: never give a concession (discount, scope, terms) without receiving one (scope, term, references, payment, expansion commitment).
- Prepare competitive-displacement narratives for the realistic alternatives (incumbent renewal, point solution, build-in-house, free/open-source, do-nothing) — not vendor-by-vendor.

## AI-Agent Commercial Objections Lens

When the engagement is agentic and the procurement, legal, or finance team raises commercial objections, layer on the ten common agent procurement asks and the trade-not-give responses:

- "We don't pay for failed tasks" — Intervention Credit Clause.
- "We want a price floor below unit price" — Performance Corridor with Floor.
- "We want a price corridor on the SLA" — SLA Class Credit Schedule.
- "We want to audit the audit log" — Audit Rights with allowance and Evidence-Pack Fee.
- "We want a refund if the agent fails" — Abort-and-Refund Triggers (five named).
- "We want unlimited liability for agentic action" — General cap + Irreversible-Action Sub-Cap.
- "We want indemnity for regulator action" — Indemnity for named obligations only.
- "We want the model-cost increase absorbed by you" — Vendor-Cost-Pass-Through with Cap and Margin Floor.
- "We want unlimited audit-log retention" — 7 years + regulator-mandated.
- "We want to terminate without cause at any time, no refund clawback" — 90-day notice + pro-rata of unused subscription.

Every concession is traded for term, scope, volume guarantee, payment terms, SLA-class movement, or price. The agency does not give a default away under pressure; it trades it. Things the agency declines even at the cost of the deal: uncapped liability, open-ended regulator indemnity, no floor on per-resolution, full absorption of model-cost increases, refund as "good faith" instead of formula.

Use [ai-agent-procurement-objections-on-commercials](../../ai-agent-commercial/ai-agent-procurement-objections-on-commercials/SKILL.md) for the full ten-objection playbook and [ai-agent-commercial-objection-handling](../../profiles-sectors/references/ai-agent-commercial-objection-handling.md) for long-form responses.

## Do Not Use When

- Do not use this skill when a neighbouring specialist named in the description owns the primary decision; route there first and use this skill only as a supporting layer.
- Do not use it to invent buyer facts, evidence, legal positions, statutory rules, delivery capacity, or current external claims.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| brief, known stakeholders, decision process, assumptions, objections, and concession authority | Buyer, ToR, approved project record, accountable owner, or verified evidence source | Yes | Stop the affected decision, name the missing source, and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| discovery plan, assumption log, and objection responses | Account lead and proposal owner | Claims trace to supplied evidence; assumptions, owners, exclusions, decisions, and observable acceptance tests are explicit. |

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
| Ask, infer with qualification, respond, or escalate | Use decision impact and evidence risk to prioritise questions and trades. | Confidently guessing a buyer position. |
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

The timeline is fixed but data readiness is unknown. Ask who owns data acceptance and offer a phased start; do not promise the full rollout against an untested assumption.

<!-- dual-compat-end -->

## References

- [discovery-question-bank-for-proposals](../../profiles-sectors/references/discovery-question-bank-for-proposals.md) - reusable question bank for buyer discovery and proposal clarification.
- [ai-agent-commercial-objection-handling](../../profiles-sectors/references/ai-agent-commercial-objection-handling.md) - agent commercial objection playbook.
- [ai-agent-procurement-objections-on-commercials](../../ai-agent-commercial/ai-agent-procurement-objections-on-commercials/SKILL.md) - agent commercial objection skill.
- [proposal-objection-handling](../../profiles-sectors/references/proposal-objection-handling.md) - ethical objection handling for price, risk, timeline, staffing, technology, local context, support, AI, and procurement.
- [saas-discovery-question-bank](../../profiles-sectors/references/saas-discovery-question-bank.md) - SaaS-specific discovery (ICP, Critical Event, pain chain, impact per role, decision process).
- [meddic-and-command-of-message-for-saas](../../profiles-sectors/references/meddic-and-command-of-message-for-saas.md) - SaaS qualification overlay and Six-Lens Value Claim.
- [saas-objection-handling-playbook](../../profiles-sectors/references/saas-objection-handling-playbook.md) - SaaS-specific objection-handling library and trade discipline.
- [saas-vendor-vs-build-narrative](../../profiles-sectors/references/saas-vendor-vs-build-narrative.md) - build-vs-buy framing for SaaS displacement.
- [premium-pricing-and-value-defense](../premium-pricing-and-value-defense/SKILL.md) - value-based pricing and premium fee defence.
- [premium-client-proposal-strategy](../premium-client-proposal-strategy/SKILL.md) - premium buyer positioning and executive confidence.
- [saas-discovery-and-qualification](../../saas-proposals/saas-discovery-and-qualification/SKILL.md) - SaaS-specific discovery and qualification skill.
- [saas-objection-handling-and-competitive-displacement](../../saas-proposals/saas-objection-handling-and-competitive-displacement/SKILL.md) - SaaS-specific objection and displacement skill.
