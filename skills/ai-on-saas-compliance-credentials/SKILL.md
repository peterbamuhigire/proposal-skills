---
name: ai-on-saas-compliance-credentials
description: Use when the AI-on-SaaS proposal must showcase Trust and Compliance credentials specific to AI inside a multi-tenant SaaS. Provides the Trust-and-Compliance-for-AI section template covering AI Act readiness, model-card practice, eval-harness CI, hallucination SLO, red-team practice, sub-processor disclosure for model providers, training-data posture, region routing, and sovereign-AI options. Extends `saas-trust-and-compliance-credentials-section` with the AI subsection.
---

# AI-on-SaaS Compliance Credentials
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The proposal includes a Trust and Compliance section and the engagement contains AI features.
- The buyer's procurement, CISO, or DPO will score the AI compliance posture.
- The bid is in a regulated vertical or an AI-Act-relevant market.
- The competitive set includes vendors who present generic SaaS trust pages with no AI specifics.

## Do Not Use When

- The engagement contains no AI (use `saas-trust-and-compliance-credentials-section`).
- The proposal does not include a Trust and Compliance section (rare for premium / regulated bids).

## Required Inputs

- The Trust and Compliance posture from the SaaS skill (`saas-trust-and-compliance-credentials-section`).
- The model-provider list and contractual posture.
- The eval discipline (datasets, metrics, refresh cadence, CI integration).
- The red-team practice (frequency, scope, scorecard).
- The model-card practice (which features have model cards, what they contain, where they are published).
- The region-routing capability.
- The sovereign-AI offer (if any).

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

## Quality Standards

- AI compliance map names regulators specifically, not "applicable laws."
- Posture per regulator is one of ready / in-progress / not-in-scope, with evidence reference for ready and a target date for in-progress.
- Model-card practice describes content and publication location, not "we publish model cards."
- Eval-harness is in CI; threshold breach blocks deploy.
- Hallucination SLO is a number with a measurement method, not "we monitor hallucination."
- Sub-processor disclosure names the providers, not "third-party AI providers."
- Region-routing and sovereign-AI options are described concretely.

## Anti-Patterns

- "We comply with all applicable AI laws."
- "We follow Responsible AI principles" with no commitment.
- Model cards mentioned without content or location.
- Eval mentioned without CI integration.
- Hallucination SLO as a target, not a measurement.
- "Third-party AI providers" instead of named providers.
- Sovereign-AI promised without an architecture description.

## Outputs

- AI Trust Posture paragraph.
- AI Compliance Map table.
- Model-Card Practice subsection.
- Eval-Harness-in-CI subsection.
- Hallucination SLO subsection.
- Red-Team Practice subsection.
- AI Sub-Processor Disclosure subsection.
- Region Routing and Sovereign-AI Options subsection.

## References

- `../references/ai-on-saas-trust-and-compliance-section-template.md` — full template.
- `../references/ai-on-saas-procurement-questionnaire-pack.md` — questionnaire answers consistent with these credentials.
- `../references/ai-on-saas-responsible-ai-commitment.md` — commitment that this section makes visible.
- `../references/saas-trust-and-compliance-section-template.md` — base SaaS trust template.
- `../saas-trust-and-compliance-credentials-section/SKILL.md` — base SaaS trust credentials skill.
- `../ai-on-saas-risk-and-responsible-ai/SKILL.md` — risk register and commitment.
- `../ai-on-saas-procurement-and-questionnaire/SKILL.md` — procurement answers.
