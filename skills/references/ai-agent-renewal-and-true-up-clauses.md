# AI-Agent Renewal and True-Up Clauses

Drop-in renewal mechanics, true-up clauses, ramp-down protection, autonomy-progression price-step, and index-linked renewal for agentic engagements. Pairs with `../ai-agent-renewal-and-true-up/SKILL.md`.

---

## Section A — Renewal Mechanics

### A.1 Auto-Renewal (Default for Commercial Buyers)

> The Initial Term of this Agreement shall be [12 / 24 / 36] months from the Effective Date. Thereafter, this Agreement shall automatically renew for successive periods of twelve (12) months ("Renewal Term") unless either party gives written notice of non-renewal not less than ninety (90) days before the end of the then-current Term.

### A.2 Express Renewal (Default for Regulated / Public-Sector Buyers)

> The Initial Term shall be [12 / 24 / 36] months. Thereafter, this Agreement shall renew only on written agreement of both parties not less than sixty (60) days before the end of the then-current Term ("Pre-Renewal Review"). If the parties do not agree, the engagement winds down per the Wind-Down clause in the Pricing Exhibit.

### A.3 Hybrid (Auto with Pre-Renewal Review)

> The Initial Term shall be [12 / 24 / 36] months. The parties shall conduct a Pre-Renewal Review at month [10] of the Initial Term and at month [10] of each Renewal Term, covering:
> (a) Autonomy progression against the Autonomy Ramp;
> (b) SLA performance for the trailing twelve (12) months;
> (c) Credit and Refund history;
> (d) Model-Provider posture and Sub-Processor changes;
> (e) FX movement against the Reference Rate;
> (f) Regulatory environment.
> If neither party gives written notice of non-renewal within thirty (30) days of the Pre-Renewal Review, the Agreement automatically renews for a Renewal Term of twelve (12) months.

---

## Section B — True-Up

### B.1 True-Up Period

> The **True-Up Period** is **[quarterly / annual]**. At the end of each True-Up Period, the parties shall reconcile observed volume against Included Volume.

### B.2 Overage

> Volume above the Included Volume during the True-Up Period is billed at the Overage Rate set out in the Pricing Exhibit. Overage is invoiced within thirty (30) days of the end of the True-Up Period.

### B.3 Under-Use

> Volume below the Included Volume during the True-Up Period shall not refund. Up to twenty-five per cent (25 %) of the unused Included Volume may, at the Agency's discretion, roll forward into the next True-Up Period. Roll-forward expires at the end of the next True-Up Period.

### B.4 Material Divergence

> Where observed volume diverges from the volume forecast in the Pricing Exhibit by more than thirty per cent (30 %) over two consecutive True-Up Periods, either party may request a Commercial Review.

### B.5 Commercial Review

> A Commercial Review is held within thirty (30) days of the request. The parties review: forecast accuracy, root cause of divergence, future demand, and whether the Pricing Exhibit needs adjustment. The Pricing Exhibit may be amended only by written change order signed by both parties.

---

## Section C — Autonomy-Progression Price-Step

### C.1 Definition

> The Unit Price is subject to **Autonomy-Progression** adjustments as the Agent's autonomy matures.

### C.2 Step-Up (Better Economics for Buyer)

> Where the Intervention Rate is sustained at or below the Step-Up Threshold (**[T1 %]**) for three consecutive calendar months, the Unit Price shall move to the next lower tier in the Price-Step Schedule (Annex [BB]) at the start of the following calendar month.

### C.3 Step-Down (More Supervisor Recovery)

> Where the Intervention Rate is sustained at or above the Step-Down Threshold (**[T2 %]**) for three consecutive calendar months, the Unit Price shall move to the next higher tier in the Price-Step Schedule at the start of the following calendar month.

### C.4 Maximum Movement per Renewal Term

> The Unit Price shall not move by more than one tier in either direction in any single calendar quarter. Cumulative movement within a Renewal Term is reviewed at the Pre-Renewal Review.

### C.5 Sample Price-Step Schedule

| Tier | Trigger | Unit Price |
|---|---|---|
| Tier 1 (Ramp) | Intervention Rate ≥ 15 % sustained | [$ 1.05] |
| Tier 2 (Standard) | Intervention Rate 8–15 % | [$ 0.85] |
| Tier 3 (Mature) | Intervention Rate ≤ 8 % sustained | [$ 0.70] |
| Tier 4 (Optimised) | Intervention Rate ≤ 5 % sustained for 6 months | [$ 0.60] |

---

## Section D — Ramp-Down Protection

### D.1 Reduction Right

> At each Renewal Term, the Buyer may reduce the Included Volume by up to fifteen per cent (15 %) of the prior Term's Included Volume without re-priced Base Fee.

### D.2 Reductions Beyond 15 %

> Reductions beyond fifteen per cent (15 %) trigger a re-price of the Base Fee reflecting the reduced cost recovery, on notice of not less than sixty (60) days before the start of the Renewal Term.

### D.3 SLA-Class Reduction

> The Buyer may not reduce the SLA Class at renewal without a corresponding adjustment to the Base Fee. SLA-Class reductions require thirty (30) days' notice and Agency confirmation that the lower SLA Class can be operationally honoured for the engagement.

### D.4 Engagement Wind-Down

> Where the Buyer reduces volume by more than forty per cent (40 %), the Agency may at its option treat the renewal as a wind-down and offer a wind-down Term of up to twelve (12) months at the existing Base Fee, with Buyer's right to exit during the wind-down on sixty (60) days' notice.

---

## Section E — Index-Linked Renewal

### E.1 Annual Price Reset

> At the start of each Renewal Term, the Base Fee, the Unit Price (subject to Autonomy-Progression), and the Overage Rate may be adjusted by an Index-Linked Increase, capped at the **lower** of:
>
> (a) CPI for the Buyer's primary country of operation + three per cent (3 %); and
>
> (b) Model-Provider-Price-Index + two per cent (2 %),
>
> with a minimum movement of zero per cent (0 %) in any year.

### E.2 Model-Provider-Price-Index

> The Model-Provider-Price-Index is computed by reference to the published list prices of the named Sub-Processors (Annex [SP-1]) for the model families used in the engagement, weighted by the trailing twelve-month usage share, with evidence in the annual statement.

### E.3 Margin Floor

> The Index-Linked Increase shall not be reduced below the level required for the Agency to maintain its Margin Floor. Where the cap in clause E.1 would breach the Margin Floor, the parties shall conduct a Commercial Review under clause B.5.

### E.4 Buyer Protection Floor

> The Index-Linked Increase shall not be applied in a calendar year where CPI for the Buyer's primary country of operation is at or below zero per cent (0 %).

### E.5 Notice

> The Agency shall give the Buyer notice of the Index-Linked Increase not less than sixty (60) days before the start of the Renewal Term, with evidence of the CPI and the Model-Provider-Price-Index calculation.

---

## Section F — FX Corridor at Renewal

### F.1 Reference Rate

> The Reference Rate is the **[CENTRAL BANK]** reference rate for **[LOCAL CURRENCY]** against United States Dollars on the last business day of the month preceding the invoice month.

### F.2 Corridor

> Where the Reference Rate moves by more than fifteen per cent (15 %) against the rate at the Effective Date over any rolling twelve-month period, either party may request a Commercial Review under clause B.5.

### F.3 Sustained Movement

> Sustained movements outside the Corridor are not absorbed by the Agency. The Agency may propose, and the Buyer may accept, a partial USD-denomination of the Base Fee to mitigate FX exposure on the model-cost component.

---

## Section G — Worked Examples

### G.1 Step-Up Example
- Initial Unit Price: $0.85 (Tier 2).
- Intervention Rate observed in Jan–Mar at 6 %, 5 %, 4 %.
- Trigger: ≤ 8 % sustained for 3 months → move to Tier 3.
- April Unit Price: $0.70.

### G.2 Step-Down Example
- Tier 2 Unit Price $0.85.
- Intervention Rate observed in Jan–Mar at 17 %, 18 %, 16 %.
- Trigger: ≥ 15 % sustained for 3 months → move to Tier 1.
- April Unit Price: $1.05.

### G.3 Index-Linked Renewal Example
- Year-end CPI in Kenya: 7.5 %. CPI + 3 % = 10.5 %.
- Model-Provider-Price-Index: 4 %. Index + 2 % = 6 %.
- Cap = min(10.5 %, 6 %) = 6 %.
- Renewal-Term Base Fee increase: 6 %.

### G.4 FX Corridor Example
- Effective Date USD/KES: 130.
- Observed USD/KES at month 14: 160.
- Movement: +23 % over 12 months.
- Corridor breach (> 15 %).
- Either party may invoke Commercial Review.
