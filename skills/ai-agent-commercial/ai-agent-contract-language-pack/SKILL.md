---
name: ai-agent-contract-language-pack
description: Use when the AI-agent proposal must drop contract-grade exhibit language into the financial proposal, the MSA, or the SoW. Curates the ready-to-paste exhibits — pricing exhibit, SLA exhibit, credit and refund exhibit, abandonment-and-refund policy, vendor-cost-pass-through, FX corridor, dispute resolution, audit rights for SLA metrics, action-accountability — and tells the writer which to deploy for which engagement shape.
---

# AI-Agent Contract Language Pack
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The proposal stage has moved from value narrative to contractual language.
- Procurement, legal, or finance has asked for the actual clauses, not paragraph descriptions.
- The bid must include exhibit-grade language as annexes (Pricing Exhibit, SLA Exhibit, Refund Exhibit).
- The agency's legal team is preparing the MSA / SoW and needs a starting position.
- A competitive RFP requires drop-in commercial language.

## Do Not Use When

- The proposal is still at value-narrative stage and clauses would over-commit the agency (use `ai-agent-pricing-and-packaging-proposal` for paragraph-grade language).
- The engagement is non-agent (use `saas-msa-dpa-sla-template-language`).

## Required Inputs

- The chosen pricing pattern and packaging shape.
- The SLA class and credit schedule.
- The autonomy-ramp curve.
- The kill-switch architecture and drill log.
- The audit-log completeness number and retention.
- The model-provider list and pass-through terms.
- The FX baseline and corridor.
- The buyer's governing-law and dispute-resolution preference.
- The agency's legal team's approved starting positions on liability, indemnity, insurance.

## Workflow

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
| Pricing Exhibit | `../references/ai-agent-pricing-exhibit-template.md` | Defines unit; states price per unit; included volumes; overage rates; floor; intervention credit; vendor pass-through; FX; fair-use. |
| SLA Exhibit | `../references/ai-agent-sla-exhibit-template.md` | Defines the SLA class; commits the four agent metrics and the three guardrail SLAs; credit formulas; cap; out-clauses; reporting; termination right. |
| Credit and Refund Exhibit | `../references/ai-agent-credit-and-refund-clauses.md` | Drop-in credit clauses (per-metric and per-event); refund clauses (irreversible-action, intervention overshoot, regulator action). |
| Abandonment-and-Refund Policy | `../references/ai-agent-abandonment-and-refund-policy-template.md` | Customer-facing policy on when the agency will abandon the deployment and refund. |
| MSA Addendum | `../references/ai-agent-msa-addendum-template.md` | Drop-in MSA addendum extending the SaaS MSA with action accountability, kill-switch SLA, replay availability, fee-for-evidence-pack on dispute, sub-cap for irreversible-action liability. |
| Dispute Resolution and Audit Rights | `../references/ai-agent-dispute-resolution-and-audit-rights.md` | SLA dispute mechanics; audit-log audit rights; evidence-pack fee; escalation path. |
| Outcome-Pricing Exhibits | `../references/ai-agent-outcome-pricing-clauses.md` | Gain-share, success-fee, hybrid base-plus-success language. |
| Vendor Cost Pass-Through | `../references/ai-agent-vendor-cost-pass-through.md` | Pass-through formula, indexed pricing, sovereign-AI handling. |
| Success-Definition Language | `../references/ai-agent-success-definition-language.md` | How to define a resolution / outcome / action with counter-example rule and cooling-off. |
| Renewal and True-Up Clauses | `../references/ai-agent-renewal-and-true-up-clauses.md` | Renewal mechanics; true-up; ramp-down protection; autonomy-progression price-step. |

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

## Anti-Patterns

- Submitting paragraph-grade pricing language as an "exhibit".
- Inconsistent numbers across exhibits (pricing says 15 % intervention ceiling; SLA says 12 %).
- Open placeholders in the submission ("rate to be agreed").
- Promising a clause in the cover letter that the legal team has not approved.
- Stapling the SaaS MSA on without the agent addendum.
- Drafting credits "in the spirit of partnership" instead of as a formula.
- Forgetting the FX corridor in an Africa-context engagement.

## Outputs

- Contract Language Annex (proposal artefact).
- MSA / SoW Insertion Pack (for legal team).
- Internal-consistency checklist signed.
- Legal-team sign-off recorded.

## References

- `../references/ai-agent-pricing-exhibit-template.md`
- `../references/ai-agent-sla-exhibit-template.md`
- `../references/ai-agent-credit-and-refund-clauses.md`
- `../references/ai-agent-abandonment-and-refund-policy-template.md`
- `../references/ai-agent-msa-addendum-template.md`
- `../references/ai-agent-dispute-resolution-and-audit-rights.md`
- `../references/ai-agent-outcome-pricing-clauses.md`
- `../references/ai-agent-vendor-cost-pass-through.md`
- `../references/ai-agent-success-definition-language.md`
- `../references/ai-agent-renewal-and-true-up-clauses.md`
- `../ai-agent-pricing-and-packaging-proposal/SKILL.md`
- `../ai-agent-sla-and-credit-schedule/SKILL.md`
- `../ai-agent-commercial-packaging/SKILL.md`
- `../ai-agent-msa-and-sla-addendum-templates/SKILL.md`
- `../10-financial-proposal/SKILL.md`
