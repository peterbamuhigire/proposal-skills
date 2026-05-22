# Vertical AI-on-SaaS — Financial Services

Vertical positioning, named AI use cases, regulator stance, discriminators, and risk language for AI-on-SaaS bids in banking, payments, microfinance, capital markets, and investment management. Pairs with `ai-on-saas-vertical-positioning` and extends `vertical-saas-positioning-financial-services.md`.

## Named AI Use Cases (with hallucination tolerance and HITL stance)

| Use case | Hallucination tolerance | HITL stance | Risk class |
|---|---|---|---|
| KYC and ID-document AI (OCR + extraction + matching) | ≤ 1 % on critical fields | HITL on adverse decisioning | High |
| AML / transaction-monitoring triage and alert disposition support | ≤ 2 % on rationale; recall ≥ 0.95 on alerts | HITL on disposition; AI advises only | High |
| RM / advisor copilot (drafts responses, summarises relationship, recalls product) | ≤ 2 % advisory | Human approval before send | Medium |
| Complaint and dispute classification | F1 ≥ 0.85 | HITL on classification > regulator threshold | Medium |
| Policy-Q&A copilot (employees ask internal policy questions; cited answers) | ≤ 0.5 % with citations | Trusted reference channel | Medium |
| Credit-decisioning copilot (assembles case, recommends, never decides) | Recommend only | HITL strict; AI cannot approve / decline | High |
| Fraud signal explanation (post-hoc explain a fraud score) | Explanatory only | No decisioning authority | Medium |
| Reg-reporting drafting assistance | ≤ 0.5 % on figures; ≥ 95 % citation | HITL by named officer | High |

## Regulator Stance

Primary regulators across the agency's likely footprint:
- **Kenya**: CBK; Capital Markets Authority; Retirement Benefits Authority; SASRA; ODPC.
- **Uganda**: BoU; CMA; IRA; URBRA; PDPO.
- **Tanzania**: BOT; CMSA; SSRA.
- **Rwanda**: NBR; CMA; NCSA; NCDP.
- **Nigeria**: CBN; SEC; NAICOM; NDPC.
- **South Africa**: SARB / PA; FSCA; Information Regulator.
- **Cross-border / international**: Basel III / IV; SR 11-7-style model-risk management for groups with US footprint; BCBS 239; FATF; PCI DSS for cards.

Vertical-specific AI exposure:
- **Model-risk management** — most regulators expect a model inventory, independent validation, ongoing monitoring, and governance, regardless of whether AI is "in scope" of their explicit AI guidance. Use the model-risk vocabulary in the proposal even when the regulator has not published AI-specific rules.
- **Algorithmic-decisioning** — credit, insurance underwriting, fraud, AML: regulators are sensitive to fairness, explainability, and the right to human review.
- **Sanctions and watchlists** — recall-prioritised; false negatives are catastrophic.
- **Conduct-of-business** — customer-facing AI must not mis-advise; regulator-driven complaints follow.

## Discriminators for FS Bids

1. **Model-Risk Management overlay** — proposal explicitly maps controls to SR 11-7 / Basel-style governance: model inventory, independent validation cadence, ongoing monitoring, governance.
2. **HITL strict on decisioning** — the AI never approves or declines credit / fraud / AML alerts; the AI assembles the case and recommends. Named human authority signs.
3. **Citation grounding on policy-Q&A** — every advisory output cites the policy paragraph; auditor can trace.
4. **Region routing and sovereign-AI option** — for regulators sensitive to cross-border data flows on customer information.
5. **Audit access to logs** — regulator and internal audit can audit prompt / completion / decision logs without breaking sub-processor confidentiality.

## Risk Framing — FS-Specific Language

- "Model risk" (not "AI quality").
- "Independent model validation" (not "we test the model").
- "Adverse-decisioning rights" (not "user override").
- "Sanctions list freshness SLA" (not "we update the list").
- "Suspicious-activity escalation path" for AML cases.
- "Conduct-of-business risk" for customer-facing AI.

## Sample Vertical Paragraph for the Executive Summary

> Our AI-on-SaaS practice in financial services treats every customer-facing or decision-supporting AI feature as a model under model-risk management. The AI inventory is maintained alongside the existing model registry. Independent validation runs on a regulator-acceptable cadence. The human-in-the-loop design names the authority on every decisioning flow, and the AI never approves or declines on its own. Policy-Q&A copilots cite the policy paragraph so that an auditor or supervisor can trace every advisory output back to a controlled source. Where the regulator is sensitive to cross-border data, region routing keeps inference inside the supervisory jurisdiction, with a sovereign-AI option available for the most sensitive tenants.

## Cross-References

- `vertical-saas-positioning-financial-services.md` — base FS SaaS positioning.
- `ai-on-saas-risk-register-for-proposals.md` — R-AI-FS-01 entry.
- `ai-on-saas-responsible-ai-commitment.md` — commitment mapped to FS regulators.
- `ai-on-saas-trust-and-compliance-section-template.md` — FS rows in the compliance map.
