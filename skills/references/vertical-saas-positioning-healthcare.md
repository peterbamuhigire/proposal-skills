# Vertical SaaS Positioning — Healthcare

Positioning brief for SaaS implementation and SaaS product-development proposals in healthcare. Covers private hospital chains, public health facilities, national health insurance schemes, pharmacy chains, diagnostic chains, and health-information exchanges.

## Sub-Vertical Map

| Sub-vertical | Typical Buyer | Typical Pain Pattern |
|---|---|---|
| Private hospital chain | CEO + Medical Director + CIO | EMR adoption, revenue cycle, bed utilisation, multi-site operations |
| Public health facility / hospital group | Director Health Services + Director ICT | HMIS reporting, clinical service quality, supply chain |
| National health insurance scheme | CEO + Director ICT + Director Operations | Member enrolment, claims adjudication, provider network, fraud |
| Pharmacy chain | CEO + COO | Stock, expiry, regulator dispensing reports, multi-site margin |
| Diagnostic chain | CEO + Medical Director | Order-to-result cycle, multi-site quality, integration with referring providers |
| Health-information exchange | National coordinator | Cross-facility patient summary, identity, consent |

## Regulators and Compliance Realities

- **Ministry of Health** — sector regulator with HMIS reporting obligations.
- **Pharmacy regulator** — NDA (Uganda), PPB (Kenya), PCN (Nigeria), SAHPRA (South Africa).
- **Medical practitioners councils** — registration of practitioners, scope of practice.
- **National health insurance regulators** — NHIF (Kenya), NHIS (Nigeria), Ghana NHIA.
- **Data protection** — health data has heightened protection; sector-specific rules often apply.
- **HMIS standards** — DHIS2 is the dominant public-sector HMIS in East Africa; integrations with WHO codes, ICD-10/11, LOINC, SNOMED.
- **Pharmacovigilance** — adverse event reporting obligations.

## Common Integration Reality

- EMR / EHR systems (Epic, Cerner, Allscripts, OpenMRS, Bahmni for low-resource settings, OpenEMR, iSantéPlus).
- Hospital information systems / HMIS (DHIS2, district-level HMIS, in-house).
- Laboratory information systems (LIS).
- Pharmacy information systems.
- Radiology systems (RIS) and PACS.
- Health insurance claims platforms.
- National health identity systems.
- Mobile-money for out-of-pocket payments.

## Proof Points the Agency Should Cite

- EMR rollouts with measured clinician adoption and clinical outcome impact.
- Revenue-cycle modernisations with reduced days-in-A/R.
- Claims-adjudication modernisations with reduced cycle time and improved provider experience.
- HMIS integrations with measured data-quality improvements.
- Pharmacy / supply-chain modernisations with reduced stock-outs and expiries.

## Price Ceiling Notes

- Private hospital chains tolerate enterprise pricing when revenue-cycle and quality outcomes are measurable.
- Public-sector and donor-funded engagements have published rate ceilings and eligible-cost rules.
- National health insurance schemes have meaningful procurement scrutiny; expect long cycles.
- Pharmacy chains have low margins; engagement pricing must align with measured value.

## Win Themes for This Vertical

- **Clinical workflow respect** — the agency understands clinician time is the scarcest resource and that workflow disruption is the single largest reason EMR rollouts fail.
- **Patient-data residency** — explicit, defensible, regulator-aligned.
- **Quality and safety outcomes** — the agency measures and reports clinical outcomes, not just system usage.
- **Multi-site operations realism** — variability between sites, training propagation, central-vs-local governance.
- **Public-sector capacity transfer** — for HMIS work, the operating model is sustainable beyond the engagement.

## Anti-Patterns Specific to This Vertical

- Treating clinicians as system users without acknowledging the workflow disruption cost.
- Promising clinical-decision support that bypasses the clinician's judgement.
- Ignoring the offline / low-connectivity reality of many health facilities.
- Storing patient data outside the jurisdiction without explicit regulator approval.
- Treating HMIS reporting as an afterthought rather than a primary capability.
- Underestimating the change-management work for clinician adoption.

## Discovery Questions Specific to Healthcare

In addition to the standard SaaS discovery question bank:

- Which EMR, HMIS, LIS, RIS, and pharmacy systems are in scope?
- What is the clinician adoption baseline and the target?
- Which clinical outcomes are measured, and how will the SaaS contribute?
- What are the offline / low-connectivity expectations?
- How is patient consent captured and managed?
- Which national identity and insurance-membership systems must the SaaS integrate with?
- What is the HMIS reporting cadence and which codes must be supported?
- For pharmacy and supply chain, what are the regulator's dispensing and stock-reporting requirements?
- For multi-site operations, how is central-vs-local governance handled?

## See Also

- `saas-discovery-question-bank.md`.
- `saas-procurement-and-security-questionnaire-playbook.md`.
- `saas-implementation-methodology-blocks.md`.
- `saas-business-case-and-roi-template.md`.
- `vertical-saas-positioning-insurance.md` for the health-insurance overlap.
- `vertical-saas-positioning-public-sector.md` for the public-sector overlap.
