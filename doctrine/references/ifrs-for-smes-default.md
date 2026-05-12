# IFRS for SMEs — Practical Default

IFRS for SMEs is the practical default for the typical Chwezi client. This file lists the sections that drive most of the engineering, configuration, and reporting decisions.

## Why IFRS for SMEs by default

Most Chwezi clients are private companies, NGOs, schools, clinics, retailers, agribusinesses, and hospitality operators with no public accountability. For these clients the simplifications in IFRS for SMEs (cost-based PPE, no comprehensive impairment testing, simplified financial instruments, simplified income tax, no segment reporting, no EPS, no interim reporting) reduce build, audit, and operating cost without losing the IFRS conceptual framework.

## Sections that drive build decisions

| Section | Topic | Build / config implication |
|---|---|---|
| 2 | Concepts and pervasive principles | Recognition criteria for assets, liabilities, income, expenses. |
| 3 | Financial statement presentation | Statement set and minimum line items. |
| 4 | Statement of financial position | CoA statement-group taxonomy. |
| 5 | Statement of comprehensive income and income statement | Income statement structure; OCI handling. |
| 6 | Statement of changes in equity / statement of income and retained earnings | SCE generator. |
| 7 | Statement of cash flows | SCF generator; direct or indirect method choice. |
| 8 | Notes to the financial statements | Notes templates and disclosure register. |
| 9 | Consolidated and separate financial statements | Multi-entity book consolidation. |
| 10 | Accounting policies, estimates and errors | Policy register, prior-period restatement workflow. |
| 11 | Basic financial instruments | Trade receivables, payables, bank loans, simple deposits. |
| 12 | Other financial instruments issues | Hedging, fair value through P&L. Most SMEs do not use 12. |
| 13 | Inventories | Cost formula choice (FIFO, weighted average — **never LIFO**), NRV, allocation of overheads. |
| 14 | Investments in associates | Equity method. |
| 15 | Investments in joint ventures | Cost or equity method choice. |
| 16 | Investment property | Cost or fair-value-through-P&L choice. |
| 17 | Property, plant and equipment | Cost model, depreciation methods, useful lives, residual values. |
| 18 | Intangible assets other than goodwill | Cost, amortisation, no internally generated brands. |
| 19 | Business combinations and goodwill | Purchase method, goodwill amortised over useful life (max 10 years if unable to estimate). |
| 20 | Leases | Lessee classification finance vs operating. Materially simpler than IFRS 16. |
| 21 | Provisions and contingencies | Provisions register, contingent disclosure workflow. |
| 22 | Liabilities and equity | Classification, compound instruments. |
| 23 | Revenue | Recognition for sale of goods, rendering of services, construction, interest, royalties, dividends. |
| 24 | Government grants | Performance / accrual model; grants linked to assets / income. |
| 25 | Borrowing costs | Expensed (default), capitalisation not permitted under SMEs. |
| 26 | Share-based payment | Equity-settled and cash-settled. |
| 27 | Impairment of assets | Inventories, other assets, goodwill. Simplified vs IAS 36. |
| 28 | Employee benefits | Short-term, post-employment (defined contribution and defined benefit), termination, other long-term. |
| 29 | Income tax | Current and deferred (temporary differences approach). |
| 30 | Foreign currency translation | Functional currency, presentation currency, translation. |
| 31 | Hyperinflation | Restatement (rare for typical clients). |
| 32 | Events after the end of the reporting period | Adjusting and non-adjusting. |
| 33 | Related-party disclosures | Related-party register and disclosure note. |
| 34 | Specialised activities | Agriculture, extractive activities, service concessions. **Agriculture is highly relevant to BIRDC and other agribusiness clients.** |
| 35 | Transition to IFRS for SMEs | First-time adoption procedure. |

## Key differences vs full IFRS that matter for build

| Topic | IFRS for SMEs | Full IFRS |
|---|---|---|
| Inventory cost formula | FIFO or weighted average. LIFO not permitted. | FIFO or weighted average. LIFO not permitted. |
| Borrowing costs | Expensed. | IAS 23 — capitalised on qualifying assets. |
| Development costs (internally generated intangibles) | Expensed. | IAS 38 — capitalised if criteria met. |
| Leases (lessee) | Operating vs finance classification. | IFRS 16 — single on-balance-sheet model. |
| Financial instruments | Sections 11 and 12, simplified. | IFRS 9 — full classification, ECL. |
| Investment property | Cost model OR fair value through P&L (entity choice for all). | IAS 40 — cost or fair value through P&L. |
| Goodwill | Amortised. Impairment indicators reviewed. | IAS 36 — annual impairment test only. |
| Income tax | Section 29 — temporary differences approach. | IAS 12 — substantially similar but more disclosure. |
| Revenue | Section 23 — risks-and-rewards-of-ownership / completion-stage. | IFRS 15 — five-step model. |
| Segment reporting | Not required. | IFRS 8 required for listed entities. |
| EPS | Not required. | IAS 33 required for listed entities. |

## When to escalate from IFRS for SMEs to full IFRS

The system promotes the client to full IFRS when any of the following becomes true:

- Listed debt or equity issued or planned.
- Bank covenant or donor agreement requires full IFRS.
- Insurance, banking, or pension regulator requires full IFRS.
- Group parent reports under full IFRS and consolidation requires it.
- Cross-border M&A or fundraising round contractually requires it.

Promotion is a policy-change event under Section 10 with full reviewer sign-off and a prior-period restatement assessment.

## Build implications summary

The default build set for a Chwezi SME client supports: Sections 2–11, 13, 17, 18, 20 (operating-lease default), 21, 23, 24, 27, 28 (DC default), 29, 30, 32, 33. Sections 9 (consolidation), 14, 15, 16, 19, 22, 26, 31, 34 are opt-in feature modules switched on by client profile. Section 34 agriculture is the standard module for agribusiness clients (see the `ias-agriculture` skill).

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
