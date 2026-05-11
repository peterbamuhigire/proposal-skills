# AI-on-SaaS Discovery Question Bank

Long-form discovery question bank for engagements that will build AI features (RAG, copilots, agents, AI analytics, AI-assisted decisioning, generation) into a multi-tenant SaaS product. Pairs with `ai-on-saas-discovery-and-qualification` and extends `saas-discovery-question-bank.md`.

Use these questions in discovery calls, written discovery memos, paid AI-discovery workshops, and the Understanding-of-Assignment section of the proposal. Capture answers in `BRIEF.md`. Missing answers are gaps, not assumptions.

## 1. Workflow-AI Fit

- Walk us through the workflow the AI feature is meant to support. Who performs it today? At what step does AI come in?
- How many times per day, per week, per month does this workflow run? Per tenant? In total?
- How long does the workflow take today, end-to-end, in the median case and the 95th-percentile case?
- What is the baseline error rate today? How is "error" defined and detected?
- Is the AI meant to augment a human, replace a step, or enable a workflow that does not exist today? In each case, who agrees to the framing, and how will it be communicated to the users?
- Are there workflow steps where AI must not be used (regulator forbids, contract forbids, ethics forbids)?
- What is the upstream input quality the AI depends on? What does the AI do if upstream input is broken?

## 2. Data Readiness for AI

- Where is the source data located? Which systems, which databases, which file shares?
- Quality, completeness, freshness, language, currency, format (structured, unstructured, scanned, handwritten).
- Is the data **per tenant** with strict isolation, or **shared** across tenants with logical separation?
- Are there licensing constraints on the data (third-party content, customer-owned content, regulator-controlled content)?
- Is there a **golden dataset** for evaluation? If not, who would label one and on what timeline?
- Adversarial cases: prompt injection examples, edge-of-policy cases, multilingual cases, regulator-sensitive cases.
- What is the deletion path when a tenant exits — embeddings, RAG indexes, eval logs, prompt logs?

## 3. Hallucination Tolerance

- If the AI is wrong, what is the worst plausible consequence? Annoyance, rework, customer harm, regulatory breach, financial loss, reputational crisis.
- What is the **acceptable hallucination ceiling** in this use case (expressed as a rate, e.g. ≤ 2 % on a defined golden set)?
- What **abstain** behaviour does the buyer prefer when confidence is low? Refuse, escalate, downgrade to non-AI path, ask the user.
- Are **citations** required? On what evidence (source document, paragraph, page, line)?
- Does the buyer accept **judge-graded** evaluation, or only **exact-match** evaluation?
- Who signs off the hallucination ceiling on the buyer side?

## 4. AI Maturity

- Has the buyer's organisation used AI in production before? In what form (internal tool, vendor tool, copilot)?
- Is there an AI governance forum, AI policy, or AI ethics board? Who chairs? Who decides? How often?
- Is there an eval discipline today? Who owns it? What metrics?
- Does the CISO maintain an AI sub-processor list?
- Is there a Responsible-AI commitment? Where is it published?
- Has there been an AI incident, near-miss, or regulator inquiry?

## 5. Change-Readiness for AI

- How will the affected users react to the AI feature? Threatened, neutral, eager.
- Has the buyer communicated AI plans internally? Externally?
- Is union, works-council, or staff-association consultation required before AI features go to users?
- Is regulator notification required before launch?
- What is the public **augment-vs-replace** framing the buyer will use?
- What support is the buyer willing to fund: training, shadow mode, HITL design, ongoing trust-building.

## 6. Regulator Exposure

- Which AI regulator(s) apply? EU AI Act (which tier?), Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U guidance, Rwanda AI Policy, EAC, sectoral.
- Is this an **AI Act high-risk system**? If so, is the conformity assessment in scope?
- Are there sectoral AI rules (financial-services model-risk management, healthcare clinical-decision support, education student-data, public-sector procurement)?
- Is **sovereign-AI** a requirement (on-prem inference, in-country hosting, government-controlled keys)?
- What is the buyer's regulator-notification cadence? Annual filing, pre-launch notification, ad-hoc inquiry response.

## 7. Model-Provider Posture

- Single provider acceptable, multi-provider required, or sovereign-only?
- Is **training-data exclusion** a hard requirement (customer data must not train provider models)?
- Is **region routing** required (EU data routed to EU inference; KE data routed to KE / ZA)?
- What is the **fallback** model if the primary is unavailable, banned, or price-shocked?
- Does the buyer require a model gateway with model-agnosticism, or accept a single-provider build?
- Open-weight model acceptable? On-prem inference acceptable? GPU sourcing?

## 8. Tenant Variation

- Do tenants share the AI feature behaviour, or does each tenant need its own RAG index, prompt set, eval set?
- Is **per-tenant model selection** a tier feature?
- Is **per-tenant fine-tuning** in scope, or is in-context RAG sufficient?
- Is the eval cohort per tenant, per regulator, or per use case?
- Does the buyer support **bring-your-own-model** for very large enterprise tenants?

## 9. Commercial and Pricing

- How does the buyer want to price AI features today — bundled, tier-gated, usage credits, hybrid?
- What is the buyer's tolerance for variable bills?
- Are there incumbent AI vendors whose pricing the buyer references?
- What is the FX exposure if revenue is local and model costs are USD?
- What is the buyer's hypothesis on AI-tier upsell — attach rate, price, churn impact?

## 10. Operations and Maintenance

- Who operates the AI plane after go-live — agency, buyer, or a joint operating model?
- What is the on-call expectation for eval drift, hallucination spikes, model-provider incidents?
- What is the refresh cadence for golden datasets, prompts, models, RAG indexes?
- What is the runbook for an AI incident (hallucination liability event, prompt-injection breach, data leakage)?
- Who signs off model updates?

## How to Use This Bank in Discovery

- Run a structured one- to two-hour AI-discovery workshop with the buyer's product owner, CTO, CISO, DPO, sponsor, and a representative user.
- Capture answers in a discovery memo, with the gaps explicitly listed.
- Score the engagement on the **AI-on-SaaS Qualification Scorecard** (`ai-on-saas-discovery-and-qualification`).
- Decide: full proposal, paid AI discovery, joint feasibility study, polite decline.
- Carry the **Discovery Findings** paragraph into Understanding-of-Assignment so the evaluator sees the audit trail.
