# Worked Example — VAT-Inclusive Posting

A cashier records a VAT-inclusive sale of UGX 118,000 (gross). VAT standard rate is treated as a planning default here; the actual rate is read from the source register at posting time.

## Inputs

| Field | Value |
|---|---|
| Source document | POS receipt POS-2026-05-12-0042 |
| Date | 2026-05-12 |
| Customer | Walk-in (anonymous) |
| Tendered | Cash UGX 118,000 |
| Gross sale | 118,000 |
| Tax code | UG-VAT-STD (rate read from source register; planning value: 18%) |
| Net | 100,000 (computed: 118,000 / (1 + rate)) |
| Tax | 18,000 (computed: 118,000 − net) |

## Posting (single journal, balanced)

| Line | Debit | Credit | Account | Tax flag | Dimensions |
|---|---:|---:|---|---|---|
| 1 | 118,000 | | 2430 POS Cash Tendered Clearing | none | branch=Shop A |
| 2 | | 100,000 | 4000 Sales — Goods | none | branch=Shop A, product-line=… |
| 3 | | 18,000 | 2100 Output VAT Control | output-vat | branch=Shop A, tax-code=UG-VAT-STD |

Tax line is **a full journal line on the Output VAT Control account**, not a memo on the sale line. Gross is **not** posted as a single combined figure.

## Cost-of-sales (perpetual inventory; assumed cost UGX 70,000)

| Line | Debit | Credit | Account | Dimensions |
|---|---:|---:|---|---|
| 4 | 70,000 | | 5000 Cost of Sales — Goods | branch=Shop A, product-line=… |
| 5 | | 70,000 | 1510 Inventory Control — Shop A | branch=Shop A, product-line=… |

## End-of-shift drawer close

When the cashier closes the drawer, the POS Cash Tendered Clearing balance is moved to Cash on Hand:

| Line | Debit | Credit | Account |
|---|---:|---:|---|
| 6 | 118,000 | | 1000 Cash on Hand — Main |
| 7 | | 118,000 | 2430 POS Cash Tendered Clearing |

The clearing account closes to zero each shift. A non-zero residual is an exception that goes to the reconciliation triage.

## EFRIS submission

The posting service flags this sale for EFRIS submission. The EFRIS state moves: `efris-submitted` → `efris-confirmed` (carrying the URA fiscal document identifier). Failure to confirm within the configured window routes the sale to the EFRIS reconciliation exception queue.

## VAT return-pack mapping

| Return-pack line | Source |
|---|---|
| Standard-rated sales | Sum of Sales — Goods + Sales — Services where tax-code rate = standard, by filing period. |
| Output VAT | Output VAT Control posted in the filing period. |
| Source documents | POS receipts, sales invoices, credit notes — list available with each return pack. |

## Reversal (if the cashier voids the sale)

A new journal is posted that reverses lines 1–5 with opposite sign, linked to the original. The reversal carries a reason code (`customer-cancellation`, `cashier-error`, `payment-failed`, …), the actor (cashier with role context), the date, and a `partial=false` flag. The EFRIS state moves to `efris-cancelled` and a credit note is issued referencing the original fiscal document identifier.

## Print fidelity

The receipt prints in monochrome and shows:

- Entity name, TIN, address
- Date and time
- POS receipt identifier
- Cashier name
- Net amount column
- Tax amount column (with tax code)
- Gross amount column
- Tendered amount
- URA fiscal document identifier (when EFRIS confirmed)
- Print footer with version, build, framework

The receipt is printable on a thermal printer (40-column) and on A4. The thermal layout collapses to two columns (description / amount) but always preserves a separate tax line.

## What forbidden patterns are avoided

- No single gross figure posted to Sales.
- No tax in a memo.
- No `Delete` button on a posted receipt — the cashier has a `Reverse` button under permission and approval.
- Tax code carries an effective period; rate is read from source register, not hardcoded.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
