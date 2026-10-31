# Weighted page budget and bid-data-sheet compliance matrix

Parent skill: [Approach and Methodology](../SKILL.md).

Use this when a solicitation caps pages, words or files, weights its evaluation
criteria, or states its rules in a Bid Data Sheet or Data Sheet. It applies to every
framework: PPDA bidding documents, World Bank RFPs, AfDB, UNDP and GIZ packs.

## Precedence

The section skills give default lengths for briefs that set no cap (for example one
to two pages for understanding, five to ten for methodology). A solicitation's caps,
weights and exclusions override those defaults. The longest section is the one whose
criterion carries the most points, not the one a skill happens to name. If the cap or
the weights are not stated, record the gap and ask; do not infer a cap from a template.

## Step 1: extract the rules into a matrix

Build the matrix before drafting. One row per requirement; copy the solicitation's
words or paraphrase tightly and cite the clause, form or page.

| Field | What to record |
|---|---|
| ID | Stable reference, for example C-014 |
| Source | Clause, Data Sheet entry, form or page where the requirement appears |
| Requirement | Verbatim or tight paraphrase |
| Class | Eligibility, administrative (pass or fail), rated technical, submission, financial, contractual |
| Points or gate | Points and any floor, or pass/fail |
| Response location | File, section and page where the answer sits |
| Evidence | Document, form, CV entry, certificate or calculation that proves it |
| Owner | One accountable person |
| Status | Open, partial, covered, blocked, not applicable |
| Risk | Knockout, major, minor |
| Reviewer and date | Who checked the response against the source, and when |

Rows the Data Sheet usually forces you to answer, whatever the framework: selection
method and evaluation stages; envelope structure (single, two-envelope or two-stage);
delivery channel and copies; markings; deadline and time zone; bid or proposal
validity; any bid security or securing declaration; performance security; currency
and tax basis; language; who must sign and with what authority; price-schedule form;
rules for joint ventures and subcontractors; the page, word or file caps and what
they exclude (forms, CVs, annexes); the minimum technical score. If a row cannot be
filled from the issued document, mark it `NOT_ASSESSED` with an owner.

For a World Bank RFP take the form list, selection method, proposal type and page
limits from the Data Sheet and the form checklist, and use the
[form guide](../../../profiles-sectors/sectors/world-bank/references/tech-fin-forms-guide.md).
For a PPDA bid take the submission method, channel and securities from the BDS and
check them against the [PPDA submission table](../../../profiles-sectors/sectors/ppda-uganda/SKILL.md).

## Step 2: turn weights and caps into a page budget

1. List every scored criterion with its points. A criterion judged on the whole
   document (presentation or clarity) takes no pages of its own: mark it embedded and
   write the whole document to that standard.
2. Note what the solicitation excludes from the cap. CVs, forms and annexes count
   against the cap only if the solicitation says so. Proof that sits outside the cap
   can carry part of a criterion; say so in the matrix rather than hoping an
   evaluator looks.
3. Set a floor for any criterion with a minimum score, a sub-threshold, or a
   knockout test. A floor is the least space in which the claim can be evidenced.
4. Divide the cap in proportion to points, round to the unit you can lay out
   (quarter pages work), and apply floors. The proportional split is a starting
   point. It is arithmetic, not a forecast of what evaluators will award.
5. Move pages only for a stated reason: a criterion whose proof is outside the cap,
   a criterion that is weak and cheap to strengthen, or one that needs a figure.
6. Check the result with `scripts/page_budget_check.py`. It refuses an allocation that
   exceeds the cap, gives a weighted criterion no pages, misses a floor, or gives a
   lower-weighted criterion more pages than a higher-weighted one without a stated
   reason.
7. Draft to the budget, render, and count the real pages. A budget that was never
   rendered is not evidence.

### Worked example (fictional)

The brief: a six-page narrative, with forms and CVs outside the cap. Weights:
methodology 30, key experts 25, national participation and knowledge transfer 25
(unusually high), data protection and continuity 15, presentation 5. Floors: 1.0,
1.0, 1.25 (the criterion has a sub-threshold), 0.75. CV proof sits outside the cap.

`python -X utf8 scripts/page_budget_check.py tests/fixtures/page-budget-example.json --propose`

| Criterion | Points | Share of points | Pages | Share of pages |
|---|---:|---:|---:|---:|
| Methodology | 30 | 31.6% | 2.0 | 33.3% |
| Key experts | 25 | 26.3% | 1.5 | 25.0% |
| National participation and knowledge transfer | 25 | 26.3% | 1.5 | 25.0% |
| Data protection and continuity | 15 | 15.8% | 1.0 | 16.7% |
| Presentation | 5 | embedded | 0 | embedded |

Presentation is embedded, so the other four criteria share the six pages over 95
points. An allocation that follows the old "methodology is the longest section" habit
(five pages of methodology, then 0.25, 0.25 and 0.5 pages for the other three) fails
the check: three floors are missed and the 25-point national-participation criterion
gets 4% of the pages.

## Step 3: cut in the right order

When the draft is over the cap, cut in this order and stop when it fits:

1. Restatement of the brief the evaluator already has.
2. Firm background that does not serve a scored criterion.
3. Generic method language, then repeated claims.
4. Figures that duplicate a table.

Never cut the evidence that earns a floor, a mandatory form, or a statement the
matrix marks as a knockout test.

## Checks before release

- Every matrix row has a response location, an owner and a reviewed status.
- No scored content sits only in an annex that the solicitation excludes from
  evaluation, a footnote, or a link.
- Rendered page, word or file counts are measured and recorded against each cap.
- The envelope and channel rows agree with the submission pack, and no price appears
  where the pack must stay technical. For a two-envelope pack described by a
  `validator-input.json`, run `python -X utf8 scripts/proposal_fixture_check.py --input <package>/validator-input.json --check-content`; it scans text and `.docx` files and treats other file types as `NOT_ASSESSED`.
- Anything the solicitation leaves open is a clarification question, logged with its
  date, not an assumption.
