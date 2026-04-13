# Proposal Skills Repository

This repository is a dual-compatible skill system for consulting proposals, procurement responses, and related writing workflows. The portable unit is each `SKILL.md` file in place. Do not assume a special `skills/` folder is required. Read the relevant skill file directly from its current directory.

## Baseline Rules
- Preserve existing Claude Code behavior. Layer improvements on top of the current structure instead of restructuring directories.
- Treat `SKILL.md` as the execution contract and `references/` as deeper supporting material loaded only when needed.
- Load `profiles/SKILL.md` before drafting any proposal text so voice, signatory, and proposer identity stay consistent.
- Use `sectors/SKILL.md` to decide which procurement framework and industry sector skills apply.
- Keep technical and financial proposal content separate when the procurement process requires separate envelopes or forms.

## Task Routing
- Full proposal orchestration or section drafting: start at [SKILL.md](/abs/path/C:/wamp64/www/proposal-skills/SKILL.md)
- Proposal identity and voice: [profiles/SKILL.md](/abs/path/C:/wamp64/www/proposal-skills/profiles/SKILL.md)
- Procurement and sector routing: [sectors/SKILL.md](/abs/path/C:/wamp64/www/proposal-skills/sectors/SKILL.md)
- Proposal sections: use the numbered section skills `01-` through `10-`
- Supporting proposal domains: use unnumbered skills such as `project-management/`, `monitoring-and-evaluation/`, `risk-management/`, `stakeholder-engagement/`, and related folders when the ToR or methodology needs that domain
- Language and tone: use [east-african-english/SKILL.md](/abs/path/C:/wamp64/www/proposal-skills/east-african-english/SKILL.md) and [language-standards/SKILL.md](/abs/path/C:/wamp64/www/proposal-skills/language-standards/SKILL.md) as cross-cutting review layers
- Skill maintenance: use [skill-writing/SKILL.md](/abs/path/C:/wamp64/www/proposal-skills/skill-writing/SKILL.md), [skill-safety-audit/SKILL.md](/abs/path/C:/wamp64/www/proposal-skills/skill-safety-audit/SKILL.md), and [update-claude-documentation/SKILL.md](/abs/path/C:/wamp64/www/proposal-skills/update-claude-documentation/SKILL.md)
- Blog workflows: use `blog-idea-generator/` and `blog-writer/` only for content publishing tasks, not for proposal work

## Working Model
1. Identify the user’s actual deliverable.
2. Load the nearest routing skill if the deliverable spans multiple domains.
3. Load only the directly relevant section, domain, sector, and framework skills.
4. Read local `references/` files only when they add material value to the current task.
5. Draft or revise the output, then run a final pass for tone, consistency, and compliance.

## Quality Expectations
- Prefer concrete, evaluator-facing language over generic corporate boilerplate.
- Use British English and East African professional tone for proposal work unless the active skill says otherwise.
- Keep outputs aligned across profile, methodology, work plan, staffing, and pricing.
- When a skill now exposes `Use When`, `Do Not Use When`, `Required Inputs`, `Workflow`, `Quality Standards`, `Anti-Patterns`, and `Outputs`, follow those sections as the default contract.

## Change Safety
- Do not move or rename skill directories unless there is an explicit need.
- Do not duplicate logic into parallel Claude-only and Codex-only files when one `SKILL.md` can serve both.
- If you modify or add skills, keep frontmatter limited to `name` and `description`, keep the body execution-oriented, and prefer moving heavy detail into `references/`.
