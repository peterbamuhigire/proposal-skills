# Vertical AI-on-SaaS — Healthcare

Vertical positioning, named AI use cases, regulator stance, discriminators, and risk language for AI-on-SaaS bids in hospitals, health insurers, claims management, NHIS / SHA / SHIF, and clinical-decision-support adjacent products. Pairs with `ai-on-saas-vertical-positioning` and extends `vertical-saas-positioning-healthcare.md`.

## Named AI Use Cases

| Use case | Hallucination tolerance | HITL stance | Risk class |
|---|---|---|---|
| Clinical-documentation copilot (drafts notes, summaries, discharge letters) | ≤ 1 % on factual; clinician-edit before save | HITL strict on every document | High |
| Triage-support (non-diagnostic; routing, urgency hints) | Domain-cohort calibrated | HITL on dispatch | High |
| Claims and prior-authorisation triage | F1 ≥ 0.90 | HITL on declinature; auto-approve only on bright-line cases with audit | High |
| Hospital-operations copilot (rostering, supply, scheduling) | Operational | HITL on resource decisions | Medium |
| Patient-FAQ copilot (non-clinical, e.g. visiting hours, billing) | ≤ 2 % with citation | Escalation to staff for clinical | Medium |
| Coding-and-billing assistance | Recommendation only | HITL by certified coder | High |

## Regulator Stance

- **Kenya**: Ministry of Health; KMPDC; Pharmacy and Poisons Board; SHA / SHIF; ODPC.
- **Uganda**: Ministry of Health; UMDPC; PDPO.
- **Tanzania**: Ministry of Health.
- **Rwanda**: Ministry of Health; RBC; NCDP.
- **Nigeria**: Ministry of Health; NHIA; NDPC.
- **South Africa**: HPCSA; Department of Health; Information Regulator (POPIA + health).
- **Cross-border**: HIPAA where US-linked tenants exist; EU MDR / AI Act for medical-device classification.

Vertical-specific AI exposure:
- **Clinical decision support classification** — regulators in some jurisdictions classify AI that "supports clinical decisions" as a medical device. Most agency engagements should frame AI features as **non-diagnostic, non-prescriptive, non-treatment-recommending** to remain outside medical-device classification, unless the engagement is specifically a medical-device build with the requisite team.
- **Patient-data sensitivity** — health data has elevated retention, deletion, and access-control requirements.
- **Clinician-in-the-loop** — every clinical-adjacent AI feature has a named clinician authority.

## Discriminators for Healthcare Bids

1. **Non-diagnostic framing where the regulator demands** — explicit out-of-scope statements; pre-market dialogue plan; documentary evidence that the AI does not diagnose, prescribe, or recommend treatment.
2. **Clinician-in-the-loop discipline** — named clinician role with authority, SLA, and audit; no AI auto-action on clinical or claims-decisioning flows.
3. **Patient-data residency and PHI minimisation** — region-pinned inference; PHI minimised in prompts; data-minimisation pipeline documented.
4. **Citation grounding on every clinical-adjacent output** — outputs cite the source (record, guideline, protocol).
5. **Audit pack for the clinical governance committee** — model cards, eval methodology, hallucination SLO, redress log, incident summary — formatted for the committee's expectations.

## Risk Framing — Healthcare-Specific Language

- "Non-diagnostic" (not "decision support").
- "Clinician-in-the-loop" (not "human review").
- "PHI minimisation."
- "Coding fidelity" (not "accuracy") for billing-related AI.
- "Patient redress" (not "user complaint").
- "Clinical governance committee" (not "SteerCo") where appropriate.

## Sample Vertical Paragraph

> In healthcare, our AI-on-SaaS practice is explicit about what the AI does and does not do. The AI does not diagnose, does not prescribe, does not recommend treatment, and does not auto-decide on clinical or claims-decisioning flows. The AI drafts, assembles, summarises, codes, and routes — under a clinician-in-the-loop discipline that names the clinical authority and the response SLA on every clinical-adjacent feature. PHI is minimised in prompts under a residency-pinned inference path. Every clinical-adjacent output cites the record, guideline, or protocol it is grounded in. The clinical governance committee receives a quarterly Responsible-AI report formatted for clinical review, and a patient-redress mechanism is published with a clear first-response SLA. Where the regulator classifies the AI as a medical device, we will not contract for that scope without the requisite medical-device team and conformity assessment in place.

## Cross-References

- `vertical-saas-positioning-healthcare.md`.
- `ai-on-saas-risk-register-for-proposals.md` — R-AI-HC-01 clinical classification.
- `ai-on-saas-responsible-ai-commitment.md`.
- `ai-on-saas-trust-and-compliance-section-template.md`.
