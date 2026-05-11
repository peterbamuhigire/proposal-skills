# AI-Agent Outcome-Pricing Clauses

Drop-in clauses for gain-share, success-fee, hybrid base-plus-success, and performance-corridor pricing. Pairs with `../ai-agent-success-fee-and-outcome-pricing/SKILL.md` and `ai-agent-success-definition-language.md`.

---

## Structure 1 — Gain-Share

### Sample Clause (Debt-Recovery Agent)

> The Agency shall be paid a Gain-Share Fee equal to eight per cent (8 %) of Recovered Value above the agreed Baseline Recovery Rate. Recovered Value is calculated thirty (30) calendar days after the recovery event, and shall exclude any amount subject to Reversal within that window. Reversal means chargeback, reversal entry by the originating bank, or court-ordered repayment. The Baseline Recovery Rate is set out in Annex [GS-1] and shall be reviewed annually.
>
> The Gain-Share Fee is in addition to the Base Fee of [$ ] per calendar month, which covers Platform Operations, Oversight, Eval, Red-Team, Drift-Watch, and Kill-Switch operations. The aggregate Gain-Share Fee shall not exceed two hundred per cent (200 %) of the Base Fee in any calendar quarter.
>
> Attribution disputes shall be raised within sixty (60) days of the recovery event by reference to the Action Audit Log. Disputes not raised within sixty (60) days are deemed final.

### Variant — Churn Save

> The Agency shall be paid a Save-Share Fee equal to ten per cent (10 %) of Saved Annual Recurring Revenue, calculated as the ARR of a Buyer customer who would otherwise have churned, where the Agent's intervention is the proximate cause of the save as evidenced by the Save Playbook log. Reversal means the customer churns within ninety (90) days of the save event. Saved ARR is calculated ninety (90) days after the save event.

### Variant — Fraud-Loss Reduction

> The Agency shall be paid a Loss-Reduction Fee equal to five per cent (5 %) of the verified reduction in monthly Fraud Loss versus the agreed Baseline Fraud Loss Rate, measured monthly and confirmed quarterly by the Buyer's risk function. Reversal includes any subsequent reclassification of an event by the Buyer's risk committee.

---

## Structure 2 — Success Fee (Threshold-Based)

### Sample Clause (Customer-Support Resolution Agent — Return Engagement)

> The Buyer shall pay seventy per cent (70 %) of the Standard Resolution Rate as Base Fee. In any calendar month in which the Intervention Rate is at or below ten per cent (10 %) and the CSAT score on Agent-handled Resolutions is at or above 4.3 / 5, the Buyer shall pay a Success Fee of fifteen per cent (15 %) of the Standard Resolution Rate on Resolutions completed in that month.
>
> The aggregate Success Fee shall not exceed thirty per cent (30 %) of Base Fees in any calendar quarter.
>
> The metrics shall be measured from the Action Audit Log and the Buyer's CSAT system, with evidence-link in the Monthly Statement.

### Variant — Deflection Threshold

> A Success Fee of [N %] of Standard Rate is payable on Resolutions in any month in which the Deflection Rate (percentage of customer enquiries closed without human involvement) is at or above [X %].

### Variant — SLA-Breach Reduction

> A Success Fee of [$ ] per month is payable in any month in which the Buyer's named SLA Breach Rate falls below [X %] versus an agreed Baseline.

---

## Structure 3 — Hybrid Base-Plus-Success

### Sample Clause (Insurance Claims Triage Agent)

> The Buyer shall pay a Base Fee of thirty-two thousand United States Dollars (USD 32,000) per calendar month covering Platform Operations, Eval and Red-Team, Drift Watch, Kill-Switch Drills, and Supervisor Retraining. The Base Fee includes up to five thousand (5,000) Triaged Claims per month.
>
> Above five thousand (5,000) Triaged Claims, the Buyer shall pay zero point six United States Dollars (USD 0.60) per Triaged Claim.
>
> In any month in which the Intervention Rate is at or below twelve per cent (12 %), the Buyer shall pay an Outcome Bonus of zero point one zero United States Dollars (USD 0.10) per Triaged Claim above five thousand (5,000). The aggregate Outcome Bonus shall not exceed ten per cent (10 %) of Base Fee in any calendar quarter.
>
> The Monthly Statement shall itemise Base, Overage, Bonus, and Credits.

---

## Structure 4 — Performance-Corridor

### Sample Clause (High-Volume Resolution Agent)

> The Unit Price per Resolution shall slide on a Performance Corridor:
>
> | Observed Monthly Intervention Rate | Unit Price |
> |---|---|
> | At or below five per cent (5 %) | USD 1.00 |
> | Between five per cent (5 %) and ten per cent (10 %) | USD 0.85 (Standard Rate) |
> | Between ten per cent (10 %) and fifteen per cent (15 %) | USD 0.75 |
> | Between fifteen per cent (15 %) and twenty per cent (20 %) | USD 0.65 |
> | Between twenty per cent (20 %) and twenty-five per cent (25 %) | USD 0.45 (Floor) |
> | Above twenty-five per cent (25 %) for sixty (60) consecutive days | Abort-and-Refund triggers |
>
> The Standard Rate, the Floor, and the Abort threshold are reviewed annually.
>
> The Floor is the Agency's cost-recovery price. The Agency does not operate the Agent below the Floor.

---

## Cross-Structure Clauses

### Attribution Test

> An Outcome is attributable to the Agent where the Action Audit Log shows the Agent took an action that the Attribution Test in Annex [AT-1] identifies as the proximate cause. The Attribution Test is the source of truth for Outcome attribution. Disputes shall be resolved by reference to the Action Audit Log; the Buyer's right to dispute is exercisable within sixty (60) days of the Outcome event.

### Cooling-Off Period

> An Outcome shall not be billable, nor shall a Success Fee accrue, until the Cooling-Off Period has expired without a Reversal Event. The Cooling-Off Period is thirty (30) calendar days unless a longer period is specified in the Outcome Definition.

### Reversal Definition

> A Reversal Event for the purposes of this Section means: [list per outcome class, e.g. chargeback, refund, complaint upheld, ticket reopen, policy cancellation, claim withdrawal].

### Counter-Example Rule

> Each Outcome Definition shall identify at least one counter-example — an event that would otherwise appear to satisfy the Outcome Definition but is excluded by it. Counter-examples are set out in Annex [SD-1].

### Downside Protection

> Notwithstanding the Outcome-Pricing Structure, the Buyer shall pay no less than the Monthly Floor of [$ ] in any calendar month. The Monthly Floor covers Agency cost of Platform Operations, Oversight, Eval, Red-Team, Drift-Watch, and Kill-Switch.

### Cap on Success

> The aggregate Success Fee or Gain-Share Fee in any calendar quarter shall not exceed the Quarterly Cap. The aggregate Success Fee or Gain-Share Fee in any calendar year shall not exceed the Annual Cap. Caps are set out in the Pricing Exhibit.

### Re-Price on Scope Change

> Where the Buyer materially changes the Workflow, the Action Catalogue, or the data sources feeding the Agent, the Outcome-Pricing Structure is re-priced. A material change includes: a new Action Class; a more-than-twenty per cent (20 %) change in expected volume; a change in the regulator-mandated outcome definition; a change in the Buyer's baseline measurement.

### Regulator-Pause and Force-Majeure

> Outcomes shall not accrue Success Fees or Gain-Share Fees during a Regulator-Pause or a Model-Provider Force-Majeure window. Outcomes already in the Cooling-Off Period at the start of the window remain billable on expiry of the window without Reversal.

### Quarterly Review

> The Outcome-Pricing Structure shall be reviewed quarterly by the Buyer's commercial lead and the Agency's Agent Ops Lead. Material divergence from the Pricing Sensitivity Assumptions (Annex [PS-1]) shall be addressed at the review.

---

## Africa-Context Notes

- For SACCO / MFI engagements with KES / NGN / UGX / RWF / ZAR denomination, the FX corridor clause in the Pricing Exhibit applies; outcome fees that depend on USD model costs require explicit FX language.
- For public-sector engagements on citizen services, outcome pricing is generally inappropriate; use Pattern D (per-agent) instead.
- For FS engagements in CBK / CBN / SARB jurisdiction, the Attribution Test may need to reflect the regulator's automated-decisioning expectations — the regulator may treat the Agent's action as the Buyer's decision regardless of the contract; outcome pricing should not be used to shift accountability.
