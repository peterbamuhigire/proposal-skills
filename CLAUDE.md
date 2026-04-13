# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A collection of Claude Code skills for generating professional consulting proposals, Expressions of Interest, and blog content — tailored for the East and Central African consulting market (Uganda, Kenya, Rwanda, Tanzania, and neighbouring markets). There is no buildable application; the repository is entirely Markdown-based skill definitions and reference documents.

## Repository Architecture

`AGENTS.md` now exists at the repository root as a Codex-compatible routing layer. Keep `CLAUDE.md` as the Claude-specific operating file; the two documents should remain complementary rather than duplicative.

### Parent Skill: `SKILL.md` (root)
The `proposal-writing` parent skill routes to the correct sub-skill based on what section or document type is needed. It defines cross-cutting standards (British English, East African tone, first-person plural, `.docx` output).

### Proposal Section Sub-Skills (numbered — follow proposal order)
Each sub-skill lives in its own directory with a `SKILL.md` and optional `references/` folder:

- `01-cover-letter/` — cover letter and submission sheet
- `02-executive-summary/` — four differentiators, scope table, value proposition
- `03-understanding-of-assignment/` — background, objectives, scope, ToR comments
- `04-firm-profile/` — firm overview, service areas, sector expertise, individual consultant format
- `05-relevant-experience/` — summary table + project cards, the outcomes rule
- `06-methodology/` — conceptual approach, phased plans (ICT and consulting variants), risk table
- `07-team-composition/` — organogram, WB TECH-6 format, narrative format, CV rules
- `08-work-plan/` — Gantt table, milestones, staffing schedule
- `09-expression-of-interest/` — shorter EoI-specific structure
- `10-financial-proposal/` — FIN forms, fee breakdown, reimbursables, payment schedule, day rate ranges

### Supporting Domain Skills (unnumbered — reference libraries + standalone generators)
These are cross-cutting knowledge bases that proposal sections draw from. Each can also generate a standalone section when a ToR explicitly requires it.

- `project-management/` — PM frameworks (PRINCE2, PMBoK, Agile), governance, reporting, steering committees
- `change-management/` — OCM frameworks (ADKAR, Kotter), adoption strategies, resistance management
- `monitoring-and-evaluation/` — log frames, results frameworks, KPIs, theory of change
- `stakeholder-engagement/` — stakeholder mapping, consultation approaches, communication plans
- `capacity-building/` — training models, ToT, knowledge transfer, skills sustainability
- `gender-and-social-inclusion/` — GESI frameworks, gender mainstreaming, disability and youth inclusion
- `environmental-and-social-safeguards/` — ESIA, environmental management plans, WB ESF, AfDB ISS
- `data-management/` — data collection, MIS design, data governance, data protection law
- `sustainability-planning/` — exit strategies, institutional embedding, ownership transfer
- `risk-management/` — risk registers, mitigation frameworks, escalation triggers
- `business-analysis-tools/` — SWOT, PESTLE, gap analysis, benchmarking, CBA, maturity models, prioritisation matrices
- `consulting-frameworks/` — analytical building blocks for methodology design: problem structuring (8 first-principles, MECE, issue trees), financial analysis (expected value, breakeven, cannibalisation), strategy (market entry, competitive response, build/buy/partner), operations (bottleneck, stakeholder-based), communication (SCORE, recommendations, exhibit interpretation)

### Proposer Profiles: `profiles/`
- `profiles/peter-bamuhigire.md` — Individual consultant profile (first-person singular voice)
- `profiles/chwezi-core-systems.md` — Company profile (first-person plural voice)
- `profiles/client-template.md` — Template for ghostwriting on behalf of clients
- `profiles/SKILL.md` — Profile routing and selection rules

Load exactly one profile before generating any proposal content. The profile determines voice, signatory, credentials, experience, and branding throughout the document.

### Cross-Cutting References: `references/`
- `references/proposal-strategy-and-persuasion.md` — the persuasion layer: S1→S2→B baseline logic, P-I-P structure, buyer psychology, theme architecture, SCQA narrative spine, hypothesis-driven methodology, Pyramid of Ideas, Cialdini's persuasion principles, pre-emptive objection neutralisation, Red Team review process. Read before writing ANY proposal section.
- `references/world-class-proposal-patterns.md` — patterns from McKinsey/Deloitte: quantification, named frameworks, buyer role awareness, theme weaving, storyboarding, ghost packs, elevator test, budget proposal architecture, Sweet Spot positioning, prewiring
- `references/consulting-delivery-excellence.md` — implementation quality standards: McKinsey problem-solving process, 6-Step Consulting Workflow, Done-Done standard, VRM, Drucker's Five Questions, Design Thinking, Griffin Dilemma Framework, Theory of Abandonment. Read when writing methodology or implementation sections.

### Content Creation Skills
- `blog-idea-generator/` — generates 15–25 blog topic ideas using a 20-method ideation library
- `blog-writer/` — full article pipeline with SEO, bilingual output (EN/FR), and Astro page building

### Cross-Cutting Language Skills
- `east-african-english/` — tone, British spelling, courteous phrasing for all output
- `language-standards/` — multi-language standards covering English, French, and Kiswahili

### Sectors and Procurement Frameworks: `sectors/`
Reference documentation that proposal skills load for context. See `sectors/SKILL.md` for the full list.

- **Procurement frameworks** (how bids must be packaged): `ppda-uganda/`, `world-bank/`, `afdb/`, `undp/`
- **Industry sectors** (domain-specific content): `agriculture/`, `health/`, `education/`, `ict/`, `financial-services/`, `energy/`, `water-sanitation/`, `transport-infrastructure/`, `governance/`

Each sector directory now has its own `SKILL.md` so sector context is loadable as a first-class skill rather than only passive reference material.

### Meta Skills
- `skill-writing/` — guide for creating and updating skills in this repository
- `skill-safety-audit/` — scans skills for unsafe instructions
- `update-claude-documentation/` — updates project documentation files

## Proposal Workspace — How Proposals Are Built

Proposals are developed in a local `proposals/` directory (gitignored — never committed). When a consultant starts Claude Code in this repository, follow this initialization workflow:

### First-Run Initialization

1. **Check** if `proposals/` exists. If not, create it with an `INDEX.md`.
2. **Ask** the user: "What proposal are you working on?" — get the client name, assignment title, and deadline.
3. **Create** the proposal directory: `proposals/YYYY-MM-DD-short-name/` with this structure:

```
proposals/
├── INDEX.md                              # Master index of all proposals
└── 2026-03-15-client-short-name/
    ├── BRIEF.md                          # Brainstorm output — the design spec driving all writing
    ├── 01-cover-letter.md                # One MD per proposal section
    ├── 02-executive-summary.md
    ├── 03-understanding-of-assignment.md
    ├── 04-firm-profile.md
    ├── 05-relevant-experience.md
    ├── 06-methodology.md
    ├── 07-team-composition.md
    ├── 08-work-plan.md
    ├── 09-financial-proposal.md
    ├── terms/                            # ToR, RFP, adverts, client-provided templates
    ├── sheets/                           # Excel/CSV for tabular sections (staffing, budget, work plan)
    ├── team/                             # CVs and team member details for this bid
    ├── research/                         # Background materials, sector reports, client intel
    └── output/                           # Final compiled docx files (technical + financial)
```

4. **Update** `proposals/INDEX.md` with the new proposal entry.
5. **Ask** the user to paste any materials (ToR, RFP, advert, templates) into `terms/` and any team CVs into `team/`.
6. **After materials are in place**, read the terms and invoke the brainstorming skill to design the proposal approach. The brainstorm output becomes `BRIEF.md`.
7. **Write sections** one at a time into the section MDs, loading the relevant sub-skill (`01-cover-letter/SKILL.md` etc.) before writing each section.
8. **Generate tables** (staffing schedule, work plan Gantt, budget breakdown, deliverables table) as Excel/CSV files in `sheets/`.
9. **Compile** final docx files into `output/` — typically `technical-proposal.docx` and `financial-proposal.docx` as separate documents.

### INDEX.md Format

```markdown
# Proposals Index

| # | Proposal | Client | Status | Directory | Created |
|---|----------|--------|--------|-----------|---------|
| 1 | ICT Systems Assessment | Ministry of Health | Brainstorming | `2026-03-15-moh-ict-assessment/` | 2026-03-15 |
```

Status values: `Brainstorming` → `Drafting` → `Review` → `Final` → `Submitted`

### Returning to an Existing Proposal

If the user wants to continue work on an existing proposal, read `proposals/INDEX.md`, show the list, and ask which one. Then read the `BRIEF.md` and any completed section MDs to pick up where they left off.

### Proposer Profile

Before writing any proposal content, ask which proposer profile to use (or check if one is specified in `BRIEF.md`):
- `profiles/peter-bamuhigire.md` — individual consultant
- `profiles/chwezi-core-systems.md` — company
- `profiles/client-template.md` — ghostwriting for a client

## Key Conventions

- **British English always**: organisation, programme, centre, colour, travelling, specialise
- **East African professional tone**: formal, respectful, courteous — no marketing hype or AI-sounding vocabulary
- **Voice determined by proposer profile**: first-person plural for companies ("We propose…"), first-person singular for individual consultants ("I propose…")
- **Dates**: day-month-year (17 February 2026), never American format
- **AI vocabulary blacklist**: never use words like delve, tapestry, landscape (metaphor), leverage, navigate (metaphor), foster, realm, harness, synergy, embark, robust, vibrant, holistic, seamless
- **Outcomes rule**: every past project card must state what was achieved, not just what was done

## Adding a New Sub-Skill

1. Create a subdirectory with a `SKILL.md` following the existing format (YAML frontmatter with `name` and `description`, then structured instructions)
2. Add a `references/` subdirectory with a `.gitkeep`
3. Update the parent `SKILL.md` routing table
4. Update `README.md`

## Supported Procurement Frameworks

PPDA (Uganda), World Bank (TECH-1–6, FIN-1–4), AfDB/UNDP donor formats, and direct client RFPs.
