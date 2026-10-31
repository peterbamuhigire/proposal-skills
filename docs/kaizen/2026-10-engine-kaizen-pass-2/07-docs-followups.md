# Documentation wave: follow-ups (31 October 2026)

This wave changed documents only: `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `docs/skill-authoring-standard.md` and the new
[`docs/README.md`](../../README.md). It did not edit a `SKILL.md`, a script, a test or a dated record. This file lists what it
found and left alone, what it could not verify, and what the numbers in the documents were measured with.

## Left as written on purpose

- **Historical machine-path lines.** 18 lines in 10 dated records still name a Windows checkout path (`docs/audits/` 1,
  `docs/continuous-improvement/` 12 in 5 files, `docs/engine-upgrade-july-2026/` 3, `docs/dual-compatibility-report.md` 2). The count comes
  from the link gate's own pattern applied to its exempt prefixes. The pass 2 notes say "about twenty". Dated records are history, so
  they were not rewritten; the gate exempts them and `docs/README.md` says so. Whether to sanitise them stays the open decision 1 in
  [`06-next-cycle.md`](06-next-cycle.md).
- **Portfolio-managed router sentences.** The shared renderer was run from the frozen snapshot of `chwezi-engine-agents` against this
  checkout: `--dry-run` printed `{"changed": [], "dry_run": true}`, and two real runs each printed `{"changed": []}`. Nothing was
  rendered and no commit was made. The currentness sentence in `AGENTS.md` (lines 46 and 47) still reads "the catalogue binding
  `digital-research-engine`", an older path-free form; the template now says "catalogue id `digital-research-skills`". The renderer
  rewrites only sentences that name a host path, so it leaves this one alone, and it was not hand-edited.
- **`tests/agent-integration/test_proposal_agent_contract.py`.** Line 24 in this checkout (the portfolio notes cite line 28) builds the
  catalogue path as `ROOT.parent / "chwezi-engine-agents" / "catalog" / "engines.yaml"`, so it finds the coordination package only when it
  sits next to this checkout, and it ignores `CHWEZI_ENGINES_ROOT`. When the folder is absent it prints `NOT ASSESSED` and passes. The
  script is outside `unittest` discovery and CI. The README states both facts under Validation. No test was edited; the fix remains
  the P2 item in `06-next-cycle.md`.

## Mismatches with other repositories (recorded, not edited)

1. **Website Skills and this engine.** The user-level routing note says `website-skills` intentionally embeds `proposal-skills`. The
   website repository says otherwise: `AGENTS.md` (External Skill Set) calls it a "separate proposal-generation engine resolved from the
   global routing table", `docs/licensing-matrix.md` row "Proposal templates" says the same, there is no `.gitmodules`, and its git history
   holds `37780ba` "Remove cross-engine submodule; routing handles engine awareness". The website README does not mention the
   relationship. This README follows the website's own wording ("keeps no copy of this engine"). Decision for Peter: correct the
   user-level note, or restore the embedding and then update both repositories.
2. **GitHub name of the research engine.** `gh api repos/peterbamuhigire/digital-research-skills` returns `full_name` and `html_url` for
   `chwezi-research-engine`, while the portfolio catalogue entry (`repository: digital-research-skills`, alias `chwezi-research-engine`)
   and the research README's clone URLs use `digital-research-skills`. The other three renamed repositories resolve to the new names
   (`chwezi-dev-engine`, `chwezi-design-engine`, `chwezi-sdlc-documentation`). This README therefore names the research engine by catalogue
   id and gives no URL for it.
3. **Engine manifest against catalogue.** `.skills-engine/engine-manifest.yaml` declares one check (`git diff --check`); the catalogue
   entry for this engine lists seven commands. The README describes both. Aligning the manifest is a manifest change, not a documentation
   change.
4. **Local remotes.** The `origin` URLs of the local `skills-web-dev`, `srs-skills`, `design-system-skills` and `chwezi-research-engine`
   checkouts still use the old names (GitHub redirects them). Not touched.

## Small fixes outside the documentation scope

- `install.sh` is stored with mode 100644, so `./install.sh` fails with `Permission denied` on a fresh clone. The README now says
  `bash install.sh`. Setting the executable bit (`git update-index --chmod=+x install.sh`) is a repository change for the owner.
- `scripts/validate_p0_commercial_fixture.py` without an argument prints `FAIL: list index out of range` and exits 1; its sibling
  `validate_healthcare_evidence_packs.py` prints a usage line. A usage message would help. Both pass when given their fixture.
- `scripts/check_source_currency.py` and `scripts/validate_skills.py` have no `--as-of` option. The 2026-11-30 gate was checked by
  replacing `date.today` in the gate's module for one process (0 errors on 2026-11-29 and 2026-11-30, 14 on 2026-12-01 and 2027-01-01).
  An `--as-of` option would make that check repeatable by anyone.
- `.github/workflows/source-ingestion-guardrail.yml` still passes `submodules: recursive`; the repository has no `.gitmodules`.
  Harmless, and left as it is.
- Skill text outside this wave still names the catalogue path `digital-research-engine` in 4 files (5 lines):
  `retail-transformation-proposal/SKILL.md`, `kaizen-improvement-system/SKILL.md` (2 lines),
  `language-standards/references/english-collocations-and-lexical-precision-2026-09-02.md` and
  `premium-client-proposal-strategy/references/marketing-and-digital-services-proposals.md`. They resolve through the catalogue, so they are not
  wrong, but they would need a pass if the portfolio retires that path.

## Statements in the pass 2 records that no longer match the repository (records not rewritten)

- `05-final-report.md` says the work is on `kaizen/2026-10-pass2` and not merged. `git branch --contains 6efc922` now lists `main`, so the
  pass 2 commits are on `main`.
- `06-next-cycle.md` cites line 28 of the agent-integration script and "about twenty" machine-path lines; the measured values are line 24 and
  18 lines in 10 files.
- `06-next-cycle.md` says the source register fails "after" 30 November. The gate tests `today > review_date`, so 30 November is the last passing
  day and 1 December is the first failing day.

## Decisions taken in this wave

- **No `CHANGELOG.md`.** The engine keeps none and none is clearly expected: its history is `git log` and the dated Kaizen records. The
  commit list for pass 2 is in `05-final-report.md`. Creating one is a choice for the owner.
- **A documentation index was added** (`docs/README.md`) because `docs/` held 16 entries and no index.
- **Former directory names** are mentioned once, in the README's sister-engine paragraph.

## Measured numbers used in the documents

| Number | Command | Value on 2026-10-31 |
|---|---|---|
| Active skills | `find skills -name SKILL.md \| wc -l` | 115 |
| Skills per category | `find skills -name SKILL.md` grouped by second path segment | 10, 18, 16, 12, 14, 11, 11, 8, 3, 2, 9, plus the router (1); the README table matched all 115 skill links with none missing or extra |
| Tests | `python3 -X utf8 -m unittest discover -s tests`; real `pytest -p no:cacheprovider -q tests` on a copy | 117 under both; pytest also reports 43 subtests passed |
| Routing fixtures | `scripts/routing_smoke_test.py` | 41; hit rate 100%; precision@1 32/41; owned negatives 7/7; the fixtures name 27 skills |
| Source records | `docs/source-registers/2026-10-currentness.json` | 14: 10 `SCOPED`, 4 `NOT_ASSESSED`, all volatile, all reviewed by 2026-11-30 |
| File ceiling | `scripts/validate_skills.py` | 838 checkout files, 528 package files, limit 5,000 |
| Hook tests | `node hooks/test-destructive-bash-gate.js`, `node hooks/test-plugin-hook-config.js` | 61 of 61, 7 of 7 |
| Installer | `bash install.sh --scope project` into a throwaway directory, then `doctor` and `uninstall` | 353 files installed, 115 of them `SKILL.md`; `doctor` 0 missing, 0 modified; uninstall removed 353 |

## Validators before and after the edits

All run from the repository root with `PYTHONDONTWRITEBYTECODE=1`. "Before" is `main` at `a7f15b7`; "after" is the final tree of this wave.

| Command | Before | After |
|---|---|---|
| `python3 -X utf8 scripts/validate_skills.py --baseline quality-baseline.json` | 0 (115 skills, 0 findings) | 0 (115 skills, 0 findings) |
| `python3 -X utf8 scripts/routing_smoke_test.py` | 0 (41 fixtures, 100%, 32/41, 7/7) | 0 (same figures) |
| `python3 -X utf8 scripts/encoding_link_gate.py` | 0 (0 findings) | 0 (0 findings) |
| `python3 -X utf8 scripts/source_ingestion_guardrail.py` | 0 (0 findings) | 0 (0 findings) |
| `python3 scripts/proposal_fixture_check.py` | 0 (PASS) | 0 (PASS) |
| `python3 -X utf8 -m unittest discover -s tests` | 0 (117 tests, OK) | 0 (117 tests, OK) |
| `git diff --check` | 0 | 0 |

Mid-wave the link gate reported two broken links, correctly, while the README linked to `docs/README.md` and this file before they existed;
that was fixed by creating them, not by touching the gate. Before the edits these also exited 0: `scripts/check_source_currency.py`,
`scripts/check_form_labels.py`, `scripts/check_marketplace.py`, the two fixture validators, the page-budget example, the
`--check-content` run on the sanitised example, `engine_compliance.py` (115 of 115 compliant), `quick_validate.py` on
`skills/pipeline/06-methodology`, both hook tests and the agent-integration script.

## Not verified in this wave

- `install.ps1` and the Windows route: no `pwsh` on this workstation.
- The GitHub Actions workflows: not run here (they cannot run locally).
- `/plugin marketplace add` and the Codex and Claude marketplace commands: need network and a host install; the 29 October container
  record is the only evidence and is cited as such.
- `python3 .codex/ensure_model_policy.py --runtime codex --apply`: only `--check` and `--runtime claude` were run.
- Whether the PPDA and other source facts in the skills are current: this wave read no source; the register is unchanged.
