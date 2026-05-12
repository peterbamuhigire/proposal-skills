# Print Fidelity

Print is a P0 deliverable in Chwezi finance / accounting products. Uganda audits run on printed evidence. Donor audits run on printed evidence. Tax authority filings run on printed evidence or PDF equivalents. A screen that looks great in the browser and prints as a black rectangle is a failure.

## Rule

Every report, evidence pack, return-ready pack, financial statement, management pack, journal listing, GL detail, trial balance, AR / AP ageing, inventory valuation, fixed-asset register, payroll register, bank reconciliation, mobile-money reconciliation, and audit export has a print stylesheet that produces correct output on A4, black-and-white, with auditor sign-off boxes.

## Print stylesheet requirements

| Requirement | Detail |
|---|---|
| Page size | A4 default; US Letter as overlay per country extension. |
| Margins | 15 mm top and bottom; 18 mm left and right. |
| Header on every page | Entity name, report title, period, framework, page X of Y. |
| Footer on every page | Generated-at timestamp, generator identity, preparer, reviewer, document reference. |
| Body | Tabular numerals, decimal-aligned money columns, monochrome-readable status chips (with text label, never colour-only). |
| Colour usage | Pure black-and-white as the canonical print mode. Optional colour print supported but never required to convey meaning. |
| Charts | Use patterns / hatching in addition to colour so charts remain readable in monochrome. |
| Status chips | Always include the status word; never rely on colour. |
| Money triplet | Net / tax / gross preserved as separate columns in printed VAT reports and invoices. |
| Sign-off boxes | Preparer / Reviewer / Approver named boxes at the bottom of every audit-relevant report. |
| Stamp area | An empty 60 × 60 mm area on the cover of every audit-relevant report for the company stamp. |
| Page breaks | Avoid orphan totals rows. Keep section headings with their first row. Repeat column headers on every page of a multi-page table. |
| Watermark | `DRAFT` watermark when the report is generated before reviewer sign-off. Removed when status reaches `released`. |

## Required printable artefacts

1. Trial balance (summary and detail variants).
2. General ledger detail by account.
3. Journal listing by period.
4. SFP / SOCI / SCE / SCF as per `chart-of-accounts.md` statement-group taxonomy.
5. AR ageing, AP ageing.
6. Inventory valuation by item and by location.
7. Fixed-asset register and depreciation schedule.
8. Payroll register by period and by employee.
9. Bank reconciliation by account by period.
10. Mobile-money reconciliation by provider by account by period.
11. POS Z-report close pack.
12. Cash-drawer close pack.
13. VAT return pack with source-transaction listing.
14. PAYE return pack with employee schedule.
15. WHT return pack with certificate listing.
16. NSSF return pack with employee schedule.
17. Management accounts pack with variance commentary.
18. Donor / grant utilisation pack where applicable.
19. Audit-ready export index with cross-references.
20. Migration cutover pack.

## Implementation expectations

- A shared `print.css` (or framework equivalent) ships in the design system token bundle.
- Each report page has a `@media print` rule set tested in real print preview.
- Print testing is part of the CI for any UI repository that consumes the finance design tokens.
- A printed test sheet is reviewed at every release that touches finance UI.

## Forbidden patterns

1. Reports that render only in screen colour.
2. Status indicated by colour alone (must include text label).
3. Multi-column tables that overflow horizontally on A4.
4. Charts unreadable in monochrome.
5. Headers and footers that drop on subsequent pages.
6. Currency symbols missing from money columns.
7. Page numbering missing or unstable.
8. Sign-off boxes missing on audit-relevant reports.
9. Watermarks left on after sign-off.
10. PDF export that re-renders to image (kills text searchability).

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
