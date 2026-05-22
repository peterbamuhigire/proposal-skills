# AI-on-SaaS Methodology Blocks

Reusable Methodology section content for AI-on-SaaS engagements (multi-tenant SaaS + AI features). Pairs with `ai-on-saas-combined-methodology` and extends `saas-implementation-methodology-blocks.md` with the AI plane.

## Conceptual Approach (one to two pages)

Our approach to AI-on-SaaS engagements rests on four convictions:

1. **There are three planes, not two.** A SaaS implementation already has a control plane (tenant lifecycle, onboarding, identity, billing, observability) and an application plane (where the buyer's users do work). An AI-on-SaaS engagement adds a third — the **AI plane** — comprising the model gateway, model registry, per-tenant RAG indexes, eval harness, red-team harness, and drift watch. The AI plane is designed, built, tested, and operated as a discipline alongside the other two, not buried inside the application plane. Naming the AI plane explicitly is what separates a credible AI-on-SaaS methodology from "we will add AI to the SaaS."

2. **Tenant isolation extends to AI artefacts.** Cross-tenant data leakage in a RAG index, a prompt context, or an eval cohort is a security incident, not a feature gap. Per-tenant indexes, explicit tenant context in prompts, per-tenant eval cohorts where the use case demands it, and per-tenant cost attribution for AI usage are designed in Phase 1, not retrofitted.

3. **Eval is engineered before model selection.** Golden datasets, metric thresholds, and acceptance criteria exist as Phase 1 deliverables. Model selection then becomes evidence-based across at least two models, and the production architecture remains model-agnostic via the gateway. The opposite order — choose a model, then "evaluate" it — produces lock-in and unfalsifiable claims.

4. **AI adoption is engineered, not hoped for.** Trust-building (shadow → confirm → supervised → auto), human-in-the-loop design with named human authority, augment-vs-replace communications, and retraining-cadence communications are designed into the engagement from day one. An AI-on-SaaS engagement that succeeds technically but fails on adoption — or on trust — is a failed engagement.

## Standard Phases

### Phase 1 — Inception, Discovery, and AI-on-SaaS Strategy Gate (Weeks 1–3)

Carries SaaS and AI workstreams in parallel.

SaaS deliverables:
- Diagnosed pain chain and value-at-stake.
- Account map and decision process.
- Critical event named and timed.
- ADR draft for tenant model and isolation.
- Integration discovery; data residency and sub-processor map.
- Risk register and mutual action plan.

AI deliverables:
- AI use-case inventory with workflow-AI fit, hallucination tolerance, regulator exposure.
- Data readiness assessment for AI.
- Golden-dataset specification per AI feature.
- Eval metric and threshold table per feature.
- Model selection criteria and gateway architecture decision.
- Tenant AI isolation decision (per-tenant RAG vs shared with logical isolation).
- Responsible-AI commitment draft and accountable role named.

**Strategy gate**: the SteerCo signs off SaaS strategy AND AI strategy together. Failure of either blocks Phase 2.

### Phase 2 — Control Plane Build + AI Plane Foundation (Weeks 3–10)

SaaS workstream:
- Tenant onboarding automation; tenant management surface; identity model; billing integration; per-tenant observability; audit logging.

AI workstream:
- Model gateway with two-provider support and fallback routing.
- Model registry with version control.
- Eval harness with CI integration and threshold gates.
- Vector store with per-tenant index pattern.
- Embedding pipeline.
- Red-team harness skeleton.
- Drift-watch dashboards skeleton.

### Phase 3 — Application Plane Build + AI Feature Build (Weeks 4–14)

SaaS workstream:
- Workflow configuration; integrations; tenant context propagation; data partitioning; performance and load test under realistic multi-tenant patterns.

AI workstream (per AI feature):
- Prompt design and version control.
- RAG retrieval design with citation grounding.
- Abstain logic implementation and verification.
- Tool-call allowlist for agentic features.
- Eval against golden set with both candidate models.
- Latency and cost-per-call measurement at production volume profile.
- Tenant-isolation probe pack.

### Phase 4 — Trust, Compliance, AI Safety, and Operations Hardening (Weeks 10–16)

SaaS workstream:
- SAST / SCA / DAST; pen test; compliance evidence pack; BCDR; incident response.

AI workstream:
- Red-team probe execution and remediation.
- Hallucination SLO measurement and tuning.
- Sub-processor disclosure finalised.
- DPIA per high-risk AI feature.
- Conformity-assessment documentation where applicable.
- Model-card authored per feature.
- AI incident response runbook tested end-to-end.

### Phase 5 — UAT, AI Eval Acceptance, Pilot, and Go-Live (Weeks 14–20)

SaaS workstream:
- UAT entry gate; pilot cohort; 30-day pilot review; cutover with rollback.

AI workstream:
- AI eval acceptance gate: all metrics ≥ threshold; abstain-correctness verified; red-team pass; cost-per-call within target; tenant isolation verified.
- Trust-building staging confirmed (shadow → confirm → supervised → auto where in scope).
- Augment-vs-replace communications launched.
- Buyer-side AI operating roles trained-up (two-of-everything).

### Phase 6 — Adoption, Value Realisation, and AI Drift Watch (Weeks 18–34)

SaaS workstream:
- Customer success engagement; lifecycle communications launch; 30 / 60 / 90-day value reviews; QBR cadence established.

AI workstream:
- Daily drift watch on high-stakes features; weekly on others.
- Monthly eval refresh; quarterly golden-set refresh.
- AI Governance Forum monthly cadence.
- Quarterly Responsible-AI report.
- Redress-log review at the forum.

### Phase 7 — Optimisation, Eval Refresh, and Ongoing Operations (continuous)

SaaS workstream:
- Improvement backlog; quarterly tenant-cost-attribution review; annual tier-pricing review; security and compliance refresh.

AI workstream:
- Quarterly red-team; quarterly golden-set refresh; quarterly model-list review (deprecations, additions, pricing).
- Annual independent red-team.
- Annual Responsible-AI declaration to the buyer's board.
- Quarterly cost-per-call SLO review.

## Phase-Naming Mapping

If the ToR uses Inception / Design / Build / Test / Deploy / Support, map as follows:
- Inception → Phase 1.
- Design → Phase 1 close + Phase 2 start.
- Build → Phases 2 + 3.
- Test → Phase 4.
- Deploy → Phase 5.
- Support → Phases 6 + 7.

## Deliverables Summary — Sample Table

| Phase | SaaS deliverable | AI deliverable | Acceptance criterion |
|---|---|---|---|
| 1 | ADR (tenant model) | Eval threshold table; golden-set spec | SteerCo sign-off on both |
| 2 | Control plane MVP | Model gateway + registry + eval CI | Threshold-blocking deploy verified |
| 3 | Application plane workflows | AI feature with abstain logic | Both candidate models above threshold |
| 4 | Hardened security pack | Red-team pass + model cards + DPIAs | Zero critical findings; auditor-ready pack |
| 5 | Pilot cohort live | AI eval acceptance gate passed | All 5 exit criteria pass |
| 6 | QBR cadence | Drift watch + monthly eval refresh | First quarterly Responsible-AI report signed |
| 7 | Improvement backlog | Annual independent red-team | Board-level annual declaration |

## Quality Standards (Repeated for Drop-In)

- Three planes named.
- Tenant isolation extended to AI artefacts.
- Eval engineered before model selection.
- AI cost attribution from day one.
- Adoption engineered through trust-building staging.
- AI deliverables with binary, evaluator-checkable acceptance criteria.
- Responsible-AI commitment with named accountable role.
- Two-of-everything on AI operating roles by go-live.

## Cross-References

- `saas-implementation-methodology-blocks.md` — the SaaS methodology this extends.
- `saas-multi-tenant-architecture-block.md` — tenant isolation that AI must respect.
- `ai-on-saas-risk-register-for-proposals.md` — risks anchored to mitigations here.
- `ai-on-saas-responsible-ai-commitment.md` — commitment operationalised here.
- `ai-on-saas-metrics-glossary.md` — metric definitions used in acceptance criteria.
- `ai-on-saas-poc-scoping-template.md` — Phase 0 POC if required.
- `ai-on-saas-team-composition-template.md` — staffing this methodology assumes.
