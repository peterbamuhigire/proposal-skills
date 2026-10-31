# Pass 2 improvement backlog

Owner: Peter Bamuhigire. Review date for every item: 5 November 2026 (the
re-audit date in `06-next-cycle.md`). Target: 95/100; the table shows each item's
intended contribution to the mean of the ten dimensions, as an estimate to be
confirmed in `05-final-report.md`, not a claim. Eight items are selected (limit ten).
The critical defect D1 and the inherited open P1 are both in the selection.

## Five Whys for the repeated or critical defects

**D1 and D2: stale World Bank form labels in the parent skill.**
1. Why does `world-bank/SKILL.md` still teach TECH-5 as team composition? The 29 October fix edited `references/tech-fin-forms-guide.md` only.
2. Why only the reference? The defect was found in the reference, and the regression test (`tests/test_world_bank_forms.py`) opens only that file.
3. Why did nothing flag the parent? The form map exists as prose in four places (parent skill, scoring guide, AfDB comparison table, reference); no single source feeds them.
4. Why did validators pass? They check skill structure and routing, not the meaning of a form label.
5. Root cause (tooling and proof): the guard covered a file, not the claim. Fix the claim wherever it appears and scan every skill for it.

**D3 and D4: unsupported "typical" numbers and a PPDA text that contradicts the Regulations.**
1. Why does the skill say "typically 75" and "bid securing declaration included"? Both were summarised from guide-level documents and a quotation-method form.
2. Why were they not checked against the instrument? The 29 October register recorded the Regulations as `NOT_ASSESSED` and nothing forced a check before a skill stated a rule.
3. Why did the skill keep stating it? No link exists between a numeric or legal claim in a skill and a register record.
4. Why no link? The register was built as a separate file of selected claims, not as a gate on skill prose.
5. Root cause (reference and process): rules were written from secondary summaries. Correct each rule against the primary text, cite the instrument and paragraph, and record the date.

**D5 and D6: tight-cap tasks cannot be completed.**
1. Why can the engine not answer Task 3? Section skills prescribe fixed lengths.
2. Why fixed? They were written for uncapped consulting briefs.
3. Why no override? Only the GIZ skill mentions weight-driven allocation, in two sentences.
4. Why was that not generalised? No fixture or task exercised a capped, weighted brief.
5. Root cause (skill and proof): a missing method plus a missing check. Add the method as a reference, a precedence rule in the router, and a deterministic checker.

**D7: machine paths in shipped content.**
1. Why does a skill carry a Windows drive-letter path? A pointer stub copied the author's local path next to the GitHub link.
2. Why did the gate pass? `encoding_link_gate.py` matched one earlier, narrow pattern for two sibling-checkout routes and nothing else.
3. Why so narrow? It was written for one earlier incident (stale sibling routes).
4. Why no wider rule? The cycle's guardrail ("no machine-specific paths") was checked by hand.
5. Root cause (tooling): a hand check never became a validator.

**D8: envelope separation checked by file name only.**
1. Why can a technical file contain a price and still pass? The checker reads declared paths, not content.
2. Why? It was built to validate a fixture's structure, with no real files behind it.
3. Why was the content scan manual on 29 October? The files were rendered outside the repository.
4. Why no automation? The next-cycle note named the live package as the gap, not the scan.
5. Root cause (tooling): add an optional content scan so a real package can be checked the day one exists.

## Backlog

| ID / priority | Gap | Root cause | Exact change | Hypothesis | Acceptance evidence | Risk and rollback | Target contribution |
|---|---|---|---|---|---|---|---|
| P0-1 | D1, D2: stale TECH-5 to TECH-8 and FIN-5 in `world-bank/SKILL.md`, `evaluation-scoring-guide.md`, `afdb/SKILL.md` | Guard covered one file | Correct the form table and headings to the March 2025 map; remove FIN-5; add `scripts/check_form_labels.py` (scans every active skill; negation-aware) wired into `validate_skills.py`, with positive and negative unit tests | The router-loaded skill and its reference agree, and any future stale label fails validation | Scanner fails on the pre-fix tree (red), passes after (green); six registered commands exit 0; unit tests include a stale-line negative | Content-only plus one validator; revert the single commit. Risk: a negation-heuristic false negative, recorded in the log | Skill depth +10, Safety +10 |
| P0-2 | D3: universal "typical" numbers (pass mark 75, firm experience 10 to 20, methodology 30 to 50, weights, score spreads) | Rules from secondary summaries | Replace with the Regulations Seventh Edition Annex X ranges (Tables 1 and 2, para 4.5), stating the RFP Data Sheet sets the number; remove unsourced spread figures; relabel the AfDB figure as unverified | Bidders allocate effort from the issued criteria, not a remembered norm | Each changed number traces to a paragraph in the source read on 31 October 2026; grep shows no "typically 75" | Content-only; revert. Risk: over-narrowing guidance that helps; mitigated by keeping the strategy statements that do not depend on a number | Skill depth +3, Standards currency +10, Safety +3 |
| P0-3 | D4: PPDA envelope, bid-security, performance-security and channel guidance | Rules from a quotation-method form | Add a "bid submission and securities" decision table to `ppda-uganda/SKILL.md` citing regulations 66, 63, 68 (Rules and Methods) and 48 (Consultancy) and regulation 11 (Contracts); correct line 156 and lines 239 to 244; note the e-GP press statement with scope `NOT_ASSESSED`; correct the reference's "replaces bank guarantee" wording | A bidder builds the correct envelope structure and securities for the method named in the BDS | Each rule traced to a regulation paragraph read on 31 October 2026; routing and structure validators pass | Content-only; revert. Risk: a regulation amended after the 2026-03 upload; mitigated by dated citation and "BDS controls" | Skill depth +5, Output readiness +5, Safety +5 |
| P1-4 | D5, D6: no method for weight-driven page budgets or a BDS compliance matrix | Skills written for uncapped briefs | New reference `06-methodology/references/weighted-page-budget-and-compliance-matrix.md`; precedence rule in `skills/SKILL.md` decision rules; fix `06-methodology` "longest section" line; pointers from the four framework skills; deterministic `scripts/page_budget_check.py` with tests | A six-page cap with a 25-point criterion yields a defensible allocation and a failing check when a weighted criterion is starved | Worked example re-computed by the script; negative tests (starved criterion, over-cap total, missing floor); validators pass | Additive plus two small edits; revert. Risk: script mistaken for scoring prediction; the reference states it is allocation arithmetic only | Output readiness +10, Applied proof +5 |
| P1-5 | D7: machine-specific paths ship in a skill and an active standard; gate has a false negative | Hand check, narrow regex | Replace the three paths with catalogue wording; extend `encoding_link_gate.py` to flag drive-letter and home-directory paths in active content (skills, templates, rules, prompts, router, authoring standard), exempting dated evidence folders; tests | New shipped paths fail the gate | Gate flags the pre-fix tree (3 lines), passes after; negative test with a planted path | Revert the commit. Risk: exempt list too wide; listed explicitly | Hygiene +10 |
| P1-6 | D8 and inherited open P1: envelope content never scanned | Checker built for structure | `--check-content` option in `proposal_fixture_check.py`: scan text and `.docx` files in each envelope for the other envelope's markers (from the fixture, with defaults); tests with a planted price in the technical file and a planted TECH marker in the financial file | A leaked price or form fails before submission | Planted leaks fail; clean fixture passes; default run unchanged | Opt-in flag, so the registered command behaves as before; revert. Does not close the live-package gap | Applied proof +5, Production +5 |
| P1-7 | D9, D10 and inherited P2: weak routing for the touched skills | Sparse fixtures; descriptions miss the bidder's words | Add "open domestic bidding" and "bid data sheet" to `ppda-uganda`; add one discriminating World Bank proposal-type term; add fixtures so `ppda-uganda`, `afdb` and `06-methodology` reach three positives and two owned negatives; retest every original fixture | Precision@1 rises; no owned negative moves | `routing_smoke_test.py` before and after: precision@1 not lower, top-three 100%, owned negatives all pass | Metadata-only plus fixtures; revert. Keep a description change only if the original 31 fixtures hold | Taxonomy +10, Applied proof +3 |
| P1-8 | Standards currency: register lacks the claims verified this cycle; no rule links status to dates | Register built once | Add records for the PPDA Act, 2023 Regulations, e-GP statement, World Bank Regulations and RFP, AI Act timing, ISO/IEC 42001; move review dates; extend `check_source_currency.py` so `SCOPED` needs a verified date and `NOT_ASSESSED` must not carry one; tests | Overstated verification becomes a validator failure | Register validator and unit tests pass; negative tests for both mislabels | Additive; revert. Verification dates only where a primary source was read | Standards currency +10 |

## Deferred to `06-next-cycle.md` (structural or needs data that does not exist)

- Redacted real solicitation and bidder evidence pack (P1, inherited): no authorised document.
- Reviewer-rework and real routing-collision measurement (P2, inherited): no real-use data.
- Assistive-technology reading-order run on a completed form: no tool available without installing packages.
- AfDB, UNDP POPP and PRAG current-version proof: pages returned HTTP 403 to automated fetch.
- The `Scoring Scale` 0 to 4 and "score 2 is the minimum to be competitive" text in `world-bank/SKILL.md`: the Bank guidance it cites was not reachable; recorded as unverified, not changed.
