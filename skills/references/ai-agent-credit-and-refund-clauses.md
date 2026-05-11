# AI-Agent Credit and Refund Clauses

Drop-in contract language for service credits and refunds in agentic engagements. Pairs with `../ai-agent-intervention-credit-and-abort-refund/SKILL.md`, `../ai-agent-sla-and-credit-schedule/SKILL.md`, and `ai-agent-sla-exhibit-template.md`.

---

## Section A — Service Credit Clauses

### A.1 General Service-Credit Mechanism

> Where the Agency misses a Service Level in any calendar month, the Buyer shall receive a Service Credit calculated in accordance with the Credit Schedule in the SLA Exhibit. Service Credits shall be applied against the next invoice payable by the Buyer. The Buyer's claim to a Service Credit shall be evidenced by the Monthly Statement; no further claim is required. Service Credits are the sole monetary remedy for SLA misses, except where the Abort-and-Refund Clause triggers.

### A.2 Intervention Credit (Per-Resolution Pattern)

> If, in any calendar month, the Intervention Rate exceeds the Intervention Rate Ceiling of [CEILING %], the Buyer shall receive an Intervention Credit equal to [C %] of the Unit Fees billed in that month for each [P] percentage point of breach, up to a maximum Intervention Credit of [M %] of the Unit Fees billed in that month. The Intervention Credit shall be calculated by reference to the Audit Log and shall appear on the Monthly Statement with evidence-link.

### A.3 Intervention Credit (Per-Outcome Pattern)

> If, in any calendar month, the Outcome Attribution Rate (defined as the percentage of attempted Outcomes in respect of which an Attribution Dispute is raised by the Buyer and not withdrawn within sixty (60) days) exceeds [CEILING %], the Buyer shall receive an Outcome Credit equal to [C %] of the Outcome Fees billed in that month for each [P] percentage point of breach, up to [M %].

### A.4 Stepped Credit Tables

[Insert tables from `ai-agent-sla-class-table.md` for the applicable class, per metric.]

### A.5 Cap on Aggregate Credits

> Total Service Credits across all Service Levels and across all months shall not exceed the Service-Credit Cap of [CAP %] of the relevant monthly fees in any one month. Credits do not stack across metrics beyond the Cap.

### A.6 Statement Format

> The Monthly Statement shall identify, for each Service Level: the observed metric, the threshold, the breach (if any), the Service Credit applied, and a link to the underlying Audit Log entries. The Statement shall be delivered to the Buyer within ten (10) business days of the end of the calendar month.

### A.7 Claim Window

> The Buyer's right to question a Service Credit shall be raised within thirty (30) days of the Monthly Statement. After thirty (30) days the Monthly Statement is final.

---

## Section B — Refund Clauses

### B.1 General Refund Right

> Notwithstanding any other remedy under this Agreement, the Buyer may terminate the relevant Statement of Work with pro-rata refund of unused prepaid Subscription Fees on any of the Refund Triggers in Section B.2. Implementation Fees are not refundable past the milestones in Schedule [X], save where the Refund Trigger arises from a breach of an Implementation milestone.

### B.2 Refund Triggers

#### B.2.1 Irreversible-Action Incident at Agency Fault
> An Irreversible-Action Incident is an action by the Agent classified as Irreversible in the Reversibility Matrix that has caused material adverse effect on the Buyer or a third party. Where the cause is determined by the named investigation process in the Trust and Compliance Annex to be at the Agency's fault — including breach of irreversibility-gating, breach of the Action Catalogue, breach of the Kill-Switch SLA, or breach of the Audit-Log Completeness SLA — the Buyer may terminate with pro-rata refund of unused Subscription Fees and may claim under the indemnity and the sub-cap for Irreversible-Action Liability in the MSA Addendum.

#### B.2.2 Intervention Overshoot
> If the Intervention Rate exceeds the Ceiling for **sixty (60) consecutive days** after written notice and a thirty (30) day remediation window, the Buyer may terminate with pro-rata refund of unused Subscription Fees. Intervention Credits already issued shall be retained by the Buyer.

#### B.2.3 Regulator Action
> If a regulator with jurisdiction over the Buyer or the Agent issues an order to pause, restrict, or terminate the Agent and the Agency cannot remedy the cause within **ninety (90) days**, the Buyer may terminate with pro-rata refund. The Agency may, at its option, offer to credit the Buyer's next engagement against the refund.

#### B.2.4 Model-Provider Sustained Outage
> If a named upstream Sub-Processor is unavailable for the relevant service for more than **seven (7) consecutive days** and the Agency has not invoked the agreed fall-back, the Buyer may terminate with pro-rata refund of the affected window.

#### B.2.5 Audit-Log Breach
> If the Audit-Log Completeness falls below the SLA threshold for **two consecutive months** without remediation, the Buyer may terminate the affected Service with pro-rata refund of unused Subscription Fees, plus a credit equal to ten per cent (10 %) of the monthly fees for the affected months.

### B.3 Refund Formula

> Refund = Prepaid Subscription Fees × (Unused Days in Period / Total Days in Period)
>
> Where the engagement is multi-tenant or multi-agent, the Refund is computed per affected tenant or per affected agent persona unless the termination is engagement-wide.

### B.4 Implementation Fee Refundability

> Implementation Fees are refundable only against unmet milestones in Schedule [X]. Where a Refund Trigger arises from a breach of an Implementation milestone, the Implementation Fee for the affected milestone (and only the affected milestone) shall be refunded.

### B.5 Wind-Down

> Termination under a Refund Trigger shall not be immediate. The parties shall wind down the engagement over a period of up to thirty (30) days to:
> (a) ensure data return per the DPA;
> (b) preserve the Audit Log per the MSA Addendum;
> (c) safely retire the Agent (kill-switch confirmed, scope removed, identity revoked);
> (d) hand over open Tasks to the Buyer's named operations team;
> (e) settle Refunds and final invoices.

### B.6 No Double Recovery

> Refunds under this Section are in addition to Service Credits already issued. No remedy under this Agreement permits double recovery in respect of the same loss.

---

## Section C — Customer-Facing Visibility

### C.1 Monthly Statement (Sample)

```
Tenant: ACME
Period: April 2026

[Unit Performance]
Tasks attempted:                          80,000
Tasks completed without intervention:     65,600
Intervention rate observed:               18.0 %
Intervention rate ceiling:                10.0 %
Breach:                                    8.0 ppts

[Fees]
Unit Fees billed:                         $68,000
Base Fee:                                 $25,000
Subtotal:                                 $93,000

[Credits Applied]
Intervention Credit:                     -$5,440 (8.0 % of Unit Fees)
Availability Credit:                      $0
Task-Success Credit:                      $0
Time-to-Resolve Credit:                   $0
Audit-Log Credit:                         $0
                                          --------
Total Credits:                           -$5,440

[Net Invoice]
Net Invoice:                              $87,560

[Evidence]
Audit log evidence-link:                  <agent-audit/2026-04/ACME>
SLA dashboard:                            <portal/sla/ACME>
Kill-switch drill log (latest):           <drills/2026-Q1>
```

### C.2 Credit Disclosure Language

> The Agency commits to issue Service Credits on the Monthly Statement without requiring the Buyer to make a separate claim. Where the Buyer disagrees with the Statement, the dispute window in Section A.7 applies.

---

## Section D — Definitions

- **Service Credit** — a monetary credit applied against the next invoice for a Service Level miss in the relevant month.
- **Intervention Credit** — a Service Credit specific to the Intervention Rate metric and the unit-fee pricing model.
- **Refund Trigger** — one of the events listed in Section B.2.
- **Wind-Down** — the orderly handover and termination process in Section B.5.
- **Service-Credit Cap** — the maximum aggregate Service Credit in any one month, set by the SLA Class.
