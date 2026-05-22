---
name: ai-transformation-proposal
description: Use when writing proposals, EOIs, methodologies, technical approaches,
  work plans, or financial proposals for AI-powered applications, agentic workflows,
  AI analytics, automation, or digital transformation with AI components.
---

# AI Transformation Proposal
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

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

- `../ai-on-saas-combined-methodology/SKILL.md` — headline methodology (three planes: control, application, AI).
- `../ai-on-saas-discovery-and-qualification/SKILL.md` — discovery and qualification overlay.
- `../ai-on-saas-business-case-and-roi/SKILL.md` — AI ROI that resists hype.
- `../ai-on-saas-pricing-and-packaging-proposal/SKILL.md` — AI pricing patterns inside SaaS pricing.
- `../ai-on-saas-poc-and-pilot-scoping/SKILL.md` — POC with binary eval criteria.
- `../ai-on-saas-risk-and-responsible-ai/SKILL.md` — AI risk register and Responsible-AI commitment.
- `../ai-on-saas-compliance-credentials/SKILL.md` — Trust and Compliance for AI.
- `../ai-on-saas-procurement-and-questionnaire/SKILL.md` — AI procurement questionnaire pack.
- `../ai-on-saas-change-management-and-adoption/SKILL.md` — AI adoption and HITL design.
- `../ai-on-saas-team-composition/SKILL.md` — AI-on-SaaS roster (AI Safety Lead, Eval Engineer, MLOps, Prompt, RAG, Data-for-AI).
- `../ai-on-saas-vertical-positioning/SKILL.md` — vertical AI plays.

This skill (`ai-transformation-proposal`) remains the right entry point for **generic AI strategy** engagements where there is no SaaS layer (AI consulting, AI agents in a single-tenant context, AI automation in the buyer's own software estate). Once a SaaS layer is in scope, the AI-on-SaaS family takes over.

## Agent Branch

When the engagement delivers one or more AI agents (autonomous LLM systems that plan, call tools, decide, and act on the buyer's behalf), or a multi-agent system, route to the AI-agent family:

- Headline: `../ai-agent-methodology/SKILL.md` — eight-phase agentic methodology (Discover → Action-Catalogue → Architecture for Autonomy → Build → Shadow → Supervised → Agentic → Operate).
- Discovery: `../ai-agent-discovery-and-qualification/SKILL.md` — Agent-vs-Workflow Filter; autonomy ladder L0–L5; irreversibility tolerance; oversight model.
- Business case: `../ai-agent-business-case-and-roi/SKILL.md` — tasks-per-FTE with intervention discount; three-scenario ROI keyed to autonomy ramp.
- Pricing: `../ai-agent-pricing-and-packaging-proposal/SKILL.md` — six agent pricing patterns; intervention credit; vendor cost pass-through.
- Risk and Responsible-AI: `../ai-agent-risk-and-responsible-ai/SKILL.md` — twelve-entry agent register; Responsible-AI Agent Commitment with named Agent Safety Lead.
- Procurement: `../ai-agent-procurement-and-questionnaire/SKILL.md` — ten-domain agent answer pack.
- Vertical: `../ai-agent-vertical-positioning/SKILL.md` — agent plays per vertical with autonomy stance.

Use the AI-agent family **with** the AI-on-SaaS family when the agent lives inside a multi-tenant SaaS product.

## References

- `../references/technical-strategy-credibility-checklist.md` - technical strategy, SaaS, cloud, AI, roadmap, and operations credibility checks.
- `../references/discovery-question-bank-for-proposals.md` - AI use-case, data, workflow, governance, and support discovery.
- `../references/proposal-objection-handling.md` - responses to AI quality, cost, risk, data, support, and procurement objections.
- `../references/saas-multi-tenant-architecture-block.md` - tenant isolation for AI features.
- `../references/saas-implementation-methodology-blocks.md` - methodology blocks where AI workstreams slot in.
- `../references/saas-trust-and-compliance-section-template.md` - trust posture for AI-on-SaaS.
- `../premium-pricing-and-value-defense/SKILL.md` - premium AI fee justification and commercial options.
- `../customer-service-and-maintenance-proposals/SKILL.md` - AI operations, support, maintenance, and escalation language.
- `../saas-implementation-methodology/SKILL.md` - SaaS implementation methodology that AI workstreams slot into.
- `../saas-multi-tenant-architecture-credibility-block/SKILL.md` - architectural literacy for AI-on-SaaS bids.
