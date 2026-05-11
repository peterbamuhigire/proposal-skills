# AI-Agent Abandonment-and-Refund Policy Template

Customer-facing policy on when the agency will abandon the Agent deployment and refund unused fees. Designed to be published on the agency website, included in the proposal annex, and referenced in the MSA. Pairs with `ai-agent-credit-and-refund-clauses.md` and `../ai-agent-intervention-credit-and-abort-refund/SKILL.md`.

---

# Agent Abandonment and Refund Policy

**[AGENCY]** stands behind the AI Agents it operates for its clients. Where an Agent cannot meet its agreed performance, or where its continued operation would harm the Buyer, a third party, or the public, we will pause the Agent, abandon the deployment, and refund unused fees. This Policy sets out the principles and the operational mechanics by which we honour that commitment.

## Principle

We will not keep operating an Agent that is failing. We will not keep invoicing for an Agent that is failing. We will not hold a Buyer in a multi-year commitment for an Agent that cannot reach the autonomy ramp the Buyer was promised.

The Buyer's right to abort exists in addition to the routine service credits that compensate for missed Service Levels. Where the abort right triggers, the Buyer exits with pro-rata refund of unused subscription fees, retains the credits already issued, and receives our cooperation in the wind-down.

## When We Will Abandon a Deployment

We will invoke the abandonment-and-refund mechanics in any of the following situations. The mechanics are set out in the Pricing Exhibit and the MSA Addendum; this Policy summarises them in plain language.

### 1. Irreversible-Action Incident at Our Fault
An Agent action classified as Irreversible has caused material adverse effect, and our investigation determines the cause was on our side — a breach of the Action Catalogue, a breach of the kill-switch SLA, a breach of irreversibility gating, or a breach of the audit-log completeness SLA. We do not hide behind the model provider; if the Agent's reasoning was inside our scope, the accountability is ours.

### 2. Sustained Intervention Overshoot
If the Agent's monthly Intervention Rate exceeds the agreed ceiling for sixty (60) consecutive days, and our thirty (30) day remediation window does not return the rate to within the ceiling, the Buyer's autonomy expectation has not been met. The Buyer may abort.

### 3. Regulator Action
If a regulator with jurisdiction issues an order to pause, restrict, or terminate the Agent, and we cannot remedy the cause within ninety (90) days, the Buyer may abort. Where the regulator action arises from a regulator's general policy on agentic systems rather than our specific failure, we will discuss with the Buyer whether a credit against a future engagement is appropriate.

### 4. Model-Provider Sustained Outage
If an upstream model provider is unavailable for the relevant model family for more than seven (7) consecutive days, and we have not invoked the agreed multi-provider fall-back, the Buyer may abort the affected window.

### 5. Audit-Log Breach
If audit-log completeness falls below the SLA threshold for two consecutive months without remediation, the Buyer's ability to evidence the Agent's actions has been compromised. The Buyer may abort.

## How the Refund Works

The refund is pro-rata of unused prepaid subscription fees:

> Refund = Prepaid Subscription Fees × (Unused Days in Period / Total Days in Period)

Implementation fees are refundable only against unmet milestones. Where the abandonment arises from a breach of an implementation milestone, the implementation fee for that milestone (and only that milestone) is refunded.

Credits already issued under the SLA are retained by the Buyer. The Buyer is not required to repay them on abort.

## Wind-Down Period

Abort is not immediate. We will wind the engagement down over up to thirty (30) days to:

- Confirm the kill-switch is invoked and the Agent is no longer taking actions.
- Hand over open Tasks to the Buyer's named operations team.
- Return Buyer data per the Data Protection Addendum.
- Preserve the Audit Log for the retention period.
- Remove the Agent's identity and scope from the Buyer's systems.
- Settle refunds and final invoices.

The wind-down is in good faith and is not a backdoor to extend the engagement.

## What This Policy Does Not Do

This Policy does not:

- Refund fees for missed Service Levels — those are remedied by service credits on the Monthly Statement.
- Refund implementation fees for milestones the Buyer accepted and paid.
- Permit the Buyer to abort over a single miss; the triggers are deliberately calibrated to sustained or material failures, not isolated incidents.
- Substitute for arbitration of disputed claims; where the cause of an Incident is itself disputed, the Dispute Resolution Annex governs.
- Permit double recovery in respect of the same loss.

## What the Buyer Can Expect

- A Monthly Statement that shows credits applied and explains the underlying metric.
- An evidence-pack on request for any dispute or regulator inquiry; included allowance per year, additional packs at documented professional rates.
- A clear path to abort if our Agent fails the autonomy ramp we promised.
- An orderly wind-down that protects the Buyer's data, operations, and reputation.
- Cooperation with the Buyer's regulator, auditor, and legal counsel through the process.

## Limits and Honesty

We do not refund fees where the cause is the Buyer's misuse of the Agent, the Buyer's bypass of irreversibility gating, the Buyer's change to the Action Catalogue without change order, or the Buyer's pause of the supervisor queue. These exclusions are not loopholes; they protect the integrity of the Agent's operating envelope.

We do not refund fees where the cause is sustained Force-Majeure outside the model provider and outside our control. We will work with the Buyer on a fair commercial outcome where the cause is genuinely beyond either party.

## Contact

For abandonment-and-refund questions, contact:
- The Agency Account Lead named in the Statement of Work.
- The Agency's Agent Ops Lead.
- The Agency's General Counsel for any escalation.

---

This Policy is summary. The operative terms are in the Pricing Exhibit, the SLA Exhibit, the MSA Addendum, and the Trust and Compliance Annex. Where this Policy and the operative documents differ, the operative documents prevail.
