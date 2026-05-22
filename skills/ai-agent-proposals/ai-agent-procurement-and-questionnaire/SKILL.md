---
name: ai-agent-procurement-and-questionnaire
description: Use when responding to a buyer's AI-agent procurement questionnaire, or when the proposal must pre-empt the agent questionnaire with a procurement-grade answer pack. Covers autonomy level per use case, action catalogue, irreversibility classification, kill-switch architecture and drill cadence, scope-confinement evidence, agent identity and impersonation, audit-log access, sub-processor exposure for tool calls, multi-agent governance, and transparency-to-affected-party posture. Extends `ai-on-saas-procurement-and-questionnaire` with the agent overlay.
---

# AI-Agent Procurement and Questionnaire
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The buyer has issued an AI-agent-specific procurement questionnaire, or an AI questionnaire with an agentic annex.
- The agency wants to pre-empt the questionnaire with a procurement-grade answer pack inside the proposal.
- The bid is in a regulated vertical, an AI-Act jurisdiction, or a public-sector procurement.
- The buyer's CISO, DPO, general counsel, or head of supervision is the deciding evaluator.

## Do Not Use When

- The questionnaire is non-agent (use `ai-on-saas-procurement-and-questionnaire`).

## Required Inputs

- The buyer's questionnaire (if issued).
- The compliance credentials posture from `ai-agent-compliance-credentials`.
- The action catalogue, autonomy commitment, reversibility classification.
- The kill-switch architecture and drill log.
- The intervention SLO and audit-log SLA.
- The agent identity policy and red-team catalogue.
- The sub-processor list (models + tool-call APIs).

## Workflow

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
- See `../ai-agent-procurement-objections-on-commercials/SKILL.md` for trade-not-give responses to common procurement asks on these commercial dimensions.

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

## Anti-Patterns

- "Our agents comply with all applicable laws".
- Autonomy stated globally without per-action-class commitment.
- "Action catalogue available on request" — procurement reads this as not-yet-defined.
- Kill-switch named with no drill log.
- "Audit logs are available" with no completeness SLA.
- "Third-party AI providers" instead of named providers.
- Multi-agent governance skipped in multi-agent engagements.
- Liability allocation deferred to MSA negotiation without a starting position.

## Outputs

- Agent Questionnaire Response Pack — ten-domain answer pack, drop-in ready.
- Action Catalogue (annex).
- Autonomy Commitment Matrix per action class.
- Kill-Switch Architecture and Drill Log statement.
- Intervention SLA statement.
- Audit-Log SLA statement.
- Sub-Processor Disclosure (models + tool-call APIs).
- Multi-Agent Governance statement (where applicable).
- Liability Allocation and Redress statement.

## References

- `../references/ai-agent-procurement-questionnaire-pack.md` — long-form answer pack with sample language.
- `../references/ai-agent-trust-and-compliance-template.md` — trust section consistency.
- `../references/ai-agent-responsible-ai-commitment.md` — commitment consistency.
- `../references/ai-agent-sla-class-table.md` — SLA class and credit schedule (domain 11 evidence).
- `../references/ai-agent-credit-and-refund-clauses.md` — credit and refund language (domain 11 evidence).
- `../references/ai-agent-commercial-objection-handling.md` — procurement-objection responses.
- `../references/ai-on-saas-procurement-questionnaire-pack.md` — AI-on-SaaS questionnaire base.
- `../ai-on-saas-procurement-and-questionnaire/SKILL.md` — AI-on-SaaS procurement (load alongside for SaaS-embedded agents).
- `../ai-agent-compliance-credentials/SKILL.md` — credentials matching the answers.
- `../ai-agent-risk-and-responsible-ai/SKILL.md` — risk consistency.
- `../ai-agent-sla-and-credit-schedule/SKILL.md` — domain 11 SLA answers.
- `../ai-agent-procurement-objections-on-commercials/SKILL.md` — commercial objection handling.
