# Vertical SaaS Positioning — Insurance

Positioning brief for SaaS implementation and SaaS product-development proposals in insurance. Covers life, non-life (general), health, and microinsurance, including broker, agent, and direct-to-consumer distribution.

## Sub-Vertical Map

| Sub-vertical | Typical Buyer | Typical Pain Pattern |
|---|---|---|
| Life insurer | CIO + COO + Head of Actuarial | Long-tail policy admin, claims experience, ALM, regulator reporting |
| Non-life insurer | CIO + COO + Head of Claims | Claims cycle time, fraud, distribution costs |
| Health insurer | CIO + Medical Director | Provider network, claims adjudication, fraud / waste / abuse |
| Microinsurance | CEO + Head of Distribution | Premium collection (mobile-money), claims fast-path, fraud at low value |
| Insurance broker | CEO + COO | Quote-to-bind cycle, multi-insurer integration, commission |
| Reinsurer | CIO + Head of Treaty | Treaty admin, cession, reporting |

## Regulators and Compliance Realities

- **Insurance regulator** — IRA (Uganda), IRA (Kenya), TIRA (Tanzania), NAICOM (Nigeria), FSCA (South Africa).
- **Sector ombudsmen** for consumer complaints.
- **Data protection regulator** as for financial services.
- **Health-sector overlay** for medical insurance (HIPAA-equivalent and patient-data regulators).
- **Reporting cadence** — quarterly and annual prudential, with claims experience and reserving reports.
- **Solvency frameworks** — risk-based capital regimes increasingly adopted (Solvency II-influenced).

## Common Integration Reality

- Policy administration systems (Guidewire PolicyCenter, Duck Creek, Premia, Sapiens, Effisoft, INSIS, Subscribe, in-house systems).
- Claims systems (Guidewire ClaimCenter, Duck Creek Claims, Subscribe, Athenium, INSIS Claims).
- Billing (Guidewire BillingCenter, Duck Creek Billing).
- Underwriting workbench (Sapiens, FirstUW).
- Reinsurance systems (Subscribe, INSIS Re, in-house).
- Distribution platforms: broker portals, agent apps, direct-to-consumer mobile.
- Provider network platforms for health insurers.
- Bordereau and treaty reporting.

## Proof Points the Agency Should Cite

- Quote-to-bind cycle reductions with measurable conversion uplift.
- Claims cycle reductions with operational savings.
- Distribution-channel launches with measurable broker or agent productivity.
- Fraud detection with measured false-positive / true-positive rates.
- Regulator reporting automations with cycle-time reductions.

## Price Ceiling Notes

- Life and non-life insurers in stable markets accept enterprise-grade pricing.
- Health insurers face price pressure from medical inflation; engagement pricing must align with their cost-to-serve targets.
- Microinsurance has low absolute fee tolerance — tier the engagement; pilot before full implementation.
- Brokers run on commission margins; engagement must show direct revenue impact.

## Win Themes for This Vertical

- **Policy-admin and claims literacy** — the agency understands that PolicyCenter integration is different from a generic CRM integration.
- **Actuarial-grade reporting** — the agency produces reports the actuarial team trusts.
- **Distribution channel reality** — agent app, broker portal, and direct-to-consumer flows respect commission and licensing logic.
- **Health-sector privacy** — patient-data residency and consent handled explicitly.
- **Microinsurance pragmatism** — mobile-money premium collection, fast-path claims, fraud-at-low-value.

## Anti-Patterns Specific to This Vertical

- Treating insurance as "CRM with policies attached".
- Underestimating the complexity of commission rules, broker hierarchies, and producer codes.
- Promising claims automation without acknowledging fraud-and-abuse review requirements.
- Ignoring the reinsurance and bordereau dimension for non-life and life insurers with treaty programmes.
- Assuming cloud-only architecture when the regulator imposes on-shore requirements.

## Discovery Questions Specific to Insurance

In addition to the standard SaaS discovery question bank:

- Which policy admin, claims, and billing systems are in scope?
- What is the product portfolio (life products, motor, household, medical, microinsurance)?
- Which distribution channels does the SaaS serve (broker, agent, direct, partner)?
- What is the commission structure and who maintains it?
- How are reinsurance, bordereau, and treaty reporting handled today?
- Which regulator reports does the SaaS feed and at what cadence?
- What is the fraud-and-abuse review process and how does the SaaS support it?
- For health insurers, what is the provider network and claims-adjudication model?

## See Also

- `saas-discovery-question-bank.md`.
- `saas-procurement-and-security-questionnaire-playbook.md`.
- `saas-implementation-methodology-blocks.md`.
- `saas-business-case-and-roi-template.md`.
- `vertical-saas-positioning-healthcare.md` for the health-insurance overlap.
