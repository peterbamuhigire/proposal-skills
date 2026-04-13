# Proposal Skills

A Claude Code skills repository for generating professional consulting proposals that compete with McKinsey, Deloitte, PwC, and Bain — tailored for the East and Central African consulting market.

---

## How It Works

A consultant on the team clones this repo, opens a terminal, navigates to `proposal-skills/`, and starts Claude Code. From there, the entire proposal lifecycle is handled through conversation:

### 1. Start a New Proposal

```
cd proposal-skills
claude
```

Claude checks for the `proposals/` directory (created on first run), asks what proposal you are working on, and scaffolds the workspace:

```
proposals/
├── INDEX.md
└── 2026-03-15-moh-ict-assessment/
    ├── BRIEF.md                    # Brainstorm output — drives all writing
    ├── 01-cover-letter.md
    ├── 02-executive-summary.md
    ├── 03-understanding-of-assignment.md
    ├── 04-firm-profile.md
    ├── 05-relevant-experience.md
    ├── 06-methodology.md
    ├── 07-team-composition.md
    ├── 08-work-plan.md
    ├── 09-financial-proposal.md
    ├── terms/                      # Paste ToR, RFP, adverts here
    ├── sheets/                     # Excel/CSV tables generated here
    ├── team/                       # CVs for this bid
    ├── research/                   # Background materials, sector data
    └── output/                     # Final compiled docx files
```

### 2. Paste Your Materials

Drop the ToR, RFP, or advert into `terms/`. Drop team CVs into `team/`. Tell Claude when you are ready.

### 3. Brainstorm

Claude reads the terms, invokes the brainstorming workflow, and asks you focused questions — one at a time — to understand the assignment, identify themes, select frameworks, and design the proposal approach. The output is saved as `BRIEF.md`, which drives all subsequent writing.

### 4. Write Sections

Claude writes each section by loading the relevant skill (e.g., `06-methodology/SKILL.md`), applying the persuasion frameworks from `references/`, and following the approach defined in the brief. Sections are written into the per-proposal markdown files.

### 5. Generate Tables

Tabular sections — staffing schedule, work plan Gantt, budget breakdown, deliverables matrix — are generated as Excel or CSV files in `sheets/`.

### 6. Compile and Deliver

Final documents are compiled into `output/` as Word files. Most proposals produce two separate documents: `technical-proposal.docx` and `financial-proposal.docx`.

### 7. Resume Later

To continue an in-progress proposal, start Claude Code and ask to resume. Claude reads `proposals/INDEX.md`, shows your proposals, and picks up from where you left off.

---

## What Makes This Different

This is not a collection of prompt templates. It is a structured knowledge base synthesised from 22 consulting and strategy books, including:

- **Proposal strategy**: S1-S2-B logic, P-I-P structure, SCQA narrative spine, hypothesis-driven methodology, Cialdini's persuasion principles, pre-emptive objection neutralisation, Red Team review
- **Consulting frameworks**: 80+ structured analytical frameworks (McKinsey problem-solving process, Blue Ocean ERRC, Structured Choice, Theory of Constraints, SECI Knowledge Spiral, and dozens more)
- **Delivery excellence**: Done-Done standard, Value Realisation Method, Design Sprint, SOSTAC, Triple Constraints, frontloading principles
- **World-class patterns**: storyboarding, ghost packs, elevator test, Sweet Spot positioning, prewiring, action titles

Every section skill knows how to apply these frameworks to produce output that reads like it came from a top-tier firm.

Recent strengthening includes:

- business analysis governance, business event analysis, context-driven requirements discovery, and fit criteria
- project-control artefacts such as WBS dictionaries, task responsibility matrices, schedule hierarchy, and decision-gate calendars
- financial modelling patterns such as assumptions dashboards, cash-budget logic, scenario/sensitivity checks, and break-even testing

---

## Repository Structure

```
proposal-skills/
├── AGENTS.md                         # Repo-level routing/instructions for Codex and other agents
├── CLAUDE.md                         # Instructions for Claude Code
├── SKILL.md                          # Parent skill — routes to sub-skills
├── .gitignore                        # Excludes proposals/ (confidential)
│
├── 01-cover-letter/                  # Proposal section skills (numbered)
├── 02-executive-summary/
├── 03-understanding-of-assignment/
├── 04-firm-profile/
├── 05-relevant-experience/
├── 06-methodology/
├── 07-team-composition/
├── 08-work-plan/
├── 09-expression-of-interest/
├── 10-financial-proposal/
│
├── profiles/                         # Proposer identity system
│   ├── peter-bamuhigire.md           #   Individual consultant
│   ├── chwezi-core-systems.md        #   Company
│   └── client-template.md           #   Ghostwriting template
│
├── references/                       # Cross-cutting knowledge bases
│   ├── proposal-strategy-and-persuasion.md
│   ├── world-class-proposal-patterns.md
│   └── consulting-delivery-excellence.md
│
├── consulting-frameworks/            # Analytical building blocks
│   └── references/
│       ├── problem-structuring.md
│       ├── financial-analysis.md
│       ├── strategy-frameworks.md
│       ├── operations-frameworks.md
│       └── communication-structures.md
│
├── business-analysis-tools/          # Diagnostic instruments
│   └── references/
│       ├── strategic-analysis-frameworks.md
│       ├── elicitation-techniques.md
│       ├── requirements-analysis-models.md
│       ├── prioritisation-and-decision-tools.md
│       └── ...
│
├── sectors/                          # Procurement and sector knowledge
│   ├── world-bank/
│   ├── undp/
│   ├── afdb/
│   ├── ppda-uganda/
│   └── (industry sectors with their own SKILL.md entrypoints)
│
├── project-management/               # Supporting domain skills
├── change-management/
├── monitoring-and-evaluation/
├── stakeholder-engagement/
├── capacity-building/
├── gender-and-social-inclusion/
├── environmental-and-social-safeguards/
├── data-management/
├── sustainability-planning/
├── risk-management/
│
├── east-african-english/             # Language and tone standards
├── language-standards/
│
├── blog-writer/                      # Content creation skills
├── blog-idea-generator/
│
└── proposals/                        # LOCAL ONLY — gitignored
    ├── INDEX.md
    └── (per-proposal directories)
```

---

## Proposal Section Skills

| # | Section | What It Produces |
|---|---------|-----------------|
| 01 | Cover Letter | Client-specific opening, comparable past projects with outcomes, courteous closing |
| 02 | Executive Summary | Problem statement, four differentiators, scope table, timeline, value proposition |
| 03 | Understanding of Assignment | Background, objectives, scope analysis, ToR comments in the firm's own words |
| 04 | Firm Profile | Legal details, service areas, sector expertise, geographic footprint, certifications |
| 05 | Relevant Experience | Summary table + project cards with quantified outcomes (never just activities) |
| 06 | Methodology | Conceptual framework, phased plan (ICT or consulting), deliverables table, risk register, QA, governance |
| 07 | Team Composition | Organogram, role-responsibility table, CVs (World Bank TECH-6 or narrative format) |
| 08 | Work Plan | Gantt table, milestones, staffing schedule with realistic timelines and buffer |
| 09 | Expression of Interest | Shorter pre-qualification document — credentials, experience, available experts |
| 10 | Financial Proposal | Fee breakdown, reimbursables, payment schedule, assumptions (separate sealed document) |

---

## Supporting Domain Skills

These are cross-cutting knowledge bases that proposal sections draw from. Each can also generate a standalone section when a ToR explicitly requires it.

| Skill | Domain |
|-------|--------|
| `project-management/` | PRINCE2, PMBoK, Agile, governance, reporting, WBS-driven controls, steering committees |
| `change-management/` | ADKAR, Kotter, adoption strategies, resistance management |
| `monitoring-and-evaluation/` | Log frames, results frameworks, KPIs, theory of change |
| `stakeholder-engagement/` | Stakeholder mapping, consultation approaches, communication plans |
| `capacity-building/` | Training models, ToT, knowledge transfer, skills sustainability |
| `gender-and-social-inclusion/` | GESI frameworks, gender mainstreaming, disability and youth inclusion |
| `environmental-and-social-safeguards/` | ESIA, environmental management plans, World Bank ESF, AfDB ISS |
| `data-management/` | Data collection, MIS design, data governance, data protection law |
| `sustainability-planning/` | Exit strategies, institutional embedding, ownership transfer |
| `risk-management/` | Risk registers, mitigation frameworks, escalation triggers |

---

## Proposer Profiles

Every proposal needs a voice. Before writing, Claude loads the correct profile:

| Profile | Voice | Use When |
|---------|-------|----------|
| `profiles/peter-bamuhigire.md` | First-person singular ("I propose...") | Proposing as Peter Bamuhigire |
| `profiles/chwezi-core-systems.md` | First-person plural ("We propose...") | Proposing as Chwezi Core Systems |
| `profiles/client-template.md` | Customisable | Ghostwriting on behalf of a client |

---

## Supported Procurement Frameworks

| Framework | Coverage |
|-----------|----------|
| **PPDA** (Uganda) | Public Procurement and Disposal of Public Assets |
| **World Bank** | TECH-1 through TECH-6 and FIN-1 through FIN-4 standard forms |
| **AfDB** | African Development Bank procurement formats |
| **UNDP / UN System** | United Nations procurement and evaluation criteria |
| **Direct RFPs** | Private sector, NGO, and government ministry bids |

---

## Language Standards

- **British English** throughout: organisation, programme, centre, colour
- **East African professional tone**: formal, respectful, courteous — no marketing hype
- **Dates**: day-month-year (17 February 2026)
- **Banned AI vocabulary**: delve, tapestry, landscape (metaphor), leverage, navigate (metaphor), foster, realm, harness, synergy, embark, robust, vibrant, holistic, seamless

---

## Knowledge Base

The reference library is synthesised from 22 consulting and strategy books:

| Reference File | Sections | Content |
|----------------|----------|---------|
| `references/proposal-strategy-and-persuasion.md` | 17 | S1-S2-B logic, P-I-P structure, buyer psychology, SCQA, Cialdini, Red Team review |
| `references/world-class-proposal-patterns.md` | 18 | McKinsey/Deloitte patterns, storyboarding, ghost packs, elevator test, prewiring |
| `references/consulting-delivery-excellence.md` | 34 | McKinsey problem-solving, Design Sprint, SCAMPER, SOSTAC, SECI, Done-Done standard |
| `consulting-frameworks/references/` (5 files) | 53 | Problem structuring, financial analysis, strategy, operations, communication |
| `business-analysis-tools/references/` (8 files) | 40+ | SWOT, PESTLE, gap analysis, business analysis governance, requirements planning, fit criteria, transition evaluation, maturity models |

---

## Getting Started

### Prerequisites
- [Claude Code](https://claude.ai/code) installed and authenticated
- Git (to clone the repository)

### Setup

```bash
git clone <repository-url> proposal-skills
cd proposal-skills
claude
```

Claude reads `CLAUDE.md`, understands the full skill set, and walks you through creating your first proposal.

### Adding a New Skill

1. Create a subdirectory with a `SKILL.md` (YAML frontmatter with `name` and `description`)
2. Add a `references/` subdirectory if needed
3. Update the parent `SKILL.md` routing table
4. Update this README

---

*Built for world-class results in the East and Central African consulting market.*
