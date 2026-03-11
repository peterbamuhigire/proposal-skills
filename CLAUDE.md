# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A collection of Claude Code skills for generating professional consulting proposals, Expressions of Interest, and blog content — tailored for the East and Central African consulting market (Uganda, Kenya, Rwanda, Tanzania, and neighbouring markets). There is no buildable application; the repository is entirely Markdown-based skill definitions and reference documents.

## Repository Architecture

### Parent Skill: `SKILL.md` (root)
The `proposal-writing` parent skill routes to the correct sub-skill based on what section or document type is needed. It defines cross-cutting standards (British English, East African tone, first-person plural, `.docx` output).

### Proposal Sub-Skills
Each sub-skill lives in its own directory with a `SKILL.md` and optional `references/` folder:

- `cover-letter/` — cover letter and submission sheet
- `relevant-experience/` — past projects with outcomes (most heavily weighted in evaluation)
- `methodology/` — approach, phase-by-phase plan, risk register, deliverables
- `financial-proposal/` — separate sealed document with fees, reimbursables, payment schedule

### Content Creation Skills
- `blog-idea-generator/` — generates 15–25 blog topic ideas using a 20-method ideation library
- `blog-writer/` — full article pipeline with SEO, bilingual output (EN/FR), and Astro page building

### Cross-Cutting Language Skills
- `east-african-english/` — tone, British spelling, courteous phrasing for all output
- `language-standards/` — multi-language standards covering English, French, and Kiswahili

### Meta Skills
- `skill-writing/` — guide for creating and updating skills in this repository
- `skill-safety-audit/` — scans skills for unsafe instructions
- `update-claude-documentation/` — updates project documentation files

## Key Conventions

- **British English always**: organisation, programme, centre, colour, travelling, specialise
- **East African professional tone**: formal, respectful, courteous — no marketing hype or AI-sounding vocabulary
- **First-person plural in proposals**: "We propose…", "Our team will…"
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
