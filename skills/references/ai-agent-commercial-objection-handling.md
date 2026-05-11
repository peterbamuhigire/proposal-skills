# AI-Agent Commercial Objection Handling

Long-form responses to the ten common procurement objections on agent commercials. Pairs with `../ai-agent-procurement-objections-on-commercials/SKILL.md`. Maintain the trade-not-give discipline.

---

## Objection 1 — "We don't pay for failed tasks"

### What the buyer is protecting
The buyer does not want to pay the agency for the agent's mistakes. They have read about agents failing. They have a CFO who has seen AI vendors invoice for work that was redone by humans.

### Default response
The Intervention Credit Clause is exactly the protection the buyer is asking for. When the Intervention Rate exceeds the agreed Ceiling, the Buyer receives a credit on Unit Fees for that month. The buyer pays the Unit Price minus the credit, which is the price of the work the Agent actually did. The Audit Log evidences every Task — the Buyer can verify the count themselves. The Monthly Statement shows the credit applied.

### Trade
A stricter Ceiling (e.g. 5 % instead of 10 %) is available in exchange for: (i) a 3–6 month ramp window where the Ceiling is softer; or (ii) a higher Base Fee; or (iii) a longer commitment term.

### Decline
A pure "no pay for failed tasks" clause without an attribution test is unworkable. The Audit Log is the source of truth. The buyer cannot pay zero for Tasks where the Agent did 80 % of the work and a human did the last 20 %.

### Sample language for the response

> Our Pricing Exhibit already addresses this through the Intervention Credit Clause: when the Agent's monthly Intervention Rate exceeds the agreed Ceiling, the Unit Fees are reduced by a formula tied to the breach, up to a cap. The Audit Log evidences every Task, and the Monthly Statement shows the credit applied. We can tighten the Ceiling in exchange for a slower ramp window or a Base Fee uplift. We do not offer zero-pay on failed tasks, because the Audit Log evidences the work the Agent did even when a human had to finish.

---

## Objection 2 — "We want a price floor below the unit price"

### What the buyer is protecting
The buyer fears the agent will be slow to mature. They want the price-per-unit to drop if it is.

### Default response
The Performance-Corridor structure (Outcome-Pricing Structure 4) gives exactly that — the unit price slides on a band. At target performance, the Standard Rate. Below target, the price falls through documented steps to a Floor. Above target, the price rises to a Ceiling. The Floor is the agency's cost recovery.

### Trade
A wider corridor (e.g. 25 % below standard) is available in exchange for: (i) a longer commitment term (24–36 months); or (ii) volume guarantees; or (iii) a higher Base Fee.

### Decline
A floor below the agency's cost stack is unworkable. The agency cannot operate the Agent for less than the model calls, supervisor cost, eval, red-team, and audit-log cost.

---

## Objection 3 — "We want a price corridor on the SLA"

### What the buyer is protecting
The buyer wants the price to track SLA performance — pay less when the agent underperforms.

### Default response
The SLA Class Table already does this. Credits per metric per SLA Class. The price is reduced when the agent misses. The Service-Credit Cap protects both sides.

### Trade
An SLA-upside clause (a modest bonus on sustained over-performance) is available in exchange for: (i) a Credit-Cap reduction; or (ii) a longer term. The upside is genuinely a bonus, not a price increase by another name.

### Decline
A corridor that lets the price fall below the agency's Floor blows the margin. The Floor is non-negotiable.

---

## Objection 4 — "We want to audit the audit log"

### What the buyer is protecting
The buyer wants independent assurance that the Audit Log is real, complete, and tamper-evident.

### Default response
Audit-log audit rights are in the MSA Addendum and the Dispute Resolution Annex:
- Routine annual audit (twice annual for Gold and Platinum).
- Independent auditor's report (SOC 2 Type II, ISO 27001, ISO 42001) accepted as substitute.
- On-incident audit available.
- On-regulator audit available.
- Evidence-Pack mechanism with included allowance + documented fee.

### Trade
Twice-annual audit on Silver (regulated buyer in a non-Gold sector) is available in exchange for a documented audit-cost recovery clause.

### Decline
Unlimited audit rights without scope, scheduling, and SLA are unworkable. Open-ended access to Audit Log without a request mechanism is unworkable.

---

## Objection 5 — "We want a refund if the agent fails"

### What the buyer is protecting
The buyer wants an exit that returns money if the agent does not deliver.

### Default response
The Abort-and-Refund Clause names five triggers explicitly:
1. Irreversible-Action Incident at Agency fault.
2. Intervention Rate above Ceiling for 60 consecutive days.
3. Regulator Action the agency cannot remedy within 90 days.
4. Model-provider sustained outage of 7+ days where agency did not invoke fall-back.
5. Audit-Log completeness below threshold for 2 consecutive months without remediation.

Pro-rata refund of unused prepaid Subscription Fees. Implementation Fees refundable only against unmet milestones. Credits already issued are retained by the Buyer.

### Trade
A wider refund window (90 days of intervention overshoot instead of 60) is available in exchange for a longer remediation window (45 days instead of 30).

### Decline
"Refund if the agent fails to meet any commitment" is unworkable. Credits are the sole remedy for missed SLAs except where the named triggers apply.

---

## Objection 6 — "We want unlimited liability for agentic action"

### What the buyer is protecting
The buyer fears serious agentic harm and wants serious recovery.

### Default response
The MSA general cap (typically 12 months of fees, or a multiple thereof for material breaches) applies. The Irreversible-Action Sub-Cap in the MSA Addendum caps liability for an Agent-Fault Irreversible-Action Incident at the lower of (a) the action value and (b) 12 months of fees, except where the cause is gross negligence, wilful misconduct, or breach of the named irreversibility obligations — in which case the general cap applies. Indemnity for third-party claims operates above the Sub-Cap up to the general cap.

### Trade
An elevated general cap (e.g. 24 months of fees) is available in exchange for: (i) a higher price; or (ii) a higher SLA Class (with the eval / red-team / supervisor investment that goes with it).

### Decline
Uncapped liability is unworkable and uninsurable. The agency declines. The buyer's mitigation is the SLA Class and the Sub-Cap structure, not unlimited liability.

---

## Objection 7 — "We want indemnity for regulator action against the agent"

### What the buyer is protecting
The buyer fears a regulator fine and wants the agency to pay.

### Default response
The agency indemnifies for breach of named obligations — Action Accountability, Audit Log Completeness, Kill-Switch SLA, Agent-Identity Warranty. The agency does not indemnify the Buyer for: (i) the Buyer's use of the Agent outside the Action Catalogue; (ii) the Buyer's failure on its own regulator-facing obligations; (iii) regulator decisions not attributable to the agency's named obligations.

### Trade
Specific named regulator-action exposures (e.g. a data-residency breach due to agency-side configuration error) are indemnifiable.

### Decline
Open-ended regulator indemnity is unworkable. The agency is not the buyer's regulator counterparty.

---

## Objection 8 — "We want the model-cost increase absorbed by you"

### What the buyer is protecting
The buyer wants a price that does not move when the model provider raises prices.

### Default response
The Vendor-Cost-Pass-Through Clause caps pass-through at the verified provider increase, with notice (60 days), evidence (provider list-price changes), and an annual cap (CPI + 3 % or model-price-index + 2 %). The agency maintains a margin floor. The buyer is protected against arbitrary increases; the agency is protected against shock absorption.

### Trade
A pass-through deferral (the agency absorbs the first 5 % of any provider increase) is available in exchange for a small Base-Fee uplift.

### Decline
Full absorption is unworkable. An agent fans out 10–100 model calls per task. An invisible 30 % provider hike is catastrophic.

---

## Objection 9 — "We want unlimited audit-log retention"

### What the buyer is protecting
The buyer wants to investigate forever.

### Default response
Audit-log retention is the longer of seven (7) years and the Buyer's regulator-mandated period. Beyond seven years, the buyer can request continued retention at the agency's documented storage cost.

### Trade
Specific high-stakes action classes (e.g. transactions above a threshold) can have longer retention by default. Mass retention beyond seven years has a documented cost line.

### Decline
Open-ended retention without a cost mechanism is unworkable. Storage and access cost is real.

---

## Objection 10 — "We want to terminate without cause at any time, no refund clawback"

### What the buyer is protecting
The buyer wants maximum flexibility to exit.

### Default response
Termination for convenience is allowed with 90-day notice and pro-rata refund of unused prepaid Subscription Fees. Implementation Fees are not refundable past defined milestones.

### Trade
A shorter notice period (60 days) is available in exchange for: (i) a non-refundable advance on the first 3 months of the next renewal; or (ii) a higher Base Fee.

### Decline
Same-day termination with full refund of paid fees is unworkable. The agency is paying supervisor, eval, and red-team cost weekly.

---

## Cross-Cutting Discipline

- Every concession is traded for something of equivalent commercial value.
- Every decline is reasoned, not stonewalled.
- The agency is willing to lose a deal on uncapped liability, open-ended regulator indemnity, no-floor pricing, full absorption of model-cost increases.
- The buyer sees principled discipline. Principled discipline is itself a discriminator.
- The trade ledger is documented in the win-room file and signed off by the agency's legal and commercial leads.
