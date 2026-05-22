---
name: ai-on-saas-change-management-and-adoption
description: Use when the AI-on-SaaS proposal must present change management and adoption specifically for AI features inside a multi-tenant SaaS. Covers AI mindset transition, augment-vs-replace framing, model trust, human-in-the-loop design, escalation paths, retraining cadence communications, and union / works-council / regulator-facing communications. Extends `change-management` with the AI overlay.
---

# AI-on-SaaS Change Management and Adoption
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The AI-on-SaaS engagement changes how people do work and the proposal must engineer adoption.
- The buyer's workforce is exposed to AI for the first time, or has had a bad AI experience.
- Union, works-council, or regulator-facing AI communications are required.
- The proposal competes against vendors who treat AI adoption as training.

## Do Not Use When

- The engagement is non-AI (use `change-management`).
- The engagement is generic AI strategy with no SaaS users (use `ai-transformation-proposal`).

## Required Inputs

- Affected user populations per AI feature (counts, roles, locations).
- Buyer's communications posture (proactive, reactive, silent).
- Union / works-council / staff association presence.
- Regulator-facing transparency obligations.
- Existing change management forum and sponsor.

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

## Quality Standards

- Adoption is engineered, not assumed.
- Augment-vs-replace framing is honest and explicit; no euphemisms.
- Trust-building activities are staged from shadow to auto, not all-at-once.
- HITL design names the human's authority, not just "human review."
- Retraining communications are part of the operating model, not a one-off.
- Union / regulator communications are scoped where applicable.
- Adoption metrics include abstain-correctness and override rate, not just usage counts.

## Anti-Patterns

- "We will train the users on the new AI."
- "AI will augment your team" with no role-by-role analysis.
- HITL described as "human review" with no authority or SLA.
- Trust-building skipped because "the model is accurate."
- Retraining communications skipped because "the model improves silently."
- Union consultation skipped where required.
- Adoption metric is "logins per user."

## Outputs

- AI Adoption Plan subsection for `06-methodology` close or standalone change-management section.
- Augment-vs-Replace Communications Brief.
- Trust-Building Staging Plan (shadow → confirm → supervised → auto).
- HITL Design table per feature.
- Retraining Cadence Communications Plan.
- Union / Works-Council / Regulator Communications Plan (where applicable).
- AI Adoption Metrics dashboard specification.

## Agent Overlay

For agentic engagements, trust staging is sharper: each stage has **named action-class evidence** (agreement rate in Shadow; confirmation latency and override rate in Confirm; intervention rate and zero irreversibility in Supervised; task-success and contestability cases in Agentic). The augment / replace framing extends to **augment / redeploy / retrain** per role, with a funded six-module supervisor retraining curriculum. An **agent-on-your-behalf disclosure UX** becomes a named deliverable. Adoption metrics add intervention rate, override rate, supervisor CSAT, queue headroom, and contestability case load. Load `../ai-agent-change-management-and-adoption/SKILL.md` for the agent playbook.

## References

- `../references/ai-on-saas-change-management-playbook.md` — full playbook.
- `../change-management/SKILL.md` — base change management discipline.
- `../ai-on-saas-combined-methodology/SKILL.md` — methodology that adoption sits inside.
- `../ai-on-saas-team-composition/SKILL.md` — roles required (AI safety lead, change lead).
- `../monitoring-and-evaluation/SKILL.md` — adoption metric placement.
- `../stakeholder-engagement/SKILL.md` — stakeholder mapping for AI communications.
