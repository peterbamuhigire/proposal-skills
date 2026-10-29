# Validation record — 29 October 2026

Baseline commands were rerun on the clean starting code before implementation;
all exited 0. The original outputs remain in external preparation logs. The
same commands ran after each selected experiment. No Windows/production/portal
operation or paid model call was performed.

| Exact command from checkout root | Baseline | Final |
|---|---|---|
| `python -X utf8 scripts/validate_skills.py --baseline quality-baseline.json` | 115 skills, zero findings | 115 skills, zero findings; package and scoped currentness gates included |
| `python -X utf8 scripts/routing_smoke_test.py` | 26/26 top-three, 19/26 first-rank recovered from log | 31/31 top-three, 23/31 first-rank, two/two owned-negative primary checks |
| `python scripts/proposal_fixture_check.py` | Synthetic package PASS | Synthetic package PASS; no authenticity/pricing/legal/submission claim |
| `python -X utf8 scripts/source_ingestion_guardrail.py` | Zero findings | Zero findings |
| `python -X utf8 scripts/encoding_link_gate.py` | Zero findings | Zero findings |
| `python -B -X utf8 -m unittest discover -v` | 52 passed | 62 passed |
| `python .codex/ensure_model_policy.py --runtime codex --check` | PASS | No policy/configuration change |
| `git diff --check` | Clean baseline | No new whitespace defects |

## Native packaging

On clean `be2c774`, Codex 0.165.0 and Claude 2.1.312 installed
`proposal@chwezi-proposal` from the local checkout in disposable offline
containers. Commands: `codex plugin marketplace add /engine --json`,
`codex plugin add proposal@chwezi-proposal --json`, `codex plugin list --json`;
Claude uses `install` and `details proposal@chwezi-proposal` after adding the
same local marketplace. Both exit 0. The mount `/engine` is disposable, not a
host binding. No model call or public-directory submission occurs.

The hard ceiling covers files and symlink entries in both full checkout
(including Git/caches) and package inventory. Directory symlinks count once;
unreadable subtrees fail closed. Exact counts are printed by the registered
validator, not estimated from skill count. Native discovery is separate from
public marketplace approval, hooks and behavioural task quality.

## Practitioner reruns

Full synthetic task outputs remain in [02-practitioner-tasks.md](02-practitioner-tasks.md).
The corrected World Bank crosswalk now matches their source-backed form
sequence. The unit fixture rejects the old TECH-7 staffing map and invented
FIN-5; it also rejects duplicate forms. The separate technical/financial outputs
remain synthetic and blocked for missing bidder identity, authority and actual
solicitation evidence. Price assumptions and weights are fixture-owned.

Root found the preparation renderer used a prohibited Arial style. The final
rerun changes all document styles to Public Sans and renders using isolated
font configuration and LibreOffice profile, with official font files already
verified in the design cycle. The original preparation render is not claimed
as compliant. Final font/page measurements are recorded below after rendering.

## Scope limits

One of 115 routes now has three positive and two owned-negative cases; the
World Bank FTP lexical prompt still ranks UNDP first. No paid behavioural
routing or actual evaluator study was performed. Scoped local links pass;
semantic cross-engine completeness is not established. The new register has
11 selected source records, zero overdue on the run date, and explicit
NOT_ASSESSED entries; it is not an exhaustive review of every citation.
Actual tender validity, bidder credentials, tax/legal compliance, portal
receipt and independent real-bid review remain NOT_ASSESSED and block release.

Final Codex discovery at clean `be2c774` exposes **115/115** canonical paths
with explicit Luna/high and `skills.max_context_tokens=10000`; the baseline
default-budget run also exposed 115/115. Alias expansion was applied before
exact path comparison. No runtime prompt text is committed.

Final render observation: `pdfinfo` reports 11 technical and five financial pages,
both tagged. `pdffonts` confirms embedded Public Sans Regular/Bold subsets; a
Nimbus Roman fallback remains for a small character range, so exact glyph-level
font fidelity is not certified. Static font instances were derived from the
verified official variable font in disposable storage because LibreOffice
initially chose the Thin face. Visual inspection of the method page confirms
readable text, but it is a sparse structural render, not a completed substantive
bid. The full exercise content is the Markdown task record; neither its page
counts nor these synthetic summaries predict a completed bidder package's size.

Final acceptance preparation adds a real miniature package regression that
rejects identity mismatch, duplicate/path-escaping entries and a symlinked
SKILL.md. The full suite now passes **63 tests**; all six registered commands
still exit 0. Final pre-review inventory is 632 checkout / 512 package entries,
both below 5,000; Git commit growth is recounted at portfolio release.
