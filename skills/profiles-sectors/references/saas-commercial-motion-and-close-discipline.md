# SaaS Commercial Motion and Close Discipline

Parents: [SaaS discovery and qualification](../../saas-proposals/saas-discovery-and-qualification/SKILL.md), [SaaS mutual action planning and close plans](../../saas-proposals/saas-mutual-action-planning-and-close-plans/SKILL.md), [SaaS pricing and packaging](../../saas-proposals/saas-pricing-and-packaging-proposal/SKILL.md). Related: [SaaS GTM motion design](saas-gtm-motion-design-reference.md), [SaaS metrics glossary](saas-metrics-glossary-for-proposals.md).

**When to read:** when a SaaS implementation, SaaS product-development or SaaS commercial-launch proposal needs the closing and commercial-design disciplines below. These consolidate capabilities previously documented only in the engine's 2026 SaaS audit notes, rewritten as task guidance on 2026-09-23.

Concept inputs (durable ideas only): Winning by Design, *The SaaS Sales Method for Account Executives* (2018) and *The SaaS Sales Method Fundamentals*; Walling, R. (2023) *The SaaS Playbook*; Mersch, E. (2023) *How to Run a SaaS Business*; Cotton, B. *Hacking SaaS*; Garbugli, É. *The SaaS Email Marketing Playbook*; Golding, T. (2024) *Building Multi-Tenant SaaS Architectures*, O'Reilly. Named proprietary techniques and figures from these sources are not reproduced.

## 1. Three proposal layers for premium SaaS bids

| Layer | Reader | Content |
|---|---|---|
| Quote | Procurement | Line-item pricing, terms, assumptions |
| Impact proposal | Business owner | The client's value in its own language: paid back, risk reduced, time to value |
| Business case | Finance | Net present value, payback, return, sensitivity and break-even (see the SaaS business-case template) |

Produce all three; a price sheet alone leaves value undefended.

## 2. Not-a-fit discipline

State explicitly the conditions under which the engagement should not proceed (for example no executive sponsor, no data access, a timeline that cannot include testing). It builds credibility and removes the "we will say yes to anything" impression.

## 3. Buyer silence ("going dark")

Do not chase. Maintain an alert layer (news, hiring, regulatory events), send insight rather than status checks, and re-engage through the agreed sponsor route with a proposed decision date. Every follow-up carries fresh value or a proof point.

## 4. Mirrored engagement (role coverage)

Match our senior roles to the buyer's decision roles, for example executive to executive sponsor, solution lead to technical owner, delivery lead to operations owner, so that each buyer role has a named counterpart through selection, contract and go-live.

## 5. Trade discipline

Never give without getting. Pair every concession with a trade: scope, term, payment terms, references, case-study rights, user count or earlier start. Time-bound mutual incentives (an accelerated close) must be genuine and documented. See [strategic-account negotiation](../../strategy-positioning/premium-pricing-and-value-defense/references/strategic-account-negotiation.md).

## 6. Segment shape of the engagement

Declare which shape the client's SaaS business has, because it changes the proposal's language:

| Shape | Typical traits | Proposal emphasis |
|---|---|---|
| Enterprise | Long cycles, higher contract values, sales-led, services-heavy, multi-year contracts | Governance, security, integration, change management, success engineering, executive sponsorship |
| Mid-market | Mid-length cycles, hybrid sales and self-serve, light services | Time to value, onboarding speed, low-touch success, trial-to-paid conversion |
| Consumer | Short cycles, low prices, self-serve, high churn tolerated | Acquisition funnels, activation, in-app triggers, lifecycle messaging, volume unit economics |

Use investor-grade vocabulary (Rule of 40, magic number, services attach rate) only where the buyer is structurally investor-aware.

## 7. Commercial design choices for client-owned SaaS revenue models

- **Dual funnels:** when the product serves two buyer segments (self-serve and sales-led), design two funnels and name the primary motion; never force both through one.
- **Expansion path from day one:** decide which features, volumes or seats become billable later and what triggers the upgrade conversation.
- **Path to net negative churn:** expansion revenue from existing customers exceeding revenue lost to churn and contraction; scope at-risk identification, save plays and win-back plays.
- **Phased funding for capital-light clients:** design the first phase to reach the first paying customers and the first recurring revenue, then fund later phases from that revenue.
- **Freemium or paid trial:** freemium only where viral or self-serve conversion is structurally credible; otherwise a paid or card-first trial.
- **Price increases:** include cadence, communication, grandfathering rules and operational steps.

## 8. Health dashboard: growth and drag measures

Report three growth measures (for example paid sign-ups, expansion revenue, activation rate) and three drag measures (for example churn, time to first value, support cost per account), defined in the engine's metrics glossary.

## 9. Workstreams to scope explicitly when relevant

- **Sales enablement** for clients with a sales function: playbooks, training, CRM configuration, lead-routing rules and a 90-day handover review.
- **Sales capacity plan** when standing up a client sales team: quota design, on-target earnings structure, ramp plan, commissions and productivity assumptions.
- **Channel-portfolio review** at a fixed cadence with reallocation triggers; channels and tactics lose effectiveness over time, so never tie a launch to a single channel without monitoring.
- **Hypothesis and experiment register** for pricing and channel tests.
- **Lifecycle communications operating rules:** frequency caps, suppression, escalation, holiday calendars; internal-control measurement (A/B or holdout) rather than industry benchmarks.
- **Recurring meetings:** each has a stated purpose, a named artefact produced and a decision required by the close.

## 10. Architecture credibility reminders

Name both the control plane and the application plane; treat tenant context as a concern in every service; scope cost attribution per tenant and noisy-neighbour management; commit to automated tenant onboarding; for migration from installed software, scope tenant model selection, data migration, parallel run, customer-by-customer cutover and retirement of legacy support. Detail lives in the [multi-tenant architecture block](saas-multi-tenant-architecture-block.md) and [implementation methodology blocks](saas-implementation-methodology-blocks.md).

## 11. Discovery conversation discipline

Record every discovery conversation against one template (situation, pain, impact, decision process, decision criteria, timing) so it feeds the brief and the methodology's diagnosis phase directly. Every interaction should be relevant to the buyer's current situation, respectful of their time, and recent enough to reflect what has changed. Separate objections (addressable concerns) from rejections (no current fit), and make every follow-up carry a fresh insight or proof point rather than a status check. Question lists live in the [SaaS discovery question bank](saas-discovery-question-bank.md).
