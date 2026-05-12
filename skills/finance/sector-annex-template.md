# Sector Annex Template

Every sector annex in a Chwezi proposal follows this structure. Sectors: schools, clinics, NGOs, retail / POS, manufacturing, agribusiness, hospitality. Country-extension overlays apply on top of this template.

## 1. Operating boundary

What is in scope as finance / accounting in this sector. Examples for clinics: outpatient billing, in-patient billing, insurance claims, pharmacy POS, lab POS, supplier purchases, payroll, statutory deductions, donor / NGO claims.

## 2. Transaction flows

Per flow: trigger → role → workflow surface → posting service → CoA accounts → subledger → reconciliation → close → reporting → tax.

For clinics:

- Patient registration → cashier → AR ledger / receipt → POS Cash / Mobile Money / Bank.
- Insurance claim → claims clerk → AR (insurer) → reconciliation against insurer statement.
- Pharmacy dispensing → cashier → POS sale + inventory.
- Lab service → cashier → service revenue.
- Supplier purchase → AP clerk → AP ledger → payment run.
- Payroll → Payroll Officer → gross + statutory deductions + net.
- Donor reporting → controller → restricted-fund utilisation.

## 3. Chart of Accounts overlay

Sector-specific control accounts and revenue / cost lines. For clinics: Outpatient Revenue, In-patient Revenue, Pharmacy Revenue, Lab Revenue, Insurance Receivables Control, Patient Receivables Control, Medical Supplies Inventory.

## 4. Internal controls

Sector-specific control set referencing `internal-controls-library`. For clinics: SoD between dispensing pharmacist and billing cashier; controlled-drugs schedule controls; pharmacy stock cycle counts; patient-confidentiality boundaries on audit-log access; insurance-claim ageing review.

## 5. Reports

The standard reports plus sector-specific:

- Clinics: Service Mix by Doctor, Insurance Ageing by Scheme, Pharmacy Margin, Controlled-Drugs Movement, Bed Occupancy and Revenue per Bed-Day.
- Schools: Fees Collected vs Billed by Term, Defaulters Ageing, Bursary Utilisation, Donor Project Report.
- NGOs: Grant Utilisation per Donor, Restricted vs Unrestricted Funds, Eligible Cost Categorisation.
- Retail / POS: Sales by Branch by SKU by Channel, Margin by SKU, Shrinkage Report.
- Manufacturing: Standard-Cost Variances, WIP Ageing, Yield by Batch.
- Agribusiness: Biological-Asset Cohort Report, Mortality Report, Yield per Hectare / per Bird / per Cow / per Pond.
- Hospitality: REVPAR, Occupancy, F&B Margin, Banquet Profitability.

## 6. Roles

Sector role list. For clinics: Receptionist / Registrar, Cashier, Claims Clerk, Pharmacist, Lab Officer, Doctor (read-only billing view), Accountant, Controller, Tax Reviewer, Internal Auditor, Administrator.

## 7. Risks

Common risk register for the sector. For clinics: missed claim deadlines, billed but uncollected services, controlled-drugs leakage, insurance denial ageing, NHIF / NSSF mismatch, donor-restriction breach.

## 8. Acceptance evidence

What proves the system is fit for the sector at delivery:

- A passing finance / accounting quality-gate run.
- A passing `finance-module-audit` scorecard at `pass` or `pass-with-caveats`.
- Sector reports produced from real test data.
- Reviewer sign-off by an accountant familiar with the sector.

## 9. Data-model implications

Specific entities and attributes added on top of the base data model. For clinics: Patient, Visit, Service, Drug, Insurance Scheme, Claim, Diagnosis Code, Prescription, Lab Test, Bed-Day.

## 10. Live-rate / compliance dependencies

Tax codes, statutory deductions, regulator-specific rates, donor-rule constraints — all routed through the source register. Per country extension: add country-specific authority dependencies.

## 11. Caveats

Standard caveat block:

> The vendor-replacement scope described above is bounded by the acceptance evidence listed. The system supports operational accounting through the workflows above; it does not replace professional accounting, audit, or tax-advisory judgement. Final statutory filings remain the responsibility of the client's accountant and / or tax adviser. Rates, thresholds, and statutory templates referenced in this proposal are dated planning defaults and require current-source verification before client go-live.

## Sector annex files in this skill

Each sector has its own annex file (to be authored as clients arrive):

- `schools/`
- `clinics/`
- `ngos/`
- `retail-pos/`
- `manufacturing/`
- `agribusiness/`
- `hospitality/`

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
