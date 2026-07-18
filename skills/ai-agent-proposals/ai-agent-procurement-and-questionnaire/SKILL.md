---
name: ai-agent-procurement-and-questionnaire
description: Use when answering or pre-empting an AI-agent procurement questionnaire on autonomy, action scope, reversibility, kill switches, audit logs, identity, subprocessors, and governance.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent Procurement and Questionnaire
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The buyer has issued an AI-agent-specific procurement questionnaire, or an AI questionnaire with an agentic annex.
- The agency wants to pre-empt the questionnaire with a procurement-grade answer pack inside the proposal.
- The bid is in a regulated vertical, an AI-Act jurisdiction, or a public-sector procurement.
- The buyer's CISO, DPO, general counsel, or head of supervision is the deciding evaluator.

## Do Not Use When

- The questionnaire is non-agent (use `ai-on-saas-procurement-and-questionnaire`).

## Domain Inputs

- The buyer's questionnaire (if issued).
- The compliance credentials posture from `ai-agent-compliance-credentials`.
- The action catalogue, autonomy commitment, reversibility classification.
- The kill-switch architecture and drill log.
- The intervention SLO and audit-log SLA.
- The agent identity policy and red-team catalogue.
- The sub-processor list (models + tool-call APIs).

## Domain Method

1. Read the questionnaire. Categorise each question into one of the **ten agent procurement domains** (below). Where a domain is unaddressed, **volunteer the answer** — procurement teams reward proactivity on agentic concerns.
2. Where a question cannot be answered affirmatively, give the **honest staged answer** — today / in-progress with date / committed for this engagement / out of scope with rationale. Do not fabricate.
3. Cross-link every answer to the methodology, the risk register, the action catalogue, and the kill-switch drill log so the answer is internally consistent.
4. Output the **Agent Questionnaire Response Pack** as a standalone document or an annex to the Trust and Compliance section.

## The Ten Agent Procurement Domains

### 1. Autonomy Level and Action Scope
- For each agent and each action class, the autonomy level (L0–L5) committed at go-live and the trajectory.
- The action catalogue published and signed.
- The reversibility classification of each action.
- The scope-confinement architecture (tool allowlist, parameter bounds, value bounds, time-window, tenant scope).

### 2. Oversight and Intervention
- Oversight model per action class (HITL / HOTL / audit).
- Intervention SLA (how fast a human can intervene; how the agent behaves while waiting).
- Oversight-queue staffing model and on-call coverage.
- Escalation tree from supervisor to safety lead to SteerCo.

### 3. Irreversibility Gating
- Every irreversible action requires a named human approver.
- Value-bound transaction confirmation (e.g. transactions above $X require dual approval; agent cannot bypass).
- Dry-run pattern (where applicable) before commit.
- Reversibility classification kept current via change-control.

### 4. Kill-Switch and Drill
- Kill-switch architecture (per-action, per-agent, per-tenant, global).
- Named authority chain with after-hours coverage.
- Drill cadence (quarterly minimum).
- Drill log available to the buyer / auditor / regulator.
- Time-to-stop SLA.

### 5. Audit Log
- What is logged (decision, tool call, parameters, result, reasoning trace where feasible, human decision if any).
- Retention period.
- Completeness SLA (e.g. ≥ 99 %).
- Buyer / auditor / regulator access.
- Replay capability for forensic review.

### 6. Identity, Impersonation, Transparency-to-Affected-Party
- Agent identity model (own / service / delegated).
- External-communication disclosure (every outbound email, chat, or call discloses agent identity in line with applicable rules).
- AI Act Article 50-style transparency where applicable.
- Sectoral disclosure rules (e.g. financial-services advice rules; legal practice rules).

### 7. Model and Tool-Call Sub-Processors
- Model providers named (OpenAI, Anthropic, Google, AWS Bedrock, Azure OpenAI, Mistral, Cohere, open-weight self-hosted).
- Tool-call APIs named (third-party services the agent calls).
- For each: region of inference / processing, retention default, training-data posture, contractual notice, fallback.
- Sub-processor change-notification policy.

### 8. Eval, Red-Team, Drift
- Eval methodology, golden-dataset description, metric thresholds, refresh cadence.
- Agent red-team catalogue (prompt injection via tool output, scope manipulation, memory poisoning, multi-agent collusion, identity confusion).
- Drift watch and alerting.
- Regression harness in CI.

### 9. Multi-Agent Governance (where applicable)
- Orchestration pattern (manager-worker, planner-actor-critic, swarm).
- Inter-agent contract.
- Blast-radius limit.
- Anti-collusion guard.
- Replay determinism for audit.

### 10. Incident, Liability, Redress
- Agent incident classification and runbook.
- Regulator-notification triggers.
- Contractual liability allocation (who is liable for what; where insurance applies).
- Redress mechanism for affected users / customers / regulators with named owner and SLA.
- Public communications policy.

### 11. Commercial and Contractual Answers (Agent SLA, Credits, Refund, Audit Rights)
- SLA Class committed (Bronze / Silver / Gold / Platinum) with the four agent metrics + three guardrails.
- Credit Schedule per metric and aggregate Service-Credit Cap.
- Intervention-Credit Clause: ceiling, formula, customer-facing statement.
- Abort-and-Refund Triggers: Irreversible-Action Incident, Intervention overshoot, Regulator Action, Model-Provider sustained outage, Audit-Log Breach.
- Liability Sub-Cap for Irreversible-Action.
- Audit Rights on the Audit Log: cadence, independent-auditor substitute, Evidence-Pack Fee, allowance.
- Vendor Cost Pass-Through: trigger, notice, cap, evidence, Margin Floor.
- FX Corridor for the local currency / USD pair.
- Renewal: auto / express / hybrid; Ramp-Down Protection; Autonomy-Progression Price-Step; Index-Linked Renewal.
- See [ai-agent-procurement-objections-on-commercials](../../ai-agent-commercial/ai-agent-procurement-objections-on-commercials/SKILL.md) for trade-not-give responses to common procurement asks on these commercial dimensions.

## Quality Standards

- Every answer is honest, staged, and dated.
- Autonomy commitment is per action class, not per agent.
- Action catalogue is published.
- Kill-switch drill cadence and drill log are named.
- Audit-log completeness is a number.
- Sub-processor list names tool-call APIs as well as model providers.
- Multi-agent governance is addressed where the engagement is multi-agent.
- Liability allocation is named.
- Redress mechanism names an owner and SLA.
- Answers are internally consistent with the risk register and the compliance credentials.

## Domain Risks

- "Our agents comply with all applicable laws".
- Autonomy stated globally without per-action-class commitment.
- "Action catalogue available on request" — procurement reads this as not-yet-defined.
- Kill-switch named with no drill log.
- "Audit logs are available" with no completeness SLA.
- "Third-party AI providers" instead of named providers.
- Multi-agent governance skipped in multi-agent engagements.
- Liability allocation deferred to MSA negotiation without a starting position.

## Domain Outputs

- Agent Questionnaire Response Pack — ten-domain answer pack, drop-in ready.
- Action Catalogue (annex).
- Autonomy Commitment Matrix per action class.
- Kill-Switch Architecture and Drill Log statement.
- Intervention SLA statement.
- Audit-Log SLA statement.
- Sub-Processor Disclosure (models + tool-call APIs).
- Multi-Agent Governance statement (where applicable).
- Liability Allocation and Redress statement.

## Anti-Patterns

- Inventing a metric, credential, constraint, or buyer position. Fix: cite the supplied source or mark the item as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and state the evidence needed to resume.
- Advancing autonomy without a named gate owner. Fix: require observable evidence, accountable acceptance, and a rollback path.
- Reusing another sector or use case without reassessment. Fix: retest affected parties, action scope, reversibility, and jurisdiction.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: define an observable measure, threshold, evidence record, and decision owner.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| buyer questionnaire, proposed architecture, action catalogue, control evidence, and subprocessor register | Buyer evidence, ToR, approved discovery record, system owner, or measured operating data | Yes | Stop the affected decision; list the missing source and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Procurement answer pack and evidence index | Procurement, CISO, DPO, and legal counsel | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| procurement answer pack and evidence index | Procurement, CISO, DPO, and legal counsel | Every load-bearing claim traces to supplied evidence; assumptions, owners, gates, exclusions, and observable acceptance conditions are explicit. |

## Capability Contract

Default to read-only for discovery, analysis, review, and planning. Minimum capability is access to the supplied artefacts and permission to calculate or inspect evidence. Edit only the requested proposal working copy. Do not change production systems, contact affected parties, publish, spend, certify compliance, or approve autonomous action without explicit authority from the accountable owner.

## Degraded Mode

If files, interviews, telemetry, specialist review, network access, or calculation tools are unavailable, produce the narrowest useful qualified result. Mark each unavailable check as not assessed, separate facts from assumptions, lower confidence, and state the evidence needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Answer, qualify, or decline | Tie each answer to current scoped evidence; mark planned controls and owner-approved exceptions. | Fabricated compliance or ambiguous control ownership. |
| Required evidence, authority, or accountable owner is missing | Stop the affected recommendation or commitment and record the gap. | Invented evidence or unauthorised autonomy. |
| Gate evidence is complete and accepted | Advance only within the approved scope and retain the evidence trace. | Scope drift and irreproducible approval. |

## Workflow

1. Confirm the consumer, authority, neighbouring-skill route, and required inputs; stop when a mandatory source or accountable owner is missing.
2. Inspect the evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a failed safety, finance, regulatory, or acceptance gate.
3. Apply the domain method and decision rules within the qualified scope, retaining an evidence trace.
4. Draft the contracted output and reconcile it with methodology, work plan, staffing, pricing, risk, and governance; recover by revising the affected scope or control and rerunning the failed gate.
5. Verify acceptance conditions, permission boundaries, direct references, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

For a question on kill-switch testing, cite the dated drill record and recovery result. If no drill exists for the proposed environment, answer planned, name the owner, and state the gate before go-live.

<!-- dual-compat-end -->

## References

- [ai-agent-procurement-questionnaire-pack](../../profiles-sectors/references/ai-agent-procurement-questionnaire-pack.md) — long-form answer pack with sample language.
- [ai-agent-trust-and-compliance-template](../../profiles-sectors/references/ai-agent-trust-and-compliance-template.md) — trust section consistency.
- [ai-agent-responsible-ai-commitment](../../profiles-sectors/references/ai-agent-responsible-ai-commitment.md) — commitment consistency.
- [ai-agent-sla-class-table](../../profiles-sectors/references/ai-agent-sla-class-table.md) — SLA class and credit schedule (domain 11 evidence).
- [ai-agent-credit-and-refund-clauses](../../profiles-sectors/references/ai-agent-credit-and-refund-clauses.md) — credit and refund language (domain 11 evidence).
- [ai-agent-commercial-objection-handling](../../profiles-sectors/references/ai-agent-commercial-objection-handling.md) — procurement-objection responses.
- [ai-on-saas-procurement-questionnaire-pack](../../profiles-sectors/references/ai-on-saas-procurement-questionnaire-pack.md) — AI-on-SaaS questionnaire base.
- [ai-on-saas-procurement-and-questionnaire](../../ai-on-saas-proposals/ai-on-saas-procurement-and-questionnaire/SKILL.md) — AI-on-SaaS procurement (load alongside for SaaS-embedded agents).
- [ai-agent-compliance-credentials](../ai-agent-compliance-credentials/SKILL.md) — credentials matching the answers.
- [ai-agent-risk-and-responsible-ai](../ai-agent-risk-and-responsible-ai/SKILL.md) — risk consistency.
- [ai-agent-sla-and-credit-schedule](../../ai-agent-commercial/ai-agent-sla-and-credit-schedule/SKILL.md) — domain 11 SLA answers.
- [ai-agent-procurement-objections-on-commercials](../../ai-agent-commercial/ai-agent-procurement-objections-on-commercials/SKILL.md) — commercial objection handling.
