# Required Patterns

The positive set. Every artefact in finance scope honours these.

## Accounting / ledger

1. Approved posting services are the only path to the ledger.
2. Double entry holds for every posted journal in every currency.
3. Reversal is the only reversal mechanism.
4. Correction is the only re-statement mechanism (after a reversal).
5. Period state is checked on every posting.
6. Audit log captures actor, evidence, lineage, and posting service version.
7. Idempotency keys carried on all integration-driven postings.
8. Control accounts tie to their subledger at every close and at migration cutover.
9. Evidence attached inline on every posting screen.

## CoA backbone

10. CoA carries full metadata per `chart-of-accounts.md`.
11. Dimensions are governed, not free-text tags.
12. Control accounts and clearing accounts are direct-post-restricted.
13. Statement-group taxonomy drives reporting; reports are derived from the CoA, not stitched manually.

## Framework

14. Framework is identified explicitly on every artefact.
15. IFRS for SMEs is the practical default; full IFRS is the overlay where the client profile demands it.
16. Policy choices are recorded with owner, reviewer, effective date, and report impact.

## Tax

17. VAT-inclusive decomposition at posting time.
18. Tax codes carry rate, jurisdiction, effective period, and source-register reference.
19. Output VAT, Input VAT, WHT, PAYE, NSSF route through governed control accounts.
20. Return-ready packs produced for every authority in scope, period by period.
21. EFRIS / eTIMS reconciled daily or weekly against the ledger.

## Live-rate verification

22. Every rate, threshold, or template version is logged in the source register.
23. Use state is one of `draft`, `pass-with-caveats`, `verified-current`, `blocked`.
24. Verifications combine Tier 1 or Tier 2 sources with a current-period reading.
25. Verifier and date are recorded; verifications cite the source URL or document and the archive path.

## Reconciliation

26. Bank, mobile-money, POS cash drawer, card settlement, and clearing-account reconciliations have an owner, a cadence, an evidence pack, and exception ageing.
27. Reconciliation is a triage UI, not a report.
28. Unmatched items have an ageing column always visible.

## Close

29. Close is a controlled workflow with tasks, owners, dependencies, evidence, review state, and release decision (`pass`, `pass-with-caveats`, `fail`).
30. First close has named reviewer support.

## Migration

31. Cutover pack contains: legacy TB, CoA mapping, open AR, open AP, inventory, fixed assets, bank balances, payroll/tax liabilities, opening journal, sign-off.
32. Migration suspense reaches zero (or is formally waived) at acceptance.

## Controls

33. Maker-checker on payments, refunds, credit notes, manual journals, opening balances, tax settings, supplier master changes, payroll changes, period reopen.
34. Segregation of duties between maker, checker, approver, accountant, controller, auditor, admin.
35. Master-data change history retained.

## Reports

36. Every figure is drillable to source.
37. Print stylesheet for every report.
38. Reports cite the framework, period, and reviewer.

## UI

39. Two surface modes: workflow surface and ledger surface.
40. Role-conditioned shell with entity, book, period state, role, environment always visible.
41. Status taxonomy used consistently.
42. Semantic colour reserved for state.
43. Drilldown is a first-class primitive.
44. Net, tax, gross shown as three distinct fields.

## Microcopy

45. Plain East African business English on workflow surfaces.
46. Accountant terminology on ledger surfaces.
47. Error messages address the user's situation; not clinical, not blaming the user.

## Reviewers

48. Accountant, Controller, CFO/finance lead, Tax reviewer roles exist where the trigger applies.
49. Reviewer sign-off recorded in the audit log before release.

## Versioning

50. Every doctrine, skill, reference, and example carries a version, a last-reviewed date, and a next-review-due date.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
