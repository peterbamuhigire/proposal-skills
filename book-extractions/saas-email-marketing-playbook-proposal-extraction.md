# SaaS Email Marketing Playbook — Proposal Extraction (2026)

Internal synthesis for the proposal-skills engine. Source: Étienne Garbugli, *The SaaS Email Marketing Playbook: Convert Leads, Increase Customer Retention, and Close More Recurring Revenue With Email*. Use as audit trail and implementation source, not for redistribution.

## Source Awareness

The book covers six SaaS email-lifecycle programs: cold/outbound, welcome and onboarding, behavioural and lifecycle, upgrade/upsell/expansion, retention, referral, and reactivation. It also covers segmentation, custom-field data implementation, journey mapping, sequence pacing, copy, subject lines, deliverability, opens, body optimisation, landing-page integration, and benchmarks. It treats email as the operational core of a SaaS lifecycle program, not as a marketing afterthought.

## Copyright Boundary

- No reproduction of the book's specific sequence diagrams, custom-field schemas, or named worked examples.
- Translate principles into original guidance, templates, and deliverable scoping language for the engine.

## Proposal-Relevant Synthesis for SaaS Implementation Proposals

### Lifecycle Communications as a Deliverable
For SaaS implementation engagements (especially in vertical SaaS for financial services, insurance, healthcare, education, and public sector), the agency should propose the *lifecycle communication program* as a scoped, priced deliverable — not as a bonus or marketing add-on. The proposal should name the six lifecycle programs, identify which apply to the client, and price each.

### The Six Lifecycle Programs (engine naming)
For internal engine vocabulary, restate as:

1. **Acquisition sequence** — cold/outbound and lead conversion.
2. **Activation sequence** — welcome and onboarding to first value moment.
3. **Engagement sequence** — behavioural and lifecycle triggers tied to in-product events.
4. **Expansion sequence** — upgrade, upsell, cross-sell, and seat-expansion triggers.
5. **Retention sequence** — renewal protection, churn-risk recovery, and value-reinforcement.
6. **Advocacy and reactivation** — referral programs and win-back sequences.

The proposal scopes each program with: trigger logic, segment definition, content count, channel mix (email, in-app, SMS where appropriate), measurement plan, and review cadence.

### Data Implementation Plan as a Costable Workstream
The book's emphasis on a *data implementation plan* (custom fields, identify events, segmentation, journey mapping) translates directly into a proposal workstream: discovery of user data sources, definition of identify and event schemas, mapping to the marketing automation platform, integration with the SaaS product backend, and operating rules. This is engineering-grade work and should be priced as such, not bundled invisibly inside "email setup".

### Sequence Pacing, Speed, and Operating Rules
The book's "Operating Rules" concept — frequency caps, suppression logic, escalation handling, holiday calendars — should be a proposal artefact. The engine should produce a one-page Operating Rules document inside the methodology section as evidence of mature program design.

### Optimisation and Benchmarks
The book treats benchmarks with appropriate scepticism: prefer same-program lift over industry averages. For the proposal, the M&E section should commit to internal-control measurement (A/B, holdout, propensity-matched) rather than industry-benchmark comparisons, which evaluators see as marketing hand-waving.

### Post-Implementation Communication Strategy
This book reinforces what the AE and Fundamentals books also imply: SaaS implementation is incomplete without a deliberate post-sale communication strategy. The proposal must include a "first 90 days" customer-success communication plan as part of the engagement's customer-success and adoption deliverables.

## Repository Changes Driven

- New skill: `skills/saas-lifecycle-communications-as-deliverable/` — scopes the six lifecycle programs as priced workstreams inside SaaS implementation engagements.
- New reference: `saas-lifecycle-email-program-proposal-template.md` — six-program structure, data implementation plan, operating rules, measurement plan, and pricing drivers.
- Enhancement: `skills/customer-service-and-maintenance-proposals/` adds lifecycle-communication scope language for post-launch.
- Enhancement: `skills/monitoring-and-evaluation/` adds internal-control measurement guidance for SaaS lifecycle programs.
- Enhancement: `skills/data-management/` adds the data-implementation-plan workstream framing.

## Quality Guardrails

- Do not reproduce named sequences or example copy from the book.
- Translate principles into engine-native names ("acquisition", "activation", "engagement", "expansion", "retention", "advocacy") and original scoping language.
- Avoid benchmark name-dropping in proposals; rely on internal-control measurement language.
