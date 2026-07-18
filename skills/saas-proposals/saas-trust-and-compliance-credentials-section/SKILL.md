---
name: saas-trust-and-compliance-credentials-section
description: Use when a SaaS proposal needs an evidence-qualified trust and compliance section covering security, privacy, certifications, sub-processors, continuity, audit posture, insurance, and exit; use the procurement skill to manage questionnaire and negotiation workflow.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Trust and Compliance Credentials Section
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The ToR explicitly requires a Trust and Compliance, Security, or Information Governance section.
- The buyer is regulated and the bid will face structured security review.
- The proposal includes premium fee defence and the trust posture is part of the value justification.
- The agency must produce a standalone Trust and Compliance document for procurement.

## Do Not Use When

- The bid is purely a price response with no security or compliance content required.
- The standard security paragraph in Methodology is sufficient (use `06-methodology/` directly).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The buyer's vertical and regulator stance. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The agency's certifications, sub-processors, BCDR posture, and insurance limits. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's specific security questionnaire (if issued). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The data residency and sovereignty obligations. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Produce the 16-section structure: opening; information security management; tenant isolation; data residency; identity and access; encryption; application security; logging and audit; BCDR; incident response; compliance certifications; exit; audit rights; insurance; SLA; continuous trust posture.
2. Tailor each section to the buyer's vertical and regulator stance.
3. Add Annex A (Sub-Processor Register), Annex B (Compliance Mapping), Annex C (Incident Response Summary).
4. Cross-reference the relevant risk register entries and the MSA / DPA / SLA template language.
5. Quality-check every claim for evidence (certification scope, audit report, penetration test report, DR test report).
6. Brief the agency team for security-review meetings.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Every claim is specific or evidenced.
- Sub-processors fully disclosed.
- Certification scope stated explicitly.
- SLA and credit structure consistent across MSA, DPA, SLA documents.
- Continuous-trust posture (annual pen-test, annual DR test, annual customer-facing trust report) committed.

## Anti-Patterns

- Marketing language ("industry-leading", "world-class") in security claims. **Fix:** Replace adjectives with named controls, assurance evidence, scope, owner, status, limitations, and review date.
- Promising certifications without scope. **Fix:** State certification entity, service scope, locations, standard version, validity, exclusions, and evidence location.
- Hidden sub-processors. **Fix:** Publish the sub-processor name, purpose, data class, region, terms, change process, and customer options.
- Mismatched breach-notice times across MSA, DPA, and SLA. **Fix:** Use one breach-notice rule across MSA, DPA, SLA, incident response, and provider contracts, or document lawful differences.
- Insurance limits without certificate availability. **Fix:** State insurer, policy type, limit, territory, expiry, exclusions, and whether a current certificate can be provided.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Trust and Compliance section for the proposal. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Standalone Trust and Compliance document for procurement. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Sub-processor register. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Compliance mapping table. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Incident response summary. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## AI Compliance Subsection

When the SaaS contains AI features, the Trust and Compliance section must add an AI subsection: AI Trust Posture paragraph, AI Compliance Map (EU AI Act, Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U guidance, Rwanda AI Policy, ISO 42001 / 23894, NIST AI RMF, sectoral), Model-Card Practice, Eval-Harness-in-CI, Hallucination SLO (numeric ceiling, measurement, alerting, runbook), Red-Team Practice (frequency, scope, scorecard), AI Sub-Processor Disclosure (named providers, region, retention, training posture, fallback), and Region Routing and Sovereign-AI Options. The named accountable role (AI Safety Lead) appears here and in the Responsible-AI commitment. See `../ai-on-saas-compliance-credentials/SKILL.md` and `../references/ai-on-saas-trust-and-compliance-section-template.md`.

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

When a certification has expired or cannot be verified, omit the badge and claim, state the current evidenced control posture, and assign verification to the compliance owner.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/saas-trust-and-compliance-section-template.md](../../profiles-sectors/references/saas-trust-and-compliance-section-template.md) — primary template.
- [../references/ai-on-saas-trust-and-compliance-section-template.md](../../profiles-sectors/references/ai-on-saas-trust-and-compliance-section-template.md) — AI Trust and Compliance subsection template.
- [../references/ai-on-saas-responsible-ai-commitment.md](../../profiles-sectors/references/ai-on-saas-responsible-ai-commitment.md) — Responsible-AI commitment.
- [../ai-on-saas-compliance-credentials/SKILL.md](../../ai-on-saas-proposals/ai-on-saas-compliance-credentials/SKILL.md) — companion skill for AI-on-SaaS trust credentials.
- [../references/saas-procurement-and-security-questionnaire-playbook.md](../../profiles-sectors/references/saas-procurement-and-security-questionnaire-playbook.md) — underlying playbook.
- [../references/saas-msa-dpa-sla-template-language.md](../../profiles-sectors/references/saas-msa-dpa-sla-template-language.md) — contract-grade language.
- [../references/saas-multi-tenant-architecture-block.md](../../profiles-sectors/references/saas-multi-tenant-architecture-block.md) — architecture credibility.
- [../references/saas-risk-register-for-proposals.md](../../profiles-sectors/references/saas-risk-register-for-proposals.md) — linked risks.
- [../saas-procurement-and-security-questionnaire/SKILL.md](../saas-procurement-and-security-questionnaire/SKILL.md) — procurement and security workstream.
