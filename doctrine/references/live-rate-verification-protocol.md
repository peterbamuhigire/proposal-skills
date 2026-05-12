# Live-Rate Verification Protocol

## Rule

Planning defaults may seed estimates and drafts only. Before any final document, pricing claim, payroll run, statutory filing, statutory schedule, client implementation, or software default ships, the rate, threshold, or template version must be verified against current authoritative sources and logged in the source register.

## Topics that always require verification

- VAT (rates, thresholds, registration, place of supply, zero-rated and exempt schedules)
- PAYE (rates, brackets, allowances, reliefs, NSSF interaction)
- NSSF (employee and employer contribution rates, ceilings)
- Withholding tax (rates by transaction type, residency rules, certificates)
- Income tax (corporate rates, small-taxpayer regime, presumptive tax, advance tax)
- Customs duty and excise
- Stamp duty, local-government rates, hotel and tourism levies (where applicable)
- Exchange rates (closing, average, customs)
- EFRIS (Uganda) and eTIMS (Kenya) — endpoint, certificate, schema, return mappings
- Statutory schedules (PAYE schedule, NSSF return, VAT return, WHT credit, income tax schedule)
- Country-specific statutory deadlines and filing calendars

## Source hierarchy

| Tier | Sources |
|---|---|
| **Tier 1 — authoritative law** | Enacted Acts, statutory instruments, finance acts, gazettes (Parliament of Uganda, Kenya Law, Government Printer). |
| **Tier 2 — authoritative regulator** | URA, KRA, RRA, TRA, SARS, NSSF Uganda, KRA-iTax, eTIMS, BoU, CBK, ICPAU. |
| **Tier 3 — authority operational guidance** | URA notices, KRA notices, regulator FAQs, EFRIS handbook, eTIMS user guide. |
| **Tier 4 — accredited professional bodies** | ICPAU, ICPAK, IFRS Foundation, ACCA, CIMA, IIA. |
| **Tier 5 — Big Four / accredited firm publications** | EY, PwC, KPMG, Deloitte annual tax guides and IFRS bulletins. |
| **Tier 6 — secondary commentary** | Other reputable accounting press. Never used alone for a verification. |

A verification combines a Tier 1 or Tier 2 source with a current-period reading. Tier 3–5 sources support interpretation; they do not replace Tier 1 or Tier 2 for a rate value.

## Verification cadence

| Topic | Cadence |
|---|---|
| VAT standard rate, zero-rated schedule, exempt schedule | Per quarter and per Finance Act. |
| PAYE rates, brackets, reliefs | Per quarter and per Finance Act. |
| NSSF rates and ceilings | Per quarter and per relevant amendment. |
| WHT rates by transaction type | Per quarter. |
| Income tax rates | Per Finance Act and on first use of the year. |
| Customs and excise | Per Finance Act and per gazette notice. |
| Exchange rates (closing, average, customs) | Per artefact for final figures; daily snapshots for transactional use. |
| EFRIS / eTIMS endpoints, certificates, schema versions | Per release of the authority's e-invoicing platform. |
| Statutory deadlines and filing calendars | Annually, plus on any authority notice. |

## Verification log

Every verification creates an entry in the source register at the country level:

```yaml
- topic: Uganda VAT standard rate
  jurisdiction: UG
  value_or_rule: "<verified value>"
  source_url_or_doc: "<Tier-1 or Tier-2 source>"
  source_tier: 1
  date_accessed: "YYYY-MM-DD"
  verifier: "<named human or named agent run>"
  output_affected: ["sales-tax-codes", "vat-return-pack", "efris-validation"]
  expiry_or_recheck: "YYYY-MM-DD"
  state: verified-current | pass-with-caveats | blocked | draft
  evidence_archive: "<path-or-url-to-archived-source>"
  notes: ""
```

## Use states

| State | Meaning | Allowed use |
|---|---|---|
| `draft` | Planning default; not verified. | Internal drafts, brainstorming, structure. Never final output. |
| `pass-with-caveats` | Verified against a Tier 3+ source pending Tier 1/2 confirmation. | Internal proposals and design drafts with explicit caveat text; not statutory filings. |
| `verified-current` | Verified Tier 1 or Tier 2 within the cadence window. | All output, including final. |
| `blocked` | Verification attempted and failed (source not available, conflicting sources, source deprecated). | No output. The artefact fails the quality gate. |

## Marking in artefacts

Every artefact that consumes a verifiable value marks it inline:

```
VAT standard rate: <value>   [verified-current — URA, accessed YYYY-MM-DD, verifier <role>]
```

Or where draft:

```
VAT standard rate: <planning default — verify from URA before final output>
```

## Country-extension placeholders

The protocol applies identically to country extensions. Each country extension provides a source-register schema, authority list, cadence table, and verification owners. Initial placeholders:

- Uganda: URA, NSSF Uganda, BoU, ICPAU, URSB, Parliament, Government Printer.
- Kenya: KRA (iTax, eTIMS), Kenya Law, NSSF Kenya, NHIF, CBK, ICPAK.
- Rwanda: RRA, RSSB, BNR, iCPAR.
- Tanzania: TRA, NSSF, PPF, BoT, NBAA.
- South Africa: SARS, UIF, SARB, SAICA.

## Forbidden patterns

- Hardcoded tax, payroll, statutory, EFRIS, or exchange-rate values in final outputs without an entry in the source register.
- Verification claimed without Tier 1 or Tier 2 evidence.
- Verification logged without the named verifier and date.
- Source-register entries that have passed their `expiry_or_recheck` date and are still referenced in final output.
- Verifications based on third-party blog posts or undated PDFs.

## Quality-gate consequence

Missing or stale verification on any topic in scope is a blocker under the finance/accounting quality gate. See `../../governance/finance-accounting-quality-gate.md`.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
