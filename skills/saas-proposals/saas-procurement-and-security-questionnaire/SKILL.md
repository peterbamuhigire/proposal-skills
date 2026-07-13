---
name: saas-procurement-and-security-questionnaire
description: Use when a SaaS bid must address procurement, legal, privacy, security, DPA, MSA, SLA, residency, sub-processor, audit-right, insurance, and exit review; use the AI questionnaire skill when model-provider and training-data issues apply.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Procurement and Security Questionnaire
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The SaaS bid is at procurement, legal review, security review, or BAFO stage.
- The buyer is regulated (financial services, insurance, public sector, healthcare) and the security questionnaire is rigorous.
- The agency must produce a Trust and Compliance section as a standalone document.
- The contract negotiation requires DPA, MSA, SLA template language.

## Do Not Use When

- The engagement is not SaaS-related.
- The buyer's procurement has no security or compliance scrutiny (rare for premium engagements).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The buyer's vertical and applicable regulators. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The procurement framework (PPDA, World Bank, AfDB, UNDP, direct client). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The agency's current certifications, sub-processors, BCDR posture, and insurance limits. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Any specific procurement, legal, or security questionnaire issued by the buyer. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Map the procurement path: RFI → RFP → submission → technical evaluation → references → demo → security review → legal review → BAFO → award → contract → signature.
2. Prepare or refresh the security questionnaire pack covering 12 standard categories (organisational security, tenant isolation, data residency, identity, encryption, application security, logging, BCDR, incident response, compliance certifications, exit, contractual flow-down).
3. Tailor the pack to the buyer's vertical and regulator stance.
4. Pre-empt likely security questions before they are asked; submit the pack with the proposal or as Annex A to the Trust and Compliance section.
5. Prepare DPA / MSA / SLA template language and standard negotiated carve-outs.
6. Identify procurement clarification requests early in the clarification window.
7. Brief the agency's account team before security review and legal review meetings.
8. Manage redline rounds with the agency's legal team.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Every security answer is specific or evidenced, not marketing language.
- Sub-processors are fully disclosed, not hidden.
- Certifications stated include their certified scope.
- SLA and SLA-credit structure is internally consistent across MSA, DPA, and SLA documents.
- Insurance limits stated are backed by certificates available on signature.

## Anti-Patterns

- Marketing language in security answers ("world-class", "industry-leading"). **Fix:** Answer with control description, scope, evidence, owner, status, and limitations rather than unsupported adjectives.
- Promising certifications the agency does not hold. **Fix:** State only certifications held in the applicable entity, service, region, and validity period, linking approved evidence.
- Hiding sub-processors. **Fix:** Maintain a named sub-processor register with purpose, data, region, terms, change notice, objection, and exit process.
- Mismatched DPA breach-notice (24h) and SLA breach-notice (72h). **Fix:** Reconcile MSA, DPA, SLA, incident plan, and provider obligations to one achievable breach-notice timeline.
- "We will commit to X" with no penalty structure. **Fix:** Convert any future commitment into a dated obligation with owner, evidence, remedy, service credit, or negotiated limitation.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Trust and Compliance section. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Security questionnaire response pack. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Sub-processor register. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| DPA / MSA / SLA template language. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Procurement clarification requests. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Redline strategy for contract negotiation. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## AI Questionnaire Pack

When the SaaS contains AI features, the procurement response must answer the eight AI procurement domains: model providers and sub-processors (named, not "third-party AI providers"); training-data posture (zero retention, opt-out, basis); retention and deletion (numbers and runbook); region routing (per data class); sovereign-AI / on-prem options; eval, hallucination, and quality (numeric thresholds and cadence); safety, security and abuse (prompt injection, jailbreak, abuse detection, incident runbook); governance, audit, and redress (forum, audit access, redress SLA). Sub-processor list now includes model providers. See `../ai-on-saas-procurement-and-questionnaire/SKILL.md` and `../references/ai-on-saas-procurement-questionnaire-pack.md` for the full answer pack with sample language.

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
| Control claim | Provide approved evidence or mark the answer pending with an owner and date | False assurance or silent procurement gap |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

If the current sub-processor register is unavailable, answer the affected questionnaire item as not assessed, name the security owner and due date, and do not state that no sub-processors are used.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/saas-procurement-and-security-questionnaire-playbook.md](../../profiles-sectors/references/saas-procurement-and-security-questionnaire-playbook.md) — primary playbook.
- [../references/ai-on-saas-procurement-questionnaire-pack.md](../../profiles-sectors/references/ai-on-saas-procurement-questionnaire-pack.md) — AI questionnaire answer pack.
- [../ai-on-saas-procurement-and-questionnaire/SKILL.md](../../ai-on-saas-proposals/ai-on-saas-procurement-and-questionnaire/SKILL.md) — companion skill for AI-on-SaaS procurement.
- [../references/saas-msa-dpa-sla-template-language.md](../../profiles-sectors/references/saas-msa-dpa-sla-template-language.md) — contract-grade language patterns.
- [../references/saas-trust-and-compliance-section-template.md](../../profiles-sectors/references/saas-trust-and-compliance-section-template.md) — section template.
- [../references/saas-risk-register-for-proposals.md](../../profiles-sectors/references/saas-risk-register-for-proposals.md) — linked risks.
- [../references/saas-mutual-action-plan-template.md](../../profiles-sectors/references/saas-mutual-action-plan-template.md) — Phase 2 detail.
- [../sectors/SKILL.md](../../profiles-sectors/sectors/SKILL.md) — procurement framework routing.
