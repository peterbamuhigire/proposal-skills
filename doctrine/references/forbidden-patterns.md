# Forbidden Patterns

These patterns are blockers under the quality gate. They are forbidden in code, schemas, SRS, SDS, test plans, proposals, business plans, dashboards, UI, prints, and any other artefact.

## Accounting / ledger

1. Direct write to `journal_headers` or `journal_lines` (or equivalent named tables) outside an approved posting service.
2. Single-sided ledger effects in scope of double-entry.
3. Editing or deleting posted accounting history through any normal application path.
4. Soft-delete fields on posted journal records.
5. Cascading delete from any parent record that owns journals.
6. Background "cleanup" jobs that purge posted journals.
7. Tax amounts stored in line memos rather than on tax control accounts.
8. Reposting after edit. (Only reversal + new posting is permitted.)
9. Free-text accounts.
10. Routine postings to "Other", "Miscellaneous", or "Suspense" without an ageing plan.

## IFRS / framework

11. **LIFO** presented as IFRS or IFRS for SMEs compliant, or offered as an unguarded reusable option in either framework.
12. **US GAAP defaults** silently applied without explicit client selection.
13. Goodwill amortisation under full IFRS (IFRS 3 / IAS 36 require annual impairment, not amortisation).
14. Capitalised borrowing costs under IFRS for SMEs (Section 25 requires expensing).
15. Internally generated brands or goodwill capitalised.
16. Operating-lease classification for lessees under full IFRS where IFRS 16 applies and exemptions do not.

## Tax / statutory

17. Hardcoded VAT, PAYE, NSSF, WHT, income-tax, NHIF, customs, or other statutory values in any final artefact.
18. Authority return templates copied into the system without a verified version reference.
19. Authority filing claimed as automated when only a return pack is produced.
20. EFRIS / eTIMS treated as the source of truth instead of as a parallel system reconciled against the ledger.
21. VAT-inclusive postings that do not split net revenue or expense from tax control balances.
22. Tax codes without an effective period.
23. WHT amounts netted into operating expenses instead of posting to WHT Payable.

## Rates and FX

24. "Always use" language for FX, tax, or statutory values without a verification entry.
25. Source-register entries past their `expiry_or_recheck` date still referenced in final output.
26. Verifications based on undated blog posts or third-party PDFs.
27. Verifications without named verifier and date.

## Migration

28. Migration cutover without opening-balance and subledger tie-out sign-off.
29. Migration suspense non-zero (or unwaived) at cutover acceptance.
30. Trial-balance-only migration where open subledgers exist.

## UI / UX

31. Destructive verbs (`Delete`, `Remove`) on posted accounting records.
32. Gross-only transaction display that conflates net, tax, and gross into one figure.
33. Dashboards that show summary numbers without a drilldown affordance to source.
34. Green/red used for non-state purposes (branding, CTAs, decorative).
35. Hero illustrations inside ledger, journal, reconciliation, or close screens.
36. Single density mode applied to all roles (no separate workflow vs ledger surface).
37. Bottom navigation that hides the active entity, book, or period state.
38. Reports without a print stylesheet.
39. Status text used without the controlled status taxonomy.
40. Compliance disclosures rendered as modal dumps disconnected from the field they qualify.
41. Login flows that grant accounting power without role check.
42. "Aesthetic refresh" PRs that change colour or type without revisiting IA or task flow.

## Proposals / business plans

43. Vendor-replacement claims (e.g. "replaces QuickBooks") without professional-review caveats, acceptance criteria, and a named scope.
44. Third-party-product-first language used without a Chwezi-specific accounting standard backing it.
45. Country-context rate values shipped as permanent facts.
46. Business-plan financials without an explicit reporting framework header.
47. LIFO appearing as an IFRS-permitted planning assumption.

## Reviewer / governance

48. Final artefact released without the required reviewer sign-off in the audit log.
49. Admin role granting accounting approval power without role-specific approval.
50. Stale skill / doctrine version referenced without an adoption-checklist entry.

## Enforcement

Each pattern maps to a blocker in `../../governance/finance-accounting-quality-gate.md`. PR reviewers, the `finance-module-audit` skill, and the CI lints share this list.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
