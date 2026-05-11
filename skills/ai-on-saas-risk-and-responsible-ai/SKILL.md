---
name: ai-on-saas-risk-and-responsible-ai
description: Use when the AI-on-SaaS proposal must present an AI risk register and a Responsible-AI commitment that survives a CISO, DPO, regulator, and ethics review. Provides the full AI risk register (model risk, hallucination liability, prompt injection, data leakage, sub-processor exposure, regulatory shift, vendor lock-in, training-data contamination, drift, reputational) with triggers, mitigations, owners, and escalation; plus a Responsible-AI commitment section template tied to named regulators.
---

# AI-on-SaaS Risk and Responsible AI
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

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

- The AI use-case inventory.
- The regulator stance and jurisdiction(s).
- The buyer's hallucination tolerance per use case.
- The model-provider posture (single, multi, sovereign).
- The sub-processor list including model providers.
- The buyer's escalation expectations (timing, parties).

## Workflow

1. Populate the **AI Risk Register** from the ten core risks (below) plus engagement-specific entries. Each entry carries: risk name, description, likelihood, impact, trigger, mitigation, owner, escalation.
2. Populate the **Responsible-AI Commitment** section: scope, principles, governance forum, accountable role, eval discipline, transparency commitments, redress mechanism, sign-off frequency.
3. Map the Responsible-AI commitment to the named regulator(s): AI Act (article references where applicable), Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U guidance, Rwanda AI Policy, sectoral rules.
4. Pair every risk with a methodology mitigation in `ai-on-saas-combined-methodology` and a procurement answer in `ai-on-saas-procurement-and-questionnaire`.
5. Output the **Risk Analysis subsection** and the **Responsible-AI Commitment subsection** of the proposal.

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

- "We will follow Responsible AI principles" as the only commitment.
- Risks listed without triggers, owners, or escalation.
- Mitigations promised but not anchored in the methodology.
- Hallucination treated only as a UX disclaimer.
- "Compliance with applicable laws" as the regulator language.
- Responsible-AI lead role unnamed.
- Sub-processor disclosure deferred to a separate document never delivered.

## Outputs

- AI Risk Register (table form) — drop into proposal `12-risk-analysis` or `risk-management`.
- Responsible-AI Commitment subsection — drop into proposal `06-methodology` close or a standalone section.
- Regulator Mapping table.

## Agent Addendum

For agentic engagements, add the twelve agent-specific risks from `../ai-agent-risk-and-responsible-ai/SKILL.md`: autonomy-action incident, irreversibility incident, accountability dispute, scope-creep, multi-agent collusion / failure cascade, prompt-injection via tool output, memory poisoning, regulator action on agentic system, kill-switch failure, identity / impersonation breach, escalation overload, legacy-system damage. The Responsible-AI commitment extends to include **human-final on irreversibility**, **full audit log with 99 % completeness SLA**, **contestability**, **transparency-to-affected-party** (AI Act Article 50-style), and **quarterly kill-switch drill cadence**. The accountable role becomes **Agent Safety Lead**.

## References

- `../references/ai-on-saas-risk-register-for-proposals.md` — full risk register template.
- `../references/ai-on-saas-responsible-ai-commitment.md` — full Responsible-AI commitment template.
- `../references/ai-on-saas-trust-and-compliance-section-template.md` — trust section linkage.
- `../references/ai-on-saas-procurement-questionnaire-pack.md` — procurement answers that match the risk register.
- `../risk-management/SKILL.md` — generic risk register discipline.
- `../ai-on-saas-combined-methodology/SKILL.md` — methodology that anchors the mitigations.
- `../ai-on-saas-compliance-credentials/SKILL.md` — trust and compliance posture for AI-on-SaaS.
- `../ai-on-saas-procurement-and-questionnaire/SKILL.md` — procurement answer pack.
