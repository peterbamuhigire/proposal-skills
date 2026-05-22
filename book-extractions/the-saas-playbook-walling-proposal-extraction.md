# The SaaS Playbook (Walling) — Proposal Extraction (2026)

Internal synthesis for the proposal-skills engine. Source: Rob Walling, *The SaaS Playbook: Build a Multimillion Dollar Startup Without Venture Capital* (2023). Use as audit trail and implementation source, not for redistribution.

## Source Awareness

The book covers strengthening product-market fit, competing in crowded markets, building moats, pricing structure, expansion revenue, freemium decisions, credit-card-up-front trade-offs, raising prices, marketing funnels, dual funnels, B2B SaaS marketing approaches, sales-demo structure, team design, manager hiring, equity and stock options, the 80/20 SaaS metrics framework (3-high / 3-low), virality, churn, net negative churn, and founder mindset.

## Copyright Boundary

- No reproduction of named "cheat code" frameworks, dual-funnel diagrams, or the 3-high / 3-low table.
- Translate principles into the engine's vertical-positioning, pricing, and metrics guidance.

## Proposal-Relevant Synthesis

### Vertical SaaS Positioning and Niche
Walling's central thesis — that durable SaaS businesses pick a defensible niche and beat horizontal generalists through depth — directly informs the engine's vertical-positioning library. For an African-region agency, the realistic verticals to position SaaS implementation expertise in are: financial services (banking, microfinance, payments), insurance, public sector and revenue authorities, healthcare (private hospital chains, NHIS-style schemes), education (universities, EdTech), agribusiness and supply chain, NGO programme operations, and SMB ERP. Each vertical needs a proposal-ready positioning brief that names the regulatory landscape, the dominant pain pattern, the buyer roles, the proof points the agency holds, and the realistic price ceiling.

### Pricing Structure, Expansion, and Raising Prices
The book's pricing chapters translate to proposal-grade guidance:

- **Tiering**: every SaaS implementation proposal that recommends a client-facing SaaS commercial model should propose three tiers, with expansion paths designed in (per-seat, per-volume, per-feature-gate).
- **Expansion revenue** is treated as the cheat code. The proposal should design the expansion path on day one: which features, volumes, or seats become billable later, and what triggers the upgrade conversation.
- **Freemium decisions**: include a freemium pro-and-con block in proposals where the SaaS reaches end users directly. Default position: freemium only where viral acquisition or self-serve conversion is structurally credible — otherwise paid trial.
- **Credit-card-up-front**: the proposal can recommend a paid-trial-with-card model when the buyer is risk-tolerant and trial-quality matters more than trial-quantity.
- **Raising prices**: include a price-increase clause in the SaaS commercial design: cadence, communication, grandfathering rules, and the operational steps required to execute.

### Marketing Approaches and Dual Funnels
The dual-funnel idea (separate funnels for trial-led self-serve and sales-led enterprise) supports the proposal anti-pattern call-out: never design a SaaS commercial launch with a single funnel when the product clearly serves two buyer segments. The methodology should call out which funnel is the primary motion and which is the parallel.

### Sales Demo Structure
The book's demo structure (problem-first, then specific-to-prospect, then proof) maps to the engine's POC scoping language. The proposal should commit to demo design as a deliverable: discovery-tuned demo scripts, a demo environment, and a recorded library of role-specific demos for hand-over.

### The 80/20 SaaS Metrics Framework
The 3-high / 3-low metrics idea (three metrics you want high, three you want low) is operationalised in the engine as the SaaS health dashboard inside the M&E and customer-success sections. In engine vocabulary: three growth metrics (e.g., paid signups, expansion revenue, activation rate) and three drag metrics (e.g., churn, time-to-first-value, support cost per account).

### Churn and Net Negative Churn
The proposal must include a churn-protection workstream where the client owns or will own a SaaS revenue model: at-risk identification, save plays, win-back plays, and the path to net negative churn through expansion that exceeds churn.

### Bootstrap-Friendly Cost Discipline
For African-context proposals where many clients are capital-light, Walling's bootstrap-friendly framing supports a commercial-options approach: the agency proposes a phased implementation that achieves first paying customers and first dollar of recurring revenue inside the first phase, then funds further phases from the SaaS revenue line itself.

## Repository Changes Driven

- New skill: `skills/saas-proposals/saas-vertical-positioning/` — vertical positioning briefs for financial services, insurance, public sector, healthcare, education.
- New reference: `vertical-saas-positioning-financial-services.md`.
- New reference: `vertical-saas-positioning-insurance.md`.
- New reference: `vertical-saas-positioning-public-sector.md`.
- New reference: `saas-pricing-models-reference.md` — tiering, expansion, freemium, paid trial, price increases.
- New skill: `skills/saas-proposals/saas-pricing-and-packaging-proposal/` — applies pricing-model guidance for client-owned SaaS commercial models inside implementation engagements.
- Enhancement: `skills/domain-delivery/monitoring-and-evaluation/` adds the SaaS health-dashboard pattern.
- Enhancement: `skills/strategy-positioning/premium-pricing-and-value-defense/` adds SaaS-specific commercial options.

## Quality Guardrails

- Do not reproduce "SaaS Cheat Code" naming or the 3-high / 3-low specific list as labelled artefacts.
- Translate to engine vocabulary: "growth metrics" / "drag metrics", "expansion path", "tier ladder".
- Keep examples grounded in the engine's actual African and global vertical-SaaS context.
