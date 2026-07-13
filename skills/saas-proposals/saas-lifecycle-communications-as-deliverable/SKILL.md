---
name: saas-lifecycle-communications-as-deliverable
description: Use when acquisition, activation, engagement, expansion, retention, and advocacy communications must be a scoped and priced SaaS delivery workstream; use customer-success planning when the need is operating cadence rather than communications production.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Lifecycle Communications as Deliverable
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The SaaS implementation includes lifecycle programs as a delivery scope.
- The buyer's adoption, retention, or expansion goals depend on engineered communications.
- The agency proposes a managed-service or retainer relationship that includes lifecycle program operation.
- The buyer has previously failed at email or in-app lifecycle communications and needs disciplined structure.

## Do Not Use When

- The engagement does not include lifecycle communications.
- The buyer's compliance environment forbids lifecycle marketing (rare; even regulated industries permit operational lifecycle communications).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| Which of the six lifecycle programs are in scope (acquisition, activation, engagement, expansion, retention, advocacy). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The channels in scope (email, in-app, SMS, push, webhook). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The languages in scope. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's data sources and identity model. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's consent and preference management practices. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The regulator stance on lifecycle marketing in the buyer's vertical. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Confirm which lifecycle programs apply to the buyer and prioritise. Default sequence: Activation → Retention → Engagement → Expansion → Acquisition → Advocacy.
2. Scope the Data Implementation Plan workstream: identify schema, event schema, custom fields, identity resolution, consent and preference, segmentation, data hygiene.
3. Scope the Content Production workstream: master content, triggered content, manual outreach. Per-program asset count.
4. Scope the Automation Engineering workstream: MAP configuration, in-product messaging, SMS / push integration, webhook / CRM sync, suppression and frequency-cap engine, holiday and quiet-hours engine.
5. Define the Operating Rules: frequency caps, quiet hours, suppression triggers, escalation rules, holiday calendar, compliance rules, brand voice.
6. Scope the Measurement and Optimisation workstream: per-program KPIs, internal-control measurement (A/B, holdout, propensity-matched), quarterly optimisation cycle.
7. Price each workstream by driver: programs, segments, channels, languages, vertical regulatory review, continuous-optimisation retainer.
8. Produce the lifecycle program section for Methodology and the priced workstream for Financial Proposal.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Each program has a stated goal, trigger, channel, and measurement.
- Operating rules signed off by the client before any program goes live.
- Internal-control measurement (not industry benchmarks) is the standard.
- Compliance review is built into the production cycle for regulated verticals.
- Touch limits set as operating rules at design time, not after launch.

## Anti-Patterns

- "Email setup" bundled invisibly as a sub-line of implementation. **Fix:** Scope channels, triggers, data, consent, content, automation, QA, ownership, measurement, and price as a visible workstream.
- All six programs launched at once. **Fix:** Sequence programmes by lifecycle constraint and evidence, launching the highest-value journey before expanding.
- Benchmark comparisons used as the sole evidence. **Fix:** Use product and cohort baselines as primary evidence and label external benchmarks as contextual.
- Touch limits set after launch. **Fix:** Set contact-policy limits, suppression, consent, priority, quiet hours, and exception handling before automation goes live.
- Content review without regulator-aware review in regulated verticals. **Fix:** Add legal, privacy, clinical, financial, or public-sector review gates appropriate to the message, data, and jurisdiction.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Lifecycle program section for Methodology. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Priced workstream for Financial Proposal. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Data Implementation Plan scope. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Operating Rules document. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Per-program KPI plan. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Measurement and optimisation plan. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

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
| Lifecycle trigger | Define audience, event, content owner, consent rule, and success measure | Unscoped marketing activity or unlawful messaging |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

For a planned release, prepare administrator, end-user, support, and executive messages with distinct actions and timing; hold distribution until the release owner approves the final scope and support route.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/saas-lifecycle-email-program-proposal-template.md](../../profiles-sectors/references/saas-lifecycle-email-program-proposal-template.md) — primary template.
- [../references/saas-customer-success-engagement-package.md](../../profiles-sectors/references/saas-customer-success-engagement-package.md) — adjacent customer-success workstream.
- [../references/saas-discovery-question-bank.md](../../profiles-sectors/references/saas-discovery-question-bank.md) — Section L (measurement).
- [../data-management/SKILL.md](../../domain-delivery/data-management/SKILL.md) — Data Implementation Plan workstream depth.
- [../monitoring-and-evaluation/SKILL.md](../../domain-delivery/monitoring-and-evaluation/SKILL.md) — measurement standard.
- [../change-management/SKILL.md](../../domain-delivery/change-management/SKILL.md) — adoption communications overlap.
