---
name: ai-on-saas-vertical-positioning
description: Use when the AI-on-SaaS proposal must position the agency for a specific vertical — financial services, insurance, public sector, healthcare, education, customer support. Provides vertical-specific AI plays, regulator stance, discriminators, named use cases, risk-framing language, and competitive displacement angles. Extends `saas-vertical-positioning` with the AI overlay.
---

# AI-on-SaaS Vertical Positioning
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The AI-on-SaaS bid is in a defined vertical and the proposal must demonstrate vertical literacy.
- The buyer's evaluators include vertical specialists (regulator, sector champion, clinical lead, head of supervision).
- The competitive set includes horizontal vendors who do not understand the vertical's AI exposure.
- The vertical carries AI-specific regulator stances (financial-services model-risk, healthcare clinical decision support, public-sector procurement on AI, education student-data).

## Do Not Use When

- The engagement is horizontal and the vertical is not a discriminator.
- The vertical is non-AI (use `saas-vertical-positioning`).

## Required Inputs

- The buyer's vertical and sub-vertical.
- The regulator(s) and stance.
- The candidate AI use cases.
- The competitive set (named or inferred).
- The buyer's hallucination tolerance and HITL appetite.

## Workflow

1. Identify the vertical and load the matching vertical reference (`vertical-ai-on-saas-<vertical>.md`).
2. Choose two to four **named AI use cases** appropriate to the vertical (e.g. in financial services: KYC document understanding, transaction-monitoring triage, complaint classification, RM copilot; in insurance: claims-document triage, policy-comparison copilot, fraud signal explanation).
3. Position the agency's **discriminators** for the vertical: regulator literacy, model-risk practice, HITL design, eval discipline for vertical metrics, language coverage, sovereign-AI option, data-residency capability.
4. Frame **risk and regulator** language using the vertical's vocabulary, not generic AI language (financial-services: model-risk management, SR 11-7-style governance; healthcare: clinical decision support classification; public-sector: procurement-grade AI, sovereignty; education: minor data, exam integrity).
5. Choose the **win themes** from `ai-on-saas-win-themes-and-discriminators.md` that fit the vertical.
6. Draft the **vertical positioning paragraph** for Executive Summary, the **vertical case studies** (or comparable references) for Relevant Experience, and the **vertical methodology variations** for `06-methodology`.

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

- "AI for banking" with no named use case.
- Regulator framed as "applicable laws."
- Discriminators copy-pasted across verticals.
- Healthcare AI claimed as diagnostic where the regulator requires non-diagnostic.
- Public-sector AI without a sovereignty or sovereignty-option position.
- Education AI without a minor-data stance.

## Outputs

- Vertical positioning paragraph for Executive Summary.
- Vertical-specific use-case list with hallucination tolerance per case.
- Vertical discriminators block.
- Vertical risk and regulator language.
- Vertical methodology variations for `06-methodology`.
- Vertical case studies or comparable-reference selection.

## References

- `../references/vertical-ai-on-saas-financial-services.md`
- `../references/vertical-ai-on-saas-insurance.md`
- `../references/vertical-ai-on-saas-public-sector.md`
- `../references/vertical-ai-on-saas-healthcare.md`
- `../references/vertical-ai-on-saas-education.md`
- `../references/vertical-ai-on-saas-customer-support.md`
- `../references/ai-on-saas-win-themes-and-discriminators.md`
- `../saas-vertical-positioning/SKILL.md` — base SaaS vertical positioning.
- `../ai-on-saas-combined-methodology/SKILL.md` — methodology that the vertical variations sit inside.
- `../ai-on-saas-risk-and-responsible-ai/SKILL.md` — risk register with vertical-specific entries.
