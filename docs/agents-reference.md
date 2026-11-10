# Reference sections moved out of AGENTS.md

Moved verbatim on 2026-11-10 to keep the always-loaded file small (token economy; Codex reads at most 32 KiB of AGENTS.md). Open the section you need.

## Document and Spreadsheet Tooling

- Before promising `.docx`, `.pdf`, `.xlsx`, application registers, scoring matrices, price schedules, budgets, dashboards, CV packs, or annexes, check whether document and spreadsheet tooling is available on the machine.
- Prefer available Codex/Claude document and spreadsheet plugins. If unavailable, use local Python libraries such as `openpyxl`, `XlsxWriter`, `pandas`, `python-docx`, `docxtpl`, `docxcompose`, `pypandoc`, `markdown`, `PyMuPDF`, `pypdf`, `pdfplumber`, and `reportlab`.
- Check binaries such as `pandoc`, LibreOffice/`soffice`, `wkhtmltopdf`, and `tesseract` where the output route needs them.
- Run a minimal DOCX/XLSX smoke test on a new machine before production export.
- Never claim a generated Word, PDF, or Excel file exists unless it was actually written and opened or validated.

## July 2026 authoring and release gate

- The active catalogue is every `SKILL.md` under `skills/`, including `skills/SKILL.md`; discover it from the filesystem and keep the documented count aligned with machine output.
- Follow [the local authoring standard](docs/skill-authoring-standard.md) and start new work from [the skill template](templates/skill-template.md).
- Every active skill requires neighbour-aware positive and negative triggers, input/output/evidence contracts, capability and permission boundaries, degraded mode, a decision table, stop and recovery workflow, observable quality standards, five corrected anti-patterns, and direct references.
- Analysis, review, critique, planning, and audit procedures default to read-only. Mutation, publishing, submission, spending, destructive action, and certification claims require explicit authority.
- Run `python3 -X utf8 scripts/validate_skills.py --baseline quality-baseline.json` and `python3 -X utf8 scripts/routing_smoke_test.py` before release. The baseline must stay at zero findings; it is not a waiver.
- Run `python3 -X utf8 scripts/encoding_link_gate.py` before release to reject invalid UTF-8, verified mojibake markers, broken local Markdown links, machine-specific paths outside dated records, and stale device-specific sibling-engine routes.
- Run the canonical scanner and canonical quick validator for each changed skill directory, then the skill-safety and anti-slop gates. Grade F blocks release.
- Run `python3 -X utf8 scripts/source_ingestion_guardrail.py`; any finding blocks release. Do not bypass the gate by renaming, compressing, splitting, or moving source material.
- Use `python` where `python3` is not on the path (for example on Windows). The [README validation table](README.md#validation) lists every check, what it needs and its expected result.

## Human-English editorial standard (2026-08 Kaizen)

Every proposal, bid, EOI, cover letter, executive summary, methodology, case study, and evaluator-facing message must load the [human-English editorial standard](skills/language/language-standards/references/human-english-editorial-standard.md) and the [proposal phrase bank](skills/writing-content/premium-commercial-writing/references/proposal-phrase-bank.md) alongside the profile, ToR, section skill, critical-analysis, and anti-slop gates. Apply its five passes and preserve evaluator-specific register, proof, compliance language, and honest delivery constraints.

The required result is readable British English with concrete verbs, accurate grammar and collocation, purposeful rhythm, visible judgement, and no copy-pasted prestige language. Do not simulate a human voice with errors, forced warmth, unsupported claims, or invented credentials. Record the buyer/purpose, claim-proof map, terms checked, revision/proof status, gaps, reviewer, and date.

## PORTFOLIO CRAFT CONTRACT

Load `chwezi-engine-agents/docs/operations/portfolio-craft-standard-2026-09-04.md` through the catalogue when available. Craft a proposal section by section: frame the decision-maker and win thesis, select one argument or compliance response, inspect the brief and evidence, draft the smallest persuasive unit, test it against the evaluation logic and counter-case, refine the language and layout, and record source, review, and acceptance evidence. Keep delivery proof, assumptions, risks, commercial logic, and next action visible. Do not produce a generic full proposal as an opaque batch. Apply `Observe -> Baseline -> Select -> Experiment -> Check -> Standardise -> Teach -> Re-measure` to kaizen itself. Missing source, compliance, financial, design, render, reviewer, or authority evidence is `NOT ASSESSED`, never a pass.

October Kaizen evidence is in `docs/kaizen/2026-10-engine-kaizen/`; pass 2 (31 October 2026) is in
`docs/kaizen/2026-10-engine-kaizen-pass-2/`. The skill validator also scans every skill for retired World Bank
form labels (`scripts/check_form_labels.py`), the link gate rejects machine-specific paths, and
`scripts/proposal_fixture_check.py --check-content` scans a package's envelope files for cross-envelope leaks.
Check `docs/source-registers/2026-10-currentness.json` before reusing volatile
procurement or AI claims; scoped support never substitutes for the issued RFP.
Every record there has a review date of 2026-11-30, and `scripts/validate_skills.py`
fails from 2026-12-01 until each record is re-verified against its source.
The skill validator also enforces marketplace parity, source review dates and
the hard 5,000-entry limit for both package and complete checkout.

