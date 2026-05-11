# AI-on-SaaS Trust and Compliance Section Template

Drop-in section template for Trust and Compliance specifically covering AI inside a multi-tenant SaaS. Pairs with `ai-on-saas-compliance-credentials` and extends `saas-trust-and-compliance-section-template.md`. Drops as a subsection of the proposal's main Trust and Compliance section, or stands alone where the buyer requests it.

## Section Skeleton

1. AI Trust Posture (opening paragraph).
2. AI Compliance Map.
3. Model-Card Practice.
4. Eval-Harness-in-CI.
5. Hallucination SLO.
6. Red-Team Practice.
7. AI Sub-Processor Disclosure.
8. Region Routing and Sovereign-AI Options.
9. Cross-references.

## 1. AI Trust Posture — Sample Opening Paragraph

> We deliver AI features inside a multi-tenant SaaS under a Responsible-AI commitment that is engineered, not aspirational. Each AI feature has a named AI Safety Lead, a golden dataset signed off by a Customer subject-matter expert, an eval threshold gated in CI, a hallucination SLO measured monthly, a red-team scorecard refreshed quarterly, a model-card published before launch, and a sub-processor list refreshed at every renewal. Where the use case is high-stakes, a human-in-the-loop design specifies the human's authority, SLA, and escalation. The trust posture is the same in production as it is in this proposal — observable, auditable, and signed.

## 2. AI Compliance Map

| Regulator / standard | Posture | Evidence (or target) |
|---|---|---|
| EU AI Act | Ready for non-high-risk classification; tier assessment included in Phase 1 for high-risk | Tier-assessment doc; conformity readiness pack on request |
| Kenya NCAIS principles | Ready | Principles-to-commitment map (Section 2 of Responsible-AI commitment) |
| Nigeria NAIS | Ready | Principles-to-commitment map |
| South Africa AI policy (draft) | In progress — guidance pending | Quarterly scan; commitment updated on policy publication |
| Uganda NITA-U AI guidance | Ready | Principles-to-commitment map |
| Rwanda AI Policy | Ready | Principles-to-commitment map |
| EAC AI position | Not applicable to this engagement | — |
| Kenya DPA / Nigeria NDPA / Uganda DPPA / Rwanda DPL / POPIA | Ready | DPA in MSA; DPIA per high-risk feature |
| GDPR | Ready for EU-routed tenants | DPA, SCCs, region routing, DPIA |
| ISO 42001 (AI management system) | In progress — target year 2 | Gap pack on request |
| ISO 23894 (AI risk) | Aligned | Mapping document |
| NIST AI RMF | Aligned | Govern / Map / Measure / Manage map |
| Financial-services model-risk management (SR 11-7-style) | Ready where the engagement is FS-vertical | Model registry, independent validation cadence |
| Healthcare clinical decision support classification | Non-diagnostic framing applied | Out-of-scope statement; regulator dialogue plan |

## 3. Model-Card Practice

Each launched AI feature carries a model card containing:

- Feature scope and intended use.
- Out-of-scope uses.
- Model family and version (or model gateway with model list).
- Training-data summary (for any fine-tuned models; for foundation models, provider-published card linked).
- Evaluation summary (golden-set version, metrics, thresholds, last refresh date).
- Limitations and known failure modes.
- Risks and mitigations (link to risk register).
- Contact for redress.
- Card version and last update.

Cards published in a single accessible location (typically the customer trust portal); auditor access on request.

## 4. Eval-Harness-in-CI

- Golden datasets per feature, versioned in git.
- Metric thresholds defined in the engagement Statement of Work; changes require AI Governance Forum approval.
- CI gate: threshold breach blocks deploy to production.
- Drift watch in production: daily for high-stakes features; weekly for others.
- Monthly eval refresh; quarterly golden-set refresh.
- Eval reports retained for the engagement life plus three years; available to auditor on request.

## 5. Hallucination SLO

- **Definition**: rate of outputs containing unsupported factual claims, measured on a constructed evaluation cohort representative of production.
- **Ceiling per feature**: stated numerically (e.g. ≤ 2 % for advisory copilot; ≤ 0.5 % for citation-grounded RAG).
- **Measurement**: monthly human-review of a 2–5 % sample plus LLM-as-judge on 100 %.
- **Alerting**: weekly indicator; threshold breach triggers AI Governance Forum review within 5 business days.
- **Response runbook**: rollback to previous model version; abstain-logic tightening; root-cause review; user-facing disclosure if material.

## 6. Red-Team Practice

- **Scope**: prompt injection, jailbreak, data exfiltration, sensitive-output, tool-misuse.
- **Frequency**: quarterly for production AI features; pre-launch for new features.
- **Scorecard**: number of probes, success rate, severity distribution, remediation cadence.
- **Owner**: AI Safety Lead, supported by an independent red-team partner annually.
- **Bug-bounty**: optional add-on for premium-tier customers.

## 7. AI Sub-Processor Disclosure

The sub-processor list is published in the trust portal and updated at least quarterly. For each provider:

- Name and role (foundation-model inference, embedding, evaluation, vector store, observability).
- Region of inference.
- Retention default.
- Training-data posture (zero-retention API, opt-out, opt-in, BAA).
- Contractual notice obligation on the provider.
- Fall-back provider for the same role.

Customers are notified of material sub-processor changes at least 30 days before effective date, with the right to object per the DPA.

## 8. Region Routing and Sovereign-AI Options

- **Default routing**: per data-residency policy of the buyer's tenants.
- **EU-routed tenants**: inference confined to EU regions.
- **KE / NG / ZA / UG / RW tenants**: inference confined to the customer's chosen region within the available provider footprint; sovereign-AI option for regulated tenants.
- **Sovereign-AI**: open-weight model self-hosted on customer-controlled or in-country infrastructure; pricing differential stated in the financial proposal; SLA stated separately.
- **Region pinning**: contractual option for enterprise and regulated tiers.

## 9. Cross-References Block (for the proposal)

- AI Sub-Processor List — published version.
- DPA, MSA, SLA for AI features.
- DPIA template per high-risk AI feature.
- Incident response runbook for AI events.
- Responsible-AI commitment (section reference).
- Risk register (section reference).

## Cross-References (internal)

- `ai-on-saas-responsible-ai-commitment.md` — commitment that this section makes visible.
- `ai-on-saas-procurement-questionnaire-pack.md` — answers consistent with this section.
- `ai-on-saas-risk-register-for-proposals.md` — risks mapped to mitigations here.
- `saas-trust-and-compliance-section-template.md` — base SaaS trust template.
