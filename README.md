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
5. Sections are written into the per-proposal markdown files. Tables are generated into `sheets/`, and final `.docx` outputs are compiled into `output/`.

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
- Consulting delivery patterns such as McKinsey-style problem solving, Done-Done quality, Value Realisation Method, Design Thinking, SECI, and SOSTAC.
- Business analysis governance, context-driven requirements discovery, fit criteria, and transition planning.
- Project control artefacts such as WBS dictionaries, responsibility matrices, decision gates, staffing schedules, and work plan hierarchies.
- Manufacturing, industrial production, inventory, capacity, material handling, MRP, scheduling, and green production diagnostics for bids involving operations-heavy businesses.

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
| `skills/sustainability-planning/SKILL.md` | Exit strategies, institutional embedding, ownership transfer |
| `skills/risk-management/SKILL.md` | Risk registers, mitigation frameworks, escalation triggers |
| `skills/business-analysis-tools/SKILL.md` | SWOT, PESTLE, gap analysis, benchmarking, requirements analysis, maturity models |
| `skills/consulting-frameworks/SKILL.md` | Problem structuring, financial analysis, strategy, operations, and communication frameworks |

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
