# Proposal Skills Repository

This repository is a dual-compatible skill system for consulting proposals, procurement responses, and related writing workflows. Active skills live under `skills/`; load the relevant `skills/<skill-name>/SKILL.md` file directly.

## Baseline Rules
- Treat each `SKILL.md` as the execution contract and nearby `references/` files as deeper supporting material loaded only when needed.
- Every `SKILL.md` must include this exact acknowledgement line immediately below the first top-level `# ...` heading, not in frontmatter: `Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.`
- Load `skills/profiles/SKILL.md` before drafting any proposal text so voice, signatory, and proposer identity stay consistent.
- Use `skills/sectors/SKILL.md` to decide which procurement framework and industry sector skills apply.
- Keep technical and financial proposal content separate when the procurement process requires separate envelopes or forms.

## Task Routing
- Full proposal orchestration or section drafting: start at [skills/SKILL.md](/C:/wamp64/www/proposal-skills/skills/SKILL.md)
- Proposal identity and voice: [skills/profiles/SKILL.md](/C:/wamp64/www/proposal-skills/skills/profiles/SKILL.md)
- Procurement and sector routing: [skills/sectors/SKILL.md](/C:/wamp64/www/proposal-skills/skills/sectors/SKILL.md)
- Proposal sections: use the numbered section skills under `skills/01-` through `skills/10-`
- Supporting proposal domains: use unnumbered skills such as `skills/project-management/`, `skills/monitoring-and-evaluation/`, `skills/risk-management/`, `skills/stakeholder-engagement/`, and related folders when the ToR or methodology needs that domain
- Language and tone: use [skills/east-african-english/SKILL.md](/C:/wamp64/www/proposal-skills/skills/east-african-english/SKILL.md) and [skills/language-standards/SKILL.md](/C:/wamp64/www/proposal-skills/skills/language-standards/SKILL.md) as cross-cutting review layers
- Skill maintenance: use [skills/skill-writing/SKILL.md](/C:/wamp64/www/proposal-skills/skills/skill-writing/SKILL.md), [skills/skill-safety-audit/SKILL.md](/C:/wamp64/www/proposal-skills/skills/skill-safety-audit/SKILL.md), and [skills/update-claude-documentation/SKILL.md](/C:/wamp64/www/proposal-skills/skills/update-claude-documentation/SKILL.md)
- Blog workflows: use `skills/blog-idea-generator/` and `skills/blog-writer/` only for content publishing tasks, not for proposal work

## Working Model
1. Identify the user's actual deliverable.
2. Load `skills/SKILL.md` when the deliverable spans multiple proposal sections or domains.
3. Load only the directly relevant section, domain, sector, and framework skills.
4. Read local `references/` files only when they add material value to the current task.
5. Draft or revise the output, then run a final pass for tone, consistency, and compliance.

## Quality Expectations
- Prefer concrete, evaluator-facing language over generic corporate boilerplate.
- Use British English and East African professional tone for proposal work unless the active skill says otherwise.
- Keep outputs aligned across profile, methodology, work plan, staffing, and pricing.
- When a skill exposes `Use When`, `Do Not Use When`, `Required Inputs`, `Workflow`, `Quality Standards`, `Anti-Patterns`, and `Outputs`, follow those sections as the default contract.

## Change Safety
- Keep active skills under `skills/` unless the repository architecture is explicitly changed.
- Do not duplicate logic into parallel Claude-only and Codex-only files when one `SKILL.md` can serve both.
- If you modify or add skills, keep frontmatter limited to `name` and `description`, keep the body execution-oriented, and prefer moving heavy detail into `references/`.
