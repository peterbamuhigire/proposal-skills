# Worked Example — Reconciliation Evidence Pack

A bank reconciliation evidence pack for May 2026, Stanbic UGX account.

## Pack contents

| File | Purpose |
|---|---|
| `bank-statement-2026-05.pdf` | The bank's PDF statement as downloaded from the Stanbic portal, with retrieval timestamp and verifier identity in the pack manifest. |
| `bank-feed-2026-05.csv` | The structured bank feed used by the system, with checksum and date of import. |
| `ledger-detail-1100-2026-05.csv` | All journal lines posted against 1100 Bank — Stanbic UGX during the period. |
| `reconciliation-2026-05.csv` | The reconciliation worksheet: bank rows, ledger rows, match status, ageing. |
| `exceptions-2026-05.csv` | Unresolved items at sign-off, with ageing and assignee. |
| `manifest.yaml` | Period, owner, preparer, reviewer, status, signatures. |

## Manifest example

```yaml
period: "2026-05"
entity: "Chwezi Demo Ltd"
account_code: "1100"
account_name: "Bank — Stanbic UGX"
currency: "UGX"
opening_balance_ledger: 12_345_000
opening_balance_bank: 12_345_000
closing_balance_ledger: 18_780_500
closing_balance_bank: 18_750_500
unreconciled_difference: 30_000

statement:
  source: "Stanbic portal"
  retrieved_at: "2026-06-02T08:31:00+03:00"
  retrieved_by: "Jane Doe (Accountant)"
  archive_path: "evidence/bank-statement-2026-05.pdf"

feed:
  source: "Stanbic CSV export"
  imported_at: "2026-06-02T08:35:00+03:00"
  imported_by: "Jane Doe (Accountant)"
  checksum_sha256: "<hash>"

reconciliation:
  matched_count: 142
  partial_match_count: 3
  exception_count: 4
  unmatched_count: 1

exceptions:
  - id: EX-2026-05-001
    description: "Bank charge UGX 30,000 on 2026-05-28, no ledger entry."
    resolution: "Post bank charge journal (J-...); included in this period."
    age_days: 5
    assignee: "Jane Doe"

  - id: EX-2026-05-002
    description: "Inbound transfer UGX 1,200,000 from MTN MoMo settlement; ledger entry pending."
    resolution: "Match against mobile-money settlement clearing once provider statement received."
    age_days: 2
    assignee: "Jane Doe"

  - id: EX-2026-05-003
    description: "Cheque 000456 cleared bank but ledger shows status 'awaiting-clearance'."
    resolution: "Update cheque clearance status; auto-match expected next run."
    age_days: 1
    assignee: "Jane Doe"

  - id: EX-2026-05-004
    description: "Standing-order debit UGX 750,000 (rent) posted in ledger but missing from bank statement."
    resolution: "Suspected timing — bank will post on 2026-06-01; carry as outstanding."
    age_days: 1
    assignee: "Jane Doe"

sign_off:
  preparer: "Jane Doe (Accountant)"
  preparer_signed_at: "2026-06-02T11:15:00+03:00"
  reviewer: "Peter Bamuhigire (Controller)"
  reviewer_signed_at: "2026-06-02T11:42:00+03:00"
  release_state: "pass-with-caveats"
  caveats:
    - "EX-2026-05-001 will post in 2026-06 (bank charge journal)."
    - "EX-2026-05-002 awaiting provider statement; expected within 5 working days."

evidence_pack:
  files:
    - "bank-statement-2026-05.pdf"
    - "bank-feed-2026-05.csv"
    - "ledger-detail-1100-2026-05.csv"
    - "reconciliation-2026-05.csv"
    - "exceptions-2026-05.csv"
    - "manifest.yaml"
  pack_archive: "evidence/recon-1100-2026-05.zip"
  pack_archive_sha256: "<hash>"
```

## Print-fidelity expectation

When the controller prints the reconciliation, a single-page summary appears with: opening balance, closing balance, unreconciled difference, exception count by ageing bucket, sign-off boxes. The exception listing prints on subsequent pages. Status chips are rendered with text labels; the print remains correct in monochrome.

## How this maps to release state

The reconciliation is `pass-with-caveats` because two exceptions carry forward into June. A `pass` requires zero outstanding exceptions or a documented waiver per exception. A `fail` is recorded when the unreconciled difference is material to the entity (threshold configured at entity level) or when ageing exceeds the configured maximum without an assignee or plan.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
