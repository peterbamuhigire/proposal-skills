---
name: ai-agent-poc-and-pilot-scoping
description: Use when scoping an AI-agent proof of concept or pilot with shadow, supervised, and agentic stages, measurable gates, abort conditions, and production-exit criteria.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent POC and Pilot Scoping
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The buyer wants a pilot or POC before committing to a full agentic build or rollout.
- The agency proposes a paid agent feasibility study before pricing the full engagement.
- The pilot must produce evidence the buyer's CTO, CISO, head of operations, and regulator can act on.
- The buyer has been burned by agent demos that "looked autonomous" but failed on integration, intervention rate, or irreversible incidents.

## Do Not Use When

- The POC is for a non-agent AI feature (use `ai-on-saas-poc-and-pilot-scoping`).
- The POC is for a copilot with no action-taking (use `ai-on-saas-poc-and-pilot-scoping`).

## Domain Inputs

- The candidate agent use case (named workflow, named outcome, named volume).
- The action catalogue v0 with reversibility classification.
- The autonomy-level target per action class.
- The success-metric definition (task-success rate / intervention rate / deflection / time-to-resolution) with floor and ceiling.
- The golden dataset assembly plan or the live-traffic shadow plan.
- The kill-switch architecture and the human operator on call.
- The time-box the buyer accepts (typically 8–16 weeks for agent pilots).

## Domain Method

1. Write the **Agent POC Charter** in one page: one workflow, one outcome, one production decision the pilot enables, one binary go / no-go question. Name the autonomy-level target and the action catalogue.
2. Define the **Three Pilot Stages** in sequence: Shadow, Supervised, Agentic. The pilot transitions between stages only when binary thresholds are met.
3. Define the **Golden Dataset and Shadow Traffic**: size, source, labelling rule, labelling owner, adversarial cases (prompt injection via tool output, scope-edge cases, irreversibility-edge cases, multilingual cases, regulator-sensitive cases). Include **live shadow traffic** where the production environment permits — agents fail in ways the golden set cannot anticipate.
4. Define the **Success Thresholds** for stage transition and production exit:
   - Task-success rate ≥ X on the golden set and on the shadow traffic.
   - Intervention rate ≤ Y on the supervised stage.
   - Irreversible-action ceiling — zero unauthorised irreversible actions; zero scope breaches.
   - Cost-per-task within target at P99 model-call count.
   - Kill-switch drill executed at least twice with sub-N-minute time-to-stop.
   - Red-team pass (prompt injection via tool output, scope manipulation, identity confusion, memory poisoning).
   - Audit-log completeness ≥ 99 % of actions.
5. Define the **Abort Conditions** for each stage with the abort fee and the evidence pack returned to the buyer:
   - Irreversible-action incident at agency fault → abort.
   - Scope breach not detected by the agency → abort.
   - Intervention rate above ceiling for two consecutive weeks at agentic stage → abort or fall back to supervised.
   - Regulator inquiry → joint review with abort option.
6. Define the **Tenant Confinement in POC** even when the buyer wants quick demonstration — agents that share state across tenants in POC produce evidence that cannot transfer.
7. Define the **Time-Box** (8–16 weeks typical, with weekly stand-ups, a mid-pilot gate, and a stage-transition gate).
8. Define the **Exit-to-Production Gate** — all of (a) golden-set thresholds met, (b) shadow-traffic thresholds met, (c) supervised stage intervention rate within ceiling, (d) zero irreversibility incidents, (e) kill-switch drill verified, (f) red-team pass, (g) audit-log completeness verified, (h) regulator / sponsor sign-off where required. Partial pass is a "pilot extension", not a production exit.
9. Write the **Agent POC Proposal Section** (scope, success criteria, exclusions, deliverables, fee, time-box, exit gates, abort conditions, what happens after pass / after fail).

## The Three Agent Pilot Stages

### Stage 1 — Shadow Mode
- The agent runs against real traffic but does **not** act. Every proposed action is logged.
- The human operator processes the case normally. A reviewer compares the agent's proposed action with the human's actual action.
- Success threshold: agreement rate ≥ X on the action level and ≥ Y on the outcome level on N cases.
- Duration: typically two to four weeks at meaningful volume.
- Exit: move to Supervised when agreement is consistent and abstain logic is verified.
- Evidence pack: agreement-rate report, disagreement-class analysis, abstain-correctness report.

### Stage 2 — Supervised Mode
- The agent acts on **reversible** actions only. Irreversible actions are proposed and a named human confirms.
- The oversight queue is live. The intervention SLA is measured.
- Success threshold: task-success rate ≥ X on reversible actions; intervention rate ≤ Y; zero unauthorised irreversible actions.
- Duration: typically four to eight weeks.
- Exit: move to Agentic stage when intervention rate is at ceiling and irreversibility incidents are zero.
- Evidence pack: task-success rate, intervention-rate curve, scope-confinement audit, oversight-queue metrics.

### Stage 3 — Agentic Mode
- The agent acts on reversible actions without confirmation. Irreversible actions still require a human (the agent's autonomy-level commitment).
- Human-on-the-loop: humans monitor metrics, intervene on flagged cases, audit a sample.
- Success threshold: task-success rate ≥ X over a sustained period; intervention rate ≤ Y for at least two consecutive weeks; zero scope breaches; kill-switch drill verified; red-team pass.
- Duration: typically two to four weeks before production exit decision.
- Exit: production exit decision based on the full evidence pack.

## Quality Standards

- One workflow, one outcome, one decision per pilot.
- Success thresholds are numeric and binary; no "agent quality is good".
- The pilot transitions Shadow → Supervised → Agentic; no leapfrog.
- Irreversible actions remain HITL through all three stages.
- Kill-switch drill is executed at least twice and the drill log is shared with the buyer.
- Red-team includes agent-specific attack classes (prompt injection via tool output, scope manipulation, memory poisoning, multi-agent collusion if applicable).
- Tenant confinement is respected even in POC.
- Abort conditions are named with fee and evidence-pack handover.
- Exit gates are all-or-nothing; partial pass triggers a pilot extension or a re-scope.

## Domain Risks

- "Agentic-mode pilot from day one" with no Shadow stage.
- Agreeing to act on irreversible actions in pilot to "make the demo impressive".
- Golden set assembled after the pilot starts.
- Intervention rate not measured because "the supervisor handles it".
- Kill-switch drill skipped because "we will test later".
- Red-team skipped because "we have not seen any attacks".
- Production exit on partial pass because the buyer wants velocity.
- Multi-agent system tested as a black-box without component-level evaluation.
- Pilot stretches indefinitely without an abort condition.

## Domain Outputs

- Agent POC Charter (one page).
- Three-Stage Pilot Plan (Shadow / Supervised / Agentic) with thresholds.
- Golden Dataset Specification.
- Shadow Traffic Specification.
- Success Threshold Table (task-success, intervention, irreversibility, audit completeness, kill-switch drill).
- Action Catalogue v1 with reversibility classification.
- Abort Conditions and Fee Structure.
- Tenant Confinement Note.
- Exit-to-Production Gate Criteria.
- Agent POC Proposal Section.

## Anti-Patterns

- Inventing a metric, credential, constraint, or buyer position. Fix: cite the supplied source or mark the item as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and state the evidence needed to resume.
- Advancing autonomy without a named gate owner. Fix: require observable evidence, accountable acceptance, and a rollback path.
- Reusing another sector or use case without reassessment. Fix: retest affected parties, action scope, reversibility, and jurisdiction.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: define an observable measure, threshold, evidence record, and decision owner.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| qualified use case, action catalogue, baseline, risk limits, pilot users, and production constraints | Buyer evidence, ToR, approved discovery record, system owner, or measured operating data | Yes | Stop the affected decision; list the missing source and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Pilot charter and exit decision | Sponsor, safety lead, and production owner | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| pilot charter and exit decision | Sponsor, safety lead, and production owner | Every load-bearing claim traces to supplied evidence; assumptions, owners, gates, exclusions, and observable acceptance conditions are explicit. |

## Capability Contract

Default to read-only for discovery, analysis, review, and planning. Minimum capability is access to the supplied artefacts and permission to calculate or inspect evidence. Edit only the requested proposal working copy. Do not change production systems, contact affected parties, publish, spend, certify compliance, or approve autonomous action without explicit authority from the accountable owner.

## Degraded Mode

If files, interviews, telemetry, specialist review, network access, or calculation tools are unavailable, produce the narrowest useful qualified result. Mark each unavailable check as not assessed, separate facts from assumptions, lower confidence, and state the evidence needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Advance, hold, abort, or exit | Use pre-agreed task success, intervention, irreversible-action, confinement, and kill-switch gates. | A pilot drifting into production without evidence. |
| Required evidence, authority, or accountable owner is missing | Stop the affected recommendation or commitment and record the gap. | Invented evidence or unauthorised autonomy. |
| Gate evidence is complete and accepted | Advance only within the approved scope and retain the evidence trace. | Scope drift and irreproducible approval. |

## Workflow

1. Confirm the consumer, authority, neighbouring-skill route, and required inputs; stop when a mandatory source or accountable owner is missing.
2. Inspect the evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a failed safety, finance, regulatory, or acceptance gate.
3. Apply the domain method and decision rules within the qualified scope, retaining an evidence trace.
4. Draft the contracted output and reconcile it with methodology, work plan, staffing, pricing, risk, and governance; recover by revising the affected scope or control and rerunning the failed gate.
5. Verify acceptance conditions, permission boundaries, direct references, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

A support agent completes shadow evaluation but exceeds the intervention ceiling. Hold it in shadow mode, diagnose the error cohort, and rerun the gate rather than averaging the failure away.

<!-- dual-compat-end -->

## References

- [ai-agent-poc-scoping-template](../../profiles-sectors/references/ai-agent-poc-scoping-template.md) — full template with worked examples.
- [ai-agent-metrics-glossary](../../profiles-sectors/references/ai-agent-metrics-glossary.md) — task-success, intervention, irreversibility, scope-confinement, audit completeness definitions.
- [ai-on-saas-poc-scoping-template](../../profiles-sectors/references/ai-on-saas-poc-scoping-template.md) — AI-on-SaaS POC base.
- [ai-on-saas-poc-and-pilot-scoping](../../ai-on-saas-proposals/ai-on-saas-poc-and-pilot-scoping/SKILL.md) — AI-on-SaaS POC skill (load when the agent lives inside a SaaS product).
- [ai-agent-methodology](../ai-agent-methodology/SKILL.md) — production methodology after pilot pass.
- [ai-agent-discovery-and-qualification](../ai-agent-discovery-and-qualification/SKILL.md) — discovery that scopes the pilot.
- [ai-agent-risk-and-responsible-ai](../ai-agent-risk-and-responsible-ai/SKILL.md) — risk register entries.
- [saas-poc-and-pilot-scoping](../../saas-proposals/saas-poc-and-pilot-scoping/SKILL.md) — base SaaS POC discipline.
