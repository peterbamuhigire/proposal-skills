---
name: ai-agent-risk-and-responsible-ai
description: Use when drafting an AI-agent risk register or responsible-AI commitment covering autonomous actions, irreversibility, scope, tool injection, identity, kill switches, and contestability.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent Risk and Responsible AI
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The proposal must present an agent risk register inside the Risk Analysis section.
- The buyer's CISO, DPO, general counsel, ethics committee, or regulator will review the proposal.
- The bid is in a regulated vertical or an AI-Act-relevant jurisdiction.
- The agency must demonstrate Responsible-AI agent practice — not promise it.
- An incumbent or competitor has had a public agentic incident the buyer will reference.

## Do Not Use When

- The engagement is non-agent (use `ai-on-saas-risk-and-responsible-ai` or `risk-management`).

## Domain Inputs

- The action catalogue with reversibility classification.
- The autonomy-level commitment per action class.
- The oversight model and intervention SLA.
- The regulator stance and jurisdiction(s).
- The kill-switch architecture and the named authority.
- The agent identity and impersonation policy.
- The sub-processor list (model providers, tool-call APIs).
- The buyer's escalation expectations.

## Domain Method

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

## Domain Risks

- "We follow Responsible AI principles" as the only commitment.
- Risks listed without triggers, owners, or escalation.
- Mitigations promised but not anchored in the methodology.
- Irreversibility treated as a UX concern.
- Kill-switch named but no drill cadence.
- "Audit log will be available" with no completeness SLA.
- Contestability deferred to "future work".
- Agent Safety Lead role unnamed.
- Multi-agent risk not addressed in multi-agent engagements.

## Domain Outputs

- Agent Risk Register (table form) — drop into proposal risk section or `risk-management`.
- Responsible-AI Agent Commitment subsection — drop into proposal `06-methodology` close or a standalone section.
- Regulator Mapping table.
- Kill-Switch Drill Cadence statement.

## Anti-Patterns

- Inventing a metric, credential, constraint, or buyer position. Fix: cite the supplied source or mark the item as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and state the evidence needed to resume.
- Advancing autonomy without a named gate owner. Fix: require observable evidence, accountable acceptance, and a rollback path.
- Reusing another sector or use case without reassessment. Fix: retest affected parties, action scope, reversibility, and jurisdiction.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: define an observable measure, threshold, evidence record, and decision owner.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| use cases, action catalogue, affected parties, threat evidence, jurisdiction, and risk appetite | Buyer evidence, ToR, approved discovery record, system owner, or measured operating data | Yes | Stop the affected decision; list the missing source and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Agent risk register and responsible-AI commitment | Risk owner, CISO, DPO, legal counsel, and evaluator | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| agent risk register and responsible-AI commitment | Risk owner, CISO, DPO, legal counsel, and evaluator | Every load-bearing claim traces to supplied evidence; assumptions, owners, gates, exclusions, and observable acceptance conditions are explicit. |

## Capability Contract

Default to read-only for discovery, analysis, review, and planning. Minimum capability is access to the supplied artefacts and permission to calculate or inspect evidence. Edit only the requested proposal working copy. Do not change production systems, contact affected parties, publish, spend, certify compliance, or approve autonomous action without explicit authority from the accountable owner.

## Degraded Mode

If files, interviews, telemetry, specialist review, network access, or calculation tools are unavailable, produce the narrowest useful qualified result. Mark each unavailable check as not assessed, separate facts from assumptions, lower confidence, and state the evidence needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Accept, mitigate, transfer, or avoid | Rate inherent risk, name controls and evidence, assign an owner, then assess residual risk against appetite. | A generic register that hides autonomous-action exposure. |
| Required evidence, authority, or accountable owner is missing | Stop the affected recommendation or commitment and record the gap. | Invented evidence or unauthorised autonomy. |
| Gate evidence is complete and accepted | Advance only within the approved scope and retain the evidence trace. | Scope drift and irreproducible approval. |

## Workflow

1. Confirm the consumer, authority, neighbouring-skill route, and required inputs; stop when a mandatory source or accountable owner is missing.
2. Inspect the evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a failed safety, finance, regulatory, or acceptance gate.
3. Apply the domain method and decision rules within the qualified scope, retaining an evidence trace.
4. Draft the contracted output and reconcile it with methodology, work plan, staffing, pricing, risk, and governance; recover by revising the affected scope or control and rerunning the failed gate.
5. Verify acceptance conditions, permission boundaries, direct references, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

An agent can alter a legacy account. Classify the action by reversibility and blast radius, require approval and rollback evidence, name the incident owner, and prohibit agentic mode until the residual risk is accepted.

<!-- dual-compat-end -->

## References

- [ai-agent-risk-register-for-proposals](../../profiles-sectors/references/ai-agent-risk-register-for-proposals.md) — full register template.
- [ai-agent-responsible-ai-commitment](../../profiles-sectors/references/ai-agent-responsible-ai-commitment.md) — full commitment template.
- [ai-agent-trust-and-compliance-template](../../profiles-sectors/references/ai-agent-trust-and-compliance-template.md) — trust section linkage.
- [ai-agent-procurement-questionnaire-pack](../../profiles-sectors/references/ai-agent-procurement-questionnaire-pack.md) — procurement answers consistent with the register.
- [ai-on-saas-risk-and-responsible-ai](../../ai-on-saas-proposals/ai-on-saas-risk-and-responsible-ai/SKILL.md) — AI-on-SaaS risk register (load alongside for SaaS-embedded agents).
- [risk-management](../../domain-delivery/risk-management/SKILL.md) — generic risk register discipline.
- [ai-agent-methodology](../ai-agent-methodology/SKILL.md) — methodology that anchors mitigations.
- [ai-agent-compliance-credentials](../ai-agent-compliance-credentials/SKILL.md) — trust and compliance posture.
- [ai-agent-procurement-and-questionnaire](../ai-agent-procurement-and-questionnaire/SKILL.md) — procurement answers.
