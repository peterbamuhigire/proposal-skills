# Ledger Invariants

The non-negotiable rules that every ledger implementation, every posting service, every test suite, and every reviewer enforces.

## 1. Posting boundary

Feature modules (POS, payroll, AR, AP, inventory, banking, mobile money, grants, fixed assets, tax engine, intercompany) submit **accounting events** (business commands) to an approved **posting service**. They do not write to journal headers or journal lines directly.

The posting service is the only code path that:

- Validates account mapping against the Chart of Accounts.
- Applies tax treatment.
- Applies dimensions (cost centre, project, grant, branch, …).
- Checks period state.
- Checks role permissions.
- Validates evidence attachment requirements.
- Applies idempotency keys.
- Produces a balanced journal in each currency.
- Writes to the ledger inside a single transaction.
- Emits the audit event.

Any code that inserts into `journal_headers` or `journal_lines` (or the equivalent named tables) outside this service is a blocker finding under the quality gate.

## 2. Double entry

Every posted journal balances debits and credits, separately for each currency and for each book. Multi-currency journals carry a translation row to the reporting currency. Rounding differences route to a designated rounding clearing account with a hard tolerance (set per entity, default ≤ 0.50 of the smallest currency unit) and an audit-log entry whenever a rounding row appears.

## 3. Immutability

A posted journal is not edited and not deleted through ordinary application paths. The only corrections are:

- **Reversal:** a new journal that reverses the original by amount and sign, linked to the original.
- **Correction:** a new journal that re-states the effect, linked to both the reversal and the original.

Admin-level deletion exists only as a database-level operation, requires Controller + CFO sign-off, leaves an immutable audit-log entry, and is restricted to fraud, data-protection erasure orders, or court orders.

## 4. Reversal

A reversal links to the original transaction and preserves:

- Reason code (selected from a controlled list; free-text reason is also recorded).
- Actor (named human, not a service account, unless the service account is the documented owner of an automated reversal class).
- Date and timestamp.
- Original journal ID.
- Reversal type: full or partial.
- Effect on subledgers (AR/AP open-item resurrection, inventory layer restoration, tax-code re-application).

Reversals of cross-period journals respect period state: a reversal posted into a locked period is rejected or routed through the period-reopen workflow.

## 5. Period state

Every period (month, quarter, year) carries a state:

| State | Meaning | Posting behaviour |
|---|---|---|
| `open` | Period accepts ordinary posting. | Posting allowed by all permitted roles. |
| `soft-closed` | Period closed for ordinary users; accountants and controllers may still post adjustments. | Posting requires `controller-adjustment` permission. |
| `locked` | Period locked. | Posting is rejected. Reopen workflow is required. |
| `reopened` | Period reopened for a bounded purpose, tracked. | Posting allowed; every entry tagged with the reopen reason. |
| `archived` | Period permanently locked and archived. | No posting under any circumstance; new corrections create a prior-period adjustment in the current open period. |

Period transitions are themselves audit-logged events with reason, approver, and timestamp.

## 6. Audit log

Every posting writes an audit-log row containing: actor identity (human + service), authentication context, request identifier, timestamp, before/after state, source document reference, evidence pack reference, journal ID, reversal/correction lineage, and posting service version.

The audit log is append-only. Even an admin role cannot edit or delete an audit-log row through any application path.

## 7. Idempotency

Posting commands carry an idempotency key. The posting service rejects:

- Duplicate keys with identical payloads (returns the prior result rather than re-posting).
- Duplicate keys with **different** payloads (rejects with an integrity error and writes an audit-log entry).

Idempotency keys are required on all integration-driven postings (POS Z-report close, payroll run commit, bank-feed import, mobile-money settlement).

## 8. Control-account tie-out

Subledger control accounts (AR control, AP control, Inventory control, VAT control, PAYE control, WHT control, NSSF control, Fixed-Assets cost and accumulated depreciation, Petty Cash, Cash on Hand, Bank, Mobile Money) reconcile to their subledger balance at every close and at migration cutover. A control-account variance is a blocker finding.

## 9. Evidence requirement

Every posting that requires evidence under the CoA evidence policy (typically supplier invoices, customer invoices, payroll registers, journal vouchers, bank statements, mobile-money statements, POS Z-reports, asset-purchase documents) has at least one attached evidence file (PDF, image, structured file) or a documented exception with reviewer sign-off.

## 10. Forbidden practices

- Reposting after edit: never. Only reversal + new posting.
- Soft-delete fields on journal lines: never.
- Cascading delete from a parent record that owns journals: never.
- Background "cleanup" jobs that purge posted journals: never.
- Storing tax amounts in line memos: never. Tax lines are first-class journal lines on governed tax control accounts.

## 11. Acceptance tests

Every consumer engine derives ledger acceptance tests from this file. See `../../skills/internal-controls-library/references/acceptance-tests.md` for the canonical test set.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
