# SaaS GTM Motion Design Reference

Go-to-market motion design for SaaS implementation and SaaS product-development engagements where the client owns or will own a SaaS revenue model. Use inside the Methodology, Work Plan, and Financial Proposal when the engagement scope includes commercial launch, GTM redesign, or sales-team build.

## Motion Patterns

| Motion | Pattern | Typical ACV | Sales Cycle | Best for |
|---|---|---|---|---|
| Product-Led Growth (PLG) | Self-serve trial → activation → conversion → expansion | Low to mid | Days to weeks | Productivity SaaS, developer tools, low-friction B2C-adjacent SaaS |
| Inside Sales | SDR outbound + AE close, mostly remote | Mid | Weeks to a quarter | SMM B2B SaaS, mid-market |
| Field Sales | Named-account AE + sales engineering, often in person | Enterprise | One to three quarters | Enterprise B2B, regulated industries, complex integration |
| Partner / Channel | Reseller, system integrator, OEM, BaaS | Varies | Varies | Geographic expansion, regulated entry, embedded capability |
| Community / Open Source | Open-source core + commercial extension | Mid | Weeks to a quarter | Developer-targeted SaaS, infrastructure SaaS |
| Hybrid | PLG self-serve at low end + Inside Sales at mid + Field at top | Tiered | Tiered | Broad-market SaaS that serves multiple segment shapes |

## Motion Selection Decision

1. What is the typical ACV target? (Determines the unit economics that can sustain each motion.)
2. What is the buyer-discovery and product-evaluation pattern in the target market? (Self-serve vs assisted.)
3. What is the integration depth required by typical customers? (Determines need for sales engineering.)
4. What is the regulatory complexity of typical customers? (Determines need for compliance-aware GTM.)
5. What is the founder or executive team's experience? (Determines what motion they can credibly stand up.)

Most resale SaaS engagements end up with a hybrid motion. The proposal should declare which motion is the primary engine and which is the parallel.

## Channel Design

For each motion, the proposal scopes a channel portfolio:

| Channel | Strengths | Risks | Decay Watch |
|---|---|---|---|
| Inbound: content / SEO | Compounding, defensible, cheap at scale | Slow to start, sensitive to algorithm changes | Search and AI-search reformatting |
| Inbound: paid search | Predictable, measurable | Cost-per-click rises with competition | Click-cost decay, conversion-rate decay |
| Inbound: paid social | Targetable, fast | High variance, ad-fatigue | Platform shifts, audience aging |
| Outbound: SDR-driven | Targetable, measurable, controllable | Expensive per meeting, deliverability risk | Email deliverability, response-rate decay |
| Events and conferences | Trust-building, deal-acceleration | Expensive, hard to attribute | Audience shift to virtual / hybrid |
| Partner / reseller | Geographic and vertical reach | Margin share, partner-management overhead | Partner attention, conflict with direct |
| Community / open source | Trust, developer reach | Conversion-to-paid challenge | Open-source-to-paid skepticism |
| Referrals | High trust, low CAC | Hard to scale beyond a ceiling | Referrer fatigue |

Every channel has decay characteristics. The proposal commits to a quarterly channel review with explicit reallocation triggers.

## Sales-Team Design

For engagements that include standing up a SaaS sales function:

- **AE (Account Executive)**: quota-carrying closer. Quota typically 5–8× OTE.
- **SDR (Sales Development Representative)**: top-of-funnel, books meetings. Typically 1–2 SDRs per AE.
- **Sales Engineering**: technical depth in demos, POCs, security questionnaires. Often 1 SE per 2–4 AEs at enterprise.
- **Sales Operations**: tooling, reporting, deal-desk, commission, capacity planning.
- **Sales Enablement**: playbook, onboarding, content, training, certification.

Never build a SaaS sales team with one rep. The minimum viable team is two AEs (one to benchmark the other) plus an SDR and a shared SE.

## Sales Capacity Plan

The capacity plan for any proposed SaaS sales team has three components:

- Number of quota-carrying AEs.
- Quota per AE (annual, in ACV).
- Productivity factor (over-assignment factor — accounts for ramp time, attrition, and capacity loss).

Sales capacity = AEs × quota × productivity factor.

For new SaaS sales teams: productivity factor in year 1 is typically 0.5–0.7 of stated quota.

## Sales Enablement Workstream

For engagements that include sales enablement:

- **Playbook authorship**: discovery script, demo script, objection-handling library, close plays.
- **CRM configuration**: pipeline stages, exit criteria per stage, required fields per stage, reporting.
- **Lead routing**: SDR-to-AE handoff rules, territory rules, account-based assignment.
- **Onboarding curriculum**: 30/60/90-day ramp for new hires.
- **Certification**: AEs certify on product, vertical, and discovery before being released to live accounts.
- **Coaching cadence**: weekly 1:1, monthly deal review, quarterly skills review.
- **Content library**: case studies, comparable engagements, calculator tools, references.

## Pricing Experimentation Register

For engagements where the client owns SaaS pricing, propose a pricing-experimentation register:

| Hypothesis | Experiment | Cohort | Duration | Decision Rule |
|---|---|---|---|---|
| Tier-2 price increase of 10% maintains conversion | Half of new mid-market signups see the new price | 100 signups | 8 weeks | Proceed if conversion ≥ 90% of control |
| Per-seat to per-volume migration improves expansion | New customers on per-volume pricing | 50 new customers | 6 months | Proceed if NRR ≥ 10pp higher than control |
| Annual prepay discount tightening | New customers see 5% (vs 10%) annual prepay discount | 100 customers | 12 weeks | Proceed if prepay rate drops < 5pp |

Each experiment has named owners, named metrics, and a written learning at conclusion.

## Anti-Patterns

- Selecting a motion based on what the founder personally is comfortable with rather than what the market demands.
- Treating channels as fixed forever — channel decay is real and ignored at peril.
- Hiring AEs without SDR support and without SE depth — single-threaded selling that does not scale.
- Quota set arbitrarily rather than from capacity-plan logic.
- Pricing experiments without a written learning — repeats the same mistake.

## See Also

- `saas-pricing-models-reference.md` for the underlying pricing structures.
- `saas-business-case-and-roi-template.md` for the unit economics behind motion selection.
- `saas-metrics-glossary-for-proposals.md` for vocabulary.
- `saas-customer-success-engagement-package.md` for the post-sale layer.
- `saas-lifecycle-email-program-proposal-template.md` for the communication backbone.
