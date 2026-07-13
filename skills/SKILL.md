---
name: skills
description: Use when routing, drafting, reviewing, or assembling a complete consulting proposal, EoI, bid, or tender response; use a numbered pipeline skill when only one known section is required.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Proposal Writing - Parent Skill
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

This parent skill covers the full range of consulting proposal documents. All active proposal skills live under the repository `skills/` directory. Paths below are repository-root-relative so agents and project documentation refer to the same layout.

<!-- dual-compat-start -->
## Use When
- Use this skill when the user needs to draft, review, or assemble any consulting proposal, bid, or Expression of Interest.
- Load it when you need routing guidance to the correct numbered section skill or supporting skill.

## Do Not Use When
- The task is only about blog writing or skill maintenance.
- The work is unrelated to proposals, tenders, or bid responses.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| ToR, RFP, advert, or proposal brief | Client or procurement portal | Yes | Stop section drafting and request the governing terms or return a qualified routing-only result. |
| Proposer identity | `profiles` skill and approved profile file | Yes for drafting | Load exactly one profile; do not infer credentials or signatory authority. |
| Procurement, sector, template, deadline, and envelope constraints | Client instructions and `sectors` skill | Conditional | State the gap and avoid compliance or submission claims until verified. |

## Workflow
1. Identify the requested document or proposal section.
2. Load `skills/profiles-sectors/profiles/SKILL.md` before drafting proposal text so voice and identity are consistent.
3. Load the relevant numbered section skill, then add procurement, sector, and supporting domain skills only where they materially improve the output.
4. Load `skills/strategy-positioning/website-design-proposal-strategy/SKILL.md` whenever the proposal includes website design, redesign, SEO, web content, ecommerce, portal, landing page, web frontend, hosting, maintenance, or website costing.
5. Load `skills/domain-delivery/retail-transformation-proposal/SKILL.md` whenever the proposal includes retail, omnichannel, e-commerce operations, POS, merchandising, pricing, promotions, markdowns, loyalty, CRM, fulfilment, returns, store operations, shrink, vendor terms, private label, planogram, new-store opening, or retail KPI/WBR scope.
6. Load premium, discovery, service-design, storytelling, support, and pricing skills where the buyer context, value defence, implementation credibility, or post-launch operation requires them.
7. Load `skills/domain-delivery/accounting-finance-advisory/SKILL.md` whenever the proposal needs a finance/accounting section, project financial management section, accounting controls, budget governance, donor/grant finance, statutory/tax handling, audit evidence, financial modelling, bookkeeping, ERP/POS finance, revenue assurance, cost controls, or management reporting. Also load `skills/strategy-positioning/embedded-accounting-engine-proposal/SKILL.md` when the proposal includes embedded accounting, finance automation, inventory accounting, payroll accounting, tax/VAT automation, or a claim that the system replaces QuickBooks/Sage/Pastel/Tally-class workflows.
8. Load `skills/writing-content/premium-commercial-writing/SKILL.md` when the proposal, cover letter, executive summary, case study, business document, or public-facing content needs premium commercial polish, evaluator-friendly structure, stronger proof, or search-aware writing.
9. Load `skills/strategy-positioning/critical-analysis-business-logic/SKILL.md` before drafting high-stakes, methodology, work plan, financial, transformation, or final-review content.
9. Apply `skills/meta/anti-ai-slop/SKILL.md` as a REAL-TIME gate on every section while you write it, so slop never enters the draft in the first place.
10. After each section or major iteration, run `skills/meta/ai-slop-audit/SKILL.md` on what was just produced. The audit grades A/B/C/F; a grade of F (Blocked) blocks submission, so fix the blocking findings before moving to the next section. Run it again as the final gate before assembly or submission.
11. Draft the requested content and keep proposal-wide themes, evidence, terminology, methodology, work plan, and pricing aligned.
12. Verify compliance, logic, feasibility, section order, and separation between technical and financial content before finalizing.
13. Stop when a mandatory form, proposer fact, authority, price basis, or evidence source is missing.
14. Recover by obtaining the source, narrowing the deliverable, or returning an explicitly qualified gap rather than inventing content.

## Capability Contract

Read and search are required for the ToR, profile, sector rules, and existing proposal artefacts. Editing is permitted only when drafting or revision is authorised. External submission, publishing, spending, destructive file changes, legal certification, and claims on behalf of the proposer require explicit authority.

## Degraded Mode

Fallback: when files, network sources, rendering, spreadsheet tooling, or evidence are unavailable, return the narrowest useful routing decision or qualified draft, mark affected checks `not assessed`, and never present missing compliance evidence as passed.

## Decision Rules

| Condition or choice | Action | Failure or risk avoided |
|---|---|---|
| Full bid or several interdependent sections | Use this parent router, profile, sector, reasoning, and quality gates | Cross-section contradiction |
| One known proposal section only | Route to the matching numbered pipeline skill | Loading the whole catalogue unnecessarily |
| Technical and financial envelopes are separate | Produce and validate them independently | Procurement disqualification |
| Software, finance, website, SaaS, or agentic scope appears | Add the named domain engine or specialist skill | Unsupported technical or commercial claims |

## Quality Standards
- Treat each [SKILL.md](SKILL.md) as the portable unit and load it from the `skills/` folder.
- Maintain British English, East African professional tone, and proposer-specific voice.
- Keep the proposal client-specific, evaluator-aware, and measurable where evidence exists.

## Anti-Patterns
- Drafting before selecting the proposer profile. Fix: load exactly one approved profile first.
- Generating a full proposal from memory. Fix: inspect the ToR and load each relevant section skill.
- Mixing technical and financial envelopes. Fix: produce separate artefacts and run separate compliance checks.
- Claiming compliance without the governing form or instruction. Fix: mark the requirement not assessed until verified.
- Allowing methodology, staffing, schedule, and price to diverge. Fix: reconcile them against one deliverables and effort model.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Routing decision or proposal component | Proposal lead and downstream section skills | Correct profile, sector, section, quality, and domain routes are named with no unresolved collision. |
| Assembled proposal set | Evaluator and submission owner | Required sections, forms, evidence, cross-section consistency, and envelope separation pass their gates. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Routing and compliance record | Proposal release owner | Loaded skills, source documents, unassessed requirements, and blocking findings are traceable. |

## Core Routing References
- [skills/profiles-sectors/profiles/SKILL.md](profiles-sectors/profiles/SKILL.md) for proposer selection.
- [skills/profiles-sectors/sectors/SKILL.md](profiles-sectors/sectors/SKILL.md) for procurement and sector routing.
- `skills/profiles-sectors/references/` for persuasion, delivery, and proposal patterns.

## References

- [Proposer profile router](profiles-sectors/profiles/SKILL.md)
- [Procurement and sector router](profiles-sectors/sectors/SKILL.md)
- [Critical analysis and business logic](strategy-positioning/critical-analysis-business-logic/SKILL.md)
- [Anti-slop production guardrail](meta/anti-ai-slop/SKILL.md)
- [AI slop audit gate](meta/ai-slop-audit/SKILL.md)
<!-- dual-compat-end -->

## Sub-Skills - Proposal Sections

| # | Task | Sub-Skill to Read |
|---|---|---|
| 01 | Cover letter | `skills/pipeline/01-cover-letter/SKILL.md` |
| 02 | Executive summary | `skills/pipeline/02-executive-summary/SKILL.md` |
| 03 | Understanding of the assignment | `skills/pipeline/03-understanding-of-assignment/SKILL.md` |
| 04 | Firm or consultant profile | `skills/pipeline/04-firm-profile/SKILL.md` |
| 05 | Relevant experience and past projects | `skills/pipeline/05-relevant-experience/SKILL.md` |
| 06 | Approach and methodology | `skills/pipeline/06-methodology/SKILL.md` |
| 07 | Team composition and CVs | `skills/pipeline/07-team-composition/SKILL.md` |
| 08 | Work plan and timeline | `skills/pipeline/08-work-plan/SKILL.md` |
| 09 | Expression of Interest | `skills/pipeline/09-expression-of-interest/SKILL.md` |
| 10 | Financial proposal | `skills/pipeline/10-financial-proposal/SKILL.md` |

## Supporting Skills - Cross-Cutting Knowledge

Read the relevant supporting skill when the proposal requires that domain. Each can also generate a standalone section if the ToR explicitly requires it.

| Supporting Skill | When to Read |
|---|---|
| `skills/domain-delivery/project-management/SKILL.md` | PM frameworks, governance, reporting, steering committees |
| `skills/domain-delivery/change-management/SKILL.md` | OCM frameworks, adoption strategies, resistance management |
| `skills/domain-delivery/monitoring-and-evaluation/SKILL.md` | Log frames, results frameworks, KPIs, theory of change |
| `skills/domain-delivery/stakeholder-engagement/SKILL.md` | Stakeholder mapping, consultation approaches, communication plans |
| `skills/domain-delivery/capacity-building/SKILL.md` | Training models, ToT, knowledge transfer, skills sustainability |
| `skills/domain-delivery/gender-and-social-inclusion/SKILL.md` | GESI frameworks, gender mainstreaming, disability and youth inclusion |
| `skills/domain-delivery/environmental-and-social-safeguards/SKILL.md` | ESIA, environmental management plans, World Bank ESF, AfDB ISS |
| `skills/domain-delivery/data-management/SKILL.md` | Data collection, MIS design, data governance, data protection law |
| `skills/strategy-positioning/website-design-proposal-strategy/SKILL.md` | Website philosophy, UX/content/SEO methodology, stack explanation, costing, QA, launch, handover, and support |
| `skills/strategy-positioning/ai-transformation-proposal/SKILL.md` | AI applications, automation, agents, analytics, governance, evaluation, operations, and maintenance proposals |
| `skills/strategy-positioning/premium-client-proposal-strategy/SKILL.md` | Executive, enterprise, affluent, high-ticket, premium, and strategic transformation proposal positioning |
| `skills/strategy-positioning/premium-pricing-and-value-defense/SKILL.md` | Premium fee justification, value stack, commercial options, and price defence |
| `skills/writing-content/premium-commercial-writing/SKILL.md` | Premium commercial writing quality for proposals, cover letters, executive summaries, case studies, business documents, and public content |
| `skills/strategy-positioning/sales-discovery-and-objection-handling/SKILL.md` | Discovery questions, qualification, buyer concerns, objection handling, and follow-up logic |
| `skills/strategy-positioning/service-design-proposal-strategy/SKILL.md` | Journey mapping, service blueprints, co-creation, service implementation, and experience redesign |
| `skills/strategy-positioning/proposal-storytelling-and-evaluator-journey/SKILL.md` | Narrative spine, evaluator journey, case stories, design rationale, and presentation logic |
| `skills/strategy-positioning/customer-service-and-maintenance-proposals/SKILL.md` | Support, maintenance, SLAs, escalation, incident response, customer success, and post-launch optimisation |
| `skills/domain-delivery/sustainability-planning/SKILL.md` | Exit strategies, institutional embedding, ownership transfer |
| `skills/domain-delivery/risk-management/SKILL.md` | Risk registers, mitigation frameworks, escalation triggers |
| `skills/domain-delivery/business-analysis-tools/SKILL.md` | SWOT, PESTLE, gap analysis, benchmarking, cost-benefit analysis, maturity models, prioritisation matrices |
| `skills/domain-delivery/consulting-frameworks/SKILL.md` | Problem structuring, financial analysis, strategy frameworks, operations frameworks, communication structures |
| `skills/domain-delivery/accounting-finance-advisory/SKILL.md` | World-class finance/accounting proposal sections, project financial management, accounting, bookkeeping, ERP finance, controls, audit evidence, tax, donor/grant finance, financial modelling, and finance transformation |
| `skills/domain-delivery/retail-transformation-proposal/SKILL.md` | Retail, omnichannel, e-commerce operations, POS, merchandising, pricing, promotions, markdowns, loyalty, CRM, fulfilment, returns, store operations, shrink, vendor terms, private label, planogram, new-store opening, and retail KPI/WBR proposals |
| `skills/strategy-positioning/embedded-accounting-engine-proposal/SKILL.md` | Embedded ledger/accounting engine proposals that replace routine external bookkeeping software and produce audit-ready reports |
| `skills/strategy-positioning/critical-analysis-business-logic/SKILL.md` | Cross-cutting serious analysis, evaluator logic, business sense, feasibility, and achievability gate |
| `skills/meta/anti-ai-slop/SKILL.md` | Real-time anti-slop guardrail on every section while writing: specificity floor, verify-before-write, authored voice, cover the hard parts, banned vocabulary |
| `skills/meta/ai-slop-audit/SKILL.md` | Per-section and per-iteration slop audit; grades A/B/C/F with evidence and fixes; grade F blocks submission; also the final gate before assembly |
| `skills/saas-proposals/saas-discovery-and-qualification/SKILL.md` | SaaS discovery: ICP, Critical Event, pain chain, impact per role, decision process (consensus vs hierarchy), MEDDPICC qualification gate |
| `skills/saas-proposals/saas-business-case-and-roi-modeling/SKILL.md` | SaaS business case: TCO vs on-premise, time-to-value, CAC payback, LTV uplift, ROI, NPV, sensitivity, Rule of 40 for investor-grade buyers |
| `skills/saas-proposals/saas-pricing-and-packaging-proposal/SKILL.md` | SaaS pricing and packaging: subscription, usage, hybrid, enterprise tiering, expansion, freemium, paid trial, price-increase clauses |
| `skills/saas-proposals/saas-implementation-methodology/SKILL.md` | End-to-end SaaS implementation methodology: control plane, application plane, tenant isolation, data partitioning, observability, billing integration, cost attribution, onboarding automation |
| `skills/saas-proposals/saas-poc-and-pilot-scoping/SKILL.md` | SaaS POC and pilot scoping: hypothesis, success criteria, exit criteria, time-box, decision gate |
| `skills/saas-proposals/saas-procurement-and-security-questionnaire/SKILL.md` | Procurement path, security questionnaire pack, DPA / MSA / SLA, data residency, sub-processors, exit clauses |
| `skills/saas-proposals/saas-customer-success-and-adoption-proposal/SKILL.md` | Customer success engagement package: onboarding, activation, success plan, QBR, expansion plays, save plays, health scoring |
| `skills/saas-proposals/saas-mutual-action-planning-and-close-plans/SKILL.md` | Mutual Action Plan from selection to go-live to value realisation; close plan from BAFO to signature |
| `skills/saas-proposals/saas-vertical-positioning/SKILL.md` | Vertical positioning for financial services, insurance, public sector, healthcare, education, and other priority verticals |
| `skills/saas-proposals/saas-objection-handling-and-competitive-displacement/SKILL.md` | Objections (price, risk, vendor lock, build-in-house, AI, adoption) and competitive displacement (incumbent renewal, point solution, build, open-source, do-nothing) |
| `skills/saas-proposals/saas-lifecycle-communications-as-deliverable/SKILL.md` | Lifecycle programs (acquisition, activation, engagement, expansion, retention, advocacy) as priced workstreams |
| `skills/saas-proposals/saas-trust-and-compliance-credentials-section/SKILL.md` | Trust and Compliance section: security, privacy, certifications, sub-processors, BCDR, audit, exit clauses, insurance |
| `skills/saas-proposals/saas-multi-tenant-architecture-credibility-block/SKILL.md` | Methodology-grade content block proving SaaS architectural literacy: control plane, application plane, tenant isolation, tenant context, cost attribution |
| `skills/saas-proposals/saas-pilot-to-rollout-change-management/SKILL.md` | SaaS mindset transition: per-tenant operations, continuous release, customer success replaces installation services, recurring revenue model |
| `skills/ai-on-saas-proposals/ai-on-saas-combined-methodology/SKILL.md` | Headline AI-on-SaaS methodology: three planes (control / application / AI), phases, gates, binary AI acceptance criteria, Responsible-AI commitment hook |
| `skills/ai-on-saas-proposals/ai-on-saas-discovery-and-qualification/SKILL.md` | Eight AI-on-SaaS qualifying lines: workflow-AI fit, data, hallucination tolerance, AI maturity, change-readiness, regulator, model-provider posture, tenant variation |
| `skills/ai-on-saas-proposals/ai-on-saas-business-case-and-roi/SKILL.md` | AI ROI that resists hype: AI Value Stack, AI Cost Stack, eval-margin, cost-of-tokens P50/P90/P99, three-scenario ROI, downside scenarios |
| `skills/ai-on-saas-proposals/ai-on-saas-pricing-and-packaging-proposal/SKILL.md` | Five AI pricing patterns, model-by-tier, fair-use, price-increase indexed and capped, FX clause, worked examples |
| `skills/ai-on-saas-proposals/ai-on-saas-poc-and-pilot-scoping/SKILL.md` | AI POC with binary eval criteria, golden dataset, model-selection matrix, hallucination ceiling, abstain logic, exit gates, abort fee |
| `skills/ai-on-saas-proposals/ai-on-saas-risk-and-responsible-ai/SKILL.md` | Ten-entry AI risk register and Responsible-AI commitment with named accountable role (AI Safety Lead) |
| `skills/ai-on-saas-proposals/ai-on-saas-compliance-credentials/SKILL.md` | AI Trust and Compliance subsection: EU AI Act, NCAIS, NAIS, AI Policy KE/NG/ZA/UG/RW, ISO 42001/23894, NIST AI RMF, model cards, eval CI, hallucination SLO, red-team, sub-processor disclosure, region routing, sovereign-AI |
| `skills/ai-on-saas-proposals/ai-on-saas-procurement-and-questionnaire/SKILL.md` | Eight-domain AI procurement answer pack: model providers and sub-processors, training-data posture, retention and deletion, region routing, sovereign-AI, eval and hallucination, safety and abuse, governance and redress |
| `skills/ai-on-saas-proposals/ai-on-saas-change-management-and-adoption/SKILL.md` | AI mindset transition: trust staging (shadow → confirm → supervised → auto), augment-vs-replace framing, HITL design with named human authority, retraining cadence communications, union / regulator communications |
| `skills/ai-on-saas-proposals/ai-on-saas-team-composition/SKILL.md` | AI-on-SaaS roster: irreducible AI trio (AI Safety Lead, Eval Engineer, MLOps) plus ML Lead, Prompt Engineer, RAG Engineer, Data Engineer (AI), AI Change Lead, with RACI, ramp curve, blended-rate considerations |
| `skills/ai-on-saas-proposals/ai-on-saas-vertical-positioning/SKILL.md` | Vertical AI plays: financial services (model-risk management), insurance (claims-AI HITL), public sector (sovereign-AI), healthcare (non-diagnostic clinician-in-the-loop), education (minor-data + instructor-in-the-loop), customer support (containment honesty + agent-assist) |
| `skills/ai-agent-proposals/ai-agent-methodology/SKILL.md` | Headline AI-agent methodology: eight phases (Discover → Action-Catalogue → Architecture for Autonomy → Build → Shadow → Supervised → Agentic → Operate); gates per phase; binary agentic acceptance; eval + red-team; kill-switch and drill; multi-agent orchestration where applicable |
| `skills/ai-agent-proposals/ai-agent-discovery-and-qualification/SKILL.md` | Agent-vs-Workflow Filter (5 tests), L0–L5 Autonomy Ladder, ten agent-specific discovery lines (workflow fit, autonomy target, action catalogue, oversight, success metric, irreversibility tolerance, accountability, scope-confinement, regulator exposure, operational readiness), Agentic Qualification Scorecard |
| `skills/ai-agent-proposals/ai-agent-business-case-and-roi/SKILL.md` | Agent ROI: Agent Value Stack + Agent Cost Stack, tasks-per-FTE-saved with intervention discount, cost per outcome at P50/P90/P99, three-scenario model keyed to autonomy ramp, downside scenarios (irreversible-incident, regulator action, intervention overshoot, scope-creep, model-price shock) |
| `skills/ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md` | Six agent pricing patterns (per-resolution / per-outcome / per-step / per-agent / hybrid / success-based), intervention credit, vendor cost pass-through with margin floor, fair-use, abort-and-refund, autonomy-ramp clause, FX |
| `skills/ai-agent-proposals/ai-agent-poc-and-pilot-scoping/SKILL.md` | Three-stage pilot (Shadow → Supervised → Agentic) with binary thresholds, intervention-rate ceiling, irreversible-action ceiling, scope-confinement, kill-switch drill, red-team pass, audit-log completeness, abort conditions, exit-to-production gate |
| `skills/ai-agent-proposals/ai-agent-risk-and-responsible-ai/SKILL.md` | Twelve-entry agent risk register (autonomy-action, irreversibility, accountability, scope-creep, multi-agent collusion, prompt injection via tool output, memory poisoning, regulator action, kill-switch failure, identity, escalation overload, legacy-system damage), Responsible-AI Agent Commitment with named Agent Safety Lead |
| `skills/ai-agent-proposals/ai-agent-compliance-credentials/SKILL.md` | Trust and Compliance for Agents: agentic compliance map (AI Act, NCAIS, NAIS, KE/NG/ZA/UG/RW policy, ISO 42001/23894, NIST AI RMF, sectoral), action audit log practice, irreversibility gating, intervention SLO, kill-switch architecture and drill, agent red-team catalogue, identity and impersonation, action-scope attestation, multi-agent governance, transparency-to-affected-party, sovereign-AI |
| `skills/ai-agent-proposals/ai-agent-procurement-and-questionnaire/SKILL.md` | Ten-domain agent procurement answer pack: autonomy level and action scope, oversight and intervention, irreversibility gating, kill-switch and drill, audit log, identity / impersonation / transparency, model and tool-call sub-processors, eval / red-team / drift, multi-agent governance, incident / liability / redress |
| `skills/ai-agent-proposals/ai-agent-change-management-and-adoption/SKILL.md` | Trust staging with named evidence (Shadow → Confirm → Supervised → Agentic), augment / redeploy / retrain framing per affected role, funded six-module supervisor retraining curriculum, union / works-council communications, agent-on-your-behalf disclosure UX, adoption metrics (intervention, override, abstain-correctness, supervisor CSAT, queue headroom, contestability case load) |
| `skills/ai-agent-proposals/ai-agent-team-composition/SKILL.md` | Agent roster: Agent Architect, Tool Engineer, Prompt Engineer, Retrieval/Memory Engineer, Multi-Agent Orchestrator Engineer (where applicable), Agent Safety Lead, Eval Engineer, Red-Team Lead, Human-in-the-loop Designer, AI Change Lead, Agent Ops Lead, SRE for Agents; RACI; ramp curve with safety at Phase 1; Two-of-Everything buyer-side counterparts |
| `skills/ai-agent-proposals/ai-agent-vertical-positioning/SKILL.md` | Vertical agent plays: customer support (resolution agents with containment-vs-deflection honesty), financial services (compliance / reconciliation; HITL strict; model-risk overlay), insurance (claims triage; HITL on declinature and payout), public sector (extreme caution; agents do not decide on citizens; sovereign-AI), healthcare (admin-only; clinician-final on clinical artefacts), legal (lawyer-final on filings and advice; confidentiality by tenant), operations (sandbox-first; merge-gate human; coding-agent specific eval) |
| `skills/ai-agent-commercial/ai-agent-sla-and-credit-schedule/SKILL.md` | Bronze / Silver / Gold / Platinum SLA classes on four agent metrics (availability + task-success + intervention rate + time-to-resolve) + three guardrails (kill-switch SLA, audit-log completeness, intervention SLA); credit schedule per metric; service-credit cap by class; out-clauses for upstream model-provider force-majeure, customer-fault exclusions, regulator-pause |
| `skills/ai-agent-commercial/ai-agent-commercial-packaging/SKILL.md` | Three packaging shapes — Included in Pro, Add-on, Standalone — with worked decision matrix, SLA-class alignment, renewal posture, eval / red-team cost recovery shape, adoption-weighted economics stress test |
| `skills/ai-agent-commercial/ai-agent-contract-language-pack/SKILL.md` | Drop-in exhibit assembly with trade-not-give discipline — pricing exhibit, SLA exhibit, credit and refund exhibit, MSA addendum, abandonment-and-refund policy, dispute resolution and audit rights, vendor cost pass-through, renewal and true-up, outcome-pricing clauses, success-definition library |
| `skills/ai-agent-commercial/ai-agent-success-fee-and-outcome-pricing/SKILL.md` | Four outcome-pricing structures (gain-share, success-fee threshold, hybrid base-plus-success, performance-corridor) with success-definition discipline (counter-example rule, cooling-off, attribution, reversal), downside protection (base covers cost, cap on success, unit floor) |
| `skills/ai-agent-commercial/ai-agent-intervention-credit-and-abort-refund/SKILL.md` | Intervention-credit formula on Unit Fees with stepped tables, customer-facing monthly statement format, five abort-and-refund triggers (irreversible-action at agency fault, intervention overshoot 60 days, regulator action, model-provider sustained outage, audit-log breach), pro-rata refund formula |
| `skills/ai-agent-commercial/ai-agent-msa-and-sla-addendum-templates/SKILL.md` | Eight agent-specific MSA clauses — action accountability, audit-log retention and replay, kill-switch SLA, fee-for-evidence-pack on dispute, sub-cap for irreversible-action liability, model-provider force-majeure, agent-identity warranty, intervention SLA and supervisor cost allocation — plus SLA addendum |
| `skills/ai-agent-commercial/ai-agent-procurement-objections-on-commercials/SKILL.md` | Ten common procurement asks — no pay for failed tasks, price floor, price corridor, audit the audit log, refund if fail, unlimited liability, regulator indemnity, absorb model cost, unlimited retention, terminate at will — with trade-not-give responses |
| `skills/ai-agent-commercial/ai-agent-renewal-and-true-up/SKILL.md` | Auto / express / hybrid renewal posture, true-up clause for volume divergence, ramp-down protection up to 15 %, autonomy-progression price-step at maturity thresholds, index-linked renewal capped at lower of CPI + 3 % and Model-Provider-Price-Index + 2 %, FX corridor for Africa-context |

## Reference - Proposal Strategy and Persuasion

Read `skills/profiles-sectors/references/proposal-strategy-and-persuasion.md` before writing any proposal. Apply its S1-S2-B baseline logic, P-I-P phase structure, buyer psychology, theme architecture, hypothesis-driven methodology, Pyramid of Ideas, SCQA narrative spine, objection handling, Cialdini principles, and Red Team review process.

## Reference - World-Class Proposal Patterns

Read `skills/profiles-sectors/references/world-class-proposal-patterns.md` before writing any proposal. Apply its guidance on quantified evidence, named frameworks, client-first problem framing, scannability, programme-level thinking, storyboarding, ghost packs, the elevator test, and prewiring.

## Reference - Critical Analysis and Business Logic

Read `skills/strategy-positioning/critical-analysis-business-logic/SKILL.md` before writing methodology, work plan, financial proposal, risk, M&E, sustainability, transformation, or final review content. Apply its claim-evidence-warrant discipline, essential questions, business-sense checks, mental-model pass, and achievability gate so the proposal is persuasive because it is logical and deliverable.

## Reference - Premium, Discovery, and Service Credibility

Use the shared references in `skills/profiles-sectors/references/` when a proposal needs deeper buyer insight, ethical persuasion, premium value defence, service design, support language, narrative structure, or technical strategy:

- [ethical-persuasion-and-evaluator-psychology-gate.md](profiles-sectors/references/ethical-persuasion-and-evaluator-psychology-gate.md)
- [premium-rate-justification-framework.md](profiles-sectors/references/premium-rate-justification-framework.md)
- [discovery-question-bank-for-proposals.md](profiles-sectors/references/discovery-question-bank-for-proposals.md)
- [proposal-objection-handling.md](profiles-sectors/references/proposal-objection-handling.md)
- [service-design-methodology-module.md](profiles-sectors/references/service-design-methodology-module.md)
- [website-software-maintenance-support-language.md](profiles-sectors/references/website-software-maintenance-support-language.md)
- [proposal-narrative-patterns-and-case-story-spine.md](profiles-sectors/references/proposal-narrative-patterns-and-case-story-spine.md)
- [technical-strategy-credibility-checklist.md](profiles-sectors/references/technical-strategy-credibility-checklist.md)
- [customer-service-and-escalation-commitments.md](profiles-sectors/references/customer-service-and-escalation-commitments.md)

Use `skills/writing-content/premium-commercial-writing/SKILL.md` as the cross-cutting writing layer when those strategy references must become sharper client-facing prose, case studies, executive summaries, public documents, or thought leadership.

## Reference - SaaS Implementation and SaaS Product-Development Proposals

For SaaS-specific bids, the engine carries dedicated skills and references. The SaaS-specific reference library in `skills/profiles-sectors/references/` includes:

- [saas-discovery-question-bank.md](profiles-sectors/references/saas-discovery-question-bank.md) - SaaS discovery (ICP, Critical Event, pain chain, impact, decision process).
- [meddic-and-command-of-message-for-saas.md](profiles-sectors/references/meddic-and-command-of-message-for-saas.md) - MEDDPICC qualification gate and Six-Lens Value Claim.
- [saas-mutual-action-plan-template.md](profiles-sectors/references/saas-mutual-action-plan-template.md) - MAP from selection to value realisation.
- [saas-demo-script-template.md](profiles-sectors/references/saas-demo-script-template.md) - discovery-tuned demo script.
- [saas-poc-scoping-template.md](profiles-sectors/references/saas-poc-scoping-template.md) - POC and pilot scoping.
- [saas-business-case-and-roi-template.md](profiles-sectors/references/saas-business-case-and-roi-template.md) - TCO / unit economics / ROI / NPV / sensitivity.
- [saas-pricing-models-reference.md](profiles-sectors/references/saas-pricing-models-reference.md) - subscription / usage / hybrid / tiering / expansion / freemium.
- [saas-procurement-and-security-questionnaire-playbook.md](profiles-sectors/references/saas-procurement-and-security-questionnaire-playbook.md) - procurement path and security questionnaire pack.
- [saas-msa-dpa-sla-template-language.md](profiles-sectors/references/saas-msa-dpa-sla-template-language.md) - contract-grade language patterns.
- [saas-customer-success-engagement-package.md](profiles-sectors/references/saas-customer-success-engagement-package.md) - customer success scope.
- [saas-lifecycle-email-program-proposal-template.md](profiles-sectors/references/saas-lifecycle-email-program-proposal-template.md) - six lifecycle programs.
- [saas-implementation-methodology-blocks.md](profiles-sectors/references/saas-implementation-methodology-blocks.md) - reusable methodology blocks.
- [saas-multi-tenant-architecture-block.md](profiles-sectors/references/saas-multi-tenant-architecture-block.md) - architectural credibility paragraphs.
- [saas-risk-register-for-proposals.md](profiles-sectors/references/saas-risk-register-for-proposals.md) - SaaS risk register.
- [vertical-saas-positioning-financial-services.md](profiles-sectors/references/vertical-saas-positioning-financial-services.md), [vertical-saas-positioning-insurance.md](profiles-sectors/references/vertical-saas-positioning-insurance.md), [vertical-saas-positioning-public-sector.md](profiles-sectors/references/vertical-saas-positioning-public-sector.md), [vertical-saas-positioning-healthcare.md](profiles-sectors/references/vertical-saas-positioning-healthcare.md), [vertical-saas-positioning-education.md](profiles-sectors/references/vertical-saas-positioning-education.md) - vertical positioning briefs.
- [saas-objection-handling-playbook.md](profiles-sectors/references/saas-objection-handling-playbook.md) - objection-handling library.
- [saas-vendor-vs-build-narrative.md](profiles-sectors/references/saas-vendor-vs-build-narrative.md) - build-vs-buy framing.
- [saas-win-themes-and-discriminators.md](profiles-sectors/references/saas-win-themes-and-discriminators.md) - SaaS win themes.
- [saas-gtm-motion-design-reference.md](profiles-sectors/references/saas-gtm-motion-design-reference.md) - GTM motion design.
- [saas-metrics-glossary-for-proposals.md](profiles-sectors/references/saas-metrics-glossary-for-proposals.md) - SaaS vocabulary.
- [saas-trust-and-compliance-section-template.md](profiles-sectors/references/saas-trust-and-compliance-section-template.md) - Trust and Compliance section template.

Load the SaaS skills and references when the engagement is SaaS implementation, SaaS product development, multi-tenant platform build, SaaS migration from installed software, SaaS commercial launch, or SaaS-on-AI work. The audit synthesis in `book-extractions/saas-proposal-skills-audit-2026.md` documents how these skills and references were derived from the seven SaaS books processed in 2026.

## Reference - Consulting Delivery Excellence

Read `skills/profiles-sectors/references/consulting-delivery-excellence.md` when writing methodology, quality assurance, or implementation sections. Use it to describe credible delivery methods such as McKinsey-style problem solving, consulting workflow, Done-Done quality, Value Realisation Method, Drucker's Five Questions, Design Thinking, SCAMPER, SOSTAC, SECI, and frontloaded work planning.

## Proposer Profiles - Who Is Proposing?

Before writing any proposal, load the correct proposer profile from `skills/profiles-sectors/profiles/SKILL.md`. The profile determines the voice, credentials, experience, and branding used throughout the document.

| Profile | When to Use |
|---|---|
| `skills/profiles-sectors/profiles/peter-bamuhigire.md` | Proposing as Peter Bamuhigire as an individual consultant |
| `skills/profiles-sectors/profiles/chwezi-core-systems.md` | Proposing as Chwezi Core Systems |
| `skills/profiles-sectors/profiles/client-template.md` | Writing on behalf of a client; copy, customise, and save |

If no proposer is specified, ask before proceeding. The profile affects every section: voice, signatory, experience, team, and references.

## Proposal Workspace

All proposals are developed in the local `proposals/` directory, which is gitignored. See `CLAUDE.md` for the full initialization workflow, directory structure, and `INDEX.md` format. Every proposal lives in its own subdirectory with section markdown files plus `terms/`, `sheets/`, `team/`, `research/`, and `output/` folders.

## Standards That Apply to All Sub-Skills

- Follow [skills/language/east-african-english/SKILL.md](language/east-african-english/SKILL.md) for tone, spelling, and courteous phrasing throughout.
- Use British English spelling: organisation, programme, centre, colour.
- Let the loaded proposer profile determine voice: first-person singular for individual consultants and first-person plural for companies.
- Never use exaggerated marketing language. Confident, measured, professional writing is preferred.

## Typical Proposal Section Order

1. Cover Letter
2. Technical Proposal Submission Sheet
3. Executive Summary
4. Understanding of the Assignment
5. Firm Profile
6. Relevant Experience
7. Approach and Methodology
8. Team Composition
9. Work Plan and Timeline
10. References

Financial Proposal is always a separate sealed document when the procurement process requires separation.
