# Proposal Skills: Kaizen Wave 2 Report

Date: 11 August 2026
Repository: `C:\wamp64\www\proposal-skills`
Wave: 2 independent implementation audit
Owner: Peter / proposal-engine maintainer

## Scope and evidence rules

This report covers only the assigned repository. No commit, push, fetch, pull,
reset, publish, procurement submission, external URL check, or sibling-repository
write was performed.

Evidence is separated into the following classes:

- Structural: catalogue, routes, encoding, links, controller surfaces, and
  repository-local compliance checks.
- Behavioural: executable fixture validation and mutation assertions.
- Render: document or visual inspection. Not run in this wave.
- System: execution against an external procurement or agent platform. Not run.
- Production: evidence from a real tender or live engagement. Not supplied.
- NOT ASSESSED: unavailable evidence is not treated as a pass.

The fixture remains labelled fictional test data. It is not a tender, client
record, credential, past-performance claim, or submission package.

## Fresh re-audit findings

Wave 1 correctly added a positive fictional bid package, a missing-mandatory
response test, and the encoding/link gate. Its three-test suite passed, but the
first audit did not mutate evidence completeness or envelope-location membership
independently (`docs/continuous-improvement/kaizen-wave-1-2026-08-11.md`, Wave 1
validation record).

The fresh audit found two validator bypasses:

1. A response with an `evidence_ids` field containing no IDs could pass, even
   though its requirement named an evidence owner.
2. A requirement and response could be changed together to point to a file
   outside the declared envelope. The existing equality checks would agree with
   one another, and the existing overlap check would not see the leak.

The audit also found that the existing encoding/link negative test combined
three defects in one temporary fixture. It proved detection, but not the
intended reason for each failure. The gate itself rejected isolated stale-route
and invalid-UTF-8 mutations, so no gate implementation change was required.

The thin `CLAUDE.md` bridge remains seven lines in the Wave 1 change set. The
new test checks the `@AGENTS.md` import and the generic README plus
`skills/SKILL.md` route without copying policy back into the bridge. Runtime
Claude import behaviour and automatic discovery by an unspecified agent remain
NOT ASSESSED.

## Wave 1 challenge and result

The independent mutation command deliberately changed one condition at a time.
It exited `1` after reporting all six expected negative controls. The exact
results were:

| Mutation | Intended failure reason | Result |
| --- | --- | --- |
| Evidence owner changed from `technical-lead` to `finance-lead` | Owner mismatch | `requirement M-TECH-01 evidence owner is not technical-lead` |
| Financial envelope received `technical/methodology.md` | Technical and financial file overlap | `technical and financial envelope files must not overlap` |
| Technical requirement and response pointed to `financial/price-schedule.md` | Location outside declared technical envelope | `requirement M-TECH-01 response location is not in the technical envelope` |
| Response for `M-FIN-01` removed | Missing mandatory response | `mandatory requirement M-FIN-01 has no response` |
| README received a stale device-specific route | Stale route | `stale device-specific sibling route: README.md` |
| A Markdown file received byte `0xff` | Invalid UTF-8 | `invalid UTF-8: bad.md` |

These are negative controls, not release failures. The unmutated fixture still
returns `PASS`, and the repository encoding/link gate still reports zero
findings (`python -X utf8 scripts\proposal_fixture_check.py` and
`python -X utf8 scripts\encoding_link_gate.py`, both exit `0`).

## Wave 2 actions

### W2-01: close evidence and envelope-membership bypasses

- Gap: The fictional validator did not require evidence for a response and did
  not verify that a requirement location belonged to its declared envelope.
  The fresh mutations above are the evidence.
- Root cause: Wave 1 checked owner equality and response-location equality but
  did not enforce evidence presence or an envelope file-membership invariant.
- Change: `scripts/proposal_fixture_check.py` now rejects an empty requirement
  set, a missing requirement evidence owner, a missing response evidence list,
  an undeclared requirement envelope, a requirement location outside its
  envelope, and a response location outside its declared envelope.
- Hypothesis: Requiring an evidence item and checking location membership will
  stop a self-consistent but leaked technical/financial package from passing.
- Owner: Peter / proposal-engine maintainer.
- Measure: The positive fixture remains `PASS`; the wrong-owner, missing-
  evidence, envelope-overlap, and envelope-location mutations fail with their
  named reasons; the 11-test suite passes.
- Risk: A stricter fixture contract may reject a future package that intentionally
  has no evidence or no file manifest. That is a useful stop condition at this
  boundary, but it is not evidence of client submission readiness.
- Rollback: Revert only the Wave 2 validation hunk if an approved fixture schema
  changes; retain the Wave 1 fixture, route gate, and negative evidence while
  updating the schema and tests together.
- Acceptance evidence: `python -X utf8 -m unittest discover -v` exits `0` with
  11 tests; the explicit mutation command exits `1` and reports the expected
  owner, evidence, overlap, location, and mandatory-item errors.
- Standardisation: Keep `evidence_owner`, `evidence_ids`, envelope names, and
  envelope file membership as executable fixture invariants. Add future
  mutations to `tests/test_proposal_behaviour.py` only for a named recurring
  failure mode.
- Re-audit: 25 August 2026.

### W2-02: make proposal mutations reason-specific

- Gap: Wave 1 had one positive fixture, one mandatory-omission case, and one
  combined encoding/link regression case. It did not isolate the priority
  mutations in the default suite.
- Root cause: The first fixture tests asserted that an error existed, rather
  than asserting the smallest expected error for each deliberate mutation.
- Change: `tests/test_proposal_behaviour.py` adds isolated tests for wrong
  evidence owner, missing evidence, envelope file overlap, envelope-location
  leakage, an empty requirement set, and the existing missing mandatory item.
- Hypothesis: Exact error assertions will expose future validator weakening or
  misclassification instead of allowing an unrelated error to satisfy a test.
- Owner: Peter / proposal-engine maintainer.
- Measure: The default suite discovers 11 tests and all pass; the explicit
  mutation run has four proposal failure classes with the intended messages.
- Risk: Exact diagnostic text can require test updates when wording changes.
  The test should change only with a documented contract change, not to hide a
  regression.
- Rollback: Revert only the added mutation methods if the fixture contract is
  replaced; do not delete the positive or mandatory-omission coverage.
- Acceptance evidence: The 11-test `unittest` run and the exit-`1` mutation
  command output are retained in this report.
- Standardisation: Treat negative controls as first-class evidence. A future
  fixture change must retain a positive case and at least one mandatory-item,
  owner, and envelope mutation.
- Re-audit: 25 August 2026.

### W2-03: isolate encoding/link, bridge, and generic-routing controls

- Gap: The Wave 1 gate test showed stale-route, invalid-byte, and broken-link
  detection in one temporary tree, but did not prove isolated stale-route and
  bad-encoding results. The bridge was structurally reviewed but not covered by
  a deterministic repository test.
- Root cause: The first regression test optimised for compact coverage and did
  not assert the finding set for each gate mutation.
- Change: `tests/test_encoding_link_gate.py` adds isolated stale-route and
  invalid-UTF-8 tests. `tests/test_proposal_behaviour.py` checks the thin
  `CLAUDE.md` bridge, root `AGENTS.md`, README, and `skills/SKILL.md` route.
- Hypothesis: Reason-specific gate tests and a small bridge assertion will keep
  the vendor adapter thin while preserving a generic manual route.
- Owner: Peter / proposal-engine maintainer.
- Measure: Isolated stale-route and invalid-UTF-8 tests pass; the encoding/link
  gate reports zero findings on the repository; bridge and generic-route test
  passes without increasing `CLAUDE.md` policy content.
- Risk: Static bridge checks cannot prove vendor runtime behaviour, and local
  URL presence cannot prove network reachability.
- Rollback: Revert only the new assertions if a vendor contract changes; keep
  canonical rules in `AGENTS.md`, `README.md`, and `skills/SKILL.md`.
- Acceptance evidence: `python -X utf8 scripts\encoding_link_gate.py` exits
  `0`; isolated stale-route and bad-encoding mutations are reported by the
  expected reason; bridge test passes.
- Standardisation: Keep model-neutral proposal behaviour in `AGENTS.md`,
  `README.md`, and `skills/SKILL.md`. Keep `CLAUDE.md` as an import bridge and
  use the README plus direct `SKILL.md` route as the generic fallback.
- Re-audit: 25 August 2026; vendor compatibility review 11 November 2026.

### W2-04: correct Wave 1 report whitespace found by the re-audit

- Gap: Three Wave 1 metadata lines had trailing spaces. They are harmless in
  rendered Markdown but would be reported by `git diff --check` once the
  untracked report is included in a patch.
- Root cause: The Wave 1 report used Markdown hard-break whitespace in metadata
  lines without a rendering need.
- Change: `docs/continuous-improvement/kaizen-wave-1-2026-08-11.md` removes
  only those trailing spaces.
- Hypothesis: The retained Wave 1 evidence will remain semantically unchanged
  and pass whitespace review when the report is later staged.
- Owner: Peter / proposal-engine maintainer.
- Measure: `git diff --check` exits `0`; an explicit whitespace scan of the
  untracked text files reports no trailing whitespace.
- Risk: None beyond a formatting-only line-ending or rendering difference;
  no content or evidence claim was changed.
- Rollback: Restore the three spaces only if a documented Markdown renderer
  requires them; this would reintroduce the diff-check finding.
- Acceptance evidence: `git diff --check` exit `0` and the post-patch text scan.
- Standardisation: Do not use trailing spaces for metadata line breaks in
  Kaizen reports; use paragraph or list structure instead.
- Re-audit: 25 August 2026.

## Exact Wave 2 files

Only these files were newly changed or added in this second wave. The first
three are implementation or test surfaces; the fourth is the Wave 1 whitespace
correction; the last is this report.

- `scripts/proposal_fixture_check.py`
- `tests/test_proposal_behaviour.py`
- `tests/test_encoding_link_gate.py`
- `docs/continuous-improvement/kaizen-wave-1-2026-08-11.md`
- `docs/continuous-improvement/kaizen-wave-2-2026-08-11.md`

The Wave 1 fixture, encoding/link implementation, controller files, and
README routes were preserved. No sibling repository or workspace-level report
was modified.

## Before, Wave 1, and Wave 2 measures

| Measure | Before Wave 1 | Wave 1 | Wave 2 | Evidence |
| --- | ---: | ---: | ---: | --- |
| Default behavioural tests discovered | `0` | `3` passing | `11` passing | Baseline and Wave 1 report; `python -X utf8 -m unittest discover -v` exit `0` |
| Positive fictional package | Not present | `PASS` | `PASS` | `scripts/proposal_fixture_check.py` exit `0` |
| Mandatory-item negative control | Not present | One test | One exact-message test | `test_missing_mandatory_requirement_blocks` and mutation command exit `1` |
| Evidence-owner negative control | Not assessed | Validator branch existed | Exact-message test and mutation | `test_wrong_evidence_owner_blocks_for_owner_reason` |
| Empty evidence-list bypass | Not assessed | Accepted by validator | Rejected | `test_missing_evidence_cannot_bypass_owner_control` |
| Envelope-location membership | Not assessed | Not enforced | Rejected | `test_envelope_file_leakage_blocks_for_location_reason` |
| Encoding/link gate findings on repository | Not assessed | `0` | `0` | `scripts/encoding_link_gate.py` exit `0` |
| Explicit stale-route mutation | Not assessed | Combined regression case | Isolated expected finding | `test_stale_route_is_the_only_reported_mutation` |
| Explicit invalid-UTF-8 mutation | Not assessed | Combined regression case | Isolated expected finding | `test_bad_encoding_is_the_only_reported_mutation` |
| Published exercise score | `55` cap applied to raw `60.8` | `55` cap applied to raw `73.0` | NOT ASSESSED; no new scoring instrument | `C:\wamp64\www\KAIZEN-INITIAL-ASSESSMENT.md`, `C:\wamp64\www\KAIZEN-WAVE-1-REPORT.md`; no score inferred |

Wave 2 does not claim a new raw score. The bounded improvement is accepted on
the named fixture and gate evidence, not on a score increase.

## Validation and command evidence

| Command | Exit | Result |
| --- | ---: | --- |
| `python -X utf8 scripts\validate_skills.py --baseline quality-baseline.json --details` | `0` | `108` active skills; `0` findings |
| `python -X utf8 scripts\routing_smoke_test.py` | `0` | `18` fixtures; `100.0%` top-three precision |
| `python -X utf8 scripts\encoding_link_gate.py` | `0` | `0` findings; encoding, local links, and portable sibling routes pass |
| `python -X utf8 scripts\source_ingestion_guardrail.py` | `0` | `0` findings |
| `python -X utf8 C:\wamp64\www\skills-web-dev\skills\sdlc-meta\skill-engine-audit\scripts\engine_compliance.py --root . --active-root skills --details` | `0` | `108` skills; `108` fully compliant; `0` safe fixes |
| `python -X utf8 -m unittest discover -v` | `0` | `11` tests passed |
| `python -X utf8 -m py_compile scripts\encoding_link_gate.py scripts\proposal_fixture_check.py tests\test_encoding_link_gate.py tests\test_proposal_behaviour.py` | `0` | Python syntax/bytecode compilation passed |
| `git diff --check` | `0` | No tracked-change whitespace findings; Wave 1 report metadata was also checked as untracked text |
| Explicit six-mutation command | `1` expected | All six deliberate defects were reported; non-zero exit is preserved as negative evidence |

The explicit negative command used temporary directories and in-memory copies
of the fictional package. It did not change repository files. No real
procurement portal, external URL, agent runtime, or client artefact was used.

## Safety and anti-slop review

Safety status: Safe for the bounded change.

The changed validator, tests, fictional JSON, and Wave 1/Wave 2 reports were
read in full. Static review found no installer, remote script, credential
request, secret collection, upload, exfiltration, hidden system action, or
unapproved dependency. The source-ingestion guardrail returned `0` findings.
The only generic pattern hit during the first scan was routing-tokenisation
code in `scripts/routing_smoke_test.py`; it was not a secret or a new Wave 2
surface.

Anti-slop status: Manual gate passed for the changed implementation and report.
The report uses repository paths, exact command exits, named failure messages,
fictional-data boundaries, and explicit unassessed states. No unverified client
claim, procurement statistic, organisation, credential, direct external quote,
or submission outcome was added. The banned-vocabulary scan returned no matches
on the changed controller, script, test, fixture, and report surfaces.

An automated `ai-slop-audit` runner is not available in this repository; that
automated check remains NOT ASSESSED. The repository's `skills/meta/anti-ai-slop`
contract remains the applicable manual production guardrail.

## Portability and routing status

| Entry path | Status | Evidence and limitation |
| --- | --- | --- |
| Claude | Structural PASS | `CLAUDE.md` remains a thin bridge containing `@AGENTS.md`; the bridge test passes. Runtime Claude import behaviour is NOT ASSESSED. |
| Codex-style | Structural PASS | Root `AGENTS.md`, canonical `skills/SKILL.md`, `108`-skill validation, and routing fixtures pass. Runtime model discovery is not independently observed. |
| Generic/manual agent | Structural PASS | README, root `AGENTS.md`, and direct `skills/SKILL.md` route are present and tested. Universal automatic discovery is NOT ASSESSED. |

No vendor-specific proposal logic was re-expanded into `CLAUDE.md`.

## Residual P0, P1, P2, and NOT ASSESSED states

### P0

- No new P0 defect was found in the assigned Wave 2 scope.
- The repository still must not be treated as submission-ready from these
  fixture results. A real solicitation, authority record, evidence pack, and
  release review remain required before any submission decision.

### P1

- The fictional fixture does not test evaluator scoring, arithmetic
  reconciliation, staffing/schedule consistency, document fidelity, or live
  submission behaviour.
- Native DOCX/PDF/PPTX generation, reopen, render, accessibility, pagination,
  and visual inspection are NOT ASSESSED.
- External URL reachability for the canonical sibling routes is NOT ASSESSED;
  the gate checks route form and presence only.

### P2

- Claude runtime compatibility and generic-agent automatic instruction
  discovery need a dated vendor/runtime check. Structural bridge evidence does
  not replace that check.
- Additional fixture mutations should be added only when a recurring proposal
  failure justifies them, such as unsupported credentials or staffing/schedule
  mismatch. No client data should be added for this purpose.
- The mutable standards and vendor-instruction review remains scheduled for
  11 November 2026 in the portfolio source register and Wave 1 report.

### NOT ASSESSED register

- Live Claude loading of `@AGENTS.md`.
- Universal automatic instruction discovery by unspecified agents.
- External URL reachability and procurement portal behaviour.
- Native document generation, render, accessibility, and pagination.
- Real client tender evaluation, submission, win/loss, or production outcome.
- Longitudinal evidence that the fixture prevents defects in real proposals.
- A new diagnostic raw score for this wave.
- Automated `ai-slop-audit` execution.

## Final scope review

`git status --short --branch` shows only the assigned repository's Wave 1 and
Wave 2 files. `git diff --check` exits `0`; the Wave 1 report's three metadata
lines were corrected because the whitespace finding was independently observed.
Generated Python caches were removed after verification. No commit or remote
operation was performed.

The next useful check is the scheduled 25 August 2026 re-audit of the fixture
against a fresh context, followed by the 11 November 2026 portability and
standards review. These dates are review controls, not evidence that the future
checks have passed.
