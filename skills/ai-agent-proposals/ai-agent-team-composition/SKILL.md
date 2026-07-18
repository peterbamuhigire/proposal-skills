---
name: ai-agent-team-composition
description: Use when defining an AI-agent delivery team, role accountabilities, RACI, mobilisation curve, safety coverage, client counterparts, or evaluator-facing staffing evidence.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent Team Composition
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The Team Composition section of an AI-agent proposal must demonstrate that the agency understands the staffing of agentic systems.
- The evaluator scores roster credibility (World Bank TECH-6, AfDB, public-sector procurement, premium enterprise).
- The buyer's CTO will challenge the roster ("who is the agent safety lead?", "who owns the kill-switch drill?", "who designs the action catalogue?").
- The bid is competitive and a generic AI roster will lose.

## Do Not Use When

- The engagement is non-agent (use `ai-on-saas-team-composition` or `07-team-composition`).

## Domain Inputs

- The methodology phases and workstreams from `ai-agent-methodology`.
- The buyer's procurement framework (TECH-6, AfDB, UNDP, RFP).
- The buyer's blended-rate tolerance.
- The buyer's local-content / sovereign-staffing requirements.
- The agency's bench and named CV pool.
- Whether the engagement is multi-agent (additional orchestration roles required).

## Domain Method

1. Build the **Agent Roster** from the standard role library (below), tuned to the engagement's workstreams and phases.
2. Decide the **Two-of-Everything** rule for client-side critical agent operating roles by go-live — eval owner, action-catalogue owner, kill-switch operator, oversight-queue lead. The proposal explicitly trains a buyer-side counterpart per agency-side role.
3. Build the **RACI** across discover → action-catalogue → architecture → build → shadow → supervised → agentic → operate phases.
4. Build the **Ramp Curve**: who is full-time, who is part-time, who is on call, when each role ramps in and out. **Agent Safety Lead, Eval Engineer, and Tool Engineer ramp at Phase 1 alongside the Agent Architect.** Safety is not a hardening role in agentic engagements; it is foundational.
5. Build the **Blended-Rate Table** if procurement requires it, with agent roles costed separately.
6. Map to **TECH-6** or equivalent format if required.
7. Output the **Team Composition** section.

## Standard Agent Roster

### Agent Engineering
- **Agent Architect** — the agent loop (perceive / plan / act / observe), the planner / actor / critic separation, the memory model, the autonomy architecture; signs the ADR.
- **Tool Engineer** — the tool layer; allowlist, parameter bounds, value bounds, dry-run pattern, post-call assertions, transaction wrappers, rollback. Owns the action catalogue with the architect.
- **Prompt Engineer** — system prompts, planner prompts, critic prompts, regression suite.
- **Retrieval / Memory Engineer** — RAG (where applicable), memory scoping per session / tenant, memory audit.
- **Multi-Agent Orchestrator Engineer** (where applicable) — orchestration topology, inter-agent contract, blast-radius limit, anti-collusion guard.

### Agent Safety
- **Agent Safety Lead** — Responsible-AI agent commitment owner; red-team scorecard owner; escalation owner; named accountable role on irreversibility.
- **Eval Engineer** — golden datasets, eval CI, drift watch; component-level eval and end-to-end eval.
- **Red-Team Lead** — agent-specific attack catalogue, quarterly refresh.

### Human-in-the-loop and Adoption
- **Human-in-the-loop Designer** — oversight queue, intervention SLA, escalation tree, supervisor experience, contestability channel.
- **AI Change and Adoption Lead** — augment / redeploy / retrain framing, trust staging, supervisor retraining curriculum.

### Operations
- **Agent Ops Lead (MLOps for agents)** — model gateway, agent registry, region routing, fallback, observability, kill-switch authority operator.
- **SRE for Agents** — uptime, intervention SLA, audit-log completeness SLA, drift watch dashboards.
- **DevOps / Platform Engineer** — CI/CD with eval gates, infrastructure as code.

### Programme and Sponsor
- **Engagement Lead / Programme Manager** — senior accountable.
- **Solution Architect (where the agent lives inside a SaaS product)** — control plane / application plane / tenant isolation; co-owns the architecture with the Agent Architect.
- **Security and Compliance Lead** — DPA, sub-processor disclosure for tool calls and models, audit, hardening.
- **Customer Success Lead** — adoption, value realisation, expansion (in product engagements).
- **Sponsor / Executive Sponsor** — partner side, signs the close.

### Buyer-Side Counterparts (Two-of-Everything)
- **Buyer-side Action-Catalogue Owner** — signs every action catalogue change.
- **Buyer-side Eval Owner** — co-owns the eval discipline, signs threshold changes.
- **Buyer-side Kill-Switch Operator** — has the authority to fire the kill-switch out-of-hours; named on the runbook.
- **Buyer-side Oversight-Queue Lead** — leads the supervisor team; receives the supervisor retraining curriculum.
- **Buyer-side Agent Safety Lead** — counterpart to the agency Agent Safety Lead; signs Responsible-AI commitments.

## Quality Standards

- Agent Safety Lead is a named role with a named owner.
- Eval Engineer is a distinct role from QA, ramped at Phase 1.
- Tool Engineer is a distinct role from Application Engineer in any engagement with more than five action classes.
- Human-in-the-loop Designer is a named role; UI / UX cannot replace it.
- Multi-Agent Orchestrator Engineer is a named role in multi-agent engagements.
- Two-of-Everything applies on the agent side as well as the SaaS side.
- Ramp curve has Agent Safety, Eval, Tool Engineer at Phase 1.
- Blended-rate table separates agent roles where procurement requires it.
- TECH-6 mapping is exact where required (key vs non-key experts).
- Local-content / sovereign-staffing requirement honoured.

## Domain Risks

- "Agent lead" as the only agent role.
- Agent Safety as a shared duty of the architect.
- Tool Engineer collapsed into Application Engineer in an engagement with 20+ action classes.
- Eval Engineer collapsed into QA.
- Human-in-the-loop Designer skipped because "the UI handles it".
- Multi-Agent Orchestrator Engineer skipped in multi-agent engagements.
- Ramp curve that puts safety into hardening.
- Roster larger than the budget can sustain.
- No buyer-side counterparts named.

## Domain Outputs

- Agent Roster table (role, name, allocation, ramp).
- RACI across phases.
- Ramp Curve.
- Blended-Rate Table (where required).
- TECH-6 (or equivalent) mapping (where required).
- Two-of-Everything Plan for client-side counterparts.
- Buyer-Side Counterparts list with named owners.

## Anti-Patterns

- Inventing a metric, credential, constraint, or buyer position. Fix: cite the supplied source or mark the item as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and state the evidence needed to resume.
- Advancing autonomy without a named gate owner. Fix: require observable evidence, accountable acceptance, and a rollback path.
- Reusing another sector or use case without reassessment. Fix: retest affected parties, action scope, reversibility, and jurisdiction.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: define an observable measure, threshold, evidence record, and decision owner.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| scope, work plan, role requirements, availability, CV evidence, and buyer counterparts | Buyer evidence, ToR, approved discovery record, system owner, or measured operating data | Yes | Stop the affected decision; list the missing source and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Staffing plan, RACI, and mobilisation schedule | Evaluator, delivery lead, and client sponsor | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| staffing plan, RACI, and mobilisation schedule | Evaluator, delivery lead, and client sponsor | Every load-bearing claim traces to supplied evidence; assumptions, owners, gates, exclusions, and observable acceptance conditions are explicit. |

## Capability Contract

Default to read-only for discovery, analysis, review, and planning. Minimum capability is access to the supplied artefacts and permission to calculate or inspect evidence. Edit only the requested proposal working copy. Do not change production systems, contact affected parties, publish, spend, certify compliance, or approve autonomous action without explicit authority from the accountable owner.

## Degraded Mode

If files, interviews, telemetry, specialist review, network access, or calculation tools are unavailable, produce the narrowest useful qualified result. Mark each unavailable check as not assessed, separate facts from assumptions, lower confidence, and state the evidence needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Assign or leave a role unfilled | Use verified competence, availability, segregation of duties, and phase demand; expose gaps instead of inflating CV claims. | A paper team with unavailable or conflicted personnel. |
| Required evidence, authority, or accountable owner is missing | Stop the affected recommendation or commitment and record the gap. | Invented evidence or unauthorised autonomy. |
| Gate evidence is complete and accepted | Advance only within the approved scope and retain the evidence trace. | Scope drift and irreproducible approval. |

## Workflow

1. Confirm the consumer, authority, neighbouring-skill route, and required inputs; stop when a mandatory source or accountable owner is missing.
2. Inspect the evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a failed safety, finance, regulatory, or acceptance gate.
3. Apply the domain method and decision rules within the qualified scope, retaining an evidence trace.
4. Draft the contracted output and reconcile it with methodology, work plan, staffing, pricing, risk, and governance; recover by revising the affected scope or control and rerunning the failed gate.
5. Verify acceptance conditions, permission boundaries, direct references, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

The Agent Safety Lead also authored the runtime. Assign an independent gate reviewer for release evidence, confirm availability, and show the client counterpart for kill-switch authority.

<!-- dual-compat-end -->

## References

- [ai-agent-team-composition-template](../../profiles-sectors/references/ai-agent-team-composition-template.md) — full roster template with sample CV bullets.
- [ai-on-saas-team-composition-template](../../profiles-sectors/references/ai-on-saas-team-composition-template.md) — AI-on-SaaS roster base.
- [ai-on-saas-team-composition](../../ai-on-saas-proposals/ai-on-saas-team-composition/SKILL.md) — AI-on-SaaS roster (load alongside for SaaS-embedded agents).
- [07-team-composition](../../pipeline/07-team-composition/SKILL.md) — base team composition.
- [ai-agent-methodology](../ai-agent-methodology/SKILL.md) — workstreams the roster covers.
- [ai-agent-change-management-and-adoption](../ai-agent-change-management-and-adoption/SKILL.md) — change roles overlap.
- [ai-agent-risk-and-responsible-ai](../ai-agent-risk-and-responsible-ai/SKILL.md) — Agent Safety Lead role.
- [10-financial-proposal](../../pipeline/10-financial-proposal/SKILL.md) — fee schedule.
