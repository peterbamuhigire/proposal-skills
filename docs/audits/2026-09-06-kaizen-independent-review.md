# Independent fixture-checker review — 6 September 2026

Disposition: both independently reproduced residual defects are now CLOSED by
the authorised narrow repair and targeted regressions. All 19 native tests pass;
the unchanged fictional fixture passes. The original review evidence below is
historical; the repair disposition records the subsequent changes and checks.

## Review scope and evidence

Reviewed [checker](../../scripts/proposal_fixture_check.py),
[tests](../../tests/test_proposal_behaviour.py), their working-tree diff and the
[fictional fixture](../../tests/fixtures/fictional-bid-package.json), under root
AGENTS, the skills router, local Kaizen/adoption, authoring and safety-review rules.
Baseline HEAD: `dd41ac5fda13dbcfedd3798803d668ec2eeb0697`; the reviewed patch is uncommitted.
SHA-256 at inspection:

- Checker: `91C4486ABCEA4F6A715951F30802AF6B78D805437E241352F8467093E763339B`.
- Tests: `AC5356AEC7FA7F14DB7D7D964B664A44B6373DFC9FEE080C85A3ACC74699194B`.

| Check, from repository root | Result | Exit |
|---|---|---:|
| `python -B -X utf8 -m unittest discover -v` | 17 tests passed, including 13 proposal-behaviour tests | 0 |
| `python -B -X utf8 scripts/proposal_fixture_check.py` | Unmodified fictional fixture PASS | 0 |
| `python -B -X utf8 scripts/source_ingestion_guardrail.py` | 0 findings; heuristic ingestion check only | 0 |
| In-memory mutation probe via `python -B -X utf8 -` | 17 cases: 12 rejected, five accepted, no exceptions | 0 (harness completed; not a gate pass) |

The 12 rejected probes covered three duplicate collections, three non-boolean
mandatory values (`None`, `"true"`, `1`), four non-object collection rows,
unavailable evidence and whitespace-only approval owner. The native suite also
covers missing mandatory flags. No fixture, script or test file was edited by
the probes; bytecode writing was disabled.

## Original residual findings (both now closed)

### P2 — Evidence ownership accepts matching non-identities

Checker lines 99 and 122–128 test owner truthiness and equality, but do not require
nonblank strings for `requirements[].evidence_owner` and `evidence[].owner`.
Setting both first-row owners to `" "`, `True`, `["not-a-name"]`, or
`{"role": "not-a-name"}` returned `[]` in each case. An available evidence row can
therefore appear accountable without a valid owner identifier. The new approval
owner check is stricter and correctly rejects a whitespace owner.

Acceptance: validate both ownership fields as nonblank strings before comparison;
add isolated negative cases for each malformed value and retain the existing
wrong-owner and positive-fixture checks. Owner: main checker/test maintainer.

### P2 — Lexical path comparison misses an envelope collision

Checker lines 79–83 compare raw filename strings. Replacing the technical file,
its requirement location and its response location with
`technical/../financial/price-schedule.md` returned `[]`, while the financial
envelope still contains `financial/price-schedule.md`. Lexical normalisation of
the first path yields the second. This bypasses the intended file-separation
invariant; no real bid file was opened or leaked in the probe.

Acceptance: define canonical relative fixture paths and reject parent traversal
or compare normalised identities before membership/overlap checks. Cover the
demonstrated alias and retain the distinct-file positive case. Keep this a
fixture-path rule, not an implied live filesystem or submission check.
Owner: main checker/test maintainer.

Historical pre-repair reproductions after loading `p` as a fresh deep copy of the
fixture (both now return findings instead of `[]`):

```python
# Ownership bypass; run on its own copy.
p['requirements'][0]['evidence_owner'] = ' '
p['evidence'][0]['owner'] = ' '
assert validate_bid_package(p) == []  # observed residual gap

# Envelope bypass; run on a separate fresh copy.
alias = 'technical/../financial/price-schedule.md'
p['envelopes']['technical']['files'][0] = alias
p['requirements'][0]['response_location'] = alias
p['responses'][0]['response_location'] = alias
assert validate_bid_package(p) == []  # observed residual gap
```

## Output and approval limits

The script explicitly validates a deterministic fictional fixture. Its CLI reads
that fixed JSON file. `available` and `approved` are declared strings: the checker
does not retrieve evidence, authenticate reviewers, verify authority or inspect
the referenced bid documents. A nonblank approval owner demonstrates a named
record, not a signed live approval. These are scope limits, not additional patch
defects or grounds to turn this helper into a production submission service.

Live bid compliance, source support, arithmetic, staffing/schedule reconciliation,
native document rendering and submission authority remain NOT ASSESSED. No external
claims, finance opinion or numeric readiness score is issued. Safety review of the
two changed code surfaces found no added network, installer, credential collection
or file-mutation behaviour. Manual editorial review found no unsupported claim in
this report; automated genericness scoring and visual review are NOT ASSESSED.
The repair below closes the two demonstrated probes, not these live-output limits.

## Authorised repair disposition — 6 September 2026

- Ownership finding CLOSED: both `requirements[].evidence_owner` and
  `evidence[].owner` must be nonblank strings before indexing/comparison. Existing
  wrong-owner, availability, mandatory and approval checks remain intact.
- Path finding CLOSED: envelope files and requirement/response locations reject
  `..` segments with either slash style before membership/overlap checks. This is
  a lexical fixture rule; it does not resolve symlinks, establish physical file
  identity or inspect live bid files.
- Two added regression methods cover 21 owner mutations (seven values, each
  field separately and both together) and eight path mutations (two separators,
  each path surface separately and all together). Before repair: two tests,
  29 failing subtests, exit 1. After repair: all those cases pass.
- `python -B -X utf8 -m unittest discover -v`: 19 tests passed (15 proposal
  behaviour tests), exit 0; baseline was 17 passed.
- `python -B -X utf8 scripts/proposal_fixture_check.py`: PASS, exit 0.

Only the checker, its behaviour tests and this report were edited, using
`apply_patch`; existing changes were preserved. The fixture was not edited.
No external access, production document writes or proposal submission occurred.
