---
name: ai-agent-contract-language-pack
description: Use when selecting and adapting agent-specific contract exhibits for a proposal, MSA, or statement of work; use the addendum skill when drafting the full MSA/SLA overlay.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent Contract Language Pack
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The proposal stage has moved from value narrative to contractual language.
- Procurement, legal, or finance has asked for the actual clauses, not paragraph descriptions.
- The bid must include exhibit-grade language as annexes (Pricing Exhibit, SLA Exhibit, Refund Exhibit).
- The agency's legal team is preparing the MSA / SoW and needs a starting position.
- A competitive RFP requires drop-in commercial language.

## Do Not Use When

- The proposal is still at value-narrative stage and clauses would over-commit the agency (use `ai-agent-pricing-and-packaging-proposal` for paragraph-grade language).
- The engagement is non-agent (use `saas-msa-dpa-sla-template-language`).

## Domain Inputs

- The chosen pricing pattern and packaging shape.
- The SLA class and credit schedule.
- The autonomy-ramp curve.
- The kill-switch architecture and drill log.
- The audit-log completeness number and retention.
- The model-provider list and pass-through terms.
- The FX baseline and corridor.
- The buyer's governing-law and dispute-resolution preference.
- The agency's legal team's approved starting positions on liability, indemnity, insurance.

## Domain Method

1. Confirm the pricing pattern (`ai-agent-pricing-and-packaging-proposal`) and packaging shape (`ai-agent-commercial-packaging`). The pack adapts to both.
2. Confirm the SLA class (`ai-agent-sla-and-credit-schedule`).
3. Assemble the **contract pack** from the references below — pricing exhibit + SLA exhibit + credit/refund exhibit + MSA addendum + abandonment-and-refund policy + dispute resolution. Each is drop-in.
4. Tailor named placeholders — currency, jurisdiction, reference rate, model providers, autonomy ramp, kill-switch time, intervention rate ceiling, audit-log completeness, retention period.
5. Run the **internal consistency pass** — pricing, SLA, refund, MSA addendum all reference the same numbers, the same definitions, and the same evidence trail.
6. Hand the pack to the agency's legal team for sign-off before submission.
7. Output the **Contract Language Annex** for the proposal and a parallel **MSA / SoW Insertion Pack** for the legal team.

## The Contract Language Pack — Index

| Exhibit | Source reference | Purpose |
|---|---|---|
| Pricing Exhibit | [ai-agent-pricing-exhibit-template](../../profiles-sectors/references/ai-agent-pricing-exhibit-template.md) | Defines unit; states price per unit; included volumes; overage rates; floor; intervention credit; vendor pass-through; FX; fair-use. |
| SLA Exhibit | [ai-agent-sla-exhibit-template](../../profiles-sectors/references/ai-agent-sla-exhibit-template.md) | Defines the SLA class; commits the four agent metrics and the three guardrail SLAs; credit formulas; cap; out-clauses; reporting; termination right. |
| Credit and Refund Exhibit | [ai-agent-credit-and-refund-clauses](../../profiles-sectors/references/ai-agent-credit-and-refund-clauses.md) | Drop-in credit clauses (per-metric and per-event); refund clauses (irreversible-action, intervention overshoot, regulator action). |
| Abandonment-and-Refund Policy | [ai-agent-abandonment-and-refund-policy-template](../../profiles-sectors/references/ai-agent-abandonment-and-refund-policy-template.md) | Customer-facing policy on when the agency will abandon the deployment and refund. |
| MSA Addendum | [ai-agent-msa-addendum-template](../../profiles-sectors/references/ai-agent-msa-addendum-template.md) | Drop-in MSA addendum extending the SaaS MSA with action accountability, kill-switch SLA, replay availability, fee-for-evidence-pack on dispute, sub-cap for irreversible-action liability. |
| Dispute Resolution and Audit Rights | [ai-agent-dispute-resolution-and-audit-rights](../../profiles-sectors/references/ai-agent-dispute-resolution-and-audit-rights.md) | SLA dispute mechanics; audit-log audit rights; evidence-pack fee; escalation path. |
| Outcome-Pricing Exhibits | [ai-agent-outcome-pricing-clauses](../../profiles-sectors/references/ai-agent-outcome-pricing-clauses.md) | Gain-share, success-fee, hybrid base-plus-success language. |
| Vendor Cost Pass-Through | [ai-agent-vendor-cost-pass-through](../../profiles-sectors/references/ai-agent-vendor-cost-pass-through.md) | Pass-through formula, indexed pricing, sovereign-AI handling. |
| Success-Definition Language | [ai-agent-success-definition-language](../../profiles-sectors/references/ai-agent-success-definition-language.md) | How to define a resolution / outcome / action with counter-example rule and cooling-off. |
| Renewal and True-Up Clauses | [ai-agent-renewal-and-true-up-clauses](../../profiles-sectors/references/ai-agent-renewal-and-true-up-clauses.md) | Renewal mechanics; true-up; ramp-down protection; autonomy-progression price-step. |

## Trade-Not-Give Discipline

Every exhibit is drafted with a default position. The agency does not give away a default without trading it for something:

- Buyer wants a longer audit-log retention → agency trades against a fee-for-evidence-pack on dispute.
- Buyer wants higher SLA class → agency trades against package shape (move from Included to Add-on; from Add-on to Standalone).
- Buyer wants tighter intervention credit → agency trades against a longer cooling-off period in the outcome definition.
- Buyer wants uncapped credits → agency declines; credits are the sole remedy except where contract or law requires otherwise.
- Buyer wants no pass-through → agency declines; pass-through is the agency's protection against model-price shock.

## Quality Standards

- Every exhibit is internally consistent — same definitions, same numbers, same evidence trail.
- Every placeholder is named and filled.
- No "TBD" in submission-grade language.
- Pricing, SLA, credit, refund, MSA addendum reference the same autonomy ramp, the same intervention rate ceiling, the same audit-log completeness, the same retention.
- Legal team has signed off on the starting positions for liability, indemnity, insurance.
- The pack survives a procurement read without requiring the agency to "circle back".

## Domain Risks

- Submitting paragraph-grade pricing language as an "exhibit".
- Inconsistent numbers across exhibits (pricing says 15 % intervention ceiling; SLA says 12 %).
- Open placeholders in the submission ("rate to be agreed").
- Promising a clause in the cover letter that the legal team has not approved.
- Stapling the SaaS MSA on without the agent addendum.
- Drafting credits "in the spirit of partnership" instead of as a formula.
- Forgetting the FX corridor in an Africa-context engagement.

## Domain Outputs

- Contract Language Annex (proposal artefact).
- MSA / SoW Insertion Pack (for legal team).
- Internal-consistency checklist signed.
- Legal-team sign-off recorded.

## Anti-Patterns

- Quoting an unverified commercial term. Fix: trace it to the approved brief or contract record and label any unresolved variable.
- Billing an attempted task as a completed outcome. Fix: define the eligible event, exclusions, reversal window, and evidence source.
- Leaving credits, refunds, or liability uncapped. Fix: state the eligible fee base, cap, trigger, exclusions, and approval owner.
- Updating one exhibit while dependent terms still conflict. Fix: reconcile pricing, SLA, credit, refund, renewal, and liability provisions together.
- Removing a legal placeholder without authority. Fix: retain the marker, name the decision owner, and require qualified review before issue.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| approved commercial positions and governing documents | Buyer, proposal owner, approved contract record, or measured operating evidence | Yes | Stop before making a commitment; list the missing evidence and provide only a qualified option set. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Selected and adapted contract exhibits | Legal counsel and proposal lead | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| selected and adapted contract exhibits | Legal counsel and proposal lead | Assumptions, measures, authority, exclusions, and acceptance tests are explicit and traceable to the supplied evidence. |

## Capability Contract

Minimum capability is read access to the approved commercial record and calculation support for any stated formula. Drafting authority permits edits only inside the requested proposal or contract working copy. Do not sign, publish, spend, change production configuration, concede liability, or represent legal approval without explicit authority. Legal and tax conclusions require qualified review.

## Degraded Mode

Fallback when tools are unavailable: use the qualified path below.

If source terms, telemetry, calculation tools, or legal review are unavailable, return the narrowest useful marked draft: identify unverified variables, preserve placeholders, show the calculation method where possible, and mark each unavailable check as not assessed. Never convert missing evidence into approval.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Select an exhibit set | Map each negotiated commercial position to its controlling exhibit. | Contradictory or unnecessary clauses. |
| Evidence is incomplete or positions conflict | Stop commitment drafting, record the conflict, and request the named owner’s decision. | Invented terms, double recovery, or an unauthorised concession. |
| Evidence and authority are complete | Draft, cross-check dependent exhibits, and retain the calculation or clause trace. | An internally inconsistent commercial package. |

## Workflow

1. Confirm the consumer, authority, controlling commercial record, and required inputs; stop when a baseline or accountable owner is missing.
2. Reproduce relevant calculations and identify conflicts across pricing, SLA, credit, refund, renewal, liability, and scope; stop when a formula cannot be reproduced.
3. Apply the domain method and decision rules within delegated authority, recording assumptions and exclusions.
4. Draft the contracted output and cross-check every dependent exhibit; recover by reconciling the controlling term with its owner and rerunning the calculation.
5. Verify acceptance conditions, evidence trace, legal-review markers, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

The proposal includes outcome pricing and an intervention credit. Select the pricing, SLA, credit/refund, audit-rights, and dispute exhibits; flag every legal placeholder for counsel.

<!-- dual-compat-end -->

## References

- [ai-agent-pricing-exhibit-template](../../profiles-sectors/references/ai-agent-pricing-exhibit-template.md)
- [ai-agent-sla-exhibit-template](../../profiles-sectors/references/ai-agent-sla-exhibit-template.md)
- [ai-agent-credit-and-refund-clauses](../../profiles-sectors/references/ai-agent-credit-and-refund-clauses.md)
- [ai-agent-abandonment-and-refund-policy-template](../../profiles-sectors/references/ai-agent-abandonment-and-refund-policy-template.md)
- [ai-agent-msa-addendum-template](../../profiles-sectors/references/ai-agent-msa-addendum-template.md)
- [ai-agent-dispute-resolution-and-audit-rights](../../profiles-sectors/references/ai-agent-dispute-resolution-and-audit-rights.md)
- [ai-agent-outcome-pricing-clauses](../../profiles-sectors/references/ai-agent-outcome-pricing-clauses.md)
- [ai-agent-vendor-cost-pass-through](../../profiles-sectors/references/ai-agent-vendor-cost-pass-through.md)
- [ai-agent-success-definition-language](../../profiles-sectors/references/ai-agent-success-definition-language.md)
- [ai-agent-renewal-and-true-up-clauses](../../profiles-sectors/references/ai-agent-renewal-and-true-up-clauses.md)
- [ai-agent-pricing-and-packaging-proposal](../../ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md)
- [ai-agent-sla-and-credit-schedule](../ai-agent-sla-and-credit-schedule/SKILL.md)
- [ai-agent-commercial-packaging](../ai-agent-commercial-packaging/SKILL.md)
- [ai-agent-msa-and-sla-addendum-templates](../ai-agent-msa-and-sla-addendum-templates/SKILL.md)
- [10-financial-proposal](../../pipeline/10-financial-proposal/SKILL.md)
