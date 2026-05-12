# Seed CoA — Uganda SME (Limited Company)

Planning-default seed Chart of Accounts for a typical Uganda private limited company. **Tax-control account codes and rate references are planning defaults** — verify per `live-rate-verification-protocol.md` before final use.

Numeric range convention: 1xxx assets, 2xxx liabilities, 3xxx equity, 4xxx income, 5xxx cost of sales, 6xxx operating expenses, 7xxx other income/expense, 8xxx finance income/cost, 9xxx tax / other.

## 1xxx — Assets

| Code | Name | Class | Statement group | Normal | Control? | Tax flag | Direct-post | Recon |
|---|---|---|---|---|---|---|---|---|
| 1000 | Cash on Hand — Main | Asset | Current — Cash | Dr | Yes | none | restricted | daily |
| 1010 | Petty Cash Imprest | Asset | Current — Cash | Dr | Yes | none | restricted | event-driven |
| 1100 | Bank — Stanbic UGX | Asset | Current — Cash | Dr | Yes | none | restricted | monthly |
| 1110 | Bank — Centenary UGX | Asset | Current — Cash | Dr | Yes | none | restricted | monthly |
| 1120 | Bank — Stanbic USD | Asset | Current — Cash | Dr | Yes | none | restricted | monthly |
| 1200 | Mobile Money — MTN Business | Asset | Current — Cash | Dr | Yes | none | restricted | daily |
| 1210 | Mobile Money — Airtel Business | Asset | Current — Cash | Dr | Yes | none | restricted | daily |
| 1300 | Trade Receivables Control | Asset | Current — Receivables | Dr | Yes | none | restricted | monthly |
| 1310 | Allowance for Doubtful Debts | Asset (contra) | Current — Receivables | Cr | No | none | restricted | monthly |
| 1320 | Other Receivables | Asset | Current — Receivables | Dr | No | none | permitted | event-driven |
| 1330 | Staff Advances | Asset | Current — Receivables | Dr | No | none | permitted | monthly |
| 1340 | Customer Deposits Control | Asset | Current — Receivables | Cr | Yes | none | restricted | monthly |
| 1400 | Prepayments | Asset | Current — Prepayments | Dr | No | none | permitted | monthly |
| 1500 | Inventory Control — Main Warehouse | Asset | Current — Inventory | Dr | Yes | none | restricted | monthly |
| 1510 | Inventory Control — Shop A | Asset | Current — Inventory | Dr | Yes | none | restricted | monthly |
| 1520 | Inventory — Goods in Transit | Asset | Current — Inventory | Dr | Yes | none | restricted | event-driven |
| 1530 | Inventory — Allowance for Obsolescence | Asset (contra) | Current — Inventory | Cr | No | none | restricted | monthly |
| 1600 | Input VAT Control | Asset | Current — Tax Assets | Dr | Yes | input-vat | restricted | monthly |
| 1610 | Tax Receivable — Income Tax | Asset | Current — Tax Assets | Dr | Yes | tax-receivable | restricted | monthly |
| 1620 | Tax Receivable — WHT Credits | Asset | Current — Tax Assets | Dr | Yes | tax-receivable | restricted | monthly |
| 1700 | Fixed Assets — Land | Asset | Non-current — PPE | Dr | Yes | none | restricted | annually |
| 1710 | Fixed Assets — Buildings | Asset | Non-current — PPE | Dr | Yes | none | restricted | annually |
| 1720 | Fixed Assets — Motor Vehicles | Asset | Non-current — PPE | Dr | Yes | none | restricted | annually |
| 1730 | Fixed Assets — Furniture & Fittings | Asset | Non-current — PPE | Dr | Yes | none | restricted | annually |
| 1740 | Fixed Assets — Computer Equipment | Asset | Non-current — PPE | Dr | Yes | none | restricted | annually |
| 1750 | Fixed Assets — Plant & Machinery | Asset | Non-current — PPE | Dr | Yes | none | restricted | annually |
| 1790 | Accumulated Depreciation Control | Asset (contra) | Non-current — PPE | Cr | Yes | none | restricted | monthly |
| 1800 | Intangible Assets — Software | Asset | Non-current — Intangibles | Dr | Yes | none | restricted | annually |
| 1890 | Accumulated Amortisation Control | Asset (contra) | Non-current — Intangibles | Cr | Yes | none | restricted | annually |
| 1900 | Deferred Tax Asset | Asset | Non-current — Tax | Dr | Yes | none | restricted | annually |
| 1990 | Migration Suspense | Asset / Liability | Current — Suspense | Dr/Cr | Yes | none | system-only | event-driven |

## 2xxx — Liabilities

| Code | Name | Class | Statement group | Normal | Control? | Tax flag |
|---|---|---|---|---|---|---|
| 2000 | Trade Payables Control | Liability | Current — Payables | Cr | Yes | none |
| 2010 | Accrued Expenses | Liability | Current — Payables | Cr | No | none |
| 2020 | Supplier Deposits Control | Liability | Current — Payables | Dr | Yes | none |
| 2100 | Output VAT Control | Liability | Current — Tax Payables | Cr | Yes | output-vat |
| 2110 | PAYE Payable | Liability | Current — Tax Payables | Cr | Yes | paye-payable |
| 2120 | NSSF Payable | Liability | Current — Statutory | Cr | Yes | nssf-payable |
| 2130 | WHT Payable | Liability | Current — Tax Payables | Cr | Yes | wht-payable |
| 2140 | Local Service Tax Payable | Liability | Current — Statutory | Cr | Yes | none |
| 2150 | Income Tax Payable | Liability | Current — Tax Payables | Cr | Yes | none |
| 2200 | Customer Advances / Deferred Revenue | Liability | Current — Deferred | Cr | Yes | none |
| 2300 | Salaries Payable | Liability | Current — Employee Benefits | Cr | Yes | none |
| 2400 | Card Settlement Clearing | Liability | Current — Settlement | Cr | Yes | none |
| 2410 | Mobile-Money Settlement Clearing — MTN | Liability | Current — Settlement | Cr | Yes | none |
| 2420 | Mobile-Money Settlement Clearing — Airtel | Liability | Current — Settlement | Cr | Yes | none |
| 2430 | POS Cash Tendered Clearing | Liability | Current — Settlement | Cr | Yes | none |
| 2500 | Provisions — Short-term | Liability | Current — Provisions | Cr | No | none |
| 2600 | Borrowings — Bank Loan Current Portion | Liability | Current — Borrowings | Cr | Yes | none |
| 2700 | Borrowings — Bank Loan Non-current | Liability | Non-current — Borrowings | Cr | Yes | none |
| 2800 | Deferred Tax Liability | Liability | Non-current — Tax | Cr | Yes | none |
| 2900 | Provisions — Long-term | Liability | Non-current — Provisions | Cr | No | none |

## 3xxx — Equity

| Code | Name | Class | Statement group | Normal |
|---|---|---|---|---|
| 3000 | Issued Share Capital | Equity | Equity — Capital | Cr |
| 3100 | Share Premium | Equity | Equity — Capital | Cr |
| 3200 | Retained Earnings | Equity | Equity — Reserves | Cr |
| 3300 | Current-Year Profit/Loss | Equity | Equity — Reserves | Cr |
| 3400 | Revaluation Reserve | Equity | Equity — Reserves | Cr |
| 3500 | Translation Reserve | Equity | Equity — Reserves | Cr |
| 3900 | Dividends Declared | Equity (contra) | Equity — Reserves | Dr |

## 4xxx — Revenue

| Code | Name | Statement group | Notes |
|---|---|---|---|
| 4000 | Sales — Goods | Revenue | VAT-inclusive postings split here. |
| 4100 | Sales — Services | Revenue | |
| 4200 | Sales Returns | Revenue (contra) | |
| 4300 | Trade Discounts | Revenue (contra) | |
| 4400 | Other Operating Income | Other operating income | |

## 5xxx — Cost of sales / cost of services

| Code | Name | Notes |
|---|---|---|
| 5000 | Cost of Sales — Goods | Posted at sale (perpetual) or at month-end (periodic). |
| 5100 | Cost of Services | Direct services cost. |
| 5200 | Carriage Inwards | |
| 5300 | Inventory Adjustments — Shrinkage / Obsolescence | |
| 5400 | Inventory Write-Down to NRV | |

## 6xxx — Operating expenses

| Code | Name |
|---|---|
| 6000 | Salaries and Wages — Gross |
| 6010 | Employer NSSF |
| 6020 | Employer Other Benefits |
| 6100 | Rent — Premises |
| 6110 | Utilities — Electricity / Water |
| 6120 | Internet & Communications |
| 6200 | Marketing and Advertising |
| 6300 | Travel and Subsistence |
| 6400 | Office Supplies and Consumables |
| 6500 | Depreciation Expense |
| 6510 | Amortisation Expense |
| 6600 | Bad Debts Expense |
| 6700 | Insurance |
| 6800 | Professional Fees |
| 6900 | Bank Charges and Commissions |

## 7xxx — Other income / expense

| Code | Name |
|---|---|
| 7000 | Gain / (Loss) on Disposal of Assets |
| 7100 | Foreign Exchange Gain / (Loss) — Unrealised |
| 7110 | Foreign Exchange Gain / (Loss) — Realised |

## 8xxx — Finance

| Code | Name |
|---|---|
| 8000 | Interest Income |
| 8100 | Interest Expense |

## 9xxx — Tax

| Code | Name |
|---|---|
| 9000 | Current Income Tax Expense |
| 9100 | Deferred Tax Expense |

## Dimensions enabled by default

- entity
- branch / site
- cost-centre
- project
- product-line (for revenue and cost-of-sales accounts)

## Notes

- VAT rate, EFRIS tax codes, NSSF rates, PAYE brackets, WHT rates: see source register; never hardcoded.
- The CoA above is a Uganda SME limited-company seed. Sole-trader, NGO, school, clinic, agribusiness, and hospitality variants exist as overlays in the relevant sector annex.
- Account codes are stable. Adding accounts uses unused numeric space; removing accounts requires migration sign-off.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
