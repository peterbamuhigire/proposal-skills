---
name: proposal-writing
description: Use this skill whenever the user asks to write, draft, review, or generate any part of a consulting proposal, Expression of Interest, bid document, or tender response. Routes to the correct sub-skill based on the required section or document type.
---

# Proposal Writing - Parent Skill
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

This parent skill covers the full range of consulting proposal documents. All active proposal skills live under the repository `skills/` directory. Paths below are repository-root-relative so agents and project documentation refer to the same layout.

## Use When
- Use this skill when the user needs to draft, review, or assemble any consulting proposal, bid, or Expression of Interest.
- Load it when you need routing guidance to the correct numbered section skill or supporting skill.

## Do Not Use When
- The task is only about blog writing or skill maintenance.
- The work is unrelated to proposals, tenders, or bid responses.

## Required Inputs
- The ToR, RFP, advert, or proposal brief.
- The proposer identity and any known procurement or sector context.
- Any mandatory templates, deadlines, or submission constraints.

## Workflow
1. Identify the requested document or proposal section.
2. Load `skills/profiles/SKILL.md` before drafting proposal text so voice and identity are consistent.
3. Load the relevant numbered section skill, then add procurement, sector, and supporting domain skills only where they materially improve the output.
4. Load `skills/website-design-proposal-strategy/SKILL.md` whenever the proposal includes website design, redesign, SEO, web content, ecommerce, portal, landing page, web frontend, hosting, maintenance, or website costing.
5. Load `skills/critical-analysis-business-logic/SKILL.md` before drafting high-stakes, methodology, work plan, financial, transformation, or final-review content.
6. Draft the requested content and keep proposal-wide themes, evidence, terminology, methodology, work plan, and pricing aligned.
7. Verify compliance, logic, feasibility, section order, and separation between technical and financial content before finalizing.

## Quality Standards
- Treat each `SKILL.md` as the portable unit and load it from the `skills/` folder.
- Maintain British English, East African professional tone, and proposer-specific voice.
- Keep the proposal client-specific, evaluator-aware, and measurable where evidence exists.

## Anti-Patterns
- Do not draft proposal text before selecting the proposer profile.
- Do not generate a full proposal from memory without reading the relevant section skill.
- Do not merge technical and financial content when the procurement process separates them.

## Outputs
- The requested proposal section, routing decision, or proposal component.

## Core Routing References
- `skills/profiles/SKILL.md` for proposer selection.
- `skills/sectors/SKILL.md` for procurement and sector routing.
- `skills/references/` for persuasion, delivery, and proposal patterns.

## Sub-Skills - Proposal Sections

| # | Task | Sub-Skill to Read |
|---|---|---|
| 01 | Cover letter | `skills/01-cover-letter/SKILL.md` |
| 02 | Executive summary | `skills/02-executive-summary/SKILL.md` |
| 03 | Understanding of the assignment | `skills/03-understanding-of-assignment/SKILL.md` |
| 04 | Firm or consultant profile | `skills/04-firm-profile/SKILL.md` |
| 05 | Relevant experience and past projects | `skills/05-relevant-experience/SKILL.md` |
| 06 | Approach and methodology | `skills/06-methodology/SKILL.md` |
| 07 | Team composition and CVs | `skills/07-team-composition/SKILL.md` |
| 08 | Work plan and timeline | `skills/08-work-plan/SKILL.md` |
| 09 | Expression of Interest | `skills/09-expression-of-interest/SKILL.md` |
| 10 | Financial proposal | `skills/10-financial-proposal/SKILL.md` |

## Supporting Skills - Cross-Cutting Knowledge

Read the relevant supporting skill when the proposal requires that domain. Each can also generate a standalone section if the ToR explicitly requires it.

| Supporting Skill | When to Read |
|---|---|
| `skills/project-management/SKILL.md` | PM frameworks, governance, reporting, steering committees |
| `skills/change-management/SKILL.md` | OCM frameworks, adoption strategies, resistance management |
| `skills/monitoring-and-evaluation/SKILL.md` | Log frames, results frameworks, KPIs, theory of change |
| `skills/stakeholder-engagement/SKILL.md` | Stakeholder mapping, consultation approaches, communication plans |
| `skills/capacity-building/SKILL.md` | Training models, ToT, knowledge transfer, skills sustainability |
| `skills/gender-and-social-inclusion/SKILL.md` | GESI frameworks, gender mainstreaming, disability and youth inclusion |
| `skills/environmental-and-social-safeguards/SKILL.md` | ESIA, environmental management plans, World Bank ESF, AfDB ISS |
| `skills/data-management/SKILL.md` | Data collection, MIS design, data governance, data protection law |
| `skills/website-design-proposal-strategy/SKILL.md` | Website philosophy, UX/content/SEO methodology, stack explanation, costing, QA, launch, handover, and support |
| `skills/sustainability-planning/SKILL.md` | Exit strategies, institutional embedding, ownership transfer |
| `skills/risk-management/SKILL.md` | Risk registers, mitigation frameworks, escalation triggers |
| `skills/business-analysis-tools/SKILL.md` | SWOT, PESTLE, gap analysis, benchmarking, cost-benefit analysis, maturity models, prioritisation matrices |
| `skills/consulting-frameworks/SKILL.md` | Problem structuring, financial analysis, strategy frameworks, operations frameworks, communication structures |
| `skills/critical-analysis-business-logic/SKILL.md` | Cross-cutting serious analysis, evaluator logic, business sense, feasibility, and achievability gate |

## Reference - Proposal Strategy and Persuasion

Read `skills/references/proposal-strategy-and-persuasion.md` before writing any proposal. Apply its S1-S2-B baseline logic, P-I-P phase structure, buyer psychology, theme architecture, hypothesis-driven methodology, Pyramid of Ideas, SCQA narrative spine, objection handling, Cialdini principles, and Red Team review process.

## Reference - World-Class Proposal Patterns

Read `skills/references/world-class-proposal-patterns.md` before writing any proposal. Apply its guidance on quantified evidence, named frameworks, client-first problem framing, scannability, programme-level thinking, storyboarding, ghost packs, the elevator test, and prewiring.

## Reference - Critical Analysis and Business Logic

Read `skills/critical-analysis-business-logic/SKILL.md` before writing methodology, work plan, financial proposal, risk, M&E, sustainability, transformation, or final review content. Apply its claim-evidence-warrant discipline, essential questions, business-sense checks, mental-model pass, and achievability gate so the proposal is persuasive because it is logical and deliverable.

## Reference - Consulting Delivery Excellence

Read `skills/references/consulting-delivery-excellence.md` when writing methodology, quality assurance, or implementation sections. Use it to describe credible delivery methods such as McKinsey-style problem solving, consulting workflow, Done-Done quality, Value Realisation Method, Drucker's Five Questions, Design Thinking, SCAMPER, SOSTAC, SECI, and frontloaded work planning.

## Proposer Profiles - Who Is Proposing?

Before writing any proposal, load the correct proposer profile from `skills/profiles/SKILL.md`. The profile determines the voice, credentials, experience, and branding used throughout the document.

| Profile | When to Use |
|---|---|
| `skills/profiles/peter-bamuhigire.md` | Proposing as Peter Bamuhigire as an individual consultant |
| `skills/profiles/chwezi-core-systems.md` | Proposing as Chwezi Core Systems |
| `skills/profiles/client-template.md` | Writing on behalf of a client; copy, customise, and save |

If no proposer is specified, ask before proceeding. The profile affects every section: voice, signatory, experience, team, and references.

## Proposal Workspace

All proposals are developed in the local `proposals/` directory, which is gitignored. See `CLAUDE.md` for the full initialization workflow, directory structure, and `INDEX.md` format. Every proposal lives in its own subdirectory with section markdown files plus `terms/`, `sheets/`, `team/`, `research/`, and `output/` folders.

## Standards That Apply to All Sub-Skills

- Follow `skills/east-african-english/SKILL.md` for tone, spelling, and courteous phrasing throughout.
- Use British English spelling: organisation, programme, centre, colour.
- Let the loaded proposer profile determine voice: first-person singular for individual consultants and first-person plural for companies.
- Never use exaggerated marketing language. Confident, measured, professional writing is preferred.

## Typical Proposal Section Order

1. Cover Letter
2. Technical Proposal Submission Sheet
3. Executive Summary
4. Understanding of the Assignment
5. Firm Profile
6. Relevant Experience
7. Approach and Methodology
8. Team Composition
9. Work Plan and Timeline
10. References

Financial Proposal is always a separate sealed document when the procurement process requires separation.
