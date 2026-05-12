# Worked Example — Reversal Pattern

An accountant must correct a supplier bill that was posted with the wrong supplier. The bill was already posted yesterday and is in an open period.

## Forbidden approach

- Edit the journal line and change the supplier.
- Delete the journal.
- Re-save the journal under a different supplier.

All three are blockers under the ledger invariants.

## Required approach: reversal + new posting

### Step 1 — Reverse the original

A new journal is posted that exactly reverses the original by amount and sign, linked to the original by `original-journal-id`.

Original (J-2026-05-11-0123):

| Line | Debit | Credit | Account | Subledger |
|---|---:|---:|---|---|
| 1 | 1,000,000 | | 6100 Rent — Premises | |
| 2 | | 1,000,000 | 2000 Trade Payables Control | Supplier: WRONG SUPPLIER LTD |

Reversal (J-2026-05-12-0901, links to J-2026-05-11-0123):

| Line | Debit | Credit | Account | Subledger |
|---|---:|---:|---|---|
| 1 | | 1,000,000 | 6100 Rent — Premises | |
| 2 | 1,000,000 | | 2000 Trade Payables Control | Supplier: WRONG SUPPLIER LTD |

Reversal metadata:

| Field | Value |
|---|---|
| Reason code | `wrong-supplier-master` |
| Reason free-text | "Posted under WRONG SUPPLIER LTD; correct supplier is RIGHT SUPPLIER LTD." |
| Actor | Accountant Jane Doe |
| Role | Accountant |
| Date / time | 2026-05-12 09:31 EAT |
| Original journal | J-2026-05-11-0123 |
| Reversal type | Full |
| Period | 2026-05 (Open) |
| Approval | Maker-checker required; Controller approved at 09:32 EAT. |

The reversal restores the AP open item against WRONG SUPPLIER LTD (which was previously settled by this bill) by resurrecting it; if a payment had been made against the original, that payment is also reversed as a separate linked journal.

### Step 2 — New posting

The accountant posts the corrected bill (J-2026-05-12-0902):

| Line | Debit | Credit | Account | Subledger |
|---|---:|---:|---|---|
| 1 | 1,000,000 | | 6100 Rent — Premises | |
| 2 | | 1,000,000 | 2000 Trade Payables Control | Supplier: RIGHT SUPPLIER LTD |

The new posting carries `correction-of` = J-2026-05-12-0901 (the reversal), which transitively links to the original. The lineage is: J-2026-05-11-0123 (original, status `reversed`) ← J-2026-05-12-0901 (reversal) ← J-2026-05-12-0902 (correction).

### Audit-log entries

| Time | Actor | Action | Object | Notes |
|---|---|---|---|---|
| 2026-05-12 09:30 | Jane Doe (Accountant) | request reversal | J-2026-05-11-0123 | Reason: wrong-supplier-master |
| 2026-05-12 09:31 | Jane Doe (Accountant) | post reversal | J-2026-05-12-0901 | Awaiting approval |
| 2026-05-12 09:32 | Peter Bamuhigire (Controller) | approve reversal | J-2026-05-12-0901 | Posted |
| 2026-05-12 09:33 | Jane Doe (Accountant) | post correction | J-2026-05-12-0902 | Awaiting approval |
| 2026-05-12 09:34 | Peter Bamuhigire (Controller) | approve correction | J-2026-05-12-0902 | Posted |

## Reversal across a locked period

If the original journal is in a locked period and the error is discovered later:

- The reversal cannot post in the locked period.
- The reversal posts in the **current open period** as a prior-period adjustment.
- The audit log records the lineage and the prior-period adjustment flag.
- If the error is material under IAS 8 / Section 10, the policy register flags the restatement and the reviewer routes it through the prior-period restatement workflow.

## Reversal across an archived period

Archived periods accept no journals, even prior-period adjustments. Corrections appear only in the current open period with explicit reference to the archived original and a note in the financial statements where material.

## UI presentation

- The original record shows the status chip `reversed` with a link to the reversal.
- The reversal shows status `posted` and a link back to the original and forward to the correction.
- The correction shows status `posted` and a link back to the reversal and the original.
- No `Delete` button anywhere on any of the three records.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
