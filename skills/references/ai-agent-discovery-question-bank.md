# AI-Agent Discovery Question Bank

Long-form discovery question bank for engagements that will design, build, or operate AI agents — software that plans, calls tools, decides, and acts on the buyer's behalf. Pairs with `ai-agent-discovery-and-qualification` and extends `ai-on-saas-discovery-question-bank.md`.

Use these questions in discovery calls, written discovery memos, paid agent-discovery workshops, and the Understanding-of-Assignment section of the proposal. Capture answers in `BRIEF.md`. Missing answers are gaps, not assumptions.

## 0. The Agent-vs-Workflow Filter

- What is the outcome you want the agent to own end-to-end?
- Can the steps to that outcome be enumerated up-front in a workflow tool? If yes, why are we not using a workflow tool?
- Does the agent need to call tools and act on systems of record, or only respond conversationally?
- Will the agent need to judge whether evidence is sufficient and decide to act, escalate, or abstain?
- Are you buying agent **outcomes**, or are you buying step-by-step assistance to your team?

If three or more of these point to a workflow, recommend the workflow path and avoid pricing this as an agent.

## 1. Workflow Fit and Outcome Definition

- Walk us through the workflow the agent will live inside. Who owns the outcome today? Who fixes things when the outcome is wrong?
- What is the outcome unit (resolved ticket, triaged claim, reconciled batch, drafted contract, recovered debt, closed bug)?
- Volume per day per tenant; expected growth; seasonal peaks.
- Baseline cost per outcome today (fully loaded).
- Baseline cycle time, in median and 95th-percentile.
- Baseline success rate — what does "success" mean, and who defines it?
- What is the upstream input quality? What does the workflow do if upstream is broken?

## 2. Autonomy Level Target

- What autonomy level do you expect at go-live? At month six? At month twelve?
- Are there action classes for which you accept L3+ autonomy at go-live? If yes, name them.
- Are there action classes for which L0 (suggest only) is the permanent commitment? If yes, name them.
- Who signs off autonomy-level decisions per action class?
- How will autonomy be reviewed (cadence, evidence required)?

## 3. Action Catalogue

- List every action you expect the agent to be able to take. For each: the system it acts on, the authority required, the rate per day per agent per tenant.
- Which actions are reversible without harm (read, draft, propose)?
- Which actions are reversible with effort (update record, send draft to internal review)?
- Which actions are **irreversible** (money out, regulatory filing submitted, public statement issued, ledger posted, account closed, refund authorised, transaction settled)?
- Which actions cross legal entity, regulator jurisdiction, or contractual boundary?
- Which actions trigger external communications (email, chat, SMS, voice)?

## 4. Oversight Model

- Human-in-the-loop on every action; human-on-the-loop monitoring a queue; human-out-of-the-loop with audit only — pick per action class.
- Intervention SLA — how long can a human take to confirm or reject before the agent times out, acts, or aborts?
- Oversight queue staffing — who will staff it; what is the floor headcount; what is on-call coverage out-of-hours?
- Escalation tree — supervisor → safety lead → SteerCo. Who is on call?

## 5. Success Metric

- Is the success metric task-success rate (binary), intervention rate, deflection rate, time-to-resolution, or a composite?
- What is the floor below which the engagement is a failure?
- What is the ceiling at which the engagement is a win?
- Are there leading indicators you want to track (abstain-correctness, override rate, contestability cases)?
- Who signs the metric definition?

## 6. Irreversibility Tolerance

- For each irreversible action class, what is the worst plausible single-incident cost (financial, regulatory, reputational, safety)?
- What is your tolerance for irreversibility incidents per quarter? (Often zero in regulated workflows.)
- Do you require human-final approval on every irreversible action regardless of agent confidence?
- Do you require dual approval above a value threshold?

## 7. Accountability and Liability

- Who is legally accountable for an agent action? In our position the buyer is always accountable to the regulator and the customer; is there a different expectation?
- Is professional indemnity, errors-and-omissions, or AI-specific liability cover in place?
- Is there a contractual liability allocation the buyer expects in the MSA?
- What is the redress mechanism for an affected user, customer, or regulator? Named owner; SLA.

## 8. Scope-Confinement and Identity

- How will the agent be confined — tool allowlist, parameter bounds, value bounds, time-window, tenant scope, data scope?
- Does the agent act under its own identity, a service identity, or the user's identity (delegated)?
- What is the impersonation policy when the agent communicates externally? What disclosure is required?
- Are there jurisdictions where disclosure rules are stricter (EU AI Act Article 50; sectoral rules)?

## 9. Regulator Exposure for Agentic Actions

- Which regulators have a stance on agentic systems or autonomous decisioning that affects your scope?
- Is there a sectoral rule on autonomous decisioning (financial-services credit / AML; healthcare clinical / non-clinical; legal practice rules; public-sector administrative law)?
- Is transparency-to-affected-party required by regulation, sectoral code, or your own policy?
- Has the regulator engaged with you on agentic AI? If yes, on what terms?
- Is sovereign-AI a requirement (on-prem / in-country inference)?

## 10. Operational Readiness

- Who operates the agent fleet after go-live — agency, buyer, joint?
- What is the kill-switch architecture (per-action, per-agent, per-tenant, global)? Who has authority?
- What is the drill cadence — quarterly minimum recommended?
- What is the incident runbook for an irreversible-action incident? For a prompt-injection breach? For a scope breach? For a regulator inquiry?
- What is the refresh cadence for prompts, models, and the action catalogue?
- How will the buyer audit the agent fleet — internal audit, external audit, regulator audit, third-party assurance?

## 11. Multi-Agent (where applicable)

- Will the engagement involve multiple agents that delegate to or supervise each other?
- What orchestration pattern is expected — manager-worker, planner-actor-critic, swarm?
- What is the blast-radius limit if one agent fails?
- How will multi-agent loops be detected and broken?
- Will inter-agent communications be auditable to the same standard as agent-system communications?

## 12. Commercial Posture

- Pricing instinct — per-resolution, per-outcome, per-step, per-agent, hybrid, success-based?
- Tolerance for variable bills — high, medium, low?
- Skin-in-the-game appetite — happy with success-based bonus, or prefer fixed?
- Incumbent vendor or in-house team that the agent displaces — political sensitivity?
- FX exposure — model costs in USD, revenue in local currency?

## 13. Change-Readiness

- How will affected staff react — augmented, redeployed, retrained, displaced?
- Has the buyer communicated agent plans internally? Externally?
- Is union, works-council, or staff-association consultation required?
- What is the supervisor retraining commitment?
- What is the augment / redeploy / retrain framing the buyer will use publicly?

## How to Use This Bank

- Run a structured one- to three-hour agent-discovery workshop with the buyer's product owner, head of operations, CTO, CISO, DPO, general counsel, sponsor, and a representative supervisor.
- Capture answers in a discovery memo, with the gaps explicitly listed.
- Run the **Agent-vs-Workflow Filter** before any pricing discussion.
- Score the engagement on the **Agentic Qualification Scorecard** (`ai-agent-discovery-and-qualification`).
- Decide: full proposal, paid agent feasibility study, shadow-mode pilot first, or polite decline.
- Carry the **Agentic Discovery Findings** paragraph into Understanding-of-Assignment.
