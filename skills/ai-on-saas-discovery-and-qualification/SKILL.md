---
name: ai-on-saas-discovery-and-qualification
description: Use during discovery, qualification, and proposal shaping for an engagement that will build AI features into a multi-tenant SaaS product. Provides AI-on-SaaS-specific discovery questions across workflow-AI fit, data readiness for AI, hallucination tolerance, AI maturity, change-readiness for AI, regulator exposure, model-provider posture, and tenant variation. Extends `saas-discovery-and-qualification` with the AI overlay.
---

# AI-on-SaaS Discovery and Qualification
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- An AI-on-SaaS engagement is in discovery, shaping, or qualification.
- The agency is being asked to scope AI features inside a SaaS product and needs to qualify the engagement before pricing.
- The proposal must demonstrate that the agency has interrogated AI fit, AI risk, AI maturity, and AI economics — not assumed them.
- The bid is competitive and the agency needs a discovery audit trail in the proposal to outshine vendors who skipped discovery.

## Do Not Use When

- The discovery is for a non-AI SaaS engagement (use `saas-discovery-and-qualification`).
- The discovery is for generic AI strategy with no SaaS layer (use `ai-transformation-proposal` + `sales-discovery-and-objection-handling`).

## Required Inputs

- The base SaaS discovery output (ICP, Critical Event, pain chain) from `saas-discovery-and-qualification`.
- The candidate AI use-case list (RAG, copilot, agent, analytics, decisioning, generation).
- Access to or a working hypothesis of the buyer's data estate.
- The buyer's regulator(s) and sector.
- The buyer's incumbent AI usage (none, point tools, in-house).

## Workflow

1. Run the base SaaS discovery first. Do not skip it; AI-on-SaaS discovery layers onto SaaS discovery, it does not replace it.
2. Run the **eight AI-on-SaaS qualifying lines** below. Each line has a written answer captured in `BRIEF.md`. Missing answers are flagged as discovery gaps, not assumed away.
3. Score the engagement against the **AI-on-SaaS Qualification Scorecard** (low, medium, high, do-not-bid). The score determines whether to proceed to proposal or to recommend a paid AI discovery first.
4. Decide and document: full proposal, paid AI discovery, joint AI-on-SaaS feasibility study, or polite decline.
5. Write the **Discovery Findings** paragraph into Understanding-of-Assignment so the evaluator sees the discovery audit trail.

## The Eight AI-on-SaaS Qualifying Lines

### 1. Workflow-AI Fit
- Which specific workflow is the AI feature inside? Who performs it today? How often? How long does it take?
- Is the AI **augmenting** a human, **replacing** a step, or **enabling** a workflow that does not exist today?
- Is the workflow **high-volume / low-stakes** (good RAG / copilot fit) or **low-volume / high-stakes** (HITL mandatory)?

### 2. Data Readiness for AI
- Where is the source data? Quality, completeness, structured / unstructured, language, currency.
- Is the data **per tenant** (RAG index per tenant) or **shared** (single index across tenants with logical isolation)?
- Are there licensing constraints on using the data to train, embed, or retrieve?
- Is there a **golden dataset** for eval? Who labels it? How quickly can it be assembled?

### 3. Hallucination Tolerance
- What happens if the AI is wrong? (Annoyance / rework / customer harm / regulatory breach / financial loss / reputational crisis.)
- What is the **acceptable hallucination ceiling** per use case (e.g. ≤ 2 % for advisory copilot, 0 % for regulated decisioning)?
- What **abstain** behaviour does the buyer prefer (refuse, escalate, downgrade to non-AI path)?
- Does the buyer require **citation-grounded** outputs (RAG with citations) or are uncited generative outputs acceptable?

### 4. AI Maturity
- Has the buyer's organisation used AI in production before? Internal tools? Vendor tools?
- Does the buyer have an AI governance forum, AI policy, or AI ethics board?
- Does the buyer have an eval discipline, or does this engagement establish it?
- Does the buyer's CISO have an AI sub-processor list, or does this engagement create it?

### 5. Change-Readiness for AI
- How will the affected users react? (Threatened, neutral, eager.)
- Has the buyer communicated AI plans internally? Externally?
- Is union, works-council, or regulator consultation required before AI features go to users?
- What is the **augment-vs-replace** framing the buyer will use publicly?

### 6. Regulator Exposure
- Which AI regulator(s) apply? EU AI Act (tier?), Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U guidance, Rwanda AI Policy, EAC, sectoral.
- Is this an **AI Act high-risk system**? If so, the conformity assessment is in scope and the methodology must reflect it.
- Are there sectoral AI rules (financial-services model-risk management, healthcare clinical-decision support, education student-data)?
- Is **sovereign-AI** a requirement (on-prem inference, in-country model hosting, government-controlled keys)?

### 7. Model-Provider Posture
- Single provider (vendor lock), multi-provider (gateway), or sovereign (on-prem / open-weight)?
- Is **training-data exclusion** a hard requirement (customer data must not train provider models)?
- Is **region routing** required (EU data routed to EU inference; KE data routed to KE / ZA inference)?
- What is the **fallback** model if the primary is unavailable or banned?

### 8. Tenant Variation
- Do tenants share the AI feature behaviour, or does each tenant need its own RAG index, prompt set, or eval set?
- Is **per-tenant model selection** a tier feature (premium tier picks model, standard tier locked)?
- Is **per-tenant fine-tuning** in scope, or is in-context RAG sufficient?
- Is the eval cohort per tenant, per regulator, or per use case?

## AI-on-SaaS Qualification Scorecard

| Dimension | Low (proceed) | Medium (proceed with caveats) | High (paid discovery first) | Do-not-bid |
|---|---|---|---|---|
| Workflow-AI fit | Workflow named, baseline metric exists, AI augments | Workflow named, no baseline metric | Workflow vague, AI replaces with no HITL | No workflow, "AI for AI's sake" |
| Data readiness | Golden set exists or feasible within 4 weeks | Golden set feasible within 12 weeks | Data scattered, labelling effort > 12 weeks | Data inaccessible or licensed against AI use |
| Hallucination tolerance | Stated ceiling, abstain logic acceptable | Tolerance discussed, abstain to be designed | Tolerance unclear, regulator-facing | Zero-tolerance, generative, no HITL — refuse |
| AI maturity | Forum, policy, prior production AI | Some governance, no prior production AI | No governance, no policy | Active hostility to AI from CISO / DPO |
| Change-readiness | Communications begun, augment framing | Communications planned | No communications, union consultation pending | Active resistance, no sponsor |
| Regulator exposure | Known and stable | Known, pending guidance | Tier unclear, conformity assessment ambiguous | Tier-1 ban risk in target market |
| Model-provider posture | Multi-provider acceptable | Single provider with gateway | Sovereign required, no on-prem capability | Sovereign-only and no GPU access |
| Tenant variation | Shared RAG, shared eval | Shared RAG, per-regulator eval | Per-tenant RAG, per-tenant eval | Per-tenant fine-tuning at low fee |

Score the engagement on each row; one **do-not-bid** row is sufficient to decline politely.

## Quality Standards

- Discovery questions are open and behavioural, not yes/no.
- Each dimension has a written answer or a flagged gap.
- The qualification scorecard is in the agency's win-room file, not the proposal — the proposal carries the **Discovery Findings** paragraph instead.
- The Discovery Findings paragraph shows the evaluator that the agency interrogated the AI scope before pricing.

## Anti-Patterns

- "Tell us about your AI vision" as the only AI discovery question.
- Skipping the data-readiness line because the buyer "has data."
- Assuming a hallucination tolerance from the use-case name.
- Treating AI maturity as binary (have AI / no AI).
- Failing to ask about regulator tier in AI Act / NCAIS / NAIS jurisdictions.
- Committing to a model provider in discovery.

## Outputs

- AI-on-SaaS Discovery Findings paragraph for Understanding-of-Assignment.
- Eight AI-on-SaaS qualifying line answers in `BRIEF.md`.
- AI-on-SaaS Qualification Scorecard in the win-room file.
- Go / no-go / paid-discovery / feasibility-study decision.

## References

- `../references/ai-on-saas-discovery-question-bank.md` — long-form question bank.
- `../references/discovery-question-bank-for-proposals.md` — base discovery patterns.
- `../references/saas-discovery-question-bank.md` — SaaS discovery overlay.
- `../saas-discovery-and-qualification/SKILL.md` — base SaaS discovery skill.
- `../ai-on-saas-combined-methodology/SKILL.md` — how discovery outputs feed methodology.
- `../ai-on-saas-business-case-and-roi/SKILL.md` — how discovery outputs feed the business case.
- `../ai-on-saas-poc-and-pilot-scoping/SKILL.md` — when discovery output triggers a paid POC.
- `../ai-on-saas-risk-and-responsible-ai/SKILL.md` — risk and Responsible-AI register.
- `../sales-discovery-and-objection-handling/SKILL.md` — discovery and objection handling discipline.
