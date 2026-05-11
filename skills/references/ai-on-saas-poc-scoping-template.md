# AI-on-SaaS POC Scoping Template

Template for an AI POC or pilot inside a multi-tenant SaaS, with binary eval criteria, golden-set design, model selection, hallucination ceiling, abstain logic, and exit gates. Pairs with `ai-on-saas-poc-and-pilot-scoping`.

## POC Charter — One Page

- **Workflow**: [named workflow, e.g. "RM responds to retail-banking customer enquiry by drafting a reply"].
- **User persona**: [named role, e.g. "relationship manager, retail branch network"].
- **Production decision this POC enables**: [single sentence, e.g. "decision to roll RM copilot to the 1 200-RM population at Pro-tier price"].
- **Binary go / no-go question**: [single question, e.g. "Does the RM copilot achieve precision ≥ 0.85 and hallucination ≤ 2 % on the golden set, with abstain-correctness ≥ 0.95, at cost-per-call ≤ $0.05?"].
- **Time-box**: [6–12 weeks].
- **Fee**: [defined; non-contingent].
- **What happens on pass**: [enter the Combined Methodology Phase 2 onward].
- **What happens on fail**: [evidence pack handed back; structured option to extend, pivot, or close].

## Golden Dataset Specification

| Item | Detail |
|---|---|
| Size | 100–500 representative cases for an initial POC |
| Sourcing | Production extracts (anonymised), human-authored adversarial cases, regulator-authored test cases |
| Distribution | Representative of production: language mix, channel mix, sentiment, edge cases |
| Adversarial subset | Prompt injection, edge-of-policy, multilingual, regulator-sensitive, ambiguous |
| Labelling owner | Named buyer-side SME |
| Sign-off owner | Named buyer-side SteerCo member |
| Refresh cadence in POC | Mid-point top-up of 10 % cases |
| Versioning | Git-tagged; tie eval results to golden-set version |

## Eval Metrics — Sample Threshold Table

| Metric | Definition | Threshold | Measurement |
|---|---|---|---|
| Precision | Correct-positive / (correct-positive + false-positive) | ≥ 0.85 | LLM-as-judge + human review on 20 % sample |
| Recall | Correct-positive / (correct-positive + false-negative) | ≥ 0.80 | Same as above |
| Citation accuracy | Citations point to a passage that supports the claim | ≥ 0.90 | Human-review on 30 % sample |
| Hallucination rate | Outputs containing unsupported factual claims | ≤ 2 % | Human-review on 30 % sample |
| Abstain-correctness | On the should-abstain subset, the system abstained | ≥ 0.95 | Constructed should-abstain subset |
| p95 latency | 95th-percentile end-to-end latency | ≤ 3 000 ms | Synthetic load + production trace |
| Cost-per-call | Tokens-in + tokens-out at vendor list price | ≤ $0.05 | Telemetry |
| Tenant isolation | No cross-tenant data leak across N adversarial probes | 0 leaks | Red-team probe pack |

All thresholds must pass for production exit. Partial pass = pilot extension, not exit.

## Hallucination Ceiling and Abstain Logic

- **Ceiling**: ≤ 2 % hallucination on the production-representative golden set.
- **Abstain behaviour**: when retrieved-context confidence is below the threshold, the system returns "I do not have sufficient information to answer that. Please [escalate to specialist / consult source X / contact desk]." It does **not** generate a best-guess answer.
- **Abstain-correctness**: a separate metric — on the should-abstain subset, the system must abstain. False auto-answer on should-abstain is treated as a hallucination event.
- **Disclaimer**: the UX disclaimer is a complement, not a substitute, for engineered abstain.

## Model Selection Matrix

| Model | Eval score | p95 latency | Cost/call | Region | Training-data posture | Score |
|---|---|---|---|---|---|---|
| Model A (Claude Sonnet) | 0.89 | 2 400 ms | $0.049 | EU + US | Zero retention, no training | 9 / 10 |
| Model B (GPT-4o) | 0.88 | 2 100 ms | $0.052 | EU + US | Zero retention via API, no training opt-out by default — confirmed for this engagement | 8 / 10 |
| Model C (Llama self-hosted) | 0.79 | 1 800 ms | $0.018 | Sovereign | Full control | 7 / 10 |
| Model D (Gemini) | 0.84 | 2 600 ms | $0.043 | EU | Confirmed for this engagement | 7 / 10 |

The POC tests at least two models against the same golden set, so the production architecture remains model-agnostic. The model-gateway architecture must be present even in POC.

## Tenant Isolation in POC

Even at POC stage:
- RAG indexes per tenant (or per regulator class), not a single index across all POC tenants.
- Prompt context carries tenant identity explicitly.
- Eval cohorts respect tenant boundaries.
- Cross-tenant adversarial probes (5 minimum) confirm isolation.

## Time-Box and Gates

| Week | Milestone | Decision |
|---|---|---|
| 0–1 | Kickoff, golden-set assembly begins | — |
| 2 | Golden-set v0 signed off; model selection narrowed to two | Continue / pause |
| 3–5 | First eval round on both models; abstain logic implemented | — |
| 6 | Mid-point gate — eval ≥ 80 % of threshold or pivot | **Continue / Pivot / Abort** |
| 7–9 | Iteration; second eval round; red-team probe pack | — |
| 10 | Tenant-isolation probe; cost-per-call confirmed at production volume profile | — |
| 11 | Eval rerun on final model; production-readiness pack assembled | — |
| 12 | Exit gate review; signed exit-to-production decision | **Exit / Extend / Abort** |

## Exit-to-Production Gate Criteria

All five must pass:

1. **Eval thresholds** — all metrics at or above threshold on the final golden-set version.
2. **Abstain logic** — abstain-correctness ≥ 0.95 on the should-abstain subset.
3. **Red-team pass** — zero critical findings on the red-team probe pack (prompt injection, jailbreak, data exfiltration, sensitive-output).
4. **Cost-per-call** — within target at production volume profile.
5. **Tenant isolation** — zero leaks on adversarial probes.

Plus: **buyer SteerCo sign-off** on the production exit.

## Abort Gate Criteria

Trigger an abort if any of the following occurs by week 8:

- Eval below 70 % of threshold and trajectory flat.
- Red-team uncovers a class of vulnerability that requires architectural change.
- Cost-per-call > 2 × target with no path to reduce.
- Buyer-side data access blocked beyond the time-box.

Abort fee structure: the agency invoices the time-and-materials consumed up to the abort decision plus a defined abort fee covering team release; the buyer receives the full evidence pack (golden set, eval results, model matrix, red-team findings, architecture notes, recommended pivots).

## POC Proposal Section — Sample Skeleton

1. POC Scope — workflow, user, decision, binary question.
2. Time-box and gates.
3. Golden dataset and acceptance criteria.
4. Eval metrics and thresholds.
5. Model selection and gateway architecture (POC scope).
6. Tenant isolation in POC.
7. Hallucination ceiling and abstain logic.
8. Red-team probe pack.
9. Cost-per-call calculation and target.
10. Exit-to-production criteria.
11. Abort criteria and abort fee.
12. Deliverables and what the buyer keeps.
13. Fee, time-box, and assumptions.

## Cross-References

- `ai-on-saas-metrics-glossary.md` — metric definitions.
- `ai-on-saas-methodology-blocks.md` — production methodology after exit.
- `ai-on-saas-risk-register-for-proposals.md` — risk consistency.
- `saas-poc-scoping-template.md` — base SaaS POC template.
