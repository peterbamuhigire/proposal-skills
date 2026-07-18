---
name: ai-agent-compliance-credentials
description: Use when presenting verified agent-specific trust and compliance credentials, including action logs, irreversibility gates, kill-switch drills, identity controls, and scope attestations.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent Compliance Credentials
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The proposal includes a Trust and Compliance section and the engagement involves agentic systems.
- The buyer's procurement, CISO, DPO, or general counsel will score the agentic compliance posture.
- The bid is in a regulated vertical or an AI-Act-relevant market.
- The competitive set includes vendors who present generic AI trust pages with no agentic specifics.
- The buyer or their regulator has signalled concern about agentic systems, autonomous decisioning, or AI taking actions.

## Do Not Use When

- The engagement is non-agent (use `ai-on-saas-compliance-credentials` or `saas-trust-and-compliance-credentials-section`).

## Domain Inputs

- The Trust and Compliance posture from the AI-on-SaaS or SaaS skill.
- The action catalogue with reversibility classification.
- The autonomy-level commitment per action class.
- The kill-switch architecture and drill evidence.
- The intervention SLO and the audit-log completeness SLA.
- The red-team catalogue specific to agents.
- The agent identity and impersonation policy.
- The transparency-to-affected-party posture per jurisdiction.

## Domain Method

1. Open with the **Agentic Trust Posture** paragraph: the agency operates agents under an explicit action catalogue, with reversibility classification, with autonomy levels committed per action class, with kill-switch authority named, with audit completeness measured, under a Responsible-AI agent commitment with a named accountable role.
2. Populate the **Agentic Compliance Map** — for each regulator and standard the bid touches, state the agency's posture (ready, in-progress, not-in-scope) with evidence references:
   - EU AI Act (high-risk articles where the agent decisions affect rights or safety; transparency Article 50; post-market monitoring).
   - Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U guidance, Rwanda AI Policy.
   - GDPR / POPIA / Kenya DPA / Nigeria NDPA / Uganda DPPA / Rwanda DPL — automated decision-making and data-subject rights.
   - ISO 42001 (AI management system) and ISO 23894 (AI risk).
   - NIST AI RMF — Govern, Map, Measure, Manage.
   - Sectoral — FS model-risk management (SR 11-7-style), healthcare admin / clinical separation, legal-practice bar rules, public-sector administrative-law fairness.
3. Populate the **Action Audit Log Practice** subsection — what is logged (decision, tool call, parameters, result, human decision), retention period, completeness SLA, audit access for buyer / auditor / regulator, replay capability.
4. Populate the **Irreversibility Gating** subsection — reversibility classification, L1 gating on irreversible actions, named human approver per class, value-bound transaction confirmation, dry-run pattern where applicable.
5. Populate the **Intervention SLO** subsection — definition, target, measurement, alerting, review cadence.
6. Populate the **Kill-Switch Architecture and Drill** subsection — kill-switch layers (per-action, per-agent, per-tenant, global), named authority, drill cadence (quarterly minimum), drill log availability.
7. Populate the **Agent Red-Team Catalogue** subsection — attack classes (prompt injection via tool output, scope manipulation, identity confusion, memory poisoning, multi-agent collusion, side-channel leakage), frequency, scope, scorecard, remediation cadence.
8. Populate the **Agent Identity and Impersonation Policy** subsection — agent identity model (own / service / delegated), external-communication disclosure, signature on outgoing communications, regulator-aligned transparency.
9. Populate the **Action-Scope Attestation** subsection — every agent has a published action-scope attestation listing the actions it can take, the systems it can touch, the limits; auditor-verifiable.
10. Populate the **Multi-Agent Governance** subsection (where applicable) — orchestrator-level governance, inter-agent contract, blast-radius limit, anti-collusion guard, replay determinism.
11. Populate the **Transparency-to-Affected-Party** subsection — when and how affected parties are informed; reference to applicable rules (AI Act Article 50; sectoral fairness rules).
12. Populate the **Sub-Processor Disclosure for Tool Calls and Models** — model providers, tool-call APIs, retention defaults, training-data posture, region routing, fallback.
13. Populate the **Sovereign-AI / On-Prem Option** subsection — when sovereign deployment is offered; architecture; SLA; pricing differential.
14. Output the **Trust and Compliance for Agents** subsection to drop into the proposal's main Trust and Compliance section.

## Quality Standards

- The compliance map names regulators and standards specifically, not "applicable laws".
- Posture per regulator is one of ready / in-progress / not-in-scope, with evidence reference for ready and a target date for in-progress.
- Action audit log practice describes content, retention, completeness SLA, and access — not "we log everything".
- Irreversibility gating is explicit by action class.
- Intervention SLO is a number with a measurement method.
- Kill-switch drill cadence is named (quarterly minimum) and the drill log is available.
- Red-team catalogue is agent-specific, not generic.
- Identity policy is committed; external communications are disclosed.
- Action-scope attestation is published per agent.
- Multi-agent governance subsection exists where the engagement involves multiple agents.
- Transparency-to-affected-party references applicable rule.
- Sub-processor disclosure names tool-call APIs as well as model providers.

## Domain Risks

- "We comply with all applicable AI laws".
- "Agents are audit-logged" with no completeness SLA.
- Irreversibility addressed only in a footnote.
- Intervention SLO as a target without measurement.
- Kill-switch named without drill evidence.
- Red-team described in generic AI terms.
- Identity policy missing — external communications appear human-authored.
- "Multi-agent governance handled at runtime" with no architecture.
- Transparency-to-affected-party deferred to a future review.
- Sub-processor list omits tool-call APIs.

## Domain Outputs

- Agentic Trust Posture paragraph.
- Agentic Compliance Map table.
- Action Audit Log Practice subsection.
- Irreversibility Gating subsection.
- Intervention SLO subsection.
- Kill-Switch Architecture and Drill subsection.
- Agent Red-Team Catalogue subsection.
- Agent Identity and Impersonation Policy subsection.
- Action-Scope Attestation subsection.
- Multi-Agent Governance subsection (where applicable).
- Transparency-to-Affected-Party subsection.
- Sub-Processor Disclosure (models + tool-call APIs).
- Sovereign-AI / On-Prem Option subsection.

## Anti-Patterns

- Inventing a metric, credential, constraint, or buyer position. Fix: cite the supplied source or mark the item as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and state the evidence needed to resume.
- Advancing autonomy without a named gate owner. Fix: require observable evidence, accountable acceptance, and a rollback path.
- Reusing another sector or use case without reassessment. Fix: retest affected parties, action scope, reversibility, and jurisdiction.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: define an observable measure, threshold, evidence record, and decision owner.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| credential register, control evidence, action catalogue, and jurisdiction | Buyer evidence, ToR, approved discovery record, system owner, or measured operating data | Yes | Stop the affected decision; list the missing source and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Verified agent trust-and-compliance section | CISO, DPO, legal counsel, and evaluator | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| verified agent trust-and-compliance section | CISO, DPO, legal counsel, and evaluator | Every load-bearing claim traces to supplied evidence; assumptions, owners, gates, exclusions, and observable acceptance conditions are explicit. |

## Capability Contract

Default to read-only for discovery, analysis, review, and planning. Minimum capability is access to the supplied artefacts and permission to calculate or inspect evidence. Edit only the requested proposal working copy. Do not change production systems, contact affected parties, publish, spend, certify compliance, or approve autonomous action without explicit authority from the accountable owner.

## Degraded Mode

If files, interviews, telemetry, specialist review, network access, or calculation tools are unavailable, produce the narrowest useful qualified result. Mark each unavailable check as not assessed, separate facts from assumptions, lower confidence, and state the evidence needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| State or omit a credential claim | Publish only current, scoped evidence tied to the proposed system and entity. | Misrepresentation or scope ambiguity. |
| Required evidence, authority, or accountable owner is missing | Stop the affected recommendation or commitment and record the gap. | Invented evidence or unauthorised autonomy. |
| Gate evidence is complete and accepted | Advance only within the approved scope and retain the evidence trace. | Scope drift and irreproducible approval. |

## Workflow

1. Confirm the consumer, authority, neighbouring-skill route, and required inputs; stop when a mandatory source or accountable owner is missing.
2. Inspect the evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a failed safety, finance, regulatory, or acceptance gate.
3. Apply the domain method and decision rules within the qualified scope, retaining an evidence trace.
4. Draft the contracted output and reconcile it with methodology, work plan, staffing, pricing, risk, and governance; recover by revising the affected scope or control and rerunning the failed gate.
5. Verify acceptance conditions, permission boundaries, direct references, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

The supplier has a current audit report covering its platform but not the buyer-specific tools. State the platform scope, list buyer-specific controls as planned, and attach only approved evidence.

<!-- dual-compat-end -->

## References

- [ai-agent-trust-and-compliance-template](../../profiles-sectors/references/ai-agent-trust-and-compliance-template.md) — full template.
- [ai-agent-procurement-questionnaire-pack](../../profiles-sectors/references/ai-agent-procurement-questionnaire-pack.md) — questionnaire answers consistent with these credentials.
- [ai-agent-responsible-ai-commitment](../../profiles-sectors/references/ai-agent-responsible-ai-commitment.md) — commitment that this section makes visible.
- [ai-on-saas-trust-and-compliance-section-template](../../profiles-sectors/references/ai-on-saas-trust-and-compliance-section-template.md) — AI-on-SaaS trust base.
- [ai-on-saas-compliance-credentials](../../ai-on-saas-proposals/ai-on-saas-compliance-credentials/SKILL.md) — load alongside for SaaS-embedded agents.
- [ai-agent-risk-and-responsible-ai](../ai-agent-risk-and-responsible-ai/SKILL.md) — risk register and commitment.
- [ai-agent-procurement-and-questionnaire](../ai-agent-procurement-and-questionnaire/SKILL.md) — procurement answers.
