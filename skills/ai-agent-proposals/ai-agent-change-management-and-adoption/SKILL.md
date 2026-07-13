---
name: ai-agent-change-management-and-adoption
description: Use when planning workforce adoption, trust staging, supervisor training, affected-party disclosure, or contestability for agents that act on a buyer's behalf.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent Change Management and Adoption
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The AI-agent engagement changes how people do work — agents take actions previously taken by humans, or take actions humans previously did not have capacity to take.
- The buyer's workforce includes the role(s) the agent is augmenting, redeploying, or — rarely and only with care — replacing.
- Union, works-council, staff-association, or regulator-facing communications are required.
- The buyer has had a bad experience with previous automation, RPA, or chatbots that were announced as "augmentation" and behaved as "replacement".
- The agent communicates externally on the buyer's behalf and the disclosure UX (the way affected parties are told they are dealing with an agent) is part of the deliverable.

## Do Not Use When

- The engagement is non-agent (use `ai-on-saas-change-management-and-adoption` or `change-management`).

## Domain Inputs

- Affected user populations per agent (counts, roles, locations, contracts).
- Buyer's communications posture (proactive, reactive, silent).
- Union / works-council / staff-association presence and consultation rules.
- Regulator-facing transparency obligations.
- Existing change-management forum and sponsor.
- Autonomy-level commitment per action class.
- Reversibility classification of agent actions.

## Domain Method

1. Run the base change-management discovery, then layer the **seven agent-specific concerns**: existential anxiety (jobs), trust under autonomy, oversight workload, accountability, escalation expectations, retraining cadence, external-disclosure UX.
2. Build the **Agent Adoption Plan** — for each agent, name the affected internal users, the augment / redeploy / retrain framing, the trust-building stages, the oversight design, the escalation path, the retraining communications, the external-disclosure UX, the adoption metric.
3. Draft the **Augment-Redeploy-Retrain Communications Brief** — honest framing of what changes. If a role is reduced, the buyer says so with timing and support; if a role is augmented, the buyer says how; if a role shifts from doer to supervisor, the buyer says what the supervisor's new authority is.
4. Design the **Trust Staging Plan** with named evidence per stage:
   - **Shadow** — the agent proposes; the human acts. Evidence: agreement rate, disagreement-class analysis. Communication: "the agent is learning; you remain the decision maker."
   - **Confirm** — the agent acts on the human's confirmation. Evidence: confirmation latency, override rate. Communication: "the agent does the keystrokes; you decide."
   - **Supervised** — the agent acts on reversible actions; the human confirms irreversible. Evidence: intervention rate, irreversibility incidents (zero). Communication: "the agent handles the routine; you handle the exception."
   - **Agentic** — the agent acts on reversible without confirmation. Irreversibles remain HITL. Evidence: task-success, intervention rate at ceiling, contestability cases. Communication: "the agent handles the work end-to-end; you supervise the queue."
5. Specify the **Supervisor Retraining Curriculum** — moving from doer to supervisor is not a renaming; it is a re-skill. The curriculum covers reading agent reasoning, judging abstain, intervening fast, using the contestability channel, and reading the audit log. The curriculum is funded; the cost is in the financial proposal.
6. Specify the **Union / Works-Council / Staff-Association Communications** where applicable — consultation cadence, evidence pack (action catalogue, autonomy commitment, oversight model, retraining curriculum, redeployment plan), escalation, redress.
7. Specify the **External Communications Plan** — what affected customers / citizens / counterparties are told about the agent; the disclosure UX (every external message identifies the agent in line with applicable rules); the contestability channel; the redress path.
8. Specify the **Adoption Metrics**:
   - Internal: feature adoption, intervention-rate trend, override rate, abstain-correctness, supervisor satisfaction (CSAT for supervisors), supervisor capacity headroom, contestability case load.
   - External: affected-party satisfaction, escalation rate to human, complaint rate, redress SLA performance.
9. Output the **Agent Adoption Plan** subsection of the proposal's change-management section.

## The Augment-Redeploy-Retrain Framing — Why Honest Wins

Agents change jobs. Pretending otherwise loses union trust, loses regulator trust, and loses adoption inside the workforce that has to make the agent work. The proposal commits to a framing per affected role:

- **Augment** — the role remains; the agent removes the routine load and the human focuses on the complex. Use only where the volume justifies it; honest about the productivity expectation.
- **Redeploy** — the role changes; the human shifts from doer to supervisor / quality / exception handler. The retraining cost is in the financial proposal; the supervision queue is the new work.
- **Retrain** — the role is replaced; the human moves to a different role with funded retraining. The proposal commits to the support and timing.

Vague "AI will augment our workforce" without role-by-role analysis is unprofessional. Procurement evaluators in regulated and unionised environments penalise it.

## The Agent-on-Your-Behalf Disclosure UX

When the agent communicates with a third party or takes an action on the buyer's behalf, the third party is informed in line with applicable rules. The disclosure is engineered, not improvised:

- Every outbound message from the agent is signed (name, role, agent-status, contact for human).
- The disclosure language is short and clear; jurisdiction-tuned (EU AI Act Article 50 style where applicable; sectoral disclosure where required).
- A contestability link is always present.
- Voice agents identify as agents at the start of the call.
- High-stakes actions (refund, denial, dispute) carry a human-review prompt; the affected party can ask for a human at any moment.

Buyers in financial services, insurance, healthcare admin, and public sector reject agentic systems that hide the agent. The proposal makes the disclosure UX a named deliverable.

## Adoption Metrics — Agent-Specific

| Metric | Why it matters | Floor / ceiling pattern |
|---|---|---|
| Intervention rate | Inverse of autonomy actually achieved | Floor = ceiling target from pricing model |
| Override rate | Frequency with which supervisor changes the agent's decision after the fact | Watch for trend; spikes mean drift |
| Abstain-correctness | Did the agent abstain when it should have | Floor ≥ 0.95 on the should-abstain subset |
| Supervisor satisfaction (CSAT) | Whether supervisors trust the agent | Above 4.0/5 to sustain adoption |
| Supervisor capacity headroom | Whether supervisor queue has slack | Above 20 % headroom to absorb spikes |
| Contestability case load | How many affected parties contest | Trend is the signal; high load means a deeper issue |
| External satisfaction | Affected party experience | Sectoral benchmark |
| Complaint rate | External complaints attributable to agent | Below incumbent baseline |
| Redress SLA performance | How fast contested actions are resolved | Sectoral benchmark |

## Quality Standards

- Adoption is engineered, not assumed.
- Augment / redeploy / retrain framing is honest and per role.
- Trust staging is named with evidence per stage.
- Supervisor retraining is a funded curriculum, not a slide deck.
- Union / works-council / staff-association consultation is scoped where applicable.
- External-disclosure UX is a deliverable.
- Adoption metrics include intervention and override, not just usage.

## Domain Risks

- "We will train the users on the new AI".
- "AI will augment your team" with no role-by-role analysis.
- HITL described as "human review" with no authority or SLA.
- Trust-building skipped because "the agent is accurate".
- Supervisor role unchanged; same headcount expected to do new supervisory work without retraining.
- Union consultation skipped where required.
- External disclosure deferred — "we will figure it out before launch".
- Adoption metric is "logins per user".
- "Replacement" framed as "augmentation" until the first redundancy notice.

## Domain Outputs

- Agent Adoption Plan subsection for `06-methodology` close or standalone change-management section.
- Augment-Redeploy-Retrain Communications Brief per affected role.
- Trust Staging Plan with named evidence per stage.
- Supervisor Retraining Curriculum (funded; in the financial proposal).
- Union / Works-Council / Staff-Association Communications Plan (where applicable).
- External Communications Plan with the Agent-on-Your-Behalf Disclosure UX.
- Adoption Metrics dashboard specification.

## Anti-Patterns

- Inventing a metric, credential, constraint, or buyer position. Fix: cite the supplied source or mark the item as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and state the evidence needed to resume.
- Advancing autonomy without a named gate owner. Fix: require observable evidence, accountable acceptance, and a rollback path.
- Reusing another sector or use case without reassessment. Fix: retest affected parties, action scope, reversibility, and jurisdiction.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: define an observable measure, threshold, evidence record, and decision owner.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| stakeholder map, workforce impact, autonomy stages, and consultation obligations | Buyer evidence, ToR, approved discovery record, system owner, or measured operating data | Yes | Stop the affected decision; list the missing source and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Adoption and trust-staging plan | Change lead, workforce representatives, and service owner | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| adoption and trust-staging plan | Change lead, workforce representatives, and service owner | Every load-bearing claim traces to supplied evidence; assumptions, owners, gates, exclusions, and observable acceptance conditions are explicit. |

## Capability Contract

Default to read-only for discovery, analysis, review, and planning. Minimum capability is access to the supplied artefacts and permission to calculate or inspect evidence. Edit only the requested proposal working copy. Do not change production systems, contact affected parties, publish, spend, certify compliance, or approve autonomous action without explicit authority from the accountable owner.

## Degraded Mode

If files, interviews, telemetry, specialist review, network access, or calculation tools are unavailable, produce the narrowest useful qualified result. Mark each unavailable check as not assessed, separate facts from assumptions, lower confidence, and state the evidence needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Advance an autonomy stage | Require stage evidence, trained supervisors, disclosure, contestability, and agreed workforce actions. | Premature autonomy or hidden workforce impact. |
| Required evidence, authority, or accountable owner is missing | Stop the affected recommendation or commitment and record the gap. | Invented evidence or unauthorised autonomy. |
| Gate evidence is complete and accepted | Advance only within the approved scope and retain the evidence trace. | Scope drift and irreproducible approval. |

## Workflow

1. Confirm the consumer, authority, neighbouring-skill route, and required inputs; stop when a mandatory source or accountable owner is missing.
2. Inspect the evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a failed safety, finance, regulatory, or acceptance gate.
3. Apply the domain method and decision rules within the qualified scope, retaining an evidence trace.
4. Draft the contracted output and reconcile it with methodology, work plan, staffing, pricing, risk, and governance; recover by revising the affected scope or control and rerunning the failed gate.
5. Verify acceptance conditions, permission boundaries, direct references, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

A claims agent enters shadow mode. Supervisors compare recommendations with actual decisions, record overrides and abstentions, and advance only after the agreed evidence gate and workforce briefing.

<!-- dual-compat-end -->

## References

- [ai-agent-change-management-playbook](../../profiles-sectors/references/ai-agent-change-management-playbook.md) — full playbook.
- [ai-agent-metrics-glossary](../../profiles-sectors/references/ai-agent-metrics-glossary.md) — adoption-metric definitions.
- [ai-on-saas-change-management-playbook](../../profiles-sectors/references/ai-on-saas-change-management-playbook.md) — AI-on-SaaS base.
- [ai-on-saas-change-management-and-adoption](../../ai-on-saas-proposals/ai-on-saas-change-management-and-adoption/SKILL.md) — AI-on-SaaS adoption (load alongside for SaaS-embedded agents).
- [change-management](../../domain-delivery/change-management/SKILL.md) — base change-management discipline.
- [ai-agent-methodology](../ai-agent-methodology/SKILL.md) — methodology that adoption sits inside.
- [ai-agent-team-composition](../ai-agent-team-composition/SKILL.md) — roles required (Agent Safety Lead, AI Change Lead, Human-in-the-loop Designer).
- [monitoring-and-evaluation](../../domain-delivery/monitoring-and-evaluation/SKILL.md) — adoption metrics placement.
- [stakeholder-engagement](../../domain-delivery/stakeholder-engagement/SKILL.md) — stakeholder mapping.
