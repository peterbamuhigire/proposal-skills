# How to Run a SaaS Business (Mersch) — Proposal Extraction (2026)

Internal synthesis for the proposal-skills engine. Source: Eric Mersch, *How to Run a SaaS Business: Lessons Learned from a Trio of Billion Dollar Companies* (2023, sometimes packaged as *Hacking SaaS*). Use as audit trail and implementation source, not for redistribution.

## Source Awareness

The book is the CFO-perspective manual on SaaS commercial structure and metrics:

- Part 1 — SaaS 101: SaaS vs perpetual licence models, SaaS financial reporting, top-line metrics, unit economics, financial metrics, using SaaS metrics for management decisions.
- Part 2 — Customer-centric SaaS models: Enterprise financial profile, enterprise GTM, enterprise metrics, SMM financial profile and GTM, SMM metrics, B2C financial profile, B2C GTM, B2C metrics.
- Part 3 — Industry-centric models: horizontal vs vertical SaaS models.
- Extensive glossary of SaaS commercial terms (ARR, MRR, ACV, TCV, RPO, CAC, LTV, payback, magic number, quick ratio, Rule of 40, dollar-based net retention, gross churn, net churn, sales capacity plan, OTE, commission accelerators, professional services attach rate, etc.).

## Copyright Boundary

- No reproduction of the book's defined formulas as named artefacts attributable to the book.
- The metric formulas are standard industry definitions and can be used as commodity SaaS terminology, but tables, examples, and the trio of billion-dollar case studies must not be reproduced.

## Proposal-Relevant Synthesis

### SaaS Financial Literacy for Premium Proposals
Premium SaaS implementation proposals must show CFO-grade fluency in:

- **Top-line**: ARR, MRR, bookings (new, expansion, renewal), billings, deferred revenue, RPO (deferred revenue + backlog).
- **Unit economics**: CAC by channel, CAC payback period, LTV, LTV:CAC ratio, gross margin, contribution margin per customer.
- **Retention**: gross dollar churn, net churn, dollar-based net retention/expansion, renewal rate vs retention rate (and why they differ).
- **Efficiency**: magic number, sales efficiency, Rule of 40, quick ratio, burn multiple, professional services attach rate (PSAR).
- **Sales capacity**: AE quota, productivity factor (over-assignment), OTE structure, commission with accelerators, ramp time.

The business-case and ROI section of every premium SaaS implementation proposal should use this vocabulary where the client owns or will own SaaS economics — and explicitly avoid it where the client is purely an internal user, where TCO and time-to-value are the right anchors.

### Segment-Differentiated GTM
Mersch's separation of Enterprise, SMM, and B2C SaaS models has direct proposal implications:

- **Enterprise SaaS**: long cycle, ACV $50k+, sales-led, professional-services-heavy, multi-year contracts, high gross retention, expansion-revenue-driven. Proposal language emphasises governance, security, change management, integration, success engineering, executive sponsorship, and reference architectures.
- **SMM SaaS**: mid-cycle, ACV $5k–50k, hybrid sales + self-serve, light professional services. Proposal language emphasises time-to-value, onboarding velocity, low-touch success, in-product engagement, and structured trial-to-paid conversion.
- **B2C SaaS**: short cycle, low ACV, self-serve only, content/SEO/paid-acquisition led, high churn tolerated against high acquisition volume. Proposal language emphasises acquisition funnels, activation, in-app behavioural triggers, lifecycle email, and unit economics tuned for volume.

The engine's vertical-positioning skill must declare the segment shape of each engagement.

### Horizontal vs Vertical SaaS Models
The book's horizontal/vertical chapter supports the engine's vertical-positioning brief. Vertical SaaS in regulated industries (financial services, insurance, healthcare) commands higher ACV, longer retention, and deeper integration — and therefore higher implementation fees. The proposal's value defence in vertical contexts must lean on regulatory-compliance, vertical-specific-workflow, and integration-with-vertical-systems language.

### Sales Capacity, Quota, and OTE for Internal SaaS Sales Teams
When the implementation includes standing up a client-side SaaS sales team (for vendors of SaaS, or for revenue-generating digital products inside banks/insurers/public sector), the proposal must scope: quota design, OTE structure, ramp plan, commission with accelerators, productivity assumptions, and the sales-capacity-plan artefact. This is engineering-grade work, not "we'll help with sales."

### Professional Services Attach Rate (PSAR)
The PSAR metric (services revenue / subscription bookings) is a useful evaluator-facing number to call out in financial proposals: it justifies a non-trivial services fee against the SaaS licence cost in a way that vendor-managed SaaS clients understand.

### Rule of 40, Magic Number, Quick Ratio
For premium SaaS proposals to investor-backed clients or PE-owned SaaS targets, including a Rule-of-40 or magic-number reference in the business case demonstrates the agency speaks the buyer's commercial language. Use sparingly and only where the buyer is investor-grade.

## Repository Changes Driven

- New skill: `skills/saas-proposals/saas-business-case-and-roi-modeling/` — TCO, ROI, payback, LTV/CAC, Rule of 40, business-case template.
- New reference: `saas-business-case-and-roi-template.md` — TCO vs on-prem, CAC payback, LTV uplift, retention uplift, sensitivity.
- New reference: `saas-metrics-glossary-for-proposals.md` — ARR, MRR, ACV, TCV, RPO, NRR, gross churn, magic number, Rule of 40, PSAR, etc., explained in the engine's own words for proposal use.
- Enhancement: `skills/pipeline/10-financial-proposal/` adds SaaS pricing model variants (subscription, usage, hybrid, enterprise tiering) and PSAR framing.
- Enhancement: `skills/pipeline/02-executive-summary/` and `skills/strategy-positioning/premium-client-proposal-strategy/` add Rule-of-40 / magic-number language for investor-grade clients.

## Quality Guardrails

- Do not reproduce Mersch's specific examples, the three billion-dollar case studies, or his glossary entries verbatim.
- Treat SaaS metric formulas as commodity vocabulary and re-define them in the engine's own words.
- Reserve investor-grade vocabulary (Rule of 40, magic number) for proposals where the buyer is structurally investor-aware.
