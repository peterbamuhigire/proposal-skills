# Role-Conditioned Shell

The Chwezi UI varies its chrome by role. Same data underneath; different presentation, density, and affordances on top.

## Roles

| Role | Surface | Default density | Default landing |
|---|---|---|---|
| Cashier | Workflow | Comfortable | POS or receive-payment |
| Clerk | Workflow | Comfortable | Sales / purchases entry |
| Manager (branch / shop) | Workflow + light ledger | Comfortable | Branch dashboard |
| Accountant | Ledger | Compact | Trial balance / journal listing |
| Controller | Ledger | Compact | Close board |
| Auditor | Ledger (read-only) | Compact | Audit export index |
| CFO / Finance Lead | Ledger summary + management pack | Compact | Management pack |
| Tax Reviewer | Ledger filtered to tax control accounts | Compact | Tax-return pack list |
| Payroll Officer | Workflow | Comfortable | Payroll run board |
| Inventory Manager | Workflow + inventory ledger | Comfortable | Stock movement board |
| Administrator | Configuration only — no automatic accounting approval | Compact | Configuration board |

## Top bar (always present)

```
[ Entity ▾ ]  [ Book ▾ ]  [ Period: <state-chip> ]  [ Role ]  [ Environment ]    [ Quick action ▾ ]  [ Notifications ]  [ User ]
```

- **Entity:** the legal entity context. Multi-entity users switch here. Single-entity users see this as a label only.
- **Book:** the reporting framework (`IFRS for SMEs` / `IFRS` / `Tax book` / …). Most users see one book. Multi-book users (typically Controllers and CFOs) switch here.
- **Period:** chip in the semantic colour of the current period state (`open` neutral, `soft-closed` amber, `locked` grey, `reopened` info-blue, `archived` grey).
- **Role:** the role the user is currently acting in. Users with multiple roles switch here; the audit log records the role used.
- **Environment:** `prod`, `staging`, `test`. Non-prod has a coloured environment banner across the whole top bar.

## Permissions matrix (abridged)

| Action | Cashier | Clerk | Manager | Accountant | Controller | Auditor | Admin |
|---|---|---|---|---|---|---|---|
| Record sale / receive payment | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| Record purchase / pay supplier | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| Refund / credit note | request only | request only | approve under threshold | approve | approve | ✗ | ✗ |
| Manual journal | ✗ | ✗ | ✗ | ✓ (within rules) | ✓ | ✗ | ✗ |
| Reverse posted journal | ✗ | ✗ | request only | ✓ | ✓ | ✗ | ✗ |
| Close period (soft) | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | ✗ |
| Close period (lock) | ✗ | ✗ | ✗ | request only | ✓ | ✗ | ✗ |
| Reopen period | ✗ | ✗ | ✗ | ✗ | ✓ + approver | ✗ | ✗ |
| Edit CoA | ✗ | ✗ | ✗ | request only | ✓ | ✗ | ✗ |
| Edit tax codes | ✗ | ✗ | ✗ | request only | ✓ + tax reviewer | ✗ | ✗ |
| Edit roles / permissions | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ + Controller approval |
| Drill from report → source | filtered by their data | filtered | filtered | full | full | full | ✗ |
| Export audit pack | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✗ |

Admin is **not** an accounting approver. Administrative actions that affect accounting (role assignment, period reopen, tax-code change) require the relevant finance role's approval in addition to the admin action.

## Surface contracts

### Workflow surface

- Bottom nav with at most 4 destinations: Home, Record (primary), Match / Reconcile, More.
- Each screen has at most one primary action.
- Lists and detail screens use cards or large rows.
- Forms collect business-event fields first; accounting detail (account selection, dimensions) is auto-derived by the posting service from the posting rule register.
- Status chip top-right on each card.

### Ledger surface

- Side nav (collapsible) with grouped destinations: Ledger, Subledgers, Reconciliations, Close, Reports, Tax, Migration, Configuration.
- Dense grid as primary content. Sticky column headers, sticky totals row, sticky filter row.
- Keyboard shortcuts: `j` / `k` row navigation, `Enter` open, `Esc` close, `Ctrl+S` save, `Ctrl+Enter` post, `/` focus search, `?` show shortcut help.
- Filter bar persistent. Filters can be saved as views per user.
- Bulk actions on selected rows with strict per-action permission check.

### Read-only auditor surface

- Same as ledger surface but every action is disabled and replaced with `View` / `Drill` / `Export`.
- Audit-log filter is always visible.
- Export is watermarked with auditor identity.

## Last-reviewed footer

Every shell route renders a small footer line: `Doctrine version: <semver> · Last reviewed: <date> · Next review due: <date> · Build: <build-id>`.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
