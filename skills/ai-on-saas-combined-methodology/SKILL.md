---
name: ai-on-saas-combined-methodology
description: Use when the engagement simultaneously delivers a multi-tenant SaaS product AND its AI features (RAG, copilots, agents, AI analytics, AI-assisted workflows). Provides the combined methodology — phases, gates, deliverables, and acceptance criteria — that interleaves the SaaS workstreams (control plane, application plane, tenant isolation, observability, billing) with the AI workstreams (eval harness, model gateway, RAG indexes per tenant, red-team, hallucination SLO, model lifecycle). Headline skill of the AI-on-SaaS family. Drops into proposal `06-methodology` for AI-on-SaaS engagements.
---

# AI-on-SaaS Combined Methodology
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The deliverable is a multi-tenant SaaS product that contains AI features built into the product.
- The buyer expects investor-grade or board-grade rigour: AI ROI that survives a sceptical CFO, eval evidence that survives a sceptical CTO, procurement answers that survive a sceptical CISO.
- The Methodology section must demonstrate simultaneous SaaS literacy (control plane, tenant isolation, cost attribution) and AI literacy (eval harness, model gateway, hallucination SLO, red-team).
- The engagement faces AI-specific regulators (EU AI Act, Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U guidance, Rwanda AI Policy, sectoral rules).
- A generic SaaS implementation methodology or a generic AI methodology will not pass evaluator scrutiny.

## Do Not Use When

- The engagement is a SaaS implementation with no AI features — use `saas-implementation-methodology` instead.
- The engagement is generic AI strategy or AI proof-of-concept with no SaaS / multi-tenant layer — use `ai-transformation-proposal` instead.
- The engagement is a pure consulting assignment without software delivery.

## Required Inputs

- ToR / RFP with the AI scope (use cases, tenants, regulators, languages).
- Discovery outputs from `ai-on-saas-discovery-and-qualification`.
- Tenant model expectations (number of tenants, variation, regulator stance, residency).
- AI feature inventory (RAG, copilot, agent, analytics, decisioning, generation) with the workflow each one sits inside.
- Hallucination tolerance per use case (zero-tolerance, low-tolerance, advisory).
- Eval-data availability per tenant or per regulator.
- Model-provider posture (single provider, multi-provider, sovereign / on-prem).
- Buyer's AI maturity level (no AI / experimenting / scaling).
- Engagement length and phasing constraints.

## Workflow

1. Open the Methodology with the **Three-Plane Mental Model** paragraph: control plane, application plane, and **AI plane** (model gateway, eval harness, RAG indexes per tenant, model registry, red-team harness). The AI plane is named and resourced as a discipline alongside the other two, not buried inside the application plane.
2. State the **Conceptual Approach** paragraph: tenant isolation extends to AI artefacts; eval is engineered before models are chosen; AI cost attribution is designed from day one; AI adoption is engineered, not hoped for; the agency operates a **Responsible-AI commitment** (`ai-on-saas-risk-and-responsible-ai`).
3. Apply the **Standard Phases**. Each phase carries SaaS workstreams and AI workstreams in parallel, gated at the same time so that an AI deficiency cannot be hidden behind SaaS progress (and vice versa):
   - Phase 1: Inception, Discovery, and AI-on-SaaS Strategy Gate.
   - Phase 2: Control Plane Build + AI Plane Foundation.
   - Phase 3: Application Plane Build + AI Feature Build.
   - Phase 4: Trust, Compliance, AI Safety, and Operations Hardening.
   - Phase 5: UAT, AI Eval Acceptance, Pilot, and Go-Live.
   - Phase 6: Adoption, Value Realisation, and AI Drift Watch.
   - Phase 7: Optimisation, Eval Refresh, and Ongoing Operations.
4. Inside each phase, apply P-I-P (Premise – Implementation – Proof): open with why this phase is right for this buyer; middle with specific actions, artefacts, and gates; close with the deliverable and the decision the buyer makes at the gate.
5. Populate the **Deliverables Summary** table — every AI deliverable has an acceptance criterion that is **binary and evaluator-checkable**, not "AI-quality is good".
6. Populate the **Risk Register** from `ai-on-saas-risk-register-for-proposals.md`. Include the AI risks the buyer's CISO will look for: model risk, hallucination liability, prompt injection, data leakage into model providers, sub-processor exposure, regulatory shift, vendor lock-in to a single model family, training-data contamination, drift.
7. Populate the **Eval Strategy** subsection: golden dataset(s), eval metric(s) with thresholds, LLM-as-judge + human-in-the-loop arrangement, regression harness in CI, drift watch in production.
8. Populate the **Model Lifecycle** subsection: model selection criteria, model gateway, model registry, retraining / re-prompting cadence, deprecation, fall-back model, region routing.
9. Populate the **Tenant AI Isolation** subsection: per-tenant RAG indexes, per-tenant prompt context, per-tenant eval cohorts, per-tenant cost attribution for AI usage, per-tenant model preference where the buyer offers tier-based model selection.
10. Cross-link to the architecture credibility block, the trust and compliance section, the customer success engagement package, the lifecycle communications program, and the Responsible-AI commitment.
11. Map to the ToR's phase naming (Inception / Design / Build / Test / Deploy / Support) if required, preserving the AI workstream content under whatever phase names the buyer uses.

## Quality Standards

- Three planes are named — control plane, application plane, AI plane — each with its own deliverables.
- Tenant isolation model is decided in Phase 1 by ADR; the ADR explicitly covers AI artefacts (RAG index per tenant or shared with logical isolation; prompt context; eval cohorts).
- Eval is engineered **before** model selection; golden datasets and metric thresholds exist as Phase 1 deliverables.
- AI cost attribution is designed from day one — tokens, model calls, and embedding generation are attributed per tenant per call.
- Adoption is engineered through customer success + lifecycle communications + AI-mindset change management (`ai-on-saas-change-management-and-adoption`).
- Each phase has at least one binary, evaluator-checkable AI deliverable (golden-set pass rate ≥ X, hallucination rate ≤ Y, p95 latency ≤ Z ms, cost-per-call ≤ $W).
- Responsible-AI commitment is named, sectioned, and signed by a named accountable role.
- Two-of-everything for client-side critical AI operating roles by go-live (eval owner, prompt owner, AI safety owner, model-gateway operator).

## Anti-Patterns

- "Multi-tenant AI architecture" stated without naming an isolation model for RAG indexes, prompt context, and eval cohorts.
- Eval mentioned only as "we will evaluate the model" — no golden set, no metric, no threshold, no cadence.
- Hallucination treated as a UX issue ("we will display a disclaimer") instead of an engineered ceiling with abstain logic.
- Model selection committed in the proposal ("we will use GPT-4o") with no fallback, no gateway, no model-agnosticism, no regulator-driven region routing.
- Tokens treated as an undifferentiated cloud cost instead of attributed per tenant per call.
- AI cost attribution treated as something to address "later."
- "Responsible AI" as a single sentence instead of a section with a named owner.
- Per-customer AI operating mindset (a separate eval per customer) reproduced as if it were a feature; or the opposite, a single eval for all tenants in a regulated vertical.
- AI workstream collapsed into the application plane build, hidden from the gate review.

## Outputs

- Methodology section for AI-on-SaaS engagements, drop-in ready for proposal `06-methodology`.
- Three-Plane Mental Model paragraph.
- Conceptual Approach paragraph.
- Standard Phases with P-I-P pattern, each carrying parallel SaaS and AI workstreams.
- Deliverables Summary table with binary AI acceptance criteria.
- Eval Strategy subsection.
- Model Lifecycle subsection.
- Tenant AI Isolation subsection.
- Risk Register entries (link to `ai-on-saas-risk-register-for-proposals.md`).
- Responsible-AI commitment hook (link to `ai-on-saas-responsible-ai-commitment.md`).
- ToR phase-name mapping where required.

## References

- `../references/ai-on-saas-methodology-blocks.md` — reusable Methodology section content.
- `../references/ai-on-saas-risk-register-for-proposals.md` — risk entries for AI-on-SaaS.
- `../references/ai-on-saas-responsible-ai-commitment.md` — Responsible-AI section template.
- `../references/ai-on-saas-trust-and-compliance-section-template.md` — Trust and Compliance section for AI-on-SaaS.
- `../references/ai-on-saas-metrics-glossary.md` — eval, hallucination, abstain, citation, cost-per-call definitions.
- `../references/ai-on-saas-poc-scoping-template.md` — AI POC with binary eval criteria.
- `../references/saas-implementation-methodology-blocks.md` — the SaaS methodology this skill extends.
- `../references/saas-multi-tenant-architecture-block.md` — tenant isolation that AI artefacts must respect.
- `../06-methodology/SKILL.md` — methodology section discipline.
- `../saas-implementation-methodology/SKILL.md` — companion SaaS methodology.
- `../ai-transformation-proposal/SKILL.md` — generic AI strategy where there is no SaaS layer.
- `../ai-on-saas-discovery-and-qualification/SKILL.md` — discovery inputs to this methodology.
- `../ai-on-saas-poc-and-pilot-scoping/SKILL.md` — POC inside Phase 1.
- `../ai-on-saas-risk-and-responsible-ai/SKILL.md` — risk register and Responsible-AI commitment.
- `../ai-on-saas-team-composition/SKILL.md` — staffing that this methodology assumes.
