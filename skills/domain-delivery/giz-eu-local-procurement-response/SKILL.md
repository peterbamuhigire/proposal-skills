---
name: giz-eu-local-procurement-response
description: Use when responding to GIZ local procurement, EU/BMZ/GIZ tender packs, AVB/local application requirements, two-zip submissions, GIZ technical grids, self-declarations, price schedules, or GIZ clarification protocols.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# GIZ EU Local Procurement Response
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Overview

Use this skill to make GIZ local procurement failures structurally hard to miss. It turns a GIZ tender pack into a compliance matrix, eligibility verdict, two-envelope submission architecture, page-budgeted concept plan, and rejection-risk register before proposal drafting starts.

This skill is built from the GIZ 7000012724 EU-EAC DEEP tender evidence, but it is reusable for GIZ local tenders with similar application requirements. For 7000012724, remember the decisive constraints: technical 30 percent, personnel 70 percent, 500 technical-point floor, two separate zip folders, no price in the technical bid, two-page concept excluding CVs, CVs of four pages or less, and mandatory eligibility evidence.

## Use When

- The buyer is GIZ, a GIZ-implemented EU/BMZ programme, or the tender pack includes GIZ AVB/local application requirements.
- The pack has a GIZ technical grid, self-declaration, price schedule, two-envelope or two-zip submission rule, or technical threshold.
- You need a bid/no-bid, compliance, submission, or final readiness review for a GIZ tender.

## Do Not Use When

- The tender is World Bank, UNDP, AfDB, PPDA, open commercial, or another donor with its own procurement rules.
- You only need marketing copy, credentials text, or generic methodology prose.
- The tender pack has not been read. Do not infer GIZ rules from memory.

## Required Inputs

| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Complete tender pack, forms, grid, deadlines, and submission rules | Official GIZ procurement channel | required | Stop compliance conclusions and request the missing pack. |
| Proposer eligibility, reference, team, and CV evidence | Authorised proposer records | required for bid decision | Mark criterion unverified; never infer it. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.

1. Build the compliance matrix before writing. Map every mandatory and scored requirement to tender location, evidence owner, document location, status, risk, and sign-off.
2. Run the eligibility knockout scan. Check turnover, staff, sanctions, registration extract age, reference-project value, field relevance, geography, and date window before investing in a full draft.
3. Decide bid, no-bid, or consortium. If a pass/fail minimum is not met, surface the consortium requirement explicitly.
4. Map the two-envelope architecture. Keep technical and financial folders separate. Grep or search the technical bid for prices, rates, budgets, VAT, totals, and currency tokens before submission.
5. Create the technical concept page budget. Allocate scarce space to positively weighted criteria and leave personnel proof to the CV pack where the grid weights it.
6. Protect GIZ templates. Do not alter required forms, self-declarations, or price schedules beyond allowed completion fields.
7. Run sanctions, integrity, and clarification controls. Clarifications go only to the official contact, by deadline, with no side-channel contact.
8. Handoff financial inputs to the spreadsheet/tooling workflow. Confirm net-of-VAT treatment, person-days, fixed budgets, flexible remuneration, and other costs against the price schedule.
9. Run the final rejection-risk scan, then pass the pack to the red-team/QC skill.

## Quality Standards

- The compliance matrix has 100 percent coverage of mandatory and scored items.
- Eligibility is either met, evidenced, or escalated as a no-bid/consortium issue.
- The technical bid contains no price information.
- Page, font, CV, zip, file-size, naming, and template rules are checked mechanically.
- Every proposal claim has evidence or is downgraded to an assumption.

## Anti-Patterns
- Treating a GIZ local tender as a generic donor bid. Fix: map the official application requirements and assessment grid first.
- Starting prose before eligibility review. Fix: complete the knockout scan and bid decision before drafting.
- Allowing price content into the technical folder. Fix: block release and scan the assembled technical archive.
- Restyling a protected form. Fix: edit only fields that the tender permits.
- Hiding scored content outside the page limit. Fix: allocate the page budget to positively weighted criteria.

- Treating a GIZ local tender as a generic donor proposal.
- Starting with prose before the eligibility scan.
- Allowing any price, rate, budget, VAT, or total into the technical folder.
- Editing protected tender templates for style.
- Hiding load-bearing content in links, footnotes, or annexes excluded by page limits.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| GIZ submission control pack | Bid lead, signatory, final checker | Contains complete matrix, eligibility verdict, folder architecture, page budget, clarifications, integrity checks, and rejection-risk sign-off. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Tender-to-file trace and no-price scan | Matrix plus machine/manual check log | Every mandatory and scored item has source, owner, file location, status, and final evidence. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.

Audit and planning default to read-only. Editing forms requires bid authority; sending clarifications or submissions, signing declarations, changing templates, or making consortium commitments requires explicit authorised-person approval.

## Degraded Mode

Without the official tender pack, file inspection, archive inspection, or search capability, return only a qualified checklist and mark the affected tests not assessed. Never infer that a technical folder is price-free.

## Decision Rules

| Finding | Action | Risk avoided |
|---|---|---|
| Pass/fail evidence is missing | No-bid, obtain evidence, or assess consortium before drafting | Knockout after bid effort |
| Price token appears in technical files | Block release and remove it at source | Envelope rejection |
| Tender wording is ambiguous | Log and submit official clarification by deadline | Side-channel or guessed interpretation |

## Worked Example

For a two-zip GIZ bid, map every grid item to its file and owner, scan the technical archive for rates and currency tokens, verify protected forms and CV limits, then release only after signatory evidence closes all knockout items.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.

- [references/giz-compliance-matrix.md](references/giz-compliance-matrix.md): Matrix fields, knockout tests, and scoring alignment.
- [references/submission-pack-checklist.md](references/submission-pack-checklist.md): Two-zip, no-price, page-limit, CV, template, and final submission controls.
