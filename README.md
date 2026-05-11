# Proposal Skills

A Claude Code and Codex skills repository for generating professional consulting proposals tailored for the East and Central African consulting market.

## How It Works

A consultant clones this repo, opens a terminal, navigates to `proposal-skills/`, and starts Claude Code or another compatible agent. Active skills live under `skills/`; the parent router is `skills/SKILL.md`.

Every `SKILL.md` in this repository must place this exact line immediately below the first top-level `# ...` heading, not in frontmatter: `Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.`

## Proposal Workflow

1. Start in the repository root and launch the agent.
2. The agent creates or resumes a local `proposals/` workspace, which is gitignored.
3. Place ToR, RFP, adverts, and templates in the proposal `terms/` folder, and place CVs or team data in `team/`.
4. The agent reads `skills/SKILL.md`, loads `skills/profiles/SKILL.md`, routes through `skills/sectors/SKILL.md`, and then loads the relevant proposal section skills.
5. For high-stakes content, the agent runs `skills/critical-analysis-business-logic/SKILL.md` so claims, assumptions, feasibility, budget, and delivery logic are tested before final writing.
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

## Repository Structure

```text
proposal-skills/
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── .gitignore
├── docs/
└── skills/
    ├── SKILL.md
    ├── 01-cover-letter/
    ├── 02-executive-summary/
    ├── 03-understanding-of-assignment/
    ├── 04-firm-profile/
    ├── 05-relevant-experience/
    ├── 06-methodology/
    ├── 07-team-composition/
    ├── 08-work-plan/
    ├── 09-expression-of-interest/
    ├── 10-financial-proposal/
    ├── profiles/
    ├── references/
    ├── consulting-frameworks/
    ├── business-analysis-tools/
    ├── sectors/
    ├── project-management/
    ├── change-management/
    ├── monitoring-and-evaluation/
    ├── stakeholder-engagement/
    ├── capacity-building/
    ├── gender-and-social-inclusion/
    ├── environmental-and-social-safeguards/
    ├── data-management/
    ├── sustainability-planning/
    ├── risk-management/
    ├── east-african-english/
    ├── language-standards/
    ├── premium-commercial-writing/
    ├── blog-writer/
    ├── blog-idea-generator/
    ├── skill-writing/
    ├── skill-safety-audit/
    └── update-claude-documentation/
```

## Proposal Section Skills

| # | Skill Path | What It Produces |
|---|---|---|
| 01 | `skills/01-cover-letter/SKILL.md` | Client-specific opening, comparable past projects with outcomes, courteous closing |
| 02 | `skills/02-executive-summary/SKILL.md` | Problem statement, four differentiators, scope table, timeline, value proposition |
| 03 | `skills/03-understanding-of-assignment/SKILL.md` | Background, objectives, scope analysis, ToR comments in the firm's own words |
| 04 | `skills/04-firm-profile/SKILL.md` | Legal details, service areas, sector expertise, geographic footprint, certifications |
| 05 | `skills/05-relevant-experience/SKILL.md` | Summary table and project cards with quantified outcomes |
| 06 | `skills/06-methodology/SKILL.md` | Conceptual framework, phased plan, deliverables table, risk register, QA, governance |
| 07 | `skills/07-team-composition/SKILL.md` | Organogram, role-responsibility table, CVs, and team narrative |
| 08 | `skills/08-work-plan/SKILL.md` | Gantt table, milestones, staffing schedule, realistic timelines and buffer |
| 09 | `skills/09-expression-of-interest/SKILL.md` | Shorter pre-qualification document with credentials, experience, and available experts |
| 10 | `skills/10-financial-proposal/SKILL.md` | Fee breakdown, reimbursables, payment schedule, and assumptions |

## Supporting Domain Skills

| Skill Path | Domain |
|---|---|
| `skills/project-management/SKILL.md` | PRINCE2, PMBoK, Agile, governance, reporting, WBS-driven controls, steering committees |
| `skills/change-management/SKILL.md` | ADKAR, Kotter, adoption strategies, resistance management |
| `skills/monitoring-and-evaluation/SKILL.md` | Log frames, results frameworks, KPIs, theory of change |
| `skills/stakeholder-engagement/SKILL.md` | Stakeholder mapping, consultation approaches, communication plans |
| `skills/capacity-building/SKILL.md` | Training models, ToT, knowledge transfer, skills sustainability |
| `skills/gender-and-social-inclusion/SKILL.md` | GESI frameworks, gender mainstreaming, disability and youth inclusion |
| `skills/environmental-and-social-safeguards/SKILL.md` | ESIA, environmental management plans, World Bank ESF, AfDB ISS |
| `skills/data-management/SKILL.md` | Data collection, MIS design, data governance, data protection law |
| `skills/ai-transformation-proposal/SKILL.md` | AI-powered applications, agentic workflows, AI analytics, automation, governance, evaluation, and maintenance proposals |
| `skills/website-design-proposal-strategy/SKILL.md` | Website design/development strategy, UX/content/SEO methodology, stack explanation, launch, handover, costing, and support |
| `skills/premium-client-proposal-strategy/SKILL.md` | Executive, enterprise, affluent, high-ticket, premium, and strategic transformation proposal positioning |
| `skills/premium-pricing-and-value-defense/SKILL.md` | Premium fee justification, commercial options, value stack, total-cost-of-ownership logic, and price defence |
| `skills/premium-commercial-writing/SKILL.md` | Cross-cutting premium commercial writing for proposals, cover letters, executive summaries, case studies, business documents, public content, and SEO/AI-search friendly thought leadership |
| `skills/sales-discovery-and-objection-handling/SKILL.md` | Discovery questions, qualification, buyer concerns, objection handling, and follow-up logic |
| `skills/service-design-proposal-strategy/SKILL.md` | Service design, customer/citizen experience, journey maps, blueprints, co-creation, and implementation evidence |
| `skills/proposal-storytelling-and-evaluator-journey/SKILL.md` | Narrative spine, evaluator journey, case-study story structure, design rationale, and presentation flow |
| `skills/customer-service-and-maintenance-proposals/SKILL.md` | Support, maintenance, SLAs, escalation, incident response, managed services, and post-launch optimisation |
| `skills/sustainability-planning/SKILL.md` | Exit strategies, institutional embedding, ownership transfer |
| `skills/risk-management/SKILL.md` | Risk registers, mitigation frameworks, escalation triggers |
| `skills/business-analysis-tools/SKILL.md` | SWOT, PESTLE, gap analysis, benchmarking, requirements analysis, maturity models |
| `skills/consulting-frameworks/SKILL.md` | Problem structuring, financial analysis, strategy, operations, and communication frameworks |
| `skills/critical-analysis-business-logic/SKILL.md` | Serious analysis, evaluator logic, business sense, feasibility, and achievability gate |
| `skills/saas-discovery-and-qualification/SKILL.md` | SaaS discovery: ICP, Critical Event, pain chain, impact per role, decision process, MEDDPICC qualification gate |
| `skills/saas-business-case-and-roi-modeling/SKILL.md` | CFO-grade SaaS business case: TCO, time-to-value, payback, LTV / CAC, NPV, sensitivity |
| `skills/saas-pricing-and-packaging-proposal/SKILL.md` | Subscription, usage, hybrid, enterprise tiering, expansion, freemium, paid trial, price-increase |
| `skills/saas-implementation-methodology/SKILL.md` | End-to-end SaaS implementation methodology with control plane and application plane build |
| `skills/saas-poc-and-pilot-scoping/SKILL.md` | POC and pilot scoping with explicit success criteria and decision gates |
| `skills/saas-procurement-and-security-questionnaire/SKILL.md` | Procurement, security review, DPA / MSA / SLA, data residency, exit clauses |
| `skills/saas-customer-success-and-adoption-proposal/SKILL.md` | Customer success engagement: onboarding, success plan, QBR, expansion / save plays, health scoring |
| `skills/saas-mutual-action-planning-and-close-plans/SKILL.md` | MAP from selection to value realisation; close plan from BAFO to signature |
| `skills/saas-vertical-positioning/SKILL.md` | Vertical positioning for financial services, insurance, public sector, healthcare, education |
| `skills/saas-objection-handling-and-competitive-displacement/SKILL.md` | Objection handling and competitive displacement |
| `skills/saas-lifecycle-communications-as-deliverable/SKILL.md` | Six lifecycle programs as priced workstreams |
| `skills/saas-trust-and-compliance-credentials-section/SKILL.md` | Trust and Compliance section template |
| `skills/saas-multi-tenant-architecture-credibility-block/SKILL.md` | Methodology block proving SaaS architectural literacy |
| `skills/saas-pilot-to-rollout-change-management/SKILL.md` | SaaS mindset transition and change management |
| `skills/ai-on-saas-combined-methodology/SKILL.md` | Headline AI-on-SaaS methodology: three planes, gates, binary AI acceptance criteria |
| `skills/ai-on-saas-discovery-and-qualification/SKILL.md` | Eight AI-on-SaaS qualifying lines and the qualification scorecard |
| `skills/ai-on-saas-business-case-and-roi/SKILL.md` | AI Value Stack + AI Cost Stack + eval-margin + cost-of-tokens + three-scenario ROI |
| `skills/ai-on-saas-pricing-and-packaging-proposal/SKILL.md` | Five AI pricing patterns, model-by-tier, fair-use, price-increase, FX |
| `skills/ai-on-saas-poc-and-pilot-scoping/SKILL.md` | AI POC with binary eval criteria, golden dataset, model-selection matrix, exit gates |
| `skills/ai-on-saas-risk-and-responsible-ai/SKILL.md` | Ten-entry AI risk register and Responsible-AI commitment with named accountable role |
| `skills/ai-on-saas-compliance-credentials/SKILL.md` | AI Trust and Compliance subsection (EU AI Act, NCAIS, NAIS, AI Policy KE/NG/ZA/UG/RW, ISO/NIST) |
| `skills/ai-on-saas-procurement-and-questionnaire/SKILL.md` | Eight-domain AI procurement answer pack |
| `skills/ai-on-saas-change-management-and-adoption/SKILL.md` | AI mindset transition: trust staging, augment-vs-replace, HITL design |
| `skills/ai-on-saas-team-composition/SKILL.md` | AI-on-SaaS roster: AI Safety Lead, Eval Engineer, MLOps, Prompt, RAG, Data-for-AI |
| `skills/ai-on-saas-vertical-positioning/SKILL.md` | Vertical AI plays for FS, insurance, public sector, healthcare, education, customer support |

## Proposer Profiles

| Profile Path | Voice | Use When |
|---|---|---|
| `skills/profiles/peter-bamuhigire.md` | First-person singular | Proposing as Peter Bamuhigire |
| `skills/profiles/chwezi-core-systems.md` | First-person plural | Proposing as Chwezi Core Systems |
| `skills/profiles/client-template.md` | Customisable | Ghostwriting on behalf of a client |

## Knowledge Base

| Reference Path | Content |
|---|---|
| `skills/references/proposal-strategy-and-persuasion.md` | S1-S2-B logic, P-I-P structure, buyer psychology, SCQA, Cialdini, Red Team review |
| `skills/references/world-class-proposal-patterns.md` | McKinsey and Deloitte proposal patterns, storyboarding, ghost packs, elevator test, prewiring |
| `skills/references/consulting-delivery-excellence.md` | McKinsey-style problem solving, Design Sprint, SCAMPER, SOSTAC, SECI, Done-Done standard |
| `skills/references/ethical-persuasion-and-evaluator-psychology-gate.md` | Ethical persuasion, evaluator concerns, risk perception, social proof discipline, and persuasion red flags |
| `skills/references/premium-rate-justification-framework.md` | Premium value stack, proof ladder, commercial options, discount rules, and price defence |
| `skills/references/discovery-question-bank-for-proposals.md` | Proposal discovery questions for outcomes, buyers, users, scope, technology, AI, support, and commercial assumptions |
| `skills/references/proposal-objection-handling.md` | Ethical handling of price, risk, timeline, staffing, technology, AI, local-context, support, and procurement objections |
| `skills/references/service-design-methodology-module.md` | Service design phases, journey mapping, blueprints, co-creation, prototypes, implementation, and acceptance criteria |
| `skills/references/website-software-maintenance-support-language.md` | Website/software/AI maintenance categories, SLA language, support commitments, client responsibilities, and pricing notes |
| `skills/references/proposal-narrative-patterns-and-case-story-spine.md` | Evaluator journey, narrative spine, case-study story cards, design rationale, and storyboard use |
| `skills/references/technical-strategy-credibility-checklist.md` | Software, SaaS, AI, cloud, API, operations, roadmap, governance, and maintainability checks |
| `skills/references/customer-service-and-escalation-commitments.md` | Service communication, escalation, complaint recovery, known-problem updates, and support boundaries |
| `skills/premium-commercial-writing/references/premium-writing-quality-gate.md` | Cross-cutting gate for professional, persuasive, premium-fee-worthy writing |
| `skills/premium-commercial-writing/references/document-section-patterns.md` | Patterns for cover letters, executive summaries, proposal sections, case studies, business documents, and blogs |
| `skills/premium-commercial-writing/references/seo-ai-search-writing.md` | Search-intent, SEO, and AI-search guidance for public-facing content |
| `skills/premium-commercial-writing/references/book-extractions-audit-synthesis.md` | Copyright-safe book and EPUB inspiration rules plus current audit status |
| `skills/critical-analysis-business-logic/references/reasoning-and-business-sense-gate.md` | Essential questions, argument map, mental-model pass, business-sense checks, and achievability gate |
| `skills/consulting-frameworks/references/` | Problem structuring, financial analysis, strategy, operations, communication |
| `skills/business-analysis-tools/references/` | SWOT, PESTLE, gap analysis, requirements planning, fit criteria, transition evaluation, maturity models |

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
