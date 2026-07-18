---
name: ai-transformation-proposal
description: Use when shaping a proposal for AI applications, analytics, automation, or transformation; use the AI-on-SaaS or AI-agent families when multi-tenancy or autonomous action is the primary deliverable.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI Transformation Proposal
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- A bid, concept note, or client proposal includes AI strategy, AI software development, AI automation, agents, RAG, predictive analytics, dashboards, or AI-enabled service delivery.
- The proposal must show business value, technical credibility, governance, implementation realism, and long-term maintenance capability.

## Proposal Positioning

Position AI as a disciplined business capability:

- Improve decisions, productivity, service quality, risk control, revenue, and operational speed.
- Build on the client's data, workflows, governance, and users.
- Start with high-value, feasible use cases and scale after evidence.
- Include evaluation, monitoring, security, change management, and maintenance from the beginning.

Avoid promising generic "AI transformation" without measurable use cases, data readiness, and operating ownership.

For premium AI work, lead with the value system being improved: decision quality, cycle time, service resolution, risk detection, staff productivity, customer experience, compliance, or revenue. Then show the evidence path: use-case hypothesis, data access, prototype, evaluation threshold, human oversight, deployment, support, and optimisation.

## Methodology Structure

1. **Discovery and value mapping**: Stakeholders, workflows, pain points, baseline metrics, use-case scorecard, and ROI assumptions.
2. **Data and readiness assessment**: Data inventory, quality, sensitivity, access, integration, governance, and gap remediation.
3. **Solution design**: UX, architecture, AI pattern selection, model/provider options, RAG/tool/workflow design, security, and human approval.
4. **Prototype and evaluation**: Golden test cases, user review, quality thresholds, cost/latency targets, and risk controls.
5. **Implementation**: Agile delivery, integrations, data pipelines, model gateway, monitoring, audit logs, and documentation.
6. **Deployment and adoption**: Pilot rollout, training, change management, support, feedback loops, and governance handover.
7. **Maintenance and optimization**: Prompt/model updates, eval refresh, cost review, incident response, performance tuning, and roadmap expansion.

## Technical Strategy Rules

- Start from validated use cases, not model fashion. Prioritise by value, feasibility, data readiness, risk, and adoption.
- State the architecture decision logic: build, buy, configure, integrate, or defer.
- Include data flow, system boundaries, access control, audit logs, monitoring, fallback, and incident response.
- Define evaluation before build: representative test cases, acceptance thresholds, review cadence, and release gates.
- Treat AI as an operating capability with ownership, maintenance budget, support roles, and continuous improvement.
- For SaaS or multi-client platforms, address tenant isolation, configuration, scalability, measured usage, upgrades, and support cost.

## Objection Handling

- If the evaluator questions AI accuracy, respond with evaluation thresholds, human review, monitoring, fallback, and controlled release.
- If the evaluator questions cost, separate discovery, build, model/API usage, evaluation, governance, support, and optimisation so the price is defensible.
- If the evaluator questions risk, state the specific risk, its trigger, mitigation, owner, and escalation path.
- If the evaluator questions data readiness, propose a discovery or pilot phase that tests assumptions before full implementation.

## Sections to Include

- AI value proposition tied to client objectives.
- Prioritized AI use-case portfolio with value, feasibility, risk, and sequencing.
- Technical architecture covering data, models, tools, APIs, security, observability, and fallback.
- Responsible AI and governance plan covering privacy, explainability, bias, human oversight, and auditability.
- Evaluation plan with acceptance thresholds and release gates.
- Capacity building plan for client teams.
- Maintenance model and SLA assumptions.
- Financial proposal that separates discovery, build, cloud/model usage, support, and optimization.

## Evidence of Capability

- Relevant case studies or comparable experience.
- Team roles for product, data, AI engineering, software engineering, UX, security, QA, change management, and support.
- Sample deliverables: AI opportunity map, AI product brief, architecture decision record, eval report, runbook, and adoption plan.

## Red Flags

- No baseline metric or economic value.
- No access to required data.
- No evaluation method.
- No human approval for high-risk actions.
- No maintenance budget for model, prompt, data, and platform drift.
- Client expects a fully autonomous system where policy, law, or operational risk requires oversight.

## SaaS-on-AI and AI-on-SaaS Lens

When the AI engagement runs on or builds a SaaS platform, layer on SaaS-specific concerns:

- **Tenant isolation for AI features**: per-tenant context propagation in prompts, RAG indexes, model gateways, and eval suites. Cross-tenant data leakage in AI features is a security incident, not a feature gap.
- **Per-tenant cost attribution for AI usage**: model and API costs must be attributable per tenant; tier-aware throttling protects shared infrastructure.
- **Tenant-aware evaluation**: golden test sets per tenant or per regulator, not just per use case.
- **AI lifecycle communications**: the agency proposes lifecycle communications around new AI features (activation nudges, value reinforcement, opt-out flows) as a priced workstream.
- **AI commercial models inside SaaS pricing**: usage-based pricing for AI features, hybrid floor + overage, or tier-gated for premium tiers.

## When AI Is Delivered as a SaaS Feature

When the engagement is specifically the build of AI features inside a multi-tenant SaaS product — RAG, copilots, agents, AI analytics, AI-assisted decisioning, AI-generated artefacts inside the SaaS — **branch out of this skill** and use the AI-on-SaaS family:

- [ai-on-saas-combined-methodology](../../ai-on-saas-proposals/ai-on-saas-combined-methodology/SKILL.md) — headline methodology (three planes: control, application, AI).
- [ai-on-saas-discovery-and-qualification](../../ai-on-saas-proposals/ai-on-saas-discovery-and-qualification/SKILL.md) — discovery and qualification overlay.
- [ai-on-saas-business-case-and-roi](../../ai-on-saas-proposals/ai-on-saas-business-case-and-roi/SKILL.md) — AI ROI that resists hype.
- [ai-on-saas-pricing-and-packaging-proposal](../../ai-on-saas-proposals/ai-on-saas-pricing-and-packaging-proposal/SKILL.md) — AI pricing patterns inside SaaS pricing.
- [ai-on-saas-poc-and-pilot-scoping](../../ai-on-saas-proposals/ai-on-saas-poc-and-pilot-scoping/SKILL.md) — POC with binary eval criteria.
- [ai-on-saas-risk-and-responsible-ai](../../ai-on-saas-proposals/ai-on-saas-risk-and-responsible-ai/SKILL.md) — AI risk register and Responsible-AI commitment.
- [ai-on-saas-compliance-credentials](../../ai-on-saas-proposals/ai-on-saas-compliance-credentials/SKILL.md) — Trust and Compliance for AI.
- [ai-on-saas-procurement-and-questionnaire](../../ai-on-saas-proposals/ai-on-saas-procurement-and-questionnaire/SKILL.md) — AI procurement questionnaire pack.
- [ai-on-saas-change-management-and-adoption](../../ai-on-saas-proposals/ai-on-saas-change-management-and-adoption/SKILL.md) — AI adoption and HITL design.
- [ai-on-saas-team-composition](../../ai-on-saas-proposals/ai-on-saas-team-composition/SKILL.md) — AI-on-SaaS roster (AI Safety Lead, Eval Engineer, MLOps, Prompt, RAG, Data-for-AI).
- [ai-on-saas-vertical-positioning](../../ai-on-saas-proposals/ai-on-saas-vertical-positioning/SKILL.md) — vertical AI plays.

This skill (`ai-transformation-proposal`) remains the right entry point for **generic AI strategy** engagements where there is no SaaS layer (AI consulting, AI agents in a single-tenant context, AI automation in the buyer's own software estate). Once a SaaS layer is in scope, the AI-on-SaaS family takes over.

## Agent Branch

When the engagement delivers one or more AI agents (autonomous LLM systems that plan, call tools, decide, and act on the buyer's behalf), or a multi-agent system, route to the AI-agent family:

- Headline: [ai-agent-methodology](../../ai-agent-proposals/ai-agent-methodology/SKILL.md) — eight-phase agentic methodology (Discover → Action-Catalogue → Architecture for Autonomy → Build → Shadow → Supervised → Agentic → Operate).
- Discovery: [ai-agent-discovery-and-qualification](../../ai-agent-proposals/ai-agent-discovery-and-qualification/SKILL.md) — Agent-vs-Workflow Filter; autonomy ladder L0–L5; irreversibility tolerance; oversight model.
- Business case: [ai-agent-business-case-and-roi](../../ai-agent-proposals/ai-agent-business-case-and-roi/SKILL.md) — tasks-per-FTE with intervention discount; three-scenario ROI keyed to autonomy ramp.
- Pricing: [ai-agent-pricing-and-packaging-proposal](../../ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md) — six agent pricing patterns; intervention credit; vendor cost pass-through.
- Risk and Responsible-AI: [ai-agent-risk-and-responsible-ai](../../ai-agent-proposals/ai-agent-risk-and-responsible-ai/SKILL.md) — twelve-entry agent register; Responsible-AI Agent Commitment with named Agent Safety Lead.
- Procurement: [ai-agent-procurement-and-questionnaire](../../ai-agent-proposals/ai-agent-procurement-and-questionnaire/SKILL.md) — ten-domain agent answer pack.
- Vertical: [ai-agent-vertical-positioning](../../ai-agent-proposals/ai-agent-vertical-positioning/SKILL.md) — agent plays per vertical with autonomy stance.

Use the AI-agent family **with** the AI-on-SaaS family when the agent lives inside a multi-tenant SaaS product.

## Do Not Use When

- Do not use this skill when a neighbouring specialist named in the description owns the primary decision; route there first and use this skill only as a supporting layer.
- Do not use it to invent buyer facts, evidence, legal positions, statutory rules, delivery capacity, or current external claims.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| AI brief, use cases, data constraints, operating context, and decision criteria | Buyer, ToR, approved project record, accountable owner, or verified evidence source | Yes | Stop the affected decision, name the missing source, and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| AI proposal strategy and method block | Evaluator and delivery lead | Claims trace to supplied evidence; assumptions, owners, exclusions, decisions, and observable acceptance tests are explicit. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Decision and source trace for the output | Reviewer and release owner | Each load-bearing choice identifies its source, rationale, accountable owner, and any unassessed check. |

## Capability Contract

Default to read-only for analysis, critique, discovery, and review. Minimum capability is access to the supplied artefacts and permission to inspect or calculate relevant evidence. Edit only the requested working copy. Do not publish, send, spend, change production systems, certify compliance, make a statutory claim, or approve a commercial concession without explicit authority.

## Degraded Mode

If required files, interviews, finance doctrine, search evidence, calculation tools, network access, or specialist review are unavailable, return the narrowest useful qualified result. Mark unavailable checks as not assessed, separate facts from assumptions, and state what is needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Choose generic AI, AI-on-SaaS, or AI-agent route | Classify by tenancy and autonomous-action scope before drafting. | Using a generic AI method for a multi-tenant or action-taking system. |
| Evidence conflicts or authority is absent | Stop the affected recommendation, record the conflict, and seek the named owner’s decision. | Invented facts or unauthorised commitments. |
| Evidence and approval are complete | Proceed within scope and retain the decision trace. | Irreproducible approval or scope drift. |

## Workflow

1. Confirm the consumer, decision, neighbouring-skill route, authority, and required inputs; stop if the primary route or accountable owner is unknown.
2. Inspect supplied evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a load-bearing contradiction.
3. Apply the domain method and decision rules, preserving the repository’s proposal voice and specialist constraints.
4. Draft the contracted output with observable acceptance conditions and an evidence trace.
5. Review alignment with scope, work plan, team, pricing, risk, and dependent proposal sections; recover by revising the affected choice and rerunning the check.
6. Run the critical-analysis and anti-slop gates; block release on unsupported claims, failed safety or finance gates, or an F slop grade.

## Quality Standards

- Every load-bearing claim is verified or explicitly qualified, and the output distinguishes fact, assumption, recommendation, and commitment.
- Scope, method, work plan, staffing, pricing, risks, dependencies, and acceptance conditions remain mutually consistent.
- The output preserves domain constraints, names accountable owners, covers failure paths, and blocks unsupported or unauthorised promises.
- British English and the repository’s East African professional tone are used unless the buyer requires another standard.
- The critical-analysis and anti-slop gates pass before release, with no unassessed check represented as passed.

## Anti-Patterns

- Inventing a buyer fact or proof point. Fix: cite the supplied source or mark the statement as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and name the evidence needed to resume.
- Copying a neighbouring skill’s method without routing. Fix: use the specialist for the primary decision and retain only the supporting layer here.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: state an observable measure, evidence record, and decision owner.
- Adding premium or technical claims without delivery capacity. Fix: reconcile the claim with named people, time, budget, dependencies, and authority.

## Worked Example

A buyer wants document classification and a supervisor copilot, with no autonomous actions. Use this skill, define evaluation and human review, and do not import agentic autonomy claims.

<!-- dual-compat-end -->

## References

- [technical-strategy-credibility-checklist](../../profiles-sectors/references/technical-strategy-credibility-checklist.md) - technical strategy, SaaS, cloud, AI, roadmap, and operations credibility checks.
- [discovery-question-bank-for-proposals](../../profiles-sectors/references/discovery-question-bank-for-proposals.md) - AI use-case, data, workflow, governance, and support discovery.
- [proposal-objection-handling](../../profiles-sectors/references/proposal-objection-handling.md) - responses to AI quality, cost, risk, data, support, and procurement objections.
- [saas-multi-tenant-architecture-block](../../profiles-sectors/references/saas-multi-tenant-architecture-block.md) - tenant isolation for AI features.
- [saas-implementation-methodology-blocks](../../profiles-sectors/references/saas-implementation-methodology-blocks.md) - methodology blocks where AI workstreams slot in.
- [saas-trust-and-compliance-section-template](../../profiles-sectors/references/saas-trust-and-compliance-section-template.md) - trust posture for AI-on-SaaS.
- [premium-pricing-and-value-defense](../premium-pricing-and-value-defense/SKILL.md) - premium AI fee justification and commercial options.
- [customer-service-and-maintenance-proposals](../customer-service-and-maintenance-proposals/SKILL.md) - AI operations, support, maintenance, and escalation language.
- [saas-implementation-methodology](../../saas-proposals/saas-implementation-methodology/SKILL.md) - SaaS implementation methodology that AI workstreams slot into.
- [saas-multi-tenant-architecture-credibility-block](../../saas-proposals/saas-multi-tenant-architecture-credibility-block/SKILL.md) - architectural literacy for AI-on-SaaS bids.
