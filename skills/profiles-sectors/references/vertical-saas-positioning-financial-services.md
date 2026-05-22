# Vertical SaaS Positioning — Financial Services

Positioning brief for SaaS implementation and SaaS product-development proposals in financial services. Covers retail and commercial banks, microfinance institutions, payment service providers, mobile-money operators, capital-markets firms, FinTech challengers, and bank-adjacent corporates (savings and credit cooperatives, building societies).

## Sub-Vertical Map

| Sub-vertical | Typical Buyer | Typical Pain Pattern |
|---|---|---|
| Tier-1 retail bank | CIO + COO + CDO | Core banking modernisation, customer-experience digital channels, compliance pressure |
| Tier-2 / 3 bank | CEO + CIO | Cost-to-serve, customer acquisition in digital, regulator pressure for stability |
| Microfinance | CEO + CIO | Field-agent productivity, mobile-first member experience, regulator reporting |
| Payment service provider | CEO + CTO | Scale, fraud, regulatory licensing, settlement |
| Mobile-money operator | CEO + COO | Agent network, KYC, AML, cross-border, regulator reporting |
| Capital markets firm | COO + Head of Trading | Order management, surveillance, regulator reporting, market data |
| FinTech challenger | Founder + CTO | Speed to market, BaaS partner integration, compliance-as-feature |
| SACCOs / building societies | CEO + CIO | Modernisation, mobile, prudential reporting, agent expansion |

## Regulators and Compliance Realities

- **Central banks** — Bank of Uganda, Central Bank of Kenya, Bank of Tanzania, Central Bank of Nigeria, South African Reserve Bank, Bank of Ghana. Each has prudential, AML/CFT, and increasingly data-handling expectations.
- **National data protection authorities** — NITA-U (Uganda), ODPC (Kenya), NDPC (Ghana), NDPR (Nigeria), Information Regulator (South Africa).
- **Payment regulators** — separate or combined with central bank depending on country.
- **Capital markets regulators** — CMA (Kenya, Uganda), SEC (Nigeria), FSCA (South Africa).
- **Cross-cutting** — FATF, AML risk-rated jurisdictions, Common Reporting Standard, sanctions screening.
- **Cloud and data residency** — most central banks have published cloud-use guidance ranging from permissive (Kenya, South Africa) to restrictive (some markets retain on-shore data requirements for core banking systems).

## Common Integration Reality

- Core banking system (Temenos T24, Finastra, Flexcube, Mambu, Profile, Bankworks, T24 derivatives, in-house cores in larger banks).
- Card management system (Way4, Vision Plus, Compass Plus, Tieto).
- Switch (Postilion, OpenWay, BPC SmartVista, OnPoint).
- AML/KYC engine (Actimize, Oracle Mantas, FICO TONBELLER, ComplyAdvantage, Refinitiv WorldCheck).
- Customer information system / MDM.
- Channels: USSD, mobile app, internet banking, agency banking, branch.
- Mobile-money switches: M-Pesa G2, MTN MoMo, Airtel Money, Orange Money.
- Reporting: regulator reporting (XBRL or custom), management reporting, finance / GL integration.

## Proof Points the Agency Should Cite

- Core banking modernisation case studies (anonymised where required).
- Mobile-first banking launches with measurable activation and retention.
- AML / KYC modernisations with reduced false-positive rates and regulator-cleared outcomes.
- BCDR exercises with measured RTO / RPO.
- Regulator-cleared cloud or hybrid hosting outcomes for sensitive workloads.
- Payment-corridor integrations: cross-border, multi-currency, settlement reconciliation.

## Price Ceiling Notes

- Financial services tolerates premium implementation fees when the risk-and-compliance story is clear.
- Tier-1 banks accept day rates at the high end of the regional market for senior, vertical-experienced consultants.
- Mid-market banks typically expect blended teams with one senior anchor and onshore mid-level execution.
- Microfinance and SACCOs have meaningful price-sensitivity; tier the engagement.
- FinTech challengers are often venture-funded with short cycles — fixed-price, milestone-based works well.

## Win Themes for This Vertical

- **Regulatory-grade engineering** — the agency builds for regulators, not just product teams. Show pen-test outcomes, BCDR test reports, regulator dry-run.
- **Core integration realism** — every claim about integration with the named core banking system is backed by comparable engagement evidence.
- **Per-tenant isolation defensibility** — for SaaS sold to banks-of-banks (BaaS, white-label), the isolation story is the proof.
- **Channels-first customer experience** — the agency understands that in this market, the channels (mobile, USSD, agent) are where value is captured, not the core.
- **Vertical-experienced team** — named consultants with prior bank or PSP experience.

## Anti-Patterns Specific to This Vertical

- Pitching "AI-everything" before establishing core stability and regulator alignment.
- Promising central-bank approval the agency cannot influence.
- Assuming cloud-only architecture when the regulator requires on-shore data.
- Pricing without acknowledging the long procurement cycle (often 6–12 months from RFP issuance to contract).
- Ignoring the integration reality of the named core banking system.

## Discovery Questions Specific to Financial Services

In addition to the standard SaaS discovery question bank:

- Which central-bank guidance applies to cloud and outsourcing for this institution's tier?
- What is the institution's stance on data residency for customer data, transaction data, and regulator reports?
- Which core, switch, AML, and CRM systems are in scope for integration?
- What is the regulator-reporting calendar and which reports does the SaaS feed?
- What is the BCDR posture mandated by the regulator?
- Which sanctions and watchlist sources are required?
- What is the audit cadence and which auditors will review the system?

## See Also

- `saas-discovery-question-bank.md` for the general SaaS discovery.
- `saas-procurement-and-security-questionnaire-playbook.md` for the regulator-grade security pack.
- `saas-implementation-methodology-blocks.md` for the implementation phases.
- `saas-business-case-and-roi-template.md` for the value case.
