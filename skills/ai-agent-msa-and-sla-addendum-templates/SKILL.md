---
name: ai-agent-msa-and-sla-addendum-templates
description: Use when the MSA and SLA need agent-specific addendums. Extends `saas-msa-dpa-sla-template-language` with the agent overlay — action accountability, audit-log retention and replay availability, kill-switch SLA, fee-for-evidence-pack on dispute, sub-cap for irreversible-action liability, model-provider force-majeure, agent-identity warranty, intervention SLA, and the SLA-credit interaction with the base SaaS SLA. Provides drop-in MSA addendum and drop-in SLA addendum.
---

# AI-Agent MSA and SLA Addendum Templates
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The engagement is contracted on the agency's standard SaaS MSA (or the buyer's MSA) and needs an agent-specific addendum.
- The buyer's legal team has requested explicit language on action accountability, audit-log retention, kill-switch SLA, and liability allocation for agentic action.
- The bid is in a regulated vertical and the MSA must reflect regulator expectations (named accountability for automated decisioning, citizen redress, clinical safety).
- The SaaS MSA already exists with the buyer and the agent is being added under that MSA via an addendum or schedule.

## Do Not Use When

- The engagement is non-agent (use `saas-msa-dpa-sla-template-language`).
- The engagement is a one-off study with no operational deliverable.

## Required Inputs

- The base MSA (the agency's or the buyer's).
- The chosen pricing pattern and packaging shape.
- The SLA class and credit schedule.
- The action catalogue with reversibility classification.
- The kill-switch architecture and drill log.
- The audit-log completeness, retention period, and replay window.
- The model-provider sub-processor list.
- The agency's legal-team starting positions on liability, indemnity, insurance.
- The buyer's regulator and the regulator's expectations on automated decisioning.

## Workflow

1. Read the base MSA and identify which standard clauses need an agent overlay — Scope of Services, Fees and Payment, Warranties, Liability, Indemnity, Insurance, Term and Termination, IP, Confidentiality, Sub-Processors, Audit, Force Majeure, Dispute Resolution.
2. Draft the **MSA Addendum** with the eight agent-specific clauses (below). The addendum overrides the base MSA only where named.
3. Draft the **SLA Addendum** with the four agent metrics + three guardrails + credit schedule + out-clauses (from `ai-agent-sla-and-credit-schedule`).
4. Run the **internal consistency pass** — addendum references match the pricing exhibit, the SLA class table, the refund triggers, the audit-log SLA, the kill-switch SLA.
5. Tailor named placeholders — currency, jurisdiction, reference rate, model providers, autonomy ramp, retention, replay window, sub-cap.
6. Hand to the agency's legal team for sign-off before submission.

## The Eight Agent-Specific MSA Clauses

### 1. Action Accountability
The Agent is operated by the Agency on behalf of the Buyer within the Action Catalogue. The Buyer retains accountability for actions the Buyer authorises through the Action Catalogue and approves through the Buyer's named approvers for irreversible actions. The Agency retains accountability for the Agent operating within the Action Catalogue, the autonomy commitment per action class, the kill-switch SLA, and the audit-log completeness SLA. Actions outside the Action Catalogue are not authorised; if attempted, the Agency is accountable for the breach and the consequences.

### 2. Audit Log Retention and Replay Availability
The Agency shall maintain an Action Audit Log capturing, for every Agent action: decision, tool call, parameters, result, reasoning trace where feasible, human approval where applicable, timestamp, identity, tenant, and outcome. Audit-log completeness shall be at or above the SLA-class threshold. Retention period shall be no less than the longer of seven (7) years or the period required by the Buyer's regulator. Replay shall be available within the SLA-class window on the Buyer's request, the Buyer's regulator's request, or the Agency's own dispute review.

### 3. Kill-Switch SLA
The Agency operates a Kill-Switch that suspends the Agent within the SLA-class time-to-stop on authorised command. The named authority chain (with after-hours coverage), the drill cadence (quarterly minimum), and the drill log are in the Trust and Compliance Annex. The Kill-Switch may be invoked by the Buyer's named officers, the Agency's Agent Safety Lead, or the relevant regulator.

### 4. Fee-for-Evidence-Pack on Dispute
On the Buyer's request for a forensic evidence pack outside the routine monthly statement (typically because of a dispute, an incident, or a regulator inquiry), the Agency shall produce the pack within the agreed SLA window. The first two evidence packs per calendar year are included; thereafter the Agency may charge a documented Evidence-Pack Fee at standard professional rates. Evidence packs required because of an Agency-fault Irreversible-Action Incident are at the Agency's cost.

### 5. Sub-Cap for Irreversible-Action Liability
Notwithstanding the base MSA's general liability cap, the Agency's liability for an Irreversible-Action Incident (defined in the Trust and Compliance Annex) shall be capped at the lower of (a) the value of the action and (b) twelve (12) months of fees paid under this engagement, except where the cause is the Agency's gross negligence, wilful misconduct, or breach of the named irreversibility-gating obligations, in which case the cap is the base MSA general cap. Indemnity for third-party claims arising from an Agency-fault Irreversible-Action Incident applies above this sub-cap up to the general cap.

### 6. Model-Provider Force-Majeure
Where a named upstream model-provider Sub-Processor declares an outage of the relevant model family for more than the agreed window, the corresponding SLA is suspended for the affected window. The Agency commits to multi-provider fall-back where the Buyer has accepted the model-routing-policy variation; otherwise the Buyer accepts the single-provider exposure. Force-Majeure does not relieve either party of the obligation to pay undisputed fees up to the date of the event and does not suspend the Kill-Switch SLA or the Audit-Log Completeness SLA, both of which remain in force.

### 7. Agent-Identity Warranty
The Agency warrants that every external communication initiated by the Agent (email, chat, voice call, ticket, posted message, regulatory filing) discloses the Agent's identity in line with applicable rules — AI Act Article 50 where applicable, the buyer's regulator's transparency-to-affected-party rules, and the agency's own Responsible-AI Agent Commitment. The Agency warrants that the Agent will not impersonate a named human, will not claim authority it does not have, and will route to a named human for actions outside the Action Catalogue.

### 8. Intervention SLA and Supervisor Cost Allocation
The Agency commits to the Intervention SLA — time-to-human escalation — at the SLA-class threshold. Where the Buyer's procurement instinct treats the Agent as a replacement for FTE, the supervisor cost the Buyer retains (people on the oversight queue, on-call, escalation engineer) is the Buyer's cost; the Intervention Credit Clause in the Pricing Exhibit reduces the per-resolution price when intervention rate exceeds the agreed Ceiling, compensating the Buyer for that retained supervisor cost.

## The SLA Addendum

The SLA Addendum is `../references/ai-agent-sla-exhibit-template.md`, attached to the MSA. It defines:

- SLA Class (Bronze / Silver / Gold / Platinum) and the four metric thresholds.
- Kill-switch, audit-log completeness, intervention SLAs (the three guardrails).
- Credit formulas, cap, monthly statement format.
- Out-clauses (model-provider force-majeure, customer-fault, regulator-pause).
- Reporting cadence and audit rights.
- Termination right at consecutive misses.

## Quality Standards

- The addendum names the base MSA it modifies and the precedence of conflicting terms.
- Every clause references named annexes — Action Catalogue, Trust and Compliance Annex, Pricing Exhibit, SLA Exhibit.
- The sub-cap for irreversible-action liability is named with a number.
- The fee-for-evidence-pack is named with included-pack allowance and SLA window.
- The model-provider force-majeure names the providers and the outage window.
- The agent-identity warranty is concrete.
- The legal team has signed off.

## Anti-Patterns

- Submitting the SaaS MSA without an addendum and hoping the buyer notices.
- Drafting the addendum without the Trust and Compliance Annex it points at.
- Stating "appropriate audit log retention" without a number.
- Stating "we will maintain a kill-switch" without an SLA.
- Sub-cap absent — the agency is exposed to general-cap liability on the agent's worst day.
- Fee-for-evidence-pack absent — the agency drowns in unfunded forensic requests after the first dispute.
- Agent-identity warranty absent — regulator transparency rules in jeopardy.

## Outputs

- MSA Addendum (drop-in).
- SLA Addendum (drop-in).
- Annexes referenced — Action Catalogue, Trust and Compliance Annex, Pricing Exhibit, SLA Exhibit.
- Legal-team sign-off record.

## References

- `../references/ai-agent-msa-addendum-template.md` — drop-in MSA addendum.
- `../references/ai-agent-sla-exhibit-template.md` — drop-in SLA addendum / exhibit.
- `../references/ai-agent-credit-and-refund-clauses.md` — credits and refunds.
- `../references/ai-agent-vendor-cost-pass-through.md` — pass-through language.
- `../references/ai-agent-dispute-resolution-and-audit-rights.md` — dispute and audit rights.
- `../references/saas-msa-dpa-sla-template-language.md` — base SaaS MSA / DPA / SLA.
- `../ai-agent-sla-and-credit-schedule/SKILL.md` — SLA classes.
- `../ai-agent-contract-language-pack/SKILL.md` — full contract pack assembly.
- `../ai-agent-compliance-credentials/SKILL.md` — Trust and Compliance Annex.
