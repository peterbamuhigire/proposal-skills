---
name: ai-agent-compliance-credentials
description: Use when the AI-agent proposal must showcase Trust and Compliance credentials specific to agentic systems. Provides the Trust-and-Compliance-for-Agents subsection template covering action audit log, irreversibility gating, intervention SLO, kill-switch architecture and drill evidence, agent red-team catalogue, agent identity and impersonation policy, action-scope attestation, multi-agent governance evidence, transparency-to-affected-party posture, and sovereign-AI options. Extends `ai-on-saas-compliance-credentials` with the agent overlay.
---

# AI-Agent Compliance Credentials
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The proposal includes a Trust and Compliance section and the engagement involves agentic systems.
- The buyer's procurement, CISO, DPO, or general counsel will score the agentic compliance posture.
- The bid is in a regulated vertical or an AI-Act-relevant market.
- The competitive set includes vendors who present generic AI trust pages with no agentic specifics.
- The buyer or their regulator has signalled concern about agentic systems, autonomous decisioning, or AI taking actions.

## Do Not Use When

- The engagement is non-agent (use `ai-on-saas-compliance-credentials` or `saas-trust-and-compliance-credentials-section`).

## Required Inputs

- The Trust and Compliance posture from the AI-on-SaaS or SaaS skill.
- The action catalogue with reversibility classification.
- The autonomy-level commitment per action class.
- The kill-switch architecture and drill evidence.
- The intervention SLO and the audit-log completeness SLA.
- The red-team catalogue specific to agents.
- The agent identity and impersonation policy.
- The transparency-to-affected-party posture per jurisdiction.

## Workflow

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

## Anti-Patterns

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

## Outputs

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

## References

- `../references/ai-agent-trust-and-compliance-template.md` — full template.
- `../references/ai-agent-procurement-questionnaire-pack.md` — questionnaire answers consistent with these credentials.
- `../references/ai-agent-responsible-ai-commitment.md` — commitment that this section makes visible.
- `../references/ai-on-saas-trust-and-compliance-section-template.md` — AI-on-SaaS trust base.
- `../ai-on-saas-compliance-credentials/SKILL.md` — load alongside for SaaS-embedded agents.
- `../ai-agent-risk-and-responsible-ai/SKILL.md` — risk register and commitment.
- `../ai-agent-procurement-and-questionnaire/SKILL.md` — procurement answers.
