---
name: ai-agent-vertical-positioning
description: Use when the AI-agent proposal must position the agency for a specific vertical — customer support (resolution agents), financial services (compliance, reconciliation, KYC), insurance (claims triage), public sector (citizen-service agents — extreme caution and sovereign-AI), healthcare (admin-only, non-clinical), legal (drafting and review under bar rules), operations (alerting, triage, coding agents). Provides vertical autonomy-and-irreversibility stances, named use cases, regulator framing, discriminators, risk language, and competitive displacement angles. Extends `ai-on-saas-vertical-positioning` with the agent overlay.
---

# AI-Agent Vertical Positioning
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The AI-agent bid is in a defined vertical and the proposal must demonstrate vertical literacy in agentic terms.
- The buyer's evaluators include vertical specialists (regulator, sector champion, clinical lead, head of supervision, bar council, ombudsman).
- The competitive set includes horizontal vendors who do not understand the vertical's autonomy stance.
- The vertical carries sector-specific autonomy limits (financial-services decisioning, healthcare clinical separation, legal practice rules, public-sector administrative law).

## Do Not Use When

- The engagement is horizontal and the vertical is not a discriminator.
- The vertical is non-agent (use `ai-on-saas-vertical-positioning`).

## Required Inputs

- The buyer's vertical and sub-vertical.
- The regulator(s) and stance on autonomous decisioning.
- The candidate agent use cases.
- The competitive set (named or inferred).
- The buyer's irreversibility tolerance and HITL stance.
- Local-content / sovereign requirements.

## Workflow

1. Identify the vertical and load the matching vertical reference (`vertical-ai-agent-<vertical>.md`).
2. Choose two to four **named agent use cases** appropriate to the vertical, each with autonomy level and reversibility profile.
3. Position the agency's **discriminators** for the vertical: regulator literacy, autonomy discipline, irreversibility gating, kill-switch readiness, action audit log, redress mechanism, sovereign-AI option, language coverage, supervisor retraining capability.
4. Frame **risk and regulator** language using the vertical's vocabulary, not generic agent language (FS: model-risk management and adverse-decisioning rights; healthcare: clinical decision support classification and non-diagnostic agentic; legal: bar rules and lawyer responsibility; public sector: administrative-law fairness and sovereign-AI).
5. Choose the **win themes** from `ai-agent-win-themes-and-discriminators.md` that fit the vertical.
6. Draft the **vertical positioning paragraph** for Executive Summary, the **vertical case studies** for Relevant Experience, and the **vertical methodology variations** for `06-methodology`.

## Vertical Library (Brief)

### Customer Support — Resolution Agents
- Agent use cases: ticket triage and routing; deflection on FAQ and account self-serve; agent-assist (suggest reply, draft macro, find article); end-to-end resolution on bounded action sets (refund up to value bound, ticket close, status update); voice-of-customer summarisation.
- Autonomy stance: L3 on triage; L2 on agent-assist; L1 on irreversible (refund, cancellation, account closure).
- Regulator: data-protection regulators (general); sectoral where the support is for regulated services.
- Discriminators: containment-vs-deflection honesty (containment is bad if the customer left the journey frustrated); agent-assist before agent-replace framing; escalation SLA with named human; multilingual depth; supervisor retraining curriculum.

### Financial Services — Compliance and Reconciliation Agents
- Agent use cases: KYC document triage and exception assembly; AML alert disposition assembly (the agent assembles the case, a named human dispositions); transaction reconciliation across systems; complaint classification and routing; sanctions-screening triage.
- Autonomy stance: L3 on triage and case assembly; L1 (strict) on disposition, closure, and any customer-facing action.
- Regulator: CBK, CBN, SARB, BoU, NBR, FSCA, NDPC; model-risk management discipline; adverse-decisioning rights; FATF guidance on AI in AML; SR 11-7-style governance for groups with US footprint.
- Discriminators: model-risk overlay on every agent; HITL strict on decisioning; the agent **never** approves / declines / closes alerts on its own; full audit log with regulator-grade access; sovereign-AI option; reconciliation determinism with replay.

### Insurance — Claims Triage Agents
- Agent use cases: claims-document triage and categorisation; fraud-signal assembly (the agent assembles the signal pack, a human decides); first-notification-of-loss summarisation; policy-comparison drafting for customer service; subrogation candidate identification.
- Autonomy stance: L3 on triage and assembly; L1 on declinature, payout, fraud determination.
- Regulator: IRA (KE / UG), NAICOM, FSCA; conduct-of-business; fairness in claims handling.
- Discriminators: explainability of triage; HITL strict on declinature and payout; citation grounding; complaint-channel awareness; sectoral retraining for claims handlers shifting from doer to supervisor.

### Public Sector — Citizen-Service Agents (Extreme Caution)
- Agent use cases: citizen-FAQ and information retrieval (cited); case routing inside ministries; multilingual translation of forms; complaint triage and routing; document understanding for procurement / judiciary; non-decisioning support to caseworkers.
- Autonomy stance: L1 / L2 only on anything affecting a citizen's right or entitlement. **L0 on benefit determinations, immigration decisions, criminal-justice decisions, tax assessments.** The agent assembles; the named officer decides.
- Regulator: NCAIS Kenya, NAIS Nigeria, NITA-U Uganda, RGB / Rwanda AI Policy, ICASA / DCDT South Africa; administrative-law fairness; right to human review; transparency-to-affected-party; sovereign-AI expectations.
- Discriminators: sovereign-AI option (on-prem or in-country inference); local-language depth; administrative-law literacy (no decisioning); transparency-to-affected-party UX with contestability; published action catalogue; quarterly kill-switch drill with regulator observer.
- **Honesty principle** — the proposal does not promise citizen-service agents that take decisions on citizens. Public-sector buyers reward this honesty; competitors who over-promise lose to enforcement.

### Healthcare — Admin-Only Agents
- Agent use cases: clinical-documentation drafting (summary, discharge letter, referral) with clinician sign-off; prior-authorisation triage; claims and billing reconciliation; appointment scheduling and follow-up; hospital-operations triage.
- Autonomy stance: L2 / L3 on admin; **L0 on anything clinical** — diagnosis, treatment recommendation, dose decision, triage of patient acuity for life-critical care.
- Regulator: Ministries of Health, KMPDC, NHIS / SHA / SHIF, HPCSA; HIPAA where US-linked; clinical-decision-support classification and the line where AI becomes a medical device.
- Discriminators: explicit non-clinical scope on the action catalogue; clinician-in-the-loop on every drafted clinical artefact; audit log with retention matched to clinical record-keeping rules; residency.

### Legal — Drafting and Review Agents
- Agent use cases: contract first-draft generation and clause comparison; due-diligence document review (the agent flags; the lawyer decides); legal-research synthesis with citations; filing assembly (the agent assembles; the lawyer files); e-discovery triage; client-intake drafting.
- Autonomy stance: L2 / L3 on drafting and assembly; **L0 on filings, advice, and any communication purporting to be from a lawyer or to bind a client.** The lawyer remains the responsible party; bar rules require it.
- Regulator: Bar associations and law societies (Uganda Law Society, Law Society of Kenya, NBA, GCB, GCB, SRA in UK-aligned jurisdictions); civil-procedure rules; confidentiality and privilege rules.
- Discriminators: confidentiality by tenant scope (no shared memory across firms); citation grounding (no hallucinated cases); audit log; lawyer-final on every filing and communication; insurance arrangement aligned to E&O.

### Operations — Alerting, Triage, and Coding Agents
- Agent use cases: alert triage (incident routing, runbook execution on bounded actions); coding agents (refactor, test generation, dependency update, pull-request authorship under human review); infrastructure-change triage (the agent proposes; the SRE applies); log-summary and root-cause assembly.
- Autonomy stance: L2 / L3 on triage and assembly; **L1 on production changes**; L2 / L3 on reversible code changes within a sandbox; L1 on merge-to-main and any prod deployment.
- Regulator: data-protection (general); sectoral where the operations are inside a regulated service.
- Discriminators: deterministic replay; sandbox by default; merge-gate human review; observability of the agent itself; rollback by default; coding-agent specific eval (test pass, regression, dependency-safety, secret-leak).

## Sample Vertical Paragraphs (illustrative)

### Financial Services
> Our financial-services agentic practice treats every agent as a model under model-risk management. Agents triage and assemble; named officers decide. The agent never approves or declines a credit, an AML alert, or a sanctions match on its own. The action catalogue is published, every action class has a reversibility classification, and irreversible actions are L1-gated with a named approver. The audit log is regulator-grade and replay-deterministic so an internal auditor or a supervisor can reconstruct any decision the agent influenced. A sovereign-AI option is available for the most sensitive tenants.

### Public Sector
> Our public-sector agent practice begins with what an agent must not do. Agents do not decide on benefits, status, tax, or justice; agents assemble the case, in the language the citizen speaks, with citations to the controlling regulation, and a named officer decides. The action catalogue is published. Every external communication discloses the agent and offers an immediate route to a human. Sovereign-AI deployment is supported for ministries whose data must not leave the country. The kill-switch drill is run quarterly, with a regulator observer where invited.

### Healthcare
> Our healthcare agent practice is explicitly admin-only. Agents draft discharge summaries, route prior-authorisations, reconcile claims, schedule follow-ups; agents do not diagnose, do not triage clinical acuity for life-critical care, and do not recommend treatment. Every drafted clinical artefact is signed by the responsible clinician. The action catalogue makes the non-clinical boundary explicit and auditable, and the methodology classifies any expansion across that boundary as a regulated-device decision that pauses the engagement until the regulator concurs.

## Quality Standards

- Vertical use cases are named and bounded; no generic "agents for the sector".
- Autonomy stance is per use case, with reversibility profile.
- Regulator references are specific.
- Discriminators are vertical-specific.
- Risk framing uses the vertical's vocabulary.
- Honesty principle is applied — promises the regulator would not accept are not made.
- Case studies or comparable references are in the vertical or transferable with stated rationale.

## Anti-Patterns

- "Agents for banking" with no named use case.
- L4 / L5 autonomy promised for citizen-service or healthcare clinical decisioning.
- Legal drafting agents promised without lawyer-final on filings.
- Coding agents that auto-merge to main without human review.
- Insurance claims agents that decide payout or declinature on their own.
- Customer-support agents that close tickets without resolution evidence (containment masquerading as deflection).
- Operations agents that act on production without a sandbox or merge gate.

## Outputs

- Vertical positioning paragraph for Executive Summary.
- Vertical-specific use-case list with autonomy and reversibility profile.
- Vertical discriminators block.
- Vertical risk and regulator language.
- Vertical methodology variations for `06-methodology`.
- Vertical case studies or comparable references.

## References

- `../references/vertical-ai-agent-customer-support.md`
- `../references/vertical-ai-agent-financial-services.md`
- `../references/vertical-ai-agent-insurance.md`
- `../references/vertical-ai-agent-public-sector.md`
- `../references/vertical-ai-agent-healthcare.md`
- `../references/vertical-ai-agent-legal.md`
- `../references/vertical-ai-agent-operations.md`
- `../references/ai-agent-win-themes-and-discriminators.md`
- `../ai-on-saas-vertical-positioning/SKILL.md` — AI-on-SaaS verticals (load alongside for SaaS-embedded agents).
- `../ai-agent-methodology/SKILL.md` — methodology that variations sit inside.
- `../ai-agent-risk-and-responsible-ai/SKILL.md` — vertical-specific risk entries.
