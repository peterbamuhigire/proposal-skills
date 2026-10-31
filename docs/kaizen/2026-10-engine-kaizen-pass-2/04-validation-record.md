# Pass 2 validation record: 31 October 2026

Every command ran from the repository root on the final tree (HEAD plus the
evidence files and the `AGENTS.md` pointer committed after this record). The
registered commands name `python`; this host has only `python3`, so `python3` was
used. No `sudo`, no package installation, no model call and no network write.
Primary sources were fetched into a disposable directory outside the repository.

## Registered and added checks

| Command | Baseline | Final |
|---|---|---|
| `python3 -X utf8 scripts/validate_skills.py --baseline quality-baseline.json` | exit 0; 115 skills, 0 findings; `checkout_files=653 package_files=512` | exit 0; 115 skills, 0 findings; `checkout_files=817 package_files=525`. An independent `find` over the checkout (files and symlinks, including `.git`) also returns 817. The run now includes the form-label scan |
| `python3 -X utf8 scripts/routing_smoke_test.py` | exit 0; 31 fixtures; top three 31/31; precision@1 23/31; owned negatives 2/2 | exit 0; 41 fixtures; top three 41/41; precision@1 32/41; owned negatives 7/7 |
| `python3 scripts/proposal_fixture_check.py` | exit 0; PASS | exit 0; PASS |
| `python3 -X utf8 scripts/source_ingestion_guardrail.py` | exit 0; 0 findings | exit 0; 0 findings |
| `python3 -X utf8 scripts/encoding_link_gate.py` | exit 0; 0 findings | exit 0; 0 findings, now including the machine-path rule |
| `python3 -B -X utf8 -m unittest discover` | exit 0; 63 tests | exit 0; 117 tests |
| `python3 -B -X utf8 scripts/check_form_labels.py` (new) | not present; the same scan on the old tree reported 12 findings | exit 0; PASS |
| `python3 -B -X utf8 scripts/check_source_currency.py` | exit 0 | exit 0; 14 records, 0 overdue, 4 `NOT_ASSESSED` |
| `python3 scripts/proposal_fixture_check.py --input examples/uganda-eoi-sanitised/validator-input.json --check-content` (new) | not present; the old checker returned PASS on a planted price | exit 0 on the clean example; exit 1 on the planted-price copy |
| `python3 -B -X utf8 scripts/page_budget_check.py tests/fixtures/page-budget-example.json --propose` (new) | not present | exit 0; 2.0 / 1.5 / 1.5 / 1.0 pages, 6 of 6 |
| `python3 -B -X utf8 <dev-engine>/skills/sdlc-meta/skill-engine-audit/scripts/engine_compliance.py --root . --active-root skills --details` | exit 0; 115 of 115 compliant | exit 0; 115 of 115 compliant; 0 safe fixes applied |
| `python3 .codex/ensure_model_policy.py --runtime codex --check` | exit 0; PASS | exit 0; PASS. Codex adapter; read-only check; no policy change |
| `git diff --check` | clean | clean |

`NOT_ASSESSED`, with reasons:

- **GitHub Actions run of the widened workflow.** No runner is available. The YAML parses and every command in it passes locally.
- **Native install in a disposable container** (done on 29 October). No container was created this cycle and nothing was installed, so the install path was not re-run. The package file count (525) is below the 5,000 ceiling.
- **`tests/agent-integration/test_proposal_agent_contract.py`.** It is a standalone script, outside unittest discovery and CI. Run directly it prints `PASS: proposal-skills agent contract`. It looks for the sibling `chwezi-engine-agents` catalogue through `ROOT.parent` (line 28); it did not fail here and no change was made.
- **Tier 3 behavioural routing and any model-judged check.** Not run by rule. Routing figures are the lexical proxy only.
- **Assistive-technology reading order and font fidelity of a completed form.** No tool available without installing packages.
- **A redacted real solicitation and bidder evidence pack.** None authorised or supplied.

## Step 1 re-runs after the changes

### Task 1: PPDA open domestic bidding, ICT system

Router: the lexical probe now ranks `ppda-uganda` first (35.47 against 13.68 for the next skill; it was fourth at baseline). Following `AGENTS.md` by hand reaches the skill, its new submission table and the weighted-page-budget reference.

Submission-structure decision, now derivable from the skill. For the synthetic BDS (technical compliance method, physical sealed bid, price in the same package) the table gives one-stage single envelope (Rules and Methods Regulations 2023, regs 66(2) and 66(6)(a)); an ICT-systems buyer may instead choose two envelopes or two stages (reg 66(4)), so the BDS wording is the deciding fact and any silence is a clarification question. The 29 October pack (original and copy in one outer package) is consistent with the single-envelope rule.

BDS compliance matrix produced with the new reference (fictional BDS values from the 29 October fixture; rows that need bidder evidence stay open):

| ID | Source | Requirement | Class | Gate | Response location | Evidence | Status | Risk |
|---|---|---|---|---|---|---|---|---|
| C-001 | BDS: method | Open domestic bidding, technical compliance evaluation | submission | pass/fail | Bid cover sheet | BDS clause | covered (synthetic) | minor |
| C-002 | BDS: submission | One outer package holding the original and the copy; technical response and price schedule together | submission | pass/fail | Pack index | Regulations reg 66(2), 66(6)(a) agree | covered; confirm against the issued BDS | major |
| C-003 | BDS: channel | Physical delivery; no e-GP requirement stated | submission | pass/fail | Delivery plan | Reg 68(2) permits both; e-GP status for this entity | open: `NOT_ASSESSED` for e-GP | major |
| C-004 | BDS: bid security | Not stated | financial | pass/fail | none | Reg 63(1): the bidding document states any requirement | open: clarification question, not an assumption | knockout |
| C-005 | BDS: performance security | Not stated | contractual | pass/fail | none | Contracts reg 11(1) | open: clarification question | major |
| C-006 | BDS: deadline | 30 November 2026, 11:00 East Africa Time (synthetic) | submission | pass/fail | Pack index | One timestamp used everywhere | covered (synthetic) | knockout |
| C-007 | BDS: validity | 90 days from the deadline | submission | pass/fail | Bid cover sheet | Any bid security must outlast it by 28 days (reg 63(5)) | covered; depends on C-004 | major |
| C-008 | BDS: currency and tax | UGX, amounts exclude taxes | financial | pass/fail | Price schedule | No rate assumed | covered (synthetic) | major |
| C-009 | Section 3: eligibility | Registration, tax and ownership declarations | eligibility | pass/fail | Eligibility file | None supplied | open: `NOT_ASSESSED`, release blocker | knockout |
| C-010 | Section 6: requirements | Technical response is Responsive or Non-Responsive | rated technical | R/NR | Technical response | Fixture response only | open | major |
| C-011 | Qualification form | Similar contracts and key personnel | eligibility | pass/fail | Staffing schedule | None supplied | open: `NOT_ASSESSED`, release blocker | knockout |
| C-012 | Preference | Margin of preference claimed | financial | n/a | Eligibility file | Cap. 205 s.62: 15% goods, 7% works or services; ownership evidence absent | open: `NOT_ASSESSED` | minor |

Result: the two artefacts the engine could not support at baseline (matrix and envelope decision) can now be produced from the skill and the reference, with the legal basis cited. No bidder identity, credential, price or signature was invented; the package stays blocked.

### Task 2: World Bank QCBS consulting RFP

Independent cross-check, run on 31 October 2026: the form checklist was extracted from the downloaded March 2025 RFP text, then compared with `tests/fixtures/world-bank-form-map.json` and with the table in `world-bank/SKILL.md`. All 12 form ids (TECH-1 to TECH-8, FIN-1 to FIN-4) agree; no FIN-5 exists in any of the three. `check_form_labels.py` returns PASS. The Data Sheet template's blank minimum technical score and the indicative range 70 to 85 now match the skill (`test_world_bank_forms.py`, three tests). The 29 October synthetic pack (11 technical and 5 financial pages, form order TECH-1 to TECH-8 then FIN-1 to FIN-4) was not re-rendered; it still satisfies the corrected map.

### Task 3: unusual weighted criterion, tight page limit

Router: the lexical probe now ranks `06-methodology` first for the capped, weighted prompt (14.08; at baseline no relevant skill appeared). The reference and `scripts/page_budget_check.py` handle the brief:

`python3 -B -X utf8 scripts/page_budget_check.py tests/fixtures/page-budget-example.json --propose` returns methodology 2.0, key experts 1.5, national participation and knowledge transfer 1.5, data protection and continuity 1.0, presentation embedded, 6 of 6 pages. The hand calculation (6 pages over 95 live points: 1.89, 1.58, 1.58, 0.95, rounded to quarter pages by largest remainder) gives the same. The allocation that follows the old "methodology is the longest section" habit (5.0, 0.25, 0.25, 0.5) exits 1 with three floors missed and the 25-point criterion at 4% of the pages. Allocation arithmetic only; no evaluator score is predicted.

## Step 5: currency record

Access date for every row: 31 October 2026. Review date for every volatile row: 30 November 2026. The machine-readable register is `docs/source-registers/2026-10-currentness.json`; the gate enforces the dates.

| Item | Source read | Support state | What was and was not established |
|---|---|---|---|
| PPDA Act, Cap. 205 | PPDA-hosted PDF (HTTP `Last-Modified` 19 March 2026), full text | `SCOPED` | Section 62 margins 15% goods, 7% works or services, 4% joint venture; section 128 leaves the suspension period to the Authority. The engine's margin text was correct. Later amendments not checked |
| PPDA Regulations 2023 | Rules and Methods, Consultancy Services, Contracts (PPDA-hosted PDFs); Schedule 4 instrument 2023 No. 96 | `SCOPED` | Regs 63, 66, 68, 47, 48, 62, 11, 43 read. The 30% advance ceiling was correct. Schedule 4 changes Contracts Committee composition only. Not read: guidelines and circulars |
| PPDA thresholds | Not reachable in the regulations; they sit in guidelines | `NOT_ASSESSED` | Micro-procurement limits and security amounts unverified; the old UGX 5M and 10M figures are now labelled |
| PPDA standard bidding documents | Index page 1 | `SCOPED` | 12 documents listed with no version or date; two further index pages not read |
| PPDA e-GP | PPDA home page entry; Rules and Methods reg 68(2) | `SCOPED` for the title, the 5 June 2026 date and the regulation; mandate scope `NOT_ASSESSED` | The statement's body could not be retrieved. Secondary reports conflict on rollout status and were not relied on |
| World Bank Regulations | Bank PDF, front matter "Seventh Edition - September 2025" | `SCOPED` | Annex X Tables 1 and 2, paras 4.5 to 4.10, 5.36, 5.41, 5.46, 5.81 to 5.82, 7.17 read. The standstill (10 Business Days) and debriefing (3 and 5 Business Days) text in the engine was correct |
| World Bank consulting RFP | Bank docx, March 2025 revision | `SCOPED` | Form map, Data Sheet ranges and formulas read; the issued RFP controls |
| AfDB procurement framework | Framework page and May 2026 Operations Procurement Manual: HTTP 403 | `NOT_ASSESSED` | A site search listing (secondary) shows Board approval on 14 October 2015 and effect from 1 January 2016; no revision found; not a primary reading |
| UNDP procurement | Supplier page and POPP: HTTP 403 on re-fetch | `SCOPED` (verified 29 October, not re-verified) | A search listing (secondary) shows POPP updates dated 17 and 30 September 2026, which may touch solicitation and evaluation text |
| EU PRAG | Commission page read | `NOT_ASSESSED` | The page states the guide is regularly updated and gives no edition or date; the edition sits behind an EU Login |
| GIZ terms | GIZ PDF front page | `SCOPED` | "Version: 1 September 2025 (Terms and Conditions 2025)"; the 29 October note of an August 2025 status date was wrong and is corrected |
| EU AI Act timing | Commission AI Act Service Desk page | `SCOPED` | General application and Article 50 from 2 August 2026; Article 50(2) marking for earlier systems until 2 December 2026; Annex III from 2 December 2027; Annex I from 2 August 2028. The page does not name the amending act; EUR-Lex returned an empty page to the fetch tool; secondary reports name Regulation (EU) 2026/1744 and were not relied on |
| ISO/IEC 42001 | ISO catalogue page | `SCOPED` | Published, December 2023, stage 60.60, Edition 1. A listing is not evidence of any organisation's conformity |
| Uganda data protection | Not read | `NOT_ASSESSED` | No buyer data map or legal review |
| Model currentness | Codex adapter check only | `NOT_ASSESSED` for a new comparison | The adapter check passes; no official release or catalogue comparison was made for Claude, and no model policy was changed or proposed |

Two engine statements that the checks left unverified, not changed: the 0 to 4
scoring scale in the World Bank skill (the Bank's rated-criteria guidance was not
reachable) and the AfDB shortlist size and weighting figures. Both carry a label.

## Scope limits

- Fixture and routing figures are a lexical proxy over skill descriptions, not measured model behaviour.
- Scanner and gate passes are label, path and content-marker checks. They do not verify claims, authenticity or compliance.
- No bid was prepared, signed, priced or submitted. The synthetic package remains blocked for missing bidder identity, evidence and authority.
