# Country Extension Framework

Uganda is the home jurisdiction. Every other country is an extension over the same doctrine. This file specifies the shape of a country extension so that adding Kenya, Rwanda, Tanzania, South Africa, or any future market is a configuration and verification exercise, not a doctrine rewrite.

## Country extension contents

A country extension provides:

| File / module | Purpose |
|---|---|
| `country-profile.md` | ISO codes, languages, currencies, reporting frameworks adopted (IFRS / IFRS for SMEs / local GAAP), filing calendar overview. |
| `authority-list.md` | Tax authority, social-security authority, central bank, accounting standards body, registrar, customs, others. With source URLs. |
| `live-rate-register.yaml` | Source-register seed for the topics in `live-rate-verification-protocol.md`. |
| `return-templates/` | Reference templates for each return type the country supports (VAT, PAYE, WHT, income tax, …). With template version and verified-current state. |
| `payroll-schedule.md` | Payroll deductions list, contribution rules, employer obligations. |
| `e-invoicing.md` | Country e-invoicing or fiscal-device regime (EFRIS, eTIMS, …), if any. |
| `coa-overlay.md` | Country-specific tax control accounts and statutory liability accounts added on top of the base CoA. |
| `verification-cadence.md` | Country-specific overrides on the verification cadence table. |
| `country-quality-gate.md` | Country-specific gate items beyond the cross-cutting gate. |

## Initial country placeholders

| Country | Status | Notes |
|---|---|---|
| Uganda (UG) | Home jurisdiction. | Built first, doctrine-level coverage in `uganda-compliance-caveats.md`. |
| Kenya (KE) | Named placeholder. | Authorities: KRA (iTax, eTIMS), NSSF Kenya, NHIF, CBK, Kenya Law, ICPAK. |
| Rwanda (RW) | Named placeholder. | Authorities: RRA, RSSB, BNR, iCPAR. |
| Tanzania (TZ) | Named placeholder. | Authorities: TRA, NSSF Tanzania, PPF, BoT, NBAA. |
| South Africa (ZA) | Named placeholder. | Authorities: SARS, UIF, SARB, SAICA. |

## Adding a country

The procedure for adding a country extension:

1. Create the country folder under `doctrine/country-extensions/<ISO>/`.
2. Populate the nine files / modules above. Mark all rates and templates as `draft` initially.
3. Run the live-rate verification protocol for each topic to promote from `draft` to `verified-current`.
4. Update the country-profile with the reporting framework decision per `policy-hierarchy.md`.
5. Add country-specific quality-gate items.
6. Update the cross-cutting quality gate adoption plan with the new country in scope.
7. Update the consumer engines' README / CLAUDE.md to surface the new country.
8. Run the `finance-module-audit` skill against any existing client that operates in the new country.

## Forbidden patterns

- Copying Uganda rate values into another country without verification.
- Treating one country's e-invoicing regime as a drop-in for another.
- Reporting framework selection inherited silently across countries.
- Cross-country payroll calculations sharing rules without per-country source-register entries.
- Foreign exchange handling that assumes USD as a universal pivot currency without explicit configuration per entity.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
