# Terminology Glossary

Controlled terminology used across all four Chwezi skill engines. Use these terms verbatim. Synonyms are noted but discouraged in published artefacts.

| Term | Canonical meaning |
|---|---|
| Accounting boundary | The service, workflow, permission, and review boundary where operational events become financial records. |
| Posting service | Approved service that validates account mapping, tax handling, period state, permissions, evidence, idempotency, and balanced journal output before committing financial records. |
| Journal | A balanced set of debits and credits posted by a posting service. |
| Journal line | A single debit or credit row within a journal. |
| Subledger | An auxiliary record of detail for a control account (AR, AP, inventory, fixed assets, payroll, …). |
| Control account | A CoA account whose balance ties to a subledger, clearing process, statutory schedule, or reconciliation pack. |
| Clearing account | Temporary CoA account used to bridge timing between operational capture and settlement or reconciliation. |
| Suspense account | An account holding items pending resolution. Use only with an ageing plan; never as a routine destination. |
| Period state | One of `open`, `soft-closed`, `locked`, `reopened`, `archived`. |
| Reversal | A new journal that reverses an earlier journal by amount and sign, linked to the original. |
| Correction | A new journal that re-states an effect after a reversal, linked to both the reversal and the original. |
| Live-rate verification | Current-source verification for tax, payroll, statutory, regulator, exchange-rate, EFRIS, return-format, and threshold values before operational use. |
| Source register | The system-of-record for all verifiable values, including value, source, date accessed, verifier, expiry, and state. |
| Tax-return pack | Authority-specific period bundle with mapped tax accounts, source transactions, filing period, return-template version, evidence, reviewer sign-off, and verification status. |
| Evidence pack | Source documents, approvals, reconciliations, workpapers, exports, and audit trail sufficient for review. |
| Professional review | Sign-off by Accountant, Controller, CFO, Tax reviewer, Internal Auditor, or external professional. |
| Drilldown chain | Report line → account → journal → journal line → source document → evidence file → audit event. |
| Workflow surface | UI surface used by cashiers, clerks, managers, and family-business users. Plain business words, large touch targets, one primary action per screen. |
| Ledger surface | UI surface used by accountants, controllers, and auditors. Dense grids, keyboard-first, drillable, exportable. |
| Role-conditioned shell | UI chrome that varies by role: top bar shows entity, book, period state, role, environment. |
| Status taxonomy | The controlled set: `draft`, `awaiting-approval`, `posted`, `reversed`, `matched`, `unmatched`, `exception`, `locked`. |
| Country extension | Country-specific overlay on the doctrine, providing authority list, return templates, payroll schedule, e-invoicing, CoA overlay, and verification cadence. |
| Quality gate | The release gate run on any finance-scope artefact. Returns `pass`, `pass-with-caveats`, or `fail`. |
| Backbone (CoA) | The doctrine that the Chart of Accounts drives postings, control accounts, reporting groups, dimensions, permissions, and audit evidence. |
| Cutover | The named conversion date at which legacy data crosses into the Chwezi system. |
| Opening balances | The trial balance and subledger balances at cutover. |
| Migration suspense | Cutover-only clearing account that must reach zero (or be formally waived with sign-off) at acceptance. |
| First close | The first month-end close after go-live. Requires extra reviewer support. |
| VAT-inclusive | A price quoted gross of VAT; decomposed by the posting service into net and tax. |
| VAT-exclusive | A price quoted net of VAT. |
| Reverse charge | Self-accounting for VAT on imported services. |
| Zero-rated | Subject to VAT at the zero rate. Still appears on the VAT return. |
| Exempt | Outside the scope of VAT. Reported separately on the VAT return. |
| Withholding tax (WHT) | Tax withheld by the buyer on payments to the supplier and remitted to the authority. |
| Output VAT | VAT collected on sales. |
| Input VAT | VAT incurred on purchases, recoverable subject to rules. |
| PAYE | Pay-As-You-Earn tax on employment income. |
| NSSF | National Social Security Fund (Uganda); similar funds exist by country extension. |
| EFRIS | URA's electronic fiscal receipting and invoicing system. |
| eTIMS | KRA's electronic tax invoice management system. |
| ECL | Expected credit loss (IFRS 9). |
| ROU asset | Right-of-use asset under IFRS 16. |
| RCSA | Risk control self-assessment. |
| Maker-checker | Two-person rule on a transaction class. |
| Segregation of duties (SoD) | Controls preventing one role from completing an end-to-end risky transaction alone. |
| Reconciliation triage | Two-pane reconciliation UI: imported items on one side, ledger items on the other, with match / unmatch / exception in the middle and ageing always visible. |
| Print fidelity | The doctrine that every report and evidence pack renders correctly on A4, black-and-white, with auditor sign-off boxes. |

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
