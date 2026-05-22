# AI-on-SaaS Objection Handling Playbook

Objections specific to AI inside a multi-tenant SaaS, with calm, evidence-bearing replies. Pairs with `saas-objection-handling-and-competitive-displacement` and `proposal-objection-handling.md`. Use in sales conversations, written responses, evaluator Q&A, and proposal text.

Each objection is treated as a legitimate question, restated faithfully, then answered with a concrete commitment anchored elsewhere in the proposal.

## 1. Price Objections

**"Your AI tier is too expensive."**

> The AI-tier price reflects three identifiable cost layers: model and inference cost at projected production volume (P50 / P90 / P99 modelled per tenant), eval and red-team discipline (typically 2–8 % of feature cost, defending against the "demo well, fail in production" pattern), and operating cost for drift watch and incident response. The financial proposal separates these. We are willing to discuss a hybrid floor-and-overage structure, which moves the variable-cost risk to the heavy users without changing the per-call economics for the median tenant.

**"Why are we paying for tokens? Our competitor includes AI."**

> Competitors who bundle AI either subsidise it from licence revenue and will reprice on renewal, or meter it implicitly through silent rate-limits. We prefer transparent pricing because regulator-grade buyers prefer transparent pricing. Where bundling fits your usage profile, we can move you to an included-allowance model with overage above a stated ceiling.

**"Can you guarantee the price will not increase?"**

> Our price-increase clause is indexed and capped. The cap is the lower of (a) CPI in your billing country plus three percentage points, or (b) the weighted change in our underlying model-provider list prices plus a five-percent margin. Where the underlying price falls, we pass through the reduction at the next renewal.

## 2. Accuracy / Hallucination Objections

**"How do we know the AI will not be wrong?"**

> The AI is wrong some of the time, by design. Our commitment is a stated ceiling and an engineered abstain path. The ceiling is numeric — typically ≤ 2 % hallucination on the production-representative golden set for advisory copilots, ≤ 0.5 % for citation-grounded RAG. The abstain logic is a system behaviour, not a UX disclaimer. The user-facing experience makes the AI's confidence and citations visible. The eval is in CI — a deploy that drops below threshold does not ship.

**"What happens if the AI hallucinates and we are sued?"**

> Three layers of protection. First, the hallucination ceiling and abstain logic minimise occurrence. Second, the HITL design on high-stakes flows places a named, authorised human between the AI and the customer. Third, our professional indemnity cover and the contractual liability allocation address residual risk. We will agree liability language with your General Counsel and DPO before signature.

**"AI can be biased. How do you prevent that?"**

> Bias is measured per feature where the use case touches a protected class. Our golden datasets carry intentional sub-cohorts (gender, language, age band, region, channel) where relevant. The eval reports per-cohort metric performance, not only aggregate. A per-cohort drop below threshold blocks deploy. The Responsible-AI commitment names fairness as an engineered control with redress.

## 3. Vendor Lock-In Objections

**"What if your AI provider raises prices or goes out of business?"**

> Our production architecture uses a model gateway. Every AI feature is evaluated against at least two foundation-model providers on the same golden set, and a fallback route is in production. The eval is portable. If the primary provider raises prices, we route to fallback within hours, not weeks. The contract gives you contractual notice if the underlying provider's price moves materially.

**"We will be locked into your product."**

> The exit clauses in the MSA name data egress (tenant data, embeddings, prompts, eval logs, configurations) on a structured timeline at no per-byte fee. The data is exportable in open formats. Where AI features depend on prompts, the prompt library is exported. Where the buyer chooses sovereign-AI, the open-weight models we use remain available to you after exit.

## 4. Regulator Objections

**"What about the EU AI Act?"**

> Phase 1 of the engagement includes an AI Act tier assessment per feature. For features classified as high-risk, the conformity-assessment documentation is in scope. The methodology aligns to Articles 9, 10, 13, 14, 15 — risk management, data governance, logging, transparency, and human oversight. Where you serve EU customers, region routing keeps inference inside the EU.

**"What about Kenya NCAIS / Nigeria NAIS / South Africa AI policy / Uganda NITA-U / Rwanda AI Policy?"**

> Our Responsible-AI commitment maps to each. The principles each regulator publishes — accountability, transparency, fairness, safety, privacy, human oversight — are operationalised as named controls in the commitment. The compliance map names the regulator and the evidence per principle.

**"Will the regulator approve this?"**

> Where pre-launch regulator notification or approval is required, the engagement plans the dialogue with the regulator from Phase 1. We have produced regulator-ready evidence packs (DPIA, model cards, Responsible-AI commitment, sub-processor list, eval methodology) for similar engagements.

## 5. Ethics Objections

**"This is going to replace people. We are not comfortable with that."**

> The augment-vs-replace framing is agreed before user communications begin. Where the intent is to augment, the methodology designs HITL with named human authority. Where the intent is to replace a step, the framing is honest and the union / works-council consultation runs alongside the build where applicable. The redress mechanism is published. The Responsible-AI commitment is signed at SteerCo level and reviewed quarterly.

**"What if our customers find out we use AI?"**

> Transparency is part of our commitment. We help draft the customer-facing transparency document and the in-product disclosure. Buyers who treat AI as a secret incur reputational risk far greater than buyers who treat AI as a tool. The communications brief we produce in Phase 1 covers internal, leadership, and external audiences.

## 6. Jobs Objections

**"Will this lead to layoffs?"**

> The headcount-impact assessment is an explicit Phase 1 deliverable. Where the engagement augments, the impact is on workflow time, not headcount. Where the engagement replaces a step, the impact is on role mix — typically reallocation rather than reduction in well-designed engagements. The communications brief and the union / works-council consultation address the question directly. We do not write proposals that promise headcount reduction we cannot defend.

## 7. Ban / Existential-Risk Objections

**"What if AI gets banned in our market?"**

> The risk register names regulatory shift, including ban. The mitigation includes regional fallback, a kill-switch for affected features, and a sovereign-AI option. The model gateway permits us to route around banned providers in days, not months. The contract gives you the right to suspend or terminate AI features without penalty in the event of regulatory ban.

**"What if AI causes a public scandal in our sector?"**

> The Responsible-AI commitment, the redress mechanism, and the incident response runbook are exactly the controls that the regulator and the public expect after such an event. Buyers with a documented Responsible-AI posture survive sector-level scandals; buyers without one do not.

## Use of This Playbook

- Read the objection back faithfully before responding.
- Anchor every response in a section of the proposal — risk register, Responsible-AI commitment, financial proposal, methodology, procurement pack.
- Do not promise outcomes the methodology cannot deliver.
- Calm, specific, named-control language wins.

## Cross-References

- `proposal-objection-handling.md` — base objection patterns.
- `saas-objection-handling-playbook.md` — SaaS objections.
- `ai-on-saas-risk-register-for-proposals.md` — risks behind the answers.
- `ai-on-saas-responsible-ai-commitment.md` — commitment behind the answers.
- `ai-on-saas-pricing-models-reference.md` — pricing structures behind price answers.
