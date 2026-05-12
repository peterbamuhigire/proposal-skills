# Design System — Finance & Accounting UI

The Chwezi finance/accounting design system. This is the single source of design tokens and component contracts that the four engines and all client products must honour. Derived from the cross-industry fintech research synthesis plus the accounting-specific constraints the consumer-fintech literature does not address.

## Foundational principles

1. **Trust is paid for in typographic discipline, not graphics.** Consistent spacing, restrained colour, deliberate type weight, zero visual noise in transaction flows.
2. **Two surface modes.** Workflow surface (cashiers / clerks / managers / family-business users) is minimal, large touch targets, one primary action per screen. Ledger surface (accountants / controllers / auditors) is Bloomberg-grade: dense grids, keyboard-first, filterable, exportable, drillable.
3. **Role-conditioned shell.** Top bar always shows: entity · book · period state · role · environment (prod / staging / test). Always.
4. **Drilldown as a first-class primitive.** Every figure is clickable. Report line → account → journal → line item → source document → evidence file → audit event.
5. **Status taxonomy used consistently.** See `status-taxonomy.md`.
6. **Semantic colour.** Green and red are signals only. Never brand. Never CTA. Never decoration.
7. **Light is the default for SME clients in East Africa.** Daylight kiosks, paper invoices, printed evidence. Dark is opt-in.
8. **Print fidelity is P0.** See `print-fidelity.md`.
9. **Low-bandwidth, low-spec Android is the harder constraint than desktop.** Optimistic post + reconcile; offline drawer close; no silent loss.

## Design tokens

### Typography

| Token | Value | Use |
|---|---|---|
| `font-sans` | One sans-serif family with tabular numerals. Suggested: Inter, IBM Plex Sans, or system stack. | Body, labels, UI chrome. |
| `font-mono` | One monospaced family with tabular numerals. | Account codes, journal IDs, idempotency keys, hash references. |
| `numerals` | `tabular-nums` everywhere money appears. | All ledger surfaces, reports, prints. |
| `scale-1` … `scale-7` | 11 / 12 / 14 / 16 / 18 / 24 / 32 (px). | Type scale. Max 7 steps. |
| `weight-regular` | 400. | Body. |
| `weight-medium` | 500. | Labels, secondary headings. |
| `weight-semibold` | 600. | Primary headings, account balances. |
| `weight-bold` | 700. | Reserved for amounts on totals rows and signed totals. |

### Spacing

| Token | Value | Use |
|---|---|---|
| `space-base` | 4 px. | Base unit. |
| `space-chrome` | 8 px rhythm. | Application chrome (top bar, side nav, dialogs). |
| `space-table` | 4 px row rhythm in compact mode, 8 px in comfortable mode. | Ledger grids. |
| `space-form` | 12 px between fields, 24 px between sections. | Forms. |

### Colour

Restraint over energy.

| Token | Use |
|---|---|
| `brand-primary` | Primary CTAs, selection states. Used sparingly. |
| `neutral-bg` | Default background. |
| `neutral-fg` | Default foreground. |
| `neutral-muted` | Secondary text, dividers. |
| `gain` (semantic green) | Positive amounts, matched / posted state, profit. Never used for chrome or CTAs. |
| `loss` (semantic red) | Negative amounts, unmatched / failed / overdue / rejected state, loss. Never used for chrome or CTAs. |
| `warning` (semantic amber) | Awaiting approval, ageing approaching threshold, draft. |
| `info` (semantic blue) | Information chips, links, system notes. |
| `locked` (semantic grey) | Locked period, archived, read-only. |
| `reversed` (semantic purple or muted secondary) | Reversed journals, credit notes against an original. |

### Density modes

| Mode | Use |
|---|---|
| `comfortable` | Workflow surface. Larger row height, larger touch targets. |
| `compact` | Ledger surface. Dense grids. |

Only two modes. No infinite density slider.

### Elevation

Flat by default. Elevation reserved for transient surfaces (menus, dialogs, toasts). Posted records, reports, and forms are flat.

### Motion

| Token | Value | Use |
|---|---|---|
| `motion-fast` | ≤ 120 ms. | Hover, focus. |
| `motion-default` | ≤ 200 ms. | Open / close, slide. |
| `motion-never` | 0 ms. | Numbers on posted records. They never animate. |

### Iconography

One stroke weight. Abstract over decorative. Never coloured. Icons are signposts, not art.

## Component contracts

### Money cell

A money cell renders an amount with:

- Tabular numerals
- Currency code as a small adjacent label (unless the column header carries it)
- Negative sign in semantic `loss` colour, positive sign in semantic `gain` colour only where the amount is signed in business meaning (P&L lines, variance columns). Plain neutral colour in pure ledger columns.
- Decimal alignment in tables
- A drilldown affordance (hover underline, click to open source)

### Net / Tax / Gross triplet

Where VAT-inclusive amounts are displayed, three adjacent cells appear: net, tax, gross. Never collapsed into one cell. Never with tax in a tooltip. The triplet is preserved on prints.

### Status chip

A short label rendered against a semantic background. Uses only the status taxonomy from `status-taxonomy.md`. Same colour and shape in web, mobile, and print.

### Top bar

Always shows: entity, book, period state, role, environment. Period state is a chip with semantic colour. If the period is locked, all editing affordances on the page disappear and a "request reopen" affordance appears.

### Reconciliation triage

Two-pane layout:

| Column | Content |
|---|---|
| Left | Imported items (bank statement rows, mobile-money statement rows, POS Z-report rows). |
| Centre | Match / unmatch / exception / split actions. |
| Right | Ledger items (posted journals on the relevant control account). |
| Top | Ageing summary, filters, evidence pack export. |
| Bottom | Pagination, status counts. |

Unmatched items always show ageing. Exceptions always show reason and assignee.

### Drilldown breadcrumb

When the user drills, a breadcrumb shows: `Report → Account → Journal → Line → Source → Evidence`. The user can step back at any level.

### Posting screen

- Header: business event ("Receive payment from customer" or "Record supplier bill"), date, source document reference.
- Body: lines (amount in net / tax / gross triplet where applicable, account from CoA, dimensions, description).
- Evidence dropzone above the Save button.
- Audit-log preview: who, when, what.
- Status: `draft` until submitted, then `awaiting-approval` (if maker-checker is on), then `posted`.

No `Delete` button. Posted records use `Reverse`.

### Report header

Every report carries: entity, book, period (and comparative period), framework (`IFRS for SMEs` / `IFRS` / …), preparer, reviewer, status, generated-at, print stylesheet trigger.

### Mobile workflow shell

- Bottom nav with at most 4 destinations.
- Top bar always visible (sticky).
- One primary action per screen.
- Touch targets ≥ 44 px.
- Skeleton + optimistic post + reconcile on flaky connectivity.

## Accessibility

- WCAG AA contrast on all text and meaningful UI.
- Keyboard-first ledger grids. Every cell reachable by keyboard; every action available without a pointer.
- Screen-reader labels on every numeric cell: account name, currency, amount, sign.
- Focus rings are visible and persistent.
- Reduced-motion preference respected (motion goes to zero).
- No colour-only signal. Colour is paired with text or icon for every status.

## Internationalisation

- All currency symbols / codes per locale; tabular numerals preserved.
- Date formats per locale; ISO date stored on the wire.
- Number formats per locale; never embed locale-specific separators in stored values.
- Right-to-left support not required for current markets but tokens designed to allow it.

## Tooling

The design system ships as:

- A token JSON file (consumed by Tailwind / CSS variables / mobile theming).
- A storybook of component contracts (in the `finance-ui-pattern-library` skill).
- A print stylesheet template.
- A figma library (separately maintained).

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
