# AI-Agent Procurement Questionnaire Pack

Drop-in procurement answer pack across the ten agent procurement domains. Pairs with `ai-agent-procurement-and-questionnaire`. Tune per bid; honest staged answers only.

## How to Use

- Read the questionnaire. Categorise each question into one of the ten domains below.
- Where the questionnaire skips a domain, volunteer the answer.
- Staged answer convention: **Today / In-progress with date / Committed for this engagement / Out of scope with rationale**.
- Cross-link every answer to the methodology, the action catalogue, the risk register, and the kill-switch drill log.

## 1. Autonomy Level and Action Scope

| Question | Sample answer pattern |
|---|---|
| What autonomy level operates at go-live per use case? | Today: L2 on triage and assembly; L1 on irreversible. Committed: trajectory to L3 on reversible at month 6 contingent on Stage 3 thresholds. |
| Is the action catalogue published? | Yes — Annex X. Signed by Agency Engagement Lead and Buyer SteerCo Chair. Changes via change-control only. |
| How is scope confined? | Tool-call allowlist; parameter bounds; value bounds; time-window; tenant scope; identity scope. Anomalous-action alerting. |
| Reversibility classification? | Every action has a class — Reversible-no-harm / Reversible-with-effort / Irreversible. Annex X. |

## 2. Oversight and Intervention

| Question | Sample answer pattern |
|---|---|
| Oversight model per action class? | HITL on Irreversible; HOTL with sampled audit on Reversible-with-effort; audit-only on Reversible-no-harm at L3+. |
| Intervention SLA? | Reviewer responds within [N minutes]; agent times out and aborts after [M minutes] if unconfirmed. |
| Queue staffing? | Buyer staffs at floor [N FTE], on-call out-of-hours per shift roster. Supervisor retraining curriculum funded in the engagement. |
| Escalation tree? | Supervisor → Agent Safety Lead → SteerCo → CEO. Named owners; after-hours coverage. |

## 3. Irreversibility Gating

| Question | Sample answer pattern |
|---|---|
| Is human approval required on every irreversible action? | Yes, by named role per action class. Recorded in Audit Log. |
| Value-bound dual approval? | Above $[X] per action class; threshold in Annex X. |
| Dry-run pattern? | Available on actions where the target system supports it; otherwise transaction-confirmation token. |
| How is reversibility kept current? | Change-control on Action Catalogue; quarterly review by Agent Safety Council. |

## 4. Kill-Switch and Drill

| Question | Sample answer pattern |
|---|---|
| Kill-switch architecture? | Four layers — per-action, per-agent, per-tenant, global. |
| Named authority? | Agency Agent Safety Lead, Buyer Agent Safety Lead, Agent Ops Lead, SteerCo Chair. After-hours coverage on rotation. |
| Drill cadence? | Quarterly minimum. First drill in pilot Stage 2. Second in Stage 3. Drill log available. |
| Time-to-stop SLA? | 60 seconds (per-action / per-agent); 5 minutes (per-tenant); 15 minutes (global). |

## 5. Audit Log

| Question | Sample answer pattern |
|---|---|
| What is logged? | Decision, reasoning trace where the model surface permits, tool call name and parameters, return value, post-call assertions, human decision (if any), named approver, timestamp, tenant, agent identity, session, task. |
| Retention? | Minimum seven (7) years or sectoral requirement (whichever is greater). |
| Completeness SLA? | 99 % measured monthly. Breach triggers Agent Safety Council review. |
| Access? | Buyer, internal audit, external auditor, regulator (subject to disclosure controls). Replay capability available. |

## 6. Identity, Impersonation, Transparency-to-Affected-Party

| Question | Sample answer pattern |
|---|---|
| Agent identity model? | Service identity by default; delegated user identity for actions on behalf of a specific user. Never anonymous. |
| External communications disclosure? | Every outbound email, chat, SMS, or voice call discloses agent status per jurisdictional rule (e.g. EU AI Act Article 50 where applicable). |
| Voice agents? | Identify at the start of the call; route to human at any moment. |
| Transparency UX? | Engineered, not improvised. Reviewed by buyer Communications and Compliance. Contestability link always present. |

## 7. Model and Tool-Call Sub-Processors

| Question | Sample answer pattern |
|---|---|
| Model providers named? | [Provider A] (primary), [Provider B] (fallback), [Self-host open-weight] (sovereign option). Sub-processor list in Annex X. |
| Tool-call APIs named? | [Tool API X], [Tool API Y]. Annex X. |
| Region of inference / processing? | Per data class — EU data to EU inference; KE data to KE / ZA inference; SOV data to on-prem. |
| Training-data posture? | Customer data is **not** used to train provider models. Zero-retention API where the provider offers; otherwise contractual training-opt-out. |
| Sub-processor change notification? | Thirty (30) days' notice or earlier where the regulator requires. |

## 8. Eval, Red-Team, Drift

| Question | Sample answer pattern |
|---|---|
| Eval methodology? | Golden datasets per use case with adversarial cases; LLM-as-judge plus human review; thresholds set per action class; eval CI gates deploy. |
| Refresh cadence? | Monthly during engagement; quarterly in production. |
| Agent red-team catalogue? | Prompt injection (direct and via tool output); scope manipulation; memory poisoning; identity confusion; multi-agent collusion (where applicable); side-channel leakage. Quarterly refresh. |
| Drift watch? | Production dashboards on task-success, intervention rate, abstain-correctness, irreversibility incidents, cost-per-task. Monthly review. |

## 9. Multi-Agent Governance (where applicable)

| Question | Sample answer pattern |
|---|---|
| Orchestration pattern? | [Manager-worker / planner-actor-critic / swarm]. Documented in the architecture ADR. |
| Inter-agent contract? | Input / output schema; error handling; retry policy; escalation. Versioned. |
| Blast-radius limit? | Per-agent action cap; orchestrator pause on alarm. |
| Anti-collusion guard? | Independent verifier on high-stakes decisions; cross-agent disagreement triggers human review. |
| Replay determinism? | Orchestrator log is replay-deterministic for forensic review. |

## 10. Incident, Liability, Redress

| Question | Sample answer pattern |
|---|---|
| Agent incident classification? | Class 1 (Irreversible) / Class 2 (Scope breach) / Class 3 (Intervention SLA cluster) / Class 4 (Near-miss). Runbook attached. |
| Regulator notification triggers? | Class 1 immediate per sectoral SLA; Class 2 within 24 hours; Class 3 at quarterly Council; Class 4 at quarterly Council. |
| Liability allocation? | Buyer remains accountable to regulator and customer; Agency carries delivery liability per MSA. PI / E&O cover at $[N] aggregate. |
| Redress mechanism? | Published channel; 24-hour acknowledgement SLA; 10-business-day resolution SLA; named owner; human decision on contested outcomes. |
| Public communications? | Per buyer policy; Agency Communications and Security & Compliance leads in support. |

## Quality Standards for the Pack

- Honest staged answers; no fabrication.
- Specific named providers; named regulators; named roles.
- Numbers, not adjectives.
- Internally consistent with risk register, trust and compliance section, and methodology.
- Volunteered answers where the questionnaire skipped a domain.
- Annexes for action catalogue, sub-processor list, kill-switch runbook, contestability process.
