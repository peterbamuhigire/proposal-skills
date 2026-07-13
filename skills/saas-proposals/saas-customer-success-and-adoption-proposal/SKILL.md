---
name: saas-customer-success-and-adoption-proposal
description: Use when a SaaS proposal must scope and price onboarding, activation, health scoring, success cadence, expansion, retention, and value realisation; use pilot-to-rollout change management for internal operating-model change.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Customer Success and Adoption Proposal
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The SaaS implementation includes meaningful adoption risk.
- The buyer's CFO asks "what happens after go-live?"
- The proposal must defend premium fees with a credible post-go-live engagement.
- The agency proposes a retainer or managed-service relationship after implementation.

## Do Not Use When

- The engagement is a one-off configuration with no ongoing relationship expected.
- The buyer explicitly excludes post-go-live services from the scope.

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The buyer's segment (Enterprise / SMM / B2C) — drives intensity. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The number of named accounts (for resale SaaS) or business units (for internal-use). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The vertical and any regulatory cadence (annual audits, regulator reviews). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The expansion-path expectations. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's tolerance for ongoing investment. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Scope the engagement at the right intensity: Light Touch (SMB), Standard (mid-market), High Touch (enterprise).
2. Design Onboarding (Weeks 0–6): welcome, discovery refresh, account map, success plan v1, activation playbook, first admin training.
3. Design Activation (Weeks 4–12): TTV milestone, behavioural telemetry, training waves, adoption nudges, triage runbook.
4. Establish Operating Cadence: weekly during implementation, monthly during stabilisation, quarterly QBR, annual renewal review.
5. Define Expansion Plays: triggers, plays, owners.
6. Define Save Plays: churn-risk signals, save plays, owners.
7. Implement Health Scoring: composite score with components and weights, Red/Amber/Green status.
8. Name the Customer Success roles: CSM, CSE, Account Director, Executive Sponsor, CS Operations.
9. Define the tooling stack.
10. Produce the Customer Success section and the priced workstream for the Financial Proposal.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Customer success priced as a named workstream, not unfunded warranty.
- Success plans name measurable outcomes.
- QBRs are honest value-realisation reviews, not demos with new charts.
- Save plays defined for the predictable churn signals (sponsor change, usage drop, support spike, QBR dissatisfaction, stalled renewal).
- Health score components, weights, and response actions all defined.

## Anti-Patterns

- Customer success as unfunded warranty inside the licence cost. **Fix:** Scope customer success as a funded service with outcomes, capacity, cadence, boundaries, and price separate from warranty.
- Single CSM owning 30+ accounts without tiering. **Fix:** Tier accounts by value, complexity, and risk, then model CSM capacity and service levels by tier.
- Generic success plans without measurable outcomes. **Fix:** Give each success plan a baseline, target outcome, owner, milestone, evidence source, risk, and review date.
- "QBR" that is a feature update slide deck. **Fix:** Use the QBR to compare realised value with targets, decide interventions, address risks, and agree the next value milestone.
- No defined save play for sponsor change. **Fix:** Define sponsor-change detection, executive re-alignment, value revalidation, handover, and escalation steps.
- Bundling support and success (different goals, different staffing). **Fix:** Separate incident resolution and maintenance SLAs from adoption, value realisation, retention, and expansion responsibilities.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Customer Success and Adoption section for the proposal. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Priced workstream for the Financial Proposal. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Operating cadence and review pack templates. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Expansion play list with triggers and owners. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Save play list with triggers and owners. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Health-score design. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

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
| Adoption outcome | Assign a baseline, target, owner, cadence, and intervention | Activity reporting without realised value |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

For a phased rollout, define activation and competent-use measures by role, assign the customer success and business owners, and delay expansion when adoption evidence misses the agreed gate.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/saas-customer-success-engagement-package.md](../../profiles-sectors/references/saas-customer-success-engagement-package.md) — primary reference.
- [../references/saas-lifecycle-email-program-proposal-template.md](../../profiles-sectors/references/saas-lifecycle-email-program-proposal-template.md) — communication backbone.
- [../references/saas-business-case-and-roi-template.md](../../profiles-sectors/references/saas-business-case-and-roi-template.md) — value-realisation review pack.
- [../references/saas-mutual-action-plan-template.md](../../profiles-sectors/references/saas-mutual-action-plan-template.md) — Phase 5 / Phase 6 detail.
- [../references/saas-risk-register-for-proposals.md](../../profiles-sectors/references/saas-risk-register-for-proposals.md) — adoption risks.
- [../customer-service-and-maintenance-proposals/SKILL.md](../../strategy-positioning/customer-service-and-maintenance-proposals/SKILL.md) — support layer adjacent to success.
- [../change-management/SKILL.md](../../domain-delivery/change-management/SKILL.md) — change management workstream that supports adoption.
