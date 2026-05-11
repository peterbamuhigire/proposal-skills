---
name: ai-on-saas-poc-and-pilot-scoping
description: Use when scoping an AI proof-of-concept or pilot inside an AI-on-SaaS engagement. Provides binary eval-metric success criteria, golden dataset definition, model selection criteria, hallucination ceiling, abstain logic, exit-to-production gates, and time-box rules that protect both sides. Extends `saas-poc-and-pilot-scoping` with AI-specific acceptance criteria.
---

# AI-on-SaaS POC and Pilot Scoping
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The buyer wants an AI POC before committing to a full AI-on-SaaS build.
- The agency proposes a paid AI discovery / feasibility study as a Phase 0.
- The pilot must produce evidence the buyer's CTO, CISO, and regulator can act on.
- The buyer has been burned by AI POCs that "demoed well" but failed in production.

## Do Not Use When

- The POC is for a non-AI SaaS feature (use `saas-poc-and-pilot-scoping`).
- The engagement is a fee-for-service AI consult with no production exit (use `ai-transformation-proposal`).

## Required Inputs

- The candidate AI use case (named workflow, named user, named volume).
- Access to or assembly plan for the golden dataset.
- The hallucination tolerance per use case.
- The eval metric(s) the buyer's domain accepts (precision, recall, F1, citation accuracy, exact-match, judge-graded usefulness).
- The model-provider posture (single, multi, sovereign).
- The time-box the buyer accepts (typically 6–12 weeks).

## Workflow

1. Write the **POC Charter** in one page: one workflow, one user persona, one production decision the POC enables, one binary go / no-go question.
2. Define the **Golden Dataset**: size (typically 100–500 representative cases for an initial POC), source, labelling rule, labelling owner, sign-off owner. Capture intentional adversarial cases (prompt injection, edge-of-policy, multilingual, regulator-sensitive).
3. Define the **Eval Metric(s)** with numeric thresholds: e.g. precision ≥ 0.85 on the golden set; citation accuracy ≥ 0.90; hallucination rate ≤ 2 %; abstain-correctness ≥ 0.95 on the should-abstain subset; p95 latency ≤ 3 s; cost-per-call ≤ $0.04.
4. Define the **Hallucination Ceiling and Abstain Logic**: what the system does when confidence is below threshold (refuse, escalate, downgrade). This is a system behaviour, not a UX disclaimer.
5. Define the **Model Selection Criteria**: which models are evaluated, on what dimensions (eval score, cost, latency, region availability, training-data posture, ban risk). The POC tests at least two models so the production architecture is model-agnostic.
6. Define the **Tenant Isolation in POC**: even in POC, RAG indexes and prompt context respect tenant boundaries — POCs that ignore tenant isolation produce evidence that does not transfer to production.
7. Define the **Time-Box** (6–12 weeks typical) with weekly check-ins and a single mid-point gate (continue / pivot / abort).
8. Define the **Exit Criteria — Production Gate**: golden-set thresholds met **and** abstain logic verified **and** red-team pass **and** cost-per-call within target **and** tenant isolation verified **and** evaluator sign-off. All five must pass; partial pass is a "pilot extension," not a production exit.
9. Define the **Exit Criteria — Abort Gate**: which metric breach triggers a polite abort, with the abort fee and the evidence pack handed back to the buyer.
10. Write the **POC Proposal Section** (scope, success criteria, exclusions, deliverables, fee, time-box, exit gates, what happens after pass / after fail).

## Quality Standards

- One workflow, one user, one decision per POC.
- Eval metrics are numeric and binary; no "AI quality is good."
- Golden set is sized, sourced, labelled, and signed off before model work starts.
- Hallucination ceiling is paired with abstain logic, not a disclaimer.
- At least two models are evaluated against the same golden set.
- Tenant isolation is respected in POC.
- Exit gates are all-or-nothing for production exit.
- Abort gate is named with a fee structure, not buried.

## Anti-Patterns

- POC scope of "explore AI for the business."
- "We will evaluate the model" with no metric or threshold.
- Golden set assembled after the POC starts.
- Hallucination addressed as a UX disclaimer.
- Single model evaluated; lock-in baked into the production architecture.
- POC ignores tenant isolation; the evidence does not transfer.
- POC extends repeatedly without an abort gate.
- Production exit on partial pass without the buyer's explicit sign-off.

## Outputs

- POC Charter (one page).
- Golden Dataset Specification.
- Eval Metric and Threshold Table.
- Hallucination Ceiling and Abstain Logic Specification.
- Model Selection Matrix (≥ 2 models scored).
- Tenant Isolation in POC Note.
- Time-Box and Gates Plan.
- Exit-to-Production Gate Criteria.
- Abort Gate Criteria with fee.
- POC Proposal Section.

## References

- `../references/ai-on-saas-poc-scoping-template.md` — full template with worked examples.
- `../references/ai-on-saas-metrics-glossary.md` — eval, hallucination, abstain, citation, latency definitions.
- `../references/saas-poc-scoping-template.md` — base SaaS POC template.
- `../saas-poc-and-pilot-scoping/SKILL.md` — base SaaS POC skill.
- `../ai-on-saas-combined-methodology/SKILL.md` — production methodology after POC pass.
- `../ai-on-saas-discovery-and-qualification/SKILL.md` — discovery that scopes the POC.
- `../ai-on-saas-risk-and-responsible-ai/SKILL.md` — risk register entries.
