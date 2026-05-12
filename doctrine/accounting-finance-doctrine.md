---
name: accounting-finance-doctrine
version: 1.0.0
status: pass-with-caveats
applies-to: skills-web-dev, srs-skills, proposal-skills, business-plan-skills, and any consumer engine that generates finance- or accounting-touching artefacts.
owner: Chwezi Core Systems finance/accounting doctrine owner.
---

# Chwezi Accounting & Finance Doctrine

## 1. Purpose and scope

This doctrine is the canonical accounting and finance reference for every skill engine, agent, developer, analyst, proposal writer, business-plan author, and finance reviewer working across the Chwezi system. It governs what counts as accounting, how the books are kept, how money-touching workflows enter the ledger, how tax is treated, how controls are designed, how non-accountants interact with the system, and how outputs are released.

It is an implementation standard. It is not a substitute for accountant, auditor, tax adviser, legal adviser, regulator, or standard-setter authority. Any client-facing IFRS, statutory, tax, payroll, exchange-rate, or regulator claim remains subject to current-source verification.

## 2. The accounting and finance boundary

Payroll, expenses, purchases, stock and inventory, POS, banking, mobile money, grants, fixed assets, and tax are finance and accounting scope whenever they touch the Chart of Accounts, subledgers, postings, rates, reconciliations, approvals, financial reports, statutory returns, or audit evidence.

A sale, payment received, supplier bill, stock receipt, payroll run, bank charge, refund, mobile-money transaction, cash-drawer close, grant receipt, asset acquisition, or tax event enters the accounting boundary through an approved posting service, reconciliation, or review workflow.

Non-accountant screens may present business language first, but they must not permit accounting damage without permissions, review, reversal controls, and audit evidence.

## 3. The Chart of Accounts backbone

The Chart of Accounts is the backbone for account mapping, control accounts, reporting groups, dimensions, permissions, and audit evidence. It drives posting rules, subledger control accounts, tax and statutory liability accounts, clearing accounts, migration mapping, management-accounting dimensions, reporting groups, and direct-posting permissions.

No workflow may bypass the CoA, rely on free-text pseudo-accounts, or treat financial reports as disconnected summaries.

Minimum CoA metadata: account class, statement group, normal or enforced direction rule, contra-account flag, control-account owner, tax or statutory flag, currency rule, dimension requirements, direct-posting permission, subledger binding, reconciliation requirement, and evidence requirement. See `references/chart-of-accounts.md`.

## 4. Policy hierarchy and reporting basis

The reporting framework is identified explicitly on every artefact: IFRS, IFRS for SMEs, local statutory basis, client-specific basis, or not applicable.

| Level | Rule |
|---|---|
| 1 | **IFRS for SMEs is the practical default** for typical Chwezi clients (SMEs, schools, clinics, NGOs, retail, agribusiness, hospitality) — see `references/ifrs-for-smes-default.md`. |
| 2 | **Full IFRS** is selected where the client is a public-interest entity, carries external financing covenants requiring it, has donor-mandated full IFRS, or expects regulated/listed status — see `references/full-ifrs-overlay.md`. |
| 3 | Local statutory, tax, payroll, filing, regulator, and exchange-rate requirements override generic templates only after current-source verification. |
| 4 | Client-specific accounting policy choices are documented with owner, effective date, affected books and entities, professional-review status, and report impact. |
| 5 | Professional review is required for complex judgement, statutory sign-off, audit positions, tax positions, and final reporting where the output would otherwise imply authority. |

US GAAP is **not** the default. If US GAAP applies, it is explicitly marked as a client-specific or jurisdiction-specific overlay. See `references/policy-hierarchy.md`.

## 5. Ledger invariants

Non-negotiable. Every artefact that affects the ledger must honour these. Full detail in `references/ledger-invariants.md`.

| Invariant | Rule |
|---|---|
| Posting boundary | Feature modules submit accounting events to approved posting services. They do not write directly to journal lines. |
| Double entry | Posted journals balance by currency and contain debit and credit effects. |
| Immutability | Posted history is not edited or deleted through ordinary application paths. Corrections use linked reversal or correction postings. |
| Reversal | Reversals link to the original transaction and preserve reason, actor, date, amount, and full or partial reversal state. |
| Period state | Locked-period posting is rejected or routed to an approved adjustment path. |
| Audit log | Posted transactions remain traceable to source documents, preparer and reviewer actions, approvals, evidence, and system identity. |
| Idempotency | Retried mutating posting commands do not create duplicate accounting events. Reused keys with changed payloads are rejected or quarantined. |
| Control-account tie-out | Control accounts reconcile to their subledger at every close and at migration. |

## 6. Tax, VAT-inclusive posting, and return-ready packs

Systems produce tax reports and tax-return data outputs when VAT, PAYE, WHT, NSSF, KRA, URA, or other statutory filings are in scope.

VAT-inclusive sales and purchases are split so ledger postings and reports separate net revenue or expense from VAT control-account balances. Output VAT, input VAT, withholding, PAYE, NSSF, and other statutory balances route through governed CoA control or liability accounts, never through informal notes, spreadsheet-only adjustments, or free-text report lines.

A tax-return pack includes: jurisdiction and authority, taxpayer identity, filing period, return type and template version, ledger and subledger source accounts, tax codes and current-source evidence, return-line mapping where verified, source documents (invoices, credit notes, payroll schedules, WHT certificates, payment slips, acknowledgements), evidence pack, reviewer sign-off, and open gaps with filing caveats.

See `references/tax-vat-and-returns.md`.

## 7. Live-rate and current-source verification

Any current tax, payroll, statutory, regulator, threshold, exchange-rate, EFRIS, filing, or return-format claim is marked `verified-current` or blocked before release. Planning defaults may seed estimates and drafts only; they must not appear in final operational output without verification logged in the source register. See `references/live-rate-verification-protocol.md`.

## 8. Forbidden patterns

Strict. Every consumer engine, every generated artefact, every PR review enforces these:

1. Direct write paths to `journal_lines` or equivalent accounting tables outside approved posting services.
2. Single-sided ledger effects where double entry is in scope.
3. Editing or deleting posted accounting history without reconstructable immutable audit evidence.
4. **LIFO** as an IFRS or IFRS for SMEs compliant option.
5. **US GAAP** defaults applied without explicit selection.
6. Hardcoded tax, payroll, statutory, EFRIS, NSSF, PAYE, VAT, WHT, or exchange-rate values in final outputs without current-source verification.
7. VAT-inclusive postings that do not split net revenue or expense from tax control-account balances.
8. Migration cutover without opening-balance and subledger tie-out sign-off.
9. Vendor-replacement proposal language without professional-review caveats and acceptance criteria.
10. Stale FX rates used for invoicing, revaluation, or tax reporting.
11. Third-party-product-first language ("just like QuickBooks", "Tally-style") in proposals or design docs without a Chwezi-specific accounting standard backing it.
12. Destructive verbs (`Delete`, `Remove`) exposed on posted accounting records in UI.
13. Gross-only transaction display that conflates net, tax, and gross into one figure.
14. Dashboards that show summary numbers without a drilldown affordance to source.

See `references/forbidden-patterns.md`.

## 9. Required patterns

1. Approved posting services as the only path to the ledger.
2. Double-entry, reversal, period-lock, audit-log, idempotency, and control-account tie-out wherever ledger postings are in scope.
3. CoA backbone with full metadata and dimensions.
4. Tax-return pack capability where statutory filing is in scope.
5. VAT-inclusive decomposition.
6. Reconciliation as a triage UI for bank, POS, cash drawer, and mobile money.
7. Opening-balance and migration sign-off.
8. Role-conditioned UI with separate workflow and ledger surfaces.
9. Drilldown chain from report line to account to journal to source document to evidence file to audit event.
10. Status taxonomy used consistently: `draft`, `awaiting-approval`, `posted`, `reversed`, `matched`, `unmatched`, `exception`, `locked`.
11. Print-fidelity stylesheet for every report and evidence pack.
12. Plain East African business English microcopy on workflow surfaces; accountant terminology on ledger surfaces.
13. Live-rate verification logged at the point of every rate, threshold, or template reference.
14. Evidence attachment inline on every posting screen.

See `references/required-patterns.md` and `references/design-system-finance-accounting.md`.

## 10. UI/UX foundation

Finance/accounting UI in the Chwezi system is built on:

- **Two surface modes.** Workflow surface for cashiers, clerks, managers, and family-business users. Ledger surface for accountants, controllers, and auditors. Same data, different chrome and density.
- **Role-conditioned shell.** Top bar always shows entity, book, period state, role, and environment.
- **Drilldown as a first-class primitive.** Every number is clickable into its provenance.
- **Status taxonomy used consistently.**
- **Semantic colour.** Green and red are signals only. They are not brand. They are not button colours.
- **Print fidelity is P0.** Every report renders correctly on A4, black-and-white, with auditor sign-off boxes.
- **Low-bandwidth, low-spec Android tolerated.** Optimistic post + reconcile; offline drawer close; no silent loss.

Full design system in `references/design-system-finance-accounting.md`; anti-patterns in `references/design-anti-patterns.md`.

## 11. Country extension framework

Uganda is the home jurisdiction. Country extensions for Kenya, Rwanda, Tanzania, and South Africa are named placeholders that consume the same doctrine through the country-extension framework. Each country extension provides: authority list, return-form templates and versions, rate/threshold register, payroll statutory schedule, exchange-rate source, e-invoicing or equivalent (EFRIS, eTIMS, …), and verification protocol. See `references/country-extension-framework.md` and `references/uganda-compliance-caveats.md`.

## 12. Terminology

A controlled glossary is in `references/terminology-glossary.md`. Use these terms verbatim across all consumer engines: accounting boundary, posting service, control account, clearing account, live-rate verification, tax-return pack, evidence pack, professional review, drilldown chain, workflow surface, ledger surface, role-conditioned shell, status taxonomy, period state, country extension.

## 13. Versioning and change control

This doctrine is versioned with semver. The current version is at the top of this file. Every breaking change requires a major-version bump, a CHANGELOG entry, a deprecation note in `integration/deprecation-list.md`, and a mirror sync to every consumer engine. See `references/versioning-and-changelog.md`.

Every consumer engine adoption records: engine name, doctrine version adopted, adoption date, owner, reviewer, affected files, and any unresolved gaps.

## 14. Quality-gate triggers

The finance and accounting quality gate runs whenever an artefact touches money, inventory, payroll, tax, grants, banking, POS, mobile money, statutory compliance, or accounting records. Trigger detail and pass/fail criteria are in `../governance/finance-accounting-quality-gate.md`.

## 15. How to reference this doctrine

See `../governance/how-to-reference-this-doctrine.md` for the exact pattern each consumer engine uses.

## 16. Known verification gaps

Documented gaps that are blockers for final operational claims:

- Authoritative IFRS Foundation text and current effective dates not re-verified in this pass.
- Current Uganda VAT, PAYE, WHT, NSSF, exchange-rate, EFRIS, URA return-template, URSB filing, and ICPAU framework values remain verification targets per `references/live-rate-verification-protocol.md`.
- No stable public BoU daily exchange-rate CSV/API endpoint identified.
- No public canonical EFRIS API/schema URL identified.
- Sector-specific statutory and regulator details for schools, clinics, NGOs, retail/POS, manufacturing, agribusiness, hospitality not finalised in this pass.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
