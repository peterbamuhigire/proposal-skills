# AI-on-SaaS Team Composition Template

Roster template, RACI, ramp curve, and blended-rate considerations for AI-on-SaaS engagements. Pairs with `ai-on-saas-team-composition`. Drops into proposal `07-team-composition` and the TECH-6 / equivalent procurement format.

## Standard Roster (Sample)

| # | Role | Side | Allocation | Phase ramp |
|---|---|---|---|---|
| 1 | Engagement Lead / Programme Manager | Agency | 0.4 FTE | Phases 1–7 |
| 2 | Sponsor / Executive Sponsor | Agency | 0.1 FTE | Phases 1–7 |
| 3 | Solution Architect (SaaS) | Agency | 0.6 FTE | Phases 1–5 |
| 4 | Control Plane Lead | Agency | 1.0 FTE | Phases 2–5 |
| 5 | Application Plane Lead | Agency | 1.0 FTE | Phases 3–5 |
| 6 | Security and Compliance Lead | Agency | 0.5 FTE | Phases 1–7 |
| 7 | Customer Success Lead | Agency | 0.5 FTE | Phases 5–7 |
| 8 | SRE | Agency | 0.5 FTE | Phases 4–7 |
| 9 | DevOps Engineer | Agency | 0.6 FTE | Phases 2–6 |
| 10 | AI Solution Architect / ML Lead | Agency | 0.8 FTE | Phases 1–7 |
| 11 | Prompt Engineer | Agency | 0.6 FTE | Phases 2–6 |
| 12 | AI Safety Lead | Agency | 0.4 FTE | Phases 1–7 |
| 13 | Eval Engineer | Agency | 0.6 FTE | Phases 1–7 |
| 14 | MLOps Engineer | Agency | 0.6 FTE | Phases 2–7 |
| 15 | Data Engineer (AI) | Agency | 0.6 FTE | Phases 1–5 |
| 16 | RAG / Retrieval Engineer | Agency | 0.5 FTE | Phases 2–5 |
| 17 | AI Change and Adoption Lead | Agency | 0.3 FTE | Phases 4–7 |
| 18 | QA Lead | Agency | 0.6 FTE | Phases 3–6 |
| 19 | Project Manager | Agency | 0.5 FTE | Phases 1–7 |

The roster scales up or down with engagement size. Roles 12, 13, and 14 (AI Safety, Eval, MLOps) are the irreducible AI-side trio — no AI-on-SaaS engagement should ship without them named.

## Buyer-Side Counterparts (Two-of-Everything Rule)

| Agency role | Buyer-side counterpart | Knowledge transfer milestone |
|---|---|---|
| AI Safety Lead | AI Safety Sponsor (buyer DPO or CISO or designated) | Phase 4 close |
| Eval Engineer | Eval Owner | Phase 5 close |
| Prompt Engineer | Prompt Owner | Phase 5 close |
| MLOps Engineer | Model Gateway Operator | Phase 6 mid |
| Customer Success Lead | CS Manager | Phase 6 mid |

## RACI — Sample

| Workstream | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Tenant isolation ADR | Solution Architect | Engagement Lead | CISO, DPO, Product Owner | SteerCo |
| Model gateway | MLOps Engineer | ML Lead | AI Safety, Security | SteerCo |
| Eval CI | Eval Engineer | ML Lead | AI Safety | SteerCo |
| Red-team | AI Safety Lead | Engagement Lead | Security, External RT | SteerCo |
| Hallucination SLO | Eval Engineer | AI Safety Lead | Product Owner | SteerCo, AI Gov Forum |
| Responsible-AI commitment | AI Safety Lead | Sponsor | DPO, CISO, Legal | SteerCo, Board |
| Trust portal | Security Lead | Engagement Lead | DPO | SteerCo |
| Adoption | AI Change Lead | Sponsor | CS Lead | SteerCo |

## Ramp Curve — Sample

Phases 1 → 7 with FTE level per role. AI safety, eval, and red-team must ramp at Phase 1, not at hardening — late ramp produces eval theatre, not eval discipline.

## Blended-Rate Table — Sample (USD, indicative)

| Role | Day rate (USD) |
|---|---|
| Engagement Lead | 1 600 |
| Solution Architect (SaaS) | 1 400 |
| AI Solution Architect / ML Lead | 1 600 |
| AI Safety Lead | 1 500 |
| Eval Engineer | 1 200 |
| Prompt Engineer | 1 100 |
| MLOps Engineer | 1 200 |
| Data Engineer (AI) | 1 100 |
| RAG Engineer | 1 100 |
| Control Plane Lead | 1 300 |
| Application Plane Lead | 1 300 |
| SRE | 1 100 |
| DevOps Engineer | 1 000 |
| QA Lead | 1 000 |
| Customer Success Lead | 1 000 |
| Project Manager | 1 100 |
| Security and Compliance Lead | 1 300 |
| AI Change Lead | 1 100 |

Tune to local-market rates and procurement framework. PPDA Uganda, AfDB, World Bank and UNDP have their own format. Day rates published here are indicative; the proposal financial section drives the final figures from the agency profile and the buyer's framework.

## TECH-6 Mapping (World Bank)

Key Experts:
- Team Leader (Engagement Lead).
- Senior SaaS Solution Architect.
- AI Solution Architect / ML Lead.
- AI Safety Lead.
- Eval Engineer.
- Security and Compliance Lead.

Non-Key Experts:
- All other roles per TECH-6 non-key expert categories.

## Sample CV Bullets (for Relevant Experience or CV format)

- **AI Safety Lead, [Engagement]** — operated the Responsible-AI commitment for an X-tenant SaaS in [vertical]; chaired the AI Governance Forum; signed quarterly Responsible-AI reports; led quarterly red-team and annual independent red-team.
- **Eval Engineer, [Engagement]** — assembled and maintained N-case golden datasets across M AI features; integrated CI eval gates blocking deploys on threshold breach; led monthly eval refresh and quarterly golden-set refresh; reduced hallucination rate from X % to Y %.
- **ML Lead, [Engagement]** — owned the AI plane; selected models against the golden set across [Anthropic / OpenAI / Google / open-weight]; designed the model gateway with two-provider fallback; produced model cards for each launched feature.
- **MLOps Engineer, [Engagement]** — operated the model gateway and registry; built the region-routing matrix per residency policy; operated daily drift watch with rollback automation.
- **Prompt Engineer, [Engagement]** — designed and version-controlled the prompt library; designed citation-grounded RAG; designed abstain logic verified against the should-abstain subset.

## Cross-References

- `ai-on-saas-methodology-blocks.md` — workstreams the roster covers.
- `ai-on-saas-change-management-playbook.md` — change role overlap.
- `ai-on-saas-responsible-ai-commitment.md` — accountable-role detail.
- `07-team-composition/SKILL.md` — TECH-6 and narrative format discipline.
