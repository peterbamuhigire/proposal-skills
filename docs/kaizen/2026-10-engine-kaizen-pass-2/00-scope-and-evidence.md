# Pass 2 scope and evidence: proposal engine

Date: 31 October 2026. Branch `kaizen/2026-10-pass2`, created from `main` at
`9089c0a`. This continues the 29 October cycle in
`docs/kaizen/2026-10-engine-kaizen/`; it does not repeat it.

## Step 0: preconditions

| Item | Result |
|---|---|
| `git status --porcelain` at start | empty (0 lines); no foreign uncommitted files to preserve |
| Starting branch / HEAD | `main` / `9089c0a docs(proposal): record independent acceptance review` |
| Working branch | `kaizen/2026-10-pass2` (the 29 October branch `kaizen/2026-10` is already merged into `main`) |
| Read | Portfolio Kaizen Standard, currentness gate, router `AGENTS.md`, `skills/SKILL.md`, `skills/meta/kaizen-improvement-system/SKILL.md`, the September audits, the 29 October evidence folder (`05-final-report.md`, `06-next-cycle.md`, baseline, backlog, validation record, `currentness-evidence.md`, `official-form-observations.md`) |
| Host safety | No `sudo`, no package install, no service change. Primary sources were downloaded into a disposable directory outside the repository and are not committed |

### Status of the backlog inherited from 29 October (confirmed, not assumed)

| Inherited item | State at start of pass 2 | Evidence |
|---|---|---|
| P0 fixture false passes closed, regressions kept | Closed, still guarded | 63 unit tests pass, including the evidence-owner and path-alias negatives |
| P1 redacted end-to-end technical and financial package, with envelope-content and deadline checks | **Open.** No authorised redacted solicitation or bidder evidence exists. The fixture checker still validates declared file names only, never file content (`scripts/proposal_fixture_check.py` has no content scan). This cycle adds the content scan (P1-6) and leaves the live-package part open | `proposal_fixture_check.py` read in full |
| P1 PPDA amendment, thresholds, AfDB, UNDP, PRAG, GIZ currency | **Partly closed this cycle.** PPDA Act and 2023 Regulations read from PPDA-hosted PDFs; World Bank Regulations Seventh Edition read from the Bank PDF. AfDB, UNDP POPP and PRAG pages returned HTTP 403 to automated fetch and remain `NOT_ASSESSED` | Step 5 record in `04-validation-record.md` |
| P2 World Bank FTP prompt ranks UNDP first | **Open** (`wb-ftp` top three: UNDP, World Bank, AfDB) | `routing_smoke_test.py` output below |
| P2 three positives and two owned negatives beyond one route | **Open**: 1 of 115 skills | fixture census below |
| P2 reviewer rework data, assistive-technology reading order | **Open, `NOT_ASSESSED`**: no real-use data, no assistive-technology run | none available |

## Step 0.5: validators, run once before any change

All commands ran from the repository root with `python3` (the registered commands
say `python`; there is no `python` on this host).

| Command | Exit | Result |
|---|---:|---|
| `python3 -X utf8 scripts/validate_skills.py --baseline quality-baseline.json` | 0 | 115 active skills, 0 findings; `checkout_files=653 package_files=512 hard_limit=5000` |
| `python3 -X utf8 scripts/routing_smoke_test.py` | 0 | 31 fixtures; expected-in-top-three 31/31; precision@1 23/31; owned-negative primary 2/2 |
| `python3 scripts/proposal_fixture_check.py` | 0 | synthetic package PASS |
| `python3 -X utf8 scripts/source_ingestion_guardrail.py` | 0 | 0 findings |
| `python3 -X utf8 scripts/encoding_link_gate.py` | 0 | 0 findings |
| `python3 -B -X utf8 -m unittest discover` | 0 | 63 tests, OK |
| `python3 -B -X utf8 <dev-engine>/skills/sdlc-meta/skill-engine-audit/scripts/engine_compliance.py --root . --active-root skills --details` (read-only; the script writes only under `--fix`) | 0 | 115 skills, 115 fully compliant, 0 safe fixes applied |
| `python3 .codex/ensure_model_policy.py --runtime codex --check` (read-only check; Codex adapter, not applicable to Claude) | 0 | PASS. No model-policy change proposed or made |
| `git diff --check` | 0 | clean |

## Step 1: observe

Three tasks, run as a practitioner would: route through `AGENTS.md`, load the
named skills, produce the artefact, then judge it against the standard in the
mission. Every solicitation below is a synthetic fixture. No bidder identity,
credential, price or signature was invented; blank is recorded as blank.

### How the router was exercised

The router is `AGENTS.md` and `skills/SKILL.md`; the repository's own harness is
a lexical proxy (`routing_smoke_test.py`). Both were used. The lexical probe
ranked the three task prompts as follows (probe script kept outside the
repository; it reuses the harness's `tokens` and `frontmatter` functions):

| Task | Lexical top three | Correct skill present? |
|---|---|---|
| 1. PPDA open domestic ICT bid | `05-relevant-experience`, `sectors/ict`, `08-work-plan`; `ppda-uganda` is fourth | Found at rank 4, not rank 1. The `ppda-uganda` description does not contain "open domestic bidding" or "bid data sheet", which a bidder would say |
| 2. World Bank QCBS RFP | `world-bank`, `undp`, `kaizen-improvement-system` | Yes, rank 1 |
| 3. Weighted criterion, tight page cap | `website-design-proposal-strategy`, `ppda-uganda`, `risk-management` | **No.** No skill owns weight-driven page allocation outside GIZ |

Following `AGENTS.md` by hand (the real path an agent takes) gave: Task 1 ->
`skills/SKILL.md`, profile, `sectors/ppda-uganda`, `sectors/ict`, pipeline 03, 06,
07, 08, 10; Task 2 -> `sectors/world-bank` plus its two references and the same
pipeline skills; Task 3 -> `06-methodology`, `08-work-plan`, and the sector skill
for the named framework. The hand route was correct for Tasks 1 and 2. For Task 3
the router names no skill and no reference that decides what to cut.

### Task 1: PPDA open domestic bidding, ICT system

Request: technical proposal, work plan, staffing and a compliance matrix against
the Bid Data Sheet (BDS) for an ICT system, open domestic bidding. Fixture: a
fictional district office buying configuration, migration, deployment, training and
support for a ticketing system (synthetic; deadlines and values owned by the
fixture, as in the 29 October record).

What the engine's guidance produced, and what the primary source says:

| Question a bidder must answer | Engine guidance | Primary source (read 31 October 2026) | Verdict |
|---|---|---|---|
| How many envelopes? | `ppda-uganda/SKILL.md` lines 134 to 141: "All QCBS, QBS, LCS, and FBS procurements use two sealed envelopes". Nothing on supplies, works or non-consultancy services | Rules and Methods Regulations 2023, reg 66(2): "The one stage-single envelope method shall be used for the procurement of supplies, works and non-consultancy services"; reg 66(4): for "design and build, text books and information technology systems" the method may be one-stage two-envelope or two-stage; reg 66(6) ties the method to the evaluation method | **Major gap.** An ICT bidder following the skill would split price from technical in a single-envelope procurement |
| Is a bid securing declaration always required? | `ppda-uganda/SKILL.md` line 156: "Bid securing declaration included" as a universal Stage 1 check | Reg 63(1): the bidding document states any requirement for a bid security or bid securing declaration; reg 63(9): a declaration is required where restricted domestic bidding or quotation is used; reg 63(5): a bid security stays valid at least 28 days after bid validity expires | **Major defect.** Open domestic bidding is governed by the bidding document, which may require a bid security |
| Performance security form? | `ppda-uganda/SKILL.md` lines 239 to 244: "Uganda PPDA uses a Performance Securing Declaration rather than traditional bank guarantees" | Contracts Regulations 2023, reg 11(1): the bidding documents state the requirement for "a performance security or a performance securing declaration"; reg 11(3): a bank guarantee must be acceptable to the Bank of Uganda and an insurance bond to the Insurance Regulatory Authority | **Major defect.** Over-generalised from the quotation-method form |
| Submission channel? | Skill assumes sealed physical envelopes ("signed, sealed, submitted", line 155) | Reg 68(2): delivery "in person or electronically", by PDU staff or "a bid box or government electronic system". PPDA's home page lists a press statement dated 5 June 2026, "Uganda to Roll Out E-GP to all Entities on 1st July 2026"; its body could not be retrieved, so the mandate's scope per entity is `NOT_ASSESSED` | **Currency gap.** The channel must come from the solicitation |
| Margins of preference? | `ppda-act-and-regulatory-framework.md` lines 117 to 146 | Cap. 205 section 62: 15% goods, 7% works or services, 4% joint ventures with a Ugandan partner | **Correct.** Verified; keep |
| Advance payment ceiling? | Reference line 231: above 30% needs Treasury approval | Contracts Regulations 2023, reg 43(3) and (4) | **Correct.** Verified; keep |
| A compliance matrix against the BDS? | None for PPDA. Only the GIZ skill has a matrix reference (`giz-compliance-matrix.md`) | Not applicable | **Gap.** The matrix was improvised from the GIZ field list |

The technical proposal, work plan and staffing table repeat the 29 October fixture
and are not reproduced here. The two artefacts the engine could not support were the
BDS compliance matrix and the submission-structure decision: neither could be
derived from the engine alone, and the second would have been wrong if derived from
the skill. That is the finding. The re-run after the fixes is in
`04-validation-record.md`.

### Task 2: World Bank QCBS consulting RFP, mandated forms

Request: respond using the mandated forms; check form order, page limits and
technical/financial separation. Source re-read: the March 2025 revision of the
non-supervision consulting RFP (`TECH-1` to `TECH-8`, `FIN-1` to `FIN-4`; the form
checklist, the Data Sheet's blank page-limit column and the "[insert number]"
minimum technical score were reconfirmed on 31 October 2026).

| Question | Engine guidance | Verdict |
|---|---|---|
| Form labels | `references/tech-fin-forms-guide.md` is correct (fixed on 29 October). The parent `world-bank/SKILL.md` lines 144 to 155 still teach the old map: TECH-5 team composition, TECH-6 CVs, TECH-7 staffing schedule, TECH-8 Gantt. Line 320 still promises "FIN-1 through FIN-5". `references/evaluation-scoring-guide.md` lines 130 and 142 head "Key Personnel (TECH-5/6)" and "Work Plan (TECH-7/8)". `afdb/SKILL.md` line 230 repeats "TECH-1 through TECH-8, FIN-1 through FIN-5" | **Critical.** The router loads `SKILL.md` first. The 29 October fix reached only the reference, so the skill and its reference now contradict each other |
| Pass mark | `SKILL.md` lines 136 and 273: "typically 75 out of 100"; "Score 74 = eliminated" | Regulations Seventh Edition (September 2025), Annex X, para 4.5: the minimum "shall normally be in the range of 70-85%"; the RFP sets the number. **Major defect** (unsupported universal number) |
| Criterion ranges | `SKILL.md` lines 165 to 169: firm experience 10 to 20, methodology 30 to 50, key staff 30 to 60 | Annex X, Table 1: methodology 20 to 50%, key staff 30 to 60%, relevant experience of firm 0 to 10%, transfer of knowledge 0 to 10%, nationals 0 to 10%. Firm experience is overstated by a factor of two. **Major defect** |
| Quality/cost weighting | `SKILL.md` line 125: "typically 70-80%, financial 20-30%" | Annex X, Table 2: 90/10 for highly complex work, 70-80/30-20 for moderate complexity, 60-50/40-50 for routine. Partial. **Minor defect** |
| Standstill, debrief | `evaluation-scoring-guide.md`: 10 business-day standstill; 3 days to request, 5 to provide | Regulations paras 5.81 and 5.82 and the standstill text (10 Business Days). **Correct** |
| Page limits, envelope separation | Guide correctly tells the bidder to copy limits from the issued RFP | Consistent with the SPD: the limit column is blank in the template. **Correct** |

### Task 3: unusual weighted criterion, tight page limit

Synthetic RFP (new for this pass): technical narrative capped at six pages, CVs and
forms excluded. Weights: methodology 30, key experts 25, national participation and
transfer of knowledge 25 (unusually high), data protection and continuity 15,
presentation 5. Sub-threshold: national participation must score at least 60% of
its points.

What the engine's section skills prescribe by default (sum of the stated lengths):
`03-understanding-of-assignment` 1 to 2 + 0.5 + 1 + 0.5 to 1 pages, `06-methodology`
"five to ten pages" and the line "this section should be the longest in the technical
proposal" (`06-methodology/SKILL.md` line 342), `07-team-composition` 1 page,
`08-work-plan` 0.5 page. The minimum is 9.5 pages before the executive summary
(`02`, "two to three pages maximum") and the firm profile (`04`, one to two). Against
a six-page cap that is at least 3.5 pages over, and the methodology rule directs the
largest share to a 30-point criterion while the 25-point national-participation
criterion, with its sub-threshold, has no home. No skill says that the solicitation's
cap and weights override these defaults. Only `giz-eu-local-procurement-response`
(`SKILL.md` lines 49 and 68; `giz-compliance-matrix.md` line 42) says "allocate page
budget according to score weight", and it gives no method, floor or check.

**Verdict: major gap and contradiction.** A proportional allocation (30/25/25/15/5 of
six pages is 1.8/1.5/1.5/0.9/0.3) is the starting point; the national-participation
sub-threshold sets a floor and the five-point criterion cannot be a page. That
arithmetic was done by hand; no tool in the engine checks it.

## Defect register from Step 1

| ID | Severity | File and line | Defect |
|---|---|---|---|
| D1 | Critical | `skills/profiles-sectors/sectors/world-bank/SKILL.md` 144-155, 251, 320 | Pre-March-2025 TECH map and FIN-5 survive in the router-loaded skill |
| D2 | Major | `world-bank/references/evaluation-scoring-guide.md` 130, 142; `afdb/SKILL.md` 230 | Same stale labels in the scoring guide and the AfDB comparison table |
| D3 | Major | `world-bank/SKILL.md` 125, 136, 165-169, 263-264, 273; `afdb/SKILL.md` 138, 149, 231 | Universal "typical" numbers contradict Regulations Annex X or have no source |
| D4 | Major | `ppda-uganda/SKILL.md` 134-141, 155-156, 239-244 | Envelope structure, bid security and performance security guidance contradicts the 2023 Regulations; electronic submission absent |
| D5 | Major | `06-methodology/SKILL.md` 342; pipeline skills 01 to 09 fixed page lengths | Fixed lengths and "longest section" rule contradict a solicitation's cap and weights; no rule of precedence |
| D6 | Major | no file | No method or check for weight-driven page allocation or a BDS compliance matrix outside GIZ |
| D7 | Major | `skills/meta/skill-writing/SKILL.md` 13; `docs/skill-authoring-standard.md` 3 and 50 | Windows absolute paths to a sibling checkout shipped in a skill and an active standard. `scripts/encoding_link_gate.py` flags only one earlier, narrow sibling-route pattern and `scripts/check_marketplace.py` scans only `AGENTS.md` and `README.md`. The count was later widened by a script census (see `03-experiment-log.md`) |
| D8 | Major | `scripts/proposal_fixture_check.py` | Envelope separation checks file names only. The 29 October "no FIN token in the technical file" scan was manual and left no automated trace |
| D9 | Minor | `sectors/ppda-uganda/SKILL.md` description | Lacks "open domestic bidding" and "bid data sheet"; rank 4 for the Task 1 prompt |
| D10 | Minor | `sectors/world-bank/SKILL.md` description | `wb-ftp` fixture still ranks UNDP first |

Guidance that was contradictory (D1/D2, D5), missing (D6) or ignored in practice
(the 29 October fix of the reference was ignored by the parent skill, D1) is
listed above. Critical defects: **one (D1)**. It must be fixed and verified or
escalated (see `02-improvement-backlog.md`).

## Primary sources read this cycle (access date 31 October 2026)

Downloaded into a disposable directory outside the repository; hashes let a
reviewer confirm they read the same bytes. Nothing is committed.

| Source | SHA-256 (first 16 hex) |
|---|---|
| PPDA Act, Cap. 205 (PPDA-hosted PDF, HTTP `Last-Modified` 19 March 2026) | `e4f882f2c96f777f` |
| PPDA Rules and Methods for Supplies, Works and Non-Consultancy Services Regulations 2023 (Statutory Instrument 2023 No. 100) | `b47e3c2398abb5f1` |
| PPDA Procurement of Consultancy Services Regulations 2023 | `34ded9302b2f254b` |
| PPDA Contracts Regulations 2023 | `309bc7e5543faadc` |
| PPDA Evaluation Regulations 2023 (downloaded; not relied on for any claim) | `deac6077119a3ad8` |
| PPDA Amendment of Schedule 4 Instrument 2023 (No. 96; Contracts Committee composition only) | `3c87d3e747ef7e09` |
| World Bank Procurement Regulations for IPF Borrowers, front page "Seventh Edition - September 2025" | `7f118ac8fa8949ef` |
| World Bank Standard RFP, Consulting Services (Non-supervision), revision "March 2025" | `2db5b2de645494aa` |

Fetch failures, recorded as `NOT_ASSESSED` evidence rather than guessed: AfDB
procurement framework page and the AfDB Operations Procurement Manual (May 2026)
returned HTTP 403; UNDP POPP and the Commission's PRAG page returned HTTP 403;
ISO's standard page returned HTTP 403 on direct fetch; EUR-Lex returned an empty
page to the fetch tool.
