# Contributing to Proposal Skills

Treat every active `SKILL.md` as executable instruction, not background prose. Preserve proposal-domain knowledge and keep changes small enough to review.

## Add or change a skill

1. Read [the authoring standard](docs/skill-authoring-standard.md) and copy [the skill template](templates/skill-template.md) as a starting shape; do not activate the template itself.
2. Discover neighbouring skills from `skills/**/SKILL.md`. Write positive and negative triggers that resolve the closest collision.
3. Preserve the exact acknowledgement line, British English, East African professional tone, proposer identity rules, evidence discipline, and separate-envelope requirements.
4. Put routing, permissions, decisions, degraded mode, workflow, outputs, evidence, and acceptance conditions in `SKILL.md`. Move only deep detail to a directly linked `references/` file and link that file back to its parent.
5. Add or update routing fixtures for positive, negative, collision, limited-capability, and failure-path prompts.
6. Do not add a skill to improve a metric. Add one only for an independently justified repeatable workflow or domain contract.

## Validate locally

```text
python3 -X utf8 scripts/validate_skills.py --baseline quality-baseline.json
python3 -X utf8 scripts/routing_smoke_test.py
python3 -X utf8 scripts/encoding_link_gate.py
python3 -X utf8 scripts/source_ingestion_guardrail.py
python3 scripts/proposal_fixture_check.py
python3 -X utf8 -m unittest discover -s tests
python3 -X utf8 <chwezi-dev-engine>/skills/sdlc-meta/skill-engine-audit/scripts/engine_compliance.py --root . --active-root skills --details
```

`<chwezi-dev-engine>` is the checkout of the `chwezi-dev-engine` repository on your machine. The checks need Python 3.11 or newer and PyYAML; use `python` where `python3` is not on the path. The [README validation table](README.md#validation) gives each command's purpose and expected result.

Run the canonical quick validator with each changed skill directory, not its file:

```text
python3 -X utf8 <chwezi-dev-engine>/skills/sdlc-meta/skill-writing/scripts/quick_validate.py skills/path/to/skill
```

Finish with repository-specific tests, link and syntax checks, `git diff --check`, the skill-safety audit, and the anti-slop audit. The baseline must remain empty; update its skill or fixture counts only when the catalogue or fixture set changes intentionally.

`scripts/validate_skills.py` also enforces the dated source register (`docs/source-registers/2026-10-currentness.json`). Its records carry a review date of 2026-11-30, so the check fails from 2026-12-01 until each record is re-verified against its source and given a new review date. Do not extend a review date without re-reading the source.

## Release

1. Fetch `origin` and confirm local `main` is not behind `origin/main`.
2. Run every validation gate and remove generated caches.
3. Inspect the complete diff, stage only intended files, and review the staged statistic and representative diffs.
4. Commit once with a concise engine-level message.
5. Push without force and verify `HEAD`, `origin/main`, and the pushed commit are identical.

If remote history diverges, authentication fails, branch protection rejects the push, or a required check cannot run, preserve the local commit and report the exact blocker.
