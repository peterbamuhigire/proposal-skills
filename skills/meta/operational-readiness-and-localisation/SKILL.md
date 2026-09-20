---
name: operational-readiness-and-localisation
description: Use when a proposal must prove locally executable operations across banking, tax, licensing, payroll, FX, compliance, logistics, privacy, government interface, or partnerships; use risk-management or financial-proposal for single-section drafting.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Operational Readiness and Localisation
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- An evaluator needs evidence that the proposed delivery model can operate in the target country or market.
- A technical or financial proposal depends on local banking, tax, licences, labour, currency, compliance, logistics, data, public-sector, or partner assumptions.
- Several proposal sections need one readiness matrix with consistent owners, evidence, hold points, and evaluator-facing consequences.

## Do Not Use When

- The request is only to write a normal risk register, work plan, or financial schedule; route to that skill and add this route when the ten-point readiness test is material.
- The proposal contains current legal, tax, privacy, procurement, banking, payroll, or FX claims without a verified source or approved proposer evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| ToR/RFP, jurisdiction, buyer, evaluation criteria, and submission constraints | Buyer documents and approved clarification log | Yes | Stop evaluator-facing claims and return a routing gap |
| Delivery model, work sites, transaction flows, staffing, technology/data flows, vendors, and partners | Approved discovery, architecture, profile, and delivery evidence | Yes | Mark the affected readiness item `NOT_ASSESSED` |
| Current compliance, tax, licensing, privacy, banking, FX, and procurement evidence | Digital Research, Chwezi, buyer instructions, and proposer register | Conditional but required for factual claims | Qualify or remove the claim |
| Staffing effort, timeline, price basis, risks, acceptance criteria, and governance | Methodology, team, work plan, financial proposal, and risk register | Yes for release | Return contradictions to the owning section |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Ten-point evaluator readiness matrix | Proposal lead, reviewer, and evaluator | Each row has proposal section, evidence, owner, status, timing, dependency, and consequence |
| Localisation and compliance action register | Delivery lead and accountable proposer | Current claims are source-linked; commitments have an owner, date, evidence, and remedy |
| Cross-section handoff map | Methodology, team, work plan, risk, financial, and security owners | Scope, effort, cost, timeline, acceptance, and risk language reconcile |
| Qualified trust-and-readiness narrative | Evaluator and release owner | It states what is ready, planned, conditional, or not assessed without overclaiming |

## Evidence Produced

| Evidence | Consumer | Format | Acceptance condition |
|---|---|---|
| Readiness matrix and claim/evidence map | Proposal working paper | Every material assertion maps to buyer evidence, proposer evidence, current source, approved assumption, or gap |
| Localisation action and dependency log | Work plan, compliance matrix, or annex | Owners, due dates, hold points, fallback, and evaluator implication are visible |
| Red-team and reconciliation note | Review record | A second reviewer can test the proposal without relying on persuasive prose |

## Workflow

1. Freeze the buyer decision, ToR/RFP, jurisdiction, sector, procurement path, and relevant proposal envelope. Keep technical and financial content separate where required.
2. Build a ten-point matrix and map each point to the proposal's evidence location:
   - operational banking: payment rails, limits, settlement, integrations, multi-currency, reconciliation, and fallback;
   - precise tax registration: entity activity, indirect-tax treatment, invoicing, filing surface, and reviewer route;
   - sector licensing: regulated activity, authority, approval dependency, lead time, and go-live hold point;
   - payroll and labour: staffing form, loaded effort cost, statutory source dependency, contractor/employee boundary, and termination exposure;
   - FX: proposal currency, delivery-cost currency, exposure, pricing/adjustment clause, cash timing, and sensitivity;
   - compliance calendar: registrations, reports, renewals, insurance, data, contract, and acceptance milestones with owners;
   - last-mile logistics: suppliers, delivery path, SLA, lead time, failure handling, and alternate source;
   - data protection: data classes, residency/transfer, encryption, retention, subprocessors, incident route, and reviewer;
   - government relations: legitimate policy-monitoring owner, engagement channel, escalation, and conflict safeguards;
   - local partnerships: role, standing evidence, due diligence, deliverables, incentives, and substitution/exit path.
3. Label each claim `verified`, `context-bound`, `proposal commitment`, `assumption`, `partial`, or `NOT_ASSESSED`. The user's framework is a durable design prompt, not evidence of a law, licence, rate, deadline, or relationship.
4. Route current law, tax, licensing, privacy, labour, procurement, banking, and FX claims to Digital Research source evaluation and verification. Route money-flow, payroll, tax, banking, FX, and reporting treatment to Chwezi Accounting Doctrine. Do not promise registration, approval, exemption, account capability, or compliance certification without evidence.
5. Convert each material dependency into a deliverable, owner, timing, acceptance test, hold point, risk response, and price/timeline implication. If it changes scope or price, update the financial proposal and technical envelope consistently.
6. Reconcile the matrix with methodology, team composition, work plan, risk register, data/security answers, pricing, assumptions, and contract language. Return conflicts to the owner; do not hide them in a footnote.
7. Run an evaluator red-team: identify which row would cause a clarification, score loss, non-compliance finding, delivery delay, margin loss, data exposure, or mobilisation failure. State the smallest evidence or clarification needed.
8. Release only when material rows are evidenced or presented as dated, owned, conditional commitments. Missing evidence remains `NOT_ASSESSED` and may block submission readiness.

## Decision Rules

| Finding | Action | Failure or risk avoided |
|---|---|---|
| “A local account/licence/partner will be arranged” has no requirement or proof | Replace it with an evidence-backed dependency, owner, hold point, and fallback | Generic assurance and evaluator doubt |
| A current legal, tax, procurement, privacy, or FX statement lacks source support | Quarantine or narrow the claim and name the verification owner | False compliance or stale commitment |
| A readiness dependency changes effort, price, timeline, or acceptance | Reconcile all affected sections and envelopes | Underpriced or undeliverable proposal |
| A local partner is used as credibility without role or due diligence | State the bounded role and evidence, or omit the claim | Name-dropping and reputational risk |
| A stronger readiness claim reduces privacy, quality, margin, or control | Reject or redesign the claim and retain the guardrail | Persuasion optimised at delivery's expense |

## Quality Standards

- Readiness is buyer- and jurisdiction-specific; it is not a legal, tax, procurement, or professional certification.
- Every material row shows evidence state, owner, timing, evaluator implication, and recovery or fallback.
- Staffing and financial proposal logic uses loaded delivery effort and does not invent statutory values.
- FX treatment names the currencies, source/observation date, adjustment mechanism, exposure allocation, and sensitivity where material.
- Data, licensing, compliance, and government interface claims name the responsible reviewer and approval boundary.
- Local partnerships and vendor relationships show role, evidence, due diligence, and exit logic.
- A proposal is not submission-ready while a mandatory readiness or compliance item is missing or unassessed.

## Capability Contract

Read, search, calculate, and draft within the authorised proposal workspace. Review is read-only by default. This skill must not contact regulators, bind a partner, open an account, register taxes, obtain a licence, sign a contract, submit a bid, certify compliance, or disclose confidential evidence without explicit authority.

## Degraded Mode

If the ToR, source, proposer evidence, model, reviewer, or buyer clarification is unavailable, produce the supported matrix only, qualify the affected rows as `NOT_ASSESSED`, state the evidence needed, and withhold submission-readiness claims. Never treat an unavailable check as passed.

## Anti-Patterns

- Generic “local presence” language. Fix: state the partner's bounded role and evidence.
- Promising registration or approvals. Fix: show the dependency and hold point, not an invented outcome.
- Separating a compliance dependency from price and schedule. Fix: reconcile effort, milestone, risk, and cost.
- Writing “data is secure” or “tax compliant”. Fix: name the data/control or tax surface, source, owner, and status.
- Listing stakeholders or deadlines without action logic. Fix: add owner, trigger, evidence, escalation, and review cadence.

## Worked Example

For a proposal to deploy a payment-enabled platform across rural sites, the readiness matrix should distinguish payment-rail capability, licence dependency, data-transfer review, field logistics SLA, local implementation role, FX exposure, and government interface. If the proposer has not verified the bank/provider limits or partner evidence, the proposal states the dependency and mobilisation hold point rather than promising seamless rollout.

<!-- dual-compat-end -->

## References

- [Approach and Methodology](../../pipeline/06-methodology/SKILL.md)
- [Work Plan and Timeline](../../pipeline/08-work-plan/SKILL.md)
- [Financial Proposal](../../pipeline/10-financial-proposal/SKILL.md)
- [Risk Management](../../domain-delivery/risk-management/SKILL.md)
- [Data Management](../../domain-delivery/data-management/SKILL.md)
- [Stakeholder Engagement](../../domain-delivery/stakeholder-engagement/SKILL.md)
- Digital Research Engine: source-evaluation, source-verification, and the Kaizen currentness gate.
- Chwezi Accounting Doctrine: tax-statutory-source-register-and-country-packs, payroll-and-statutory-postings-east-africa, fx-management-and-hedging, and bank-and-mobile-money-reconciliation.
