---
name: ai-on-saas-team-composition
description: Use when the AI-on-SaaS proposal must present the team composition. Provides the AI-on-SaaS roster (ML lead, prompt engineer, AI safety lead, eval engineer, MLOps engineer, data engineer for AI, RAG engineer) layered on the SaaS roster (control plane lead, application plane lead, SRE, security lead, customer-success lead), with blended-rate and ramp considerations. Extends `07-team-composition` with the AI overlay.
---

# AI-on-SaaS Team Composition
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The Team Composition section of an AI-on-SaaS proposal must demonstrate that the agency understands both SaaS and AI staffing.
- The evaluator scores roster credibility (World Bank TECH-6, AfDB, public-sector procurement, premium enterprise).
- The buyer's CTO will challenge the roster ("who is the AI safety lead?").
- The bid is competitive and a generic roster will lose.

## Do Not Use When

- The engagement is non-AI (use `07-team-composition`).
- The engagement is generic AI consulting with no SaaS layer (use `ai-transformation-proposal` + `07-team-composition`).

## Required Inputs

- The methodology phases and workstreams from `ai-on-saas-combined-methodology`.
- The buyer's procurement framework (TECH-6, AfDB, UNDP, RFP).
- The buyer's blended-rate tolerance.
- The buyer's local-content / sovereign-staffing requirements (if any).
- The agency's bench and named CV pool.

## Workflow

1. Build the **AI-on-SaaS Roster** from the standard role library (below), tuned to the engagement's workstreams and phases.
2. Decide the **Two-of-Everything** rule for client-side critical AI operating roles by go-live: eval owner, prompt owner, AI safety owner, model-gateway operator. The proposal explicitly trains a buyer-side counterpart per agency-side role.
3. Build the **RACI** across SaaS workstreams and AI workstreams.
4. Build the **Ramp Curve**: who is full-time, who is part-time, who is on call, when each role ramps in and out. AI safety, eval, and red-team roles ramp earlier than the build roles, not later.
5. Build the **Blended-Rate Table** if procurement requires it, with AI roles separately costed.
6. Map to **TECH-6** (or equivalent) format if required.
7. Output the **Team Composition** section.

## Standard AI-on-SaaS Roster

### SaaS Side
- **Engagement Lead / Programme Manager** — senior accountable.
- **Solution Architect (SaaS)** — control plane / application plane / tenant isolation.
- **Control Plane Lead** — onboarding, identity, billing, observability.
- **Application Plane Lead** — workflows, integrations, performance.
- **Security and Compliance Lead** — DPA, sub-processor list, audit, hardening.
- **Customer Success Lead** — adoption, value realisation, expansion.
- **Site Reliability Engineer (SRE)** — uptime, SLO, incident response.
- **DevOps Engineer** — CI/CD, environments, infrastructure as code.

### AI Side
- **AI Solution Architect / ML Lead** — AI plane design, model selection criteria, model gateway, AI workstream owner.
- **Prompt Engineer** — system prompts, RAG prompt design, prompt regression.
- **AI Safety Lead** — Responsible-AI commitment owner, red-team scorecard, escalation owner.
- **Eval Engineer** — golden datasets, metric thresholds, eval CI, drift watch.
- **MLOps Engineer** — model gateway, model registry, region routing, fallback, observability for AI.
- **Data Engineer (AI)** — RAG ingestion, embedding pipelines, vector store, data lineage.
- **RAG / Retrieval Engineer** — chunking, retrieval, citation grounding, per-tenant indexes.
- **AI Change and Adoption Lead** — augment-vs-replace, HITL design, trust-building (can be the Customer Success Lead in smaller engagements).

### Shared
- **Quality Assurance Lead** — covers functional QA + AI eval coordination.
- **Project / Programme Manager** — phase orchestration, SteerCo, MAP.
- **Sponsor / Executive Sponsor** — partner side, signs the close.

## Quality Standards

- AI Safety Lead is a named role with a named owner.
- Eval Engineer is a distinct role from QA, ramped early.
- MLOps and Data Engineer (AI) are distinct roles from DevOps and Data Engineer (SaaS), unless the engagement is small enough to combine.
- Two-of-everything applies on the AI side as well as the SaaS side.
- Ramp curve has AI safety, eval, and red-team ramped at Phase 1, not at hardening.
- Blended-rate table separates AI roles where procurement requires it.
- TECH-6 mapping is exact where required (key experts vs non-key experts).

## Anti-Patterns

- "AI lead" as the only AI role on the roster.
- AI Safety as a shared duty of the solution architect.
- Eval Engineer collapsed into QA.
- MLOps collapsed into DevOps in a regulated engagement.
- Ramp curve that puts AI safety into hardening (too late).
- Roster larger than the budget can support.
- Local-content / sovereign-staffing requirement ignored.

## Outputs

- AI-on-SaaS Team Roster table (role, name, allocation, ramp).
- RACI across SaaS and AI workstreams.
- Ramp Curve.
- Blended-Rate Table (where required).
- TECH-6 (or equivalent) mapping (where required).
- Two-of-Everything Plan for client-side counterparts.

## Agent Overlay

For agentic engagements, add three roles not present in the AI-on-SaaS roster: **Agent Architect** (agent loop, planner / actor / critic, autonomy architecture), **Tool Engineer** (tool layer, allowlist, parameter bounds, dry-run, post-call assertions, rollback), and **Human-in-the-loop Designer** (oversight queue, intervention SLA, escalation tree, contestability channel). In multi-agent engagements add **Multi-Agent Orchestrator Engineer**. The AI Safety Lead becomes **Agent Safety Lead** with kill-switch authority. Two-of-Everything extends to **buyer-side Action-Catalogue Owner, Eval Owner, Kill-Switch Operator, Oversight-Queue Lead, Agent Safety Lead**. Load `../ai-agent-team-composition/SKILL.md` for the agent roster.

## References

- `../references/ai-on-saas-team-composition-template.md` — full roster template with sample CV bullets.
- `../07-team-composition/SKILL.md` — base team composition skill.
- `../ai-on-saas-combined-methodology/SKILL.md` — workstreams that the roster covers.
- `../ai-on-saas-change-management-and-adoption/SKILL.md` — change roles overlap.
- `../ai-on-saas-risk-and-responsible-ai/SKILL.md` — AI Safety Lead role.
- `../10-financial-proposal/SKILL.md` — fee schedule that the roster drives.
