# AI-Agent Dispute Resolution and Audit Rights

SLA dispute mechanics, audit-log audit rights, evidence-pack fee, and escalation path. Drop-in annex for the MSA. Pairs with `../ai-agent-msa-and-sla-addendum-templates/SKILL.md` and `ai-agent-credit-and-refund-clauses.md`.

---

# Annex — Dispute Resolution and Audit Rights (Agent)

This Annex governs disputes arising under the Pricing Exhibit, the SLA Exhibit, and the MSA Addendum in respect of the Agent.

## 1. Sources of Truth

1.1 The **Action Audit Log** is the source of truth for: (i) actions the Agent took; (ii) decisions and reasoning traces where captured; (iii) human approvals; (iv) tool calls and outcomes; (v) Intervention events; (vi) Resolution / Outcome / Step / Action counts; (vii) SLA-metric measurement.

1.2 The **Monthly Statement** is the source of truth for: (i) fees billed; (ii) credits applied; (iii) the metric numbers used for the month.

1.3 The **Drill Log** is the source of truth for: (i) kill-switch drill cadence; (ii) drill outcomes.

1.4 The **Sub-Processor Notice Log** is the source of truth for: (i) Sub-Processor changes; (ii) effective dates; (iii) Buyer responses.

## 2. SLA Dispute Mechanics

### 2.1 Time-bar
Disputes on Service Credits or SLA-metric observations shall be raised within **thirty (30) days** of the Monthly Statement to which they relate. Disputes raised after thirty (30) days are barred and the Monthly Statement is final.

### 2.2 Notice
A dispute is raised by written notice to the Agency Account Lead and the Agency General Counsel, identifying the metric, the period, the disputed observation, and the Buyer's proposed correction.

### 2.3 Initial response
The Agency shall respond within **ten (10) business days** with: (i) Audit Log evidence; (ii) explanation of the observation; (iii) accept / reject / counter-propose of the Buyer's position.

### 2.4 Operational review
If the parties do not agree within twenty (20) business days, the Agency's Agent Ops Lead and the Buyer's named operations lead shall hold a joint review within thirty (30) days.

### 2.5 Escalation
If unresolved, the matter escalates to the Agency's Managing Partner / Director and the Buyer's named executive sponsor, who shall meet within twenty (20) business days.

### 2.6 Final mechanism
Unresolved disputes are referred to the dispute resolution mechanism in clause [X] of the MSA (mediation followed by arbitration), with the Action Audit Log evidence preserved.

## 3. Attribution Disputes (Outcome Pricing)

3.1 Where the Pricing Exhibit uses outcome or success-based structures, attribution disputes follow the mechanics in clause 2 with the following adjustments:

(a) the attribution test in Annex [AT-1] of the Outcome-Pricing Clauses is the source of truth;
(b) the dispute window is **sixty (60) days** from the Outcome event;
(c) Cooling-Off periods do not start running again once a dispute is raised; the contested Outcome is held pending resolution.

3.2 An Outcome that is the subject of a Reversal Event is excluded from billing regardless of attribution; the Buyer's Reversal Notice shall identify the Audit Log entry.

## 4. Audit Rights on the Audit Log

### 4.1 Buyer audit
The Buyer may audit Agency adherence to the Audit-Log Completeness SLA and the Audit-Log Retention obligation:

(a) once per calendar year (twice for Gold and Platinum SLA Class) on no less than thirty (30) days' notice;
(b) on incident, within fourteen (14) days of the incident;
(c) on regulator request, within the regulator's window.

### 4.2 Scope
The audit shall cover: (i) completeness of logging per the SLA Class; (ii) retention; (iii) replay availability; (iv) integrity (no tampering); (v) access control.

### 4.3 Independent auditor
The Buyer may instead accept an independent auditor's report (SOC 2 Type II, ISO 27001, ISO 42001) covering the audit-log control objectives, provided annually at the Agency's cost.

### 4.4 Cost
- Routine annual audit: each party bears its own cost.
- On-incident audit: at the Agency's cost where the incident is determined to be the Agency's fault; at the Buyer's cost otherwise.
- On-regulator audit: at the Agency's cost.

### 4.5 Confidentiality
Audit findings shall be confidential. The Buyer may share findings with its regulator and its own auditor without further notice.

## 5. Evidence-Pack Fee

### 5.1 Definition
An **Evidence Pack** is a forensic compilation of Audit Log entries, screenshots, eval results, drill logs, prompt versions, and configuration snapshots relevant to a specific dispute, incident, or regulator inquiry.

### 5.2 Allowance
The Agency shall produce up to **two (2) Evidence Packs per calendar year** at no additional cost.

### 5.3 Fee
Beyond the allowance, Evidence Packs are charged at the documented professional rate in the Pricing Exhibit. The rate card shall identify the rate per hour and the minimum charge per pack.

### 5.4 SLA on production
- Routine Evidence Pack: **fifteen (15) business days**.
- Urgent Evidence Pack (regulator inquiry, named incident): **five (5) business days**.

### 5.5 At Agency cost
Evidence Packs required because of an Agency-fault Irreversible-Action Incident shall be produced at the Agency's cost, regardless of allowance, within the urgent SLA.

## 6. Regulator Access

6.1 Where a regulator with jurisdiction over the Buyer requests Audit Log access or an Evidence Pack, the Agency shall cooperate without delay.

6.2 The Buyer shall notify the Agency of the request within two (2) business days where the regulator's rules permit notice.

6.3 The Agency may not assert confidentiality against the regulator. The Buyer remains the regulator's counterparty; the Agency cooperates as the operator of the Agent.

## 7. Preservation Obligations

7.1 The Agency shall preserve all Audit Log entries, Monthly Statements, Drill Logs, Sub-Processor Notice Logs, and Eval Results relevant to a notified dispute for the duration of the dispute and for six (6) years thereafter, regardless of the standard retention period.

7.2 Where litigation hold is invoked by the Buyer or by the Agency in respect of an Incident, preservation extends for the duration of the hold.

## 8. Anti-Spoliation

8.1 The Agency shall not delete, alter, or compress Audit Log entries beyond the documented retention schedule.

8.2 Audit-Log integrity is established by tamper-evident storage (append-only, hash-chained, or equivalent). The integrity mechanism is described in the Trust and Compliance Annex.

## 9. Costs of Dispute

9.1 In the event of a dispute referred to mediation or arbitration:
- Each party bears its own costs until the award.
- The arbitral tribunal may award costs to the prevailing party.
- The Agency may not be required to bear costs where it has substantially complied with the Audit Log and Evidence Pack obligations and the dispute relates to a metric where the Audit Log evidences the Agency's position.

## 10. Survival

10.1 This Annex survives termination of the engagement in respect of any dispute notified before termination, and in respect of preservation obligations for the periods specified.

---

## Annexes Referenced

- Annex [AT-1] — Attribution Test (Outcome-Pricing Clauses)
- Trust and Compliance Annex
- Pricing Exhibit
- SLA Exhibit
- MSA Addendum
