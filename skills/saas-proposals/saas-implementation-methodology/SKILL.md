---
name: saas-implementation-methodology
description: Use when writing an end-to-end SaaS implementation methodology across control plane, application plane, tenant isolation, observability, billing, onboarding, cutover, and adoption; use the combined AI-on-SaaS methodology when AI features are in scope.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Implementation Methodology
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The engagement is a SaaS implementation, a SaaS migration from installed software, a multi-tenant platform build, or a SaaS product-development bid.
- The Methodology section must demonstrate SaaS architectural literacy beyond multi-customer software.
- The buyer is regulated, enterprise, or premium-priced and a generic implementation methodology will not pass.

## Do Not Use When

- The engagement is non-SaaS software development (use `06-methodology/` directly).
- The engagement is a pure consulting assignment without software delivery.

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| ToR / RFP and any architectural context. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's vertical and regulatory situation. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Discovery outputs (pain chain, ICP, Critical Event, decision process). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The integration environment (core systems, identity, payments, regulator reporting). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Tenant-model expectations (number of tenants, variation across tenants, isolation expectations). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Engagement length and any phasing constraints. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

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


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Control plane and application plane are explicitly named.
- Tenant isolation model is decided in Phase 1 by Architecture Decision Record.
- Per-tenant cost attribution is designed from day one.
- Adoption is engineered through customer success + lifecycle communications.
- Two-of-everything for client-side critical operating roles by go-live.
- Each phase has at least one named deliverable; deliverables have acceptance criteria.

## Anti-Patterns

- "Multi-tenant architecture" stated without naming an isolation model. **Fix:** Choose and justify silo, bridge, or pool isolation by data class and threat model, then specify enforcement and tests.
- Onboarding described as operations-assisted as if that were a feature. **Fix:** Automate repeatable onboarding and clearly label any temporary assisted step, owner, exit date, and scale limit.
- Cost attribution treated as something to address "later." **Fix:** Design tenant and feature metering, shared-cost allocation, budgets, alerts, and reporting before commercial launch.
- Adoption treated as training, not engagement. **Fix:** Treat adoption as a measured workstream covering workflow change, activation, behaviour, value, support, and reinforcement.
- Methodology that does not name the two planes. **Fix:** Separate control-plane and application-plane activities, dependencies, owners, gates, and acceptance evidence.
- Per-customer operations mindset reproduced in the proposed operating model. **Fix:** Replace bespoke per-customer operations with configuration, automation, standard runbooks, tenant-aware observability, and exception queues.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Methodology section for SaaS implementation engagements. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Deliverables Summary table. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Standard Phases with P-I-P pattern applied. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Cross-links to architecture credibility block, trust and compliance section, customer success package, lifecycle communications, and risk register. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## AI Overlay — When AI Features Are Built Into the SaaS

When the engagement delivers AI features inside the SaaS product (RAG, copilots, agents, AI analytics, AI-assisted decisioning), use `../ai-on-saas-combined-methodology/SKILL.md` instead of this skill, or layer it on top. The AI overlay introduces a third plane (the AI plane: model gateway, model registry, eval harness, RAG indexes per tenant, red-team harness, drift watch) alongside the control and application planes; introduces AI workstreams in every phase (golden-dataset + threshold spec in Phase 1; model gateway + eval CI in Phase 2; AI feature build with abstain logic in Phase 3; red-team + hallucination SLO in Phase 4; AI eval acceptance gate in Phase 5; drift watch in Phase 6; quarterly red-team and eval refresh in Phase 7); and introduces AI-specific acceptance criteria (golden-set pass, hallucination ceiling, abstain-correctness, cost-per-call, tenant-isolation probe pass). See also `../references/ai-on-saas-methodology-blocks.md`.

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
| Tenant architecture choice | Record isolation, context, data, observability, and cutover decisions before estimating | Non-credible plan or unsafe multi-tenancy |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

Where source-system data quality is unknown, place profiling and remediation before migration rehearsal; do not promise cutover until reconciliation, UAT, rollback, and owner approvals are evidenced.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/saas-implementation-methodology-blocks.md](../../profiles-sectors/references/saas-implementation-methodology-blocks.md) — reusable Methodology section content.
- [../references/ai-on-saas-methodology-blocks.md](../../profiles-sectors/references/ai-on-saas-methodology-blocks.md) — AI-on-SaaS methodology overlay.
- [../ai-on-saas-combined-methodology/SKILL.md](../../ai-on-saas-proposals/ai-on-saas-combined-methodology/SKILL.md) — companion skill when AI features are built into the SaaS.
- [../references/saas-multi-tenant-architecture-block.md](../../profiles-sectors/references/saas-multi-tenant-architecture-block.md) — architecture credibility paragraphs.
- [../references/saas-trust-and-compliance-section-template.md](../../profiles-sectors/references/saas-trust-and-compliance-section-template.md) — trust section structure.
- [../references/saas-customer-success-engagement-package.md](../../profiles-sectors/references/saas-customer-success-engagement-package.md) — Phase 6 detail.
- [../references/saas-lifecycle-email-program-proposal-template.md](../../profiles-sectors/references/saas-lifecycle-email-program-proposal-template.md) — adoption communications.
- [../references/saas-risk-register-for-proposals.md](../../profiles-sectors/references/saas-risk-register-for-proposals.md) — risk entries.
- [../references/saas-mutual-action-plan-template.md](../../profiles-sectors/references/saas-mutual-action-plan-template.md) — phase orchestration through MAP.
- [../06-methodology/SKILL.md](../../pipeline/06-methodology/SKILL.md) — methodology section discipline.
- [../saas-multi-tenant-architecture-credibility-block/SKILL.md](../saas-multi-tenant-architecture-credibility-block/SKILL.md) — companion skill for architectural literacy.
