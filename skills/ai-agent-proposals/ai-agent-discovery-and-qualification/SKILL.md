---
name: ai-agent-discovery-and-qualification
description: Use when qualifying an AI-agent opportunity by testing agent-versus-workflow fit, autonomy level, action reversibility, oversight, accountability, success measures, and regulatory exposure.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent Discovery and Qualification
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The buyer has asked for "an agent", "an AI agent", "a multi-agent system", "autonomous AI", "AI that does the work", or named an outcome the agent must complete end-to-end (resolved ticket, triaged claim, reconciled ledger, drafted document).
- The proposal must demonstrate that the agency interrogated **whether the requirement is really agentic** before agreeing to price one.
- The buyer's CFO, CTO, CISO, head of operations, or general counsel will challenge autonomy, irreversibility, accountability, and oversight before approving.
- A workflow-only or copilot-only response would lose to a competitor that read the brief more carefully — or win the bid and fail in delivery.

## Do Not Use When

- The bid is for a copilot, RAG search, AI analytics, or AI-assisted decisioning that does not take actions on the buyer's behalf (use `ai-on-saas-discovery-and-qualification`).
- The bid is for generic AI strategy without an action-taking deliverable (use `ai-transformation-proposal` + `sales-discovery-and-objection-handling`).
- The "agent" in the brief is a chatbot with no tool access and no action capability — qualify the term and route to copilot discovery.

## Domain Inputs

- The buyer's brief, including the verbs the buyer uses ("resolve", "triage", "draft", "post", "deploy", "execute") that imply action.
- The candidate workflow(s) the agent will inhabit, with current owner, volume, and average handling time.
- The buyer's incumbent automation (RPA, workflow engine, BPM, ticketing rules, scripts) — agents often replace or supersede these.
- The buyer's regulator(s) and sector.
- The buyer's incident history with AI, RPA, automation, or chatbots.
- An initial hypothesis of the action surface (which systems will the agent call, with what authority).

## Domain Method

1. Run the **Agent-vs-Workflow Filter** first. If three or more of the five tests fail, the bid is not agentic — push back politely and re-scope.
2. Run the **Autonomy-Level Discovery** — place the candidate use case on the **L0–L5 Agentic Autonomy Ladder**. Buyers who want L4 or L5 for a high-stakes process need a paid feasibility study first.
3. Run the **ten agent-specific discovery lines** (below). Each line has a written answer or a flagged gap. Capture in `BRIEF.md`.
4. Score the engagement on the **Agentic Qualification Scorecard**. One **do-not-bid** row is sufficient to decline politely.
5. Decide and document: full proposal, paid agent feasibility study, shadow-mode pilot first, or polite decline.
6. Write the **Agentic Discovery Findings** paragraph into Understanding-of-Assignment so the evaluator sees the audit trail.

## The Agent-vs-Workflow Filter

A requirement is genuinely agentic if it satisfies at least three of:

1. **Open-ended planning** — the steps cannot be enumerated up-front by a workflow designer; the agent must choose the next step from context.
2. **Tool calls into external systems** — the agent must read from or write to systems of record, not only respond conversationally.
3. **Decision under uncertainty** — the agent must judge sufficiency of evidence and decide to act, escalate, or abstain.
4. **Outcome ownership** — the agent is judged on the outcome (ticket resolved, claim triaged, ledger reconciled), not on a single step.
5. **Dynamic scope** — the action surface is broader than a fixed script; the agent must operate inside a defined boundary but not a defined path.

Fewer than three: this is a workflow with an LLM step. Recommend the buyer the workflow path and avoid agent-pricing exposure.

## The L0–L5 Agentic Autonomy Ladder

| Level | Description | Human role | Typical use case |
|---|---|---|---|
| L0 | Suggest only — the LLM proposes the action; the human executes | Operator | Drafting, summarising, explaining |
| L1 | Confirm each action — the agent calls the tool; the human approves each call | Approver | Email send, ticket update, transaction submit |
| L2 | Confirm exceptions — the agent acts inside policy; the human approves only when the agent flags low confidence | Reviewer | Standard support resolutions; standard claim acknowledgements |
| L3 | Supervise — the agent acts; the human monitors a queue and intervenes on flagged or sampled cases | Supervisor | Bulk triage; categorisation; first-line support |
| L4 | Operate — the agent acts; the human reviews aggregate metrics; intervention is exceptional | Auditor | Low-stakes high-volume operations; internal IT helpdesk |
| L5 | Autonomous — the agent acts; the human reviews only on incident | Accountable owner | Rarely defensible for any externally-facing or high-stakes workflow |

The proposal commits to a level per use case. Mixed-level scopes are normal: L3 for triage, L1 for action.

## The Ten Agent-Specific Discovery Lines

### 1. Workflow Fit and Outcome Definition
- Which workflow does the agent live inside? What is the **outcome** the agent owns (resolved ticket, triaged claim, posted reconciliation, drafted contract)?
- Who owns the outcome today? At what cost per outcome? At what cycle time?
- What is the baseline success rate? What is "success" — and who defines it?

### 2. Autonomy Level Target
- What autonomy level does the buyer expect at go-live? At month 6? At month 12?
- Which action classes are L1 (confirm each), which are L2 (confirm exceptions), which are L3+ (supervise)?
- Who signs off the autonomy-level decision per action class?

### 3. Action Catalogue
- List the actions the agent must be able to take. For each: the system it acts on, the authority required, the reversibility class, the rate per day per agent per tenant.
- Which actions are **irreversible** (money out, regulatory filing submitted, public statement issued, ledger posted)?
- Which actions cross legal entity, regulator jurisdiction, or contractual boundary?

### 4. Oversight Model
- Human-in-the-loop (action requires approval), human-on-the-loop (human monitors, can intervene), human-out-of-the-loop with audit (review after the fact)?
- What is the **intervention SLA** (how long does a human have to confirm or reject before the agent acts or aborts)?
- Who staffs the supervision queue at go-live? What is the cost of supervision?

### 5. Success Metric
- Is the success metric **task-success rate** (binary, did the agent complete the task), **intervention rate** (inverse — how often the human had to step in), **deflection rate** (how often the agent kept work from reaching a human), or **time-to-resolution**?
- What is the floor below which the engagement is a failure?
- What is the ceiling at which the engagement is a win?

### 6. Irreversibility Tolerance
- For each action class, what is the **maximum cost of a single wrong action**? (Financial, regulatory, reputational, safety.)
- What is the buyer's tolerance for irreversible-action incidents per quarter? (Often zero for regulated workflows.)
- Does the buyer require **human-final** approval on every irreversible action regardless of confidence?

### 7. Accountability and Liability
- Who is **legally accountable** for an action the agent takes? The buyer (always, in our position), or is the buyer seeking contractual liability transfer to the agency or the model provider?
- Is professional indemnity, errors-and-omissions, or AI-specific liability cover in place?
- What is the buyer's redress mechanism for an affected user / customer / regulator?

### 8. Scope-Confinement and Identity
- How will the agent be confined — tool allowlist, parameter bounds, value-bound transactions, time-window, tenant scope, data-scope?
- Does the agent act under its own identity, under a service identity, or under the user's identity (delegated)?
- What is the impersonation policy when the agent communicates externally (email, chat, calls)?

### 9. Regulatory Exposure for Agentic Actions
- Which regulator(s) treat agentic actions specifically — EU AI Act (high-risk if decisioning), Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U, Rwanda AI Policy, sectoral (CBK, CBN, SARB, IRA, NAICOM, FSCA, KMPDC, IRBA, ICASA, DCDT).
- Are there sector-specific rules on **autonomous decisioning** (financial services credit / AML / sanctions; healthcare; legal practice rules; bar association rules; public-sector administrative law)?
- Is **transparency-to-affected-party** required (the user is told they are interacting with or being acted upon by an agent)?

### 10. Operational Readiness
- Who operates the agent fleet after go-live — agency, buyer, joint?
- What is the **kill-switch architecture** (per-tenant, per-action-class, per-agent, global)? Who has authority to fire it?
- What is the **drill cadence** for kill-switch, incident response, and rollback?
- What is the runbook for an agent incident (irreversible action, prompt injection, scope breach, regulator inquiry)?

## Agentic Qualification Scorecard

| Dimension | Low (proceed) | Medium (proceed with caveats) | High (paid discovery first) | Do-not-bid |
|---|---|---|---|---|
| Agent vs workflow fit | 4–5 of 5 filter tests pass | 3 of 5 | 2 of 5 | 0–1 of 5 — this is a workflow |
| Autonomy level target | L1–L2 for high-stakes; L3 for low-stakes | L3 for high-stakes | L4 for high-stakes | L5 for regulated / customer-facing |
| Action catalogue | Bounded, reversibility classified, irreversible actions named | Bounded, partly classified | Open-ended, irreversibility unclear | Unbounded, irreversible actions un-named |
| Oversight model | HITL on irreversible; HOTL on reversible; SLA defined | HITL planned, SLA to be designed | HOTL only, no SLA | No oversight, "the agent decides" |
| Success metric | Task-success defined with floor and ceiling | Defined, floor missing | Discussed but not committed | "AI quality is good" |
| Irreversibility tolerance | Zero tolerance for irreversible incidents, mitigations in place | Tolerance discussed | Tolerance high but mitigation thin | Tolerance high, no mitigation |
| Accountability | Buyer-side accountable role named; insurance in place | Accountable role named; insurance pending | Accountability deferred | Accountability sought from agency without commercial basis |
| Scope-confinement | Allowlist, bounds, identity policy defined | Allowlist defined, bounds pending | Scope vague | "The agent can do anything in the system" |
| Regulator exposure | Known and stable; transparency policy in place | Known, transparency pending | Tier or rule unclear | Active regulator concern with no mitigation |
| Operational readiness | Kill-switch and drill cadence defined; operator named | Kill-switch defined, drills to be scheduled | Kill-switch architecture pending | No kill-switch, no drill, no operator |

Score the engagement on each row. Any **do-not-bid** is sufficient to decline politely.

## Quality Standards

- The Agent-vs-Workflow Filter is run before the autonomy ladder. Skipping it produces over-priced workflow projects mislabelled as agentic.
- Autonomy level is per **action class**, not per agent. The same agent can be L3 for triage and L1 for action.
- The success metric is one of task-success, intervention rate, deflection rate, time-to-resolution — not "AI quality is good".
- Irreversibility tolerance is a number, not "we will be careful".
- Accountability is named on the buyer side. The proposal does not promise to transfer liability.
- The action catalogue exists in the win-room file before pricing.
- The Discovery Findings paragraph in Understanding-of-Assignment shows the evaluator the audit trail.

## Domain Risks

- Accepting "we want an AI agent" as a scope.
- Skipping the Agent-vs-Workflow Filter and pricing a workflow as an agent.
- Promising L4 / L5 autonomy on regulated decisioning.
- Treating reversibility as a UX concern instead of a system design concern.
- Quoting "task-success rate" without a floor and a ceiling.
- Listing actions without their reversibility class.
- Letting the buyer assume that the agency will be liable for irreversible-action incidents.
- Naming a kill-switch without naming who holds the authority to fire it.
- Quoting "the agent will run autonomously" in customer-facing workflows.

## Domain Outputs

- Agent-vs-Workflow Filter result (3-of-5 minimum to proceed).
- Autonomy-Level Decision per action class (L0–L5).
- Action Catalogue v0 (system, authority, reversibility, rate).
- Oversight Model (HITL / HOTL / audit + SLA).
- Success Metric Definition with floor and ceiling.
- Agentic Qualification Scorecard (win-room file, not the proposal).
- Agentic Discovery Findings paragraph for Understanding-of-Assignment.
- Go / no-go / paid-discovery / shadow-pilot decision.

## Anti-Patterns

- Inventing a metric, credential, constraint, or buyer position. Fix: cite the supplied source or mark the item as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and state the evidence needed to resume.
- Advancing autonomy without a named gate owner. Fix: require observable evidence, accountable acceptance, and a rollback path.
- Reusing another sector or use case without reassessment. Fix: retest affected parties, action scope, reversibility, and jurisdiction.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: define an observable measure, threshold, evidence record, and decision owner.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| buyer process, action inventory, affected parties, systems, constraints, and success measures | Buyer evidence, ToR, approved discovery record, system owner, or measured operating data | Yes | Stop the affected decision; list the missing source and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Agent qualification record and discovery decision | Opportunity owner and solution architect | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| agent qualification record and discovery decision | Opportunity owner and solution architect | Every load-bearing claim traces to supplied evidence; assumptions, owners, gates, exclusions, and observable acceptance conditions are explicit. |

## Capability Contract

Default to read-only for discovery, analysis, review, and planning. Minimum capability is access to the supplied artefacts and permission to calculate or inspect evidence. Edit only the requested proposal working copy. Do not change production systems, contact affected parties, publish, spend, certify compliance, or approve autonomous action without explicit authority from the accountable owner.

## Degraded Mode

If files, interviews, telemetry, specialist review, network access, or calculation tools are unavailable, produce the narrowest useful qualified result. Mark each unavailable check as not assessed, separate facts from assumptions, lower confidence, and state the evidence needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Agent, workflow, or no-go | Use agency need, action authority, reversibility, oversight, economics, and regulatory exposure to classify the opportunity. | Building an agent where deterministic automation or no automation is safer. |
| Required evidence, authority, or accountable owner is missing | Stop the affected recommendation or commitment and record the gap. | Invented evidence or unauthorised autonomy. |
| Gate evidence is complete and accepted | Advance only within the approved scope and retain the evidence trace. | Scope drift and irreproducible approval. |

## Workflow

1. Confirm the consumer, authority, neighbouring-skill route, and required inputs; stop when a mandatory source or accountable owner is missing.
2. Inspect the evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a failed safety, finance, regulatory, or acceptance gate.
3. Apply the domain method and decision rules within the qualified scope, retaining an evidence trace.
4. Draft the contracted output and reconcile it with methodology, work plan, staffing, pricing, risk, and governance; recover by revising the affected scope or control and rerunning the failed gate.
5. Verify acceptance conditions, permission boundaries, direct references, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

A refund process has fixed rules and no planning need. Route it to workflow automation; reserve agent discovery for exception triage that requires tool use and supervised judgement.

<!-- dual-compat-end -->

## References

- [ai-agent-discovery-question-bank](../../profiles-sectors/references/ai-agent-discovery-question-bank.md) — long-form question bank.
- [ai-agent-metrics-glossary](../../profiles-sectors/references/ai-agent-metrics-glossary.md) — definitions for task-success, intervention, deflection, irreversibility.
- [ai-on-saas-discovery-question-bank](../../profiles-sectors/references/ai-on-saas-discovery-question-bank.md) — AI-on-SaaS discovery base.
- [ai-on-saas-discovery-and-qualification](../../ai-on-saas-proposals/ai-on-saas-discovery-and-qualification/SKILL.md) — AI-on-SaaS discovery skill; load alongside when the agent lives inside a SaaS product.
- [ai-agent-methodology](../ai-agent-methodology/SKILL.md) — methodology that this discovery feeds.
- [ai-agent-business-case-and-roi](../ai-agent-business-case-and-roi/SKILL.md) — business case inputs.
- [ai-agent-risk-and-responsible-ai](../ai-agent-risk-and-responsible-ai/SKILL.md) — agent risk register.
- [ai-agent-poc-and-pilot-scoping](../ai-agent-poc-and-pilot-scoping/SKILL.md) — shadow / supervised / agentic pilot.
- [sales-discovery-and-objection-handling](../../strategy-positioning/sales-discovery-and-objection-handling/SKILL.md) — base discovery discipline.
