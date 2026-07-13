---
name: ai-agent-intervention-credit-and-abort-refund
description: Use when defining intervention credits, abort rights, or refund mechanics for an agent engagement; use the SLA skill for broader credits and the outcome-pricing skill for success fees.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent Intervention Credit and Abort-Refund
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The pricing pattern depends on the agent operating without human intervention beyond an agreed ceiling.
- The buyer's procurement team has asked: "what happens if your agent fails?"
- The proposal must show, contractually, that the buyer does not pay full price for tasks where the human did the work.
- The buyer wants an honest exit if the agent does not reach autonomy in a reasonable time.
- The agency wants to demonstrate skin-in-the-game without giving away margin.

## Do Not Use When

- The pricing pattern is per-step or per-agent with included volume and no intervention sensitivity.
- The engagement is a fixed-fee build with no operational agent.

## Domain Inputs

- The intervention rate ceiling (from the autonomy ramp curve).
- The pricing pattern and the unit price.
- The supervisor cost per intervention.
- The credit cap the agency can absorb in a single month without breaching margin floor.
- The buyer's reporting cadence and the monthly statement format.
- The list of refund triggers the agency is willing to commit to.
- The pro-rata refund formula.

## Domain Method

1. Set the **intervention rate ceiling** per the autonomy ramp curve. The ceiling should be a number the agent is expected to be inside of, with margin — not a stretch number.
2. Write the **intervention-credit formula** — when monthly intervention rate exceeds the ceiling, the buyer receives a credit on the units billed for that month.
3. Set the **credit cap** — typically 25 % of units billed per month, or the SLA-class cap for unified credits.
4. Define the **customer-facing visibility** — the monthly statement shows tasks attempted, tasks completed without intervention, intervention rate, ceiling, credit applied, evidence-link to audit log.
5. Write the **abort-and-refund clause** — the buyer's exit when the agent's autonomy ramp fails or when an irreversible-action incident occurs. Pro-rata refund of unused fees; no implementation-fee refund except where milestone-tied.
6. Write the **refund triggers** explicitly — list each, with definition, evidence, and the calculation.
7. Stress-test the intervention-credit exposure at three intervention rates (P50 / P90 / P99) against the cost stack — confirm margin floor holds.
8. Output the **Intervention Credit Clause** and the **Abort-and-Refund Clause** for the financial proposal and the MSA.

## The Intervention-Credit Formula

The default formula:

> If the Intervention Rate in any calendar month exceeds the agreed Ceiling, the Buyer shall receive a credit equal to **C %** of the Unit Fees billed for that month for every **P percentage points** above the Ceiling, up to a maximum credit of **M %** of the monthly Unit Fees.

Typical calibration:
- **Ceiling** — 10 % (Silver), 8 % (Gold), 5 % (Platinum), softer in the first three months of the ramp.
- **C** — 1 % credit per 1 percentage-point breach (stepped variant: 2 % above 5 ppts; 5 % above 10 ppts).
- **M** — 25 % cap (Silver), 50 % cap (Gold), 100 % cap (Platinum).

The credit is the agency's commitment that the buyer carries no more supervision cost than agreed. It is not a discount; it is the price of the supervision overhead the buyer paid that month.

### Worked Example

- Pricing: $0.85 per resolution. Ceiling 10 %. C = 1 %. M = 25 %.
- Month observed intervention rate = 18 %. Breach = 8 ppts. Credit = 8 % of monthly Unit Fees.
- Monthly Unit Fees = $68,000. Credit = $5,440. The buyer's net invoice is $62,560 plus base.

### Customer-Facing Monthly Statement

```
Tenant: ACME
Period: April 2026
Tasks attempted: 80,000
Tasks completed without intervention: 65,600 (82.0 %)
Intervention rate observed: 18.0 %
Ceiling: 10.0 %
Breach: 8.0 ppts
Unit Fees billed: $68,000
Intervention Credit applied: $5,440 (8.0 % of Unit Fees)
Net Unit Fees: $62,560
Base Fee: $25,000
Total invoice: $87,560
Audit-log evidence-link: <agent-audit/2026-04>
```

The customer-facing visibility is the difference between "we honour our SLAs" and "we never seem to credit anyone".

## The Abort-and-Refund Clause

The buyer may exit the engagement with pro-rata refund of unused prepaid fees on any of the following triggers:

| Trigger | Definition | Refund |
|---|---|---|
| Irreversible-Action Incident at Agency fault | An agent action with material adverse effect on the Buyer or a third party where the cause is determined by the named investigation process to be at the Agency's fault. | Pro-rata refund of unused subscription; implementation fees refunded only against unmet milestones. |
| Intervention overshoot, sustained | Monthly Intervention Rate above the Ceiling for sixty (60) consecutive days, after written notice and a thirty (30) day remediation window. | Pro-rata refund of unused subscription; intervention credits already issued retained by the Buyer; the engagement winds down. |
| Regulator Action | A regulator with jurisdiction over the Buyer or the Agent's actions issues an order to pause, restrict, or terminate the Agent. | Pro-rata refund; joint review; the Agency may credit the Buyer's next engagement against this refund. |
| Model-provider sustained outage | A named upstream Sub-Processor is unavailable for the relevant service for more than the agreed window (e.g. seven (7) consecutive days) and the Agency has not invoked the agreed fall-back. | Pro-rata refund of the affected window. |
| Audit-log breach | Audit-log completeness falls below the SLA floor for two consecutive months without remediation. | Pro-rata refund of the affected window plus a credit equal to ten per cent (10 %) of monthly fees. |

Refunds are pro-rata against unused subscription. Implementation fees are not refundable past defined milestones. The buyer's right to abort is in addition to any service credits already issued.

## Pro-Rata Refund Formula

```
Refund = Prepaid Subscription Fees × (Unused Days in Period / Total Days in Period)
```

For multi-tenant engagements, refunds are computed per affected tenant. For multi-agent engagements, refunds are computed per affected agent persona unless the abort is engagement-wide.

## Quality Standards

- Intervention rate ceiling is a number, not a phrase.
- The formula has a stated C, P, and M.
- The credit cap is named.
- The customer-facing monthly statement shape is shown.
- The abort triggers are named, defined, and have evidence.
- The pro-rata formula is explicit.
- Implementation-fee refundability is named.
- The audit log is the evidence source for every trigger.
- The agency has stress-tested the credit exposure against margin floor.

## Domain Risks

- "We will work with the Buyer in good faith on intervention" — buyer reads no credit.
- Credit formula with no cap — margin floor blown.
- Credit applied invisibly on the invoice — buyer cannot see the SLA being honoured.
- Abort triggers vague ("material failure") — disputes endless.
- Refund clause without the pro-rata formula — disputes endless.
- Implementation-fee refundability silent — buyer assumes everything refunds.
- Audit log absent as evidence — disputes default to the louder party.
- Intervention rate ceiling set at the autonomy stretch target — agency credit-bleeds while the ramp is still climbing.

## Domain Outputs

- Intervention Credit Clause (drop-in).
- Abort-and-Refund Clause (drop-in).
- Refund Triggers Schedule.
- Pro-Rata Refund Formula.
- Customer-Facing Monthly Statement Template.
- Stress-test memo against margin floor.

## Anti-Patterns

- Quoting an unverified commercial term. Fix: trace it to the approved brief or contract record and label any unresolved variable.
- Billing an attempted task as a completed outcome. Fix: define the eligible event, exclusions, reversal window, and evidence source.
- Leaving credits, refunds, or liability uncapped. Fix: state the eligible fee base, cap, trigger, exclusions, and approval owner.
- Updating one exhibit while dependent terms still conflict. Fix: reconcile pricing, SLA, credit, refund, renewal, and liability provisions together.
- Removing a legal placeholder without authority. Fix: retain the marker, name the decision owner, and require qualified review before issue.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| priced task definition, intervention evidence, and fault allocation | Buyer, proposal owner, approved contract record, or measured operating evidence | Yes | Stop before making a commitment; list the missing evidence and provide only a qualified option set. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Intervention-credit schedule and abort/refund clause | Finance, legal, and contract operations | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| intervention-credit schedule and abort/refund clause | Finance, legal, and contract operations | Assumptions, measures, authority, exclusions, and acceptance tests are explicit and traceable to the supplied evidence. |

## Capability Contract

Minimum capability is read access to the approved commercial record and calculation support for any stated formula. Drafting authority permits edits only inside the requested proposal or contract working copy. Do not sign, publish, spend, change production configuration, concede liability, or represent legal approval without explicit authority. Legal and tax conclusions require qualified review.

## Degraded Mode

Fallback when tools are unavailable: use the qualified path below.

If source terms, telemetry, calculation tools, or legal review are unavailable, return the narrowest useful marked draft: identify unverified variables, preserve placeholders, show the calculation method where possible, and mark each unavailable check as not assessed. Never convert missing evidence into approval.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Apply credit or abort remedy | Test measured intervention and incident evidence against agreed triggers and caps. | Double recovery or an unsupported refund. |
| Evidence is incomplete or positions conflict | Stop commitment drafting, record the conflict, and request the named owner’s decision. | Invented terms, double recovery, or an unauthorised concession. |
| Evidence and authority are complete | Draft, cross-check dependent exhibits, and retain the calculation or clause trace. | An internally inconsistent commercial package. |

## Workflow

1. Confirm the consumer, authority, controlling commercial record, and required inputs; stop when a baseline or accountable owner is missing.
2. Reproduce relevant calculations and identify conflicts across pricing, SLA, credit, refund, renewal, liability, and scope; stop when a formula cannot be reproduced.
3. Apply the domain method and decision rules within delegated authority, recording assumptions and exclusions.
4. Draft the contracted output and cross-check every dependent exhibit; recover by reconciling the controlling term with its owner and rerunning the calculation.
5. Verify acceptance conditions, evidence trace, legal-review markers, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

Monthly intervention is 14% against a 10% ceiling. Apply the agreed formula to the eligible fee base, cap the credit, and retain the evidence line used in the customer statement.

<!-- dual-compat-end -->

## References

- [ai-agent-credit-and-refund-clauses](../../profiles-sectors/references/ai-agent-credit-and-refund-clauses.md) — drop-in language.
- [ai-agent-abandonment-and-refund-policy-template](../../profiles-sectors/references/ai-agent-abandonment-and-refund-policy-template.md) — customer-facing policy.
- [ai-agent-pricing-models-reference](../../profiles-sectors/references/ai-agent-pricing-models-reference.md) — pattern-by-pattern intervention credit examples.
- [ai-agent-sla-exhibit-template](../../profiles-sectors/references/ai-agent-sla-exhibit-template.md) — SLA exhibit alignment.
- [ai-agent-sla-and-credit-schedule](../ai-agent-sla-and-credit-schedule/SKILL.md) — SLA class and credit cap consistency.
- [ai-agent-pricing-and-packaging-proposal](../../ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md) — patterns.
- [ai-agent-business-case-and-roi](../../ai-agent-proposals/ai-agent-business-case-and-roi/SKILL.md) — downside scenario sizing.
