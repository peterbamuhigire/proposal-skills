# Dual Compatibility Report

## What Was Wrong
- The repository already worked well as a Claude-oriented knowledge base, but most `SKILL.md` files exposed their guidance through inconsistent headings. That made cross-tool routing weaker because Codex benefits from a predictable skill contract.
- The repo had strong procurement framework skills, but the nine industry sector directories under `sectors/` only contained reference files. That meant sector context existed, but it was not exposed as first-class portable skills.
- The repo had `CLAUDE.md` but no repo-level `AGENTS.md`, so Codex had no native top-level routing file explaining how to navigate the system without relying on Claude-specific assumptions.
- `skill-writing/SKILL.md` carried an extra frontmatter field beyond `name` and `description`, which was inconsistent with the desired portable frontmatter standard.

## What Was Improved
- Added a repo-level [AGENTS.md](/abs/path/C:/wamp64/www/proposal-skills/AGENTS.md) that explains the repository purpose, baseline rules, task routing, working model, quality expectations, and change-safety rules for Codex.
- Added [sectors/AGENTS.md](/abs/path/C:/wamp64/www/proposal-skills/sectors/AGENTS.md) so sector and procurement routing is explicit inside the most context-heavy subdomain.
- Standardized every existing `SKILL.md` with the same portable contract:
  `Use When`, `Do Not Use When`, `Required Inputs`, `Workflow`, `Quality Standards`, `Anti-Patterns`, `Outputs`, and `References`.
- Preserved the original Claude-tuned body content under those new sections instead of replacing it, which minimizes regression risk.
- Removed the extra `license` field from `skill-writing/SKILL.md` frontmatter so the repo now consistently centers `name` and `description` as the triggering metadata.

## What Was Added
- New sector skill entrypoints:
  `sectors/agriculture/SKILL.md`
  `sectors/education/SKILL.md`
  `sectors/energy/SKILL.md`
  `sectors/financial-services/SKILL.md`
  `sectors/governance/SKILL.md`
  `sectors/health/SKILL.md`
  `sectors/ict/SKILL.md`
  `sectors/transport-infrastructure/SKILL.md`
  `sectors/water-sanitation/SKILL.md`
- Those additions expose existing reference material as real skill units without moving any directories or duplicating domain logic.

## Why The Changes Matter
- Claude Code keeps its current repo shape, section numbering, reference layout, and orchestration model.
- Codex now has a clear repo-level instruction file and consistent skill contracts, which makes routing and execution far more predictable.
- Sector knowledge is now loadable as skills instead of living only as passive references, which closes an important portability gap without restructuring the repository.
- The repository remains one system rather than splitting into Claude-only and Codex-only versions.

## Recommendations
- Optional: compress the heaviest skill bodies further by moving some long explanatory passages into local `references/` files, especially where the main `SKILL.md` is acting as both workflow and handbook.
- Optional: add a lightweight validation script that checks every `SKILL.md` for the standard headings and two-field frontmatter.
- Optional: add one worked end-to-end proposal example under `docs/` to calibrate output quality across both Claude Code and Codex.
