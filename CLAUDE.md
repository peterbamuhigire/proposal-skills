# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A collection of Claude Code skills for generating professional consulting proposals, Expressions of Interest, and blog content — tailored for the East and Central African consulting market (Uganda, Kenya, Rwanda, Tanzania, and neighbouring markets). There is no buildable application; the repository is entirely Markdown-based skill definitions and reference documents.

## Repository Architecture

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
Reference documentation that proposal skills load for context. See `sectors/INDEX.md` for the full list.

- **Procurement frameworks** (how bids must be packaged): `ppda-uganda/`, `world-bank/`, `afdb/`, `undp/`
- **Industry sectors** (domain-specific content): `agriculture/`, `health/`, `education/`, `ict/`, `financial-services/`, `energy/`, `water-sanitation/`, `transport-infrastructure/`, `governance/`

### Meta Skills
- `skill-writing/` — guide for creating and updating skills in this repository
- `skill-safety-audit/` — scans skills for unsafe instructions
- `update-claude-documentation/` — updates project documentation files

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
