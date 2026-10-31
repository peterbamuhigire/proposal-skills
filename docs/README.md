# Documentation index

This folder holds the engine's guidance documents, its source register and the dated records of every audit and improvement cycle. The skills themselves live under [`skills/`](../skills/SKILL.md); the [root README](../README.md) gives a short start, a task-to-skill table, the installation and validation instructions and a list of what the October 2026 kaizen improved ([quality section](../README.md#what-the-october-2026-kaizen-improved)).

## Current guidance

| Path | What it is |
|---|---|
| [`skill-authoring-standard.md`](skill-authoring-standard.md) | The contract every `SKILL.md` must meet, and the release gates. |
| [`skill-catalogue.md`](skill-catalogue.md) | All 115 skills with a one-line description and a link. The root README summarises it by category. |
| [`references.md`](references.md) | The book, repository, standards and website citations. The root README summarises them. |
| [`approval-enforcement.md`](approval-enforcement.md) and [`approval-adapter.json`](approval-adapter.json) | The proposal actions that need explicit approval (credential claims, pricing, final-file release, submission) and the preview they require. |
| [`control-plane-adoption.md`](control-plane-adoption.md) | How the portfolio coordination package may read this engine. |
| [`operations/runtime-agnostic-orchestration-2026-09-07.md`](operations/runtime-agnostic-orchestration-2026-09-07.md) | The orchestration contract for multi-phase proposal work under Claude Code and Codex. |
| [`ai-prompting/domain-prompt-compilation-contract.md`](ai-prompting/domain-prompt-compilation-contract.md) | The contract for generating a ready-to-paste prompt for a proposal task. |
| [`source-registers/2026-10-currentness.json`](source-registers/2026-10-currentness.json) | Scoped, dated source records for volatile procurement and AI claims. Its review date, 2026-11-30, is enforced by `scripts/validate_skills.py`; see [Date-triggered gates](../README.md#date-triggered-gates) in the root README. |

## Improvement evidence

| Path | What it is |
|---|---|
| [`kaizen/2026-10-engine-kaizen-pass-2/`](kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md) | The 31 October 2026 cycle: baseline, backlog, experiment log, validation record, final report, next-cycle backlog and documentation follow-ups. |
| [`kaizen/2026-10-engine-kaizen/`](kaizen/2026-10-engine-kaizen/05-final-report.md) | The 29 October 2026 cycle, with the currentness evidence and the official-form observations it relied on. |
| [`continuous-improvement/`](continuous-improvement/kaizen-adoption-2026-08.md) | Eleven Kaizen records from August and September 2026. |
| [`audits/`](audits/2026-09-06-kaizen.md) | The 6 September 2026 Kaizen audit and its independent review. |

## Historical records

These are dated records kept as written. They are not maintained, and several name the Windows checkout path of the machine that produced them; the link gate exempts them from its machine-path rule on purpose.

| Path | What it is |
|---|---|
| [`engine-upgrade-july-2026/`](engine-upgrade-july-2026/00-executive-summary.md) | The July 2026 engine upgrade: discovery, scorecard, gap analysis, roadmap and conformance record. |
| [`evaluation/2026-04-13/`](evaluation/2026-04-13/README.md) | The 13 April 2026 repository evaluation. |
| [`march-12-evaluation/`](march-12-evaluation/README.md) and [`march-16-review/`](march-16-review/executive-summary.md) | The March 2026 completeness evaluation and its follow-up review. |
| [`updates/2026-06-13-giz-eac-bds-skills.md`](updates/2026-06-13-giz-eac-bds-skills.md) | The record of the two GIZ and EAC skills added on 13 June 2026. |
| [`dual-compatibility-report.md`](dual-compatibility-report.md) | The report on making the repository usable from Claude Code and Codex alike. |
