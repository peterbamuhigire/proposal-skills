# Pass 2 baseline scorecard (frozen before any change)

Date: 31 October 2026. Measured at commit `9089c0a` with a clean working tree. The
scores are reviewer judgements (inference), not bid-win probabilities. Each
dimension is on a /100 scale; the raw score is the mean of the ten dimensions. The
published score is `min(raw, 65)`. The improvement plan targets 95.

**Why the baseline is below the 29 October final.** Nothing was changed between
the two measurements: HEAD, validators and counts are identical (the last commit
after the October final is a test-only review note). The fresh baseline inspected
the parent skills and the primary sources that the October cycle did not read, and
found defects there (D1 to D8 in `00-scope-and-evidence.md`). The October final is
kept below for comparison. It is not a regression of the October work.

| Dimension | 29 Oct final | Fresh baseline | Named evidence | One-line deficiency |
|---|---:|---:|---|---|
| Doctrine | 70 | 70 | `skills/SKILL.md` forbids invented requirements and credentials; every framework skill defers to the issued solicitation | No rule says a solicitation's page cap and weights override the section skills' fixed page lengths (D5) |
| Taxonomy and routing | 55 | 50 | Harness: precision@1 23/31, expected-in-top-three 31/31, owned negatives 2/2; 1 of 115 skills has three positives and two owned negatives; lexical probe ranks `ppda-uganda` fourth for the Task 1 prompt and finds no skill for Task 3 | Sparse fixtures; `wb-ftp` still ranks UNDP first; no route for weight-driven page allocation |
| Skill depth | 65 | 55 | `world-bank/references/tech-fin-forms-guide.md` is correct; `world-bank/SKILL.md` 144-155 contradicts it; PPDA skill's envelope, bid-security and performance-security text contradicts the 2023 Regulations | Parent skills were not updated with their own references (D1 to D4) |
| Applied proof | 50 | 50 | 63 unit tests; one fictional bid package; three form regressions; synthetic Task 1 to 3 outputs | No redacted real solicitation, no evaluator, no real reviewer-rework data |
| Standards currency | 50 | 45 | Register of 11 records, 0 overdue, 4 `NOT_ASSESSED`; Regulations Annex X ranges, PPDA regulation 66 and 63 are not reflected in the skills; universal "typical" numbers carry no source (D3) | Skill prose and register are separate: nothing ties a numeric claim in a skill to a dated source |
| Output readiness | 60 | 55 | Task 1: no BDS compliance matrix route and a wrong envelope structure if the skill is followed; Task 3: 9.5-page default against a six-page cap, no allocation method | Two of three observed tasks cannot be completed from engine guidance alone |
| Accessibility and inclusion | 40 | 40 | Tagged PDF observed on the synthetic render; Public Sans embedded | No assistive-technology reading-order run, no accessibility certification (`NOT_ASSESSED`) |
| Production and handoff | 55 | 55 | Install path, marketplace parity, hard file ceiling (653 checkout, 512 package, limit 5000); submission-proof skill | No live submission receipt, signatory or portal evidence |
| Hygiene | 75 | 70 | Link and encoding gate passes, but a shipped skill (`skills/meta/skill-writing/SKILL.md` line 13) and the active authoring standard (`docs/skill-authoring-standard.md` lines 3 and 50) carry Windows absolute paths; the gate cannot see them (D7) | Machine-specific paths ship, and the validators have a false negative |
| Safety and integrity | 65 | 55 | Stale form map in the skill the router loads first (D1); bid-security and performance-security text can mislead a bidder on a legal requirement (D4) | A wrong form label or securing requirement can cause a non-responsive bid |

**Raw: 54.5.** Published: `min(54.5, 65) = 54.5`. 29 October final: raw 58.5,
published `min(58.5, 65) = 58.5`. The target for the improvement plan is 95 and is not
claimed.

**Blockers at baseline** (any one blocks release of a bid, whatever the score):
D1 (wrong current World Bank form labels in the router-loaded skill) and D4
(legal-requirement guidance on envelopes, bid security and performance security
that contradicts the issued Regulations). No live bid was in preparation, so no
bid was affected.

## Measured inputs

| Measure | Value at baseline | How measured |
|---|---|---|
| Validator results | 6 of 6 registered commands exit 0; 63 tests; 115 skills; 115 of 115 fully compliant on the canonical scanner | commands in `00-scope-and-evidence.md` |
| Routing precision@1 | 23 of 31 (74.2%) | `scripts/routing_smoke_test.py` (lexical proxy, not model behaviour) |
| Expected-in-top-three | 31 of 31 | same |
| Owned negatives (explicit `forbidden_primary`) | 2 of 2 pass; both belong to one skill | same; census script over `routing-fixtures.json` |
| Fixture coverage (three positives and two owned negatives) | 1 of 115 skills (`world-bank`) | census script over `routing-fixtures.json`: 24 distinct expected paths, 31 fixtures |
| Worked-example depth | 104 of 115 `SKILL.md` carry a `## Worked Example` heading; one sanitised EOI package under `examples/`; no worked example is a real bid | `grep` over `skills/**/SKILL.md` |
| Reference files | 221 | `find` over `skills/**/references` |
| Broken or machine-specific links | Markdown links 0 broken; machine-specific absolute paths: 3 lines in 2 active files (`skills/meta/skill-writing/SKILL.md:13`, `docs/skill-authoring-standard.md:3,50`) plus dated evidence documents, which are exempt records | `encoding_link_gate.py` plus a manual `grep` for drive-letter and home paths (the gate cannot see these) |
| Dangling cross-engine references | 0 of 6 distinct sibling paths dangle (accounting, design and research reference files resolved by `ls` in the local sibling checkouts; SRS `render_diagrams.py` found by `find`) | read-only `ls` and `find` |
| Expired source records | 0 overdue, 4 `NOT_ASSESSED`, of 11 (register review date 5 November 2026) | script over `docs/source-registers/2026-10-currentness.json` |
| Hard-coded page lengths in section skills | 8 skills prescribe fixed page lengths (`01`, `02`, `03`, `04`, `06`, `07`, `08`, `09`) | `grep` over `skills/pipeline/*/SKILL.md` |
| Stale World Bank form labels in skills | 9 lines in 3 files (D1, D2) | `grep` for `TECH-[5-8]` and `FIN-5` |
