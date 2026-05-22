---
name: ai-on-saas-procurement-and-questionnaire
description: Use when responding to a client's AI procurement questionnaire inside an AI-on-SaaS bid, or when the proposal must pre-empt the AI questionnaire with a procurement-grade answer pack. Covers model providers, sub-processor list, training-data exclusion, customer-data-in-training opt-out, retention, deletion language, region routing, and sovereign-AI options. Extends `saas-procurement-and-security-questionnaire` with the AI questionnaire pack.
---

# AI-on-SaaS Procurement and Questionnaire
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The buyer has issued an AI-specific procurement questionnaire (or a SaaS questionnaire with an AI annex).
- The agency wants to pre-empt the questionnaire with a procurement-grade answer pack inside the proposal.
- The bid is in a regulated vertical, an AI-Act jurisdiction, or a public-sector procurement.
- The buyer's CISO, DPO, or procurement team is the deciding evaluator.

## Do Not Use When

- The procurement questionnaire is non-AI (use `saas-procurement-and-security-questionnaire`).
- There is no procurement scrutiny (small private buyer, no regulator) — though the discipline is still recommended.

## Required Inputs

- The buyer's questionnaire (if issued).
- The compliance credentials posture from `ai-on-saas-compliance-credentials`.
- The model-provider list and contractual posture (sub-processor list).
- The retention, deletion, training-opt-out, region-routing capabilities.

## Workflow

1. Read the questionnaire. Categorise each question into one of the eight AI procurement domains (below). For each domain the agency has a pre-prepared answer pack, tuned per bid.
2. Where the questionnaire skips a domain, **add it as a volunteered answer** — procurement teams reward proactivity and penalise silence on items they will ask later.
3. Where the questionnaire asks a question the agency cannot answer affirmatively, give the **honest staged answer**: today / in-progress with date / committed for this engagement / out of scope with rationale. Do not fabricate.
4. Cross-link every answer to the methodology and the risk register so the answer is internally consistent.
5. Output the **AI Questionnaire Response Pack** as either a standalone document or an annex to the Trust and Compliance section.

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

- "Our AI providers comply with all applicable laws."
- "Customer data is never used for training" with no contractual basis.
- "Industry-standard retention" instead of a number.
- "Data is stored in secure regions" instead of named regions per data class.
- "Sovereign-AI available on request" with no architecture description.
- "We monitor for hallucinations" with no SLO.
- Answers internally inconsistent with the risk register or compliance credentials.

## Outputs

- AI Questionnaire Response Pack — eight-domain answer pack, drop-in ready.
- Sub-Processor Disclosure table.
- Region-Routing Matrix per data class.
- Training-Data Posture statement per provider.
- Retention and Deletion table.

## Agent Overlay

For agentic engagements, the answer pack extends from eight to **ten domains** by adding **autonomy level and action scope** (per-action-class autonomy commitment; published action catalogue; reversibility classification) and **irreversibility gating, kill-switch and drill, multi-agent governance**. Sub-processor disclosure expands to tool-call APIs alongside model providers. Load `../ai-agent-procurement-and-questionnaire/SKILL.md` for the agent procurement answer pack.

## References

- `../references/ai-on-saas-procurement-questionnaire-pack.md` — long-form answer pack with sample language.
- `../references/saas-procurement-and-security-questionnaire-playbook.md` — base SaaS questionnaire pack.
- `../references/ai-on-saas-trust-and-compliance-section-template.md` — trust section consistency.
- `../saas-procurement-and-security-questionnaire/SKILL.md` — base SaaS procurement skill.
- `../ai-on-saas-compliance-credentials/SKILL.md` — credentials that match the answers.
- `../ai-on-saas-risk-and-responsible-ai/SKILL.md` — risk register consistency.
