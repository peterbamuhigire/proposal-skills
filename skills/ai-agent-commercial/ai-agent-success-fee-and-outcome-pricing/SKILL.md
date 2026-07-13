---
name: ai-agent-success-fee-and-outcome-pricing
description: Use when structuring agent gain-share, success-fee, base-plus-success, or performance-corridor pricing; use the general pricing skill for per-step, per-agent, or usage rates.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent Success-Fee and Outcome-Pricing
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The buyer wants the agency to share commercial risk on the agent's outcomes (gain-share, success fee, hybrid).
- The buyer's procurement team has signalled they prefer outcome pricing to time-and-materials or to fixed subscription.
- The pricing pattern selected is B (Per-Outcome), F (Success-Based), or E (Hybrid) with a success component.
- The bid is competitive and outcome pricing is a discriminator the agency wants to deploy responsibly.

## Do Not Use When

- The pricing pattern is per-step or per-agent with no outcome component.
- The engagement is public sector (outcome pricing on citizen services is politically inappropriate; use Pattern D).
- The outcome cannot be attributed cleanly to the agent (attribution disputes will destroy the relationship).
- The agency's autonomy ramp and intervention rate are unproven (do the POC first; commit to outcome pricing afterwards).

## Domain Inputs

- The candidate outcome — what the agent delivers that the buyer measures.
- The buyer's baseline performance on that outcome (without the agent).
- Attribution rules — what events count as agent-driven and which do not.
- Cooling-off period — how long the outcome must hold before it is billable.
- Reversal definition — what undoes the outcome.
- Counter-example list — outcomes that look like success but are not.
- The agency's cost stack — model calls, supervisor, eval, red-team, drift, integration, contingency for credit and refund exposure.
- The success-fee cap and the unit floor.
- The dispute mechanism.

## Domain Method

1. Decide the **structure** — gain-share (share of value delivered above baseline), success fee (fee triggered on threshold), hybrid base-plus-success (base covers cost; success bonus adds margin), performance-corridor (price slides on a band of performance).
2. Write the **success definition** with the discipline below — a one-paragraph definition that names the unit, the event, the cooling-off, the reversal, the attribution test, and one counter-example.
3. Write the **base** — the floor under the agency that covers the cost stack. The base is not a discount; it is the price of being there.
4. Write the **success trigger** — the metric, the threshold, the measurement window, the evidence source (audit log, system of record, third-party).
5. Write the **cap** — outcome bonus is capped per period; success fee is capped per quarter or per annum.
6. Write the **downside protection** — what happens if the agent does not reach the threshold, if the buyer changes scope, if the regulator intervenes.
7. Write the **dispute mechanism** — attribution disputes raised within 60 days; reference to audit log; escalation to named operations leads; arbitration as final resort.
8. Stress-test the structure at three intervention rates (P50 / P90 / P99) and three volumes (light / medium / heavy). The base + worst-case success must cover the cost stack.
9. Output the **Outcome-Pricing Exhibit** as a drop-in clause.

## Four Outcome-Pricing Structures

### Structure 1 — Gain-Share
- The agency receives a share (typically 5–20 %) of the value delivered above an agreed baseline.
- Best for: debt recovery, churn save, fraud-loss reduction, claims-leakage reduction, scheduling optimisation, sales recovery.
- Worked example: 8 % of recovered debt above baseline recovery rate, with 30-day cooling-off.
- Downside protection: a base fee covering cost; cap on the gain-share at 200 % of base per quarter.

### Structure 2 — Success Fee (Threshold-Based)
- The agency receives a fee on the agent reaching a named threshold — autonomy %, intervention rate %, deflection rate %, CSAT, SLA-breach reduction.
- Best for: trust-building engagements where the buyer wants skin in the game.
- Worked example: base fee at 70 % of standard rate; success fee of 15 % on resolutions in any month where intervention rate ≤ 10 % and CSAT ≥ 4.3; cap of 30 % above base per quarter.
- Downside protection: base covers cost; threshold is binary; cap.

### Structure 3 — Hybrid Base-Plus-Success
- A base fee covers platform, oversight, eval, red-team, drift, kill-switch ops, supervisor curriculum. A success component adds bonus.
- Best for: enterprise buyers who want predictability with a performance tail.
- Worked example: base of $32k/month + bonus of $0.10/resolution above 10,000 resolutions/month in any month where intervention rate ≤ 12 %.
- Downside protection: base alone covers cost; success is genuinely a bonus.

### Structure 4 — Performance-Corridor
- The price per unit slides on a band: at target performance the price is the standard rate; below target the price falls to a floor; above target the price rises to a ceiling.
- Best for: mature engagements where the buyer wants the price to track performance.
- Worked example: $0.85/resolution at target intervention rate (10 %); $0.65/resolution if intervention rate is 15–20 %; $0.45/resolution if intervention rate > 20 %; $1.00/resolution if intervention rate ≤ 5 %; floor of $0.45 below 20 %; abort right above 25 % for 60 days.
- Downside protection: floor; abort right at the bottom of the corridor.

## Success-Definition Discipline (Counter-Example Rule)

Every outcome must survive the **counter-example rule**:

> Name one event that looks like the outcome but is not. If the definition cannot exclude that event, redraft.

Examples:
- Resolution = "ticket closed by the agent without reopen for 30 days". Counter-example: ticket auto-closed by inactivity. Redraft to exclude inactivity-closure.
- Recovered debt = "payment received". Counter-example: payment received and then chargeback within 60 days. Redraft to include 60-day cooling-off.
- Renewed policy = "policy active on the renewal date". Counter-example: policy active but in collection-default. Redraft to require premium paid.

The counter-example rule is the single biggest protection against attribution disputes. Build it into every definition. See [ai-agent-success-definition-language](../../profiles-sectors/references/ai-agent-success-definition-language.md) for the library of definitions and counter-examples.

## Downside Protections the Agency Always Reserves

- **Base covers cost** — the base fee, alone, covers the agent cost stack at expected volume. Success is bonus.
- **Cap on success** — per quarter and per annum, both.
- **Floor on units billed** — per month minimum (e.g. $25k floor) to cover quiet months.
- **Cooling-off** — outcomes do not pay until the cooling-off window passes without reversal.
- **Attribution log** — the audit log is the single source of truth for attribution; disputes default to the log.
- **Dispute window** — 60-day window to raise an attribution dispute; thereafter the outcome is final.
- **Scope-change re-price** — if the buyer changes the workflow, the action catalogue, or the data, the structure is re-priced.
- **Regulator pause / model-provider force-majeure** — outcomes do not pay during a pause attributable to upstream events.

## Quality Standards

- The outcome is defined with a counter-example.
- The base covers the cost stack alone.
- The success-fee cap is named.
- The unit floor is named.
- The cooling-off and reversal definitions are explicit.
- The attribution log is named as the source of truth.
- The dispute mechanism has an owner and an SLA.
- The structure has been stress-tested at three intervention rates and three volumes.
- The structure is in the financial proposal as an exhibit, not buried in prose.

## Domain Risks

- Outcome defined without a counter-example.
- "We share in the value created" with no attribution rule.
- Success fee dressed as a discount on base — the base is left underwater and the agency loses on every quiet month.
- Cap absent; the agency exposed to runaway success-bonus a hostile CFO will reverse.
- Cooling-off absent; reversals leak past billing.
- Attribution log unnamed; disputes become rhetorical.
- Public-sector outcome pricing on citizen services — politically inappropriate; use Pattern D instead.
- Outcome pricing committed before the autonomy ramp and intervention rate are proven in the POC.

## Domain Outputs

- Outcome-Pricing Structure (one of four), with rationale.
- Success Definition with counter-example rule applied.
- Outcome-Pricing Exhibit (drop-in).
- Downside-protection clauses.
- Stress-test memo at three intervention rates and three volumes.
- Dispute mechanism specification.

## Anti-Patterns

- Quoting an unverified commercial term. Fix: trace it to the approved brief or contract record and label any unresolved variable.
- Billing an attempted task as a completed outcome. Fix: define the eligible event, exclusions, reversal window, and evidence source.
- Leaving credits, refunds, or liability uncapped. Fix: state the eligible fee base, cap, trigger, exclusions, and approval owner.
- Updating one exhibit while dependent terms still conflict. Fix: reconcile pricing, SLA, credit, refund, renewal, and liability provisions together.
- Removing a legal placeholder without authority. Fix: retain the marker, name the decision owner, and require qualified review before issue.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| baseline outcome data, attribution rules, costs, and risk limits | Buyer, proposal owner, approved contract record, or measured operating evidence | Yes | Stop before making a commitment; list the missing evidence and provide only a qualified option set. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Outcome-pricing schedule | CFO, procurement, and legal | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| outcome-pricing schedule | CFO, procurement, and legal | Assumptions, measures, authority, exclusions, and acceptance tests are explicit and traceable to the supplied evidence. |

## Capability Contract

Minimum capability is read access to the approved commercial record and calculation support for any stated formula. Drafting authority permits edits only inside the requested proposal or contract working copy. Do not sign, publish, spend, change production configuration, concede liability, or represent legal approval without explicit authority. Legal and tax conclusions require qualified review.

## Degraded Mode

Fallback when tools are unavailable: use the qualified path below.

If source terms, telemetry, calculation tools, or legal review are unavailable, return the narrowest useful marked draft: identify unverified variables, preserve placeholders, show the calculation method where possible, and mark each unavailable check as not assessed. Never convert missing evidence into approval.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Select outcome-pricing structure | Use a measurable attributed outcome with reversal, cooling-off, floor, and cap rules. | Paying for noise or carrying uncapped delivery cost. |
| Evidence is incomplete or positions conflict | Stop commitment drafting, record the conflict, and request the named owner’s decision. | Invented terms, double recovery, or an unauthorised concession. |
| Evidence and authority are complete | Draft, cross-check dependent exhibits, and retain the calculation or clause trace. | An internally inconsistent commercial package. |

## Workflow

1. Confirm the consumer, authority, controlling commercial record, and required inputs; stop when a baseline or accountable owner is missing.
2. Reproduce relevant calculations and identify conflicts across pricing, SLA, credit, refund, renewal, liability, and scope; stop when a formula cannot be reproduced.
3. Apply the domain method and decision rules within delegated authority, recording assumptions and exclusions.
4. Draft the contracted output and cross-check every dependent exhibit; recover by reconciling the controlling term with its owner and rerunning the calculation.
5. Verify acceptance conditions, evidence trace, legal-review markers, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

For recovered arrears, charge a base covering operating cost plus a capped share of net cash retained after the cooling-off period, excluding disputed and reversed recoveries.

<!-- dual-compat-end -->

## References

- [ai-agent-outcome-pricing-clauses](../../profiles-sectors/references/ai-agent-outcome-pricing-clauses.md) — gain-share, success-fee, hybrid base-plus-success, performance-corridor language.
- [ai-agent-success-definition-language](../../profiles-sectors/references/ai-agent-success-definition-language.md) — outcome-definition library with counter-examples.
- [ai-agent-pricing-models-reference](../../profiles-sectors/references/ai-agent-pricing-models-reference.md) — patterns B, E, F.
- [ai-agent-pricing-and-packaging-proposal](../../ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md) — the six patterns.
- [ai-agent-business-case-and-roi](../../ai-agent-proposals/ai-agent-business-case-and-roi/SKILL.md) — cost stack and downside scenarios.
- [ai-agent-sla-and-credit-schedule](../ai-agent-sla-and-credit-schedule/SKILL.md) — SLA interaction with success fee.
- [premium-pricing-and-value-defense](../../strategy-positioning/premium-pricing-and-value-defense/SKILL.md) — premium fee defence.
