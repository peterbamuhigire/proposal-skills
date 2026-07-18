---
name: ai-on-saas-change-management-and-adoption
description: Use when adoption planning must address trust, human oversight, escalation, retraining communications, and workforce concerns for AI features inside multi-tenant SaaS; use the SaaS rollout skill for non-AI operating change.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI-on-SaaS Change Management and Adoption
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The AI-on-SaaS engagement changes how people do work and the proposal must engineer adoption.
- The buyer's workforce is exposed to AI for the first time, or has had a bad AI experience.
- Union, works-council, or regulator-facing AI communications are required.
- The proposal competes against vendors who treat AI adoption as training.

## Do Not Use When

- The engagement is non-AI (use `change-management`).
- The engagement is generic AI strategy with no SaaS users (use `ai-transformation-proposal`).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| Affected user populations per AI feature (counts, roles, locations). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Buyer's communications posture (proactive, reactive, silent). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Union / works-council / staff association presence. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Regulator-facing transparency obligations. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Existing change management forum and sponsor. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Run the base change-management discovery, then layer the **five AI-specific concerns**: model trust, augment-vs-replace framing, escalation paths, HITL design, retraining cadence.
2. Build the **AI Adoption Plan** — for each AI feature, name the affected users, the augment-vs-replace framing, the trust-building activities, the HITL design, the escalation path, the retraining communications, the adoption metric.
3. Draft the **Augment-vs-Replace Communications Brief**: what the buyer will say publicly and internally about whether the AI replaces a role, augments a role, or enables a workflow that did not exist. Honest framing protects adoption.
4. Design **Model Trust-Building Activities**: shadow mode (AI runs but does not act), explain-and-confirm mode (AI suggests, human confirms), supervised auto mode (AI acts on low-stakes flows, escalates on high-stakes), full auto mode (only where eval and HITL design permit).
5. Specify the **HITL Design** for each feature: when does a human review, what is the human's authority, what is the escalation, what is the SLA, who owns the review queue.
6. Specify the **Retraining / Re-Prompting Cadence Communications**: when the model is updated, what users see, what the rollback path is, who signs off.
7. Specify the **Union / Works-Council / Regulator Communications** where applicable: consultation cadence, evidence pack, escalation, redress.
8. Specify the **Adoption Metrics**: feature adoption, abstain-correctness, user trust score, override rate, escalation rate, satisfaction.
9. Output the **AI Adoption Plan** subsection of the proposal's change-management section.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Adoption is engineered, not assumed.
- Augment-vs-replace framing is honest and explicit; no euphemisms.
- Trust-building activities are staged from shadow to auto, not all-at-once.
- HITL design names the human's authority, not just "human review."
- Retraining communications are part of the operating model, not a one-off.
- Union / regulator communications are scoped where applicable.
- Adoption metrics include abstain-correctness and override rate, not just usage counts.

## Anti-Patterns

- "We will train the users on the new AI." **Fix:** Define role-based learning, supervised practice, competence evidence, support ownership, and adoption measures.
- "AI will augment your team" with no role-by-role analysis. **Fix:** Map each affected role's retained judgement, automated tasks, new controls, and redeployment or capability needs.
- HITL described as "human review" with no authority or SLA. **Fix:** Name the reviewer, decision authority, response SLA, escalation path, and evidence captured for each HITL gate.
- Trust-building skipped because "the model is accurate." **Fix:** Measure trust by use case and cohort, publish limitations, and use controlled exposure with feedback and redress.
- Retraining communications skipped because "the model improves silently." **Fix:** Publish model-change notices that state impact, effective date, retesting required, and user support route.
- Union consultation skipped where required. **Fix:** Identify consultation obligations early, name the responsible owner, and gate rollout on documented engagement.
- Adoption metric is "logins per user." **Fix:** Track task completion, accepted outputs, correction rate, escalation rate, time saved, and safe abandonment.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Adoption Plan subsection for `06-methodology` close or standalone change-management section. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Augment-vs-Replace Communications Brief. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Trust-Building Staging Plan (shadow → confirm → supervised → auto). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| HITL Design table per feature. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Retraining Cadence Communications Plan. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Union / Works-Council / Regulator Communications Plan (where applicable). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| AI Adoption Metrics dashboard specification. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## Agent Overlay

For agentic engagements, trust staging is sharper: each stage has **named action-class evidence** (agreement rate in Shadow; confirmation latency and override rate in Confirm; intervention rate and zero irreversibility in Supervised; task-success and contestability cases in Agentic). The augment / replace framing extends to **augment / redeploy / retrain** per role, with a funded six-module supervisor retraining curriculum. An **agent-on-your-behalf disclosure UX** becomes a named deliverable. Adoption metrics add intervention rate, override rate, supervisor CSAT, queue headroom, and contestability case load. Load `../ai-agent-change-management-and-adoption/SKILL.md` for the agent playbook.

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
| Trust barrier | Assign an owner, intervention, adoption measure, and escalation path | Low adoption hidden behind deployment completion |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

Before enabling an AI assistant for all caseworkers, evidence task-specific competence, escalation behaviour, user training, feedback capture, and an owner who can suspend the feature.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/ai-on-saas-change-management-playbook.md](../../profiles-sectors/references/ai-on-saas-change-management-playbook.md) — full playbook.
- [../change-management/SKILL.md](../../domain-delivery/change-management/SKILL.md) — base change management discipline.
- [../ai-on-saas-combined-methodology/SKILL.md](../ai-on-saas-combined-methodology/SKILL.md) — methodology that adoption sits inside.
- [../ai-on-saas-team-composition/SKILL.md](../ai-on-saas-team-composition/SKILL.md) — roles required (AI safety lead, change lead).
- [../monitoring-and-evaluation/SKILL.md](../../domain-delivery/monitoring-and-evaluation/SKILL.md) — adoption metric placement.
- [../stakeholder-engagement/SKILL.md](../../domain-delivery/stakeholder-engagement/SKILL.md) — stakeholder mapping for AI communications.
