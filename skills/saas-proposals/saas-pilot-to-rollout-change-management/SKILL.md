---
name: saas-pilot-to-rollout-change-management
description: Use when a SaaS rollout requires operating-model change from project delivery to per-tenant operations, continuous release, recurring revenue, and customer success; use the POC skill when the immediate decision is whether a trial proceeds.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Pilot-to-Rollout Change Management
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The client transitions from an installed-software operating model to a SaaS operating model.
- The client is launching its own SaaS product and the operating function must reorganise around per-tenant operations.
- The implementation includes meaningful change in release cadence, support model, customer success function, and commercial model.
- The buyer has signalled that prior transformations failed on adoption rather than technology.

## Do Not Use When

- The engagement is purely technical with no operating-model change.
- The change-management workstream is generic (use `change-management/` directly).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The current operating model: per-customer or per-tenant; scheduled or continuous release; installation services or customer success; perpetual licence or recurring subscription. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The target operating model and the gap between current and target. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The named operating roles affected (operations, support, customer success, sales, finance, IT). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The leadership coalition and the champions. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The absorption capacity (number of users trained per week, number of business units cutover per quarter). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Map the four substantive shifts: per-customer to per-tenant operations; scheduled to continuous release; installation services to customer success; perpetual licence to recurring revenue.
2. Apply ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement) to each shift.
3. Identify the leadership coalition and the champion network.
4. Design the communication plan with audience, message, channel, frequency, owner.
5. Design the training programme by role: operations, support, customer success, sales, finance, IT.
6. Design the resistance-management plan: identify sources of resistance, distinguish information gaps from genuine concerns, document patterns.
7. Design the pilot-to-rollout sequencing: pilot cohort, 30-day review, waved rollout, stabilisation.
8. Design the reinforcement plan: performance monitoring, recognition, feedback loops, corrective action.
9. Produce the Change Management section and the priced workstream for the Financial Proposal.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Each of the four shifts is named, scoped, measured, and reinforced.
- The change is staffed, not left to communications alone.
- Absorption capacity is respected — no compressed rollout.
- Champion network is real, named, and active.
- Reinforcement plan extends beyond go-live.

## Anti-Patterns

- Treating SaaS adoption as a training module. **Fix:** Treat adoption as workflow, role, governance, support, operating-model, incentive, and reinforcement change measured by outcomes.
- Cutting over the entire organisation at once. **Fix:** Roll out by risk and readiness cohorts with entry, support, rollback, and progression gates.
- Communication plan without role-specific training. **Fix:** Give each role tailored learning objectives, practice, competence checks, job aids, support, and manager reinforcement.
- Champion network appointed but never activated. **Fix:** Select champions with mandate and time, train them, assign local activities, measure activity, and create an escalation route.
- Reinforcement plan that ends at go-live. **Fix:** Continue reinforcement through adoption reviews, coaching, telemetry, refresher learning, and value-realisation milestones.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Change Management section for the proposal. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Priced workstream for the Financial Proposal. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Communication plan. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Training programme. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Resistance-management plan. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Pilot-to-rollout sequencing. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Reinforcement plan. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

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
| Rollout readiness | Advance only when operating owners, support, release, and adoption controls are accepted | Pilot technology scaled without organisational readiness |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

Advance a successful branch pilot only after confirming representative users, support capacity, data readiness, adoption evidence, and a rollback owner for the next cohort.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../change-management/SKILL.md](../../domain-delivery/change-management/SKILL.md) — broader change management.
- [../references/saas-multi-tenant-architecture-block.md](../../profiles-sectors/references/saas-multi-tenant-architecture-block.md) — SaaS mindset paragraph.
- [../references/saas-customer-success-engagement-package.md](../../profiles-sectors/references/saas-customer-success-engagement-package.md) — customer success workstream.
- [../references/saas-lifecycle-email-program-proposal-template.md](../../profiles-sectors/references/saas-lifecycle-email-program-proposal-template.md) — communication backbone.
- [../references/saas-mutual-action-plan-template.md](../../profiles-sectors/references/saas-mutual-action-plan-template.md) — pilot-to-rollout sequencing in MAP.
- [../references/saas-risk-register-for-proposals.md](../../profiles-sectors/references/saas-risk-register-for-proposals.md) — adoption risks.
- [../capacity-building/SKILL.md](../../domain-delivery/capacity-building/SKILL.md) — training and capacity workstream.
