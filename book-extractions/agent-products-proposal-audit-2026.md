# AI-Agent Products Proposal Skills Audit 2026

Internal audit produced for the proposal-skills engine to close the **AI-agent / multi-agent product** gap left open at the end of the 2026 AI-on-SaaS hardening session. The AI-on-SaaS family covered RAG, copilots, AI analytics, and AI-assisted workflows inside a multi-tenant SaaS product. It treated agents as one of many feature classes, with hooks but no dedicated arsenal. This audit defines the dedicated arsenal — discovery, business case, pricing, methodology, POC, risk, change management, procurement, vertical positioning — for engagements where the buyer is procuring **autonomous agents** (LLMs that plan, call tools, act, and complete tasks on the buyer's behalf), either as a stand-alone product, a multi-agent system, or an agentic layer inside a SaaS product.

Agents are the most differentiated and risk-sensitive AI feature class to propose. They make value claims a CFO can chase (per-resolution, per-outcome, FTE-equivalent). They make accuracy claims a CTO can audit (task-success, intervention rate, irreversible-action incidents). They make procurement, legal, and regulatory claims a CISO and DPO must defend (autonomy levels, audit logs, kill-switches, accountability for agent actions). They invite objections no other AI feature class invites — autonomy, irreversibility, jobs, accountability, regulator action. They support pricing models no other AI feature class supports cleanly — per-resolution, per-step, per-outcome, per-agent, hybrid. The engine must treat agents as a first-class proposal class, not as a footnote inside AI-on-SaaS.

## Scope of This Audit

The audit covers engagements with at least three of these characteristics:

1. The deliverable is one or more **autonomous AI agents** — software that perceives, plans, decides, calls tools, and acts to complete a task assigned by a user, with or without explicit step-by-step confirmation.
2. The deliverable is a **multi-agent system** — agents that delegate to, supervise, or collaborate with other agents (orchestrator pattern, manager-worker pattern, swarm pattern).
3. The agent **takes actions on the buyer's behalf** — sends communications, raises tickets, books resources, executes transactions, files claims, posts to ledgers, deploys infrastructure, mutates data in systems of record.
4. The buyer or their regulator imposes **autonomy constraints** — human-in-the-loop for irreversible actions, human-on-the-loop for high-stakes, audit-log requirements, kill-switch requirements, scope confinement.
5. The buyer expects a **commercial model attached to outcomes**, not licences — per-resolution, per-outcome, per-ticket-closed, per-claim-triaged, per-deployment, with intervention discount.

## What the Engine Has Today

| Existing asset | What it covers | Gap for agentic engagements |
|---|---|---|
| `skills/strategy-positioning/ai-transformation-proposal/SKILL.md` | AI strategy, agentic workflows hook, governance, evaluation, maintenance | No agent-specific methodology, no autonomy-level taxonomy, no agent ROI, no agent risk register, no agent pricing patterns, no agent objections |
| `skills/ai-on-saas-proposals/ai-on-saas-combined-methodology/SKILL.md` | Three-plane methodology (control, application, AI) with eval, model gateway, RAG, red-team | Treats agents as a feature class inside the AI plane; does not stage shadow → supervised → agentic; no action-catalogue design; no irreversibility gating; no kill-switch drill |
| `skills/ai-on-saas-proposals/ai-on-saas-discovery-and-qualification/SKILL.md` | Workflow-AI fit, hallucination tolerance, AI maturity | No "is this really an agent vs a workflow?" filter; no autonomy-level discovery; no irreversibility-tolerance discovery; no oversight-model discovery; no accountability discovery |
| `skills/ai-on-saas-proposals/ai-on-saas-business-case-and-roi/SKILL.md` | AI Value Stack + AI Cost Stack + eval-margin + cost-of-tokens + downside | Hallucination liability sized but **agentic incident liability, irreversibility cost, intervention overhead, scope-creep cost** not modelled; tasks-per-FTE saved with intervention discount missing |
| `skills/ai-on-saas-proposals/ai-on-saas-pricing-and-packaging-proposal/SKILL.md` | Bundled, tier upsell, usage credits, hybrid, fair-use | No per-resolution, per-outcome, per-step, per-agent, intervention-credit, vendor-cost-pass-through patterns |
| `skills/ai-on-saas-proposals/ai-on-saas-poc-and-pilot-scoping/SKILL.md` | Binary eval criteria, golden dataset, abstain logic, exit gates | No shadow-mode pilot, supervised-mode pilot, agentic-mode pilot staging; no irreversible-action ceiling; no intervention-rate ceiling; no abort condition specific to autonomy |
| `skills/ai-on-saas-proposals/ai-on-saas-risk-and-responsible-ai/SKILL.md` | Ten-entry AI risk register (model, hallucination, injection, leakage, sub-processor, regulatory, lock-in, contamination, drift, reputational) | Missing: autonomy-action incident, irreversibility incident, action accountability, scope-creep, multi-agent collusion, prompt-injection-via-tool-output, agent persistent memory poisoning, regulator action on agentic systems |
| `skills/ai-on-saas-proposals/ai-on-saas-compliance-credentials/SKILL.md` | EU AI Act, NCAIS/NAIS/AI Policy KE/NG/ZA/UG/RW, ISO 42001/23894, NIST AI RMF, model cards, eval CI, hallucination SLO, red-team, sub-processor disclosure, region routing, sovereign-AI | Missing: agent action audit log, irreversibility gating, intervention SLO, kill-switch drill, agent red-team catalogue, agent identity, action-scope attestation |
| `skills/ai-on-saas-proposals/ai-on-saas-procurement-and-questionnaire/SKILL.md` | Eight-domain AI questionnaire (providers, training, retention, region, sovereign, eval, safety, governance) | Missing: autonomy level, action catalogue, irreversibility classification, kill-switch evidence, scope-confinement evidence, agent identity / impersonation policy, action audit log access |
| `skills/ai-on-saas-proposals/ai-on-saas-change-management-and-adoption/SKILL.md` | Trust staging (shadow → confirm → supervised → auto), augment-vs-replace, HITL | Trust staging applied generically; for agents the stages, evidence, communications and union impact are sharper — also missing "agent-on-your-behalf" disclosure UX |
| `skills/ai-on-saas-proposals/ai-on-saas-team-composition/SKILL.md` | AI roster (Safety Lead, Eval Engineer, MLOps, Prompt, RAG, Data, ML Lead) | Missing: Agent Architect, Tool Engineer, Human-in-the-loop Designer, Agent Safety Lead, Agent Ops; operations after go-live distinct from non-agent AI ops |
| `skills/ai-on-saas-proposals/ai-on-saas-vertical-positioning/SKILL.md` | FS, insurance, public sector, healthcare, education, customer support | Vertical agent plays not specialised (resolution agents, compliance/reconciliation agents, claims triage, citizen-service caution, admin-only healthcare, legal drafting/review, ops triage) |
| `skills/saas-proposals/saas-objection-handling-and-competitive-displacement/SKILL.md` | Price, risk, vendor lock, build-in-house, AI accuracy, adoption | Missing: autonomy, jobs displacement, irreversibility, accountability "who is liable if the agent is wrong?", regulator action, agent-on-agent failure cascades |

The hooks point at the right concerns. They do not give the proposal writer methodology, deliverables, gates, acceptance criteria, risk entries, pricing patterns, compliance subsections, procurement answers, or objection handling specific to agents.

## What the Engine Lacks (Synthesised)

The engine cannot today produce, end-to-end, a Bain/EY/McKinsey-grade proposal for an agentic engagement because nine artefact families are missing:

1. **Agentic discovery and qualification** — the "is this an agent or a workflow?" filter; autonomy-level discovery (L0–L5); irreversibility-tolerance discovery; oversight-model discovery; success-metric discovery (task-success, intervention rate); regulatory exposure for agentic actions; accountability discovery.
2. **Agent ROI rigour that resists agentic hype** — tasks-per-FTE-saved with intervention discount; AHT reduction with quality cap; deflection rate; time-to-resolution; downside (regulator action, irreversible-incident cost, intervention overhead, scope-creep cost, escalation cost); three-scenario model accounting for autonomy-level, not just accuracy.
3. **Agent pricing patterns** — per-resolution, per-outcome, per-step, per-agent, hybrid, success-based, intervention-credit reduction, vendor-cost-pass-through; fair-use specific to agents (per-tenant action ceiling, abuse ceiling, anomalous-action ceiling); abort and refund triggers; FX and model-cost-pass-through.
4. **Agent POC and pilot scoping** — shadow-mode pilot (agent runs, does not act), supervised-mode pilot (agent acts, human confirms), agentic-mode pilot (agent acts inside scope, escalates outside); binary task-success threshold; irreversible-action ceiling; intervention-rate ceiling; abort conditions specific to autonomy.
5. **Agent methodology** — Discover → Action-Catalogue Design → Architecture (autonomy levels, oversight, kill-switch, audit) → Build → Shadow → Supervised → Agentic → Operate; gates per phase; deliverables with binary acceptance.
6. **Agent risk register and Responsible-AI agent commitments** — autonomy-action incident, irreversibility, accountability, scope-creep, multi-agent collusion, prompt-injection-via-tool-output, memory poisoning, regulator action; Responsible-AI agent commitments (human-final for irreversibility, full audit log, contestability, kill-switch drill cadence).
7. **Agent compliance credentials** — action audit log, irreversibility gating, intervention SLO, kill-switch drill evidence, red-team catalogue (agent-specific), agent identity / impersonation policy, action-scope attestation, multi-agent governance evidence.
8. **Agent procurement Q&A** — autonomy level per use case, action catalogue, irreversibility classification, kill-switch architecture and drill cadence, scope-confinement evidence, agent identity, audit-log access, sub-processor exposure for tool calls.
9. **Agent change management, team composition, objection handling, and vertical positioning** — trust staging (shadow → confirm → supervised → agentic) with named evidence per stage; employee-impact framing (augment not replace, retraining for human supervisors); union / works-council; agent-on-your-behalf disclosure UX; Agent Architect, Tool Engineer, Eval Engineer, Safety Lead, Human-in-the-loop Designer roster; vertical plays for support, FS, insurance, public sector (extreme caution), healthcare (admin-only), legal (drafting / review), operations.

## NEW SKILLS

Create the following under `skills/<skill-name>/` with `SKILL.md` and `references/` where useful.

| New skill | Why it is its own skill |
|---|---|
| `ai-agent-discovery-and-qualification` | Discovery for agents is sharply different from non-agent AI: the first question is *"is this really an agent or just a workflow with an LLM?"*; the second is autonomy level; the third is irreversibility tolerance; the fourth is accountability. Cannot be folded into `ai-on-saas-discovery-and-qualification` without losing the autonomy and accountability dimensions. |
| `ai-agent-business-case-and-roi` | Agent ROI is task-based (tasks-per-FTE, AHT, deflection, resolution time) not feature-based. Intervention discount, irreversibility cost, scope-creep cost, escalation cost are agent-specific. Cannot be folded into `ai-on-saas-business-case-and-roi`. |
| `ai-agent-pricing-and-packaging-proposal` | Per-resolution, per-outcome, per-step, per-agent, intervention-credit are agent-specific commercial structures. Vendor-cost-pass-through behaves differently when an agent makes 10–100 model calls per task. Cannot be folded into AI-on-SaaS pricing. |
| `ai-agent-poc-and-pilot-scoping` | Shadow → supervised → agentic staging is the agent-pilot pattern. Binary task-success, intervention-rate ceiling, irreversible-action ceiling are agent-specific. Cannot be folded into AI-on-SaaS POC. |
| `ai-agent-methodology` | The agent methodology adds **Action-Catalogue Design** and **Autonomy-Level Architecture** as named phases. Cannot be folded into the three-plane combined methodology without losing those phase gates. |
| `ai-agent-risk-and-responsible-ai` | Twelve agent-specific risks (autonomy, irreversibility, accountability, scope-creep, multi-agent, injection-via-tool-output, memory poisoning, regulator on agentics, kill-switch failure, identity, escalation overload, legacy-system damage). Responsible-AI agent commitments (human-final for irreversibility, full audit, contestability, kill-switch drill cadence) extend the AI-on-SaaS Responsible-AI commitment. |
| `ai-agent-compliance-credentials` | Action audit log, irreversibility gating, intervention SLO, kill-switch drill evidence, agent red-team catalogue are agent-specific compliance artefacts. |
| `ai-agent-change-management-and-adoption` | Trust staging is sharper for agents (each stage has named action-class evidence, not just "use it more"); jobs framing is more sensitive; agent-on-behalf disclosure UX is unique to agents. |
| `ai-agent-team-composition` | Agent Architect, Tool Engineer, Human-in-the-loop Designer are not in the AI-on-SaaS roster. Agent Safety Lead is distinct from AI Safety Lead in regulated bids. |
| `ai-agent-vertical-positioning` | Vertical agent plays carry vertical-specific autonomy and irreversibility stances (citizen-service extreme caution, healthcare admin-only, legal drafting/review with bar-rules implication). |

## ENHANCEMENTS TO EXISTING SKILLS

These existing skills receive an "agent branch" or "agent overlay" — not a duplication, just a pointer and a short addition so a writer working in the parent skill is routed to the agent stack when the engagement is agentic.

- `skills/strategy-positioning/ai-transformation-proposal/SKILL.md` — add agent branch in the routing close.
- `skills/ai-on-saas-proposals/ai-on-saas-combined-methodology/SKILL.md` — agent-phases overlay sentence.
- `skills/ai-on-saas-proposals/ai-on-saas-business-case-and-roi/SKILL.md` — agent ROI patterns reference pointer.
- `skills/ai-on-saas-proposals/ai-on-saas-pricing-and-packaging-proposal/SKILL.md` — agent pricing patterns reference pointer.
- `skills/ai-on-saas-proposals/ai-on-saas-risk-and-responsible-ai/SKILL.md` — agent risk addendum pointer.
- `skills/ai-on-saas-proposals/ai-on-saas-compliance-credentials/SKILL.md` — agent audit / kill-switch evidence pointer.
- `skills/ai-on-saas-proposals/ai-on-saas-procurement-and-questionnaire/SKILL.md` — agent procurement Q&A pointer.
- `skills/ai-on-saas-proposals/ai-on-saas-poc-and-pilot-scoping/SKILL.md` — agent shadow / supervised / agentic stages pointer.
- `skills/saas-proposals/saas-objection-handling-and-competitive-displacement/SKILL.md` — agent objections (autonomy, jobs, irreversibility, accountability, regulator) pointer.
- `skills/ai-on-saas-proposals/ai-on-saas-change-management-and-adoption/SKILL.md` — trust-staging detail for agents pointer.
- `skills/ai-on-saas-proposals/ai-on-saas-team-composition/SKILL.md` — agent roles added pointer.
- `skills/domain-delivery/monitoring-and-evaluation/SKILL.md` — agent dashboards (task success, intervention, irreversible-action incidents) pointer.
- `skills/domain-delivery/risk-management/SKILL.md` — agent risk register pointer.
- `skills/pipeline/06-methodology/SKILL.md` and `skills/pipeline/10-financial-proposal/SKILL.md` — agent pointer.
- Parent routing — `CLAUDE.md`, `README.md`, `AGENTS.md`, `skills/SKILL.md` — list the agent family.

## NEW REFERENCES UNDER `skills/profiles-sectors/references/`

- `ai-agent-discovery-question-bank.md` — long-form question bank covering ten agent dimensions.
- `ai-agent-business-case-template.md` — formulas (tasks-saved × intervention-discount; downside scenarios), worked examples.
- `ai-agent-pricing-models-reference.md` — per-resolution, per-step, per-agent, outcome-based, hybrid, with worked examples and clauses.
- `ai-agent-poc-scoping-template.md` — shadow / supervised / agentic stages with binary thresholds and abort gates.
- `ai-agent-risk-register-for-proposals.md` — twelve-entry agent risk register.
- `ai-agent-responsible-ai-commitment.md` — human-final, full audit, contestability, kill-switch drill cadence.
- `ai-agent-trust-and-compliance-template.md` — action audit log, intervention SLO, kill-switch evidence, red-team catalogue.
- `ai-agent-procurement-questionnaire-pack.md` — autonomy, audit, kill-switch, sub-processor, irreversibility, identity.
- `ai-agent-methodology-blocks.md` — drop-in methodology section with phases and gates.
- `ai-agent-team-composition-template.md` — agent roster with role descriptions and CV bullets.
- `ai-agent-change-management-playbook.md` — trust-staging detail with action-class evidence per stage.
- `ai-agent-objection-handling-playbook.md` — agent objections with replies and evidence.
- `ai-agent-win-themes-and-discriminators.md` — agent-specific win themes and discriminators.
- `ai-agent-metrics-glossary.md` — task success, intervention rate, escalation rate, irreversible-action rate, AHT, deflection, time-to-resolution, scope-confinement, audit completeness.
- `vertical-ai-agent-customer-support.md`
- `vertical-ai-agent-financial-services.md`
- `vertical-ai-agent-insurance.md`
- `vertical-ai-agent-public-sector.md`
- `vertical-ai-agent-healthcare.md`
- `vertical-ai-agent-legal.md`
- `vertical-ai-agent-operations.md`

## How These Skills Compose with AI-on-SaaS

When the agent is deployed as a stand-alone product or service, load the agent stack only.

When the agent is deployed as an agentic layer inside a multi-tenant SaaS product, load **both** stacks: `ai-on-saas-combined-methodology` is the headline; the agent stack overlays the AI plane with agent-specific phases (Action-Catalogue Design, Autonomy-Level Architecture), the agent risk register entries, the agent pricing pattern, the agent procurement answers, and the agent change-management staging.

When the agent is a single-LLM tool-using assistant ("copilot with actions"), use the agent stack at a lighter weight — autonomy L1–L2, scope tightly confined, action catalogue small, HITL on every action — but still apply the discipline.

## Recommended Sequencing for the Build Session

1. Write the audit (this document).
2. Build the ten new `SKILL.md` files in dependency order: discovery → business case → pricing → methodology → POC → risk → compliance → procurement → change management → team composition → vertical positioning.
3. Build the fifteen new references.
4. Enhance the existing skills with one-line agent pointers.
5. Update parent routing — `CLAUDE.md`, `README.md`, `AGENTS.md`, `skills/SKILL.md`.

## Open Questions and Future Sessions

- **Multi-agent governance** — orchestrator / manager-worker / swarm topology decision rules and proposal-grade governance language. Sketched in the new methodology and risk skills; deeper treatment merits its own session.
- **Agent benchmarks** — buyer-facing benchmark posture (SWE-bench, GAIA, τ-bench, retail / banking benchmarks). Current scope addresses bespoke evaluation; benchmark-aware positioning is a future enhancement.
- **Agent-on-agent commercial models** — when an agent procures or operates another vendor's agent, the pricing chain and accountability chain need treatment. Out of scope for this session.
- **Autonomous coding agents** as a vertical — touched in `vertical-ai-agent-operations.md`; full treatment merits its own vertical session.
- **Agent governance frameworks specific to East Africa** — NITA-U, Rwanda AI Policy, Kenya NCAIS evolving on agentic systems; quarterly regulator scan recommended.

This audit is the basis for the agent proposal arsenal build session that follows.
