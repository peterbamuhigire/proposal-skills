# AI-on-SaaS Metrics Glossary

Glossary of metrics used across AI-on-SaaS proposals — eval, hallucination, abstain, citation, latency, cost, drift, adoption, redress. Use the exact definitions below in the proposal so that evaluators read consistent language across methodology, business case, risk register, and procurement answers.

## Eval Metrics

**Precision** — Of the AI's positive predictions, the proportion that are correct. TP ÷ (TP + FP). Sensitive to false positives. Use when the cost of a false positive is high (e.g. flagging a customer as fraudulent).

**Recall (Sensitivity)** — Of the actual positives, the proportion the AI caught. TP ÷ (TP + FN). Sensitive to false negatives. Use when the cost of missing a positive is high (e.g. missing a sanctions match).

**F1 Score** — Harmonic mean of precision and recall. 2 × (P × R) ÷ (P + R). Use when precision and recall are equally important.

**Exact-Match Accuracy** — Proportion of outputs that exactly match the reference. Use for structured outputs (entity extraction, classification).

**Judge-Graded Usefulness** — Proportion of outputs an evaluation judge (LLM or human) rates as "useful." Define the rubric. Use for generative outputs where exact-match is too strict.

**Citation Accuracy** — Proportion of cited passages that actually support the claim made. Measured by human review or strict LLM-as-judge. Distinguished from hallucination: an output can be hallucination-free and citation-inaccurate.

**Cohort F1** — F1 computed per cohort (gender, language, age band, region). Used for fairness measurement.

## Hallucination and Abstain Metrics

**Hallucination Rate** — Proportion of outputs containing unsupported factual claims. Measured on an evaluation cohort representative of production. Method: human review of a 2–5 % production sample plus LLM-as-judge on 100 %.

**Abstain Rate** — Proportion of incoming cases on which the system abstained.

**Abstain-Correctness (Should-Abstain Precision)** — Of the system's abstain decisions, the proportion that were correct (the case should have been abstained). High abstain-correctness indicates calibrated confidence.

**Should-Abstain Recall** — Of the cases that should have been abstained, the proportion the system actually abstained on. High recall indicates the system catches the cases it should not answer.

**False-Auto-Answer Rate** — On the should-abstain subset, the proportion the system answered automatically. Treat as a hallucination event.

## Latency Metrics

**Time-to-First-Token (TTFT)** — Latency from request to first token streaming back. Used for streaming UX experience.

**Time-to-Last-Token (TTLT)** — Total inference time. Used for batch or non-streaming flows.

**p50 / p95 / p99 Latency** — Median / 95th / 99th percentile latency. Use p95 or p99 in SLOs; p50 misleads.

## Cost Metrics

**Cost-per-Call** — Tokens-in × token-in price + tokens-out × token-out price + embedding cost + ancillary (vector store, gateway overhead). Computed at vendor list price.

**Cost-per-Case** — Cost-per-call × calls per case. Includes RAG retrieval calls, synthesis calls, and tool-calls.

**Cost-per-Tenant at P50 / P90 / P99** — Cost-per-case × cases per tenant per month, at the 50th / 90th / 99th percentile tenant. P99 drives fair-use design.

**Eval-Margin** — Annual eval cost ÷ annual gross margin contribution of the AI feature. Target ≤ 15 %.

**Token Burn Rate** — Tokens consumed per active tenant per day. Operational metric for capacity planning.

## Drift Metrics

**Eval Drift** — Change in eval score between two consecutive eval refreshes. Triggers AI Governance Forum review if > 5 pp.

**Performance Drift** — Change in p95 latency or cost-per-call over a rolling window. Triggers SRE review if > 20 %.

**Data Drift** — Statistical divergence of production inputs from the golden-set distribution. Use KL divergence or chi-square. Triggers golden-set refresh.

## Tenant-Isolation Metrics

**Cross-Tenant Probe Pass Rate** — Proportion of adversarial probes confirming no cross-tenant data leak. Target 100 %. Below 100 % is a security incident.

**Per-Tenant Eval Pass Rate** — Where per-tenant eval is in use, proportion of tenants meeting threshold. Below 95 % triggers tenant-specific review.

## Adoption Metrics

**Feature Adoption** — Active users on the feature ÷ eligible users. Healthy ≥ 60 % by week 8.

**Active Use Rate** — Active users per period ÷ trained users. Differentiates "used once" from "in flow."

**Override Rate** — Proportion of cases the user overrides the AI. 5–25 % healthy; very low may indicate rubber-stamping; very high indicates trust issues.

**Trust Score** — Survey: "I trust the AI's draft for this workflow" on a 1–7 scale. Trend over time matters more than absolute level.

**Time Saved per Case** — User-reported or measured time delta between pre- and post-AI workflow.

## Redress and Incident Metrics

**Redress Volume** — Number of affected-party complaints logged per period.

**Redress Resolution Time** — Time from complaint logged to resolution per severity.

**AI Incidents per Quarter** — Count of AI-classified incidents (hallucination liability, prompt-injection success, data leakage, sensitive-output, sub-processor incident).

**Time-to-Detect / Time-to-Contain** — Operational incident metrics for the AI incident runbook.

## Composite Metrics for the Proposal Dashboard

| Metric | Frequency | Owner | Healthy band |
|---|---|---|---|
| Hallucination rate | Monthly | Eval Engineer | ≤ ceiling per feature |
| Abstain-correctness | Monthly | Eval Engineer | ≥ 0.95 |
| Cost-per-call | Weekly | MLOps Engineer | Within target |
| Cost-per-tenant P99 | Monthly | MLOps + Commercial | Below licence + overage |
| Eval drift | Per refresh | Eval Engineer | Δ ≤ 5 pp |
| p95 latency | Daily | SRE | ≤ SLO |
| Cross-tenant probe pass | Per probe run | AI Safety | 100 % |
| Feature adoption | Weekly | CS Lead | ≥ 60 % w8 |
| Override rate | Weekly | CS Lead | 5–25 % |
| Trust score | Quarterly | Change Lead | Trend up |
| Redress volume | Monthly | AI Safety | Stable / down |
| AI incidents per quarter | Quarterly | AI Safety | 0 critical |

## Cross-References

- `ai-on-saas-business-case-template.md` — uses cost metrics.
- `ai-on-saas-methodology-blocks.md` — uses eval and drift metrics in acceptance.
- `ai-on-saas-poc-scoping-template.md` — uses eval, hallucination, latency, cost in exit gates.
- `ai-on-saas-trust-and-compliance-section-template.md` — uses eval, hallucination, drift in trust section.
- `saas-metrics-glossary-for-proposals.md` — base SaaS metrics.
