# Chart of Accounts Backbone

The CoA is the central nervous system of the finance/accounting capability. Every artefact — code, schema, test, SRS, proposal, business plan — must respect it.

## Minimum CoA metadata

Each account carries:

| Field | Required | Description |
|---|---|---|
| `code` | yes | Stable identifier. Numeric or alphanumeric per entity convention. |
| `name` | yes | Human-readable, in plain business English. |
| `class` | yes | Asset, Liability, Equity, Income, Expense. |
| `statement-group` | yes | The line on the SFP or SOCI where this account aggregates. |
| `normal-side` | yes | `debit` or `credit`. |
| `direction-rule` | optional | `enforced` (only that side accepted) or `flexible`. |
| `contra` | optional | Flag for contra accounts (accumulated depreciation, allowance for doubtful debts, sales returns, …). |
| `control-account` | optional | If yes, names the subledger that must tie out. |
| `tax-flag` | optional | One of: `output-vat`, `input-vat`, `wht-payable`, `paye-payable`, `nssf-payable`, `tax-receivable`, `none`. |
| `currency-rule` | yes | `entity-currency-only`, `multi-currency-allowed`, or `foreign-currency-only`. |
| `dimensions-required` | yes | List of dimensions that **must** be present on every posting to this account (cost-centre, project, grant, branch, …). |
| `dimensions-permitted` | yes | List of dimensions allowed in addition. |
| `direct-posting` | yes | `permitted`, `restricted-to-controller`, or `system-only`. |
| `reconciliation-required` | yes | `daily`, `monthly`, `quarterly`, `annually`, `event-driven`, `none`. |
| `evidence-required` | yes | `always`, `over-threshold`, `none`. |
| `evidence-threshold` | conditional | If `over-threshold`, the amount. |
| `active-from` / `active-to` | yes / optional | Effective dates. |
| `owner-role` | yes | Role responsible for the account (Accountant, Controller, Payroll Officer, Inventory Manager, …). |

## Statement-group taxonomy

The canonical statement groups for IFRS for SMEs reporting (Section 4–7) are:

**Statement of Financial Position**
- Non-current assets: PPE, intangibles, biological assets, investment property, investments in associates, deferred tax assets, other non-current.
- Current assets: inventories, trade and other receivables, prepayments, current tax assets, cash and cash equivalents, mobile money, restricted cash.
- Equity: share capital, retained earnings, reserves, non-controlling interest.
- Non-current liabilities: borrowings (non-current portion), deferred tax liabilities, provisions (non-current), employee benefits (non-current).
- Current liabilities: trade and other payables, current tax payable, borrowings (current portion), provisions (current), employee benefits (current), VAT payable, PAYE payable, WHT payable, NSSF payable.

**Statement of Comprehensive Income**
- Revenue.
- Cost of sales / cost of services.
- Other income.
- Distribution costs.
- Administrative expenses.
- Other operating expenses.
- Finance income.
- Finance costs.
- Share of profit of equity-accounted investees.
- Income tax expense.
- Other comprehensive income.

These groups drive the trial-balance grouping report, the SFP, the SOCI, and the management-accounts pack.

## Control accounts

The following are control accounts by default in every Chwezi entity:

| Account | Subledger |
|---|---|
| Trade Receivables Control | AR open items |
| Trade Payables Control | AP open items |
| Inventory Control (per location, per valuation method) | Inventory ledger / stock layers |
| Fixed Assets Cost | Fixed-asset register |
| Fixed Assets Accumulated Depreciation | Fixed-asset register |
| Bank — \<account\> | Bank statement / reconciliation |
| Cash on Hand — \<drawer\> | Cash drawer reconciliation |
| Mobile Money — \<provider\> \<account\> | Mobile-money statement / reconciliation |
| Output VAT Control | Tax engine / VAT return |
| Input VAT Control | Tax engine / VAT return |
| PAYE Payable | Payroll subledger |
| NSSF Payable | Payroll subledger |
| WHT Payable | Tax engine / WHT certificates |
| Customer Deposits | AR deposit register |
| Supplier Deposits | AP deposit register |
| Petty Cash Imprest | Petty-cash register |
| POS Cash Tendered Clearing | POS Z-report reconciliation |
| Card Settlement Clearing | Card acquirer settlement |
| Mobile-Money Settlement Clearing | Provider settlement reconciliation |
| Migration Suspense | Cutover only — must be zero at sign-off |

Direct posting to these accounts is `restricted-to-controller`. Routine postings happen through the subledger workflows that own them.

## Dimensions

Standard dimensions defined globally; entities switch them on as needed:

- `entity` (always required for multi-entity books)
- `branch` / `site` / `location`
- `department`
- `cost-centre`
- `project` / `job`
- `grant` / `fund`
- `donor-restriction`
- `product-line` / `SKU` / `category`
- `customer` / `supplier` (where relevant)
- `activity` / `channel`
- `currency` / `book`

Free-text "tags" are not dimensions. They do not appear on postings.

## Seed CoA fixtures

A canonical seed CoA for a Uganda SME (sole-trader and limited-company variants) is at `../examples/coa-seed-uganda-sme.md`. Country extensions provide their own seed CoA with adapted tax and statutory accounts.

## Migration mapping

Every migration cutover provides a mapping from legacy accounts to Chwezi CoA accounts. Unmapped legacy balances route to Migration Suspense with an explicit aging plan, and Migration Suspense must reach zero (or be formally waived with sign-off) at cutover acceptance.

## Forbidden patterns

- Postings to "Other" / "Miscellaneous" / "Suspense" accounts as a routine pattern.
- Tax amounts in line memos rather than on tax control accounts.
- Hierarchies that conflate statement classes (revenue accounts under an expense parent, …).
- Free-text accounts.
- Cosmetic re-numbering of accounts after postings have hit them (use account merging or aliasing instead).
- Duplicate active accounts for the same purpose with no documented reason.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
