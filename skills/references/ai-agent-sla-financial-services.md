# AI-Agent SLA — Financial Services Variant

Regulator-aware SLA variant for agentic engagements in financial services. Pairs with `ai-agent-sla-class-table.md` and `ai-agent-sla-exhibit-template.md`. Reflects CBK, CBN, SARB, BoU, BNR, BoT, BoG, FSCA and equivalent prudential / conduct regulators across SSA.

## Applicable Regulators (Reference List)

- **Kenya**: Central Bank of Kenya (CBK); Capital Markets Authority (CMA); Insurance Regulatory Authority (IRA); SACCO Societies Regulatory Authority (SASRA).
- **Nigeria**: Central Bank of Nigeria (CBN); Securities and Exchange Commission (SEC); NAICOM.
- **South Africa**: South African Reserve Bank (SARB); Financial Sector Conduct Authority (FSCA); Prudential Authority.
- **Uganda**: Bank of Uganda (BoU); Insurance Regulatory Authority of Uganda (IRA-U); Uganda Microfinance Regulatory Authority (UMRA).
- **Rwanda**: Banque Nationale du Rwanda (BNR); CMA Rwanda.
- **Tanzania**: Bank of Tanzania (BoT); Capital Markets and Securities Authority (CMSA-TZ); Tanzania Insurance Regulatory Authority (TIRA).
- **Ghana**: Bank of Ghana (BoG); SEC Ghana; National Insurance Commission (NIC).
- **Pan-African**: Africa Continental Financial Sector regulators; cross-border AML / KYC obligations under FATF-aligned country rules.

## Mandatory SLA Class

The minimum acceptable SLA Class for production agentic engagements in financial services is **Gold**. Platinum is required where the agent:
- Initiates transactions above defined thresholds.
- Communicates investment advice or product recommendations.
- Operates in fraud, sanctions, or AML decisioning.
- Operates with named regulator notification obligations.

## FS-Specific SLA Adjustments

### 1. Named Accountability for Automated Decisioning
The MSA Addendum's Action Accountability clause is augmented:

> Where the Buyer's regulator imposes a Named-Accountability obligation for Automated Decisioning, the Buyer's named officer (typically the Chief Risk Officer or Head of Compliance) is the regulatory accountable person for the Agent's outcomes. The Agency commits to (i) operate the Agent within the Action Catalogue approved by the named officer; (ii) suspend the Agent on the named officer's instruction; (iii) provide the named officer with monthly evidence sufficient to satisfy the regulator's monitoring obligation.

### 2. Customer-Detriment SLAs
Where the Agent interacts with retail customers, a Customer-Detriment SLA applies:

| Metric | Threshold |
|---|---|
| Customer-detriment incidents per 10,000 Tasks | ≤ 0.5 (Gold); ≤ 0.1 (Platinum) |
| Median time to identify customer detriment | ≤ 24 hours |
| Customer-redress completion | ≤ 14 days from identification |
| Regulator-notification trigger | Any customer-detriment incident affecting > 100 customers, within 24 hours |

A customer-detriment incident is the Agent causing or contributing to consumer harm — incorrect fee charge, wrong product advice, identity confusion, unauthorised transaction, false rejection.

### 3. Audit-Log Retention
Audit-log retention is the **longer of seven (7) years and the regulator-mandated period**. Many FS regulators mandate ten (10) years for transaction-level logs.

### 4. Regulator-Pause SLA
A regulator instruction to pause the Agent is honoured **within four (4) hours** of receipt by the Agency. The kill-switch SLA must be tested against the regulator-pause scenario at least annually.

### 5. AML / KYC / Sanctions Scope
Where the Agent's Action Catalogue includes AML, KYC, or sanctions checks:
- The Agent does not make a final AML, KYC, or sanctions decision; the human compliance officer makes it.
- The Agent's recommendation must be auditable end-to-end.
- The Agent's Audit Log must retain the underlying data used for the recommendation for the regulator-mandated period.
- False-positive and false-negative rates are reported monthly.

### 6. Sub-Processor Disclosure
The model and tool-call Sub-Processors must be disclosed to the regulator if requested. The Buyer's Sub-Processor change-notification window is **fourteen (14) days** rather than the standard thirty (30) where the regulator has imposed shorter approval cycles.

### 7. Cross-Border Data Considerations
Where the regulator imposes data-residency (KE, NG, ZA, UG, RW), the Agent's model and Audit Log storage must be in-country or in an approved jurisdiction. The Sovereign-AI Provider Schedule (Annex SAI-1) is mandatory where the regulator does not permit cross-border model inference for the data class involved.

## FS-Specific Exclusions and Out-Clauses

In addition to the standard Out-Clauses:

- **Regulator policy change** — where the regulator changes its policy on automated decisioning, the parties shall conduct a Commercial Review within thirty (30) days of the policy change. No service credits accrue for SLA misses caused directly by the policy change in the first ninety (90) days.
- **Sanctions or AML escalation** — where the Agent is paused or restricted because of an escalation by the Buyer's compliance function, the SLA is suspended for the affected window.
- **Bank-holiday and settlement windows** — the time-to-resolve and time-to-action thresholds are suspended outside of bank-business-day windows where settlement constraints apply.

## FS-Specific Refund Triggers

In addition to the standard Refund Triggers:

- **Regulator order against the Agent** — a final regulator order to terminate the Agent triggers full pro-rata refund and a 60-day wind-down.
- **Material customer-detriment series** — three or more customer-detriment incidents in any ninety (90) day period triggers the Buyer's abort right with pro-rata refund.

## FS-Specific Pricing Caveats

- **Outcome-based pricing on consumer products** — where the regulator's conduct rules limit incentive structures on consumer outcomes (e.g. credit, retail investment), outcome-based pricing patterns should be reviewed with the regulator before deployment. Pattern E (Hybrid) is the conservative default.
- **Gain-share on recovered debt** — permitted in most jurisdictions but subject to consumer-protection caps on collection-related fees. Verify before deployment.
- **Success fee tied to renewal of consumer products** — verify against the regulator's anti-mis-selling and conduct rules.

## FS-Specific Audit Rights

- Buyer audit on quarterly basis where the regulator has imposed enhanced monitoring.
- Regulator-direct audit rights — the regulator may audit the Agent's Audit Log and the Agency's controls directly, without the Buyer as intermediary, on prior notice through the Buyer. The Agency cooperates without delay.
- Independent auditor report (SOC 2 Type II + ISO 42001) is the minimum substitute for routine audit; on-incident audit remains available.

## FS-Specific Insurance

Professional Indemnity Insurance minimum cover for FS agentic engagements: **USD 10 million** per claim and USD 20 million aggregate per year, with explicit cover for AI-system actions. Cyber Liability Insurance minimum: USD 10 million per claim. Certificates available to the Buyer's risk function on request.
