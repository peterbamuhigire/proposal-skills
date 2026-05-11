---
name: saas-implementation-methodology
description: Use when writing the Methodology section of a SaaS implementation or SaaS product-development proposal. Provides the end-to-end methodology covering control plane, application plane, tenant isolation, data partitioning, observability, billing integration, cost attribution, onboarding automation, security hardening, pilot-to-cutover, customer-success, and value realisation. Drops into proposal `06-methodology` for SaaS engagements.
---

# SaaS Implementation Methodology
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The engagement is a SaaS implementation, a SaaS migration from installed software, a multi-tenant platform build, or a SaaS product-development bid.
- The Methodology section must demonstrate SaaS architectural literacy beyond multi-customer software.
- The buyer is regulated, enterprise, or premium-priced and a generic implementation methodology will not pass.

## Do Not Use When

- The engagement is non-SaaS software development (use `06-methodology/` directly).
- The engagement is a pure consulting assignment without software delivery.

## Required Inputs

- ToR / RFP and any architectural context.
- The buyer's vertical and regulatory situation.
- Discovery outputs (pain chain, ICP, Critical Event, decision process).
- The integration landscape (core systems, identity, payments, regulator reporting).
- Tenant-model expectations (number of tenants, variation across tenants, isolation expectations).
- Engagement length and any phasing constraints.

## Workflow

1. Open the Methodology section with the engine's standard P-I-P phase pattern.
2. State the Conceptual Approach: two-plane mental model, tenant isolation as a regulatory and commercial decision, engineered adoption.
3. Apply the Standard Phases:
   - Phase 1: Inception, Discovery, and SaaS Strategy Gate.
   - Phase 2: Control Plane Build.
   - Phase 3: Application Plane Build.
   - Phase 4: Trust, Compliance, and Operations Hardening.
   - Phase 5: User Acceptance, Pilot, and Go-Live.
   - Phase 6: Adoption and Value Realisation.
   - Phase 7: Optimisation and Ongoing Operations.
4. Inside each phase, apply P-I-P: open with why this phase is right for this buyer, middle with specific actions/artefacts, close with deliverable and decision.
5. Populate the Deliverables Summary table.
6. Populate the Risk Register from `saas-risk-register-for-proposals.md`.
7. Cross-link to the architecture credibility block, the trust and compliance section, the customer success engagement package, and the lifecycle communications program where each applies.
8. Map to the ToR's phase naming (Inception / Design / Build / Test / Deploy / Support) if required.

## Quality Standards

- Control plane and application plane are explicitly named.
- Tenant isolation model is decided in Phase 1 by Architecture Decision Record.
- Per-tenant cost attribution is designed from day one.
- Adoption is engineered through customer success + lifecycle communications.
- Two-of-everything for client-side critical operating roles by go-live.
- Each phase has at least one named deliverable; deliverables have acceptance criteria.

## Anti-Patterns

- "Multi-tenant architecture" stated without naming an isolation model.
- Onboarding described as operations-assisted as if that were a feature.
- Cost attribution treated as something to address "later."
- Adoption treated as training, not engagement.
- Methodology that does not name the two planes.
- Per-customer operations mindset reproduced in the proposed operating model.

## Outputs

- Methodology section for SaaS implementation engagements.
- Deliverables Summary table.
- Standard Phases with P-I-P pattern applied.
- Cross-links to architecture credibility block, trust and compliance section, customer success package, lifecycle communications, and risk register.

## AI Overlay — When AI Features Are Built Into the SaaS

When the engagement delivers AI features inside the SaaS product (RAG, copilots, agents, AI analytics, AI-assisted decisioning), use `../ai-on-saas-combined-methodology/SKILL.md` instead of this skill, or layer it on top. The AI overlay introduces a third plane (the AI plane: model gateway, model registry, eval harness, RAG indexes per tenant, red-team harness, drift watch) alongside the control and application planes; introduces AI workstreams in every phase (golden-dataset + threshold spec in Phase 1; model gateway + eval CI in Phase 2; AI feature build with abstain logic in Phase 3; red-team + hallucination SLO in Phase 4; AI eval acceptance gate in Phase 5; drift watch in Phase 6; quarterly red-team and eval refresh in Phase 7); and introduces AI-specific acceptance criteria (golden-set pass, hallucination ceiling, abstain-correctness, cost-per-call, tenant-isolation probe pass). See also `../references/ai-on-saas-methodology-blocks.md`.

## References

- `../references/saas-implementation-methodology-blocks.md` — reusable Methodology section content.
- `../references/ai-on-saas-methodology-blocks.md` — AI-on-SaaS methodology overlay.
- `../ai-on-saas-combined-methodology/SKILL.md` — companion skill when AI features are built into the SaaS.
- `../references/saas-multi-tenant-architecture-block.md` — architecture credibility paragraphs.
- `../references/saas-trust-and-compliance-section-template.md` — trust section structure.
- `../references/saas-customer-success-engagement-package.md` — Phase 6 detail.
- `../references/saas-lifecycle-email-program-proposal-template.md` — adoption communications.
- `../references/saas-risk-register-for-proposals.md` — risk entries.
- `../references/saas-mutual-action-plan-template.md` — phase orchestration through MAP.
- `../06-methodology/SKILL.md` — methodology section discipline.
- `../saas-multi-tenant-architecture-credibility-block/SKILL.md` — companion skill for architectural literacy.
