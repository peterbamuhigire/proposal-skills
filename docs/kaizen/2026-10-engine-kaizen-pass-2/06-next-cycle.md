# Next cycle: proposal engine

Owner: Peter Bamuhigire. Re-audit: **30 November 2026**, which is also the review
date of every volatile record in the source register, or before a live bid,
whichever comes first. After that date `validate_skills.py` fails on purpose until
the register is renewed.

## Open findings

- **P1: a real, authorised, redacted solicitation and bidder evidence pack.** Run the
  whole path once on it: compliance matrix, page budget, forms, `--check-content`
  scan on the rendered pack, deadline, signatures and release manifest. This is the
  inherited September P1 and it is still open. No authorised document exists.
- **P1: PPDA e-GP mandate.** Retrieve the body of PPDA's press statement of
  5 June 2026 ("Uganda to Roll Out E-GP to all Entities on 1st July 2026") from the
  PPDA site by hand; the automated fetch returned only the title. Record which
  entities require electronic submission and from when, then update the PPDA skill's
  channel paragraph and the register row `PPDA-EGP`.
- **P1: PPDA guidelines and thresholds.** Read the current guidelines under the Rules
  and Methods Regulations 2023 (reg 23(1) micro procurement, reg 63(2) bid security
  amounts, Contracts reg 11(2) performance security value). Replace the unverified
  UGX figures in `ppda-act-and-regulatory-framework.md` or keep them labelled.
- **P1: AfDB, UNDP, PRAG.** The AfDB framework page and the May 2026 Operations
  Procurement Manual, the UNDP supplier page and POPP, and the PRAG edition all
  refused automated fetch (HTTP 403, or an EU Login). Ask Peter for the documents or
  fetch them by hand, then check the AfDB minimum-score and weighting figures, the
  AfDB shortlist size and form list, and UNDP's September 2026 POPP updates
  (solicitation and evaluation text).
- **P2: 0 to 4 scoring scale and "score 2 is the minimum to be competitive"** in
  `world-bank/SKILL.md`. The Bank's rated-criteria guidance was unreachable. Verify or
  restate as a heuristic.
- **P2: fixture coverage.** 111 of 115 skills still lack three positives and two
  owned negatives. The harness is lexical; a model-judged routing run needs Peter's
  authorisation.
- **P2: reviewer rework and routing collisions from real use**, and assistive-technology
  reading order on a completed form. No data or tool.
- **P2: the agent-integration contract test** (`tests/agent-integration/`) is a
  standalone script outside unittest discovery and CI, and finds the sibling
  `chwezi-engine-agents` catalogue through `ROOT.parent` (line 28). Wire it into CI
  and let `CHWEZI_ENGINES_ROOT` override the sibling root.
- **Data-protection claims in technology bids** stay `NOT_ASSESSED` until a buyer data
  map and legal review exist.

## Decisions needed from Peter

1. About twenty historical machine-path lines remain in dated records
   (`docs/audits/`, `docs/continuous-improvement/`, `docs/engine-upgrade-july-2026/`,
   `docs/dual-compatibility-report.md`). The gate exempts them as history. Sanitise
   them, or accept them as records?
2. Should the PPDA `Performance Securing Declaration` form text ("three years") be
   traced to a regulation or PPDA guideline? The Act leaves the period to the Authority
   (section 128), so the skill now says the form states it.

## Cross-engine boundaries (no sibling engine was edited)

Resolve these through the catalogue.

- Proposal `skills/pipeline/06-methodology/references/technical-approach-figures.md`
  and SRS `scripts/render_diagrams.py`: the render handoff is still unproven by an
  attached artefact. Mark it `NOT_ASSESSED` until a rendered figure and its
  validation result are attached.
- Proposal `skills/pipeline/10-financial-proposal/SKILL.md` and Business Plan
  `AGENTS.md`: narrative pricing must not be treated as a reconciled financial model.
  Carry over from 29 October.
- Proposal `AGENTS.md` design trigger and Design `doctrine/design-doctrine.md`: no
  mismatch found this cycle. Receiving templates must preserve approved fonts.
- Proposal `docs/source-registers/2026-10-currentness.json` and Research
  `docs/continuous-improvement/kaizen-currentness-gate.md`: the local gate checks
  metadata only. The new register rules (no verified date on a `NOT_ASSESSED` row; a
  review window of 45 days for volatile claims) are stricter than the gate text. If
  Research wants them portfolio-wide, they are the proposal engine's proposal for
  that cycle. The Research checkout's `AGENTS.md` changed on disk during this cycle
  from another session; it was not touched.
- Proposal `skills/profiles-sectors/sectors/ppda-uganda/references/local-government-procurement.md`
  (line 54) and `ngo-and-donor-procurement.md` (line 80) cite Accounting Doctrine
  `doctrine/references/uganda-public-sector-pfm.md`,
  `doctrine/references/uganda-ngo-financial-management-patterns.md` and two skills
  there. All four paths resolve today. If the accounting engine restates the
  Secretary to the Treasury's 30% advance approval, check it against Contracts
  Regulations reg 43(4), which this cycle read.

## One small experiment for next time

Link each regulation citation in the PPDA and World Bank skills to a register record
and test it. Pilot on those two skills: a test lists every "reg N" and "para N"
citation in the skill text and fails when the cited instrument has no register row or
the row is `NOT_ASSESSED`. Measure: uncited rules before and after. Keep only if it
finds a real gap without needing a list of exceptions.

No public plugin-directory acceptance, live tender submission or model-judged routing
result is claimed.
