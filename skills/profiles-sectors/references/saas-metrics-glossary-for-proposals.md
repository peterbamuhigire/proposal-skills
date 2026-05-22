# SaaS Metrics Glossary for Proposals

Engine-native definitions of SaaS commercial metrics for proposal writing. These are commodity SaaS terms; the engine restates each in its own words so the proposal can use the vocabulary fluently without copying any source.

Use the glossary when:

- Writing the business case for resale SaaS (where the client owns SaaS revenue).
- Defending premium fees to investor-grade buyers.
- Building the M&E section's SaaS health dashboard.
- Briefing the agency team before a CFO-level conversation.

## Top-Line

- **ARR (Annual Recurring Revenue)** — annualised value of the recurring subscription book of business at a point in time. Excludes one-time fees.
- **MRR (Monthly Recurring Revenue)** — ARR / 12 in steady state; or the monthly snapshot in monthly-billed businesses.
- **ACV (Annual Contract Value)** — annualised value of a single customer contract.
- **TCV (Total Contract Value)** — the total committed value over the entire term of a contract.
- **RPO (Remaining Performance Obligation)** — deferred revenue (already billed) + backlog (committed but not yet billed). Useful as a forward-looking commercial indicator.
- **Bookings** — the value of contracts signed in a period. New, expansion, and renewal bookings are reported separately.
- **Billings** — what has been invoiced in a period. Useful for cash-flow analysis.

## Unit Economics

- **CAC (Customer Acquisition Cost)** — fully-loaded sales and marketing cost divided by net-new customers acquired in the same period. Report by channel where possible.
- **CAC Payback** — months of gross profit required to recover CAC. Target varies by segment: < 12 months for SMM, < 18–24 months for enterprise.
- **LTV (Lifetime Value)** — discounted recurring gross profit over the expected customer lifetime. Sensitive to churn assumption.
- **LTV:CAC** — health ratio for the GTM engine. Target ≥ 3:1.
- **Gross Margin** — recurring revenue minus cost-of-revenue (hosting, third-party data, support cost-to-serve). Target ≥ 75% for software-dominant SaaS, lower for ops-heavy or transaction-heavy SaaS.
- **Contribution Margin per Customer** — gross profit less variable success and support cost attributable to that customer.

## Retention

- **Gross Dollar Churn** — % of ARR that does not renew at the contract anniversary. Target as low as possible.
- **Net Dollar Churn** — gross dollar churn minus expansion from the same customer cohort. Expressed as a negative if churn exceeds expansion.
- **Net Dollar Retention (NRR) / Net Dollar Expansion Rate (NDER)** — same data, expressed as a percentage of the prior period ARR for the same cohort. NRR > 100% means the existing book grows even without new sales. Target ≥ 110% for enterprise SaaS.
- **Renewal Rate** — % of ARR up for renewal that actually renews. Always lower than retention rate because the denominator only includes contracts at their anniversary.
- **Logo Churn** — % of customers lost, by customer count rather than dollar.

## Sales Efficiency

- **Magic Number** — quarter's net-new ARR annualised, divided by the prior quarter's sales and marketing spend. A magic number ≥ 0.75 indicates investable sales efficiency.
- **Sales Efficiency** — broader family of ratios comparing new ARR to S&M spend.
- **Burn Multiple** — net cash burned divided by net-new ARR generated. Investor-grade benchmark.
- **Sales Capacity Plan** — forward-looking forecast of expected production = AEs × quota × productivity factor (over-assignment factor).
- **OTE (On-Target Earnings)** — total annual compensation when an AE hits 100% of quota; typically a 50/50 base/commission split for enterprise AEs.
- **Quota** — annual bookings target for an AE.
- **Commission Accelerator** — higher commission rate for bookings above quota; standard in enterprise SaaS to incentivise overperformance.
- **Ramp Time** — months from AE hire to full productivity. Typically 6–9 months for enterprise SaaS.

## Profitability and Investor Metrics

- **Rule of 40** — growth rate + free cash flow margin should exceed 40% for a healthy investable SaaS business. High-growth companies achieve it through growth; mature companies through margin.
- **Quick Ratio for SaaS** — growth in recurring revenue divided by loss of recurring revenue (churn + downgrades). Above 1.0 is good.
- **PSAR (Professional Services Attach Rate)** — services revenue divided by subscription bookings. A 15–30% PSAR is common in enterprise SaaS implementations and provides useful colour for defending implementation fees.
- **Gross Retention Rate (GRR)** — equivalent of (1 - gross dollar churn).
- **CAC Recovery in Months** — synonym for CAC payback in many sources.

## Customer Success and Adoption Metrics

- **Activation Rate** — % of new customers who reach the defined first-value moment within a target window.
- **Time-to-Value (TTV)** — days from contract signature to first-value moment.
- **DAU/MAU and Stickiness** — daily active users divided by monthly active users, an engagement signal.
- **Number of Events per Day per User** — application-specific engagement signal.
- **Customer Health Score** — composite of usage, engagement, support, NPS, and renewal signals.

## Segment Definitions (Mersch)

- **Enterprise SaaS** — ACV $50k+, sales-led, long sales cycle, multi-year contracts, services-heavy.
- **SMM (Small-to-Mid-Market) SaaS** — ACV $5–50k, hybrid sales + self-serve, onboarding-velocity-driven.
- **B2C SaaS** — low-ACV, self-serve only, acquisition-volume-driven.

## Horizontal vs Vertical

- **Horizontal SaaS** — serves a function (CRM, HR, accounting) across many industries.
- **Vertical SaaS** — serves an industry deeply across many functions; commands higher ACV, higher retention, deeper integration.

## How to Use This Vocabulary in Proposals

- Use for *resale SaaS* proposals (client owns SaaS revenue) — full fluency expected.
- For *internal-use SaaS* proposals, use sparingly: TCO, payback, gross margin (for managed-service economics). Avoid Rule of 40 and magic number with non-investor buyers.
- For *investor-grade buyers* (PE-owned SaaS targets, VC-backed clients), explicit references to Rule of 40, magic number, NRR, and burn multiple signal the agency speaks the buyer's language.
- Always state the formula or definition the first time a less-common term is used; do not assume universal understanding even among SaaS-native readers.

## Anti-Patterns

- Quoting NRR without naming the cohort definition.
- Using "LTV" without naming the gross margin and churn assumptions underneath.
- "ARR" used loosely to include one-time fees, professional services, or non-recurring revenue — this is the most common credibility error.
- Mixing Annual and Monthly base for the Quick Ratio without saying which.
- Rule-of-40 referenced for a non-investable business (e.g., a public-sector internal-use SaaS).

## See Also

- `saas-business-case-and-roi-template.md` for these metrics in proposal context.
- `saas-pricing-models-reference.md` for the pricing structures these metrics measure.
