# SaaS Implementation Methodology Blocks

Reusable Methodology section content for SaaS implementation engagements. Drop these blocks into the proposal's `06-methodology` section and tune to the specific assignment. Blocks pair with the multi-tenant architecture credibility block (`saas-multi-tenant-architecture-block.md`).

## Conceptual Approach (one to two pages)

The agency's approach to SaaS implementation rests on three convictions:

1. **A SaaS implementation is a control-plane and an application-plane build, not a single product configuration.** Onboarding, tenant management, identity, billing integration, observability, and tenant-context propagation belong on the control plane and must be designed deliberately, not retrofitted. The application plane is where the buyer's users do work. The two planes are designed, built, tested, and operated as distinct disciplines that share a single tenant model.

2. **Tenant isolation is a regulatory and commercial decision, not only a technical one.** The isolation model (silo, pool, bridge) determines cost-per-tenant, performance characteristics, regulator alignment, and tier pricing. The decision is taken jointly with the client's CISO, DPO, CFO, and product owner, then encoded in an Architecture Decision Record at the start of the build.

3. **Adoption is engineered, not hoped for.** Onboarding automation, lifecycle communications, customer-success engagement, and value-realisation review are designed into the engagement from day one. A SaaS implementation that succeeds technically but fails on adoption is a failed engagement.

## Standard Phases for SaaS Implementation Engagements

### Phase 1: Inception, Discovery, and SaaS Strategy Gate (Weeks 1–3)

The phase begins with a structured inception and a SaaS strategy gate that prevents the engagement from proceeding on weak foundations. Outputs:

- Diagnosed pain chain and value-at-stake document (Flavour A or B per the business case template).
- Account map of sponsors, champions, blockers, and the decision process.
- Critical event named and timed.
- Architecture Decision Record draft for tenant model and isolation.
- Integration discovery: target systems, owners, latency tolerances, reconciliation rules.
- Data residency, sub-processor, and regulator map.
- Updated risk register and mutual action plan.

### Phase 2: Control Plane Build (Weeks 3–10, overlapping with Phase 3)

- Tenant onboarding automation (self-serve where commercial, sales-assisted where enterprise, regulator-assisted where required).
- Tenant management surface (admin tools for tenant lifecycle).
- Identity model and IdP integration (corporate SSO, federated, customer-facing auth).
- Billing integration with the chosen revenue platform.
- Per-tenant observability and cost-attribution telemetry.
- Audit logging architecture.

### Phase 3: Application Plane Build (Weeks 4–14)

- Configuration for client-specific workflows.
- Integration build (core systems, payment, regulatory reporting, data warehouse).
- Tenant-context propagation across every service.
- Data partitioning and isolation enforcement.
- Performance, scale, and load testing under realistic multi-tenant patterns.

### Phase 4: Trust, Compliance, and Operations Hardening (Weeks 10–16)

- Security hardening: SAST, SCA, DAST, independent penetration test.
- Compliance evidence pack assembly (SOC 2 evidence, ISO 27001 alignment, sector-specific regulator pack).
- BCDR design, runbook authoring, DR test.
- Incident response runbook tested end-to-end.
- Customer-facing security and compliance documentation.

### Phase 5: User Acceptance, Pilot, and Go-Live (Weeks 14–20)

- UAT entry gate with the buyer's test manager.
- Pilot cohort selection, launch, and 30-day review.
- Go / no-go decision based on pilot success criteria.
- Cutover plan with rollback.
- Cutover and stabilisation.

### Phase 6: Adoption and Value Realisation (Weeks 18–34)

- Customer success engagement (per the customer-success package reference).
- Lifecycle communications launch (per the lifecycle program reference).
- 30, 60, 90-day adoption and value reviews.
- QBR cadence established.
- First expansion conversation (if applicable).

### Phase 7: Optimisation and Ongoing Operations (continuous)

- Continuous improvement backlog managed jointly with the buyer.
- Quarterly tenant-cost-attribution review.
- Annual tier-pricing review.
- Annual security and compliance refresh.
- Renewal and expansion proposals.

## Phase Naming Conventions When the ToR Differs

If the ToR uses different phase names (Inception / Design / Build / Test / Deploy / Support), map the SaaS phases into those names while preserving the workstream content:

- Inception → SaaS Phase 1.
- Design → opening third of SaaS Phases 2–3 (architecture, integration design).
- Build → SaaS Phases 2–3 main effort.
- Test → SaaS Phases 4 (compliance hardening) and 5 (UAT, pilot).
- Deploy → SaaS Phase 5 cutover.
- Support → SaaS Phases 6–7.

## P-I-P Phase Description Pattern (Methodology Sales Logic)

Every SaaS implementation phase description follows the engine's standard P-I-P structure (Persuasion-Information-Persuasion):

- **P (opening)**: why this phase, designed this way, is right for this client's diagnosed pain and decision process — not a recycled generic phase.
- **I (middle)**: specific actions, artefacts, integrations, controls, and team roles for the phase.
- **P (closing)**: what the client receives at the end of the phase, what decision it enables, and how it feeds the next phase.

Example opening (template):

"Phase 1 begins with a SaaS strategy gate because [client]'s [vertical / regulatory situation] makes early architectural decisions — particularly around tenant isolation and data residency — irreversible without significant cost. We will conduct discovery sessions with [named stakeholder roles], produce an Architecture Decision Record signed by the CTO, DPO, and CFO, and update the mutual action plan with the dates and owners for Phases 2 through 5. This phase ends with a SaaS strategy gate that gives [client] the right to revise scope or terms before the build commences."

## Standard Deliverables Table (Template)

| # | Deliverable | Phase | Format | Due | Acceptance Criteria |
|---|---|---|---|---|---|
| 1 | Inception Report | 1 | Document | Week 3 | Pain chain, value at stake, decision process documented and signed |
| 2 | Architecture Decision Record | 1 | Document | Week 3 | Tenant model, isolation, residency signed by CTO + DPO + CFO |
| 3 | Mutual Action Plan v1 | 1 | Table | Week 3 | Phases 1–6 with owners and dates |
| 4 | Control Plane Build Walkthrough | 2 | Live demo + document | Week 8 | Onboarding, identity, billing, observability operational |
| 5 | Integration Map | 3 | Document | Week 6 | All integrations specified, owners on each side |
| 6 | Application Plane Walkthrough 1 | 3 | Live demo + document | Week 10 | First end-to-end user journey complete |
| 7 | Compliance Evidence Pack | 4 | Document set | Week 15 | Sufficient for security review sign-off |
| 8 | BCDR Runbook and DR Test Report | 4 | Document | Week 16 | DR test executed with named recovery objectives met |
| 9 | UAT Entry Gate | 5 | Decision artefact | Week 14 | Buyer test manager approves entry |
| 10 | Pilot 30-Day Review | 5 | Document | Week 18 | Pilot success criteria scored; go/no-go decision |
| 11 | Cutover Runbook | 5 | Document | Week 16 | Cutover and rollback steps approved |
| 12 | Stabilisation Closure | 5 | Document | Week 22 | Project closure declared |
| 13 | 90-Day QBR Pack | 6 | Document + meeting | Week 34 | First QBR closed; value scorecard reviewed |

Add or remove rows to match the engagement scope.

## Risk Table (Template)

Combine with `saas-risk-register-for-proposals.md` for the full set. Top entries for a typical SaaS implementation:

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Tenant isolation model incompatible with regulator expectation | Medium | High | Architecture Decision Record in Phase 1; regulator dry-run in Phase 4 |
| Integration latency on legacy core systems | Medium | High | Integration discovery in Phase 1; performance gate in Phase 3 |
| Sponsor change before go-live | Medium | High | Account map maintained; secondary sponsor identified |
| Adoption below threshold at 60 days | Medium | High | Lifecycle program and customer-success engagement active from Phase 5 |
| Noisy-neighbour incidents post-go-live | Low–Medium | Medium | Per-tenant telemetry and tier-aware throttling from control plane |
| Sub-processor change rejected by client | Low | Medium | Notice protocol agreed in MSA / DPA |

## Quality Assurance and Governance

- Done-Done standard: every phase's deliverable passes peer review, editorial review, and a SaaS-specific quality gate (tenant context audit, security review, integration sanity-check) before submission to the client.
- Architecture Decision Records for any decision that is hard to reverse.
- Weekly status report during build, daily during cutover week.
- Pre-briefing the steering committee before each phase-end gate.

## Knowledge Transfer

- Pair working with named client counterparts on configuration, support, and lifecycle program operation from Phase 2.
- Two-of-everything principle for client-side critical operating roles by go-live.
- Runbook hand-over for control plane, application plane, support, customer success, lifecycle programs, and security operations.
- 90-day support window after closure, then transition to the retainer model.

## See Also

- `saas-multi-tenant-architecture-block.md` for the architecture credibility paragraphs.
- `saas-procurement-and-security-questionnaire-playbook.md` for the trust and compliance work in Phase 4.
- `saas-customer-success-engagement-package.md` for the work in Phase 6.
- `saas-lifecycle-email-program-proposal-template.md` for the communication backbone of Phase 6.
- `saas-mutual-action-plan-template.md` for the MAP that orchestrates all phases.
- `saas-risk-register-for-proposals.md` for the full risk register.
- `../06-methodology/SKILL.md` for the methodology section discipline.
