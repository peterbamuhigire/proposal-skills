---
name: ai-agent-procurement-objections-on-commercials
description: Use when procurement, legal, or finance raises commercial objections specific to agentic engagements — "we don't pay for failed tasks", "we want a price floor", "we want a price corridor", "we want to audit the audit log", "we want a refund if the agent fails", "we want unlimited liability", "we want indemnity for regulator action", and similar. Provides the ten common procurement asks with ethical, trade-not-give responses that protect margin without breaking the relationship.
---

# AI-Agent Procurement Objections on Commercials
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- Procurement, legal, or finance has raised an objection on the commercial terms (pricing pattern, SLA class, credit schedule, refund clause, liability cap, audit rights).
- The proposal has reached negotiation and the agency must defend its commercial structure without folding.
- The competitive set is using aggressive commercial promises (per-resolution pricing with no floor; "uncapped SLA"; "we eat the model-cost shock").
- The agency wants to demonstrate principled commercial discipline as a discriminator.

## Do Not Use When

- The objection is technical or methodological (use `ai-agent-procurement-and-questionnaire`).
- The objection is on price level (use `premium-pricing-and-value-defense`).
- The objection is on scope (use `sales-discovery-and-objection-handling`).

## Required Inputs

- The procurement objection in the buyer's own words.
- The agency's commercial floor (margin floor, SLA-credit cap, liability sub-cap).
- The pricing pattern and SLA class.
- The buyer's competitive references (what they have heard from competitors).
- The agency's legal-team starting positions on liability and indemnity.

## Workflow

1. **Categorise** the objection to one of the ten common asks (below).
2. **Acknowledge** the concern in the buyer's frame (what they are protecting).
3. **Defend** the default position with the underlying reason.
4. **Trade** if a move is required — every concession is traded for something of equivalent commercial value.
5. **Document** the negotiated position in the contract pack so it survives the next negotiator.

## The Ten Common Procurement Asks

### Ask 1 — "We don't pay for failed tasks"
- Buyer frame: I don't want to pay for the agent's mistakes.
- Default: The Intervention Credit Clause already addresses this — when intervention rate exceeds the agreed Ceiling, the buyer receives a credit that compensates for the supervisor cost retained. The buyer pays the unit price minus the credit, which is the price of the work the agent actually did.
- Trade: If the buyer wants a stricter intervention ceiling, the agency can offer it in exchange for a 3–6 month ramp window where the ceiling is softer (and the credit accordingly lighter) while the agent learns.
- Decline: A pure "no pay for failed tasks" clause without an attribution test is unworkable — the audit log is the source of truth and the credit is the formula. The buyer cannot pay zero for tasks where the agent did 80 % of the work and a human did the last 20 %.

### Ask 2 — "We want a price floor below the unit price"
- Buyer frame: I want the price-per-resolution to fall if the agent is slow to mature.
- Default: The Performance Corridor (Structure 4 of outcome pricing) gives a sliding band — at target the standard rate; below target the price falls to a floor; above target the price rises to a ceiling. The floor is the agency's cost recovery.
- Trade: A wider corridor (e.g. 25 % below standard) is available in exchange for a longer commitment term, a higher base, or volume guarantees.
- Decline: A floor below the agency's cost stack is unworkable — the agency cannot operate the agent for free.

### Ask 3 — "We want a price corridor on the SLA"
- Buyer frame: I want the price tied to SLA performance.
- Default: The SLA Class Table already does this — credits per metric per SLA class. The price is reduced when the agent misses; the price does not rise above standard when the agent exceeds.
- Trade: An SLA-upside clause (small bonus on sustained over-performance) is available in exchange for a credit-cap reduction or a longer term.
- Decline: A corridor that lets the price fall below the floor blows the margin.

### Ask 4 — "We want to audit the audit log"
- Buyer frame: I want independent assurance that the audit log is real and complete.
- Default: Audit-log audit rights are in the MSA Addendum — annual audit, or independent auditor's report (SOC 2 Type II, ISO 27001), or on incident. The Fee-for-Evidence-Pack covers ad-hoc forensic requests beyond the included allowance.
- Trade: A twice-annual audit (regulated vertical) is available; the agency adds a documented audit-cost recovery clause.
- Decline: Unlimited audit rights without scope, scheduling, and SLA are unworkable.

### Ask 5 — "We want a refund if the agent fails"
- Buyer frame: I want an exit that returns the money.
- Default: The Abort-and-Refund Clause names the triggers (irreversible-action incident at agency fault; intervention overshoot for 60 days; regulator action; model-provider sustained outage; audit-log breach). Pro-rata refund of unused fees applies. Implementation fees are not refundable past defined milestones.
- Trade: A wider refund window (90 days of intervention overshoot instead of 60) is available in exchange for a longer remediation window.
- Decline: "Refund if the agent fails to meet any commitment" is unworkable — credits are the sole remedy for missed SLAs except where the named refund triggers apply.

### Ask 6 — "We want unlimited liability for agentic action"
- Buyer frame: If the agent does serious harm, I want to recover serious damages.
- Default: The MSA general cap (typically 12 months of fees, or a multiple thereof) applies. The Irreversible-Action sub-cap caps liability for an Agent-Fault Irreversible-Action Incident at the lower of the action value and 12 months of fees, except where the cause is gross negligence, wilful misconduct, or breach of named irreversibility-gating obligations — in which case the general cap applies. Indemnity for third-party claims operates above the sub-cap up to the general cap.
- Trade: An elevated cap (24 months of fees) is available in exchange for a higher price or a higher SLA class (which increases the agency's eval / red-team / supervisor investment).
- Decline: Uncapped liability is unworkable and uninsurable. The agency declines.

### Ask 7 — "We want indemnity for regulator action against the agent"
- Buyer frame: If the regulator fines me because of the agent, the agency should pay.
- Default: The agency indemnifies for breach of named obligations (action accountability, audit log completeness, kill-switch SLA, agent-identity warranty). The agency does not indemnify the buyer for the buyer's own use of the agent outside the Action Catalogue, the buyer's failure to maintain its own regulator-facing obligations, or regulator decisions that are not attributable to the agency's named obligations.
- Trade: Specific named regulator-action exposures (e.g. data residency breach due to agency-side configuration error) are indemnifiable; general regulator action is not.
- Decline: Open-ended regulator indemnity is unworkable.

### Ask 8 — "We want the model-cost increase absorbed by you"
- Buyer frame: I want a price that does not move when OpenAI raises prices.
- Default: The Vendor-Cost-Pass-Through Clause caps pass-through at the verified provider increase, with notice, evidence, and an annual cap (e.g. CPI + 3 % or model-price-index + N %). The agency maintains a margin floor; sustained provider price moves above the cap trigger a commercial review.
- Trade: A pass-through deferral (the agency absorbs the first 5 % of any provider increase) is available in exchange for a small base-fee uplift.
- Decline: Full absorption is unworkable — an agent fans out many model calls per task; an invisible 30 % provider hike is catastrophic.

### Ask 9 — "We want unlimited audit-log retention"
- Buyer frame: I want to be able to investigate forever.
- Default: Audit-log retention is seven (7) years or the buyer's regulator-mandated period, whichever is longer. Beyond seven years, the buyer can request continued retention at the agency's documented storage cost.
- Trade: Specific high-stakes action classes (e.g. transactions above a threshold) can have longer retention by default; mass retention beyond seven years has a documented cost.
- Decline: Open-ended retention without a cost mechanism is unworkable.

### Ask 10 — "We want to terminate without cause at any time, no refund clawback"
- Buyer frame: I want maximum flexibility.
- Default: Termination for convenience is allowed with 90-day notice and pro-rata refund of unused prepaid subscription; implementation fees are not refundable past defined milestones.
- Trade: A shorter notice period (60 days) is available in exchange for a non-refundable advance on the first three months of the next renewal.
- Decline: Same-day termination with full refund of paid fees is unworkable — the agency is paying supervisor and eval cost weekly.

## Trade-Not-Give Discipline

Every "yes" is traded for something. The agency does not yield commercial terms under pressure; it trades them for term, scope, volume guarantees, payment terms, SLA-class movement, or price.

Things the agency declines, even at the cost of the deal:
- Uncapped liability.
- Open-ended regulator indemnity.
- No floor on a per-resolution price.
- Full absorption of model-cost increases.
- Refund as "in the spirit of partnership" instead of a formula.

Things the agency trades:
- Stricter intervention ceiling for a softer ramp window.
- Higher SLA class for a higher price and/or longer term.
- Wider refund window for a longer remediation window.
- Twice-annual audit for a documented cost-recovery clause.
- Pass-through deferral for a base-fee uplift.

## Quality Standards

- Every objection has a categorised default position.
- Every trade has a stated cost.
- Every decline has a stated reason.
- The negotiated position is documented in the contract pack.
- No commercial concession is given without a trade.
- The buyer sees principled discipline, not stonewalling.

## Anti-Patterns

- Folding on liability because the deal is large.
- Agreeing to "good faith" credits instead of formulas.
- Promising unlimited audit rights without scheduling.
- Absorbing model-cost shocks to win the bid.
- Granting refunds beyond the named triggers.
- Trading away the audit-log retention floor.
- Stonewalling without offering a trade.

## Outputs

- Objection map for the engagement.
- Trade ledger for the negotiation.
- Updated contract pack reflecting the agreed positions.

## References

- `../references/ai-agent-commercial-objection-handling.md` — long-form objection responses.
- `../references/ai-agent-credit-and-refund-clauses.md` — credit and refund clauses.
- `../references/ai-agent-msa-addendum-template.md` — MSA addendum.
- `../references/ai-agent-vendor-cost-pass-through.md` — pass-through.
- `../references/ai-agent-dispute-resolution-and-audit-rights.md` — audit rights.
- `../ai-agent-sla-and-credit-schedule/SKILL.md` — SLA class.
- `../ai-agent-intervention-credit-and-abort-refund/SKILL.md` — intervention credit and abort.
- `../sales-discovery-and-objection-handling/SKILL.md` — generic objection handling.
- `../premium-pricing-and-value-defense/SKILL.md` — fee defence.
