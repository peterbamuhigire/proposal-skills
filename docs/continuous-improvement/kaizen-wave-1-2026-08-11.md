# Proposal Skills: Kaizen Wave 1 Report

Date: 11 August 2026
Repository: C:\wamp64\www\proposal-skills
Wave: 1 implementation
Owner: Peter / proposal-engine maintainer

## Scope and evidence rules

This report covers only the assigned proposal-skills working tree. No commit,
push, fetch, pull, reset, or sibling-repository write was performed.

Evidence labels used below:

- Structural: files, contracts, route declarations, encoding, and links.
- Behavioural: executable fixture assertions, including a blocking case.
- Render: document or visual inspection. No render was produced in this wave.
- System: execution against an external platform or production-like service.
- Production: evidence from a real client engagement or live deployment.
- NOT ASSESSED: the check was not available or not required for this bounded
  patch. It is not a pass.

All fixture content is explicitly fictional and test-labelled. It is not a
tender, client record, procurement claim, credential, past-performance claim, or
submission package.

## Baseline

The baseline branch was clean and aligned with origin/main:

    git status --short --branch
    ## main...origin/main

The initial assessment records 108 active skills, 193 references, one template,
39 documents, 12 book-extraction records, six scripts, and one routing-fixture
file for this repository. It records 108/108 contracts, 18/18 routes, zero
source-guardrail findings, raw score 60.8/100, published exercise score 55/100,
and maturity L2: repeatable with behavioural evidence absent. Source:
C:\wamp64\www\KAIZEN-INITIAL-ASSESSMENT.md, proposal-skills section and
baseline table.

The 55-point publication ceiling is used only in this assignment report. The
repository's permanent 65-point audit rule remains in README.md and AGENTS.md.

Baseline command evidence:

| Command | Result |
| --- | --- |
| python -X utf8 scripts\validate_skills.py --baseline quality-baseline.json --details | Exit 0; 108 active skills; zero findings |
| python -X utf8 scripts\routing_smoke_test.py | Exit 0; 18 fixtures; 100.0% top-three precision |
| python -X utf8 scripts\source_ingestion_guardrail.py | Exit 0; zero findings |
| python -X utf8 -m unittest discover -v | Exit 1; zero tests discovered; NO TESTS RAN |
| strict UTF-8 decode of tracked repository text | Exit 0; no invalid UTF-8 files |
| exact stale-route search for the two assigned sibling paths | Two findings in README.md |

The initial assessment described mojibake in router text. A strict worker-level
scan of the tracked Markdown and JSON found no verified corrupt UTF-8 sequence
or replacement character to rewrite. The patch therefore adds a gate that
prevents recurrence and repairs the independently verified stale routes without
inventing an encoding conversion.

No numeric raw re-score is issued in this worker report. The available 60.8
raw score is retained as the baseline; no dimension-level scoring instrument or
independent re-audit was supplied to support a defensible after-score. The
published after-score and target 95 are therefore NOT ASSESSED, not claims of
achievement.

## Changes implemented

### P0-05a: portable cross-engine route repair

- Gap: The README route table used the device-specific paths
  C:\Users\Peter\source\repos\social-media-skills and
  C:\Users\Peter\source\repos\business-plan-skills.
- Root cause: A historical local checkout path was retained as an active
  handoff instead of using the repository's canonical remote route.
- Exact change: Replaced both entries in README.md with the verified canonical
  repository URLs. The URLs were read from the sibling repositories' local
  origin remotes on 11 August 2026; URL network liveness was not tested.
- Hypothesis: A fresh agent can follow the handoff from an independent checkout
  without translating a machine-specific path.
- Owner: Peter / proposal-engine maintainer.
- Measure: The stale-path search returns zero findings; the new
  scripts/encoding_link_gate.py portable-route check passes.
- Risk: A remote URL can change or be unavailable even when the string is
  correct. The gate does not certify network reachability.
- Rollback: Restore only the two README route-table lines if a later
  repository-routing review identifies a different canonical target.
- Acceptance evidence: python -X utf8 scripts\encoding_link_gate.py returned
  exit 0 with zero findings; the existing 18 routing fixtures remained green.
- Standardisation: Keep sibling-engine routes as canonical URLs or named
  engine keys, never local checkout paths. The encoding/link gate is listed in
  AGENTS.md, README.md, and CONTRIBUTING.md.
- Re-audit: 18 August 2026.

### P0-05b: encoding and link regression gate

- Gap: Existing skill validation checked active skill bodies and references,
  but there was no repository-wide gate for strict UTF-8, mojibake markers,
  broken local Markdown links, and the two stale sibling routes.
- Root cause: Structural skill validation and source-ingestion validation did
  not own the full controller and documentation surface.
- Exact change: Added scripts/encoding_link_gate.py. It decodes tracked text as
  UTF-8, checks mojibake markers in Markdown, resolves local Markdown links,
  rejects the two device-specific route patterns, and requires the two verified
  canonical URLs in README.md.
- Hypothesis: A deterministic, repository-local release check will expose
  encoding and handoff regressions before they become routing defects.
- Owner: Peter / proposal-engine maintainer.
- Measure: Gate findings remain zero on the repository; its regression test
  proves that invalid bytes, a stale route, and a broken local link are
  reported.
- Risk: The gate could treat a deliberately illustrative path as a local link.
  It now follows the existing validator convention and ignores root-relative URL
  paths while still checking relative and Windows-drive local paths.
- Rollback: Remove the new script and its three documented command entries;
  retain the route repair if it remains independently useful.
- Acceptance evidence: Gate exit 0 with zero findings; gate regression test
  passed; git diff --check passed.
- Standardisation: Run the gate before release and retain its raw output in Wave
  reports. Keep unverified network reachability separate from structural URL
  presence.
- Re-audit: 18 August 2026.

### P1-05: fictional proposal behaviour fixture

- Gap: unittest discovered zero tests, so the engine had no executable
  representative bid-package evidence for requirement traceability, evidence
  ownership, technical/financial separation, or mandatory-omission blocking.
- Root cause: The repository had contract and routing checks but no deterministic
  behavioural fixture or test package.
- Exact change:
  - Added tests/fixtures/fictional-bid-package.json, labelled as fictional test
    data.
  - Added scripts/proposal_fixture_check.py with a reusable validator.
  - Added tests/test_proposal_behaviour.py with a complete positive case and a
    negative case removing mandatory requirement M-FIN-01.
  - Added tests/test_encoding_link_gate.py and tests/__init__.py so default
    unittest discovery executes the tests.
- Hypothesis: A small fixture at the proposal evidence boundary will make
  recurring compliance failures observable without fabricating a client bid.
- Owner: Peter / proposal-engine maintainer.
- Measure: Three tests execute; the complete package passes; removing one
  mandatory response produces a blocking validator error.
- Risk: A small fixture cannot prove evaluator scoring, document fidelity,
  rendering, or production submission readiness. It is explicitly limited to
  the named behaviours.
- Rollback: Remove only the new fixture, validator, test files, and package
  marker if the schema proves costly; do not weaken existing validators.
- Acceptance evidence: python -X utf8 scripts\proposal_fixture_check.py
  returned exit 0; python -X utf8 -m unittest discover -v returned exit 0 with
  three tests passing.
- Standardisation: Keep future proposal fixtures under tests/fixtures/, require
  a fictional/test label, and retain at least one mandatory omission test.
  Promote the fixture to a release gate after two stable runs and independent
  review.
- Re-audit: 25 August 2026.

### P2-03 bounded slice: model-specific duplication reduction

- Gap: CLAUDE.md was 285 lines and duplicated control-plane, routing, safety,
  and workflow content from AGENTS.md, README.md, and skills/SKILL.md.
- Root cause: Claude and Codex entrypoints evolved as parallel policy documents
  instead of one canonical rule set with a thin adapter.
- Exact change: Reduced CLAUDE.md to a seven-line Claude discovery bridge
  containing @AGENTS.md and pointers to the canonical README and parent skill.
  Canonical rules remain in AGENTS.md, README.md, and skills/SKILL.md.
- Hypothesis: Removing duplicate policy lowers drift and context cost while
  preserving the repository's model-neutral control plane.
- Owner: Peter / proposal-engine maintainer.
- Measure: CLAUDE.md decreased from 285 to seven lines; the 108-skill validator
  and 18 routing fixtures did not regress.
- Risk: Claude's vendor parser or import behaviour may change. This structural
  bridge does not prove runtime instruction discovery.
- Rollback: Restore the prior CLAUDE.md only if a dated Claude smoke test
  demonstrates a discovery failure; keep canonical rules in AGENTS.md.
- Acceptance evidence: The bridge is present, AGENTS.md exists, and all
  repository structural/routing checks pass. Claude runtime discovery is NOT
  ASSESSED.
- Standardisation: Keep vendor files as thin adapters. Put reusable rules in
  model-neutral root instructions and SKILL.md files.
- Re-audit: 25 August 2026; vendor compatibility review 11 November 2026.

## Before/after measures

| Measure | Baseline | Wave 1 result | Evidence |
| --- | ---: | ---: | --- |
| Active skills | 108 | 108 | validate_skills.py; no catalogue change |
| Contract findings | 0 | 0 | validate_skills.py --baseline |
| Routing fixtures | 18 | 18 | routing-fixtures.json and routing smoke test |
| Routing top-three precision | 100.0% | 100.0% | routing_smoke_test.py |
| Source-ingestion findings | 0 | 0 | source_ingestion_guardrail.py |
| Stale assigned device routes | 2 | 0 | exact path search and encoding/link gate |
| Strict UTF-8 invalid files | 0 | 0 | worker-level scan and encoding/link gate |
| unittest discovered tests | 0 | 3 passing | baseline and Wave 1 unittest runs |
| CLAUDE.md length | 285 lines | 7 lines | Get-Content line-count command |

The fixture adds behavioural evidence but does not convert structural evidence
into render, system, or production evidence.

## Validation record

### Structural checks

| Command | Exit | Raw result summary |
| --- | ---: | --- |
| python -X utf8 scripts\validate_skills.py --baseline quality-baseline.json --details | 0 | 108 active skills; zero findings |
| python -X utf8 scripts\routing_smoke_test.py | 0 | 18 fixtures; 100.0% top-three precision |
| python -X utf8 scripts\source_ingestion_guardrail.py | 0 | zero findings |
| python -X utf8 scripts\encoding_link_gate.py | 0 | zero findings; encoding, local links, and sibling routes passed |
| git diff --check | 0 | pass |
| python -m py_compile scripts\encoding_link_gate.py scripts\proposal_fixture_check.py tests\test_encoding_link_gate.py tests\test_proposal_behaviour.py | 0 | pass |

### Behavioural checks

| Command | Exit | Raw result summary |
| --- | ---: | --- |
| python -X utf8 scripts\proposal_fixture_check.py | 0 | fictional fixture result PASS |
| python -X utf8 -m unittest discover -v | 0 | three tests ran; three passed |
| Gate regression test | included above | invalid UTF-8, stale route, and broken link were all detected in a temporary fixture |
| Mandatory-omission test | included above | missing M-FIN-01 produced a blocking error |

### Safety and anti-slop review

The changed scripts and fixture were read in full and scanned for remote
installers, command execution, credential collection, secret handling,
exfiltration, and hidden system actions. No findings were returned by the
static safety-pattern scan. The fixture is labelled fictional and contains no
client claim or real-person credential.

The required anti-slop controls were applied during authoring: concrete
repository paths, exact command evidence, explicit limitations, a negative
case, and no unsupported procurement claims. An automated ai-slop-audit runner
was not found in the assigned repository and is NOT ASSESSED.

### Evidence boundaries

| Evidence class | Status | Reason |
| --- | --- | --- |
| Structural | PASS | Validators, route fixtures, encoding/link gate, and diff check passed |
| Behavioural | PASS for named fixture scope | Three deterministic tests cover traceability, ownership, envelope separation, and one blocking omission |
| Render | NOT ASSESSED | No DOCX, PDF, PPTX, or rendered proposal artefact was created |
| System | NOT ASSESSED | No external procurement portal, agent runner, or network reachability check was used |
| Production | NOT ASSESSED | No client tender or live engagement was supplied |

## Compatibility

| Entry path | Evidence | Status and limitation |
| --- | --- | --- |
| Codex-style repository entry | Root AGENTS.md, canonical skills/SKILL.md, and 108-skill validation | Structural PASS; runtime discovery is not independently observed |
| Claude Code entry | Seven-line CLAUDE.md bridge with @AGENTS.md | Bridge structure PASS; Claude runtime import behaviour NOT ASSESSED |
| Generic agent/manual entry | README.md plus explicit AGENTS.md and skills/SKILL.md pointers | Manual route available; universal automatic discovery NOT ASSESSED |

The repository-referenced paths
C:\Users\Peter\.claude\skills\skills\sdlc-meta\skill-engine-audit\scripts\engine_compliance.py
and
C:\Users\Peter\.claude\skills\skills\sdlc-meta\skill-writing\scripts\quick_validate.py
were not present on this machine. Those checks are NOT ASSESSED; no successful
execution is claimed.

## Remaining backlog

### P0

- No additional assigned P0 defect was observed after the route repair and
  gate run. The original mojibake report remains a re-audit item because this
  worker found no verified corrupt sequence to rewrite.
- Confirm the two canonical URLs during the 18 August 2026 re-audit. The local
  git remote -v evidence supports their identity, not network availability.

### P1

- Run the fictional fixture twice in a clean fresh context and have an
  independent reviewer inspect its boundary. The current evidence is one
  successful Wave 1 run.
- Add a separate evaluator-scoring or document-output fixture only when a real,
  authorised output contract is supplied. Do not use the current fixture to
  claim submission readiness.
- Add proposal-specific render/accessibility evidence when document tooling and
  an authorised artefact are available.

### P2

- Re-test Claude import behaviour and generic-agent instruction discovery using
  dated vendor/runtime evidence.
- Expand behavioural coverage only for recurring failure modes, such as
  inconsistent staffing and schedule, unsupported credentials, or arithmetic
  reconciliation. No client data should be added.
- Review external route ownership and mutable standards on 11 November 2026.

## Unassessed items

- Claude runtime loading of @AGENTS.md.
- Generic-agent automatic instruction discovery.
- External URL reachability.
- Native document generation, reopen, render, accessibility, and pagination.
- Real procurement-system submission or portal behaviour.
- Client readiness, evaluator scoring, win probability, past performance, and
  production outcomes.
- Automated skill-engine-audit, quick_validate.py, and ai-slop-audit execution
  because no runnable local command was found for those paths.

## Next-wave recommendations

1. Fresh-context re-audit the route gate and thin bridge on 18 August 2026.
2. Repeat the fictional fixture in a second clean run, then decide whether it
   belongs in the release gate on 25 August 2026.
3. Add one authorised proposal-output fixture only when the repository has a
   defined document/render contract and the required tooling is available.
4. Keep the exercise's 55 cap confined to reports; preserve the permanent
   repository 65 cap.

## Diff and scope review

The baseline was clean, so no pre-existing or unrelated working-tree changes
were identified. The final intended change set is:

- AGENTS.md
- CLAUDE.md
- CONTRIBUTING.md
- README.md
- scripts/encoding_link_gate.py
- scripts/proposal_fixture_check.py
- tests/__init__.py
- tests/fixtures/fictional-bid-package.json
- tests/test_encoding_link_gate.py
- tests/test_proposal_behaviour.py
- docs/continuous-improvement/kaizen-wave-1-2026-08-11.md

No sibling repository or workspace-level report was modified.
