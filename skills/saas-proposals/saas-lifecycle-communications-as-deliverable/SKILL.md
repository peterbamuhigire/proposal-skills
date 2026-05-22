---
name: saas-lifecycle-communications-as-deliverable
description: Use when a SaaS implementation proposal scopes lifecycle communications (acquisition, activation, engagement, expansion, retention, advocacy) as a priced workstream rather than a marketing afterthought. Scopes data implementation plan, content production, automation engineering, operating rules, and measurement.
---

# SaaS Lifecycle Communications as Deliverable
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The SaaS implementation includes lifecycle programs as a delivery scope.
- The buyer's adoption, retention, or expansion goals depend on engineered communications.
- The agency proposes a managed-service or retainer relationship that includes lifecycle program operation.
- The buyer has previously failed at email or in-app lifecycle communications and needs disciplined structure.

## Do Not Use When

- The engagement does not include lifecycle communications.
- The buyer's compliance environment forbids lifecycle marketing (rare; even regulated industries permit operational lifecycle communications).

## Required Inputs

- Which of the six lifecycle programs are in scope (acquisition, activation, engagement, expansion, retention, advocacy).
- The channels in scope (email, in-app, SMS, push, webhook).
- The languages in scope.
- The buyer's data sources and identity model.
- The buyer's consent and preference management practices.
- The regulator stance on lifecycle marketing in the buyer's vertical.

## Workflow

1. Confirm which lifecycle programs apply to the buyer and prioritise. Default sequence: Activation → Retention → Engagement → Expansion → Acquisition → Advocacy.
2. Scope the Data Implementation Plan workstream: identify schema, event schema, custom fields, identity resolution, consent and preference, segmentation, data hygiene.
3. Scope the Content Production workstream: master content, triggered content, manual outreach. Per-program asset count.
4. Scope the Automation Engineering workstream: MAP configuration, in-product messaging, SMS / push integration, webhook / CRM sync, suppression and frequency-cap engine, holiday and quiet-hours engine.
5. Define the Operating Rules: frequency caps, quiet hours, suppression triggers, escalation rules, holiday calendar, compliance rules, brand voice.
6. Scope the Measurement and Optimisation workstream: per-program KPIs, internal-control measurement (A/B, holdout, propensity-matched), quarterly optimisation cycle.
7. Price each workstream by driver: programs, segments, channels, languages, vertical regulatory review, continuous-optimisation retainer.
8. Produce the lifecycle program section for Methodology and the priced workstream for Financial Proposal.

## Quality Standards

- Each program has a stated goal, trigger, channel, and measurement.
- Operating rules signed off by the client before any program goes live.
- Internal-control measurement (not industry benchmarks) is the standard.
- Compliance review is built into the production cycle for regulated verticals.
- Touch limits set as operating rules at design time, not after launch.

## Anti-Patterns

- "Email setup" bundled invisibly as a sub-line of implementation.
- All six programs launched at once.
- Benchmark comparisons used as the sole evidence.
- Touch limits set after launch.
- Content review without regulator-aware review in regulated verticals.

## Outputs

- Lifecycle program section for Methodology.
- Priced workstream for Financial Proposal.
- Data Implementation Plan scope.
- Operating Rules document.
- Per-program KPI plan.
- Measurement and optimisation plan.

## References

- `../references/saas-lifecycle-email-program-proposal-template.md` — primary template.
- `../references/saas-customer-success-engagement-package.md` — adjacent customer-success workstream.
- `../references/saas-discovery-question-bank.md` — Section L (measurement).
- `../data-management/SKILL.md` — Data Implementation Plan workstream depth.
- `../monitoring-and-evaluation/SKILL.md` — measurement standard.
- `../change-management/SKILL.md` — adoption communications overlap.
