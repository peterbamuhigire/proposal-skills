---
name: ai-on-saas-compliance-credentials
description: Use when a proposal must evidence AI-specific trust and compliance controls inside multi-tenant SaaS, including model providers, evaluation practice, data use, and region routing; use the SaaS trust skill for non-AI credentials.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI-on-SaaS Compliance Credentials
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The proposal includes a Trust and Compliance section and the engagement contains AI features.
- The buyer's procurement, CISO, or DPO will score the AI compliance posture.
- The bid is in a regulated vertical or an AI-Act-relevant market.
- The competitive set includes vendors who present generic SaaS trust pages with no AI specifics.

## Do Not Use When

- The engagement contains no AI (use `saas-trust-and-compliance-credentials-section`).
- The proposal does not include a Trust and Compliance section (rare for premium / regulated bids).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The Trust and Compliance posture from the SaaS skill (`saas-trust-and-compliance-credentials-section`). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The model-provider list and contractual posture. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The eval discipline (datasets, metrics, refresh cadence, CI integration). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The red-team practice (frequency, scope, scorecard). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The model-card practice (which features have model cards, what they contain, where they are published). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The region-routing capability. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The sovereign-AI offer (if any). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Open with the **AI Trust Posture** paragraph: the agency operates AI inside a multi-tenant SaaS under a Responsible-AI commitment, with eval discipline, model-card practice, sub-processor disclosure, and a named accountable role.
2. Populate the **AI Compliance Map** — for each regulator and standard the bid touches, state the agency's posture (ready, in-progress, not-in-scope) with evidence references:
   - EU AI Act (tier assessment, conformity documentation, post-market monitoring).
   - Kenya NCAIS principles, Nigeria NAIS, South Africa AI policy, Uganda NITA-U guidance, Rwanda AI Policy.
   - GDPR / POPIA / Kenya DPA / Nigeria NDPA / Uganda DPPA / Rwanda DPL — interaction with AI features.
   - ISO 42001 (AI management system) and ISO 23894 (AI risk).
   - NIST AI RMF.
   - Sectoral: financial-services model-risk management, HIPAA, education data.
3. Populate the **Model-Card Practice** subsection: which AI features publish model cards, what they cover (training data, intended use, evaluation, limitations, risks, contact), where they live, refresh cadence.
4. Populate the **Eval-Harness-in-CI** subsection: golden datasets, metric thresholds, CI gate on threshold breach, drift watch in production.
5. Populate the **Hallucination SLO** subsection: hallucination rate ceiling per feature, measurement method, alerting threshold, response runbook.
6. Populate the **Red-Team Practice** subsection: frequency, scope (prompt injection, data exfiltration, jailbreak, sensitive-output), scorecard, remediation cadence.
7. Populate the **AI Sub-Processor Disclosure** subsection: model providers named, regions, retention defaults, training-data posture, fall-back providers, kill-switch.
8. Populate the **Region Routing and Sovereign-AI Options**: EU-data-routes-to-EU-inference, KE-data-routes-to-KE/ZA-inference, on-prem or sovereign-cloud option for regulated tenants.
9. Output the **Trust and Compliance for AI** subsection to drop into the proposal's main Trust and Compliance section.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- AI compliance map names regulators specifically, not "applicable laws."
- Posture per regulator is one of ready / in-progress / not-in-scope, with evidence reference for ready and a target date for in-progress.
- Model-card practice describes content and publication location, not "we publish model cards."
- Eval-harness is in CI; threshold breach blocks deploy.
- Hallucination SLO is a number with a measurement method, not "we monitor hallucination."
- Sub-processor disclosure names the providers, not "third-party AI providers."
- Region-routing and sovereign-AI options are described concretely.

## Anti-Patterns

- "We comply with all applicable AI laws." **Fix:** Name the jurisdiction, applicable requirement, control, evidence status, owner, and unresolved professional-review need.
- "We follow Responsible AI principles" with no commitment. **Fix:** Publish a scoped commitment with accountable owner, governance cadence, evaluation controls, transparency, and redress.
- Model cards mentioned without content or location. **Fix:** Identify each model card's owner, location, version, intended use, limitations, evaluation evidence, and review date.
- Eval mentioned without CI integration. **Fix:** Run evaluation suites in CI with thresholds, failure handling, evidence retention, and production release blocking.
- Hallucination SLO as a target, not a measurement. **Fix:** Define the SLO metric, cohort, measurement window, threshold, alert, escalation, and rollback or abstention response.
- "Third-party AI providers" instead of named providers. **Fix:** Name each provider, service, data class, region, retention term, training posture, and change-notification process.
- Sovereign-AI promised without an architecture description. **Fix:** Describe the deployable sovereign architecture, dependencies, data boundary, model options, operations, cost, and acceptance tests.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Trust Posture paragraph. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| AI Compliance Map table. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Model-Card Practice subsection. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Eval-Harness-in-CI subsection. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Hallucination SLO subsection. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Red-Team Practice subsection. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| AI Sub-Processor Disclosure subsection. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Region Routing and Sovereign-AI Options subsection. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## Agent Overlay

For agentic engagements, the Trust and Compliance section gains agent-specific subsections: **action audit log practice** with 99 % completeness SLA, **irreversibility gating** with named approvers, **intervention SLO**, **kill-switch architecture and quarterly drill** with drill log, **agent-specific red-team catalogue** (prompt injection via tool output, scope manipulation, memory poisoning, identity confusion, multi-agent collusion), **agent identity and impersonation policy**, **action-scope attestation**, **multi-agent governance** (where applicable), and **transparency-to-affected-party UX**. Sub-processor disclosure expands to name tool-call APIs as well as model providers. Load `../ai-agent-compliance-credentials/SKILL.md` for the agent trust template.

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
| Credential status | Label each control verified, planned, inherited, or not evidenced | Misrepresentation to procurement or regulators |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

If model provenance or evaluation records cannot be produced, state the gap and current controls, omit the affected trust assurance, and require compliance-owner review before submission.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/ai-on-saas-trust-and-compliance-section-template.md](../../profiles-sectors/references/ai-on-saas-trust-and-compliance-section-template.md) — full template.
- [../references/ai-on-saas-procurement-questionnaire-pack.md](../../profiles-sectors/references/ai-on-saas-procurement-questionnaire-pack.md) — questionnaire answers consistent with these credentials.
- [../references/ai-on-saas-responsible-ai-commitment.md](../../profiles-sectors/references/ai-on-saas-responsible-ai-commitment.md) — commitment that this section makes visible.
- [../references/saas-trust-and-compliance-section-template.md](../../profiles-sectors/references/saas-trust-and-compliance-section-template.md) — base SaaS trust template.
- [../saas-trust-and-compliance-credentials-section/SKILL.md](../../saas-proposals/saas-trust-and-compliance-credentials-section/SKILL.md) — base SaaS trust credentials skill.
- [../ai-on-saas-risk-and-responsible-ai/SKILL.md](../ai-on-saas-risk-and-responsible-ai/SKILL.md) — risk register and commitment.
- [../ai-on-saas-procurement-and-questionnaire/SKILL.md](../ai-on-saas-procurement-and-questionnaire/SKILL.md) — procurement answers.
