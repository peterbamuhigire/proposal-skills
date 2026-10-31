# Proposal engine kaizen, pass 2: final report

The target of 95 is not achieved. The cycle found one critical defect that the
29 October work had left behind (the stale World Bank form map survived in the
skill the router loads first) and fixed it, together with five major content
defects that the primary sources contradicted, and added the checks that stop each
class returning. Scores are reviewer judgements (inference), not bid-win
probabilities, and no real bid was prepared.

Branches: the repository started on `main` at `9089c0a` with a clean tree. All work
is on `kaizen/2026-10-pass2` (10 commits: one baseline, eight items, one report)
and is not merged, pushed or tagged. `main` was checked out again at the end.

## Scores by dimension

Raw is the mean of the ten dimensions. Published is `min(raw, 65)`. The baseline was
frozen at `7ece7c0` before any change. It is lower than the 29 October final because
it inspected the parent skills and primary sources that the October cycle did not
read; nothing was changed between the two measurements.

| Dimension | 29 Oct final | Pass 2 baseline | Pass 2 final | Evidence and remaining deficiency |
|---|---:|---:|---:|---|
| Doctrine | 70 | 70 | 72 | Router and `AGENTS.md` now say the solicitation's caps and weights override default section lengths. Authority for real bids is still absent |
| Taxonomy and routing | 55 | 50 | 56 | Precision@1 23/31 to 32/41; four skills with three positives and two owned negatives (was one); 111 skills still lack them; lexical proxy only |
| Skill depth | 65 | 55 | 66 | World Bank skill, scoring guide and PPDA skill agree with the RFP and Regulations; AfDB and UNDP depth unverified |
| Applied proof | 50 | 50 | 56 | 54 new tests with red evidence for each fix; envelope content scan on the sanitised example; still synthetic, no evaluator |
| Standards currency | 50 | 45 | 58 | 14 records, 10 `SCOPED`, 4 `NOT_ASSESSED`, gate against mislabels; AfDB, PRAG, thresholds and data protection open |
| Output readiness | 60 | 55 | 62 | The BDS matrix, envelope decision and page budget can now be produced from the engine; credentials and signatures absent |
| Accessibility and inclusion | 40 | 40 | 40 | Unchanged; no assistive-technology run (`NOT_ASSESSED`) |
| Production and handoff | 55 | 55 | 58 | CI widened from 2 to 6 commands (not run here); content scan and page-budget tools; no submission receipt |
| Hygiene | 75 | 70 | 78 | Six machine-path lines removed and gated; about twenty remain in exempt dated records |
| Safety and integrity | 65 | 55 | 68 | Stale labels and incorrect legal requirements fixed and guarded; unverified AfDB and 0 to 4 scale labelled |

**Raw 54.5 to 61.4.** Published: `min(54.5, 65) = 54.5` at baseline,
`min(61.4, 65) = 61.4` at the end. The 29 October final was raw 58.5, published 58.5.
Every dimension is equal or better than both earlier measurements. Any
missing mandatory live-bid requirement remains a release blocker whatever the score.

## Critical and major defects

| ID | Severity | Disposition |
|---|---|---|
| D1 | Critical | Fixed and verified in `6efc922`: the form table, headings and the FIN-5 promise corrected; scanner red (12 findings) then green; independent extraction of the RFP checklist agrees on all 12 form ids |
| D2, D3 | Major | Fixed in `6efc922` and `3db28f3`; ranges and formula now trace to the Regulations Annex X and the RFP Data Sheet |
| D4 | Major | Fixed in `a8cac10` against the 2023 Regulations; the e-GP mandate scope stays `NOT_ASSESSED` |
| D5, D6 | Major | Fixed in `aa49a51`: precedence rule, reference, checker |
| D7 | Major | Fixed in `7ad4f13`; the baseline undercounted it (3 lines in 2 files; actual 6 lines in 5 files), recorded in the experiment log |
| D8 | Major | Fixed in `00ef43d` for packages that can be scanned; the live-package part stays open |
| D9, D10 | Minor | Fixed in `635e76a` |

## Kept changes

| Commit | Item | Evidence |
|---|---|---|
| `6efc922` | P0-1 form labels fixed and gated | 12 findings to 0; 9 tests; cross-check against the downloaded RFP |
| `3db28f3` | P0-2 World Bank numbers from primary sources | 9 retired phrases removed; 3 tests; worked example recomputed |
| `a8cac10` | P0-3 PPDA envelope, securities, channel | 3 retired claims removed; regulation citations; 4 tests |
| `aa49a51` | P1-4 weighted page budget and matrix | Script, reference, router rule; 13 tests; old allocation fails |
| `7ad4f13` | P1-5 machine paths and CI | 6 lines to 0; gate rule with 4 tests; CI runs 6 commands |
| `00ef43d` | P1-6 envelope content scan | Planted price: old PASS, new FAIL; 13 tests |
| `635e76a` | P1-7 routing wording and fixtures | Original 31: first-rank 23 to 24; 41: 32, owned negatives 7 of 7 |
| `affb97f` | P1-8 register and register gate | 11 to 14 records; 4 new negatives |

Reverted: none. Each item was followed by the registered checks and the suite; see
[the experiment log](03-experiment-log.md) and [the validation record](04-validation-record.md).

## Residual risk

- No real solicitation, bidder evidence, evaluator or submission receipt exists. The
  new tools prove mechanics on fictional data only.
- The PPDA regulations were read selectively (eight regulations); guidelines,
  circulars, monetary thresholds and the e-GP mandate scope are not assessed.
- AfDB, UNDP (not re-verified), PRAG and Uganda data-protection claims remain
  unverified; the skills label the AfDB figures and the 0 to 4 scale.
- Routing figures come from a lexical proxy over descriptions, not from a model.
- The World Bank `Standard RFP` map is a March 2025 version; a customised or older
  RFP may differ, and the skill says the issued RFP controls.
