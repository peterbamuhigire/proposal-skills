---
name: ai-on-saas-risk-and-responsible-ai
description: Use when an AI-on-SaaS proposal needs an owned AI risk register and auditable Responsible-AI commitment for CISO, DPO, ethics, or regulator review; use generic risk management when the engagement contains no AI.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI-on-SaaS Risk and Responsible AI
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The proposal must present an AI risk register inside the Risk Analysis section.
- The buyer's CISO, DPO, or ethics committee will review the proposal.
- The bid is in a regulated vertical (financial services, insurance, healthcare, public sector, education).
- The bid is in an AI-Act-relevant jurisdiction (EU export bids) or a domestic AI-guidance jurisdiction (Kenya, Nigeria, South Africa, Uganda, Rwanda).
- The agency must demonstrate Responsible-AI practice, not promise it.

## Do Not Use When

- The engagement is non-AI (use `risk-management`).
- The engagement is generic AI strategy with no SaaS layer (use `ai-transformation-proposal`).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The AI use-case inventory. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The regulator stance and jurisdiction(s). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's hallucination tolerance per use case. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The model-provider posture (single, multi, sovereign). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The sub-processor list including model providers. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's escalation expectations (timing, parties). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Populate the **AI Risk Register** from the ten core risks (below) plus engagement-specific entries. Each entry carries: risk name, description, likelihood, impact, trigger, mitigation, owner, escalation.
2. Populate the **Responsible-AI Commitment** section: scope, principles, governance forum, accountable role, eval discipline, transparency commitments, redress mechanism, sign-off frequency.
3. Map the Responsible-AI commitment to the named regulator(s): AI Act (article references where applicable), Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U guidance, Rwanda AI Policy, sectoral rules.
4. Pair every risk with a methodology mitigation in `ai-on-saas-combined-methodology` and a procurement answer in `ai-on-saas-procurement-and-questionnaire`.
5. Output the **Risk Analysis subsection** and the **Responsible-AI Commitment subsection** of the proposal.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## The Ten Core AI Risks

| # | Risk | Trigger | Primary Mitigation |
|---|---|---|---|
| 1 | Model risk (wrong, biased, unstable output) | Eval drop below threshold; user complaint cluster | Eval harness in CI, drift watch, model rollback, abstain logic |
| 2 | Hallucination liability | Untrue output causes user / customer harm | Hallucination ceiling, abstain logic, citation grounding, HITL on high-stakes flows, professional indemnity |
| 3 | Prompt injection | User or document injects adversarial instruction | Input / output filtering, system-prompt hardening, tool-call allowlist, red-team harness |
| 4 | Data leakage into model providers | Customer data sent to model and retained / trained on | Training-data exclusion clause, retention controls, region routing, sub-processor disclosure |
| 5 | Sub-processor exposure | Model provider breach, model provider banned, model provider price shock | Multi-provider gateway, fallback model, contractual notice, exit plan |
| 6 | Regulatory shift | AI Act tier change, sectoral rule, ban in market | Quarterly regulator scan, conformity readiness, regional fallback, kill-switch |
| 7 | Vendor lock-in to single model family | Model deprecation, price increase, ban | Model-agnostic gateway, open-weight fallback, eval portability |
| 8 | Training-data contamination | Training data includes prohibited / licensed / poisoned content | Data lineage, licence audit, content filtering, retraining triggers |
| 9 | Drift (eval, performance, cost) | Production behaviour drifts from POC | Drift watch dashboards, monthly eval refresh, cost-per-call SLO, alerting |
| 10 | Reputational | Public AI incident, regulator action, employee or union pushback | Responsible-AI commitment, transparency commitments, incident communications, redress mechanism |

## Responsible-AI Commitment — Section Structure

1. **Scope** — which AI features the commitment covers; what is in and out of scope.
2. **Principles** — accountability, transparency, fairness, safety, privacy, human oversight, redress.
3. **Governance forum** — who meets, how often, what they decide; agency-side and buyer-side roles.
4. **Accountable role** — a named role (AI Safety Lead) accountable for the commitment, with escalation to the SteerCo.
5. **Eval discipline** — golden datasets, thresholds, refresh cadence, regression harness, drift watch.
6. **Transparency commitments** — model cards published or available, sub-processor list public, eval methodology described, incident disclosure policy.
7. **Redress mechanism** — how an affected user, tenant, employee, or regulator raises a concern; SLA for response; named owner.
8. **Sign-off frequency** — quarterly review by the governance forum; annual sign-off by the SteerCo.

## Quality Standards

- Every risk has likelihood, impact, trigger, mitigation, owner, escalation.
- Mitigations are anchored in the methodology, not invented for the proposal.
- Responsible-AI commitment is a section, not a sentence; it has a named accountable role.
- Regulator references are specific (article, paragraph, guideline name), not "applicable laws."
- The risk register and the commitment cross-reference each other.
- The commitment is auditable — the buyer's auditor can verify the eval discipline, the sub-processor list, the redress log.

## Anti-Patterns

- "We will follow Responsible AI principles" as the only commitment. **Fix:** Replace the slogan with a scoped commitment naming accountable lead, governance, evaluation, transparency, redress, and sign-off.
- Risks listed without triggers, owners, or escalation. **Fix:** Give every risk a trigger, likelihood, impact, mitigation, owner, escalation route, and acceptance evidence.
- Mitigations promised but not anchored in the methodology. **Fix:** Cross-reference each mitigation to a funded methodology activity, deliverable, gate, test, and responsible role.
- Hallucination treated only as a UX disclaimer. **Fix:** Control hallucination with grounding, thresholds, abstention, human approval, monitoring, incident handling, and redress.
- "Compliance with applicable laws" as the regulator language. **Fix:** Name the jurisdiction, instrument or guidance, applicability, current source, compliance action, and reviewer.
- Responsible-AI lead role unnamed. **Fix:** Appoint an AI Safety Lead with decision rights, escalation authority, reporting cadence, and named deputy.
- Sub-processor disclosure deferred to a separate document never delivered. **Fix:** Deliver a versioned sub-processor register with purpose, data classes, regions, terms, notice process, and exit route.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Risk Register (table form) — drop into proposal `12-risk-analysis` or `risk-management`. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Responsible-AI Commitment subsection — drop into proposal `06-methodology` close or a standalone section. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Regulator Mapping table. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## Agent Addendum

For agentic engagements, add the twelve agent-specific risks from `../ai-agent-risk-and-responsible-ai/SKILL.md`: autonomy-action incident, irreversibility incident, accountability dispute, scope-creep, multi-agent collusion / failure cascade, prompt-injection via tool output, memory poisoning, regulator action on agentic system, kill-switch failure, identity / impersonation breach, escalation overload, legacy-system damage. The Responsible-AI commitment extends to include **human-final on irreversibility**, **full audit log with 99 % completeness SLA**, **contestability**, **transparency-to-affected-party** (AI Act Article 50-style), and **quarterly kill-switch drill cadence**. The accountable role becomes **Agent Safety Lead**.

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
| High-consequence use case | Require human oversight, abstention, monitoring, and named escalation | Uncontrolled harm or unowned AI incident |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

For a benefits-advice assistant, record harms from incorrect eligibility guidance, require grounded responses and human escalation, define a stop threshold, and name the safety owner before live use.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/ai-on-saas-risk-register-for-proposals.md](../../profiles-sectors/references/ai-on-saas-risk-register-for-proposals.md) — full risk register template.
- [../references/ai-on-saas-responsible-ai-commitment.md](../../profiles-sectors/references/ai-on-saas-responsible-ai-commitment.md) — full Responsible-AI commitment template.
- [../references/ai-on-saas-trust-and-compliance-section-template.md](../../profiles-sectors/references/ai-on-saas-trust-and-compliance-section-template.md) — trust section linkage.
- [../references/ai-on-saas-procurement-questionnaire-pack.md](../../profiles-sectors/references/ai-on-saas-procurement-questionnaire-pack.md) — procurement answers that match the risk register.
- [../risk-management/SKILL.md](../../domain-delivery/risk-management/SKILL.md) — generic risk register discipline.
- [../ai-on-saas-combined-methodology/SKILL.md](../ai-on-saas-combined-methodology/SKILL.md) — methodology that anchors the mitigations.
- [../ai-on-saas-compliance-credentials/SKILL.md](../ai-on-saas-compliance-credentials/SKILL.md) — trust and compliance posture for AI-on-SaaS.
- [../ai-on-saas-procurement-and-questionnaire/SKILL.md](../ai-on-saas-procurement-and-questionnaire/SKILL.md) — procurement answer pack.
