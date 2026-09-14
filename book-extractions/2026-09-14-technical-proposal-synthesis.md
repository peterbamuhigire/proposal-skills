# Book-informed technical-proposal synthesis

Status: adopted on 2026-09-14 for technology-related proposals.

## Technical proposal bridge

Translate the buyer's outcome into a small number of realistic scenarios.
For each scenario, show:

1. the current pain, user/operator job, and measurable outcome;
2. the proposed capability and system boundary;
3. the delivery slice, dependencies, assumptions, and decision gates;
4. acceptance tests, non-functional budgets, security/identity controls,
   observability, support, and handover evidence;
5. risks, failure and rollback paths, ownership, and cost drivers.

The methodology must explain how evidence is produced, not merely list
activities. Link claims about scale, availability, performance, AI quality,
security, and team capability to evidence or mark them as assumptions requiring
confirmation. Separate discovery and validation from build commitments when
data, integrations, or user behaviour are uncertain.

## Engineering credibility checks

- Describe architecture by behaviour, workload, trust boundaries, and
  trade-offs, not brand names alone.
- State API and data contracts, identity lifecycle, authorisation scope,
  versioning, errors, migration, and deprecation where relevant.
- Treat AI output as a hypothesis until representative evaluation cases,
  thresholds, human oversight, privacy controls, and fallback are defined.
- Price or qualify model/API usage, hosting, support, training, governance,
  optimisation, and operational ownership as separate cost drivers.
- Keep technical and financial envelopes consistent without hiding uncertainty
  in a lump-sum promise.
- Use a narrow pilot or staged release when it reduces an irreversible risk;
  define the evidence required to expand.

## Deliberate exclusions

- No invented case studies, buyer facts, current technology claims, prices, or
  certifications.
- No generic architecture appendix that is disconnected from the proposed
  outcome and work plan.
- No proposal promise that lacks a delivery owner, acceptance evidence, or
  maintenance path.

## Sources

- Drew Hoskins, The Product-Minded Engineer.
- Aditya Chatterjee, Ue Kiao, Chew Chee Keng and contributors, System Design at
  Google: Engineering Peak for Interviews.
- Almantas Karpavičius, Software Craftsmanship Using AI.
- Nordic APIs, Identity and APIs: Techniques to Mature Platform Security.
- Adrienne Braganza, Looks Good to Me: Constructive Code Reviews.
