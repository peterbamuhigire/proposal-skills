# AI-Agent Metrics Glossary

Definitions for the metrics used in agentic proposals. Pairs with all agent skills. Use these definitions in BRIEF.md, methodology, business case, pricing, and procurement responses so the buyer reads one vocabulary.

## Outcome and Performance

- **Task-success rate** — share of agent-attempted tasks completed without human correction, override, or re-work, measured over a defined window. Binary at the task level; never "AI quality is good".
- **Intervention rate** — share of agent-attempted tasks where a human corrected, overrode, or completed the task. The inverse of practical autonomy.
- **Deflection rate** — share of workflow volume routed away from a human entirely by the agent (used in support and self-service workflows). Distinguish from containment (the user did not reach a human but their issue was not resolved).
- **Containment** — share of sessions that ended without reaching a human; misleading without a resolution check.
- **Time-to-resolution** — elapsed time from work entering the agent to outcome reached; measure P50 and P95.
- **Average handling time (AHT)** — average duration of a task end-to-end including human handoff time.
- **Capacity unlock** — additional volume the buyer can handle without hiring at constant SLA.

## Autonomy and Oversight

- **Autonomy level (L0–L5)** — committed per action class; see the autonomy ladder in `ai-agent-discovery-and-qualification`.
- **Action class** — a category of agent action (e.g. ticket close, refund authorisation, claim acknowledgement) with a single reversibility class and a single autonomy commitment.
- **Reversibility class** — Reversible-no-harm / Reversible-with-effort / Irreversible. Assigned to every action in the catalogue.
- **Irreversible-action incident** — an irreversible action taken by the agent without the required human approval, or taken with approval but materially wrong; target zero per quarter.
- **Scope breach** — an agent action outside the published Action Catalogue.
- **Intervention SLA** — time within which a human must confirm or reject before the agent times out or aborts (per action class).
- **Oversight model** — HITL (human-in-the-loop) / HOTL (human-on-the-loop) / audit-only — committed per action class.
- **Abstain** — agent declines to act when confidence is below threshold; the system escalates or downgrades to a non-AI path.
- **Abstain-correctness** — share of cases where the agent abstained and the human reviewer agreed it should have; measured on a should-abstain subset of the golden set.
- **Override rate** — share of agent decisions a supervisor changed after the agent acted; trend metric for drift.

## Safety, Audit, Drill

- **Action audit log** — record of every agent action: decision, reasoning trace where the model surface permits, tool call name and parameters, return value, post-call assertions, human decision (if any), named approver, timestamp, tenant, agent identity, session, task.
- **Audit-log completeness SLA** — percentage of expected log entries actually written; standard floor 99 % monthly.
- **Kill-switch architecture** — multi-layer stop authority (per-action / per-agent / per-tenant / global).
- **Time-to-stop SLA** — elapsed time from kill-switch fire to confirmed agent stop; standard 60 seconds per-action and per-agent, 5 minutes per-tenant, 15 minutes global.
- **Kill-switch drill** — scheduled exercise of the kill-switch; quarterly minimum; drill log shared with buyer's auditor.
- **Red-team catalogue** — agent-specific attack classes: prompt injection (direct and via tool output); scope manipulation; memory poisoning; identity confusion; multi-agent collusion; side-channel leakage; sub-processor compromise simulation.

## Cost

- **Model calls per task (P50 / P95)** — number of LLM calls the agent makes per task; agents fan out; this is the most overlooked cost line.
- **Tool calls per task** — number of external API calls.
- **Cost per outcome** — model + oversight + eval + engineering + compute, per outcome.
- **Cost-of-tokens at P99** — token-cost behaviour at the heaviest tenant; not the median.
- **Eval-margin** — cost of running the eval expressed as a share of the agent's gross-margin contribution; flag above 15–20 %.
- **Oversight cost per task** — supervisor cost amortised; falls as autonomy ramps.

## Identity and Transparency

- **Agent identity model** — service identity / delegated user identity / hybrid. Never anonymous.
- **Impersonation policy** — rules on whether the agent can sign in the name of a human; standard: never without explicit disclosure.
- **Transparency-to-affected-party** — disclosure that an agent is communicating with or acting on a third party (e.g. EU AI Act Article 50).
- **Contestability** — affected party's right to challenge an agent action through a named channel with SLA; outcome decided by a human.

## Multi-Agent

- **Orchestration pattern** — manager-worker / planner-actor-critic / swarm; named in the architecture ADR.
- **Inter-agent contract** — schema, error handling, retry, escalation between agents.
- **Blast-radius limit** — cap on actions any single agent can take in a chain.
- **Anti-collusion guard** — independent verifier on high-stakes decisions to prevent self-reinforcing errors.
- **Replay-deterministic orchestrator log** — orchestrator log can replay an interaction for forensic review.

## Adoption

- **Supervisor CSAT** — supervisor satisfaction with the agent and the operating model; floor 4.0 / 5 to sustain adoption.
- **Supervisor queue headroom** — share of queue capacity unused at peak; floor 20 % to absorb spikes.
- **Contestability case load** — count and trend of contested actions.
- **Disclosure presence rate** — share of external communications that carry the required disclosure; target 100 %.

## Worked Example — Reading the Metrics Together

A bank's customer-support resolution agent reports for month 6:
- Task-success rate 0.88 on the golden set; 0.84 on shadow traffic.
- Intervention rate 9 % (target 12 %).
- Abstain-correctness 0.96 on should-abstain subset.
- Irreversible-action incidents: 0 cumulative.
- Audit-log completeness 99.6 % (above 99 % SLA).
- Kill-switch drill: two passes; time-to-stop 38 s and 45 s.
- Red-team: pass on direct prompt injection; partial on indirect (one residual); remediation in 14 days.
- Cost per outcome 0.51 USD (target 0.55 USD).
- Supervisor CSAT 4.2 / 5; queue headroom 27 %.
- Disclosure presence 100 %.

Reading: the agent is on plan; the indirect prompt-injection residual is the watch item. Decision: continue Agentic stage; investigate the indirect-injection finding; refresh red-team in two weeks.
