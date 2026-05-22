# AI-Agent Team Composition Template

Full roster template with role descriptions, sample CV bullets, RACI, and ramp considerations. Pairs with `ai-agent-team-composition`.

## The Agent Roster (full)

### Engagement Lead / Programme Manager
- **Accountable for**: delivery to scope, schedule, cost; SteerCo orchestration; risk and change.
- **Sample CV bullet**: "Led a 14-person agent build for a regional bank's customer-support resolution programme; reached 88 % task-success with intervention at 9 % at month 6; zero irreversibility incidents."

### Agent Architect
- **Accountable for**: agent loop (perceive / plan / act / observe); planner / actor / critic separation; memory model; autonomy architecture; the architecture ADR.
- **Sample CV bullet**: "Designed the planner-actor-critic architecture for an insurance claims triage agent; authored the autonomy commitment matrix; signed the kill-switch architecture ADR."

### Tool Engineer
- **Accountable for**: the tool layer; allowlist, parameter bounds, value bounds, dry-run pattern, post-call assertions, transaction wrappers, rollback. Co-owns the action catalogue.
- **Sample CV bullet**: "Built the tool layer for a financial-services reconciliation agent across four systems of record; implemented value-bound dual approval and post-call assertions on ledger writes."

### Prompt Engineer
- **Accountable for**: system prompts, planner prompts, critic prompts, prompt regression suite.
- **Sample CV bullet**: "Authored and maintained the prompt suite for a multilingual citizen-service agent across English, Swahili, and Luganda; established prompt regression with eval CI."

### Retrieval / Memory Engineer
- **Accountable for**: RAG where applicable; memory scoping per session / tenant; memory audit; memory reset cadence.
- **Sample CV bullet**: "Designed per-tenant memory scoping and quarterly memory audit for a legal-research agent; eliminated cross-firm bleed risk on a 12-tenant deployment."

### Multi-Agent Orchestrator Engineer (where applicable)
- **Accountable for**: orchestration topology; inter-agent contract; blast-radius limit; anti-collusion guard; loop detection; replay determinism.
- **Sample CV bullet**: "Designed manager-worker orchestration for a coding-agent swarm of five specialist agents; implemented blast-radius cap and replay-deterministic logging."

### Agent Safety Lead
- **Accountable for**: the Responsible-AI Agent Commitment; the kill-switch authority; the Agent Safety Council; incident classification; regulator engagement on agentic systems.
- **Sample CV bullet**: "Owned the Responsible-AI Agent Commitment for a public-sector agent programme; conducted four kill-switch drills with regulator observer; zero irreversible incidents over two years."

### Eval Engineer
- **Accountable for**: golden datasets; eval thresholds; eval CI; drift watch; component-level and end-to-end evaluation.
- **Sample CV bullet**: "Built the eval harness for a customer-support resolution agent with 480-case golden set and adversarial subset; eval CI integrated; monthly drift refresh."

### Red-Team Lead
- **Accountable for**: agent-specific attack catalogue; quarterly refresh; scorecard; remediation cadence.
- **Sample CV bullet**: "Led quarterly red-team on a healthcare admin agent across prompt injection via tool output, scope manipulation, and memory poisoning; achieved zero critical residuals."

### Human-in-the-loop Designer
- **Accountable for**: oversight queue; intervention SLA; escalation tree; supervisor experience; contestability channel.
- **Sample CV bullet**: "Designed the supervisor queue and intervention SLA for an insurance claims agent supporting a team of 18 claims handlers shifting from doer to supervisor."

### AI Change and Adoption Lead
- **Accountable for**: augment / redeploy / retrain framing; trust staging; supervisor retraining curriculum; union / works-council communications.
- **Sample CV bullet**: "Led the change programme for a 40-FTE customer-support transition to agent-supervised operations; delivered the supervisor retraining curriculum and a union consultation evidence pack."

### Agent Ops Lead (MLOps for agents)
- **Accountable for**: model gateway; agent registry; region routing; fallback; observability; kill-switch authority operator.
- **Sample CV bullet**: "Operated the agent fleet for a regional bank across four tenants with quarterly drill cadence and 99.4 % audit-log completeness."

### SRE for Agents
- **Accountable for**: uptime; intervention SLA infrastructure; audit-log completeness SLA; drift watch dashboards.
- **Sample CV bullet**: "Ran SRE for an agentic system handling 200K daily tasks with intervention SLA at 95th percentile of 38 seconds."

### DevOps / Platform Engineer
- **Accountable for**: CI/CD with eval gates; infrastructure as code; environment isolation.

### Solution Architect (where the agent lives inside a SaaS product)
- **Accountable for**: control plane / application plane / tenant isolation; co-owns architecture with Agent Architect.

### Security and Compliance Lead
- **Accountable for**: DPA; sub-processor disclosure for tool calls and models; audit; hardening; regulator readiness on the compliance dimension (distinct from Agent Safety Lead, who owns Responsible-AI).

### Customer Success Lead
- **Accountable for**: adoption; value realisation; expansion (in product engagements). Co-leads change with AI Change Lead.

### Sponsor / Executive Sponsor (Agency)
- **Accountable for**: relationship at executive level; close-of-engagement sign-off.

### Buyer-Side Counterparts (Two-of-Everything)
- Action-Catalogue Owner.
- Eval Owner.
- Kill-Switch Operator (named on the runbook).
- Oversight-Queue Lead.
- Agent Safety Lead (buyer-side).

## Standard RACI

| Workstream | Agent Architect | Tool Eng | Prompt | Memory | Multi-Agent | Safety Lead | Eval | Red-Team | HITL Designer | Change Lead | Ops Lead | SRE | DevOps | Buyer Owners |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Action Catalogue | A | R | C | C | C | C | C | C | C | I | I | I | I | A |
| Architecture ADR | A | R | C | C | R (if multi) | R | R | C | C | I | C | C | C | A |
| Build | R | R | R | R | R (if multi) | C | R | C | C | I | R | C | R | I |
| Eval and Red-Team | C | C | R | C | C | A | R | R | C | I | C | C | C | A (Eval) |
| Oversight Queue | C | C | C | C | C | R | C | C | A | R | C | R | C | A (Oversight) |
| Kill-Switch | C | R | C | C | C | A | C | C | C | I | R | R | C | A (Operator) |
| Audit Log | C | R | C | C | C | A | C | C | C | I | R | R | C | A |
| Operate | C | C | C | C | C | A | R | R | R | C | R | R | C | A (Ops) |
| Adoption | I | I | I | I | I | C | C | I | R | A | C | I | I | A |

A = Accountable; R = Responsible; C = Consulted; I = Informed.

## Ramp Curve

| Role | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Phase 6 | Phase 7 | Phase 8 |
|---|---|---|---|---|---|---|---|---|
| Engagement Lead | FT | FT | FT | FT | FT | FT | FT | PT |
| Agent Architect | FT | FT | FT | FT | PT | PT | PT | OC |
| Tool Engineer | PT | FT | FT | FT | PT | PT | PT | OC |
| Prompt Engineer | PT | FT | FT | FT | PT | PT | PT | PT |
| Memory Engineer | PT | FT | FT | FT | PT | PT | PT | OC |
| Multi-Agent Orchestrator | OC | PT | FT | FT | PT | PT | PT | OC |
| Agent Safety Lead | FT | FT | FT | FT | FT | FT | FT | PT |
| Eval Engineer | FT | FT | FT | FT | FT | FT | FT | PT |
| Red-Team Lead | PT | PT | PT | FT | FT | FT | FT | PT |
| HITL Designer | PT | FT | FT | FT | FT | FT | PT | PT |
| Change Lead | PT | PT | PT | FT | FT | FT | FT | PT |
| Agent Ops Lead | OC | PT | PT | FT | FT | FT | FT | FT |
| SRE | OC | OC | PT | FT | FT | FT | FT | FT |
| DevOps | PT | FT | FT | FT | PT | PT | PT | PT |

FT = Full-time; PT = Part-time; OC = On call.

Key: **Agent Safety, Eval, Tool Engineer ramp at Phase 1**. Safety is not a hardening role in agentic engagements.

## Blended-Rate Considerations

- Separate agent-side rates from SaaS-side rates where procurement requires it.
- AI Safety Lead and Eval Engineer carry premium because the talent is scarce.
- Local-content / sovereign-staffing requirements may require co-sourcing with a partner in the buyer's jurisdiction.

## TECH-6 Mapping (illustrative)

| Position | Key / Non-key | Time (person-months) |
|---|---|---|
| Engagement Lead | Key | 12 |
| Agent Architect | Key | 10 |
| Agent Safety Lead | Key | 12 |
| Eval Engineer | Key | 10 |
| Tool Engineer | Non-key | 12 |
| Prompt Engineer | Non-key | 8 |
| Multi-Agent Orchestrator | Non-key | 6 |
| HITL Designer | Non-key | 6 |
| Change Lead | Non-key | 6 |
| Agent Ops Lead | Key | 10 |
| SRE | Non-key | 8 |
| DevOps | Non-key | 6 |

## Two-of-Everything Plan

By go-live, the buyer side has a named counterpart trained to operate:
- Action-Catalogue maintenance and change-control.
- Eval set ownership and threshold management.
- Kill-switch authority with after-hours rota.
- Oversight-queue leadership.
- Agent Safety Council co-chair.

The supervisor retraining curriculum is funded in the engagement.
