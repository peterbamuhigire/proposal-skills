---
name: saas-trust-and-compliance-credentials-section
description: Use when a SaaS proposal requires a dedicated Trust and Compliance section covering security, privacy, compliance certifications, sub-processors, BCDR, audit posture, regulator alignment, exit clauses, and insurance. Produces evaluator-grade content that addresses CISO, DPO, and procurement security review concerns.
---

# SaaS Trust and Compliance Credentials Section
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The ToR explicitly requires a Trust and Compliance, Security, or Information Governance section.
- The buyer is regulated and the bid will face structured security review.
- The proposal includes premium fee defence and the trust posture is part of the value justification.
- The agency must produce a standalone Trust and Compliance document for procurement.

## Do Not Use When

- The bid is purely a price response with no security or compliance content required.
- The standard security paragraph in Methodology is sufficient (use `06-methodology/` directly).

## Required Inputs

- The buyer's vertical and regulator stance.
- The agency's certifications, sub-processors, BCDR posture, and insurance limits.
- The buyer's specific security questionnaire (if issued).
- The data residency and sovereignty obligations.

## Workflow

1. Produce the 16-section structure: opening; information security management; tenant isolation; data residency; identity and access; encryption; application security; logging and audit; BCDR; incident response; compliance certifications; exit; audit rights; insurance; SLA; continuous trust posture.
2. Tailor each section to the buyer's vertical and regulator stance.
3. Add Annex A (Sub-Processor Register), Annex B (Compliance Mapping), Annex C (Incident Response Summary).
4. Cross-reference the relevant risk register entries and the MSA / DPA / SLA template language.
5. Quality-check every claim for evidence (certification scope, audit report, penetration test report, DR test report).
6. Brief the agency team for security-review meetings.

## Quality Standards

- Every claim is specific or evidenced.
- Sub-processors fully disclosed.
- Certification scope stated explicitly.
- SLA and credit structure consistent across MSA, DPA, SLA documents.
- Continuous-trust posture (annual pen-test, annual DR test, annual customer-facing trust report) committed.

## Anti-Patterns

- Marketing language ("industry-leading", "world-class") in security claims.
- Promising certifications without scope.
- Hidden sub-processors.
- Mismatched breach-notice times across MSA, DPA, and SLA.
- Insurance limits without certificate availability.

## Outputs

- Trust and Compliance section for the proposal.
- Standalone Trust and Compliance document for procurement.
- Sub-processor register.
- Compliance mapping table.
- Incident response summary.

## AI Compliance Subsection

When the SaaS contains AI features, the Trust and Compliance section must add an AI subsection: AI Trust Posture paragraph, AI Compliance Map (EU AI Act, Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U guidance, Rwanda AI Policy, ISO 42001 / 23894, NIST AI RMF, sectoral), Model-Card Practice, Eval-Harness-in-CI, Hallucination SLO (numeric ceiling, measurement, alerting, runbook), Red-Team Practice (frequency, scope, scorecard), AI Sub-Processor Disclosure (named providers, region, retention, training posture, fallback), and Region Routing and Sovereign-AI Options. The named accountable role (AI Safety Lead) appears here and in the Responsible-AI commitment. See `../ai-on-saas-compliance-credentials/SKILL.md` and `../references/ai-on-saas-trust-and-compliance-section-template.md`.

## References

- `../references/saas-trust-and-compliance-section-template.md` — primary template.
- `../references/ai-on-saas-trust-and-compliance-section-template.md` — AI Trust and Compliance subsection template.
- `../references/ai-on-saas-responsible-ai-commitment.md` — Responsible-AI commitment.
- `../ai-on-saas-compliance-credentials/SKILL.md` — companion skill for AI-on-SaaS trust credentials.
- `../references/saas-procurement-and-security-questionnaire-playbook.md` — underlying playbook.
- `../references/saas-msa-dpa-sla-template-language.md` — contract-grade language.
- `../references/saas-multi-tenant-architecture-block.md` — architecture credibility.
- `../references/saas-risk-register-for-proposals.md` — linked risks.
- `../saas-procurement-and-security-questionnaire/SKILL.md` — procurement and security workstream.
