# AI-Agent SLA Exhibit Template

Drop-in SLA exhibit for an MSA. Fill the placeholders and attach as Exhibit B (or as numbered by the MSA structure). Pairs with `ai-agent-sla-class-table.md` and `../ai-agent-sla-and-credit-schedule/SKILL.md`.

---

# Exhibit [N] — Service Level Agreement (Agent)

This Exhibit forms part of the Master Services Agreement dated [DATE] between **[BUYER]** ("Buyer") and **[AGENCY]** ("Agency"). It governs the service levels for the Agent(s) delivered under the Statement of Work referenced in [SoW ref]. Capitalised terms not defined here have the meaning given in the MSA or the Agent MSA Addendum.

## 1. SLA Class

The Service Level Class applicable to this engagement is **[BRONZE / SILVER / GOLD / PLATINUM]**.

## 2. Agent Metrics

The Agency commits to the following monthly service levels for the Agent(s):

| Metric | Definition | Threshold |
|---|---|---|
| Availability | Percentage of in-window minutes during which the Agent control plane and inference path respond within agreed latency and accept tasks. | **[ % monthly]** |
| Task-Success Rate | Percentage of attempted Tasks completed to the binary success definition in the Action Catalogue. | **[ % monthly]** |
| Intervention Rate (Ceiling) | Percentage of attempted Tasks requiring human correction, override, or completion. | **≤ [ %] monthly** |
| Time-to-Resolve / Time-to-Action P95 | Wall-clock time from Task receipt to closure (resolution) or to action (action agents) at the 95th percentile. | **≤ [time]** |

## 3. Operational Guardrails

| Guardrail | Threshold |
|---|---|
| Kill-Switch — time-to-stop from authorised command | **≤ [time]** |
| Kill-Switch — drill cadence | **[Annual / Semi-annual / Quarterly]**, drill log available to Buyer |
| Audit-Log Completeness | **≥ [ %] monthly** |
| Audit-Log Retention | **[N] years**, no less than Buyer's regulator-mandated period |
| Replay Availability | Available on request within **[time]** |
| Intervention SLA — time-to-human escalation | **≤ [time]** |

## 4. Measurement and Reporting

- Measurement Window: each calendar month.
- Source of Truth: the Action Audit Log maintained by the Agency, with summary metrics published to the Buyer's portal and to a monthly statement.
- Monthly SLA Statement: shows observed metric per metric, ceiling per metric, credits applied, exclusions invoked, evidence link to the audit log.
- Quarterly Review (Gold and Platinum): joint review with Buyer's operations and the Agency's Agent Ops Lead.
- Annual Review: full SLA review, autonomy-ramp progression, model-provider posture, regulatory environment.

## 5. Credit Schedule

Where an observed monthly metric falls below the threshold or above the ceiling (intervention), Buyer receives a service credit calculated per the table below. Credits are applied against the next invoice after the Monthly SLA Statement.

### 5.1 Availability
[Insert stepped credit table from `ai-agent-sla-class-table.md` for the applicable class.]

### 5.2 Task-Success Rate
[Insert stepped credit table.]

### 5.3 Intervention Rate
[Insert stepped credit table. The Intervention Credit Clause in the Pricing Exhibit governs unit-fee credits where Intervention Rate exceeds the Ceiling; this Exhibit's Intervention Credit operates on the SLA dimension and does not duplicate the unit-fee credit.]

### 5.4 Time-to-Resolve / Time-to-Action
[Insert stepped credit table.]

### 5.5 Kill-Switch
A breach of the Kill-Switch SLA (time-to-stop above threshold on any authorised invocation, or a failed drill not remediated within seven (7) days) triggers a one-time credit of **[25 %–50 %]** of monthly fees and an obligatory joint review.

### 5.6 Audit-Log Completeness
A monthly observed completeness below threshold triggers a credit equal to **[10 %–25 %]** of monthly fees and a remediation plan within fourteen (14) days. Two consecutive months below threshold triggers the Audit-Log Breach Refund under the Pricing Exhibit's Abort-and-Refund Clause.

## 6. Service-Credit Cap

Total credits across all metrics shall not exceed **[10 % / 25 % / 50 % / 100 %]** of monthly fees in any month. Credits do not stack across metrics beyond the cap. The cap is the sole monetary remedy for SLA misses, except where the Abort-and-Refund Clause in the Pricing Exhibit triggers.

## 7. Exclusions and Out-Clauses

The following are excluded from SLA calculation:
- **Scheduled maintenance** — announced not less than fourteen (14) days in advance, conducted in the agreed maintenance window.
- **Upstream model-provider force-majeure** — where a named Sub-Processor declares an outage of the relevant model family on its status page for more than thirty (30) consecutive minutes, the corresponding metric is suspended for the affected window. The Agency commits to multi-provider fall-back where the Buyer has accepted the model-routing-policy variation.
- **Customer-fault** — Buyer-supplied bad data outside the data-quality contract; Buyer-changed Action Catalogue without change order; Buyer-bypassed irreversibility gate; Buyer-paused supervisor queue causing Intervention SLA breach; Buyer-side identity outage preventing Agent authentication.
- **Regulator pause** — a regulator instruction to pause the Agent triggers a joint review; SLA is suspended for the affected window.
- **Beta or preview features** — explicitly named in the SoW.

The Kill-Switch SLA and the Audit-Log Completeness SLA are **not** suspended by Upstream Force-Majeure and remain in force at all times.

## 8. Termination Right

The Buyer may terminate this Exhibit (and the underlying SoW) without penalty if the Agency misses any SLA metric for **[2 / 3 / 4 / 6]** consecutive calendar months, after written notice and a thirty (30) day remediation window. Termination under this clause triggers the pro-rata refund mechanism in the Pricing Exhibit.

## 9. Audit Rights

The Buyer may audit Agency adherence to this Exhibit once per calendar year (twice for Gold and Platinum) on reasonable notice, or by an independent auditor's report (SOC 2 Type II, ISO 27001, ISO 42001) provided annually. The Audit-Log Audit Rights and the Evidence-Pack Fee are governed by the Dispute Resolution and Audit Rights Annex.

## 10. Continuity

- BCDR runbook for the Agent reviewed annually with Buyer's operations.
- Annual DR test with Buyer's participation if requested.
- RTO and RPO per SLA class:
  - Bronze: RTO 24 h / RPO 4 h
  - Silver: RTO 8 h / RPO 1 h
  - Gold: RTO 2 h / RPO 15 min
  - Platinum: RTO 30 min / RPO 5 min

## 11. Definitions

- **Agent** — the autonomous LLM-based system delivered under the SoW.
- **Task** — a unit of work submitted to the Agent for completion.
- **Intervention Rate** — percentage of attempted Tasks in the measurement window requiring human correction, override, or completion.
- **Irreversible Action** — an action classified as irreversible in the Reversibility Matrix in the Trust and Compliance Annex.
- **Action Catalogue** — the schedule of actions the Agent is authorised to take, with reversibility classification and value bounds.
- **Kill-Switch** — the mechanism by which an authorised person can suspend the Agent.
- **Audit Log** — the record of every Agent action with decision, tool call, parameters, result, reasoning trace where feasible, human approval where applicable, timestamp, identity, tenant, and outcome.

[Signatures, dates, exhibit references.]
