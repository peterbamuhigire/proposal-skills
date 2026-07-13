---
name: ai-on-saas-discovery-and-qualification
description: Use when qualifying AI features inside a multi-tenant SaaS opportunity across workflow fit, data readiness, hallucination tolerance, regulation, and tenant variation; use SaaS discovery when no AI capability is proposed.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI-on-SaaS Discovery and Qualification
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- An AI-on-SaaS engagement is in discovery, shaping, or qualification.
- The agency is being asked to scope AI features inside a SaaS product and needs to qualify the engagement before pricing.
- The proposal must demonstrate that the agency has interrogated AI fit, AI risk, AI maturity, and AI economics — not assumed them.
- The bid is competitive and the agency needs a discovery audit trail in the proposal to outshine vendors who skipped discovery.

## Do Not Use When

- The discovery is for a non-AI SaaS engagement (use `saas-discovery-and-qualification`).
- The discovery is for generic AI strategy with no SaaS layer (use `ai-transformation-proposal` + `sales-discovery-and-objection-handling`).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The base SaaS discovery output (ICP, Critical Event, pain chain) from `saas-discovery-and-qualification`. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The candidate AI use-case list (RAG, copilot, agent, analytics, decisioning, generation). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Access to or a working hypothesis of the buyer's data estate. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's regulator(s) and sector. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's incumbent AI usage (none, point tools, in-house). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Run the base SaaS discovery first. Do not skip it; AI-on-SaaS discovery layers onto SaaS discovery, it does not replace it.
2. Run the **eight AI-on-SaaS qualifying lines** below. Each line has a written answer captured in `BRIEF.md`. Missing answers are flagged as discovery gaps, not assumed away.
3. Score the engagement against the **AI-on-SaaS Qualification Scorecard** (low, medium, high, do-not-bid). The score determines whether to proceed to proposal or to recommend a paid AI discovery first.
4. Decide and document: full proposal, paid AI discovery, joint AI-on-SaaS feasibility study, or polite decline.
5. Write the **Discovery Findings** paragraph into Understanding-of-Assignment so the evaluator sees the discovery audit trail.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

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

- "Tell us about your AI vision" as the only AI discovery question. **Fix:** Build a use-case inventory covering user, decision, data, action, error cost, human oversight, and measurable outcome.
- Skipping the data-readiness line because the buyer "has data." **Fix:** Profile data ownership, access, quality, lineage, representativeness, consent, retention, and tenant separation with evidence.
- Assuming a hallucination tolerance from the use-case name. **Fix:** Ask the buyer to set error and abstention tolerances per use case and identify who accepts residual risk.
- Treating AI maturity as binary (have AI / no AI). **Fix:** Score maturity across strategy, data, evaluation, governance, operations, adoption, procurement, and incident response.
- Failing to ask about regulator tier in AI Act / NCAIS / NAIS jurisdictions. **Fix:** Identify jurisdiction and sector classification, then verify the applicable risk tier and evidence obligations.
- Committing to a model provider in discovery. **Fix:** Keep provider selection open until data residency, evaluation, cost, latency, procurement, and exit criteria are tested.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI-on-SaaS Discovery Findings paragraph for Understanding-of-Assignment. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Eight AI-on-SaaS qualifying line answers in `BRIEF.md`. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| AI-on-SaaS Qualification Scorecard in the win-room file. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Go / no-go / paid-discovery / feasibility-study decision. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

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
| Critical unknown | Pause solution claims and issue a targeted discovery question or no-bid condition | Proposal built on untested AI or buyer assumptions |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

If a proposed copilot lacks an approved knowledge source, representative task set, or error tolerance, classify it as unqualified and ask targeted discovery questions before proposing a pilot.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/ai-on-saas-discovery-question-bank.md](../../profiles-sectors/references/ai-on-saas-discovery-question-bank.md) — long-form question bank.
- [../references/discovery-question-bank-for-proposals.md](../../profiles-sectors/references/discovery-question-bank-for-proposals.md) — base discovery patterns.
- [../references/saas-discovery-question-bank.md](../../profiles-sectors/references/saas-discovery-question-bank.md) — SaaS discovery overlay.
- [../saas-discovery-and-qualification/SKILL.md](../../saas-proposals/saas-discovery-and-qualification/SKILL.md) — base SaaS discovery skill.
- [../ai-on-saas-combined-methodology/SKILL.md](../ai-on-saas-combined-methodology/SKILL.md) — how discovery outputs feed methodology.
- [../ai-on-saas-business-case-and-roi/SKILL.md](../ai-on-saas-business-case-and-roi/SKILL.md) — how discovery outputs feed the business case.
- [../ai-on-saas-poc-and-pilot-scoping/SKILL.md](../ai-on-saas-poc-and-pilot-scoping/SKILL.md) — when discovery output triggers a paid POC.
- [../ai-on-saas-risk-and-responsible-ai/SKILL.md](../ai-on-saas-risk-and-responsible-ai/SKILL.md) — risk and Responsible-AI register.
- [../sales-discovery-and-objection-handling/SKILL.md](../../strategy-positioning/sales-discovery-and-objection-handling/SKILL.md) — discovery and objection handling discipline.
