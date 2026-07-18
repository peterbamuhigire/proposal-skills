---
name: customer-service-and-maintenance-proposals
description: Use when writing proposals for post-launch support, maintenance, SLAs, help desk, managed services, customer success, incident response, complaint handling, website care, software support, AI operations, or implementation support.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Customer Service and Maintenance Proposals
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The scope includes maintenance, support, warranty, help desk, hosting, monitoring, updates, training, or post-launch optimisation.
- The client needs confidence in issue handling, escalation, service commitments, and continuity.
- A software, website, SaaS, AI, or digital service proposal must explain what happens after go-live.
- The proposal needs professional language for response times, handoffs, follow-up, complaint recovery, or incident communication.

## Domain Method

1. Define the support model: coverage hours, channels, response targets, resolution targets, severity levels, and excluded work.
2. Separate warranty, corrective maintenance, adaptive maintenance, enhancement work, hosting, licences, and client-side responsibilities.
3. Explain the escalation path: first response, diagnosis, expert review, client update, fix, verification, and closure.
4. Add service communication commitments: acknowledge quickly, explain what is known, give a next update time, and keep records.
5. Include maintenance activities: backups, monitoring, security updates, content fixes, dependency updates, model/prompt review, analytics review, and improvement backlog.
6. Price support explicitly so it does not become an unfunded promise.

## Quality Standards

- Support language must be specific enough to manage expectations and prevent scope creep.
- Do not promise 24/7 or near-immediate support unless staffing and pricing support it.
- Include client obligations: timely feedback, access, content ownership, approvals, and third-party account control.
- Incident and complaint language must be calm, transparent, and action-oriented.

## Existing Deliverables

- Support and maintenance methodology.
- SLA and escalation language.
- Post-launch optimisation scope.
- Maintenance pricing assumptions.

## SaaS Lens

For SaaS implementation engagements, support and maintenance is part of a broader Customer Success and Adoption engagement that distinguishes premium SaaS bids:

- **Support** handles tickets, incidents, and severity-based response. Tier-appropriate SLA (Starter / Pro / Enterprise) with credit mechanisms.
- **Customer Success** owns adoption, value realisation, expansion, and renewal posture. CSM-led, with QBR cadence and named save plays for predictable churn signals.
- **Lifecycle Communications** is the operational backbone of customer success: acquisition, activation, engagement, expansion, retention, advocacy programs.
- **Health Scoring** drives proactive engagement: composite score (usage, adoption breadth, support sentiment, sponsor stability, renewal posture, expansion progress) with Red/Amber/Green response actions.
- **Save Plays** for the predictable churn signals: sponsor change, active-user drop, support spike, QBR dissatisfaction, stalled renewal.

## AI-Agent Lens

When the engagement delivers an AI agent that operates after go-live, the support, SLA, and maintenance commitments take an agent-specific shape that the generic SaaS SLA does not capture:

- **Four-metric SLA** — availability, task-success, intervention rate, time-to-resolve, against a Bronze / Silver / Gold / Platinum class table. Single-metric uptime is not sufficient.
- **Three operational guardrails** — kill-switch SLA (time-to-stop), audit-log completeness SLA (with retention and replay), intervention SLA (time-to-human escalation). These remain in force during model-provider force-majeure.
- **Credit schedule** per metric, with aggregate Service-Credit Cap by class (10 / 25 / 50 / 100 %).
- **Intervention Credit Clause** on Unit Fees — buyer does not pay full price when intervention rate exceeds the ceiling. Customer-facing monthly statement shows the credit applied with evidence-link to the Audit Log.
- **Abort-and-Refund** triggers — Irreversible-Action Incident at agency fault, Intervention overshoot 60 days, Regulator Action, Model-provider sustained outage, Audit-Log Breach. Pro-rata refund of unused subscription.
- **Maintenance scope specific to agents** — eval and red-team cadence, drift watch, supervisor retraining, kill-switch drills (quarterly minimum), prompt regression in CI, model-routing posture and fallback, sub-processor change-notification, action catalogue change-control.
- **Vertical SLA variants** — financial services (regulator-aware, customer-detriment SLA), public sector (no outcome pricing on citizens, sovereign-AI default), healthcare (no autonomous clinical decision, admin-only).

Use [ai-agent-sla-and-credit-schedule](../../ai-agent-commercial/ai-agent-sla-and-credit-schedule/SKILL.md) to commit the SLA class; [ai-agent-intervention-credit-and-abort-refund](../../ai-agent-commercial/ai-agent-intervention-credit-and-abort-refund/SKILL.md) for the intervention credit and abort mechanics; [ai-agent-msa-and-sla-addendum-templates](../../ai-agent-commercial/ai-agent-msa-and-sla-addendum-templates/SKILL.md) for the MSA addendum.

## Do Not Use When

- Do not use this skill when a neighbouring specialist named in the description owns the primary decision; route there first and use this skill only as a supporting layer.
- Do not use it to invent buyer facts, evidence, legal positions, statutory rules, delivery capacity, or current external claims.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| service scope, user base, operating hours, incident history, dependencies, and support authority | Buyer, ToR, approved project record, accountable owner, or verified evidence source | Yes | Stop the affected decision, name the missing source, and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| support model, SLA, escalation matrix, and maintenance plan | Service owner, evaluator, and operations team | Claims trace to supplied evidence; assumptions, owners, exclusions, decisions, and observable acceptance tests are explicit. |

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
| Select support tier and commitments | Match service criticality, staffing, telemetry, exclusions, and remedy affordability. | An SLA the delivery team cannot measure or staff. |
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

A public portal needs weekend coverage but not 24-hour resolution. Define priority classes, weekend response, escalation ownership, maintenance windows, and evidence for monthly review.

<!-- dual-compat-end -->

## References

- [website-software-maintenance-support-language](../../profiles-sectors/references/website-software-maintenance-support-language.md) - proposal-ready support and maintenance language.
- [ai-agent-sla-class-table](../../profiles-sectors/references/ai-agent-sla-class-table.md) - agent SLA class and credit schedule.
- [ai-agent-sla-exhibit-template](../../profiles-sectors/references/ai-agent-sla-exhibit-template.md) - drop-in agent SLA exhibit.
- [ai-agent-credit-and-refund-clauses](../../profiles-sectors/references/ai-agent-credit-and-refund-clauses.md) - agent credit and refund clauses.
- [ai-agent-sla-and-credit-schedule](../../ai-agent-commercial/ai-agent-sla-and-credit-schedule/SKILL.md) - agent SLA skill.
- [ai-agent-intervention-credit-and-abort-refund](../../ai-agent-commercial/ai-agent-intervention-credit-and-abort-refund/SKILL.md) - intervention credit and abort.
- [ai-agent-msa-and-sla-addendum-templates](../../ai-agent-commercial/ai-agent-msa-and-sla-addendum-templates/SKILL.md) - MSA addendum.
- [customer-service-and-escalation-commitments](../../profiles-sectors/references/customer-service-and-escalation-commitments.md) - escalation, complaint handling, warm handoff, and follow-up commitments.
- [saas-customer-success-engagement-package](../../profiles-sectors/references/saas-customer-success-engagement-package.md) - SaaS customer success engagement scope: onboarding, activation, success plan, QBR, expansion, save plays, health scoring.
- [saas-lifecycle-email-program-proposal-template](../../profiles-sectors/references/saas-lifecycle-email-program-proposal-template.md) - lifecycle communications backbone.
- [saas-msa-dpa-sla-template-language](../../profiles-sectors/references/saas-msa-dpa-sla-template-language.md) - SLA, severity, credits, exit clauses.
- [website-design-proposal-strategy](../website-design-proposal-strategy/SKILL.md) - website launch, handover, and support context.
- [ai-transformation-proposal](../ai-transformation-proposal/SKILL.md) - AI monitoring, evaluation refresh, and operational support context.
- [saas-customer-success-and-adoption-proposal](../../saas-proposals/saas-customer-success-and-adoption-proposal/SKILL.md) - SaaS customer success skill.
- [saas-lifecycle-communications-as-deliverable](../../saas-proposals/saas-lifecycle-communications-as-deliverable/SKILL.md) - lifecycle communications skill.
