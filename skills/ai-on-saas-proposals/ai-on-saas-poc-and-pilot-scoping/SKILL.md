---
name: ai-on-saas-poc-and-pilot-scoping
description: Use when an AI feature inside SaaS needs a time-boxed POC or pilot with a golden dataset, measurable evaluation thresholds, abstention rules, and a production decision gate; use the SaaS pilot skill for non-AI trials.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI-on-SaaS POC and Pilot Scoping
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The buyer wants an AI POC before committing to a full AI-on-SaaS build.
- The agency proposes a paid AI discovery / feasibility study as a Phase 0.
- The pilot must produce evidence the buyer's CTO, CISO, and regulator can act on.
- The buyer has been burned by AI POCs that "demoed well" but failed in production.

## Do Not Use When

- The POC is for a non-AI SaaS feature (use `saas-poc-and-pilot-scoping`).
- The engagement is a fee-for-service AI consult with no production exit (use `ai-transformation-proposal`).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The candidate AI use case (named workflow, named user, named volume). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Access to or assembly plan for the golden dataset. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The hallucination tolerance per use case. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The eval metric(s) the buyer's domain accepts (precision, recall, F1, citation accuracy, exact-match, judge-graded usefulness). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The model-provider posture (single, multi, sovereign). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The time-box the buyer accepts (typically 6–12 weeks). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

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


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

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

- POC scope of "explore AI for the business." **Fix:** Limit the POC to named users, workflow, tenants, data, hypotheses, measures, duration, exclusions, and decision owner.
- "We will evaluate the model" with no metric or threshold. **Fix:** Set evaluation metrics, thresholds, confidence rules, failure cases, and buyer sign-off before build begins.
- Golden set assembled after the POC starts. **Fix:** Freeze a representative, governed golden set before model work and reserve a blind test subset.
- Hallucination addressed as a UX disclaimer. **Fix:** Engineer grounding, abstention, escalation, and a measurable hallucination ceiling into acceptance.
- Single model evaluated; lock-in baked into the production architecture. **Fix:** Evaluate at least one viable fallback and prove the gateway, portability, or documented exit path.
- POC ignores tenant isolation; the evidence does not transfer. **Fix:** Use production-representative tenant boundaries and cross-tenant tests so pilot evidence transfers safely.
- POC extends repeatedly without an abort gate. **Fix:** Set one time-box, budget ceiling, evidence review, abort condition, and written extension authority.
- Production exit on partial pass without the buyer's explicit sign-off. **Fix:** Require all blocking thresholds and explicit buyer sign-off; route partial results to remediation or stop.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| POC Charter (one page). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Golden Dataset Specification. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Eval Metric and Threshold Table. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Hallucination Ceiling and Abstain Logic Specification. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Model Selection Matrix (≥ 2 models scored). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Tenant Isolation in POC Note. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Time-Box and Gates Plan. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Exit-to-Production Gate Criteria. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Abort Gate Criteria with fee. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| POC Proposal Section. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## Agent Overlay

For agentic engagements, the pilot is staged in **three modes** rather than a single POC: **Shadow** (agent proposes, does not act; agreement rate measured), **Supervised** (agent acts on reversibles, humans confirm irreversibles; intervention SLA measured), and **Agentic** (agent acts on reversibles without confirmation; irreversibles remain HITL). Binary thresholds gate each stage. Production exit requires zero irreversibility incidents cumulative, two passed kill-switch drills, full agent red-team pass, and audit-log completeness verified. Load `../ai-agent-poc-and-pilot-scoping/SKILL.md` for the agent pilot template.

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
| Success threshold | Set the metric, dataset, owner, deadline, and production exit rule before work starts | Open-ended pilot or subjective acceptance |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

Define the pilot time box, task set, quality and safety thresholds, intervention rule, cost ceiling, and abort/refund trigger before quoting an AI pilot fee.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/ai-on-saas-poc-scoping-template.md](../../profiles-sectors/references/ai-on-saas-poc-scoping-template.md) — full template with worked examples.
- [../references/ai-on-saas-metrics-glossary.md](../../profiles-sectors/references/ai-on-saas-metrics-glossary.md) — eval, hallucination, abstain, citation, latency definitions.
- [../references/saas-poc-scoping-template.md](../../profiles-sectors/references/saas-poc-scoping-template.md) — base SaaS POC template.
- [../saas-poc-and-pilot-scoping/SKILL.md](../../saas-proposals/saas-poc-and-pilot-scoping/SKILL.md) — base SaaS POC skill.
- [../ai-on-saas-combined-methodology/SKILL.md](../ai-on-saas-combined-methodology/SKILL.md) — production methodology after POC pass.
- [../ai-on-saas-discovery-and-qualification/SKILL.md](../ai-on-saas-discovery-and-qualification/SKILL.md) — discovery that scopes the POC.
- [../ai-on-saas-risk-and-responsible-ai/SKILL.md](../ai-on-saas-risk-and-responsible-ai/SKILL.md) — risk register entries.
