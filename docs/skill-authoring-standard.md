# Proposal skill authoring standard

This repository follows the July 2026 portable skill contract. The canonical engineering source remains `C:\Users\Peter\.claude\skills`; this document translates the applicable contract for proposal skills without copying that engine.

## Active catalogue

Every file named `SKILL.md` under `skills/` is active, including `skills/SKILL.md`. Files under `templates/`, `book-extractions/`, and `docs/` are not active skills. Discover the catalogue from the filesystem for every audit or release.

## Required skill contract

Each active skill must meet all of these rules:

1. Frontmatter contains only `name`, `description`, and `metadata`. `name` matches the containing directory. `description` is a single line of no more than 350 characters, starts with `Use when`, and distinguishes the closest neighbouring route. Metadata sets `portable: true` and `compatible_with: [claude-code, codex]`.
2. The exact repository acknowledgement follows the first level-one heading.
3. `Use When` and `Do Not Use When` state concrete positive and negative triggers. The negative route names the closest neighbour or the condition that blocks activation.
4. `Inputs` names the artefact, source or provider, whether it is required, and the behaviour when it is missing.
5. `Outputs` names every artefact, consumer, and observable acceptance condition. `Evidence Produced` names the evidence and its acceptance condition separately.
6. `Capability Contract` names the minimum read, search, edit, execution, network, or rendering capabilities and the permission boundary. Audits, reviews, critiques, analyses, and plans default to read-only. Mutation, publishing, spending, destructive action, and certification claims require explicit authority.
7. `Degraded Mode` returns the narrowest useful qualified result. An unavailable check is `not assessed`; it never becomes a pass.
8. `Decision Rules` is a domain-specific table whose columns identify the condition or choice, the action, and the failure or risk avoided.
9. `Workflow` is ordered, contains decision points, names a stop condition, and explains recovery. `Quality Standards` gives observable release conditions.
10. `Anti-Patterns` contains at least five concrete failures, each paired with `Fix:` and a corrective action.
11. `References` uses direct Markdown links. Reference files link back to their parent skill near the top. Broken links block release.
12. `SKILL.md` stays at or below 500 lines. Long catalogues, schemas, case studies, and worked examples move to directly linked `references/` files; routing, safety, decisions, workflow, outputs, and acceptance remain in the entrypoint.

## Proposal-engine rules

- Preserve British English, East African professional tone, proposer identity, procurement framework, and the distinction between technical and financial envelopes.
- Use `profiles` before drafting proposal text and `sectors` for procurement and sector routing.
- Apply `critical-analysis-business-logic` to high-stakes methodology, work-plan, pricing, transformation, and final-review content.
- Apply `anti-ai-slop` during writing and `ai-slop-audit` after each major iteration. Grade F blocks release.
- Treat cited facts, client evidence, CV claims, price calculations, statutory claims, and evaluation scores as evidence-bearing. Missing evidence must be disclosed, never invented.
- Route finance and accounting claims through the external `chwezi-accounting-doctrine` engine as required by `AGENTS.md`.

## Safe normalisation boundary

Mechanical repair may add known portability metadata, correct a directory-name mismatch, remove unsupported keys, repair known encoding noise, or insert empty structural scaffolding for later completion. It must not invent proposal decisions, bidder evidence, examples, thresholds, legal claims, acceptance conditions, or client facts.

When a contract gap needs judgement, read the skill and its directly linked references. Preserve useful domain content, then add the narrowest domain-specific rule that makes execution and failure handling explicit.

## Release gates

Run these commands from the repository root:

```powershell
python -X utf8 scripts\validate_skills.py --baseline quality-baseline.json
python -X utf8 scripts\routing_smoke_test.py
python -X utf8 C:\Users\Peter\.claude\skills\skills\sdlc-meta\skill-engine-audit\scripts\engine_compliance.py --root . --active-root skills --details
```

Also run the canonical `quick_validate.py` against every skill directory, repository-specific checks, `git diff --check`, the local safety audit, and the anti-slop audit. A release baseline contains no failure counts; it is not a waiver register.

## Related files

- [Skill template](../templates/skill-template.md)
- [Contribution procedure](../CONTRIBUTING.md)
- [Routing fixtures](../tests/fixtures/routing-fixtures.json)
- [Zero-debt baseline](../quality-baseline.json)
