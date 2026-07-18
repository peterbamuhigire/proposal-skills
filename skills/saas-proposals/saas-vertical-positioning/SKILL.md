---
name: saas-vertical-positioning
description: Use when a SaaS proposal must reflect a named vertical's buyers, regulators, integration constraints, proof expectations, commercial limits, and win themes; use AI-on-SaaS vertical positioning when AI use cases and model risks shape the message.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Vertical Positioning
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The SaaS implementation engagement targets a specific vertical and the proposal must demonstrate vertical depth.
- The buyer expects vertical-experienced consultants, vertical-specific integration knowledge, and regulator-aware engineering.
- The agency competes against horizontal generalists and must show defensible vertical specialism.

## Do Not Use When

- The engagement is horizontal (cross-sector productivity SaaS, generic CRM, etc.).
- The buyer's selection criteria do not value vertical depth.

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The buyer's vertical (and sub-vertical where applicable). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's regulator(s). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's current integration environment. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The agency's comparable vertical engagements with outcome figures. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Any vertical-specific certifications or partnerships the agency holds. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Load the vertical-specific positioning brief from the references.
2. Identify the sub-vertical and the typical buyer roles for that sub-vertical.
3. Map the regulator landscape and compliance realities for that vertical.
4. Map the common integration reality (named systems the SaaS must integrate with).
5. Select the comparable engagements the agency can credibly cite.
6. State the price-ceiling realities for the sub-vertical.
7. Select 3–5 win themes from the vertical-specific list.
8. Populate the Understanding of the Assignment with vertical-specific Pain Chain.
9. Add vertical-specific discovery questions to the BRIEF.md.
10. Produce the vertical-positioning paragraph for the Executive Summary and the vertical-specific differentiators for the Relevant Experience section.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Vertical depth is shown through specifics, not adjectives.
- Named integration systems (e.g., Temenos T24, Guidewire PolicyCenter, DHIS2) demonstrate fluency.
- Regulators are named, not "the regulator."
- Price-ceiling realities are acknowledged honestly.
- Comparable engagements have outcome figures, not just names.

## Anti-Patterns

- Vertical claims with no named integration, regulator, or comparable. **Fix:** Name the integration, regulator or sector rule, comparable evidence, buyer consequence, and delivery implication.
- "Banking experience" with no named core banking system. **Fix:** Identify the core banking platform or integration class, interface evidence, security boundary, and relevant assignment proof.
- "Public sector experience" with no procurement-framework fluency. **Fix:** Name the procurement framework, mandatory forms, evaluation method, approvals, and public-sector delivery constraint.
- "Healthcare experience" with no named EMR / HMIS / claims system. **Fix:** Name the EMR, HMIS, claims, interoperability standard, data boundary, and relevant health-system evidence.
- Pricing the engagement without acknowledging vertical-specific cycle length. **Fix:** Model procurement, security, integration, regulator, data, and adoption cycle length in schedule, cash flow, and price validity.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Vertical-positioning paragraph for the Executive Summary. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Vertical-specific Pain Chain for Understanding of the Assignment. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Vertical-specific differentiators for Relevant Experience. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Vertical-specific discovery questions added to BRIEF.md. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Vertical-specific risk register entries. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

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
| Jurisdiction or sector rule | Verify the named requirement and qualify applicability before citing it | Generic or legally inaccurate positioning |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

For a regulated lender, verify the jurisdiction, regulator, operating model, and audit expectations before selecting proof points; otherwise provide only a provisional sector hypothesis and clarification list.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/vertical-saas-positioning-financial-services.md](../../profiles-sectors/references/vertical-saas-positioning-financial-services.md).
- [../references/vertical-saas-positioning-insurance.md](../../profiles-sectors/references/vertical-saas-positioning-insurance.md).
- [../references/vertical-saas-positioning-public-sector.md](../../profiles-sectors/references/vertical-saas-positioning-public-sector.md).
- [../references/vertical-saas-positioning-healthcare.md](../../profiles-sectors/references/vertical-saas-positioning-healthcare.md).
- [../references/vertical-saas-positioning-education.md](../../profiles-sectors/references/vertical-saas-positioning-education.md).
- [../references/saas-discovery-question-bank.md](../../profiles-sectors/references/saas-discovery-question-bank.md) — general discovery.
- [../references/saas-business-case-and-roi-template.md](../../profiles-sectors/references/saas-business-case-and-roi-template.md) — vertical-tuned business case.
- [../references/saas-win-themes-and-discriminators.md](../../profiles-sectors/references/saas-win-themes-and-discriminators.md) — theme selection.
- [../05-relevant-experience/SKILL.md](../../pipeline/05-relevant-experience/SKILL.md) — relevant experience discipline.
- [../sectors/SKILL.md](../../profiles-sectors/sectors/SKILL.md) — procurement and sector routing.
