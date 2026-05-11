# AI-Agent Vendor Cost Pass-Through

Drop-in language for vendor cost pass-through, indexed pricing, foundation-model-provider price changes, and sovereign-AI pass-through. Pairs with `../ai-agent-pricing-and-packaging-proposal/SKILL.md` and `ai-agent-pricing-exhibit-template.md`.

The pass-through exists because an agent fans out many model calls per task. A model-price increase that is invisible in a copilot can be catastrophic in an agent. The clause is the agency's protection against shock, capped to protect the buyer against arbitrary increase.

---

## Section A — Pass-Through Formula

### A.1 Sub-Processor List

> The Agent's named Sub-Processors are listed in Annex [SP-1], identifying for each: (i) name; (ii) role (model inference / tool-call API / vector store / compute / sovereign-AI); (iii) region of processing; (iv) the current published list price for the model families used; (v) the contractual notice period for price changes; (vi) the fallback Sub-Processor.

### A.2 Pass-Through Trigger

> Where the unit cost of model inference, tool-call API access, or compute services charged to the Agency by a named Sub-Processor increases by more than **ten per cent (10 %)** on a rolling twelve-month basis, the Agency may pass through the increase to the Buyer.

### A.3 Pass-Through Mechanics

> The Agency shall:
> (a) provide the Buyer with **sixty (60) days' written notice** of the proposed increase;
> (b) include with the notice the Sub-Processor's published list-price evidence and the calculation;
> (c) cap the pass-through at the verified Sub-Processor increase;
> (d) maintain the Margin Floor and not exceed the Annual Cap.

### A.4 Annual Cap

> Cumulative pass-through in any contract year shall not exceed the **lower** of:
> (i) CPI for the Buyer's primary country of operation + three per cent (3 %); and
> (ii) Model-Provider-Price-Index + two per cent (2 %),
> with the Margin Floor.

### A.5 Margin Floor

> The Margin Floor is the minimum operating margin the Agency requires to deliver the Agent at the agreed SLA Class. The Margin Floor is not disclosed to the Buyer but operates as the agency's veto on absorbing increases beyond the Annual Cap. Where an increase would breach the Margin Floor, the parties shall conduct a Commercial Review.

### A.6 Buyer Objection

> The Buyer may, within thirty (30) days of the notice, object to the pass-through by providing evidence that:
> (i) the Sub-Processor's published list price has not changed by the amount stated;
> (ii) a substantially equivalent Sub-Processor is available at a lower price; or
> (iii) the Agency has not maintained the Sub-Processor disclosure obligation.
>
> A valid objection requires the Agency to revise the pass-through or, where the parties cannot agree, to invoke the Commercial Review.

---

## Section B — Sovereign-AI Provider Pass-Through

Where the Buyer has elected (or the regulator has required) a Sovereign-AI deployment — a model hosted inside the Buyer's country of operation by a named sovereign provider — the pass-through has distinct mechanics.

### B.1 Sovereign Provider Schedule

> The Sovereign-AI Provider Schedule (Annex [SAI-1]) names: (i) the sovereign provider; (ii) the model family and version; (iii) the country of hosting; (iv) the price per unit at the Effective Date; (v) the contractual notice period for price changes; (vi) the data-residency commitment; (vii) the fallback (which may be a different sovereign provider or, by Buyer agreement, a global provider during outage).

### B.2 Sovereign Pass-Through Premium

> The Sovereign-AI price typically carries a premium over the global model providers reflecting data-residency, dedicated infrastructure, and regulatory compliance. The Effective-Date premium is documented in Annex [SAI-1] and is fixed for the Initial Term.

### B.3 Sovereign Pass-Through Trigger

> Pass-through for the Sovereign Provider follows the same mechanics as clause A.2 above, except the trigger is any price increase by the Sovereign Provider regardless of the 10 % threshold, given the typically less competitive sovereign market.

### B.4 Buyer Right to Revert

> Where the Sovereign Provider's price increases by more than fifteen per cent (15 %) in any twelve-month period, the Buyer may, with regulator approval, revert to a global model provider on ninety (90) days' notice. The Agency shall cooperate in the migration and shall maintain the Audit Log continuity.

### B.5 Failure-Mode Fall-Back

> Where the Sovereign Provider is unavailable for the relevant model family for more than **forty-eight (48) hours**, the Agency may, with the Buyer's prior written consent, route to the named global fallback. Where the Buyer's regulator does not permit fall-back, the Agency invokes the Model-Provider Force-Majeure clause.

---

## Section C — Tool-Call and Compute Pass-Through

### C.1 Tool-Call APIs

> Where the Agent calls a third-party tool API (search, translation, KYC, sanctions, payment gateway, document storage), the cost of those calls is included in the Unit Price up to the Tool-Call Allowance. The Tool-Call Allowance is set out in Annex [TC-1]. Tool-call usage above the Allowance is passed through at the third-party rate plus a documented administrative percentage.

### C.2 Compute and Storage

> Compute (vCPU-hours, GPU-hours), vector store, and audit-log storage costs are included in the Base Fee at expected volume. Where actual volume exceeds the Compute Envelope (Annex [CE-1]) by more than thirty per cent (30 %), the Agency may pass through the verified excess.

### C.3 Embedding Costs

> Embedding costs are included in the Unit Price for the standard embedding model. Where the Buyer elects a higher-dimensional embedding (e.g. for improved retrieval), the differential cost is passed through.

---

## Section D — Indexed Pricing (Optional Variant)

Where the parties prefer to skip the rolling pass-through and use an indexed price reset annually, the following variant applies:

### D.1 Indexed Reset

> The Unit Price and Base Fee shall reset annually on the anniversary of the Effective Date by the **lower** of:
> (a) CPI for the Buyer's primary country of operation + three per cent (3 %); and
> (b) Model-Provider-Price-Index + two per cent (2 %).

### D.2 Mid-Term Adjustment

> Within a contract year, no pass-through applies except where the cumulative Sub-Processor list-price increase exceeds **twenty per cent (20 %)**, in which case the Agency may invoke an emergency pass-through under clause A.

### D.3 Evidence

> The Agency shall publish, with each annual statement, the CPI source and the Model-Provider-Price-Index calculation, including the trailing twelve-month usage share by model family.

---

## Section E — Africa-Context FX Clause

Where the Buyer's fees are denominated in a local currency (KES, NGN, UGX, RWF, ZAR, TZS, GHS, EGP, MAD, etc.) and the model costs are denominated in USD:

### E.1 Reference Rate

> The Reference Rate is the **[CENTRAL BANK]** reference rate for the local currency against USD on the last business day of the month preceding the invoice month.

### E.2 FX Corridor

> Where the Reference Rate moves by more than **fifteen per cent (15 %)** against the rate at the Effective Date over any rolling twelve-month period, either party may request a Commercial Review. The Agency does not absorb sustained FX shocks beyond the Corridor.

### E.3 USD Sleeve (Optional)

> Where the Buyer elects, a portion of the Base Fee (up to fifty per cent (50 %), reflecting the USD model-cost share) may be denominated and invoiced in USD, removing FX exposure on that portion. Local-currency invoicing remains for the supervisor, eval, and operations components.

### E.4 Hedging

> The Agency may, at its own cost, hedge its USD model-cost exposure. The Buyer is not required to contribute to hedge cost beyond the Annual Cap in clause A.4.

---

## Section F — Anti-Patterns

- **"Subject to change at any time"** — procurement reads this as no commitment.
- **"At our discretion"** — same.
- **Pass-through without a cap** — buyer protection collapses.
- **Pass-through without notice** — buyer is ambushed.
- **Pass-through without evidence** — disputes endless.
- **No fallback Sub-Processor** — buyer has no alternative when the provider fails.
- **No Margin Floor** — agency absorbs shocks; the engagement fails on margin.
- **No FX clause in an Africa-context deal** — the FX shock destroys the engagement.

---

## Section G — Quality Checklist

- [ ] Sub-Processor list named with current list prices and contractual notice.
- [ ] Pass-through trigger numbered.
- [ ] Notice period stated.
- [ ] Evidence requirement explicit.
- [ ] Annual Cap formula stated.
- [ ] Margin Floor named (internally; not necessarily in contract).
- [ ] Buyer objection mechanism present.
- [ ] Sovereign-AI variant included where the buyer has sovereign requirement.
- [ ] Tool-call and compute envelope present.
- [ ] FX Reference Rate and Corridor present for Africa-context deals.
