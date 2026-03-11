# Proposal Skills

A collection of Claude Code skills for generating professional consulting proposals and Expressions of Interest, tailored for the East and Central African consulting market.

---

## Overview

This repository contains skills that guide Claude in producing complete, competitive bid documents — from a single cover letter to a full technical proposal. Each skill is a focused set of instructions for one section or document type, following the conventions of winning proposals in Uganda, Kenya, Rwanda, Tanzania, and neighbouring markets.

The skills are modelled on real winning proposals including Deloitte-calibre enterprise structures and East African public sector and donor-funded bid formats (World Bank, AfDB, PPDA, UNDP).

---

## Repository Structure

```
proposal-skills/
├── README.md
└── proposal-writing/
    ├── SKILL.md                        ← Parent skill — routes to sub-skills
    ├── docs/                           ← Documentation and reference notes
    ├── blog-posts/                     ← Generated blog posts on proposal writing
    ├── cover-letter/
    │   ├── SKILL.md
    │   └── references/
    ├── executive-summary/
    │   ├── SKILL.md
    │   └── references/
    ├── understanding-of-assignment/
    │   ├── SKILL.md
    │   └── references/
    ├── firm-profile/
    │   ├── SKILL.md
    │   └── references/
    ├── relevant-experience/
    │   ├── SKILL.md
    │   └── references/
    ├── methodology/
    │   ├── SKILL.md
    │   └── references/
    ├── team-composition/
    │   ├── SKILL.md
    │   └── references/
    ├── work-plan/
    │   ├── SKILL.md
    │   └── references/
    ├── financial-proposal/
    │   ├── SKILL.md
    │   └── references/
    └── expression-of-interest/
        ├── SKILL.md
        └── references/
```

---

## Skills

### proposal-writing *(parent)*
Routes to the correct sub-skill based on what section or document type is needed. Defines the standards that apply across all sub-skills: British English spelling, East African tone, first-person plural voice, and `.docx` output via the `docx` skill.

---

### cover-letter
Generates the cover letter and technical proposal submission sheet. Enforces a client-specific opening (never boilerplate), two to three comparable past projects with outcomes, and a courteous East African closing.

### executive-summary
Generates the executive summary — the most critical section of any proposal. Covers the client's problem, the firm's four differentiators, a scope table, a high-level timeline, and a value proposition closing paragraph.

### understanding-of-assignment
Generates the background, objectives, scope, and ToR comments section. Ensures the firm's understanding is expressed in its own words, with professional comments on any ToR items that need flagging.

### firm-profile
Generates the firm or individual consultant profile. Covers legal registration, core service areas, sector expertise, geographic footprint, and certifications. Supports both firm and solo-consultant formats.

### relevant-experience
Generates the past projects section with a summary table and individual project cards. Enforces the outcomes rule — every project must state what was achieved, not just what was done.

### methodology
Generates the approach and methodology section. Covers the conceptual framework, a phase-by-phase plan with activities and deliverables, a deliverables summary table, quality assurance, project governance, and a risk register. Includes standard phase templates for both ICT system and management consulting assignments.

### team-composition
Generates the team section including an organogram, a role-responsibility table, and individual CVs. Supports both World Bank TECH-6 format and the shorter narrative format used in PPDA and smaller local bids.

### work-plan
Generates the Gantt-style work plan, milestone table, and staffing schedule. Enforces realistic timelines with client review windows and buffer built in.

### financial-proposal
Generates the complete financial proposal as a separate document: submission sheet, bid price summary, fee breakdown by expert, reimbursables breakdown, milestone payment schedule, and assumptions. Includes East African day-rate reference ranges for 2025–2026.

### expression-of-interest
Generates a complete EoI document for pre-qualification and shortlisting purposes. Shorter than a full proposal — focused on firm credentials, comparable experience, and available experts.

---

## Companion Skills

These skills from the wider repository are applied alongside proposal-writing:

| Skill | Purpose |
|---|---|
| `east-african-english` | Tone, spelling, and courteous phrasing standards for all output |
| `language-standards` | Grammar and style consistency |
| `skill-writing` | Used when creating or updating skills in this repository |

---

## Output Format

All proposal sections are generated as `.docx` Word documents using the `docx` skill. Outputs follow professional formatting conventions: consistent headings, page numbers, tables, and section numbering that mirrors the RFP or ToR structure.

---

## Supported Procurement Frameworks

- **PPDA** — Public Procurement and Disposal of Public Assets (Uganda)
- **World Bank** — TECH-1 through TECH-6 and FIN-1 through FIN-4 standard forms
- **AfDB / UNDP** — Equivalent international donor formats
- **Direct client RFPs** — Private sector, NGO, and government ministry bids

---

## References Directory

Each sub-skill has a `references/` folder for storing supporting documents — sample excerpts from past winning proposals, templates, benchmark tables, and sector-specific notes. These are loaded by Claude as needed and are not part of the skill trigger.

---

## Blog Posts

The `blog-posts/` directory stores generated articles on proposal writing, bidding strategy, and consulting practice for East African markets. Generated using the content creation skills in the wider repository.

---

## Contributing

When adding a new sub-skill:
1. Create a subdirectory under `proposal-writing/`
2. Add a `SKILL.md` following the same format and level of detail as existing sub-skills
3. Add a `references/` subdirectory with a `.gitkeep`
4. Update the parent `proposal-writing/SKILL.md` routing table
5. Update this README

---

*Built for World CLass results for the East and Central African consulting market*