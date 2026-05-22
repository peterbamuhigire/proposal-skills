# SaaS Lifecycle Email Program Proposal Template

Lifecycle communications as a paid deliverable inside SaaS implementation engagements. Used by the Methodology, Work Plan, and Financial Proposal sections to scope, price, and operationalise the six lifecycle programs.

## Why Lifecycle Communications Belong in the Implementation Proposal

- Adoption, expansion, retention, and advocacy are downstream of lifecycle communication quality.
- Modern SaaS engagement is omnichannel: email, in-app, SMS, push, and webhook-driven workflows.
- Lifecycle programs require data implementation, content production, automation engineering, measurement, and continuous optimisation — engineering-grade work, not marketing afterthought.
- Premium agencies scope each program as a separate, priced workstream with named outcomes.

## The Six Lifecycle Programs (Engine Vocabulary)

| Program | Goal | Triggers | Primary Channel | Measurement |
|---|---|---|---|---|
| Acquisition | Convert leads to trial or first-call | Form submission, content download, demo request, ad-click | Email + retargeting | Trial signup rate, demo show-up rate |
| Activation | Move new accounts from signup to first value | Signup, role assignment, first login, first action | Email + in-app + admin nudge | TTV, activation rate, % achieving first-value within X days |
| Engagement | Sustain product use and deepen feature adoption | Behavioural events, dormancy windows, feature-launch | In-app + email + push | DAU/MAU, feature-adoption rate, stickiness |
| Expansion | Surface upgrade, cross-sell, and seat-expansion moments | Usage threshold, feature-gate touch, manager invite | Email + in-app + CSM outreach | Expansion ARR, attach rate, tier upgrade rate |
| Retention | Protect renewal and recover at-risk accounts | Renewal window, usage drop, sponsor change, support spike | Email + CSM call + executive outreach | Gross retention, save rate, NPS recovery |
| Advocacy | Convert satisfied customers into referrers, case studies, references | Health-score peak, NPS promoter, milestone achievement | Email + relationship outreach | Referral rate, reference availability, case-study yield |

Note: this re-statement keeps the six-program structure widely used in modern SaaS lifecycle thinking, but in the engine's own vocabulary so it can be used in proposals without naming any specific source.

## Workstream 1: Data Implementation Plan

The lifecycle program rests on a clean data layer. The proposal scopes this as the first lifecycle workstream.

- **Identify schema**: customer, account, user, role, segment, lifecycle stage, lifecycle program flags.
- **Event schema**: signup, activation, in-product actions, billing events, support events, customer-success events.
- **Custom fields**: vertical-specific fields (e.g., for insurance: policy count, claims volume; for banking: customer count, transaction volume).
- **Identity resolution**: linking the same user across product, marketing automation, CRM, support.
- **Consent and preference**: lawful basis, opt-in records, channel preferences, frequency caps.
- **Segmentation**: standard segments at launch (by tier, by lifecycle stage, by health, by industry).
- **Data hygiene**: bounce handling, suppression, decay, re-verification.

The data implementation plan is an engineering workstream priced independently of content production.

## Workstream 2: Content Production

For each program, content is produced in three layers:

- **Master content** — evergreen sequences, signed off by the client.
- **Triggered content** — event-driven sends with templated personalisation.
- **Manual outreach** — CSM-sent content with a defined cadence.

Content production is priced by the program × asset count.

## Workstream 3: Automation Engineering

- Marketing automation platform configuration.
- In-product messaging configuration.
- SMS / push provider integration (where applicable).
- Webhook and CRM-sync configuration.
- Suppression and frequency-cap engine.
- Holiday calendar and quiet-hours engine.

## Workstream 4: Operating Rules

Operating rules are documented and signed off by the client before any program goes live:

- Maximum touches per user per week (frequency cap).
- Quiet hours by time zone.
- Suppression triggers (recent support ticket, recent unsubscribe, recent purchase).
- Escalation rules (when a triggered comms suppresses to manual outreach).
- Holiday calendar.
- Compliance rules (regulator-specific content review, e.g., insurance and banking marketing copy).
- Brand voice and tone rules.

## Workstream 5: Measurement and Optimisation

- Per-program KPI dashboard (target by program, in the table above).
- Internal-control measurement: A/B for content variation, holdout for incrementality, propensity-matched comparisons for cohort programs.
- Avoid industry-benchmark comparisons — they signal weak measurement.
- Quarterly optimisation cycle: hypothesis, experiment, learning, scale-or-stop.
- Annual program review with the client's marketing, success, and product leadership.

## Pricing Drivers

| Driver | Why It Affects Price |
|---|---|
| Number of programs in scope (1–6) | More programs = more triggers, content, and engineering |
| Number of segments per program | More segments = more content variants, more measurement |
| Channels in scope (email only vs omnichannel) | Each additional channel adds engineering and operations |
| Languages in scope | Per-language content production and quality assurance |
| Vertical regulatory review | Banking, insurance, healthcare content reviews add cycle time |
| Continuous optimisation retainer | Number of experiments per quarter, content refresh cadence |

## Sample Scope-to-Price Matrix (Illustrative)

| Engagement Size | Programs | Channels | Languages | Indicative Build (one-time) | Indicative Run (monthly) |
|---|---|---|---|---|---|
| SMB | 3 (Activation, Engagement, Retention) | Email + in-app | 1 | [Indicative band] | [Indicative band] |
| Mid-market | 5 (all except Advocacy) | Email + in-app + SMS | 1–2 | [Indicative band] | [Indicative band] |
| Enterprise | 6 (all) | Email + in-app + SMS + webhook | 2–3 | [Indicative band] | [Indicative band] |

Replace indicative bands with engagement-specific pricing during proposal drafting, anchored on driver-based estimation.

## Anti-Patterns

- "Email setup" bundled invisibly as a sub-line of implementation — destroys the value defence for serious lifecycle work.
- Launching with all six programs at once — leads to thin content and unstable measurement.
- Using industry benchmarks instead of internal-control measurement.
- Touch limits set after launch rather than as operating rules at design time — leads to over-messaging incidents.
- Content review without regulator-aware review in regulated verticals.

## See Also

- `saas-customer-success-engagement-package.md` for the customer-success layer the lifecycle programs support.
- `saas-discovery-question-bank.md` Section L for the measurement-related discovery.
- `../data-management/SKILL.md` for the data-implementation-plan workstream depth.
- `../monitoring-and-evaluation/SKILL.md` for the measurement standard.
