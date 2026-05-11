---
name: ai-agent-risk-and-responsible-ai
description: Use when the AI-agent proposal must present an agent risk register and a Responsible-AI agent commitment that survives a CISO, DPO, general counsel, regulator, and ethics review. Provides the twelve-entry agent risk register (autonomy-action incident, irreversibility incident, accountability, scope-creep, multi-agent collusion, prompt-injection-via-tool-output, memory poisoning, regulator action on agentics, kill-switch failure, identity / impersonation, escalation overload, legacy-system damage) with triggers, mitigations, owners, escalation; plus the Responsible-AI agent commitment template (human-final for irreversibility, full audit log, contestability, kill-switch drill cadence, transparency-to-affected-party). Extends `ai-on-saas-risk-and-responsible-ai` with the agent overlay.
---

# AI-Agent Risk and Responsible AI
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The proposal must present an agent risk register inside the Risk Analysis section.
- The buyer's CISO, DPO, general counsel, ethics committee, or regulator will review the proposal.
- The bid is in a regulated vertical or an AI-Act-relevant jurisdiction.
- The agency must demonstrate Responsible-AI agent practice — not promise it.
- An incumbent or competitor has had a public agentic incident the buyer will reference.

## Do Not Use When

- The engagement is non-agent (use `ai-on-saas-risk-and-responsible-ai` or `risk-management`).

## Required Inputs

- The action catalogue with reversibility classification.
- The autonomy-level commitment per action class.
- The oversight model and intervention SLA.
- The regulator stance and jurisdiction(s).
- The kill-switch architecture and the named authority.
- The agent identity and impersonation policy.
- The sub-processor list (model providers, tool-call APIs).
- The buyer's escalation expectations.

## Workflow

1. Populate the **Twelve-Entry Agent Risk Register** (below). Each entry carries: risk name, description, likelihood, impact, trigger, mitigation, owner, escalation, residual.
2. Populate the **Responsible-AI Agent Commitment** section: scope, principles, governance forum, accountable role (Agent Safety Lead), human-final for irreversibility, full audit log, contestability, transparency-to-affected-party, kill-switch drill cadence, sign-off frequency.
3. Map the commitment to the named regulator(s): AI Act (high-risk articles where applicable), Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U guidance, Rwanda AI Policy, sectoral rules.
4. Pair every risk with a methodology mitigation in `ai-agent-methodology` and a procurement answer in the agent procurement pack.
5. Output the **Risk Analysis subsection** and the **Responsible-AI Agent Commitment subsection** of the proposal.

## The Twelve-Entry Agent Risk Register

| # | Risk | Description | Primary Mitigation |
|---|---|---|---|
| 1 | Autonomy-action incident | Agent acts wrongly inside its autonomy level (wrong refund, wrong escalation, wrong message) | Eval thresholds, intervention SLO, drift watch, rollback, prompt regression |
| 2 | Irreversibility incident | Agent takes an action that cannot be undone (payment, public statement, regulatory filing, deletion) | Reversibility classification, L1 gating on irreversible, human-final approval, value bounds, transaction confirmation token |
| 3 | Accountability dispute | A regulator, court, or counterparty seeks to hold a party liable for an agent action | Action audit log, contractual liability allocation, professional indemnity, redress mechanism |
| 4 | Scope creep | Agent's effective scope grows beyond the action catalogue through buyer requests or emergent behaviour | Action catalogue gate, change-control clause, monthly catalogue review, anomalous-action alerting |
| 5 | Multi-agent collusion / failure cascade | Agents in a system reinforce each other's errors or get stuck in loops | Orchestrator-level governance, blast-radius limit, loop detection, replay determinism, anti-collusion guard |
| 6 | Prompt injection via tool output | An external system returns content that injects instructions into the agent's context | Output filtering at tool boundary, system-prompt hardening, content provenance, capability minimisation |
| 7 | Memory poisoning | Persistent memory is corrupted (intentionally or accidentally) and biases future decisions | Memory scoping (per session, per tenant, per task), memory-write review, periodic memory audit, memory reset cadence |
| 8 | Regulator action on agentic system | Regulator suspends agentic operations, requires conformity assessment, imposes ban | Kill-switch, conformity readiness, sovereign-AI option, jurisdictional fallback, regulator-notification runbook |
| 9 | Kill-switch failure | Kill-switch fails in drill or in incident | Multi-layer kill-switch (per-action, per-agent, per-tenant, global), independent authority chain, quarterly drill, post-drill incident review |
| 10 | Identity / impersonation breach | Agent communicates externally without proper identity disclosure, or is mistaken for a human in violation of policy | Identity-and-impersonation policy, signature on every external communication, automated disclosure injection, regulator-aligned transparency |
| 11 | Escalation overload | Intervention rate exceeds supervisor queue capacity; cases time out; SLA breaches; users harmed | Intervention SLO, queue capacity floor, overflow plan, autonomy gating that backs off when queue is saturated |
| 12 | Legacy-system damage | Agent calls a tool that mutates a system in an unintended way (cascading effect, race condition, foreign-key explosion) | Tool-call allowlist with parameter bounds, value bounds, transaction wrapper, dry-run, post-call assertion, automatic rollback |

## Responsible-AI Agent Commitment — Section Structure

1. **Scope** — which agent(s) the commitment covers; which action classes; which tenants; which jurisdictions.
2. **Principles** — accountability, transparency, fairness, safety, privacy, human oversight, contestability, kill-switch readiness.
3. **Governance forum** — Agent Safety Council: who meets, how often, what they decide; agency-side and buyer-side roles.
4. **Accountable role** — **Agent Safety Lead** (named role) accountable for the commitment, with escalation to the SteerCo.
5. **Human-final on irreversibility** — every irreversible action requires a named human approver; the agent cannot complete an irreversible action without that approval.
6. **Full audit log** — every agent action is logged with the reasoning trace where feasible, the tool call, the parameters, the result, the human decision (if any). Audit completeness SLA ≥ 99 %.
7. **Contestability** — any affected user, tenant, or regulator can challenge an agent action through a named channel; SLA for response; a human is the decision-maker on contested actions.
8. **Transparency-to-affected-party** — when an agent communicates externally or takes an action that affects a third party, the third party is informed in line with applicable rules (e.g. AI Act Article 50-style transparency).
9. **Kill-switch readiness** — kill-switch architecture, named authority, drill cadence (quarterly minimum), post-drill review.
10. **Eval and red-team discipline** — golden datasets, thresholds, refresh cadence, regression harness, drift watch.
11. **Incident disclosure** — incident classification, notification timing, communications, redress.
12. **Sign-off frequency** — quarterly review by the Agent Safety Council; annual sign-off by the SteerCo.

## Regulator Mapping (illustrative)

| Regulator / standard | What it requires of agents | How the commitment addresses it |
|---|---|---|
| EU AI Act (high-risk) | Conformity assessment, post-market monitoring, transparency, human oversight, accuracy / robustness / cybersecurity | Action audit log, eval + red-team, human-final on irreversibility, conformity readiness, transparency-to-affected-party |
| Kenya NCAIS | Principles-based; accountability, transparency, fairness | Named accountable role; published model and agent cards; redress channel |
| Nigeria NAIS | Risk-based oversight; human accountability | Autonomy ladder; named authority on irreversible actions; audit log |
| South Africa AI policy / POPIA interaction | Automated decision-making with significant effects requires intervention | HITL on decisioning; contestability channel; data-subject rights honoured |
| Uganda NITA-U guidance | Data protection and digital trust | Audit log; sub-processor disclosure; data-residency option |
| Rwanda AI Policy | Sovereign-aware AI; transparency; accountability | Sovereign-AI option; transparency-to-affected-party; named accountable role |
| Sectoral — FS model-risk (SR 11-7-style) | Model inventory, independent validation, ongoing monitoring | Agent in the model inventory; eval discipline; drift watch; quarterly review |
| Sectoral — Healthcare admin | Non-clinical scope; HITL on clinical | Action catalogue confines agent to admin only; clinical actions excluded |
| Sectoral — Legal practice rules | Lawyer responsibility; client confidentiality | HITL on filing / advising; confidentiality bounded by tenant scope |

## Quality Standards

- Every risk has likelihood, impact, trigger, mitigation, owner, escalation, residual.
- Mitigations are anchored in the methodology, not invented for the proposal.
- Responsible-AI agent commitment is a section, not a sentence; it names an accountable role.
- The kill-switch drill cadence is set (quarterly minimum) and the first drill is in pilot.
- Human-final on irreversibility is committed and the named human authority is identified per action class.
- Transparency-to-affected-party is named, with the rule reference where applicable.
- Audit-log completeness SLA is a number.
- The commitment is auditable — the buyer's auditor can verify the audit log, the kill-switch drill log, the contestability log, the red-team scorecard.

## Anti-Patterns

- "We follow Responsible AI principles" as the only commitment.
- Risks listed without triggers, owners, or escalation.
- Mitigations promised but not anchored in the methodology.
- Irreversibility treated as a UX concern.
- Kill-switch named but no drill cadence.
- "Audit log will be available" with no completeness SLA.
- Contestability deferred to "future work".
- Agent Safety Lead role unnamed.
- Multi-agent risk not addressed in multi-agent engagements.

## Outputs

- Agent Risk Register (table form) — drop into proposal risk section or `risk-management`.
- Responsible-AI Agent Commitment subsection — drop into proposal `06-methodology` close or a standalone section.
- Regulator Mapping table.
- Kill-Switch Drill Cadence statement.

## References

- `../references/ai-agent-risk-register-for-proposals.md` — full register template.
- `../references/ai-agent-responsible-ai-commitment.md` — full commitment template.
- `../references/ai-agent-trust-and-compliance-template.md` — trust section linkage.
- `../references/ai-agent-procurement-questionnaire-pack.md` — procurement answers consistent with the register.
- `../ai-on-saas-risk-and-responsible-ai/SKILL.md` — AI-on-SaaS risk register (load alongside for SaaS-embedded agents).
- `../risk-management/SKILL.md` — generic risk register discipline.
- `../ai-agent-methodology/SKILL.md` — methodology that anchors mitigations.
- `../ai-agent-compliance-credentials/SKILL.md` — trust and compliance posture.
- `../ai-agent-procurement-and-questionnaire/SKILL.md` — procurement answers.
