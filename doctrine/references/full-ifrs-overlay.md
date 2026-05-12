# Full IFRS Overlay

When a Chwezi client is on full IFRS, this overlay describes the additional doctrine and build requirements that sit on top of the IFRS for SMEs baseline. Doctrine in the master file applies in both modes; this overlay only adds the differences.

## Trigger for full IFRS

See `ifrs-for-smes-default.md` for the promotion criteria. Once promoted, every artefact for the entity is labelled `Framework: IFRS`.

## Required standards modules

The following standards become first-class build modules:

| Standard | Topic | Module |
|---|---|---|
| IAS 1 | Presentation of financial statements | Presentation engine — primary statements, comparative period, going concern disclosure. |
| IAS 7 | Statement of cash flows | SCF generator with direct or indirect choice. |
| IAS 8 | Accounting policies, changes in accounting estimates and errors | Policy register, prior-period restatement workflow. |
| IAS 10 | Events after the reporting period | Subsequent-events workflow. |
| IAS 12 | Income taxes | Deferred tax module — see `ias-income-tax-deferred-tax` skill. |
| IAS 16 | Property, plant and equipment | PPE module with cost or revaluation model. |
| IAS 19 | Employee benefits | DC and DB modules; DB plan obligation calculation routed to actuary. |
| IAS 20 | Government grants | Grants module — see `ias-government-grants` skill. |
| IAS 21 | Effects of changes in foreign exchange rates | Multi-currency module with translation. |
| IAS 23 | Borrowing costs | Capitalisation rule on qualifying assets. |
| IAS 24 | Related-party disclosures | Related-party register and disclosure note generator. |
| IAS 27 / 28 | Separate FS, associates | Equity method module. |
| IAS 32 / 39 (legacy) / IFRS 9 | Financial instruments | See `ifrs-financial-instruments` skill. |
| IAS 33 | Earnings per share | EPS calculator. |
| IAS 34 | Interim financial reporting | Interim pack generator. |
| IAS 36 | Impairment of assets | See `ias-impairment` skill. |
| IAS 37 | Provisions, contingent liabilities and contingent assets | See `ias-provisions-contingencies` skill. |
| IAS 38 | Intangible assets | With capitalisable development costs workflow. |
| IAS 40 | Investment property | Cost or fair-value model. |
| IAS 41 | Agriculture | See `ias-agriculture` skill. |
| IFRS 3 | Business combinations | Acquisition method, purchase price allocation, goodwill (annual impairment, no amortisation). |
| IFRS 5 | Non-current assets held for sale and discontinued operations | Held-for-sale classification, discontinued-operations presentation. |
| IFRS 7 | Financial instruments: disclosures | Risk disclosure pack. |
| IFRS 8 | Operating segments | Required for listed entities. |
| IFRS 9 | Financial instruments | ECL model, classification, hedge accounting. |
| IFRS 10 / 11 / 12 | Consolidation, joint arrangements, disclosure of interests | Consolidation engine. |
| IFRS 13 | Fair value measurement | Fair-value hierarchy and inputs. |
| IFRS 15 | Revenue from contracts with customers | Five-step model. See `ifrs-revenue-recognition` skill. |
| IFRS 16 | Leases | Single lessee model, right-of-use asset and lease liability. See `ifrs-leases` skill. |

## Module priority for build

Tier 1 (typically required): IAS 1, 7, 8, 10, 12, 16, 19, 21, 23, 24, 32/IFRS 9, 36, 37, 38, IFRS 15, IFRS 16.
Tier 2 (client-dependent): IAS 20, 28, 33, 34, 40, IFRS 3, 5, 7, 8, 10, 11, 12, 13.
Tier 3 (specialised): IAS 41 (agribusiness), IAS 26 (retirement benefit plans), IFRS 17 (insurance contracts — out of scope for typical SME).

## Disclosure burden

Full IFRS materially increases note-disclosure volume. The notes generator must support:

- Significant accounting policies note (much longer than SME equivalent).
- Critical judgements and estimates note.
- Financial-risk management disclosures (IFRS 7).
- Capital management disclosures (IAS 1).
- Related-party disclosures (IAS 24).
- Segment disclosures (IFRS 8) where applicable.
- Fair-value disclosures (IFRS 13) where applicable.

## Audit-ready pack

The audit-ready pack for full IFRS includes the SME pack plus: IFRS 9 ECL workings, IAS 36 impairment workings (annual goodwill test, indicator-based test for other assets), IFRS 16 lease working, IAS 12 deferred-tax computation, IFRS 7 disclosure inputs, IFRS 13 fair-value inputs, and IFRS 15 contract-level workings where revenue is complex.

## Forbidden patterns under full IFRS

In addition to the doctrine-level forbidden patterns:

- Goodwill amortisation (full IFRS uses annual impairment, not amortisation).
- Lessee operating-lease classification (IFRS 16 requires single on-balance-sheet model except for short-term and low-value exemptions).
- Borrowing costs expensed on qualifying assets (IAS 23 requires capitalisation).
- Development costs expensed where IAS 38 criteria are met.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
