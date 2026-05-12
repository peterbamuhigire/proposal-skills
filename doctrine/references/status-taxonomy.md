# Status Taxonomy

The controlled status vocabulary. Used everywhere — web, mobile, print, exports, audit logs, integrations.

## Universal statuses

| Status | Semantic colour | Meaning |
|---|---|---|
| `draft` | warning amber (muted) | Captured but not yet submitted. Editable. Not in the ledger. |
| `awaiting-approval` | warning amber | Submitted; pending maker-checker or threshold approval. Not in the ledger. |
| `posted` | gain green | Committed to the ledger. Editable only by reversal. |
| `reversed` | reversed purple | A reversal exists against this record. Original is preserved. |
| `matched` | gain green | Reconciled to its counterparty (bank statement row, supplier invoice, customer receipt, …). |
| `unmatched` | loss red | No reconciliation counterparty found. |
| `exception` | loss red | Match attempted but failed validation (amount mismatch, date mismatch, missing reference). |
| `locked` | locked grey | Period is locked. Editing affordances disappear. |
| `released` | gain green | Output / report / pack released after sign-off. |

## Domain-specific statuses (build on the universal set)

| Domain | Status | Meaning |
|---|---|---|
| Approval workflow | `requested` | A request has been made (for a refund, period reopen, journal reversal). |
| Approval workflow | `approved` | Request approved. Action will follow. |
| Approval workflow | `rejected` | Request rejected. |
| Reconciliation | `partial-match` | Match found but only partial (split required). |
| Reconciliation | `pending-evidence` | Match found but evidence file missing. |
| Tax | `submitted` (to authority) | Pack submitted to authority portal. |
| Tax | `acknowledged` | Authority acknowledgement received. |
| Tax | `filed` | Authority filing complete. |
| EFRIS / eTIMS | `efris-submitted` / `etims-submitted` | Submitted to authority e-invoicing system. |
| EFRIS / eTIMS | `efris-confirmed` / `etims-confirmed` | Authority confirmed. |
| EFRIS / eTIMS | `efris-rejected` / `etims-rejected` | Authority rejected. |
| Migration | `mapped` | Legacy account mapped to Chwezi CoA. |
| Migration | `tie-out-ok` | Subledger tie-out matched. |
| Migration | `tie-out-fail` | Subledger tie-out failed. |
| Migration | `suspense` | Routed to migration suspense pending resolution. |
| Migration | `sign-off` | Migration sign-off recorded. |
| Period | `open` / `soft-closed` / `locked` / `reopened` / `archived` | See `ledger-invariants.md` §5. |
| Inventory | `received` / `posted` / `counted` / `adjusted` / `written-off` | Stock lifecycle. |

## Rendering rules

- Always include the status **word** alongside any colour.
- Use the same chip style across web, mobile, and print.
- Use sentence-case labels (`Awaiting approval`, not `AWAITING APPROVAL`).
- Internationalisation: store the status code (kebab-case) on the wire; render the localised label at the UI layer.
- Sort order in lists: actionable first (`exception`, `unmatched`, `awaiting-approval`), then `draft`, then `posted` / `matched`, then `reversed` / `locked` / `archived`.

## Transition rules

- `draft → awaiting-approval → posted` is the standard maker-checker path.
- `posted → reversed` is the only edit path on a posted record.
- `unmatched → matched` and `unmatched → exception → matched / written-off` are the reconciliation paths.
- `open → soft-closed → locked → archived` is the period-state path. `locked → reopened → locked` is permitted with sign-off.
- No state may skip backwards through the lifecycle except via reversal + correction.

## Forbidden

- Free-text statuses outside this set.
- Numeric status codes (`status = 1`, `status = 2`).
- Status booleans (`is_posted`, `is_locked`) used as the only state indicator.
- Status colours rendered without the label.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
