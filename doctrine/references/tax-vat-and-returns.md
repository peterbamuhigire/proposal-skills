# Tax, VAT-Inclusive Posting, and Return-Ready Packs

## Coverage

Systems produce tax reports and return-ready data outputs when any of the following are in scope: VAT, PAYE, WHT, NSSF, EFRIS, KRA, URA, customs, excise, local-government taxes, or any equivalent statutory filing in a country extension.

## VAT-inclusive decomposition

A VAT-inclusive sale or purchase is decomposed at the point of posting into:

- Net amount (revenue or expense)
- Tax amount (output VAT or input VAT)
- Gross amount (reference only)

Output VAT posts to **Output VAT Control**. Input VAT posts to **Input VAT Control**. Net posts to the appropriate revenue or expense account. Gross is recorded on the source document for reconciliation but never posted as a single combined figure.

Rounding rules:

- Tax is rounded to the smallest currency unit (e.g. 1 UGX).
- Net is derived as gross minus tax, not separately rounded — so net + tax = gross to the unit.
- The rounding direction is set per entity and never changed without a documented policy change.

The tax code on the source document carries the rate, the jurisdiction, the effective period, and a reference to the verified rate in the source register.

## Reverse charge, zero-rated, exempt, deemed VAT

- **Standard-rated:** as above.
- **Zero-rated:** tax line posts zero to Output VAT (or Input VAT), but a tax line still exists for return-pack completeness. The tax code identifies it as zero-rated.
- **Exempt:** no tax line; the tax code identifies the supply as exempt; the supply is reported in the appropriate return-pack box (exempt sales).
- **Reverse-charge import of services:** the system posts both an Output VAT (notional, on Output VAT Control) and an Input VAT (on Input VAT Control, if input-recovery applies) in the same journal, net effect zero, with the gross transaction split for return-pack mapping.
- **Deemed VAT (where applicable in country extension):** posted explicitly to a Deemed VAT control account, never netted into operating expenses.

## Withholding tax

The buyer's WHT on a supplier invoice is posted to **WHT Payable**. The payment to the supplier reduces AP by the gross less WHT, increases Bank or Mobile Money by the net amount paid, and leaves the WHT in **WHT Payable** until remittance to the authority. The supplier receives a WHT certificate, which the system can generate from the WHT subledger.

## PAYE, NSSF, and other payroll deductions

Each statutory payroll deduction posts to its dedicated liability control account. The payroll subledger maintains the per-employee history; the GL holds only the control balances. At remittance, the system clears the liability against Bank or Mobile Money and produces the statutory schedule for the authority filing.

## Return-ready packs

A return pack is an authority-specific, period-specific bundle. It contains:

| Item | Description |
|---|---|
| `jurisdiction` | Country and authority (e.g. Uganda — URA). |
| `taxpayer-identity` | TIN, legal name, branch / point of presence. |
| `filing-period` | Period start, period end, due date. |
| `return-type` | VAT monthly, PAYE monthly, WHT monthly, income tax annual, NSSF monthly, … |
| `template-version` | The verified version of the authority's return template currently in use. |
| `template-source` | Authority URL or document reference plus retrieval date. |
| `ledger-source` | Map from each return-pack line to the CoA accounts and subledger entries used to populate it. |
| `tax-codes` | The tax codes contributing to the pack, with the verified rate and effective period. |
| `source-documents` | Underlying invoices, credit notes, receipts, WHT certificates, payroll registers, payment slips. |
| `evidence-pack` | All supporting evidence in a single bundle for download. |
| `reviewer-signoff` | Accountant + Tax reviewer sign-off log. |
| `open-gaps` | Any unresolved verification gaps or filing caveats. |
| `submission-acknowledgement` | Where applicable — the authority's acknowledgement after filing. |

The system **produces** the pack. Final filing happens in the authority portal unless an authority-published API/schema is verified and integrated (see Open Gaps in the master doctrine).

## EFRIS (Uganda) and eTIMS (Kenya)

For e-invoicing regimes, the system produces invoices in the authority-required format and obtains the authority-issued fiscal number / FDI per invoice. The fiscal number is stored on the source document and on the journal line; reversals (credit notes) carry the linked original fiscal number; reconciliation against the authority's e-invoicing record is a daily or weekly reconciliation, depending on the country extension.

EFRIS/eTIMS integration defaults are not hardcoded. Every integration constant (endpoint, certificate, return-line mapping) is governed by the source register and verified-current before final use.

## Source register entries for tax

Every tax rate, threshold, and template version recorded in the system has a row in the source register:

| Column | Example |
|---|---|
| `topic` | Uganda VAT standard rate. |
| `value-or-rule` | Verified-current value. |
| `source-url-or-doc` | URA authority page or gazette reference. |
| `source-tier` | Tier-1 authority. |
| `date-accessed` | YYYY-MM-DD. |
| `verifier` | Named human or named agent run. |
| `output-affected` | Sales tax codes, VAT return pack, EFRIS validation. |
| `expiry-or-recheck` | Per `live-rate-verification-protocol.md`. |
| `state` | `verified-current`, `pass-with-caveats`, `blocked`, `draft`. |

## Forbidden patterns

- Single gross figure posted to a revenue or expense account.
- Tax included in the same line as net.
- Tax codes without an effective period.
- Authority return templates copied into the system without a verified version reference.
- Hardcoded VAT, PAYE, NSSF, WHT rates in code, configuration, or templates.
- Authority filing claimed as automated when only the pack is produced.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
