---
name: ai-on-saas-combined-methodology
description: Use when one proposal must integrate multi-tenant SaaS delivery with RAG, copilots, agents, or AI analytics across shared phases and gates; use SaaS implementation methodology when the scope contains no AI feature.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI-on-SaaS Combined Methodology
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
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

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| ToR / RFP with the AI scope (use cases, tenants, regulators, languages). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Discovery outputs from `ai-on-saas-discovery-and-qualification`. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Tenant model expectations (number of tenants, variation, regulator stance, residency). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| AI feature inventory (RAG, copilot, agent, analytics, decisioning, generation) with the workflow each one sits inside. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Hallucination tolerance per use case (zero-tolerance, low-tolerance, advisory). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Eval-data availability per tenant or per regulator. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Model-provider posture (single provider, multi-provider, sovereign / on-prem). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Buyer's AI maturity level (no AI / experimenting / scaling). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Engagement length and phasing constraints. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

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


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

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

- "Multi-tenant AI architecture" stated without naming an isolation model for RAG indexes, prompt context, and eval cohorts. **Fix:** Specify tenant boundaries for retrieval indexes, prompt context, caches, logs, evaluation cohorts, and keys, then test cross-tenant denial.
- Eval mentioned only as "we will evaluate the model" — no golden set, no metric, no threshold, no cadence. **Fix:** Define the golden set, metric, threshold, owner, run cadence, and release-blocking regression rule.
- Hallucination treated as a UX issue ("we will display a disclaimer") instead of an engineered ceiling with abstain logic. **Fix:** Set a measured hallucination ceiling with grounding, abstention, escalation, and high-stakes human approval.
- Model selection committed in the proposal ("we will use GPT-4o") with no fallback, no gateway, no model-agnosticism, no regulator-driven region routing. **Fix:** Use a model gateway and evaluation-based selection with provider fallback, region routing, and documented exit criteria.
- Tokens treated as an undifferentiated cloud cost instead of attributed per tenant per call. **Fix:** Meter tokens and non-token AI resources per tenant, feature, model, and call so cost and abuse are visible.
- AI cost attribution treated as something to address "later." **Fix:** Design attribution, budgets, alerts, and commercial treatment before pilot pricing and architecture sign-off.
- "Responsible AI" as a single sentence instead of a section with a named owner. **Fix:** Create an auditable Responsible-AI commitment with a named lead, governance cadence, redress, transparency, and sign-off.
- Per-customer AI operating mindset (a separate eval per customer) reproduced as if it were a feature; or the opposite, a single eval for all tenants in a regulated vertical. **Fix:** Segment evaluations only where tenant risk or data warrants it while retaining a shared regression core and explicit cohort rules.
- AI workstream collapsed into the application plane build, hidden from the gate review. **Fix:** Keep AI as a visible workstream with its own data, evaluation, safety, cost, and release gates linked to both SaaS planes.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Methodology section for AI-on-SaaS engagements, drop-in ready for proposal `06-methodology`. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Three-Plane Mental Model paragraph. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Conceptual Approach paragraph. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Standard Phases with P-I-P pattern, each carrying parallel SaaS and AI workstreams. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Deliverables Summary table with binary AI acceptance criteria. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Eval Strategy subsection. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Model Lifecycle subsection. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Tenant AI Isolation subsection. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Risk Register entries (link to `ai-on-saas-risk-register-for-proposals.md`). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Responsible-AI commitment hook (link to `ai-on-saas-responsible-ai-commitment.md`). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| ToR phase-name mapping where required. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## Agent Overlay

When the AI features include autonomous agents (LLM systems that plan, call tools, decide, and act on the buyer's behalf), overlay the AI plane with the **eight-phase agent methodology** from `../ai-agent-methodology/SKILL.md`: Discover → Action-Catalogue Design → Architecture for Autonomy → Build → Shadow → Supervised → Agentic → Operate. The AI plane gains an Action Catalogue with reversibility classification, an autonomy commitment per action class, a kill-switch architecture with named authority and quarterly drill, an action audit log with 99 % completeness SLA, an agent-specific red-team catalogue, and a Responsible-AI Agent Commitment with a named Agent Safety Lead. Load `../ai-agent-methodology/SKILL.md` alongside this skill for agentic engagements.

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
| Cross-plane dependency | Gate AI work on tenant isolation, data readiness, and evaluation evidence | AI release before SaaS controls are ready |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

For a tenant-aware support copilot, sequence SaaS isolation controls, grounded-answer evaluation, human escalation, shadow use, supervised release, and operating monitoring; block progression at any failed plane gate.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/ai-on-saas-methodology-blocks.md](../../profiles-sectors/references/ai-on-saas-methodology-blocks.md) — reusable Methodology section content.
- [../references/ai-on-saas-risk-register-for-proposals.md](../../profiles-sectors/references/ai-on-saas-risk-register-for-proposals.md) — risk entries for AI-on-SaaS.
- [../references/ai-on-saas-responsible-ai-commitment.md](../../profiles-sectors/references/ai-on-saas-responsible-ai-commitment.md) — Responsible-AI section template.
- [../references/ai-on-saas-trust-and-compliance-section-template.md](../../profiles-sectors/references/ai-on-saas-trust-and-compliance-section-template.md) — Trust and Compliance section for AI-on-SaaS.
- [../references/ai-on-saas-metrics-glossary.md](../../profiles-sectors/references/ai-on-saas-metrics-glossary.md) — eval, hallucination, abstain, citation, cost-per-call definitions.
- [../references/ai-on-saas-poc-scoping-template.md](../../profiles-sectors/references/ai-on-saas-poc-scoping-template.md) — AI POC with binary eval criteria.
- [../references/saas-implementation-methodology-blocks.md](../../profiles-sectors/references/saas-implementation-methodology-blocks.md) — the SaaS methodology this skill extends.
- [../references/saas-multi-tenant-architecture-block.md](../../profiles-sectors/references/saas-multi-tenant-architecture-block.md) — tenant isolation that AI artefacts must respect.
- [../06-methodology/SKILL.md](../../pipeline/06-methodology/SKILL.md) — methodology section discipline.
- [../saas-implementation-methodology/SKILL.md](../../saas-proposals/saas-implementation-methodology/SKILL.md) — companion SaaS methodology.
- [../ai-transformation-proposal/SKILL.md](../../strategy-positioning/ai-transformation-proposal/SKILL.md) — generic AI strategy where there is no SaaS layer.
- [../ai-on-saas-discovery-and-qualification/SKILL.md](../ai-on-saas-discovery-and-qualification/SKILL.md) — discovery inputs to this methodology.
- [../ai-on-saas-poc-and-pilot-scoping/SKILL.md](../ai-on-saas-poc-and-pilot-scoping/SKILL.md) — POC inside Phase 1.
- [../ai-on-saas-risk-and-responsible-ai/SKILL.md](../ai-on-saas-risk-and-responsible-ai/SKILL.md) — risk register and Responsible-AI commitment.
- [../ai-on-saas-team-composition/SKILL.md](../ai-on-saas-team-composition/SKILL.md) — staffing that this methodology assumes.
