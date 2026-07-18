---
name: ai-on-saas-vertical-positioning
description: Use when AI-on-SaaS positioning must reflect a named vertical's use cases, regulator stance, evidence expectations, and risk language; use SaaS vertical positioning when AI-specific buyer concerns are absent.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI-on-SaaS Vertical Positioning
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The AI-on-SaaS bid is in a defined vertical and the proposal must demonstrate vertical literacy.
- The buyer's evaluators include vertical specialists (regulator, sector champion, clinical lead, head of supervision).
- The competitive set includes horizontal vendors who do not understand the vertical's AI exposure.
- The vertical carries AI-specific regulator stances (financial-services model-risk, healthcare clinical decision support, public-sector procurement on AI, education student-data).

## Do Not Use When

- The engagement is horizontal and the vertical is not a discriminator.
- The vertical is non-AI (use `saas-vertical-positioning`).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The buyer's vertical and sub-vertical. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The regulator(s) and stance. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The candidate AI use cases. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The competitive set (named or inferred). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's hallucination tolerance and HITL appetite. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Identify the vertical and load the matching vertical reference (`vertical-ai-on-saas-<vertical>.md`).
2. Choose two to four **named AI use cases** appropriate to the vertical (e.g. in financial services: KYC document understanding, transaction-monitoring triage, complaint classification, RM copilot; in insurance: claims-document triage, policy-comparison copilot, fraud signal explanation).
3. Position the agency's **discriminators** for the vertical: regulator literacy, model-risk practice, HITL design, eval discipline for vertical metrics, language coverage, sovereign-AI option, data-residency capability.
4. Frame **risk and regulator** language using the vertical's vocabulary, not generic AI language (financial-services: model-risk management, SR 11-7-style governance; healthcare: clinical decision support classification; public-sector: procurement-grade AI, sovereignty; education: minor data, exam integrity).
5. Choose the **win themes** from `ai-on-saas-win-themes-and-discriminators.md` that fit the vertical.
6. Draft the **vertical positioning paragraph** for Executive Summary, the **vertical case studies** (or comparable references) for Relevant Experience, and the **vertical methodology variations** for `06-methodology`.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Vertical Library (Brief)

### Financial Services
- AI use cases: KYC and ID document AI, transaction-monitoring triage, RM copilot, complaint classification, policy-Q&A copilot.
- Regulator: CBK, CBN, SARB, BoU, NBR; model-risk management discipline (SR 11-7-style).
- Discriminators: model-risk practice, HITL on decisioning, audit access, sovereign-AI option.

### Insurance
- AI use cases: claims-document triage, fraud signal explanation, policy-comparison copilot, underwriting evidence-grounding.
- Regulator: IRA, NAICOM, FSCA, IRA Uganda; conduct-of-business and fairness.
- Discriminators: explainability, citation grounding, audit trail, HITL on declinature.

### Public Sector
- AI use cases: case routing, document understanding (procurement, judiciary), citizen-FAQ copilot, multilingual translation, complaint triage.
- Regulator: NCAIS Kenya, NAIS Nigeria, NITA-U Uganda, RGB / Rwanda AI Policy, ICASA / DCDT South Africa; AI sovereignty discussions.
- Discriminators: sovereign-AI option, public-sector procurement literacy, local-language support, transparency commitments.

### Healthcare
- AI use cases: clinical-documentation copilot, triage-support (non-diagnostic), claims and prior-auth triage, hospital-operations copilot.
- Regulator: Ministries of Health, KMPDC, NHIS / SHA / SHIF, HPCSA; HIPAA where US-linked; clinical decision support classification.
- Discriminators: HITL on clinical actions, non-diagnostic framing where the regulator demands it, citation grounding, audit, residency.

### Education
- AI use cases: tutoring copilot, assessment-marking assistance (with HITL), advisor copilot, content-generation for instructors, accessibility (TTS, translation).
- Regulator: Ministry of Education, NCHE, CUE; data-protection regulators on minor data.
- Discriminators: exam-integrity stance, minor-data handling, instructor-in-the-loop, accessibility.

### Customer Support
- AI use cases: deflection copilot, ticket triage and routing, agent-assist copilot, voice-of-customer analytics.
- Regulator: data-protection regulators (general); sectoral where the support is for regulated services.
- Discriminators: containment vs deflection honesty, agent-assist over agent-replace framing, escalation SLA, language coverage.

## Quality Standards

- Vertical use cases are named and bounded; no generic "AI for the sector."
- Regulator references are specific.
- Discriminators are vertical-specific, not generic.
- Risk framing uses the vertical's vocabulary.
- Case studies or comparable references are in the vertical or transferable with stated rationale.

## Anti-Patterns

- "AI for banking" with no named use case. **Fix:** Name the banking workflow, user, decision, data, measurable value, human control, and regulated failure mode.
- Regulator framed as "applicable laws." **Fix:** Cite the named regulator and applicable rule or guidance, its relevance, current verification date, and required evidence.
- Discriminators copy-pasted across verticals. **Fix:** Build each discriminator from a vertical-specific constraint, proven capability, evidence, and buyer consequence.
- Healthcare AI claimed as diagnostic where the regulator requires non-diagnostic. **Fix:** Limit the claim to the authorised decision-support boundary and state clinical oversight, validation, and regulator requirements.
- Public-sector AI without a sovereignty or sovereignty-option position. **Fix:** State hosting, data residency, model-provider, support-access, audit, exit, and sovereign deployment options.
- Education AI without a minor-data stance. **Fix:** Define the minor-data lawful basis, consent, safeguarding, content controls, retention, access, and human escalation.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Vertical positioning paragraph for Executive Summary. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Vertical-specific use-case list with hallucination tolerance per case. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Vertical discriminators block. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Vertical risk and regulator language. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Vertical methodology variations for `06-methodology`. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Vertical case studies or comparable-reference selection. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

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

For an insurer, connect the AI use case to the claims workflow, governed data, review authority, customer-harm controls, and regulator expectations; do not rely on generic industry language.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/vertical-ai-on-saas-financial-services.md](../../profiles-sectors/references/vertical-ai-on-saas-financial-services.md)
- [../references/vertical-ai-on-saas-insurance.md](../../profiles-sectors/references/vertical-ai-on-saas-insurance.md)
- [../references/vertical-ai-on-saas-public-sector.md](../../profiles-sectors/references/vertical-ai-on-saas-public-sector.md)
- [../references/vertical-ai-on-saas-healthcare.md](../../profiles-sectors/references/vertical-ai-on-saas-healthcare.md)
- [../references/vertical-ai-on-saas-education.md](../../profiles-sectors/references/vertical-ai-on-saas-education.md)
- [../references/vertical-ai-on-saas-customer-support.md](../../profiles-sectors/references/vertical-ai-on-saas-customer-support.md)
- [../references/ai-on-saas-win-themes-and-discriminators.md](../../profiles-sectors/references/ai-on-saas-win-themes-and-discriminators.md)
- [../saas-vertical-positioning/SKILL.md](../../saas-proposals/saas-vertical-positioning/SKILL.md) — base SaaS vertical positioning.
- [../ai-on-saas-combined-methodology/SKILL.md](../ai-on-saas-combined-methodology/SKILL.md) — methodology that the vertical variations sit inside.
- [../ai-on-saas-risk-and-responsible-ai/SKILL.md](../ai-on-saas-risk-and-responsible-ai/SKILL.md) — risk register with vertical-specific entries.
