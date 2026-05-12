# Uganda Compliance Caveats

Uganda is the home jurisdiction. This reference lists what the system must support for Uganda and what remains a live-verification target. **No statutory rate or threshold is fixed here.** All numeric values flow through the source register and the live-rate verification protocol.

## Authorities and source list

| Authority | Role |
|---|---|
| Parliament of Uganda | Statute (Income Tax Act, VAT Act, etc.) |
| Government Printer / Uganda Gazette | Gazette notices, finance acts, statutory instruments |
| Uganda Revenue Authority (URA) | VAT, PAYE, WHT, income tax, customs, excise, EFRIS |
| NSSF Uganda | National Social Security Fund |
| Bank of Uganda (BoU) | Exchange rates, banking regulation |
| ICPAU | Accounting framework guidance |
| URSB | Company filings, beneficial ownership |
| Local governments | Local-government taxes, trading licences |

## Topics requiring Uganda-specific build support

- VAT (registration threshold, standard rate, zero-rated and exempt schedules, place of supply, reverse charge on imported services, EFRIS e-invoicing)
- PAYE (rates, brackets, allowances, NSSF interaction)
- NSSF (employee and employer contributions, ceilings, voluntary contributions)
- Withholding tax (rates by transaction type, residency rules, treaty rates, certificates)
- Income tax (corporate, presumptive small-taxpayer regime, advance income tax, tax incentives)
- Customs duty and excise
- Local-service tax, trading licence, hotel and tourism levies, where applicable
- Exchange rates (BoU daily reference rates, customs rates)
- Statutory deadlines and filing calendar
- URA TaxPro portal and EFRIS integration

## EFRIS

EFRIS-related build requirements:

- Generate fiscal invoices in URA-required format
- Record the URA-issued fiscal document identifier on every sales document
- Record the URA-issued goods/services categorisation
- Reconcile recorded sales with URA's e-invoicing record on a daily or weekly cadence
- Treat credit notes as linked-fiscal-document reversals
- Carry the EFRIS state on every sales journal line: `submitted`, `confirmed`, `rejected`, `cancelled`

EFRIS endpoint, certificate, schema, and field mappings are not hardcoded. They are governed by the source register; a verified version is required before production use.

## Statutory financial reporting

Most Uganda private companies file under IFRS for SMEs (ICPAU adoption). Public-interest entities and certain regulated entities file under full IFRS. The system uses `ifrs-for-smes-default.md` for the default and `full-ifrs-overlay.md` for promoted entities.

## URSB filings

Annual returns and beneficial-ownership filings are not accounting outputs but they consume entity master data. The system exposes the entity master in a form compatible with URSB requirements, including directors, shareholders, registered office, beneficial owners, and PSC information where relevant.

## Live-verification targets

The following Uganda topics are always live-verified per `live-rate-verification-protocol.md`:

- VAT standard rate, registration threshold, zero-rated schedule, exempt schedule.
- PAYE brackets and rates.
- NSSF rates and ceilings.
- WHT rates by transaction type and by residency.
- Income tax rates (corporate, individual, presumptive).
- EFRIS schema version, endpoint, certificate, and category mappings.
- BoU exchange-rate retrieval method.
- Statutory deadlines and filing calendar.

## Known operational gaps

- **No stable public BoU daily exchange-rate CSV/API endpoint identified.** Until resolved, exchange-rate ingestion uses a documented retrieval method per environment and the verification protocol.
- **No public canonical EFRIS API/schema URL identified.** Until resolved, EFRIS field mappings are template-led with explicit version tracking and authority verification.
- **No public URA standard chart of accounts for tax-control accounts.** The system's CoA tax control accounts are designed to map cleanly to URA return-pack lines; the mapping is part of the deliverable, not assumed.
- **No public URA unified tax-report schema.** Tax reports are produced from governed ledger data and mapped to the current URA return template per filing.

## Forbidden patterns specific to Uganda outputs

- Stating a Uganda VAT, PAYE, WHT, NSSF, or income tax rate as a hardcoded value in any final artefact.
- Claiming EFRIS automation without verified integration evidence.
- Producing a tax return as a finished filing rather than a return pack.
- Treating an EFRIS confirmation as the only source of truth for a sale (the ledger remains the source of truth; EFRIS is a parallel system reconciled against it).

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
