# AI-on-SaaS Risk Register for Proposals

Drop-in risk register for AI-on-SaaS engagements, covering ten core risks plus a vertical-and-engagement-specific tail. Pairs with `ai-on-saas-risk-and-responsible-ai` and complements `saas-risk-register-for-proposals.md`.

Format: each entry carries risk name, description, likelihood (L/M/H), impact (L/M/H), trigger, mitigation, owner, escalation. Use the table in `12-risk-analysis` or the equivalent Risk Analysis section of the proposal.

## Core AI-on-SaaS Risks

### R-AI-01 Model Risk (wrong, biased, unstable output)
- **Description**: The model produces outputs that are factually wrong, biased against a protected class, or unstable under small input changes.
- **Likelihood**: M. **Impact**: H.
- **Trigger**: Golden-set pass rate drops > 5 pp; user complaint cluster on a single class; eval-margin red.
- **Mitigation**: Eval harness in CI; drift watch in production; model rollback path; abstain logic; HITL on high-stakes flows.
- **Owner**: AI Safety Lead.
- **Escalation**: SteerCo within 48 hours of trigger; regulator if breach exceeds notification threshold.

### R-AI-02 Hallucination Liability
- **Description**: An untrue output causes user, customer, or third-party harm.
- **Likelihood**: M. **Impact**: H.
- **Trigger**: Hallucination rate > ceiling; harm-event report; legal letter.
- **Mitigation**: Engineered hallucination ceiling; abstain logic; citation grounding; HITL on high-stakes; user-facing disclosure; professional indemnity cover.
- **Owner**: AI Safety Lead.
- **Escalation**: SteerCo + General Counsel.

### R-AI-03 Prompt Injection
- **Description**: A user input, retrieved document, or tool-call response carries adversarial instructions that subvert the system prompt.
- **Likelihood**: H. **Impact**: H.
- **Trigger**: Red-team probe success; production anomaly in prompt logs; sensitive-output incident.
- **Mitigation**: Input filtering; output filtering; system-prompt hardening; tool-call allowlist; document-source filtering; red-team harness; bug-bounty.
- **Owner**: AI Safety Lead + Security Lead.
- **Escalation**: SteerCo + CISO.

### R-AI-04 Data Leakage into Model Providers
- **Description**: Customer data is sent to a model provider and is retained or used to train provider models.
- **Likelihood**: M. **Impact**: H.
- **Trigger**: Provider-side retention setting change; provider breach; provider terms change.
- **Mitigation**: Zero-retention API only; training-data exclusion clauses; region routing; data-minimisation in prompts; sub-processor disclosure; quarterly contract review.
- **Owner**: DPO + AI Safety Lead.
- **Escalation**: SteerCo + Regulator (if PII at scale).

### R-AI-05 Sub-Processor Exposure
- **Description**: A model provider is breached, banned, deprecated, or price-shocked.
- **Likelihood**: M. **Impact**: M.
- **Trigger**: Provider incident notification; sanctions; deprecation notice; price increase > threshold.
- **Mitigation**: Multi-provider gateway; fallback model with eval coverage; contractual notice obligations on the provider; exit plan; price-increase contractual cap.
- **Owner**: ML Lead.
- **Escalation**: SteerCo + Procurement.

### R-AI-06 Regulatory Shift
- **Description**: AI regulator changes tier classification, issues new guidance, or bans a use case in a target market.
- **Likelihood**: M. **Impact**: H.
- **Trigger**: Regulator notice; guidance update; conformity-assessment scope change; ban.
- **Mitigation**: Quarterly regulator scan; conformity-readiness documentation; modular controls; regional fallback; kill-switch for affected use cases.
- **Owner**: AI Safety Lead + Compliance Lead.
- **Escalation**: SteerCo + Regulator liaison.

### R-AI-07 Vendor Lock-In to a Single Model Family
- **Description**: The product cannot operate without one model provider; deprecation or price-shock would be catastrophic.
- **Likelihood**: M. **Impact**: M.
- **Trigger**: Inability to swap models in a stage-gate test.
- **Mitigation**: Model-agnostic gateway from day one; open-weight fallback; eval portability; abstraction in prompt and tool layer.
- **Owner**: ML Lead.
- **Escalation**: SteerCo.

### R-AI-08 Training-Data Contamination
- **Description**: Training data (for fine-tuned or evaluation models) includes prohibited, licensed, or poisoned content.
- **Likelihood**: L–M. **Impact**: H.
- **Trigger**: Audit finding; licensor letter; eval anomalies.
- **Mitigation**: Data lineage; licence audit; content filtering; retraining triggers; pre-deployment provenance check.
- **Owner**: Data Engineer (AI) + Compliance Lead.
- **Escalation**: SteerCo + Legal.

### R-AI-09 Drift (eval, performance, cost)
- **Description**: Production behaviour drifts from POC; eval, latency, or cost-per-call degrades.
- **Likelihood**: H. **Impact**: M.
- **Trigger**: Drift watch alert; SLO breach; monthly eval refresh below threshold.
- **Mitigation**: Drift-watch dashboards; monthly eval refresh; cost-per-call SLO with alerting; auto-rollback to previous model version.
- **Owner**: MLOps Engineer + Eval Engineer.
- **Escalation**: SteerCo if threshold breach lasts > 7 days.

### R-AI-10 Reputational
- **Description**: Public AI incident, regulator action, employee or union pushback damages buyer brand.
- **Likelihood**: M. **Impact**: H.
- **Trigger**: Media coverage; viral incident; staff complaint; regulator press release.
- **Mitigation**: Responsible-AI commitment with transparency; incident communications playbook; redress mechanism; pre-launch union/works-council consultation where applicable.
- **Owner**: AI Safety Lead + Change Lead.
- **Escalation**: SteerCo + Communications.

## Vertical-Specific Tail (illustrative)

### R-AI-FS-01 Model-Risk Management Non-Compliance (Financial Services)
- Trigger: model-risk model inventory gap; regulator examination finding.
- Mitigation: SR 11-7-style governance overlay; model registry; independent model validation cadence.

### R-AI-HC-01 Clinical Decision Support Classification (Healthcare)
- Trigger: regulator reclassifies the AI feature as a medical device.
- Mitigation: Non-diagnostic framing where the regulator demands; explicit out-of-scope statements; pre-market dialogue with regulator.

### R-AI-PS-01 Sovereign-AI Mandate (Public Sector)
- Trigger: ministerial directive on sovereign-AI; procurement-level mandate.
- Mitigation: Sovereign-AI option in roadmap; open-weight model readiness; GPU sourcing readiness; in-country hosting partner.

### R-AI-EDU-01 Minor-Data and Exam-Integrity (Education)
- Trigger: data-protection regulator inquiry on minor data; exam-integrity controversy.
- Mitigation: minor-data handling baseline; consent posture; non-decisioning framing on assessment; integrity-protective UX.

## Tabular Form for Drop-In

| ID | Risk | L | I | Trigger | Mitigation | Owner | Escalation |
|---|---|---|---|---|---|---|---|
| R-AI-01 | Model risk | M | H | Golden-set pass drop > 5 pp | Eval CI, drift watch, rollback, abstain, HITL | AI Safety Lead | SteerCo |
| R-AI-02 | Hallucination liability | M | H | Rate > ceiling | Ceiling, abstain, citation, HITL, PI cover | AI Safety Lead | SteerCo + GC |
| R-AI-03 | Prompt injection | H | H | Red-team success / log anomaly | Filters, allowlist, red-team, bug-bounty | AI Safety + Security | SteerCo + CISO |
| R-AI-04 | Data leakage | M | H | Provider retention change | Zero-retention API, training exclusion, region routing | DPO + AI Safety | SteerCo + Reg |
| R-AI-05 | Sub-processor exposure | M | M | Provider incident | Multi-provider gateway, fallback | ML Lead | SteerCo |
| R-AI-06 | Regulatory shift | M | H | Regulator notice | Quarterly scan, conformity readiness, kill-switch | AI Safety + Compliance | SteerCo |
| R-AI-07 | Vendor lock-in | M | M | Cannot swap in test | Gateway, open-weight fallback, eval portability | ML Lead | SteerCo |
| R-AI-08 | Training-data contamination | L–M | H | Audit / licensor / eval anomaly | Lineage, licence audit, provenance | Data Eng (AI) + Compliance | SteerCo + Legal |
| R-AI-09 | Drift | H | M | Drift alert / SLO breach | Drift watch, monthly refresh, rollback | MLOps + Eval Eng | SteerCo |
| R-AI-10 | Reputational | M | H | Media / staff / regulator | Responsible-AI, incident plan, redress | AI Safety + Change | SteerCo + Comms |

## Cross-References

- `ai-on-saas-responsible-ai-commitment.md` — commitment that makes mitigations visible.
- `ai-on-saas-trust-and-compliance-section-template.md` — trust section consistency.
- `ai-on-saas-procurement-questionnaire-pack.md` — procurement answer consistency.
- `ai-on-saas-methodology-blocks.md` — methodology that anchors mitigations.
- `saas-risk-register-for-proposals.md` — base SaaS risk register.
