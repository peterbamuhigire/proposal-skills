---
name: ai-on-saas-team-composition
description: Use when an AI-on-SaaS proposal must justify the combined AI, data, safety, evaluation, platform, security, SRE, and customer-success roles required for delivery; use the standard team skill when no AI specialist roles are needed.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI-on-SaaS Team Composition
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The Team Composition section of an AI-on-SaaS proposal must demonstrate that the agency understands both SaaS and AI staffing.
- The evaluator scores roster credibility (World Bank TECH-6, AfDB, public-sector procurement, premium enterprise).
- The buyer's CTO will challenge the roster ("who is the AI safety lead?").
- The bid is competitive and a generic roster will lose.

## Do Not Use When

- The engagement is non-AI (use `07-team-composition`).
- The engagement is generic AI consulting with no SaaS layer (use `ai-transformation-proposal` + `07-team-composition`).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The methodology phases and workstreams from `ai-on-saas-combined-methodology`. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's procurement framework (TECH-6, AfDB, UNDP, RFP). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's blended-rate tolerance. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's local-content / sovereign-staffing requirements (if any). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The agency's bench and named CV pool. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Build the **AI-on-SaaS Roster** from the standard role library (below), tuned to the engagement's workstreams and phases.
2. Decide the **Two-of-Everything** rule for client-side critical AI operating roles by go-live: eval owner, prompt owner, AI safety owner, model-gateway operator. The proposal explicitly trains a buyer-side counterpart per agency-side role.
3. Build the **RACI** across SaaS workstreams and AI workstreams.
4. Build the **Ramp Curve**: who is full-time, who is part-time, who is on call, when each role ramps in and out. AI safety, eval, and red-team roles ramp earlier than the build roles, not later.
5. Build the **Blended-Rate Table** if procurement requires it, with AI roles separately costed.
6. Map to **TECH-6** (or equivalent) format if required.
7. Output the **Team Composition** section.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

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

- "AI lead" as the only AI role on the roster. **Fix:** Map distinct AI architecture, data, evaluation, safety, MLOps, and product responsibilities to named roles or justified combined roles.
- AI Safety as a shared duty of the solution architect. **Fix:** Assign AI safety to a named accountable lead with independent escalation and release-gate authority.
- Eval Engineer collapsed into QA. **Fix:** Staff evaluation as a model-quality discipline with golden-set ownership, statistical analysis, regression gates, and evidence retention.
- MLOps collapsed into DevOps in a regulated engagement. **Fix:** Provide explicit MLOps ownership for model gateway, versioning, evaluation deployment, drift, cost, and rollback even if one person covers both roles.
- Ramp curve that puts AI safety into hardening (too late). **Fix:** Place safety leadership in discovery and architecture, with continuing authority through pilot, rollout, and operations.
- Roster larger than the budget can support. **Fix:** Reconcile every role's allocation and ramp with deliverables, workload, rate, budget, and substitution plan.
- Local-content / sovereign-staffing requirement ignored. **Fix:** Map local-content, residency, clearance, language, and sovereign staffing requirements to named personnel and evidence.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI-on-SaaS Team Roster table (role, name, allocation, ramp). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| RACI across SaaS and AI workstreams. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Ramp Curve. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Blended-Rate Table (where required). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| TECH-6 (or equivalent) mapping (where required). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Two-of-Everything Plan for client-side counterparts. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## Agent Overlay

For agentic engagements, add three roles not present in the AI-on-SaaS roster: **Agent Architect** (agent loop, planner / actor / critic, autonomy architecture), **Tool Engineer** (tool layer, allowlist, parameter bounds, dry-run, post-call assertions, rollback), and **Human-in-the-loop Designer** (oversight queue, intervention SLA, escalation tree, contestability channel). In multi-agent engagements add **Multi-Agent Orchestrator Engineer**. The AI Safety Lead becomes **Agent Safety Lead** with kill-switch authority. Two-of-Everything extends to **buyer-side Action-Catalogue Owner, Eval Owner, Kill-Switch Operator, Oversight-Queue Lead, Agent Safety Lead**. Load `../ai-agent-team-composition/SKILL.md` for the agent roster.

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Input-and-assumption record | Proposal lead and reviewer | Every load-bearing claim maps to a source, approved assumption, or explicit gap. |
| Decision and review record | Buyer owner and delivery lead | The selected option, rationale, owner, stop condition, and approval status are visible. |
| Section acceptance check | Evaluator-readiness reviewer | Each output meets its stated acceptance condition and unresolved checks are not presented as passed. |

## Capability and Permission Boundaries

This skill may read supplied tender, discovery, architecture, commercial, security, and operating evidence and draft proposal artefacts within the authorised workspace. It must not publish, send, certify compliance, accept contractual terms, change production systems, spend funds, or disclose confidential evidence without explicit authority. Review and analysis remain read-only by default.

## Degraded Mode

If files, current legal or technical evidence, calculation tools, network access, or reviewers are unavailable, produce the narrowest useful qualified draft. Label assumptions and checks as **not assessed**, omit unsupported assurances or figures, and state the exact evidence and owner needed to complete the work. An unavailable check never becomes a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Role necessity | Tie every role and allocation to a deliverable, gate, or risk owner | Inflated roster or missing accountable specialist |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

If the proposal names an AI safety lead but no evaluation owner or tenant-security owner, show the staffing gap and mobilisation dependency instead of claiming the team is deployment-ready.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/ai-on-saas-team-composition-template.md](../../profiles-sectors/references/ai-on-saas-team-composition-template.md) — full roster template with sample CV bullets.
- [../07-team-composition/SKILL.md](../../pipeline/07-team-composition/SKILL.md) — base team composition skill.
- [../ai-on-saas-combined-methodology/SKILL.md](../ai-on-saas-combined-methodology/SKILL.md) — workstreams that the roster covers.
- [../ai-on-saas-change-management-and-adoption/SKILL.md](../ai-on-saas-change-management-and-adoption/SKILL.md) — change roles overlap.
- [../ai-on-saas-risk-and-responsible-ai/SKILL.md](../ai-on-saas-risk-and-responsible-ai/SKILL.md) — AI Safety Lead role.
- [../10-financial-proposal/SKILL.md](../../pipeline/10-financial-proposal/SKILL.md) — fee schedule that the roster drives.
