# SaaS Proposal Skills Audit 2026

Internal audit produced for the proposal-skills engine to bring it to Bain/EY/McKinsey-grade quality for SaaS implementation and SaaS product-development engagements. Use as the implementation source for new skills, enhancements, and cross-cutting references derived from the seven SaaS books processed in this session.

## Books Processed

| File | Source | Lens |
|---|---|---|
| `saas-sales-method-for-account-executives.md` | Winning by Design, *The SaaS Sales Method for AE* | Closing motion (Identify, Diagnose, Prescribe, Select, Propose, Pause, Trade, Commit), pain chain, decision process, MAP, business case |
| `saas-sales-method-fundamentals.md` | Winning by Design, *Fundamentals* | Conversation discipline, structured discovery, objection vs rejection, follow-up as system, meeting structure |
| `saas-email-marketing-playbook.md` | Étienne Garbugli | Six lifecycle email programs, data implementation plan, sequence pacing, operating rules, measurement |
| `hacking-saas.md` | Ben Cotton, essays | GTM motion design, channel decay/arbitrage, sales-marketing alignment, sales-team design, two-of-everything principle |
| `the-saas-playbook-walling.md` | Rob Walling | Vertical positioning, pricing tiering, expansion revenue, freemium decisions, raising prices, dual funnels, churn, net negative churn |
| `how-to-run-a-saas-business.md` | Eric Mersch, CFO perspective | SaaS financial vocabulary (ARR/MRR/ACV/RPO, CAC, LTV, payback, Rule of 40, magic number, PSAR), Enterprise vs SMM vs B2C model, horizontal vs vertical SaaS |
| `building-multi-tenant-saas-architectures.md` | Tod Golding (O'Reilly) | Control plane vs application plane, tenant isolation, tenant context, data partitioning, cost attribution, onboarding, multi-tenant migration |

## NEW SKILLS

Create the following under `skills/<skill-name>/` with `SKILL.md` and `references/` where useful.

| Skill | Purpose | Source Books / Chapters |
|---|---|---|
| `skills/saas-discovery-and-qualification/` | Discovery for SaaS opportunities: ICP, MEDDIC/CHAMP, pain chain, impact quantification, decision process (consensus vs hierarchy), critical event, sponsor/champion/blocker mapping. | AE book Stage 2 (Diagnose), Fundamentals communication chapters |
| `skills/saas-business-case-and-roi-modeling/` | Build TCO vs on-prem, time-to-value, CAC payback, LTV uplift, retention uplift, ROI, Rule of 40 framing for investor-grade clients, sensitivity analysis. | Mersch (entire book), AE Stage 5 |
| `skills/saas-pricing-and-packaging-proposal/` | Subscription, usage-based, hybrid, enterprise tiering; expansion paths; freemium decisions; paid-trial design; price-increase clauses. | Walling Pricing chapters, Mersch on commercial models |
| `skills/saas-implementation-methodology/` | End-to-end SaaS implementation methodology: control plane, application plane, tenant isolation, data partitioning, observability, billing integration, onboarding automation, cost attribution. | Golding (entire book) |
| `skills/saas-poc-and-pilot-scoping/` | Tightly scoped POC and pilot proposals: success criteria, exit criteria, time-box, decision-gate to full implementation. | AE Stage 3 Prescribe (Show/Demo), AE Stage 5 Propose |
| `skills/saas-procurement-and-security-questionnaire/` | Procurement navigation, security questionnaires, DPAs, MSAs, SLAs, exit clauses, escrow, data residency, sub-processors. | Cross-cutting from Golding (tenant isolation, residency), Mersch (enterprise GTM) |
| `skills/saas-customer-success-and-adoption-proposal/` | Customer success engagement package: onboarding, activation, success plan, QBR, expansion play, churn-risk monitoring, save plays. | Garbugli (lifecycle), Walling (churn / NNR), Mersch (NRR) |
| `skills/saas-mutual-action-planning-and-close-plans/` | MAP, close plan, commit logic, mutual responsibilities through to go-live. | AE Stage 8 Commit, Stage 7 Trade |
| `skills/saas-vertical-positioning/` | Vertical positioning briefs for African + global priority verticals: financial services, insurance, public sector, healthcare, education, agribusiness, NGO operations. | Walling (vertical SaaS), Mersch (vertical chapter) |
| `skills/saas-objection-handling-and-competitive-displacement/` | Competitive displacement plays (incumbent renewal, point solution, build-in-house, do-nothing), trade discipline, premium price objections. | AE Stages 4 and 7 |
| `skills/saas-lifecycle-communications-as-deliverable/` | Scopes six lifecycle communication programs (acquisition, activation, engagement, expansion, retention, advocacy) as priced workstreams inside SaaS engagements. | Garbugli (entire book) |
| `skills/saas-trust-and-compliance-credentials-section/` | Proposal section template covering security, compliance, certifications, sub-processors, BCDR, audit posture, regulator alignment. | Golding (tenant isolation, identity), procurement realities |
| `skills/saas-multi-tenant-architecture-credibility-block/` | Methodology-grade content block proving SaaS architectural literacy. | Golding (entire book) |
| `skills/saas-pilot-to-rollout-change-management/` | SaaS adoption change-management: per-tenant operations mindset, continuous-release culture, customer-success-replaces-install services. | Golding chapter 1 (SaaS mindset), AE Commit |

## ENHANCEMENTS TO EXISTING SKILLS

| Skill | What to Add | Source |
|---|---|---|
| `skills/sales-discovery-and-objection-handling/SKILL.md` | SaaS lens: ICP, MEDDIC/CHAMP overlay, pain-chain articulation, decision-process mapping (consensus vs hierarchy), trade discipline. | AE book + Fundamentals |
| `skills/premium-pricing-and-value-defense/SKILL.md` | SaaS commercial options (subscription, usage, hybrid, enterprise tier), expansion path, PSAR framing, TCO vs on-prem. | Mersch + Walling |
| `skills/ai-transformation-proposal/SKILL.md` | Cross-link to SaaS implementation methodology; tenant isolation requirements for AI-feature SaaS; lifecycle communications around AI features. | Golding + Garbugli |
| `skills/06-methodology/SKILL.md` | Standard phases for SaaS implementation: control plane, application plane, tenant isolation, data partitioning, observability, billing integration, cost attribution, onboarding automation, customer success. | Golding |
| `skills/08-work-plan/SKILL.md` | Recurring-meeting purpose-artefact-decision rule; lifecycle program build cadence; pilot-to-rollout gates. | Fundamentals + Garbugli |
| `skills/10-financial-proposal/SKILL.md` | SaaS pricing model variants and bundling (licence vs services vs implementation vs success); PSAR; payment schedule tied to SaaS go-live and first-paying-customer milestones; usage-based commercial structures. | Mersch + Walling |
| `skills/02-executive-summary/SKILL.md` | Critical event and pain-chain leadership; investor-grade vocabulary opt-in (Rule of 40, magic number) for the right buyers. | AE + Mersch |
| `skills/03-understanding-of-assignment/SKILL.md` | Pain chain articulation; ICP declaration; decision-process mapping. | AE |
| `skills/customer-service-and-maintenance-proposals/SKILL.md` | SaaS customer success engagement package; QBR cadence; expansion plays; save plays; lifecycle communications; churn-risk telemetry. | Walling + Garbugli + Mersch |
| `skills/change-management/SKILL.md` | SaaS mindset transition: per-tenant operations, continuous release, customer-success-replaces-install services. | Golding |
| `skills/monitoring-and-evaluation/SKILL.md` | SaaS health dashboard pattern (3 growth metrics, 3 drag metrics); NRR/GRR; internal-control measurement; lifecycle program A/B and holdout discipline. | Walling + Garbugli |
| `skills/risk-management/SKILL.md` | Tenant-isolation failure, noisy-neighbour, data-residency, sub-processor, exit-clause, SLA-penalty, migration risks. | Golding + procurement realities |
| `skills/data-management/SKILL.md` | Data implementation plan (custom fields, identify events, segmentation, journey mapping) as a SaaS lifecycle workstream. | Garbugli |
| `skills/05-relevant-experience/SKILL.md` | SaaS-implementation outcome anchors: time-to-value, activation rate, NRR uplift, churn reduction, expansion revenue, time-to-first-paying-customer. | Mersch + Walling |
| `skills/premium-client-proposal-strategy/SKILL.md` | SaaS-specific buyer level mapping (CRO, CFO, CIO, CISO, COO, head of digital), investor-grade vocabulary opt-in, vertical-SaaS positioning. | Mersch + Walling |
| `skills/07-team-composition/SKILL.md` | Two-of-everything redundancy principle for client-side critical roles after handover. | Cotton (Hacking SaaS) |

## REFERENCE FILES / TEMPLATES TO ADD

Place in `skills/references/` (cross-cutting) unless noted otherwise.

| Reference | Purpose |
|---|---|
| `saas-discovery-question-bank.md` | Pain chain, impact, decision criteria, decision process, critical event, sponsor/champion mapping. |
| `meddic-and-command-of-message-for-saas.md` | MEDDIC/MEDDPICC/CHAMP overlay for SaaS qualification inside proposals. |
| `saas-mutual-action-plan-template.md` | MAP template from close to go-live with shared task ownership. |
| `saas-demo-script-template.md` | Discovery-tuned demo script: problem-first, specific-to-prospect, proof, ask. |
| `saas-poc-scoping-template.md` | POC scope, success criteria, exit criteria, time-box, decision gate. |
| `saas-business-case-and-roi-template.md` | TCO vs on-prem, CAC payback, LTV uplift, retention uplift, ROI, NPV, sensitivity. |
| `saas-pricing-models-reference.md` | Subscription, usage-based, hybrid, enterprise tiering, expansion, freemium, paid trial, price-increase clauses. |
| `saas-procurement-and-security-questionnaire-playbook.md` | Security questionnaires, DPA, MSA, SLA, exit clauses, escrow, data residency, sub-processors. |
| `saas-msa-dpa-sla-template-language.md` | Reusable proposal-grade contract-language paragraphs (not legal advice; for proposal narrative). |
| `saas-customer-success-engagement-package.md` | Customer success scope: onboarding, activation, success plan, QBR, expansion, save plays, churn telemetry. |
| `saas-lifecycle-email-program-proposal-template.md` | Six lifecycle programs as priced workstreams, with data implementation plan and operating rules. |
| `saas-implementation-methodology-blocks.md` | Reusable Methodology section content for SaaS implementation engagements (control plane, application plane, tenant isolation, etc.). |
| `saas-risk-register-for-proposals.md` | Risk register specific to SaaS engagements (data residency, exit, escrow, noisy neighbour, vendor lock, model drift). |
| `vertical-saas-positioning-financial-services.md` | Banking, microfinance, payments — regulators, pain pattern, buyer roles, proof, price ceiling. |
| `vertical-saas-positioning-insurance.md` | Life, non-life, health, regulator alignment, claims/policy systems integration. |
| `vertical-saas-positioning-public-sector.md` | Ministries, revenue authorities, public-service digital portals, procurement constraints. |
| `vertical-saas-positioning-healthcare.md` | Hospital chains, NHIS-style schemes, HMIS integration, patient-data residency. |
| `vertical-saas-positioning-education.md` | Universities, school groups, EdTech, LMS integration, student-data protection. |
| `saas-objection-handling-playbook.md` | Price, risk, timeline, technology, vendor lock, exit, data sovereignty, AI features, support. |
| `saas-vendor-vs-build-narrative.md` | Build-vs-buy framing for defending vendor-managed SaaS over on-prem or in-house. |
| `saas-win-themes-and-discriminators.md` | Discriminator language for SaaS bids: vertical depth, integration realism, success engineering, transparent commercial model. |
| `saas-gtm-motion-design-reference.md` | PLG / inside-sales / field / hybrid motion selection, channel-decay monitoring, pricing-experimentation register. |
| `saas-metrics-glossary-for-proposals.md` | ARR, MRR, ACV, TCV, RPO, NRR, churn variants, magic number, Rule of 40, PSAR — engine's own definitions for proposal use. |
| `saas-trust-and-compliance-section-template.md` | Section template for security, compliance, sub-processors, BCDR, audit posture. |
| `saas-multi-tenant-architecture-block.md` | Methodology credibility paragraphs and tables. |

## CRITICAL GAPS STILL OPEN (post-session)

- **Pricing localisation**: African market price points for SaaS implementation by vertical need empirical updates from agency win/loss data; the reference files give frameworks but not local benchmarks.
- **Regulator-specific compliance maps**: per-country regulator pages (BoU, NITA-U, Kenya ODPC, NDPR Nigeria, POPIA South Africa, etc.) are referenced in vertical files but should become their own reference set in a future session.
- **Worked competitive-displacement examples** for the named incumbents (Temenos, Guidewire, etc.) would strengthen the win-themes file — left to a future session because it requires win/loss material.
- **Win-loss debrief templates** are not in this audit — could be added as a follow-up.
- **AI-feature-on-SaaS layering**: the engine has `ai-transformation-proposal` and the new `saas-implementation-methodology` — the explicit AI-on-SaaS combined methodology (RAG + multi-tenancy, model gateway + tenant isolation) is a follow-up.

## RECOMMENDED FOLLOW-UP SESSIONS

1. **Win-loss debrief and proposal post-mortem skills.**
2. **AI-on-SaaS combined methodology** (RAG, model gateway, eval, all under multi-tenant isolation).
3. **Country-specific regulator and compliance reference pack** for the African regulators most relevant to the agency's pipeline.
4. **Vertical-SaaS positioning expansion** to agribusiness, NGO operations, SMB ERP — verticals named but not yet authored.
5. **Worked competitive displacement examples** once win-loss data is available.
6. **Procurement framework alignment** (World Bank, AfDB, UNDP) overlaid onto SaaS pricing structures.

## How This Audit Drove the Repository Changes in This Session

All "NEW SKILLS" and "ENHANCEMENTS" rows above are implemented in this session. All reference files in the "REFERENCE FILES / TEMPLATES TO ADD" section are created. The audit serves as the long-form index to the changes.
