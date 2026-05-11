# AI-on-SaaS Change Management Playbook

Playbook for adoption, model-trust, HITL design, augment-vs-replace framing, and union / regulator communications for AI features inside a multi-tenant SaaS. Pairs with `ai-on-saas-change-management-and-adoption`. Extends `change-management/SKILL.md`.

## The Five AI-Specific Adoption Concerns

### 1. Model Trust
Users do not trust a model they have not seen behave. Trust is built by staging the AI's authority — not by training videos.

**Staging ladder:**
1. **Shadow** — the AI runs on every case but does not act and is not visible to the user. Outputs compared to the human's outputs to verify the eval before exposure.
2. **Confirm** — the AI suggests, the human reviews and confirms before action. UI highlights citations and abstain decisions.
3. **Supervised auto** — the AI acts on low-stakes flows. Human reviews queues of post-action samples and any flagged escalation.
4. **Full auto** — the AI acts without per-case human review, only available where eval supports it and HITL design permits.

Most AI-on-SaaS engagements ship at level 2 or 3. Level 4 is reserved for genuinely low-stakes flows with reliable abstain logic.

### 2. Augment-vs-Replace Framing
Honest framing is the single biggest adoption variable. Three options:

- **Augment** — AI supports a human; the human's authority is unchanged.
- **Replace step** — AI replaces a specific step (not the role); the human's broader role continues.
- **Enable** — AI enables a workflow that did not exist (e.g. proactive outreach a small team could not do manually).

The framing is **agreed on the buyer side** before user communications. The framing is **honest** — sugar-coated "augment" framing when the intent is "replace" breaks trust irreversibly.

### 3. Escalation Paths
For every AI feature, name the escalation:
- **From the AI** — when does the AI abstain and route to a human?
- **From the user** — when can the user override the AI? With what authority?
- **From the human reviewer** — when does the reviewer escalate to a senior?
- **From the system** — when does an anomaly trigger AI Governance Forum review?

### 4. Human-in-the-Loop Design
HITL is not "a human reviews." HITL is:
- Which human (named role).
- What authority (approve, decline, modify).
- What SLA (response time).
- What queue (priority, volume control).
- What audit (review log, post-decision audit).
- What escalation (when does this go higher).

### 5. Retraining / Re-Prompting Cadence Communications
Users see the AI's behaviour change over time. Communicate ahead:
- When models / prompts are updated (cadence).
- What users will see change (or what should remain unchanged).
- What the rollback path is.
- Who signed off.

## The Three Audience Groups

### Internal Users (the people the AI affects daily)
- Pre-launch: shadow demos; trust-building sessions; "what changes, what stays" briefings.
- Launch: in-app walkthrough; office hours; named human escalation channel.
- Post-launch: weekly digest of model behaviour changes; quarterly forum.

### Leadership and Sponsors
- Pre-launch: business-case readout; risk register walkthrough; Responsible-AI commitment briefing.
- Launch: SteerCo readout; KPI dashboard with adoption, override rate, abstain-correctness, escalation rate.
- Post-launch: quarterly Responsible-AI report signed; annual board-level declaration.

### External Audiences (union, works-council, regulator, customers, public)
- Pre-launch: consultation per the obligation; evidence pack; transparency document.
- Launch: public-facing communication if material; regulator notification if required.
- Post-launch: ongoing transparency commitments per the Responsible-AI commitment.

## Sample Augment-vs-Replace Communications Brief

**Use case**: RM copilot drafts the first response to a customer enquiry.

**Honest framing**: "The copilot drafts the first version of every response. The RM reviews, edits, and sends. The RM remains the author of record, retains full discretion, and may discard the draft. The copilot does not approve responses, does not send responses, and does not score RMs. RMs retain authority over their queues."

**Adoption metrics published**: average draft acceptance rate (target ≥ 60 %); average edit distance; override-with-rejection rate; RM-reported time saved per case.

**Honest tone**: "Some drafts are wrong. The RM is the safeguard. The copilot's value is speed in the median case, not perfection in every case."

## Sample HITL Design — High-Stakes Decisioning

**Use case**: AI-assisted KYC document review producing a recommended decision.

| Element | Specification |
|---|---|
| AI authority | Recommend only. Cannot approve or decline. |
| Human authority | Final approve / decline; modify the AI's reasoning record. |
| Human role | Trained KYC officer (named, certified). |
| SLA | First review within 4 business hours; second-line escalation within 1 business day. |
| Queue | Prioritised by risk score; volume capped at officer capacity. |
| Audit | Decision log retained 7 years; periodic independent sample audit by compliance. |
| Escalation | Risk score above threshold or AI-officer disagreement triggers second-line review. |

## Adoption Metric Dashboard — Specification

| Metric | Definition | Healthy range |
|---|---|---|
| Feature adoption | Active users on the feature ÷ eligible users | ≥ 60 % week 8 |
| Override rate | Cases where the user overrides the AI | 5–25 % healthy; lower may indicate trust issue or rubber-stamping |
| Abstain-correctness in production | Should-abstain cases where the system abstained | ≥ 0.95 |
| Hallucination rate | Per `ai-on-saas-metrics-glossary.md` | At or below ceiling |
| Escalation rate | Cases escalated to second-line / SteerCo | < 2 % steady-state |
| User trust score | Survey: "I trust the AI's draft for this workflow" | Trend up; baseline measured pre-launch |
| Redress events | Affected-party complaints logged | Trend stable or down; quarterly review |

## Union, Works-Council, and Regulator Communications

Where applicable:
- **Union / works-council**: written consultation paper covering scope, augment-vs-replace framing, headcount impact, training, redress, monitoring.
- **Regulator**: pre-launch notification where required (AI Act high-risk; sectoral); evidence pack ready (DPIA, model cards, Responsible-AI commitment).
- **Public**: customer-facing transparency document for high-impact features.

## Anti-Patterns

- "Training" treated as the adoption strategy.
- "AI augments your team" with no role-by-role honest framing.
- HITL described as "human review" with no authority, SLA, or queue.
- Retraining shipped silently because "the model improves."
- Adoption metric is logins-per-user.
- Override rate ignored or framed only as "people resisting AI."
- Union consultation skipped where required.

## Cross-References

- `change-management/SKILL.md` — base change management discipline.
- `ai-on-saas-methodology-blocks.md` — methodology that adoption sits inside.
- `ai-on-saas-team-composition-template.md` — AI Change Lead role.
- `ai-on-saas-responsible-ai-commitment.md` — commitment that adoption supports.
- `ai-on-saas-metrics-glossary.md` — metric definitions.
- `stakeholder-engagement/SKILL.md` — stakeholder mapping.
