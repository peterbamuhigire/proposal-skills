# AI-Agent Pricing Exhibit Template

Drop-in Pricing Exhibit for an MSA / SoW. Fill the placeholders and attach as Exhibit A. Covers all five primary pricing patterns and the cross-pattern commercial clauses. Pairs with `../ai-agent-pricing-and-packaging-proposal/SKILL.md`, `../ai-agent-commercial-packaging/SKILL.md`, and `../ai-agent-contract-language-pack/SKILL.md`.

---

# Exhibit [N] — Pricing and Commercial Terms (Agent)

This Exhibit forms part of the Master Services Agreement dated [DATE] between **[BUYER]** and **[AGENCY]**. It governs the fees, units, credits, refunds, pass-through, FX, and renewal mechanics for the Agent(s) under the Statement of Work referenced in [SoW ref].

## 1. Pricing Pattern

The Pricing Pattern applicable to this engagement is **[A — Per-Resolution / B — Per-Outcome / C — Per-Step / D — Per-Agent / E — Hybrid / F — Success-Based]**.

## 2. Unit Definition

[Insert the precise unit definition. Use the counter-example rule.]

> A **Resolution** is the closure of a Buyer ticket by the Agent without subsequent reopen or human re-work for thirty (30) calendar days. A ticket auto-closed by inactivity is not a Resolution. A ticket reopened within thirty (30) days is not a Resolution.

*(Adapt for Outcome, Step, Agent, etc., per the pattern.)*

## 3. Unit Price

| Item | Amount | Currency |
|---|---|---|
| Unit price | **[$ ]** per Unit | **[CURRENCY]** |
| Base Fee (monthly) | **[$ ]** | **[CURRENCY]** |
| Included volume per month (if any) | **[N]** Units | — |
| Overage rate | **[$ ]** per Unit above Included | **[CURRENCY]** |
| Monthly floor | **[$ ]** | **[CURRENCY]** |
| One-time implementation fee | **[$ ]** payable per milestones in Schedule [X] | **[CURRENCY]** |

## 4. Intervention Credit Clause

If the Intervention Rate in any calendar month exceeds **[CEILING %]**, Buyer receives a credit equal to **[C %]** of the Unit Fees billed for that month for every **[P]** percentage points above the Ceiling, up to a maximum credit of **[M %]** of the monthly Unit Fees. The credit appears on the Monthly Statement with evidence-link to the Audit Log.

| Item | Default |
|---|---|
| Intervention Rate Ceiling | [CEILING %] |
| Credit rate (C per P ppts above ceiling) | [C %] per [P] ppts |
| Cap (M %) | [M %] of monthly Unit Fees |
| Ramp period (Ceiling softened) | First [N] months: Ceiling = [CEILING + RAMP %] |

## 5. Vendor Cost Pass-Through

Where the unit cost of model inference, tool-call API access, or compute services charged to Agency by a named Sub-Processor (Annex [X]) increases by more than **[10 %]** on a rolling twelve-month basis, Agency may pass through the increase to Buyer with **sixty (60) days' notice**, capped at the verified increase. Agency maintains a margin floor and provides reasonable evidence on request. Annual cumulative pass-through shall not exceed the lower of (i) CPI + **[3 %]** and (ii) Model-Provider-Price-Index + **[2 %]**, with the margin floor.

Sovereign-AI deployments are subject to the Sovereign-AI Provider Pass-Through Schedule in Annex [Y].

## 6. Fair-Use

The Agent shall operate within the Action Catalogue (Annex [Z]). The Action Catalogue may be amended only by written change order. The Agent's daily Action volume per Tenant shall not exceed **three (3) times the trailing thirty-day P95 daily Action volume**; the Agency shall alert the Buyer and pause the relevant Tenant pending review where this threshold is breached. Anomalous-action ceiling: any Task generating more than **[STEP-MULTIPLE × P95]** Steps triggers automatic pause pending Buyer review.

## 7. Abort-and-Refund

The Buyer may exit this engagement with pro-rata refund of unused prepaid fees on any of:

- An **Irreversible-Action Incident** determined to be at the Agency's fault under the investigation process in the Trust and Compliance Annex.
- **Intervention Rate** above the agreed Ceiling for **sixty (60) consecutive days**, after written notice and a thirty (30) day remediation window.
- **Regulator Action** against the Agentic System that the Agency cannot remedy within ninety (90) days.
- **Model-provider sustained outage** of a named upstream Sub-Processor of more than **seven (7) consecutive days** where the Agency has not invoked the agreed fall-back.
- **Audit-Log Breach** — Audit-Log Completeness below threshold for two consecutive months without remediation.

Refund formula:

> Refund = Prepaid Subscription Fees × (Unused Days in Period / Total Days in Period)

Implementation Fees are not refundable past the milestones in Schedule [X]. The Buyer's right to abort is in addition to any service credits already issued.

## 8. Autonomy Ramp

The Pricing in this Exhibit assumes the Autonomy Ramp in Annex [AA]. A Buyer-initiated request to accelerate the Autonomy Ramp shall trigger a re-price reflecting additional risk and additional oversight. A Buyer-initiated request to decelerate the Autonomy Ramp shall not reduce the Base Fee.

## 9. Autonomy-Progression Price-Step

The Unit Price moves with sustained autonomy:
- Intervention Rate sustained at or below **[T1 %]** for three consecutive months → Unit Price moves to **[$ ]** (better unit economics for Buyer).
- Intervention Rate sustained at or above **[T2 %]** for three consecutive months → Unit Price moves to **[$ ]** (more supervisor cost recovered).

The Price-Step Schedule is in Annex [BB].

## 10. FX Corridor

Fees are denominated in **[LOCAL CURRENCY]**. Model and tool-call costs are denominated in USD. The Reference Rate is the **[CENTRAL BANK]** reference rate on the last business day of the month preceding the invoice month. Where the exchange rate moves by more than **fifteen per cent (15 %)** against the rate at the Effective Date over any rolling twelve-month period, either party may request a commercial review. Sustained FX moves beyond the corridor are not absorbed by the Agency.

## 11. True-Up

At the end of each **[Quarterly / Annual]** True-Up Period:
- Overage Units are billed at the overage rate.
- Under-use does not refund. Up to twenty-five per cent (25 %) of under-use may, at Agency's discretion, roll forward into the next period.
- Volume divergence from forecast by more than **30 %** over two consecutive periods triggers a commercial review.

## 12. Renewal

- Base Term: **[12 / 24 / 36 months]**.
- Renewal Term: **[Annual]** with **ninety (90) day** non-renewal notice (auto-renewal) or **sixty (60) day** pre-renewal review (express-renewal).
- Ramp-Down Protection: Buyer may reduce Included Volume by up to **fifteen per cent (15 %)** at renewal without re-priced Base; reductions beyond 15 % trigger Base re-price.
- Annual price reset capped at the lower of (i) CPI + **[3 %]** and (ii) Model-Provider-Price-Index + **[2 %]**, with margin floor.

## 13. Invoicing and Payment

- Invoiced monthly in arrears for Unit Fees, monthly in advance for Base Fee.
- Payment due **thirty (30) days** from invoice date.
- Late payment interest at the lower of the contractual rate and the maximum permitted by law.
- Disputed amounts: undisputed portion paid; disputed portion escalated under the Dispute Resolution Annex.

## 14. Worked Examples

| Tenant profile | Volume / month | Unit Fees | Base | Intervention Rate | Intervention Credit | Net Invoice |
|---|---|---|---|---|---|---|
| Small | [N1] | [$ ] | [$ ] | [ %] | [$ ] | [$ ] |
| Medium | [N2] | [$ ] | [$ ] | [ %] | [$ ] | [$ ] |
| Heavy | [N3] | [$ ] | [$ ] | [ %] | [$ ] | [$ ] |

## 15. Annexes Referenced

- Annex [X] — Implementation Milestones and Schedule
- Annex [Y] — Sovereign-AI Provider Pass-Through Schedule
- Annex [Z] — Action Catalogue
- Annex [AA] — Autonomy Ramp
- Annex [BB] — Autonomy-Progression Price-Step Schedule
- Trust and Compliance Annex
- Pricing Sub-Processor List
