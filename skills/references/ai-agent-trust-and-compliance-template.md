# Trust and Compliance for Agents — Section Template

Drop-in template for the Trust and Compliance section of an agentic proposal. Pairs with `ai-agent-compliance-credentials`. Edit names, regulators, and posture per engagement.

---

## Trust and Compliance for Agents

### Agentic Trust Posture

We operate agents under an explicit Action Catalogue, with reversibility classified per action, with autonomy levels committed per action class, with kill-switch authority named, with audit completeness measured, under a Responsible-AI Agent Commitment owned by a named Agent Safety Lead. The posture below describes how we operationalise this commitment.

### Agentic Compliance Map

| Regulator / Standard | Posture | Evidence reference | Target |
|---|---|---|---|
| EU AI Act (high-risk articles where applicable; Article 50 transparency) | Ready / In-progress | Conformity readiness pack; transparency UX evidence | [Date] |
| Kenya NCAIS | Ready | Principles map; published action catalogue; named accountable role | n/a |
| Nigeria NAIS | Ready | Risk-based oversight; HITL on irreversibility | n/a |
| South Africa AI policy / POPIA automated decision-making | Ready | HITL on decisioning; contestability channel; data-subject rights | n/a |
| Uganda NITA-U guidance | Ready | Audit log; sub-processor disclosure; data residency option | n/a |
| Rwanda AI Policy | Ready / In-progress | Sovereign-AI option; transparency-to-affected-party | [Date] |
| ISO 42001 (AI management system) | In-progress | Management-system documentation; gap analysis | [Date] |
| ISO 23894 (AI risk) | Ready | Risk register; treatment plan | n/a |
| NIST AI RMF | Ready | Govern / Map / Measure / Manage mapping | n/a |
| Sectoral — FS model-risk management (SR 11-7-style) | Ready / In-progress | Agent inventory entry; validation cadence; ongoing monitoring | [Date] |
| Sectoral — Healthcare admin / clinical separation | Ready | Non-clinical scope in action catalogue; clinician-final on every drafted clinical artefact | n/a |
| Sectoral — Legal practice rules | Ready | Lawyer-final on filings; confidentiality by tenant | n/a |
| Sectoral — Public-sector administrative-law fairness | Ready | HITL strict; transparency UX; contestability | n/a |

### Action Audit Log Practice

- **What is logged** — decision, reasoning trace (where the model surface permits), tool call name and parameters, return value, post-call assertions, human decision (if any), named approver, timestamp, tenant, agent identity, session, task.
- **Retention** — minimum seven (7) years or sectoral requirement (whichever is greater).
- **Completeness SLA** — 99 % measured monthly.
- **Access** — buyer, internal audit, external auditor, regulator (subject to disclosure controls).
- **Replay capability** — yes; replay-deterministic for forensic review.

### Irreversibility Gating

- Every action class carries a reversibility label: Reversible-no-harm / Reversible-with-effort / Irreversible.
- Irreversible actions require L1 gating — named human approval before commit.
- Value-bound dual approval applies above the threshold per action class.
- Dry-run pattern is offered where the system supports it (proposed state shown before commit).
- Reversibility classification is kept current via change-control.

### Intervention SLO

- **Definition** — the share of agent-attempted tasks where a human had to step in to correct, override, or complete.
- **Target** — set per use case; standard floor ≤ 12 % at month 6 of operation, falling thereafter.
- **Measurement** — automated from the audit log; monthly Agent Safety Council review.
- **Alerting** — breach for two consecutive weeks triggers Agent Safety Lead review.

### Kill-Switch Architecture and Drill

- **Layers** — per-action-class, per-agent, per-tenant, global.
- **Authority chain** — Agent Safety Lead (agency); buyer-side Agent Safety Lead; Agent Ops Lead; SteerCo Chair. After-hours coverage on rotation.
- **Time-to-stop SLA** — 60 seconds (per-action / per-agent); 5 minutes (per-tenant); 15 minutes (global).
- **Drill cadence** — quarterly minimum. First drill in pilot Supervised stage; second in Agentic stage; quarterly thereafter.
- **Drill log** — available to buyer and auditor; post-drill review within five business days.

### Agent Red-Team Catalogue

| Attack class | Cadence | Scorecard |
|---|---|---|
| Prompt injection — direct (in user input) | Monthly | Pass / partial / fail |
| Prompt injection — indirect (via tool output) | Quarterly | Pass / partial / fail |
| Scope manipulation (jailbreak action catalogue) | Quarterly | Pass / partial / fail |
| Memory poisoning | Quarterly | Pass / partial / fail |
| Identity confusion / impersonation | Quarterly | Pass / partial / fail |
| Multi-agent collusion / loop induction (where applicable) | Quarterly | Pass / partial / fail |
| Side-channel leakage / data exfiltration | Quarterly | Pass / partial / fail |
| Sub-processor compromise simulation | Annually | Pass / partial / fail |

Remediation cadence: critical findings within 30 days; high within 60; medium within 90.

### Agent Identity and Impersonation Policy

- Agents act under a named service identity, a delegated user identity, or both — never anonymously.
- External communications carry an agent signature, a route to a human, and the disclosure language required in the jurisdiction.
- Voice agents identify at the start of the call.
- Transparency-to-affected-party is engineered in the UX; the buyer's communications team reviews disclosures before launch.

### Action-Scope Attestation

Every agent has a published Action-Scope Attestation (Annex):
- Actions it can take.
- Systems it touches.
- Authority limits (value, time-window, tenant).
- Reversibility classification per action.

The attestation is auditor-verifiable and updated via change-control.

### Multi-Agent Governance (where applicable)

- Orchestration pattern named (manager-worker, planner-actor-critic, swarm).
- Inter-agent contract: input / output schemas, error handling, retry policy, escalation.
- Blast-radius limit per agent.
- Anti-collusion guard: independent verification on high-stakes decisions.
- Loop detection and break.
- Replay-deterministic orchestrator log.

### Transparency-to-Affected-Party

- AI Act Article 50-style disclosure on external communications where the regulation applies.
- Sectoral disclosure rules (financial-services conduct, healthcare communications, legal-practice rules) honoured.
- Contestability channel published; SLA committed.
- High-stakes actions carry an immediate route to a human.

### Sub-Processor Disclosure (Models and Tool-Call APIs)

| Sub-Processor | Use | Region | Retention | Training-data posture | Fallback |
|---|---|---|---|---|---|
| [Provider A] | Inference | EU-west / KE-mirror | Zero-retention API | Excluded | [Provider B] |
| [Provider B] | Inference fallback | EU-west | Zero-retention API | Excluded | [Open-weight self-host] |
| [Tool API X] | [Function] | [Region] | [N days] | n/a | [Alternate] |
| [Tool API Y] | [Function] | [Region] | [N days] | n/a | [Alternate] |

Changes to the sub-processor list are notified with [thirty (30)] days' notice.

### Sovereign-AI / On-Prem Option

A sovereign-AI deployment is available for tenants whose data must not leave the country or whose regulator requires on-prem inference. Architecture: open-weight model hosted on dedicated GPU; agent components on-prem; audit log on-prem with mirror to buyer security operations centre. SLA: as published in Annex. Pricing differential: as published in Annex.

### Insurance and Liability

- Professional indemnity / errors-and-omissions cover at $[N] aggregate.
- AI-specific liability cover where the market offers it.
- Contractual liability allocation in the MSA; the buyer remains accountable to the regulator and the customer; the agency carries delivery liability.

### Signed Off

- Quarterly Agent Safety Council review.
- Annual SteerCo sign-off.
- Annual independent review (year two onward).
