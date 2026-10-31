# Pass 2 experiment log: 31 October 2026

Eight items ran one at a time, highest priority first. After each change the
registered checks and the unit suite were re-run before the commit. Each item
below states what was measured before the change, what was measured after, and the
decision. None was reverted.

Baseline commit `7ece7c0` (evidence only). Starting code `9089c0a`.

## P0-1: stale World Bank form labels (commit `6efc922`)

Hypothesis: if the form map is corrected wherever it appears and a scanner checks
every active skill for the retired pairings, the router-loaded skill and its
reference agree and the defect cannot return unnoticed.

Red first. `scripts/check_form_labels.py` was written before any content change and
run on the unfixed tree: 12 findings on 8 lines in three files (`world-bank/SKILL.md`
152, 154, 155, 251, 320; `evaluation-scoring-guide.md` 130, 142; `afdb/SKILL.md` 230).
The 29 October reference (`tech-fin-forms-guide.md`) produced none.

Change: the form table and headings in the three files now follow the March 2025
RFP; FIN-5 is removed; the AfDB comparison row says the AfDB form list comes from the
issued RFP. The scanner is wired into `validate_skills.py`.

After: scanner 0 findings. Independent check, not derived from the fixture: the
form checklist was extracted from the downloaded RFP text and compared with the
fixture map and with the parent skill's table. All 12 form ids agree. Nine unit
tests cover retired rows, retired headings and ranges, current labels, a warning
paragraph, a table row inside a warning paragraph, a planted label in a temporary
skill tree and a missing rules file.

Known limit, recorded in the script: a paragraph that carries a recorded warning
phrase is exempt as a whole, so a stale label hidden in such a paragraph would pass.
Table rows are never exempted that way. Decision: keep.

## P0-2: unsourced World Bank scoring norms (commit `3db28f3`)

Hypothesis: replacing remembered "typical" figures with the ranges in the
Regulations and the RFP Data Sheet stops bidders from allocating effort by a norm
that is not in the issued documents.

Sources read on 31 October 2026: Regulations Seventh Edition (September 2025),
Annex X Tables 1 and 2 and paras 4.5 to 4.10, paras 5.36, 5.41, 5.46, 5.81 to 5.82,
7.17; the March 2025 RFP Data Sheet. Corrections: pass mark "typically 75" to "set in
the Data Sheet, indicative 70 to 85"; firm experience 10 to 20 to 0 to 10;
methodology 30 to 50 to 20 to 50; key-expert sub-weights 20-30 / 50-60 / 10-20 to
10-20 / 60-80 / 0-10; shortlist "3 to 6" to "5 to 8" (para 7.17); the scoring guide's
normalisation to the best proposal to the Data Sheet formula `S = St x T% + Sf x P%`;
invented spreads ("5-8 points", "30-40 points") replaced by arithmetic from the
weights (at 80/20 a 20% price premium costs 3.33 combined points, recovered by a
4.17-point technical lead; at 60/40, 6.67 and 11.11). The worked example in the
scoring guide was recomputed, not edited by hand.

Before: seven retired phrases found in the old `SKILL.md`, two in the old guide.
After: none. Three tests check the stated ranges against the fixture and refuse the
retired phrases. Two claims were deliberately not changed and labelled unverified:
the 0 to 4 scale (the Bank's rated-criteria guidance was unreachable) and the
AfDB figures (AfDB pages returned HTTP 403). Decision: keep.

## P0-3: PPDA envelope, security and channel guidance (commit `a8cac10`)

Hypothesis: a method, channel and securities table with regulation citations lets a
bidder build the correct pack for the method the BDS names.

Sources read: Cap. 205 Act, 2023 Rules and Methods Regulations (regs 63, 66, 68),
Consultancy Services Regulations (regs 47, 48, 62), Contracts Regulations (regs 11,
43). Before: the skill said every QCBS, QBS, LCS or FBS bid uses two envelopes (true
for consultancy, absent for supplies, works and non-consultancy), that a securing
declaration is always included (reg 63(1) leaves it to the bidding document), and
that PPDA uses a performance securing declaration instead of guarantees (reg 11(1)
allows either). After: the table covers single envelope as the default for supplies,
works and non-consultancy, the IT-systems option for two envelopes or two stages,
channel including electronic delivery, and the four securities, each with its
regulation. The e-GP press statement is cited by title and date only. Four tests
check the anchors and refuse the retired claims; the retired claims were present in
the old text. Decision: keep.

Not done: the micro-procurement limits (UGX 5M and 10M) could not be traced to a
regulation; they sit in PPDA guidelines. That was labelled unverified in P1-8.

## P1-4: weighted page budget and compliance matrix (commit `aa49a51`)

Hypothesis: a precedence rule, a method and a checker let the engine complete a
capped, weighted brief and refuse an allocation that starves a weighted criterion.

Before: the section skills' default lengths sum to at least 9.5 pages for a
six-page cap, and `06-methodology` said its section "should be the longest". After:
reference, router rule, `AGENTS.md` route, corrected methodology line, pointers from
four framework skills, and `scripts/page_budget_check.py`. The hand calculation for
the fictional brief (1.89, 1.58, 1.58, 0.95 pages over 95 live points, presentation
embedded) rounds to 2.0, 1.5, 1.5, 1.0; the script returns the same. The old
"methodology is longest" allocation (5 / 0.25 / 0.25 / 0.5) fails the script with
three floors missed. 13 tests. The script is allocation arithmetic only and says so.
Decision: keep.

## P1-5: machine-specific paths (commit `7ad4f13`)

Hypothesis: a rule in the link gate catches what the hand check caught, and removing
the paths makes shipped content portable.

Baseline correction: the frozen baseline counted three lines in two files. A Python
census then found six lines in five shipped files (`CONTRIBUTING.md` 20 and 26,
`docs/skill-authoring-standard.md` 3 and 50, `skills/meta/skill-writing/SKILL.md`
13, the example submission manifest 19) plus a `.gitignore` comment. The first
census used a regular expression that mishandled backslashes; the baseline was left
as frozen and the miscount is recorded here. Red: the extended gate reported exactly
those six lines and no false positive on URLs. After: 0. The rule exempts dated
records, `scripts/` and `tests/` (see the gate's `RECORD_PREFIXES`); about twenty
historical lines remain in those records. CI previously ran two of the registered
checks; the workflow now runs five checks plus the unit suite (not executed here:
no runner; the same commands pass locally and the YAML parses). Four tests. Decision:
keep.

## P1-6: envelope content scan (commit `00ef43d`)

Hypothesis: scanning file content, not names, catches a price in the technical file.

Red: a planted line "UGX 45,000,000" appended to the sanitised example's technical
file returned `PASS` from the previous checker (run from `HEAD` before the change).
After: the new `--check-content` option returns `FAIL` with the file, line and marker.
Text and `.docx` (body, headers, footers, footnotes) are read; other types are
`NOT_ASSESSED` unless accepted; oversized documents are refused. The registered
default run is unchanged. 13 tests. Decision: keep. A hook blocked a recursive
forced `rm` of a scratch directory while preparing this probe; it was not overridden
and a new directory name was used instead.

## P1-7: routing wording and fixtures (commit `635e76a`)

Hypothesis: adding the bidder's words to four descriptions raises first-rank
accuracy without moving any owned negative.

Measured with the repository harness (a lexical proxy; no model was called). Original
31 fixtures: first-rank 23 to 24, top three 31 to 31, owned negatives 2 to 2. Ten new
fixtures: first-rank 5 of 10 before the description edits, 8 of 10 after, top three
9 of 10 to 10 of 10. Expanded set of 41: first-rank 32 (78.0%), top three 41 of 41,
owned negatives 7 of 7. The three Step 1 prompts now rank `ppda-uganda`,
`world-bank` and `06-methodology` first. Skills with three positives and two owned
negatives: 1 to 4. Fixture floor 26 to 41. Four tests keep the census and the
live-skill references honest. Decision: keep.

## P1-8: register and register gate (commit `affb97f`)

Hypothesis: recording verification dates only where a primary source was read, and
refusing mislabelled rows, makes overstated currency a validator failure.

Register: 11 to 14 records (10 `SCOPED`, 4 `NOT_ASSESSED`). The GIZ record is
corrected to "Version: 1 September 2025". The gate now refuses a `NOT_ASSESSED` row
with a verified date, a non-https URL, an unknown freshness class, and a volatile
review date more than 45 days after verification. Seven tests, three of them new
negatives. All volatile reviews fall on 30 November 2026. Decision: keep.

## Not selected

Accessibility and inclusion stay at 40: no assistive-technology tool is available
without installing packages, and no accessibility claim was made. Real-bid proof
needs an authorised redacted solicitation.
