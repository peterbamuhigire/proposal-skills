---
name: saas-procurement-and-security-questionnaire
description: Use when navigating procurement, legal, and security review for a SaaS implementation bid. Covers procurement path mapping, security questionnaire preparation, DPA / MSA / SLA negotiation, data residency, sub-processors, exit clauses, audit rights, and insurance. Prevents premium SaaS bids from slipping at procurement or security review.
---

# SaaS Procurement and Security Questionnaire
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The SaaS bid is at procurement, legal review, security review, or BAFO stage.
- The buyer is regulated (financial services, insurance, public sector, healthcare) and the security questionnaire is rigorous.
- The agency must produce a Trust and Compliance section as a standalone document.
- The contract negotiation requires DPA, MSA, SLA template language.

## Do Not Use When

- The engagement is not SaaS-related.
- The buyer's procurement has no security or compliance scrutiny (rare for premium engagements).

## Required Inputs

- The buyer's vertical and applicable regulators.
- The procurement framework (PPDA, World Bank, AfDB, UNDP, direct client).
- The agency's current certifications, sub-processors, BCDR posture, and insurance limits.
- Any specific procurement, legal, or security questionnaire issued by the buyer.

## Workflow

1. Map the procurement path: RFI → RFP → submission → technical evaluation → references → demo → security review → legal review → BAFO → award → contract → signature.
2. Prepare or refresh the security questionnaire pack covering 12 standard categories (organisational security, tenant isolation, data residency, identity, encryption, application security, logging, BCDR, incident response, compliance certifications, exit, contractual flow-down).
3. Tailor the pack to the buyer's vertical and regulator stance.
4. Pre-empt likely security questions before they are asked; submit the pack with the proposal or as Annex A to the Trust and Compliance section.
5. Prepare DPA / MSA / SLA template language and standard negotiated carve-outs.
6. Identify procurement clarification requests early in the clarification window.
7. Brief the agency's account team before security review and legal review meetings.
8. Manage redline rounds with the agency's legal team.

## Quality Standards

- Every security answer is specific or evidenced, not marketing language.
- Sub-processors are fully disclosed, not hidden.
- Certifications stated include their certified scope.
- SLA and SLA-credit structure is internally consistent across MSA, DPA, and SLA documents.
- Insurance limits stated are backed by certificates available on signature.

## Anti-Patterns

- Marketing language in security answers ("world-class", "industry-leading").
- Promising certifications the agency does not hold.
- Hiding sub-processors.
- Mismatched DPA breach-notice (24h) and SLA breach-notice (72h).
- "We will commit to X" with no penalty structure.

## Outputs

- Trust and Compliance section.
- Security questionnaire response pack.
- Sub-processor register.
- DPA / MSA / SLA template language.
- Procurement clarification requests.
- Redline strategy for contract negotiation.

## AI Questionnaire Pack

When the SaaS contains AI features, the procurement response must answer the eight AI procurement domains: model providers and sub-processors (named, not "third-party AI providers"); training-data posture (zero retention, opt-out, basis); retention and deletion (numbers and runbook); region routing (per data class); sovereign-AI / on-prem options; eval, hallucination, and quality (numeric thresholds and cadence); safety, security and abuse (prompt injection, jailbreak, abuse detection, incident runbook); governance, audit, and redress (forum, audit access, redress SLA). Sub-processor list now includes model providers. See `../ai-on-saas-procurement-and-questionnaire/SKILL.md` and `../references/ai-on-saas-procurement-questionnaire-pack.md` for the full answer pack with sample language.

## References

- `../references/saas-procurement-and-security-questionnaire-playbook.md` — primary playbook.
- `../references/ai-on-saas-procurement-questionnaire-pack.md` — AI questionnaire answer pack.
- `../ai-on-saas-procurement-and-questionnaire/SKILL.md` — companion skill for AI-on-SaaS procurement.
- `../references/saas-msa-dpa-sla-template-language.md` — contract-grade language patterns.
- `../references/saas-trust-and-compliance-section-template.md` — section template.
- `../references/saas-risk-register-for-proposals.md` — linked risks.
- `../references/saas-mutual-action-plan-template.md` — Phase 2 detail.
- `../sectors/SKILL.md` — procurement framework routing.
