---
name: embedded-accounting-engine-proposal
description: Use for consulting proposals to design, build, implement, or replace bookkeeping/accounting functionality inside a SaaS, ERP, POS, school, clinic, NGO, hospitality, retail, manufacturing, agribusiness, mobile-money, or marketplace system. Provides client-facing positioning, single-ledger posting-engine architecture, QuickBooks/Sage/Pastel/Tally replacement language, audit-ready reporting deliverables, implementation methodology, acceptance criteria, caveats, team roles, and pricing scope.
metadata:
  portable: true
---

# Embedded Accounting Engine Proposal

## Use When

- The proposal includes bookkeeping, financial reporting, finance automation, ERP/POS finance, inventory accounting, payroll accounting, tax/VAT, donor/fund accounting, bank/mobile-money reconciliation, or statutory reports.
- The client wants to avoid separate QuickBooks, Xero, Sage, Pastel, Tally, Zoho Books, Wave, or similar subscriptions for routine books.
- A SaaS build must credibly claim audit-ready financial statements from inside the operating system.

## Do Not Use When

- The engagement is only accounting cleanup or advisory with no software build; use `accounting-finance-advisory`.
- The proposal cannot include accountant validation, posting-rule testing, reconciliation, and first-close support; do not claim automated accounting without those controls.
- The client needs statutory audit, tax filing sign-off, impairment, fair value, deferred tax, or other professional judgement; include caveats and specialist roles.

## Core Positioning

Use client-facing language:

> The system will not treat accounting as a separate module to be reconciled later. Every approved business event will post through a single embedded accounting engine into one controlled ledger. This means sales, stock, payments, payroll, grants, and assets produce audit-ready books from the same operational data the teams use every day.

Verifiable claim:

> For routine bookkeeping and statutory/management reporting of the operating entity, the system is designed to replace separate QuickBooks/Sage/Pastel/Tally-class accounting subscriptions. Statutory audit, tax filing sign-off, and complex accounting judgements remain subject to applicable law and professional review.

## Proposal Sections To Include

1. Why embedded accounting engine.
2. Single-ledger architecture.
3. Financial and operational reports delivered out of the box.
4. Implementation methodology and gates.
5. Accounting validation and reconciliation approach.
6. Caveats and professional judgement boundaries.
7. Team roles and client-side finance owner.
8. Acceptance criteria.

## Deliverables Block

- Chart of accounts template and tenant-specific mapping register.
- Posting-rule matrix for sales, purchases, payments, payroll, inventory, assets, tax, grants, and reversals.
- Embedded `LedgerPostingService` and append-only journal design.
- Financial reports: trial balance, general ledger, income statement, statement of financial position, cash flow statement, statement of changes in equity/net assets.
- Operational reports: AR ageing, AP ageing, inventory valuation, COGS, stock movement, payroll liabilities, VAT/tax schedules, bank/mobile-money reconciliation, fixed asset register, donor/fund reports where relevant.
- Migration pack: opening balances, customer/supplier balances, stock values, fixed assets, unpaid payroll/tax liabilities.
- Reconciliation and first-close support pack.

## Acceptance Criteria

- Every posted journal balances.
- No module writes directly to the ledger tables.
- Reports regenerate from journal lines.
- AR/AP/inventory/fixed assets/payroll/tax control accounts reconcile to subledgers.
- Locked periods reject new postings.
- Duplicate business events do not double-post.
- Posting rules pass accountant-reviewed test scenarios.

## References

- `references/accounting-engine-positioning.md`
- `references/accounting-caveats-and-claims.md`
