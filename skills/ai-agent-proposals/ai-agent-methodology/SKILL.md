---
name: ai-agent-methodology
description: Use when drafting the end-to-end delivery methodology for an AI agent or multi-agent system, from discovery and action-catalogue design through staged autonomy and operations.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent Methodology
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The deliverable is one or more AI agents, a multi-agent system, or an agentic layer inside an existing product.
- The buyer expects investor-grade or board-grade rigour: agent ROI that survives a sceptical CFO, agentic evidence that survives a sceptical CTO, procurement answers that survive a sceptical CISO, and a Responsible-AI commitment that survives the general counsel and the regulator.
- The Methodology section must demonstrate simultaneous mastery of agentic engineering (action catalogue, autonomy levels, oversight, kill-switch, audit), agentic safety (eval, red-team, drill, intervention SLO), and agentic operations (drift watch, regression, escalation).
- The engagement faces AI-specific regulators (EU AI Act, Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U, Rwanda AI Policy, sectoral).
- A generic AI methodology or a generic SaaS implementation methodology will not pass evaluator scrutiny.

## Do Not Use When

- The engagement is a non-agent AI build (use `ai-on-saas-combined-methodology`).
- The engagement is generic AI strategy with no agentic deliverable (use `ai-transformation-proposal`).
- The engagement is a pure consulting assignment without software delivery.

## Domain Inputs

- ToR / RFP with the agentic scope (use cases, outcomes, volume, regulators, languages).
- Discovery outputs from `ai-agent-discovery-and-qualification`.
- Autonomy-level commitment per action class.
- Action catalogue v0.
- Buyer's oversight model and intervention SLA.
- Buyer's hallucination, irreversibility, and scope-creep tolerances.
- Buyer's regulator stance and sub-processor expectations.
- Engagement length and phasing constraints.

## Domain Method

1. Open the Methodology with the **Agentic Mental Model** paragraph: an agent is a system that **plans, calls tools, decides, and acts** within an explicit action catalogue, under an explicit autonomy level, with explicit oversight, with explicit kill-switch authority, and with full audit. The methodology engineers the four parts as named disciplines.
2. State the **Conceptual Approach** paragraph: action catalogues are designed before agents are built; autonomy levels are committed per action class; oversight model and intervention SLA are designed not improvised; kill-switch authority is named; audit completeness is a measured discipline; the Responsible-AI agent commitment (`ai-agent-risk-and-responsible-ai`) is signed by a named accountable role.
3. Apply the **Eight Standard Phases** (below). Each phase carries an engineering workstream, a safety workstream, and a change-management workstream in parallel, gated at the same time so that a safety deficiency cannot be hidden behind engineering progress.
4. Inside each phase, apply P-I-P (Premise – Implementation – Proof): open with why this phase is right for this engagement; middle with specific actions, artefacts, and gates; close with the deliverable and the decision the buyer makes at the gate.
5. Populate the **Deliverables Summary** table — every agentic deliverable has an acceptance criterion that is **binary and evaluator-checkable** (e.g. task-success ≥ 0.85 on the golden set; intervention rate ≤ 12 %; irreversible-action incidents = 0; audit-log completeness ≥ 99 %; kill-switch time-to-stop ≤ 60 seconds).
6. Populate the **Eval and Red-Team Strategy** subsection — golden datasets, eval metric(s) with thresholds, LLM-as-judge plus human-in-the-loop, regression harness in CI, agent-specific red-team (prompt injection via tool output, scope manipulation, memory poisoning, multi-agent collusion).
7. Populate the **Action-Catalogue and Reversibility** subsection — every action is named, its system is named, its authority is named, its reversibility class is assigned, its rate limit is set, its audit-event shape is specified.
8. Populate the **Autonomy and Oversight Model** subsection — per action class, the autonomy level (L0–L5), the human's authority, the intervention SLA, the queue staffing, the escalation tree.
9. Populate the **Kill-Switch and Drill** subsection — the kill-switch architecture (per-agent, per-action-class, per-tenant, global), the authority to fire, the drill cadence (at least quarterly), the rollback runbook, the regulator-notification runbook.
10. Populate the **Multi-Agent Orchestration** subsection (when applicable) — orchestrator pattern (manager-worker, planner-actor, swarm), inter-agent contract, blast-radius limit, anti-collusion guard, replay determinism for audit.
11. Populate the **Operate** subsection — drift watch dashboards, intervention-rate trend, irreversibility-incident counter, model-cost-per-task, refresh cadence for prompts and models, regulator-notification triggers.
12. Cross-link to the AI-on-SaaS combined methodology where the agent lives inside a SaaS product, the trust and compliance section, the customer success engagement package, the lifecycle communications program, and the Responsible-AI agent commitment.
13. Map to the ToR's phase naming (Inception / Design / Build / Test / Deploy / Support) if required, preserving the agent workstreams under the buyer's phase names.

## The Eight Standard Phases

### Phase 1 — Discover and Strategy Gate
- Run the Agent-vs-Workflow Filter and the Autonomy-Level Discovery from `ai-agent-discovery-and-qualification`.
- Confirm autonomy targets per action class.
- Confirm oversight model and intervention SLA.
- Confirm kill-switch authority.
- Gate: signed Discovery Findings; signed autonomy commitment; signed action catalogue v0.

### Phase 2 — Action-Catalogue Design
- Enumerate every action the agent will take, classify reversibility, set rate limits, define audit-event shape.
- Decide tool-call allowlist, parameter bounds, value-bound transactions, time-window, tenant scope.
- Design the agent identity and impersonation policy.
- Gate: signed Action Catalogue v1; signed Identity-and-Impersonation Policy.

### Phase 3 — Architecture for Autonomy
- Design the agent loop (perceive, plan, act, observe), the planner / actor / critic separation, the memory model, the tool layer.
- Design the oversight queue, the intervention SLA, the escalation tree, the kill-switch architecture.
- Design the audit log shape (what is logged, where, retention, access).
- Design the eval harness and the red-team harness.
- Design the multi-agent orchestration (where applicable).
- Gate: signed ADR for autonomy architecture; eval and red-team plans signed.

### Phase 4 — Build
- Build the agent, the tool layer, the oversight queue, the audit log, the kill-switch, the eval and red-team harness.
- Component-level evaluation throughout — not only end-to-end.
- Gate: green CI on the eval harness; red-team pass at component level; kill-switch test pass.

### Phase 5 — Shadow Stage
- Agent runs against real traffic without acting. Proposed actions logged.
- Reviewer compares agent decision with human decision.
- Gate: agreement rate ≥ X; abstain-correctness ≥ Y; scope-confinement audit pass.

### Phase 6 — Supervised Stage
- Agent acts on reversible actions; humans confirm irreversible.
- Oversight queue is live; intervention SLA measured.
- Gate: task-success ≥ X; intervention rate ≤ Y; zero unauthorised irreversible actions; kill-switch drill verified.

### Phase 7 — Agentic Stage
- Agent acts on reversible actions without confirmation. Irreversible remain HITL per the autonomy commitment.
- Human-on-the-loop; sampled audit.
- Gate: production exit decision — full evidence pack signed by buyer.

### Phase 8 — Operate
- Drift watch, intervention-rate trend, irreversibility incident counter, model-cost-per-task, prompt and model refresh cadence, regulator-notification triggers.
- Quarterly kill-switch drill. Quarterly red-team refresh. Quarterly model and prompt refresh decision.
- Annual Responsible-AI agent commitment sign-off.

## Quality Standards

- Action Catalogue exists as a signed artefact before Build; reversibility class is assigned to every action.
- Autonomy level is committed per action class; the same agent can be L1 for irreversible and L3 for reversible.
- Kill-switch architecture is named, the authority is named, the drill cadence is set, the first drill is in Phase 5.
- Audit-log completeness is a measured metric; the SLA is named.
- Eval is engineered before models are chosen; component-level evaluation exists alongside end-to-end.
- Red-team includes agent-specific attack classes.
- Multi-agent orchestration (where applicable) has a blast-radius limit and an anti-collusion guard.
- Each phase has at least one binary, evaluator-checkable agentic deliverable.
- Responsible-AI agent commitment is named, sectioned, and signed by a named accountable role (Agent Safety Lead).
- Two-of-everything for client-side critical agent operating roles by go-live (eval owner, action-catalogue owner, kill-switch operator, oversight-queue lead).

## Domain Risks

- "Agent architecture" stated without an action catalogue.
- "Human-in-the-loop" stated without naming the human's authority and the intervention SLA.
- "Audit log" promised without naming what is logged and what completeness SLA applies.
- "Kill-switch" promised without naming the authority and the drill cadence.
- Eval treated as a single end-to-end LLM-as-judge run; component-level evaluation skipped.
- Red-team scoped to prompt injection only; agent-specific attacks (scope manipulation, memory poisoning, multi-agent collusion) skipped.
- Multi-agent system delivered as a single black-box without orchestrator-level governance.
- Operate phase collapsed to "support tickets"; drift watch, drill cadence, refresh cadence skipped.
- Phase gates collapsed into one production gate; partial-pass leakage.

## Domain Outputs

- Methodology section for agent engagements, drop-in ready for proposal `06-methodology`.
- Agentic Mental Model paragraph.
- Conceptual Approach paragraph.
- Eight Standard Phases with P-I-P pattern, each carrying engineering, safety, and change workstreams.
- Deliverables Summary table with binary agentic acceptance criteria.
- Eval and Red-Team Strategy subsection.
- Action-Catalogue and Reversibility subsection.
- Autonomy and Oversight Model subsection.
- Kill-Switch and Drill subsection.
- Multi-Agent Orchestration subsection (where applicable).
- Operate subsection.
- ToR phase-name mapping where required.

## Anti-Patterns

- Inventing a metric, credential, constraint, or buyer position. Fix: cite the supplied source or mark the item as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and state the evidence needed to resume.
- Advancing autonomy without a named gate owner. Fix: require observable evidence, accountable acceptance, and a rollback path.
- Reusing another sector or use case without reassessment. Fix: retest affected parties, action scope, reversibility, and jurisdiction.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: define an observable measure, threshold, evidence record, and decision owner.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| ToR, qualified use cases, action catalogue, constraints, acceptance criteria, and delivery authority | Buyer evidence, ToR, approved discovery record, system owner, or measured operating data | Yes | Stop the affected decision; list the missing source and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Phased agent methodology and gate register | Evaluator, delivery team, and governance board | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| phased agent methodology and gate register | Evaluator, delivery team, and governance board | Every load-bearing claim traces to supplied evidence; assumptions, owners, gates, exclusions, and observable acceptance conditions are explicit. |

## Capability Contract

Default to read-only for discovery, analysis, review, and planning. Minimum capability is access to the supplied artefacts and permission to calculate or inspect evidence. Edit only the requested proposal working copy. Do not change production systems, contact affected parties, publish, spend, certify compliance, or approve autonomous action without explicit authority from the accountable owner.

## Degraded Mode

If files, interviews, telemetry, specialist review, network access, or calculation tools are unavailable, produce the narrowest useful qualified result. Mark each unavailable check as not assessed, separate facts from assumptions, lower confidence, and state the evidence needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Advance delivery phase | Require the prior phase's evidence, acceptance gate, owner approval, and reversible rollback path. | Skipping from prototype to unsafe autonomy. |
| Required evidence, authority, or accountable owner is missing | Stop the affected recommendation or commitment and record the gap. | Invented evidence or unauthorised autonomy. |
| Gate evidence is complete and accepted | Advance only within the approved scope and retain the evidence trace. | Scope drift and irreproducible approval. |

## Workflow

1. Confirm the consumer, authority, neighbouring-skill route, and required inputs; stop when a mandatory source or accountable owner is missing.
2. Inspect the evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a failed safety, finance, regulatory, or acceptance gate.
3. Apply the domain method and decision rules within the qualified scope, retaining an evidence trace.
4. Draft the contracted output and reconcile it with methodology, work plan, staffing, pricing, risk, and governance; recover by revising the affected scope or control and rerunning the failed gate.
5. Verify acceptance conditions, permission boundaries, direct references, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

After build, run shadow evaluation against agreed task sets. Advance to supervised action only when scope confinement, audit logging, kill switch, and task-success gates are evidenced.

<!-- dual-compat-end -->

## References

- [ai-agent-methodology-blocks](../../profiles-sectors/references/ai-agent-methodology-blocks.md) — reusable Methodology section content.
- [ai-agent-risk-register-for-proposals](../../profiles-sectors/references/ai-agent-risk-register-for-proposals.md) — agent risk entries.
- [ai-agent-responsible-ai-commitment](../../profiles-sectors/references/ai-agent-responsible-ai-commitment.md) — Responsible-AI agent commitment template.
- [ai-agent-trust-and-compliance-template](../../profiles-sectors/references/ai-agent-trust-and-compliance-template.md) — trust and compliance for agents.
- [ai-agent-metrics-glossary](../../profiles-sectors/references/ai-agent-metrics-glossary.md) — definitions.
- [ai-agent-poc-scoping-template](../../profiles-sectors/references/ai-agent-poc-scoping-template.md) — POC inside Phase 1.
- [ai-on-saas-combined-methodology](../../ai-on-saas-proposals/ai-on-saas-combined-methodology/SKILL.md) — load alongside when the agent lives inside a SaaS product.
- [06-methodology](../../pipeline/06-methodology/SKILL.md) — methodology section discipline.
- [ai-agent-discovery-and-qualification](../ai-agent-discovery-and-qualification/SKILL.md) — discovery inputs.
- [ai-agent-poc-and-pilot-scoping](../ai-agent-poc-and-pilot-scoping/SKILL.md) — pilot-stage detail.
- [ai-agent-risk-and-responsible-ai](../ai-agent-risk-and-responsible-ai/SKILL.md) — risk and commitment.
- [ai-agent-team-composition](../ai-agent-team-composition/SKILL.md) — staffing this methodology assumes.
