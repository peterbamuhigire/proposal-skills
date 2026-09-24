# Technical Proposal Evidence Bridge

Parents: [proposal router](../../SKILL.md), [06-methodology](../../pipeline/06-methodology/SKILL.md), [08-work-plan](../../pipeline/08-work-plan/SKILL.md), [critical-analysis-business-logic](../../strategy-positioning/critical-analysis-business-logic/SKILL.md).

**When to read:** for any technology-related proposal (software, SaaS, AI, websites, integration, data, cloud) when writing methodology, work plan, acceptance, risk or cost sections. It turns a buyer outcome into scenarios that produce verifiable engineering evidence. Adopted 2026-09-14 for technology proposals; moved to this location 2026-09-23.

Concept inputs (durable ideas only, no text reproduced): Hoskins, D. *The Product-Minded Engineer*; Chatterjee, A., Kiao, U., Keng, C. C. et al. *System Design at Google*; Karpavičius, A. *Software Craftsmanship Using AI*; Nordic APIs *Identity and APIs*; Braganza, A. *Looks Good to Me: Constructive Code Reviews*. Publishers and years: verify before citing externally.

## 1. The bridge: outcome → scenarios → evidence

Translate the buyer's outcome into a small number of realistic scenarios. For each scenario, show:

1. the current pain, the user or operator job, and the measurable outcome;
2. the proposed capability and its system boundary;
3. the delivery slice, dependencies, assumptions and decision gates;
4. acceptance tests, non-functional budgets, security and identity controls, observability, support and handover evidence;
5. risks, failure and rollback paths, ownership and cost drivers.

The methodology must explain how evidence is produced, not merely list activities. Link claims about scale, availability, performance, AI quality, security and team capability to evidence, or mark them as assumptions requiring confirmation. Separate discovery and validation from build commitments when data, integrations or user behaviour are uncertain.

## 2. Engineering credibility checks

- Describe architecture by behaviour, workload, trust boundaries and trade-offs, not brand names alone.
- State API and data contracts, identity lifecycle, authorisation scope, versioning, errors, migration and deprecation where relevant.
- Treat AI output as a hypothesis until representative evaluation cases, thresholds, human oversight, privacy controls and fallback are defined.
- Price or qualify model and API usage, hosting, support, training, governance, optimisation and operational ownership as separate cost drivers.
- Keep technical and financial envelopes consistent without hiding uncertainty in a lump-sum promise.
- Use a narrow pilot or staged release when it reduces an irreversible risk; define the evidence required to expand.
- Where the website or web application must meet performance or accessibility targets, cite only current, registered thresholds (for example Core Web Vitals per web.dev, checked 2026-09, claim CW-01; WCAG 2.2 Level AA, claim CW-05) and state that WCAG 3 is a draft.

## 3. Scheduling the evidence (work plan)

Schedule validation, review, QA, rollout, support and optimisation as real delivery events with owners and dates, not as a line at the end. Each scenario's acceptance evidence appears as a milestone in the [work plan](../../pipeline/08-work-plan/SKILL.md).

## 4. Deliberate exclusions

- No invented case studies, buyer facts, current technology claims, prices or certifications.
- No generic architecture appendix disconnected from the proposed outcome and work plan.
- No proposal promise that lacks a delivery owner, acceptance evidence or a maintenance path.

## 5. Handoffs

Formal requirements go to the SRS engine; implementation doctrine to the engineering engine (`chwezi-dev-engine`); resolve both through the global routing table. The proposal owns the promise and its evidence plan, not the engineering method.
