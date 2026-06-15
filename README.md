# Proposal Skills

A Claude Code and Codex skills repository for generating professional consulting proposals tailored for the East and Central African consulting market.

## SaaS + AI-on-SaaS + Agent Proposal Stack (May 2026)

Bain/EY/McKinsey-grade proposal arsenal for SaaS implementation, AI-on-SaaS engagements, and agentic product engagements.

**SaaS proposals (14 skills + 19 enhancements + 25 references):** discovery & qualification, business case / ROI modeling, pricing & packaging proposal, implementation methodology, POC / pilot scoping, procurement & security questionnaire, customer success & adoption proposal, mutual action planning & close plans, vertical positioning (5 verticals: financial services, insurance, public sector, healthcare, education), objection handling & competitive displacement, lifecycle communications as deliverable, trust & compliance credentials section, multi-tenant architecture credibility block, pilot-to-rollout change management.

**AI-on-SaaS proposals (11 skills + 13 enhancements + 20 references):** combined methodology (three-plane: control, application, AI), discovery & qualification (8 qualifying lines + scorecard), AI business case & ROI (Value Stack + Cost Stack + cost-of-tokens P50/P90/P99), AI pricing & packaging, AI POC scoping (binary eval thresholds, hallucination ceiling), AI risk & responsible-AI, AI compliance credentials, AI procurement questionnaire, AI implementation methodology blocks, AI change management, AI team composition (irreducible AI trio: AI Safety Lead + Eval Engineer + MLOps), AI vertical positioning.

**Agent proposals (11 skills + 15 enhancements + 21 references):** discovery & qualification (Agent-vs-Workflow Filter, L0–L5 autonomy ladder), agent business case & ROI (Tasks-per-FTE-Saved with Intervention Discount), agent pricing & packaging (six patterns: per-resolution / per-outcome / per-step / per-agent / hybrid / success-based), agent POC scoping (Shadow → Supervised → Agentic), agent methodology (8 phases), agent risk & responsible-AI (12-entry register, named Agent Safety Lead), agent compliance credentials, agent procurement, agent change management (trust staging, supervisor retraining), agent team composition, agent vertical positioning (7 verticals).

**Agent SLA + commercial (8 skills + 16 references):** SLA class table (Bronze/Silver/Gold/Platinum on four agent metrics + three guardrails), commercial packaging (Included / Add-on / Standalone), contract language pack, success-fee & outcome pricing structures (gain-share, success-fee, hybrid, performance-corridor), intervention-credit and abort-refund mechanics, MSA + SLA addendum templates, procurement objection handling (10 common asks), renewal & true-up clauses. Vertical SLA variants for financial services, public sector, healthcare.

**Book extractions** (in `book-extractions/`): 7 SaaS books distilled through the proposal lens, plus 4 audit documents.

## How It Works

A consultant clones this repo, opens a terminal, navigates to `proposal-skills/`, and starts Claude Code or another compatible agent. Active skills live under `skills/`; the parent router is `skills/SKILL.md`.

Every `SKILL.md` in this repository must place this exact line immediately below the first top-level `# ...` heading, not in frontmatter: `Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.`

## Proposal Workflow

1. Start in the repository root and launch the agent.
2. The agent creates or resumes a local `proposals/` workspace, which is gitignored.
3. Place ToR, RFP, adverts, and templates in the proposal `terms/` folder, and place CVs or team data in `team/`.
4. The agent reads `skills/SKILL.md`, loads `skills/profiles-sectors/profiles/SKILL.md`, routes through `skills/profiles-sectors/sectors/SKILL.md`, and then loads the relevant proposal section skills.
5. For high-stakes content, the agent runs `skills/strategy-positioning/critical-analysis-business-logic/SKILL.md` so claims, assumptions, feasibility, budget, and delivery logic are tested before final writing.
6. Sections are written into the per-proposal markdown files. Tables are generated into `sheets/`, and final `.docx` outputs are compiled into `output/`.

Example proposal workspace:

```text
proposals/
├── INDEX.md
└── 2026-03-15-moh-ict-assessment/
    ├── BRIEF.md
    ├── 01-cover-letter.md
    ├── 02-executive-summary.md
    ├── 03-understanding-of-assignment.md
    ├── 04-firm-profile.md
    ├── 05-relevant-experience.md
    ├── 06-methodology.md
    ├── 07-team-composition.md
    ├── 08-work-plan.md
    ├── 09-financial-proposal.md
    ├── terms/
    ├── sheets/
    ├── team/
    ├── research/
    └── output/
```

## What Makes This Different

This is not a collection of prompt templates. It is a structured knowledge base synthesised from consulting, strategy, project management, business analysis, manufacturing, production planning, inventory, and proposal-writing references.

Recent strengthening includes:

- Proposal strategy patterns such as S1-S2-B logic, P-I-P structure, SCQA narrative spine, Cialdini persuasion principles, theme architecture, and Red Team review.
- Critical analysis and business-logic discipline: claim-evidence-warrant reasoning, essential questions, mental-model review, feasibility checks, and achievability gates.
- Consulting delivery patterns such as McKinsey-style problem solving, Done-Done quality, Value Realisation Method, Design Thinking, SECI, and SOSTAC.
- Business analysis governance, context-driven requirements discovery, fit criteria, and transition planning.
- Project control artefacts such as WBS dictionaries, responsibility matrices, decision gates, staffing schedules, and work plan hierarchies.
- Manufacturing, industrial production, inventory, capacity, material handling, MRP, scheduling, and green production diagnostics for bids involving operations-heavy businesses.
- Premium proposal strategy, ethical evaluator psychology, sales discovery, objection handling, premium-rate defence, service design, technical strategy, and support/maintenance language derived from local HTML study materials.
- Premium commercial writing patterns for proof-led proposals, cover letters, executive summaries, case studies, business documents, and SEO/AI-search friendly thought leadership.

## Skill Categories

All sub-skills live under `skills/<category>/<skill-name>/`. The 12 thematic categories are:

| Category | Count | Purpose |
|---|---|---|
| `skills/pipeline/` | 10 | Numbered proposal section skills (01-cover-letter through 10-financial-proposal) |
| `skills/profiles-sectors/` | 3 | `profiles/`, `sectors/`, and shared `references/` |
| `skills/domain-delivery/` | 13 | Cross-cutting delivery domains (PM, change, M&E, stakeholder, capacity, GESI, ESS, data, sustainability, risk, BA tools, consulting frameworks, accounting-finance-advisory) |
| `skills/strategy-positioning/` | 10 | Positioning, premium, discovery, storytelling, service design, AI transformation, website, embedded accounting, critical analysis, support/maintenance |
| `skills/saas-proposals/` | 14 | SaaS implementation and product-development proposal skills |
| `skills/ai-on-saas-proposals/` | 11 | AI-on-SaaS methodology and supporting skills |
| `skills/ai-agent-proposals/` | 11 | Agent / multi-agent product proposal skills |
| `skills/ai-agent-commercial/` | 8 | Agent SLA, packaging, contract, outcome pricing, MSA, renewals |
| finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`) | Current doctrine catalog | Canonical finance and accounting module skills (IFRS, IAS, reconciliation, controls) — for finance/accounting/IFRS/IAS work, use the finance engine |
| `skills/writing-content/` | 3 | Blog and premium commercial writing |
| `skills/language/` | 2 | East African English and language standards |
| `skills/meta/` | 5 | Skill maintenance plus anti-slop quality: skill-writing, skill-safety-audit, update-claude-documentation, anti-ai-slop (real-time guardrail), ai-slop-audit (per-section auditor that blocks on grade F) |

## Repository Structure

```text
proposal-skills/
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── .gitignore
├── book-extractions/
├── doctrine/
├── docs/
└── skills/
    ├── SKILL.md
    ├── pipeline/                  # 01-cover-letter ... 10-financial-proposal
    ├── profiles-sectors/          # profiles/, sectors/, references/
    ├── domain-delivery/
    ├── strategy-positioning/
    ├── saas-proposals/
    ├── ai-on-saas-proposals/
    ├── ai-agent-proposals/
    ├── ai-agent-commercial/
    ├── writing-content/
    ├── language/
    └── meta/
```

## Proposal Section Skills

| # | Skill Path | What It Produces |
|---|---|---|
| 01 | `skills/pipeline/01-cover-letter/SKILL.md` | Client-specific opening, comparable past projects with outcomes, courteous closing |
| 02 | `skills/pipeline/02-executive-summary/SKILL.md` | Problem statement, four differentiators, scope table, timeline, value proposition |
| 03 | `skills/pipeline/03-understanding-of-assignment/SKILL.md` | Background, objectives, scope analysis, ToR comments in the firm's own words |
| 04 | `skills/pipeline/04-firm-profile/SKILL.md` | Legal details, service areas, sector expertise, geographic footprint, certifications |
| 05 | `skills/pipeline/05-relevant-experience/SKILL.md` | Summary table and project cards with quantified outcomes |
| 06 | `skills/pipeline/06-methodology/SKILL.md` | Conceptual framework, phased plan, deliverables table, risk register, QA, governance |
| 07 | `skills/pipeline/07-team-composition/SKILL.md` | Organogram, role-responsibility table, CVs, and team narrative |
| 08 | `skills/pipeline/08-work-plan/SKILL.md` | Gantt table, milestones, staffing schedule, realistic timelines and buffer |
| 09 | `skills/pipeline/09-expression-of-interest/SKILL.md` | Shorter pre-qualification document with credentials, experience, and available experts |
| 10 | `skills/pipeline/10-financial-proposal/SKILL.md` | Fee breakdown, reimbursables, payment schedule, and assumptions |

## Supporting Domain Skills

| Skill Path | Domain |
|---|---|
| `skills/domain-delivery/project-management/SKILL.md` | PRINCE2, PMBoK, Agile, governance, reporting, WBS-driven controls, steering committees |
| `skills/domain-delivery/change-management/SKILL.md` | ADKAR, Kotter, adoption strategies, resistance management |
| `skills/domain-delivery/monitoring-and-evaluation/SKILL.md` | Log frames, results frameworks, KPIs, theory of change |
| `skills/domain-delivery/stakeholder-engagement/SKILL.md` | Stakeholder mapping, consultation approaches, communication plans |
| `skills/domain-delivery/capacity-building/SKILL.md` | Training models, ToT, knowledge transfer, skills sustainability |
| `skills/domain-delivery/gender-and-social-inclusion/SKILL.md` | GESI frameworks, gender mainstreaming, disability and youth inclusion |
| `skills/domain-delivery/environmental-and-social-safeguards/SKILL.md` | ESIA, environmental management plans, World Bank ESF, AfDB ISS |
| `skills/domain-delivery/data-management/SKILL.md` | Data collection, MIS design, data governance, data protection law |
| `skills/strategy-positioning/ai-transformation-proposal/SKILL.md` | AI-powered applications, agentic workflows, AI analytics, automation, governance, evaluation, and maintenance proposals |
| `skills/strategy-positioning/website-design-proposal-strategy/SKILL.md` | Website design/development strategy, UX/content/SEO methodology, stack explanation, launch, handover, costing, and support |
| `skills/strategy-positioning/premium-client-proposal-strategy/SKILL.md` | Executive, enterprise, affluent, high-ticket, premium, and strategic transformation proposal positioning |
| `skills/strategy-positioning/premium-pricing-and-value-defense/SKILL.md` | Premium fee justification, commercial options, value stack, total-cost-of-ownership logic, and price defence |
| `skills/writing-content/premium-commercial-writing/SKILL.md` | Cross-cutting premium commercial writing for proposals, cover letters, executive summaries, case studies, business documents, public content, and SEO/AI-search friendly thought leadership |
| `skills/strategy-positioning/sales-discovery-and-objection-handling/SKILL.md` | Discovery questions, qualification, buyer concerns, objection handling, and follow-up logic |
| `skills/strategy-positioning/service-design-proposal-strategy/SKILL.md` | Service design, customer/citizen experience, journey maps, blueprints, co-creation, and implementation evidence |
| `skills/strategy-positioning/proposal-storytelling-and-evaluator-journey/SKILL.md` | Narrative spine, evaluator journey, case-study story structure, design rationale, and presentation flow |
| `skills/strategy-positioning/customer-service-and-maintenance-proposals/SKILL.md` | Support, maintenance, SLAs, escalation, incident response, managed services, and post-launch optimisation |
| `skills/domain-delivery/sustainability-planning/SKILL.md` | Exit strategies, institutional embedding, ownership transfer |
| `skills/domain-delivery/risk-management/SKILL.md` | Risk registers, mitigation frameworks, escalation triggers |
| `skills/domain-delivery/business-analysis-tools/SKILL.md` | SWOT, PESTLE, gap analysis, benchmarking, requirements analysis, maturity models |
| `skills/domain-delivery/consulting-frameworks/SKILL.md` | Problem structuring, financial analysis, strategy, operations, and communication frameworks |
| `skills/domain-delivery/accounting-finance-advisory/SKILL.md` | World-class finance/accounting proposal sections, project financial management, accounting, bookkeeping, ERP finance, controls, audit evidence, tax, donor/grant finance, financial modelling, and finance transformation |
| `skills/strategy-positioning/embedded-accounting-engine-proposal/SKILL.md` | Embedded ledger/accounting engine proposals that replace routine external bookkeeping software and produce audit-ready reports |
| `skills/strategy-positioning/critical-analysis-business-logic/SKILL.md` | Serious analysis, evaluator logic, business sense, feasibility, and achievability gate |
| `skills/meta/anti-ai-slop/SKILL.md` | Real-time anti-slop guardrail applied while writing every section: specificity floor, verify-before-write, authored voice, cover the hard parts, banned vocabulary |
| `skills/meta/ai-slop-audit/SKILL.md` | Per-section and per-iteration slop auditor that grades A/B/C/F with evidence and fixes; grade F blocks submission |
| `skills/saas-proposals/saas-discovery-and-qualification/SKILL.md` | SaaS discovery: ICP, Critical Event, pain chain, impact per role, decision process, MEDDPICC qualification gate |
| `skills/saas-proposals/saas-business-case-and-roi-modeling/SKILL.md` | CFO-grade SaaS business case: TCO, time-to-value, payback, LTV / CAC, NPV, sensitivity |
| `skills/saas-proposals/saas-pricing-and-packaging-proposal/SKILL.md` | Subscription, usage, hybrid, enterprise tiering, expansion, freemium, paid trial, price-increase |
| `skills/saas-proposals/saas-implementation-methodology/SKILL.md` | End-to-end SaaS implementation methodology with control plane and application plane build |
| `skills/saas-proposals/saas-poc-and-pilot-scoping/SKILL.md` | POC and pilot scoping with explicit success criteria and decision gates |
| `skills/saas-proposals/saas-procurement-and-security-questionnaire/SKILL.md` | Procurement, security review, DPA / MSA / SLA, data residency, exit clauses |
| `skills/saas-proposals/saas-customer-success-and-adoption-proposal/SKILL.md` | Customer success engagement: onboarding, success plan, QBR, expansion / save plays, health scoring |
| `skills/saas-proposals/saas-mutual-action-planning-and-close-plans/SKILL.md` | MAP from selection to value realisation; close plan from BAFO to signature |
| `skills/saas-proposals/saas-vertical-positioning/SKILL.md` | Vertical positioning for financial services, insurance, public sector, healthcare, education |
| `skills/saas-proposals/saas-objection-handling-and-competitive-displacement/SKILL.md` | Objection handling and competitive displacement |
| `skills/saas-proposals/saas-lifecycle-communications-as-deliverable/SKILL.md` | Six lifecycle programs as priced workstreams |
| `skills/saas-proposals/saas-trust-and-compliance-credentials-section/SKILL.md` | Trust and Compliance section template |
| `skills/saas-proposals/saas-multi-tenant-architecture-credibility-block/SKILL.md` | Methodology block proving SaaS architectural literacy |
| `skills/saas-proposals/saas-pilot-to-rollout-change-management/SKILL.md` | SaaS mindset transition and change management |
| `skills/ai-on-saas-proposals/ai-on-saas-combined-methodology/SKILL.md` | Headline AI-on-SaaS methodology: three planes, gates, binary AI acceptance criteria |
| `skills/ai-on-saas-proposals/ai-on-saas-discovery-and-qualification/SKILL.md` | Eight AI-on-SaaS qualifying lines and the qualification scorecard |
| `skills/ai-on-saas-proposals/ai-on-saas-business-case-and-roi/SKILL.md` | AI Value Stack + AI Cost Stack + eval-margin + cost-of-tokens + three-scenario ROI |
| `skills/ai-on-saas-proposals/ai-on-saas-pricing-and-packaging-proposal/SKILL.md` | Five AI pricing patterns, model-by-tier, fair-use, price-increase, FX |
| `skills/ai-on-saas-proposals/ai-on-saas-poc-and-pilot-scoping/SKILL.md` | AI POC with binary eval criteria, golden dataset, model-selection matrix, exit gates |
| `skills/ai-on-saas-proposals/ai-on-saas-risk-and-responsible-ai/SKILL.md` | Ten-entry AI risk register and Responsible-AI commitment with named accountable role |
| `skills/ai-on-saas-proposals/ai-on-saas-compliance-credentials/SKILL.md` | AI Trust and Compliance subsection (EU AI Act, NCAIS, NAIS, AI Policy KE/NG/ZA/UG/RW, ISO/NIST) |
| `skills/ai-on-saas-proposals/ai-on-saas-procurement-and-questionnaire/SKILL.md` | Eight-domain AI procurement answer pack |
| `skills/ai-on-saas-proposals/ai-on-saas-change-management-and-adoption/SKILL.md` | AI mindset transition: trust staging, augment-vs-replace, HITL design |
| `skills/ai-on-saas-proposals/ai-on-saas-team-composition/SKILL.md` | AI-on-SaaS roster: AI Safety Lead, Eval Engineer, MLOps, Prompt, RAG, Data-for-AI |
| `skills/ai-on-saas-proposals/ai-on-saas-vertical-positioning/SKILL.md` | Vertical AI plays for FS, insurance, public sector, healthcare, education, customer support |
| `skills/ai-agent-proposals/ai-agent-methodology/SKILL.md` | Headline AI-agent methodology: eight phases (Discover → Action-Catalogue → Architecture → Build → Shadow → Supervised → Agentic → Operate); gates per phase; eval, red-team, kill-switch, multi-agent governance |
| `skills/ai-agent-proposals/ai-agent-discovery-and-qualification/SKILL.md` | Agent-vs-Workflow Filter; L0–L5 Autonomy Ladder; ten agent-specific discovery lines; Agentic Qualification Scorecard |
| `skills/ai-agent-proposals/ai-agent-business-case-and-roi/SKILL.md` | Agent ROI: tasks-per-FTE with intervention discount; cost per outcome at P50/P90/P99; three scenarios keyed to autonomy ramp; irreversible-incident downside |
| `skills/ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md` | Six agent pricing patterns (per-resolution / per-outcome / per-step / per-agent / hybrid / success-based); intervention credit; vendor cost pass-through; autonomy-ramp clause |
| `skills/ai-agent-proposals/ai-agent-poc-and-pilot-scoping/SKILL.md` | Three-stage pilot (Shadow / Supervised / Agentic); binary thresholds; irreversibility ceiling; kill-switch drill; abort conditions |
| `skills/ai-agent-proposals/ai-agent-risk-and-responsible-ai/SKILL.md` | Twelve-entry agent risk register; Responsible-AI Agent Commitment with named Agent Safety Lead |
| `skills/ai-agent-proposals/ai-agent-compliance-credentials/SKILL.md` | Trust and Compliance for Agents: action audit log, irreversibility gating, intervention SLO, kill-switch and drill, red-team catalogue, identity policy, transparency-to-affected-party, sovereign-AI |
| `skills/ai-agent-proposals/ai-agent-procurement-and-questionnaire/SKILL.md` | Ten-domain agent procurement answer pack |
| `skills/ai-agent-proposals/ai-agent-change-management-and-adoption/SKILL.md` | Trust staging with named evidence per stage; augment / redeploy / retrain framing; funded supervisor retraining; agent-on-your-behalf disclosure UX |
| `skills/ai-agent-proposals/ai-agent-team-composition/SKILL.md` | Agent roster: Agent Architect, Tool Engineer, Agent Safety Lead, Eval Engineer, Red-Team Lead, HITL Designer, Multi-Agent Orchestrator (where applicable), Agent Ops; Two-of-Everything buyer-side |
| `skills/ai-agent-proposals/ai-agent-vertical-positioning/SKILL.md` | Vertical agent plays: customer support, FS (compliance / reconciliation), insurance (claims triage), public sector (extreme caution, sovereign-AI), healthcare (admin-only), legal (lawyer-final), operations (sandbox-first, coding agents) |
| `skills/ai-agent-commercial/ai-agent-sla-and-credit-schedule/SKILL.md` | Bronze / Silver / Gold / Platinum SLA classes on four agent metrics + three guardrails; credit schedule; service-credit cap; out-clauses (model-provider force-majeure, customer-fault, regulator-pause) |
| `skills/ai-agent-commercial/ai-agent-commercial-packaging/SKILL.md` | Agent Included in Pro vs Add-on vs Standalone packaging shapes; SLA-class alignment; renewal posture; cost recovery shape |
| `skills/ai-agent-commercial/ai-agent-contract-language-pack/SKILL.md` | Drop-in exhibit assembly — pricing exhibit, SLA exhibit, credit and refund exhibit, MSA addendum, abandonment-and-refund policy, dispute resolution, audit rights — with trade-not-give discipline |
| `skills/ai-agent-commercial/ai-agent-success-fee-and-outcome-pricing/SKILL.md` | Gain-share, success-fee, hybrid base-plus-success, performance-corridor; success-definition discipline (counter-example rule, cooling-off, attribution); downside protection |
| `skills/ai-agent-commercial/ai-agent-intervention-credit-and-abort-refund/SKILL.md` | Intervention-credit formula and customer-facing statement; five abort-and-refund triggers; pro-rata refund formula |
| `skills/ai-agent-commercial/ai-agent-msa-and-sla-addendum-templates/SKILL.md` | Eight agent-specific MSA clauses (action accountability, audit-log retention, kill-switch SLA, fee-for-evidence-pack, irreversible-action sub-cap, model-provider force-majeure, agent-identity warranty, intervention SLA) plus SLA addendum |
| `skills/ai-agent-commercial/ai-agent-procurement-objections-on-commercials/SKILL.md` | Ten common procurement asks on commercials with trade-not-give responses; ethical commercial-objection discipline |
| `skills/ai-agent-commercial/ai-agent-renewal-and-true-up/SKILL.md` | Auto / express / hybrid renewal, true-up, ramp-down protection, autonomy-progression price-step, index-linked renewal, FX corridor |

## Proposer Profiles

| Profile Path | Voice | Use When |
|---|---|---|
| `skills/profiles-sectors/profiles/peter-bamuhigire.md` | First-person singular | Proposing as Peter Bamuhigire |
| `skills/profiles-sectors/profiles/chwezi-core-systems.md` | First-person plural | Proposing as Chwezi Core Systems |
| `skills/profiles-sectors/profiles/client-template.md` | Customisable | Ghostwriting on behalf of a client |

## Knowledge Base

| Reference Path | Content |
|---|---|
| `skills/profiles-sectors/references/proposal-strategy-and-persuasion.md` | S1-S2-B logic, P-I-P structure, buyer psychology, SCQA, Cialdini, Red Team review |
| `skills/profiles-sectors/references/world-class-proposal-patterns.md` | McKinsey and Deloitte proposal patterns, storyboarding, ghost packs, elevator test, prewiring |
| `skills/profiles-sectors/references/consulting-delivery-excellence.md` | McKinsey-style problem solving, Design Sprint, SCAMPER, SOSTAC, SECI, Done-Done standard |
| `skills/profiles-sectors/references/ethical-persuasion-and-evaluator-psychology-gate.md` | Ethical persuasion, evaluator concerns, risk perception, social proof discipline, and persuasion red flags |
| `skills/profiles-sectors/references/premium-rate-justification-framework.md` | Premium value stack, proof ladder, commercial options, discount rules, and price defence |
| `skills/profiles-sectors/references/discovery-question-bank-for-proposals.md` | Proposal discovery questions for outcomes, buyers, users, scope, technology, AI, support, and commercial assumptions |
| `skills/profiles-sectors/references/proposal-objection-handling.md` | Ethical handling of price, risk, timeline, staffing, technology, AI, local-context, support, and procurement objections |
| `skills/profiles-sectors/references/service-design-methodology-module.md` | Service design phases, journey mapping, blueprints, co-creation, prototypes, implementation, and acceptance criteria |
| `skills/profiles-sectors/references/website-software-maintenance-support-language.md` | Website/software/AI maintenance categories, SLA language, support commitments, client responsibilities, and pricing notes |
| `skills/profiles-sectors/references/proposal-narrative-patterns-and-case-story-spine.md` | Evaluator journey, narrative spine, case-study story cards, design rationale, and storyboard use |
| `skills/profiles-sectors/references/technical-strategy-credibility-checklist.md` | Software, SaaS, AI, cloud, API, operations, roadmap, governance, and maintainability checks |
| `skills/profiles-sectors/references/customer-service-and-escalation-commitments.md` | Service communication, escalation, complaint recovery, known-problem updates, and support boundaries |
| `skills/writing-content/premium-commercial-writing/references/premium-writing-quality-gate.md` | Cross-cutting gate for professional, persuasive, premium-fee-worthy writing |
| `skills/writing-content/premium-commercial-writing/references/document-section-patterns.md` | Patterns for cover letters, executive summaries, proposal sections, case studies, business documents, and blogs |
| `skills/writing-content/premium-commercial-writing/references/seo-ai-search-writing.md` | Search-intent, SEO, and AI-search guidance for public-facing content |
| `skills/writing-content/premium-commercial-writing/references/book-extractions-audit-synthesis.md` | Copyright-safe book and EPUB inspiration rules plus current audit status |
| `skills/strategy-positioning/critical-analysis-business-logic/references/reasoning-and-business-sense-gate.md` | Essential questions, argument map, mental-model pass, business-sense checks, and achievability gate |
| `skills/domain-delivery/consulting-frameworks/references/` | Problem structuring, financial analysis, strategy, operations, communication |
| `skills/domain-delivery/business-analysis-tools/references/` | SWOT, PESTLE, gap analysis, requirements planning, fit criteria, transition evaluation, maturity models |

## Supported Procurement Frameworks

PPDA Uganda, World Bank, AfDB, UNDP and UN system procurement, and direct private sector, NGO, and government ministry RFPs.

## Language Standards

- British English throughout: organisation, programme, centre, colour.
- East African professional tone: formal, respectful, courteous, and free of marketing hype.
- Dates use day-month-year format, such as 17 February 2026.
- Avoid AI-sounding vocabulary such as delve, tapestry, landscape as metaphor, leverage, navigate as metaphor, foster, realm, harness, synergy, embark, robust, vibrant, holistic, and seamless.

## Getting Started

```bash
git clone <repository-url> proposal-skills
cd proposal-skills
claude
```

Claude reads `CLAUDE.md`, starts with `skills/SKILL.md`, and walks through creating or resuming a proposal.

## Adding a New Skill

1. Create a subdirectory under `skills/` with a `SKILL.md`.
2. Add a local `references/` subdirectory only if needed.
3. Update `skills/SKILL.md`, `CLAUDE.md`, and this README.
