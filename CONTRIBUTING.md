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

```powershell
python -X utf8 scripts\validate_skills.py --baseline quality-baseline.json
python -X utf8 scripts\routing_smoke_test.py
python -X utf8 C:\Users\Peter\.claude\skills\skills\sdlc-meta\skill-engine-audit\scripts\engine_compliance.py --root . --active-root skills --details
```

Run the canonical quick validator with each changed skill directory, not its file:

```powershell
python -X utf8 C:\Users\Peter\.claude\skills\skills\sdlc-meta\skill-writing\scripts\quick_validate.py skills\path\to\skill
```

Finish with repository-specific tests, link and syntax checks, `git diff --check`, the skill-safety audit, and the anti-slop audit. The baseline must remain empty; update its skill or fixture counts only when the catalogue or fixture set changes intentionally.

## Release

1. Fetch `origin` and confirm local `main` is not behind `origin/main`.
2. Run every validation gate and remove generated caches.
3. Inspect the complete diff, stage only intended files, and review the staged statistic and representative diffs.
4. Commit once with a concise engine-level message.
5. Push without force and verify `HEAD`, `origin/main`, and the pushed commit are identical.

If remote history diverges, authentication fails, branch protection rejects the push, or a required check cannot run, preserve the local commit and report the exact blocker.
