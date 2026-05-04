# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Repository Is

This is a Markdown-based skill repository for generating professional consulting proposals, Expressions of Interest, procurement responses, and related content for the East and Central African consulting market. There is no buildable application.

`AGENTS.md` exists at the repository root as a Codex-compatible routing layer. Keep `CLAUDE.md` as the Claude-specific operating file; the two documents should remain complementary rather than duplicative.

Every `SKILL.md` in this repository must place this exact line immediately below the first top-level `# ...` heading, not in frontmatter: `Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.`

## Repository Architecture

Active skills live under `skills/`. Load `skills/SKILL.md` first for full proposal orchestration, then load the specific section, profile, sector, or domain skill required by the task.

### Parent Skill
- `skills/SKILL.md` - parent proposal-writing router for proposal sections, domain skills, profiles, sectors, and cross-cutting references.

### Proposal Section Sub-Skills
Each numbered sub-skill lives in its own directory with a `SKILL.md` and optional `references/` folder:

- `skills/01-cover-letter/` - cover letter and submission sheet
- `skills/02-executive-summary/` - four differentiators, scope table, value proposition
- `skills/03-understanding-of-assignment/` - background, objectives, scope, ToR comments
- `skills/04-firm-profile/` - firm overview, service areas, sector expertise, individual consultant format
- `skills/05-relevant-experience/` - summary table plus project cards with the outcomes rule
- `skills/06-methodology/` - conceptual approach, phased plans, risk table, QA, governance
- `skills/07-team-composition/` - organogram, World Bank TECH-6 format, narrative format, CV rules
- `skills/08-work-plan/` - Gantt table, milestones, staffing schedule
- `skills/09-expression-of-interest/` - shorter EoI-specific structure
- `skills/10-financial-proposal/` - FIN forms, fee breakdown, reimbursables, payment schedule, day rate ranges

### Supporting Domain Skills
These cross-cutting knowledge bases support proposal sections and can also generate standalone sections when a ToR requires them.

- `skills/project-management/` - PM frameworks, governance, reporting, steering committees
- `skills/change-management/` - OCM frameworks, adoption strategies, resistance management
- `skills/monitoring-and-evaluation/` - log frames, results frameworks, KPIs, theory of change
- `skills/stakeholder-engagement/` - stakeholder mapping, consultation approaches, communication plans
- `skills/capacity-building/` - training models, ToT, knowledge transfer, skills sustainability
- `skills/gender-and-social-inclusion/` - GESI frameworks, disability and youth inclusion
- `skills/environmental-and-social-safeguards/` - ESIA, environmental management plans, World Bank ESF, AfDB ISS
- `skills/data-management/` - data collection, MIS design, data governance, data protection law
- `skills/website-design-proposal-strategy/` - website design/development proposal philosophy, stack explanation, UX/content/SEO methodology, costing drivers, QA, launch, handover, and support
- `skills/sustainability-planning/` - exit strategies, institutional embedding, ownership transfer
- `skills/risk-management/` - risk registers, mitigation frameworks, escalation triggers
- `skills/business-analysis-tools/` - SWOT, PESTLE, gap analysis, benchmarking, CBA, maturity models, prioritisation matrices
- `skills/consulting-frameworks/` - problem structuring, financial analysis, strategy, operations, and communication frameworks
- `skills/critical-analysis-business-logic/` - cross-cutting reasoning, evaluator logic, business sense, feasibility, and achievability gate

### Profiles, References, Sectors, and Meta Skills
- `skills/profiles/SKILL.md` - profile routing and selection rules. Load exactly one profile before generating proposal content.
- `skills/profiles/peter-bamuhigire.md` - individual consultant profile.
- `skills/profiles/chwezi-core-systems.md` - company profile.
- `skills/profiles/client-template.md` - ghostwriting template.
- `skills/references/` - cross-cutting proposal strategy, persuasion, world-class proposal patterns, and consulting delivery excellence.
- `skills/sectors/SKILL.md` - procurement and sector routing. Sector directories include PPDA Uganda, World Bank, AfDB, UNDP, and industry-specific sectors.
- `skills/blog-idea-generator/` and `skills/blog-writer/` - content creation skills, used only for publishing tasks.
- `skills/east-african-english/` and `skills/language-standards/` - cross-cutting language and tone standards.
- `skills/skill-writing/`, `skills/skill-safety-audit/`, and `skills/update-claude-documentation/` - maintenance skills.

## Proposal Workspace

Proposals are developed in a local `proposals/` directory, which is gitignored and must not be committed. When a consultant starts Claude Code in this repository, follow this initialization workflow:

1. Check if `proposals/` exists. If not, create it with an `INDEX.md`.
2. Ask the user what proposal they are working on, including client name, assignment title, and deadline.
3. Create the proposal directory as `proposals/YYYY-MM-DD-short-name/`.
4. Update `proposals/INDEX.md` with the new proposal entry.
5. Ask the user to place ToR, RFP, adverts, or templates in `terms/` and team CVs in `team/`.
6. After materials are in place, read the terms and invoke the brainstorming workflow. Save the brainstorm output as `BRIEF.md`.
7. Write sections one at a time into the proposal section files, loading the relevant sub-skill such as `skills/01-cover-letter/SKILL.md` before writing each section.
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

## Adding a New Sub-Skill

1. Create a subdirectory under `skills/` with a `SKILL.md` using YAML frontmatter limited to `name` and `description`.
2. Include the required acknowledgement line immediately below the first top-level heading.
3. Add a local `references/` subdirectory only when the skill needs deeper supporting material.
4. Update `skills/SKILL.md`, `README.md`, `AGENTS.md`, and this file with the new path.

## Supported Procurement Frameworks

PPDA Uganda, World Bank TECH-1 through TECH-6 and FIN-1 through FIN-4, AfDB, UNDP and UN system donor formats, and direct client RFPs.
