# Vertical AI-on-SaaS — Insurance

Vertical positioning, named AI use cases, regulator stance, discriminators, and risk language for AI-on-SaaS bids in life, non-life, health insurance, and reinsurance. Pairs with `ai-on-saas-vertical-positioning` and extends `vertical-saas-positioning-insurance.md`.

## Named AI Use Cases

| Use case | Hallucination tolerance | HITL stance | Risk class |
|---|---|---|---|
| Claims-document triage and information extraction | F1 ≥ 0.90 on critical fields | HITL on declinature; auto-route on simple | High |
| Fraud signal explanation (post-hoc rationale for a fraud score) | Explanatory; recall ≥ 0.95 on alerts | No decisioning | Medium |
| Underwriting evidence-grounding copilot (assembles file, cites evidence, recommends) | ≤ 1 % on cited evidence; recommendation only | HITL strict on bind / decline | High |
| Policy-comparison copilot (broker / distribution) | ≤ 2 % on advisory; ≥ 95 % citation | Broker is named adviser | Medium |
| Customer-service copilot (claims status, policy questions) | ≤ 2 % on factual | Agent-assist; agent confirms | Medium |
| Subrogation and recovery case-assembly | Drafting only | HITL strict | Medium |

## Regulator Stance

- **Kenya**: IRA (Insurance Regulatory Authority); CAK; ODPC; SHA / SHIF (health).
- **Uganda**: IRA Uganda; PDPO.
- **Tanzania**: TIRA.
- **Rwanda**: NBR (insurance supervision); NCDP.
- **Nigeria**: NAICOM; NDPC.
- **South Africa**: FSCA; PA; Information Regulator.
- **Cross-border**: IAIS principles; sectoral conduct-of-business rules.

Vertical-specific AI exposure:
- **Conduct-of-business** — fair treatment of customers; advisory AI must be calibrated, traceable, and complaint-friendly.
- **Underwriting fairness** — protected-class fairness is a live concern; per-cohort metrics expected.
- **Claims fairness** — declinature rates by cohort tracked; explainability required.
- **Health-data sensitivity** — health insurance and clinical-decision-support AI carries elevated data-protection scrutiny.

## Discriminators for Insurance Bids

1. **Claims-AI HITL discipline** — AI assembles the case, the human approves or declines; AI never auto-declines.
2. **Underwriting fairness measurement** — per-cohort metrics, cohort-drift alerting, fairness sign-off at the AI Governance Forum.
3. **Citation-grounded advisory** — broker / distribution AI cites the policy clause or comparison source.
4. **Conduct-of-business audit trail** — every customer-facing AI output has a retained audit log for complaints, dispute, and regulator review.
5. **Health-data segregation** — health policies and claims use a region-pinned, residency-controlled inference path; PHI is data-minimised in prompts.

## Risk Framing — Insurance-Specific Language

- "Fair-treatment-of-customers risk."
- "Declinature explainability."
- "Underwriting cohort drift."
- "Health-data routing."
- "Subrogation completeness."
- "Recovery-letter accuracy" for outbound communications.

## Sample Vertical Paragraph

> In insurance, our AI-on-SaaS practice treats every claims, underwriting, and customer-facing AI feature as a conduct-of-business control. AI assembles, recommends, and explains; humans approve, decline, and bind. Per-cohort metrics are published at the AI Governance Forum so that fairness is measured, not promised. Customer-facing advisory outputs cite the policy clause or product comparison source so that brokers, regulators, and customers can trace the basis of any recommendation. For health-insurance and any clinical-adjacent flows, inference is region-pinned and PHI is minimised in prompts under the residency policy agreed with the data-protection regulator.

## Cross-References

- `vertical-saas-positioning-insurance.md` — base insurance SaaS positioning.
- `ai-on-saas-risk-register-for-proposals.md`.
- `ai-on-saas-responsible-ai-commitment.md`.
- `ai-on-saas-trust-and-compliance-section-template.md`.
