---
name: ai-on-saas-procurement-and-questionnaire
description: Use when an AI-on-SaaS bid must answer or pre-empt procurement questions about model providers, data training, retention, deletion, sub-processors, region routing, and sovereign options; use the SaaS questionnaire skill for non-AI review.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI-on-SaaS Procurement and Questionnaire
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The buyer has issued an AI-specific procurement questionnaire (or a SaaS questionnaire with an AI annex).
- The agency wants to pre-empt the questionnaire with a procurement-grade answer pack inside the proposal.
- The bid is in a regulated vertical, an AI-Act jurisdiction, or a public-sector procurement.
- The buyer's CISO, DPO, or procurement team is the deciding evaluator.

## Do Not Use When

- The procurement questionnaire is non-AI (use `saas-procurement-and-security-questionnaire`).
- There is no procurement scrutiny (small private buyer, no regulator) — though the discipline is still recommended.

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The buyer's questionnaire (if issued). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The compliance credentials posture from `ai-on-saas-compliance-credentials`. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The model-provider list and contractual posture (sub-processor list). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The retention, deletion, training-opt-out, region-routing capabilities. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Read the questionnaire. Categorise each question into one of the eight AI procurement domains (below). For each domain the agency has a pre-prepared answer pack, tuned per bid.
2. Where the questionnaire skips a domain, **add it as a volunteered answer** — procurement teams reward proactivity and penalise silence on items they will ask later.
3. Where the questionnaire asks a question the agency cannot answer affirmatively, give the **honest staged answer**: today / in-progress with date / committed for this engagement / out of scope with rationale. Do not fabricate.
4. Cross-link every answer to the methodology and the risk register so the answer is internally consistent.
5. Output the **AI Questionnaire Response Pack** as either a standalone document or an annex to the Trust and Compliance section.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## The Eight AI Procurement Domains

### 1. Model Providers and Sub-Processors
- Which model providers are used (named: OpenAI, Anthropic, Google, AWS Bedrock, Azure OpenAI, Mistral, Cohere, open-weight self-hosted)?
- For each: region of inference, retention default, training-opt-out status, contractual notice obligation, fallback.
- Is the sub-processor list published, and how is the buyer notified of changes?

### 2. Training-Data Posture
- Is customer data used to train provider models? Default answer: no, with the contractual basis (provider zero-retention API, training opt-out, BAA where applicable).
- Is customer data used to fine-tune the agency's own models? If yes, scope, opt-in, deletion process.
- Is the eval dataset trained on customer data? If yes, anonymisation, consent, deletion.

### 3. Data Retention and Deletion
- What is retained at the model provider (default: nothing for zero-retention APIs; otherwise N days)?
- What is retained at the agency (prompts, completions, embeddings, eval logs, drift logs) — for how long, for what purpose, deletion process.
- How is a tenant's AI data deleted on exit? Embeddings, RAG indexes, eval logs, prompt logs.

### 4. Region Routing
- Where is inference performed for each tenant's data class (EU data, KE data, NG data, ZA data, US data)?
- What is the fall-back region if the primary is unavailable?
- Can the buyer **pin** a tenant to a region contractually?

### 5. Sovereign-AI / On-Prem
- Is a sovereign-AI / on-prem inference option available?
- Open-weight models supported (Llama, Mistral, Qwen)?
- GPU sourcing, operations, SLA in sovereign deployments.
- Pricing differential against the multi-tenant cloud offering.

### 6. Eval, Hallucination, and Quality
- Eval methodology, golden-dataset description, metric thresholds, refresh cadence.
- Hallucination SLO and measurement.
- Red-team frequency, scope, scorecard.
- Drift watch and alerting.

### 7. Safety, Security, and Abuse
- Prompt-injection defences (input filtering, output filtering, system-prompt hardening, tool allowlist).
- Jailbreak defences and the response runbook.
- Abuse detection (single tenant burst, anomalous prompts).
- AI incident response runbook and disclosure policy.

### 8. Governance, Audit, and Redress
- Responsible-AI commitment (link to commitment section).
- AI governance forum (parties, cadence, decisions).
- Audit access to logs (prompts, completions, eval, drift).
- Redress mechanism for affected users / tenants / regulators.

## Quality Standards

- Every answer is honest, staged, and dated.
- Sub-processor list names providers, not "third-party AI providers."
- Training-data posture is explicit per provider.
- Retention is a number, not "as required by law."
- Region routing is per data class, not a single global statement.
- Sovereign-AI option includes pricing and operations description, not just availability.
- Eval and hallucination answers include thresholds and cadence.
- Governance answer names a role and a forum.

## Anti-Patterns

- "Our AI providers comply with all applicable laws." **Fix:** Answer for each provider with jurisdiction, requirement, control evidence, assurance status, and named gap owner.
- "Customer data is never used for training" with no contractual basis. **Fix:** Quote the governing provider and customer contract terms, configuration, retention, and verified training-data posture.
- "Industry-standard retention" instead of a number. **Fix:** State retention by data class and lifecycle stage, including logs, prompts, outputs, backups, deletion, and exceptions.
- "Data is stored in secure regions" instead of named regions per data class. **Fix:** Name processing and storage regions per data class, provider, tenant option, backup, support access, and failover.
- "Sovereign-AI available on request" with no architecture description. **Fix:** Describe the sovereign deployment boundary, model and infrastructure dependencies, operations, evidence, cost, and limitations.
- "We monitor for hallucinations" with no SLO. **Fix:** Define hallucination metric, cohort, threshold, measurement cadence, alert, escalation, and release or rollback rule.
- Answers internally inconsistent with the risk register or compliance credentials. **Fix:** Reconcile every answer against the risk register, architecture, DPA, provider list, compliance section, and commercial terms.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Questionnaire Response Pack — eight-domain answer pack, drop-in ready. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Sub-Processor Disclosure table. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Region-Routing Matrix per data class. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Training-Data Posture statement per provider. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Retention and Deletion table. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## Agent Overlay

For agentic engagements, the answer pack extends from eight to **ten domains** by adding **autonomy level and action scope** (per-action-class autonomy commitment; published action catalogue; reversibility classification) and **irreversibility gating, kill-switch and drill, multi-agent governance**. Sub-processor disclosure expands to tool-call APIs alongside model providers. Load `../ai-agent-procurement-and-questionnaire/SKILL.md` for the agent procurement answer pack.

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
| Evidence availability | Answer from approved evidence; mark gaps and owners instead of guessing | Unsupported contractual or security assurance |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

If a model provider's retention or training terms are unverified, mark the questionnaire response not assessed, name the evidence owner, and withhold the no-training assurance.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/ai-on-saas-procurement-questionnaire-pack.md](../../profiles-sectors/references/ai-on-saas-procurement-questionnaire-pack.md) — long-form answer pack with sample language.
- [../references/saas-procurement-and-security-questionnaire-playbook.md](../../profiles-sectors/references/saas-procurement-and-security-questionnaire-playbook.md) — base SaaS questionnaire pack.
- [../references/ai-on-saas-trust-and-compliance-section-template.md](../../profiles-sectors/references/ai-on-saas-trust-and-compliance-section-template.md) — trust section consistency.
- [../saas-procurement-and-security-questionnaire/SKILL.md](../../saas-proposals/saas-procurement-and-security-questionnaire/SKILL.md) — base SaaS procurement skill.
- [../ai-on-saas-compliance-credentials/SKILL.md](../ai-on-saas-compliance-credentials/SKILL.md) — credentials that match the answers.
- [../ai-on-saas-risk-and-responsible-ai/SKILL.md](../ai-on-saas-risk-and-responsible-ai/SKILL.md) — risk register consistency.
