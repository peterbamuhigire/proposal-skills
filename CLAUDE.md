# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Repository Is

This is a Markdown-based skill repository for generating professional consulting proposals, Expressions of Interest, procurement responses, and related content for the East and Central African consulting market. There is no buildable application.

`AGENTS.md` exists at the repository root as a Codex-compatible routing layer. Keep `CLAUDE.md` as the Claude-specific operating file; the two documents should remain complementary rather than duplicative.

Every `SKILL.md` in this repository must place this exact line immediately below the first top-level `# ...` heading, not in frontmatter: `Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.`

The live catalogue contains 107 active entrypoints under `skills/`, including the parent router. Authoring follows `docs/skill-authoring-standard.md`; local release gates are `python -X utf8 scripts/validate_skills.py --baseline quality-baseline.json` and `python -X utf8 scripts/routing_smoke_test.py`.

## Repository Architecture

Active skills live under `skills/`. Load `skills/SKILL.md` first for full proposal orchestration, then load the specific section, profile, sector, or domain skill required by the task.

### Skill Categories

All sub-skills are grouped into 12 thematic categories under `skills/<category>/<skill-name>/`:

| Category | Count | Purpose |
|---|---|---|
| `skills/pipeline/` | 10 | Numbered proposal section skills (01-cover-letter through 10-financial-proposal) |
| `skills/profiles-sectors/` | 16 | Profile router, sector router, procurement frameworks, and sector skills; shared references are not active skills |
| `skills/domain-delivery/` | 16 | Cross-cutting delivery domains including GIZ/EU response, EAC e-commerce BDS, finance advisory, and retail transformation |
| `skills/strategy-positioning/` | 10 | Positioning, premium, discovery/objection, storytelling, service design, AI transformation, website, embedded accounting, critical analysis, support/maintenance |
| `skills/saas-proposals/` | 14 | SaaS implementation and SaaS product-development proposal skills |
| `skills/ai-on-saas-proposals/` | 11 | AI-on-SaaS combined methodology and supporting skills |
| `skills/ai-agent-proposals/` | 11 | Agent / multi-agent product proposal skills |
| `skills/ai-agent-commercial/` | 8 | Agent SLA, packaging, contract, outcome pricing, MSA addendums, renewals |
| finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`) | — | Finance and accounting module skills (IFRS, IAS, reconciliation, controls, audit) — for finance/accounting/IFRS/IAS work, use the finance engine |
| `skills/writing-content/` | 3 | Blog and premium commercial writing |
| `skills/language/` | 2 | East African English and language standards |
| `skills/meta/` | 5 | Skill maintenance plus anti-slop quality: skill-writing, skill-safety-audit, update-claude-documentation, anti-ai-slop (real-time guardrail), ai-slop-audit (per-section auditor; blocks on grade F) |

Router `skills/SKILL.md` and per-skill `skills/<category>/<skill>/SKILL.md` paths are canonical throughout this repo (CLAUDE.md, AGENTS.md, README.md, book-extractions). When adding a new skill, place it in the right category directory and update routing files accordingly.

### Parent Skill
- `skills/SKILL.md` - parent proposal-writing router for proposal sections, domain skills, profiles, sectors, and cross-cutting references.

### Proposal Section Sub-Skills
Each numbered sub-skill lives in its own directory with a `SKILL.md` and optional `references/` folder:

- `skills/pipeline/01-cover-letter/` - cover letter and submission sheet
- `skills/pipeline/02-executive-summary/` - four differentiators, scope table, value proposition
- `skills/pipeline/03-understanding-of-assignment/` - background, objectives, scope, ToR comments
- `skills/pipeline/04-firm-profile/` - firm overview, service areas, sector expertise, individual consultant format
- `skills/pipeline/05-relevant-experience/` - summary table plus project cards with the outcomes rule
- `skills/pipeline/06-methodology/` - conceptual approach, phased plans, risk table, QA, governance
- `skills/pipeline/07-team-composition/` - organogram, World Bank TECH-6 format, narrative format, CV rules
- `skills/pipeline/08-work-plan/` - Gantt table, milestones, staffing schedule
- `skills/pipeline/09-expression-of-interest/` - shorter EoI-specific structure
- `skills/pipeline/10-financial-proposal/` - FIN forms, fee breakdown, reimbursables, payment schedule, day rate ranges

### Supporting Domain Skills
These cross-cutting knowledge bases support proposal sections and can also generate standalone sections when a ToR requires them.

- `skills/domain-delivery/project-management/` - PM frameworks, governance, reporting, steering committees
- `skills/domain-delivery/change-management/` - OCM frameworks, adoption strategies, resistance management
- `skills/domain-delivery/monitoring-and-evaluation/` - log frames, results frameworks, KPIs, theory of change
- `skills/domain-delivery/stakeholder-engagement/` - stakeholder mapping, consultation approaches, communication plans
- `skills/domain-delivery/capacity-building/` - training models, ToT, knowledge transfer, skills sustainability
- `skills/domain-delivery/gender-and-social-inclusion/` - GESI frameworks, disability and youth inclusion
- `skills/domain-delivery/environmental-and-social-safeguards/` - ESIA, environmental management plans, World Bank ESF, AfDB ISS
- `skills/domain-delivery/data-management/` - data collection, MIS design, data governance, data protection law
- `skills/strategy-positioning/ai-transformation-proposal/` - AI applications, agentic workflows, analytics, automation, governance, evaluation, operations, and maintenance proposals
- `skills/strategy-positioning/website-design-proposal-strategy/` - website design/development proposal philosophy, stack explanation, UX/content/SEO methodology, costing drivers, QA, launch, handover, and support
- `skills/strategy-positioning/premium-client-proposal-strategy/` - executive, enterprise, affluent, high-ticket, premium, and strategic transformation proposal positioning
- `skills/strategy-positioning/premium-pricing-and-value-defense/` - premium fee justification, commercial options, value stack, and price defence
- `skills/writing-content/premium-commercial-writing/` - cross-cutting premium commercial writing for proposals, cover letters, executive summaries, case studies, business documents, public content, and SEO/AI-search friendly thought leadership where relevant
- `skills/strategy-positioning/sales-discovery-and-objection-handling/` - discovery question banks, buyer qualification, objection handling, and follow-up logic
- `skills/strategy-positioning/service-design-proposal-strategy/` - service design, customer/citizen experience, journey mapping, blueprints, co-creation, and implementation evidence
- `skills/strategy-positioning/proposal-storytelling-and-evaluator-journey/` - evaluator journey, narrative spine, case-story structure, design rationale, and sign-off flow
- `skills/strategy-positioning/customer-service-and-maintenance-proposals/` - support, maintenance, SLAs, escalation, incident response, managed services, and post-launch optimisation
- `skills/domain-delivery/sustainability-planning/` - exit strategies, institutional embedding, ownership transfer
- `skills/domain-delivery/risk-management/` - risk registers, mitigation frameworks, escalation triggers
- `skills/domain-delivery/business-analysis-tools/` - SWOT, PESTLE, gap analysis, benchmarking, CBA, maturity models, prioritisation matrices
- `skills/domain-delivery/consulting-frameworks/` - problem structuring, financial analysis, strategy, operations, and communication frameworks
- `skills/domain-delivery/retail-transformation-proposal/` - retail transformation, omnichannel, e-commerce operations, POS, merchandising, pricing, promotions, markdowns, loyalty, CRM, fulfilment, returns, store operations, shrink, vendor terms, private label, planogram, new-store opening, and retail KPI/WBR proposals
- `skills/strategy-positioning/critical-analysis-business-logic/` - cross-cutting reasoning, evaluator logic, business sense, feasibility, and achievability gate

### SaaS Implementation and SaaS Product-Development Skills

These skills bring the engine to Bain/EY/McKinsey-grade quality for SaaS implementation and SaaS product-development engagements. Load when the bid is SaaS-related.

- `skills/saas-proposals/saas-discovery-and-qualification/` - SaaS discovery (ICP, Critical Event, pain chain, impact per role, decision process, MEDDPICC qualification).
- `skills/saas-proposals/saas-business-case-and-roi-modeling/` - TCO, time-to-value, CAC payback, LTV, ROI, NPV, sensitivity; Rule of 40 for investor-grade buyers.
- `skills/saas-proposals/saas-pricing-and-packaging-proposal/` - subscription, usage, hybrid, enterprise tiering, expansion, freemium, price-increase clauses.
- `skills/saas-proposals/saas-implementation-methodology/` - end-to-end SaaS implementation methodology: control plane, application plane, tenant isolation, observability, billing integration, onboarding automation.
- `skills/saas-proposals/saas-poc-and-pilot-scoping/` - POC and pilot scoping with explicit success criteria, exit criteria, and time-box.
- `skills/saas-proposals/saas-procurement-and-security-questionnaire/` - procurement path, security questionnaire pack, DPA / MSA / SLA, data residency, exit clauses.
- `skills/saas-proposals/saas-customer-success-and-adoption-proposal/` - customer success engagement package: onboarding, activation, success plan, QBR, expansion plays, save plays, health scoring.
- `skills/saas-proposals/saas-mutual-action-planning-and-close-plans/` - MAP from selection to value realisation; close plan from BAFO to signature.
- `skills/saas-proposals/saas-vertical-positioning/` - vertical positioning for financial services, insurance, public sector, healthcare, education.
- `skills/saas-proposals/saas-objection-handling-and-competitive-displacement/` - objection handling and competitive displacement plays.
- `skills/saas-proposals/saas-lifecycle-communications-as-deliverable/` - six lifecycle programs as priced workstreams.
- `skills/saas-proposals/saas-trust-and-compliance-credentials-section/` - Trust and Compliance section template.
- `skills/saas-proposals/saas-multi-tenant-architecture-credibility-block/` - architectural credibility paragraphs for Methodology.
- `skills/saas-proposals/saas-pilot-to-rollout-change-management/` - SaaS mindset transition and change management.

The supporting reference library lives under `skills/profiles-sectors/references/` with file names starting `saas-` and `vertical-saas-`. See `book-extractions/saas-proposal-skills-audit-2026.md` for the full inventory and derivation from the seven SaaS books processed in 2026.

### AI-on-SaaS Skills

These skills bring the engine to Bain/EY/McKinsey-grade quality for engagements that build AI features (RAG, copilots, agents, AI analytics, AI-assisted decisioning) into a multi-tenant SaaS product. Load when the bid is AI-on-SaaS. Use `ai-on-saas-combined-methodology` as the headline; layer the rest on top.

- `skills/ai-on-saas-proposals/ai-on-saas-combined-methodology/` — three-plane methodology (control / application / AI); phases, gates, deliverables with binary AI acceptance criteria.
- `skills/ai-on-saas-proposals/ai-on-saas-discovery-and-qualification/` — eight AI-on-SaaS qualifying lines (workflow-AI fit, data, hallucination tolerance, maturity, change-readiness, regulator, model-provider, tenant variation).
- `skills/ai-on-saas-proposals/ai-on-saas-business-case-and-roi/` — AI Value Stack, AI Cost Stack, eval-margin, cost-of-tokens at P50/P90/P99, three-scenario ROI, downside scenarios.
- `skills/ai-on-saas-proposals/ai-on-saas-pricing-and-packaging-proposal/` — five AI pricing patterns, model-by-tier, fair-use, price-increase, FX clauses, worked examples.
- `skills/ai-on-saas-proposals/ai-on-saas-poc-and-pilot-scoping/` — AI POC with binary eval criteria, golden dataset, model-selection matrix, hallucination ceiling, abstain logic, exit gates.
- `skills/ai-on-saas-proposals/ai-on-saas-risk-and-responsible-ai/` — AI risk register (ten core risks) and Responsible-AI commitment with named accountable role.
- `skills/ai-on-saas-proposals/ai-on-saas-compliance-credentials/` — AI Trust and Compliance subsection (EU AI Act, NCAIS, NAIS, AI Policy KE/NG/ZA/UG/RW, ISO 42001/23894, NIST AI RMF, sectoral).
- `skills/ai-on-saas-proposals/ai-on-saas-procurement-and-questionnaire/` — eight-domain AI procurement answer pack.
- `skills/ai-on-saas-proposals/ai-on-saas-change-management-and-adoption/` — AI mindset transition, trust staging, augment-vs-replace, HITL design.
- `skills/ai-on-saas-proposals/ai-on-saas-team-composition/` — AI-on-SaaS roster (AI Safety Lead, Eval Engineer, MLOps, Prompt, RAG, Data-for-AI) with RACI and ramp curve.
- `skills/ai-on-saas-proposals/ai-on-saas-vertical-positioning/` — vertical AI plays (FS, insurance, public sector, healthcare, education, customer support).

The supporting reference library lives under `skills/profiles-sectors/references/` with file names starting `ai-on-saas-` and `vertical-ai-on-saas-`. See `book-extractions/ai-on-saas-proposal-audit-2026.md` for the full audit and rationale.

### AI-Agent / Multi-Agent Product Skills

These skills bring the engine to Bain/EY/McKinsey-grade quality for engagements that design, build, or operate AI agents (LLM systems that plan, call tools, decide, and act) — as stand-alone products, multi-agent systems, or agentic layers inside SaaS products. Load when the bid is agentic. Use `ai-agent-methodology` as the headline; layer the rest on top. Load alongside the `ai-on-saas-*` family when the agent lives inside a multi-tenant SaaS product.

- `skills/ai-agent-proposals/ai-agent-discovery-and-qualification/` — Agent-vs-Workflow Filter; L0–L5 Autonomy Ladder; ten agent-specific discovery lines; Agentic Qualification Scorecard.
- `skills/ai-agent-proposals/ai-agent-business-case-and-roi/` — Agent Value Stack + Agent Cost Stack + tasks-per-FTE with intervention discount + three-scenario ROI keyed to autonomy ramp + downside (irreversible-incident, regulator action, intervention overshoot, scope-creep).
- `skills/ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/` — Six agent pricing patterns (per-resolution / per-outcome / per-step / per-agent / hybrid / success-based); intervention credit; vendor cost pass-through; abort-and-refund; autonomy-ramp clause; FX.
- `skills/ai-agent-proposals/ai-agent-poc-and-pilot-scoping/` — Three-stage pilot (Shadow / Supervised / Agentic) with binary thresholds; irreversibility ceiling; intervention ceiling; kill-switch drill; abort conditions.
- `skills/ai-agent-proposals/ai-agent-methodology/` — Headline agentic methodology: eight phases (Discover → Action-Catalogue → Architecture → Build → Shadow → Supervised → Agentic → Operate); gates per phase; eval and red-team strategy; kill-switch and drill; multi-agent orchestration.
- `skills/ai-agent-proposals/ai-agent-risk-and-responsible-ai/` — Twelve-entry agent risk register; Responsible-AI Agent Commitment template with named Agent Safety Lead; regulator mapping.
- `skills/ai-agent-proposals/ai-agent-compliance-credentials/` — Trust and Compliance for Agents: action audit log, irreversibility gating, intervention SLO, kill-switch architecture and drill, agent red-team catalogue, identity policy, action-scope attestation, multi-agent governance, transparency-to-affected-party, sovereign-AI option.
- `skills/ai-agent-proposals/ai-agent-procurement-and-questionnaire/` — Ten-domain agent procurement answer pack.
- `skills/ai-agent-proposals/ai-agent-change-management-and-adoption/` — Trust staging with named evidence; augment / redeploy / retrain framing; funded supervisor retraining curriculum; agent-on-your-behalf disclosure UX; adoption metrics specific to agents.
- `skills/ai-agent-proposals/ai-agent-team-composition/` — Agent roster: Agent Architect, Tool Engineer, Agent Safety Lead, Eval Engineer, Red-Team Lead, Human-in-the-loop Designer, Multi-Agent Orchestrator Engineer (where applicable), Agent Ops Lead, plus buyer-side counterparts (Two-of-Everything).
- `skills/ai-agent-proposals/ai-agent-vertical-positioning/` — Vertical agent plays for customer support (resolution agents), financial services (compliance / reconciliation), insurance (claims triage), public sector (extreme caution, sovereign-AI), healthcare (admin-only), legal (drafting / review with lawyer-final), operations (alerting / triage / coding agents).

The supporting reference library lives under `skills/profiles-sectors/references/` with file names starting `ai-agent-` and `vertical-ai-agent-`. See `book-extractions/agent-products-proposal-audit-2026.md` for the full audit and rationale.

### AI-Agent Commercial / SLA / Contract Skills

These skills carry the **contractual and commercial layer** for agentic engagements — SLA classes with credit schedules, refund and abort mechanics, MSA / SLA addendums, outcome-pricing structures, packaging shapes, procurement-objection responses on commercials, renewal mechanics. Load alongside the `ai-agent-*` product family when the proposal moves from value narrative to contract-grade exhibits.

- `skills/ai-agent-commercial/ai-agent-sla-and-credit-schedule/` — Bronze / Silver / Gold / Platinum SLA class table on four metrics (availability + task-success + intervention rate + time-to-resolve) plus three guardrails (kill-switch, audit-log completeness, intervention SLA), with credit schedule, service-credit cap, and out-clauses.
- `skills/ai-agent-commercial/ai-agent-commercial-packaging/` — Agent Included in Pro vs Add-on vs Standalone shapes with worked decision matrix, SLA-class alignment, renewal posture, cost recovery shape.
- `skills/ai-agent-commercial/ai-agent-contract-language-pack/` — Drop-in exhibit assembly — pricing exhibit, SLA exhibit, credit and refund exhibit, MSA addendum, abandonment-and-refund policy, dispute resolution, audit rights — with trade-not-give discipline.
- `skills/ai-agent-commercial/ai-agent-success-fee-and-outcome-pricing/` — Gain-share, success-fee, hybrid base-plus-success, performance-corridor structures with success-definition discipline (counter-example rule, cooling-off, attribution test) and downside protection.
- `skills/ai-agent-commercial/ai-agent-intervention-credit-and-abort-refund/` — Intervention-credit formula, credit cap, customer-facing monthly statement, five abort-and-refund triggers, pro-rata refund formula.
- `skills/ai-agent-commercial/ai-agent-msa-and-sla-addendum-templates/` — Eight agent-specific MSA clauses (action accountability, audit-log retention, kill-switch SLA, fee-for-evidence-pack, irreversible-action sub-cap, model-provider force-majeure, agent-identity warranty, intervention SLA) plus SLA addendum.
- `skills/ai-agent-commercial/ai-agent-procurement-objections-on-commercials/` — Ten common procurement asks with trade-not-give responses; ethical commercial-objection discipline.
- `skills/ai-agent-commercial/ai-agent-renewal-and-true-up/` — Auto / express / hybrid renewal, true-up, ramp-down protection, autonomy-progression price-step, index-linked renewal, FX corridor.

The commercial layer references live under `skills/profiles-sectors/references/` with names starting `ai-agent-sla-`, `ai-agent-pricing-exhibit-`, `ai-agent-credit-`, `ai-agent-msa-addendum-`, `ai-agent-outcome-pricing-`, `ai-agent-abandonment-`, `ai-agent-packaging-`, `ai-agent-dispute-`, `ai-agent-commercial-objection-`, `ai-agent-renewal-`, `ai-agent-success-definition-`, `ai-agent-vendor-cost-pass-through`. See `book-extractions/agent-sla-commercial-proposal-audit-2026.md` for the full audit and rationale.

### Profiles, References, Sectors, and Meta Skills
- `skills/profiles-sectors/profiles/SKILL.md` - profile routing and selection rules. Load exactly one profile before generating proposal content.
- `skills/profiles-sectors/profiles/peter-bamuhigire.md` - individual consultant profile.
- `skills/profiles-sectors/profiles/chwezi-core-systems.md` - company profile.
- `skills/profiles-sectors/profiles/client-template.md` - ghostwriting template.
- `skills/profiles-sectors/references/` - cross-cutting proposal strategy, persuasion, world-class proposal patterns, consulting delivery excellence, ethical evaluator psychology, premium pricing, discovery, objection handling, service design, support commitments, narrative patterns, and technical strategy credibility.
- `skills/writing-content/premium-commercial-writing/references/` - premium writing quality gate, document and section patterns, SEO/AI-search writing guidance, and book-extractions audit/synthesis rules.
- `skills/profiles-sectors/sectors/SKILL.md` - procurement and sector routing. Sector directories include PPDA Uganda, World Bank, AfDB, UNDP, and industry-specific sectors.
- `skills/writing-content/blog-idea-generator/` and `skills/writing-content/blog-writer/` - content creation skills, used only for publishing tasks.
- `skills/language/east-african-english/` and `skills/language/language-standards/` - cross-cutting language and tone standards.
- `skills/meta/skill-writing/`, `skills/meta/skill-safety-audit/`, and `skills/meta/update-claude-documentation/` - maintenance skills.
- `skills/meta/anti-ai-slop/` - real-time anti-slop guardrail applied while writing every proposal section.
- `skills/meta/ai-slop-audit/` - per-section and per-iteration slop auditor that grades A/B/C/F and blocks submission on grade F.

## Proposal Workspace

Proposals are developed in a local `proposals/` directory, which is gitignored and must not be committed. When a consultant starts Claude Code in this repository, follow this initialization workflow:

1. Check if `proposals/` exists. If not, create it with an `INDEX.md`.
2. Ask the user what proposal they are working on, including client name, assignment title, and deadline.
3. Create the proposal directory as `proposals/YYYY-MM-DD-short-name/`.
4. Update `proposals/INDEX.md` with the new proposal entry.
5. Ask the user to place ToR, RFP, adverts, or templates in `terms/` and team CVs in `team/`.
6. After materials are in place, read the terms and invoke the brainstorming workflow. Save the brainstorm output as `BRIEF.md`.
7. Write sections one at a time into the proposal section files, loading the relevant sub-skill such as `skills/pipeline/01-cover-letter/SKILL.md` before writing each section.
8. Generate tables as Excel or CSV files in `sheets/`.
9. Compile final `.docx` files into `output/`, usually as separate technical and financial proposals.

Expected proposal directory:

```text
proposals/
├── INDEX.md
└── 2026-03-15-client-short-name/
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

Status values in `proposals/INDEX.md`: `Brainstorming`, `Drafting`, `Review`, `Final`, `Submitted`.

## Key Conventions

- British English always: organisation, programme, centre, colour, travelling, specialise.
- East African professional tone: formal, respectful, courteous, and free of marketing hype.
- Voice is determined by the proposer profile: first-person plural for companies and first-person singular for individual consultants.
- Dates use day-month-year format, such as 17 February 2026.
- Avoid AI-sounding vocabulary such as delve, tapestry, landscape as metaphor, leverage, navigate as metaphor, foster, realm, harness, synergy, embark, robust, vibrant, holistic, and seamless.
- Every past project card must state what was achieved, not just what was done.
- Every high-stakes claim must have visible logic: evidence, warrant, assumptions, countercase, and practical implication.
- Methodology, staffing, timeline, financial proposal, risk controls, and M&E must be mutually achievable, not merely well written.

## Anti-Slop Quality Gate

Two paired skills under `skills/meta/` keep proposal output free of AI slop. They sit alongside the reasoning gate at `skills/strategy-positioning/critical-analysis-business-logic/`: the critical-analysis gate tests whether the logic is sound, and the anti-slop pair tests whether the writing reads as authored, specific, and verified.

- `skills/meta/anti-ai-slop/` applies in REAL TIME on every proposal section. Use it as a live constraint while drafting each cover letter, executive summary, understanding-of-assignment, methodology, work plan, team composition, procurement response, and financial proposal, so slop is corrected in place rather than in a cleanup pass. It carries the specificity floor, verify-before-write, authored-voice, cover-the-hard-parts rules and the merged banned-vocabulary list.
- `skills/meta/ai-slop-audit/` runs AFTER EACH section or major iteration, and AUTO-RUNS whenever the user asks to analyse, review, evaluate, audit, critique, or de-slop any proposal artefact. It also runs as the final gate before assembly or submission. It produces a graded report (A/B/C/F) with per-marker evidence and a concrete fix for each finding.
- Grade **F (Blocked)** blocks submission. Do not progress to the next section or assemble the proposal until the blocking findings are fixed.

## Adding a New Sub-Skill

1. Read `docs/skill-authoring-standard.md`, then create a subdirectory under `skills/` with a `SKILL.md` using frontmatter limited to `name`, `description`, and portable `metadata`.
2. Include the required acknowledgement line immediately below the first top-level heading.
3. Add input, output, evidence, capability, degraded-mode, decision, stop/recovery, quality, anti-pattern, and reference contracts; use `templates/skill-template.md`.
4. Add a local `references/` subdirectory only when the skill needs deeper supporting material, and link each reference back to its parent.
5. Update routing fixtures and run the local validator, routing smoke test, canonical scanner, canonical quick validator, safety gate, and anti-slop gate.
6. Update `skills/SKILL.md`, `README.md`, `AGENTS.md`, and this file when routing or inventory changes.

## Supported Procurement Frameworks

PPDA Uganda, World Bank TECH-1 through TECH-6 and FIN-1 through FIN-4, AfDB, UNDP and UN system donor formats, and direct client RFPs.


## Finance & Accounting Trigger

For finance/accounting/IFRS/IAS work, use the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine` whenever the user's request, the artefact being generated, or the code being edited touches **any** of:

- Money flows: sales, purchases, payments, refunds, credit notes, expenses
- Stock and inventory
- Payroll
- Tax (VAT, PAYE, WHT, NSSF, income tax, customs, excise, EFRIS, eTIMS)
- Grants, donations, donor restrictions
- Banking, mobile money, POS, card settlement, cash drawer
- Fixed assets
- Financial reports, management accounts, statutory returns
- Chart of Accounts, journals, ledger, posting services, period state, audit trail
- Reconciliation, close, migration, opening balances
- Internal controls, audit, evidence packs
- Any IFRS or IFRS for SMEs section

When the trigger fires:

1. For finance/accounting/IFRS/IAS work, use the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine`.
2. Read the relevant doctrine reference file in the finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`).
3. Read the corresponding skill `SKILL.md` in the finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`).
4. Apply the **finance & accounting quality gate** from the finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`).
5. Record the gate run in the artefact manifest.

The `finance-module-audit` skill (the corresponding skill in the finance engine, `C:\wamp64\www\chwezi-accounting-doctrine`) auto-runs whenever the user asks to analyse, review, audit, build, propose, or replace any software system with even a slight finance element.


<!-- design-system-skills:trigger v1 -->
### Design / typography / UI/UX (cross-cutting — consult IN ADDITION)

Any work touching how an artifact LOOKS — font/typeface choice, type scale, colour, layout/grid,
visual identity, web/desktop/mobile UI screens, or the visual formatting of a DOCX/PPTX/PDF/XLSX
— routes to the **`design-system-skills`** engine, the single home for ALL design/UI/UX skills
and the anti-AI-slop doctrine.

**Resolve its location on THIS device from your global engine-routing table** (`~/.claude/CLAUDE.md`,
or `AGENTS.md` for Codex) — never assume an absolute path; it varies per machine. Then read its
`README.md` → `doctrine/design-doctrine.md` → glob `skills/**/SKILL.md` fresh and route by
frontmatter (read SKILL.md directly, not via the Skill tool). Content and structure stay in THIS
engine; presentation comes from design-system-skills. Hard rule: never use a banned AI-slop font
(Inter, Geist, Roboto, Arial, Open Sans, Lato, Space Grotesk, bare system stacks) as primary
type — state the chosen typeface and reason before producing any artifact.
<!-- /design-system-skills:trigger -->
