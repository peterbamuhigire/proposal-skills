# AI-on-SaaS Procurement Questionnaire Pack

Procurement-grade answer pack covering the eight AI procurement domains. Pairs with `ai-on-saas-procurement-and-questionnaire`. Drop in as an annex to the Trust and Compliance section, or respond directly to a client AI questionnaire.

Every answer below is a **template** with placeholders. Tune per bid. Answers must be honest, staged, and dated; do not fabricate.

## Domain 1 — Model Providers and Sub-Processors

**Q1.1 — Which model providers do you use for this engagement?**
> For this engagement, we use [Provider A, Provider B] for foundation-model inference, [Provider C] for embedding, and [self-hosted open-weight model X] for sovereign-tenant inference. All providers are listed in the published sub-processor list, with role, region, retention, and training posture for each.

**Q1.2 — Will you notify us of sub-processor changes, and on what timeline?**
> We notify the Customer of material sub-processor changes at least thirty days before effective date, in writing, via the trust-portal change-log and direct notification to the named Customer contact. The Customer has the right to object per the DPA; objection triggers a commercial conversation within five business days.

**Q1.3 — Do you maintain a fallback provider for each role?**
> Yes. Our model gateway routes to a fallback provider on primary-provider failure, deprecation, or pricing event. The fallback model is evaluated against the same golden set as the primary, with a separately stated eval score and cost-per-call.

## Domain 2 — Training-Data Posture

**Q2.1 — Is Customer data used to train provider models?**
> No. We use provider zero-retention APIs (or contractual training opt-out, where zero-retention is unavailable for the chosen provider). The contractual basis is named per provider in the sub-processor list. For BAA-relevant providers, the BAA is in place and disclosed.

**Q2.2 — Is Customer data used to fine-tune your own models?**
> [No] / [Yes, only with explicit Customer opt-in and a defined scope, retention, and deletion process. The opt-in is captured in the SoW and revocable on 30 days' notice.]

**Q2.3 — Is the eval dataset trained on Customer data?**
> The eval golden dataset is constructed from [anonymised production extracts, human-authored cases, regulator-authored test cases]. Personally identifiable information is removed at ingestion; the dataset is owned by the Customer and deleted on engagement exit.

## Domain 3 — Data Retention and Deletion

**Q3.1 — What is retained at the model provider?**
> Nothing on zero-retention APIs (the API call body and response are not persisted at the provider beyond the inference window). Where a provider's zero-retention API is unavailable, retention is [N days] as agreed in the sub-processor list.

**Q3.2 — What is retained at the Supplier?**
> Prompts and completions are retained for [30] days for debugging and quality review, then deleted. Eval logs are retained for the engagement life plus three years. Drift-watch metrics are retained for the engagement life. Embeddings and RAG indexes are retained for as long as the underlying source content is in scope, and deleted on Customer instruction.

**Q3.3 — How is a tenant's AI data deleted on exit?**
> On tenant exit, the agency executes the AI-data deletion runbook: RAG indexes purged, embeddings purged, prompt / completion logs purged, eval logs anonymised (or purged if no retention obligation applies), drift-watch metrics anonymised. The runbook is signed off as complete within ten business days. Certificate of deletion provided to the Customer.

## Domain 4 — Region Routing

**Q4.1 — Where is inference performed?**
> Inference is performed in the region matching the tenant's data-residency policy. For [EU] tenants: EU regions only. For [KE / NG / ZA / UG / RW] tenants: the closest available in-region or in-vendor region per the residency matrix in the sub-processor list. Region routing is enforced at the model gateway and audited.

**Q4.2 — Can the Customer pin a tenant to a region contractually?**
> Yes, per the enterprise and regulated tiers. The pinning is recorded in the order form and enforced at the gateway.

**Q4.3 — What is the fall-back region if the primary is unavailable?**
> The fall-back region is named per tenant in the order form. Default is the next-closest region within the same residency boundary. A fall-back is never to a region outside the residency boundary without prior Customer notification.

## Domain 5 — Sovereign-AI / On-Prem

**Q5.1 — Is a sovereign-AI option available?**
> Yes. The sovereign-AI option uses open-weight models (Llama, Mistral, Qwen — current list in the trust portal) hosted on Customer-controlled or in-country sovereign infrastructure. Pricing differential is stated in the financial proposal; SLA is stated separately.

**Q5.2 — What GPU footprint is required?**
> [Sized per the engagement; typically N × H100/A100/L40S equivalent for production workloads; sized down for development environments. Sourcing partners named in the SoW where in-country GPU is required.]

**Q5.3 — What are the SLA implications of the sovereign option?**
> Sovereign deployments have an SLA differential from the multi-tenant cloud option, stated in the SoW. The differential reflects reduced provider redundancy and the operational scope of the in-country infrastructure.

## Domain 6 — Eval, Hallucination, and Quality

**Q6.1 — What is the eval methodology?**
> We operate a golden-dataset eval per AI feature, with numeric thresholds gated in CI. Datasets are versioned in git; thresholds are agreed in the SoW; CI breaches block deploy. Eval is refreshed monthly; the golden set quarterly.

**Q6.2 — What is the hallucination SLO?**
> Hallucination is measured as the rate of outputs containing unsupported factual claims, on a constructed evaluation cohort representative of production. The ceiling per feature is stated numerically in the SoW (typically ≤ 2 % for advisory copilots; ≤ 0.5 % for citation-grounded RAG). Breach triggers AI Governance Forum review.

**Q6.3 — What is your red-team practice?**
> Quarterly red-team probes across prompt injection, jailbreak, data exfiltration, sensitive-output, and tool-misuse. Annual independent red-team. Scorecards retained for the engagement life plus three years.

**Q6.4 — How do you monitor drift?**
> Drift-watch dashboards daily for high-stakes features, weekly for others. SLO breach triggers AI Governance Forum review within five business days; sustained breach triggers rollback to a previous model version.

## Domain 7 — Safety, Security, and Abuse

**Q7.1 — What are your prompt-injection defences?**
> Input filtering, output filtering, system-prompt hardening, tool-call allowlist, retrieved-document source filtering, and a red-team harness. New injection patterns identified in red-team or production trigger filter updates within five business days.

**Q7.2 — How do you handle abuse and anomalous prompts?**
> Per-tenant anomaly detection at the model gateway. Triggers include sudden volume spikes, anomalous prompt patterns, and known-bad signatures. Detection invokes the fair-use clause where appropriate; escalates to incident response where security-relevant.

**Q7.3 — What is your AI incident response runbook?**
> The AI incident runbook covers: detection, containment (rollback, abstain-mode, kill-switch), Customer notification within 24 hours of agency awareness, regulator notification per timeline, redress workflow, post-incident review at the AI Governance Forum, public disclosure if material.

## Domain 8 — Governance, Audit, and Redress

**Q8.1 — What governance forum covers AI features?**
> The AI Governance Forum meets monthly during build and quarterly thereafter. Parties: Customer AI Safety Sponsor, Agency AI Safety Lead, DPO, CISO, product owner, engagement lead. Decisions are minuted and retained for the engagement life plus three years.

**Q8.2 — Can the Customer audit AI logs?**
> Yes. The Customer has audit access on request to prompt and completion logs (retained 30 days), eval logs (life + 3 years), drift-watch metrics (life), red-team scorecards, and AI Governance Forum minutes. Audit access is mediated through a defined process to protect sub-processor confidentiality and tenant-isolation invariants.

**Q8.3 — What is your redress mechanism for affected users?**
> An in-app channel, a dedicated email address, and an escalation phone line. First response SLA of one business day; resolution target by severity. A redress log is reviewed quarterly at the AI Governance Forum and summarised in the quarterly Responsible-AI report.

## Cross-References

- `ai-on-saas-trust-and-compliance-section-template.md` — consistency with credentials.
- `ai-on-saas-responsible-ai-commitment.md` — consistency with commitment.
- `ai-on-saas-risk-register-for-proposals.md` — risks mapped to answers.
- `saas-procurement-and-security-questionnaire-playbook.md` — base SaaS questionnaire pack.
- `saas-msa-dpa-sla-template-language.md` — contract language.
