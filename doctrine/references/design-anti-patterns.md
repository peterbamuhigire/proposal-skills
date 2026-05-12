# Design Anti-Patterns

These are blockers under the UI / UX side of the quality gate. They appear repeatedly in consumer-fintech work and in accounting software built without a doctrine.

## Layout and density

1. Cards-with-big-coloured-numbers dashboards copied from consumer fintech — they hide the audit trail and conflate signal with brand.
2. Single density mode for all roles (no separate workflow vs ledger surface).
3. Horizontal tables on mobile reconciliation screens.
4. Bottom navigation that hides the active entity, book, or period state.
5. Dashboards that show summary numbers without a drilldown affordance.

## Colour

6. Green or red used for non-state purposes (brand, header chrome, CTAs, decoration).
7. Colour as the only signal for status (must always pair with text or icon).
8. Brand palette applied to ledger surfaces.
9. Dark mode forced on workflow surfaces in daylight kiosk contexts.

## Typography

10. Proportional numerals on money columns.
11. More than seven type sizes in a single product.
12. Marketing-style hero typography on ledger pages.
13. Italics on numeric cells.

## Money display

14. Gross-only transaction lines that conflate net, tax, and gross.
15. Tax shown only in a tooltip.
16. Currency symbol baked into the value string instead of a separate column label.
17. Negative amounts as parentheses **and** semantic colour and minus sign simultaneously (pick one convention per product and use it consistently).

## Posted records

18. `Delete` or `Remove` verbs on posted accounting records.
19. Inline edit on posted journal lines.
20. Soft-delete toggles on journals.
21. Re-save semantics on a journal (the act of "save" on a posted record).

## Compliance and disclosure

22. Compliance disclosures rendered as modal dumps disconnected from the field they qualify.
23. Print-only disclosures absent from the screen version.
24. Disclosure text in a separate "Help" link rather than next to the field.

## Status

25. Free-text status not drawn from the controlled taxonomy.
26. Status colours that change per page.
27. Status chips replaced by raw boolean badges (`active true / false`).

## Print

28. Reports without a print stylesheet.
29. Black-on-near-black or pale-grey-on-white that disappears on monochrome printing.
30. Charts that lose meaning without colour.
31. Missing auditor sign-off boxes on the print version.

## Visual refresh anti-pattern

32. "Aesthetic refresh" PRs that change colour or type without revisiting IA, task flow, role-conditioned chrome, or evidence affordances.

## Mobile

33. Pinch-zoom required to read a money cell.
34. Touch targets under 44 px on cashier flows.
35. Forms that depend on hover.
36. Toasts that close on tap before the user has read them.

## Illustration and decoration

37. Hero illustrations inside ledger, journal, reconciliation, or close screens.
38. Stock photography on report pages.
39. Animated icons on posted records.

## Microcopy

40. Clinical or tone-deaf error messages (failed payments, overdrafts, flagged transactions handled as exceptions to a happy path).
41. Accountant vocabulary on workflow surfaces.
42. Business vocabulary that prevents the accountant from finding the accounting word in the ledger surface.
43. Capitalisation inconsistency between status chips, button labels, and headings.

## Search and lookup

44. Free-text supplier or customer fields when a master record exists.
45. Lookups that show codes without names.
46. Lookups that show names without codes.

## Forms

47. No keyboard shortcut on save / post / cancel for ledger forms.
48. Tab order that skips the amount column.
49. Validation errors shown only on submit, not inline.

## Reconciliation

50. Reconciliation rendered as a downloadable report rather than a triage UI.
51. Imported items committed to the ledger before matching.

## Drilldown

52. Drilldown that opens in a popup that loses context.
53. Drilldown that requires a separate menu rather than a click on the figure.

## Reviewer affordances

54. Sign-off implemented as a free-text comment.
55. Sign-off without identity proof in the audit log.

## Locked states

56. Locked-period errors shown as red toasts after the user fills the form.
57. Reopen workflows that bypass approval.

## Forbidden CTA copy

58. "Final" / "Submit final" used loosely. Reserve "submit final" for true non-reversible authority filings; reserve "post" for ledger commits.

## Enforcement

Every UI PR includes a checklist against this file. The `finance-ui-pattern-library` skill provides a lint script for the common cases (status taxonomy, money triplet, drilldown affordance, status colour mapping, print stylesheet presence).

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
