# AI-on-SaaS Proposal Skills Audit 2026

Internal audit produced for the proposal-skills engine to close the AI-on-SaaS gap flagged at the end of the 2026 SaaS hardening session: *"AI-on-SaaS combined methodology — RAG + model gateway under multi-tenant isolation has hooks in `ai-transformation-proposal` but warrants its own combined methodology skill."* This audit defines and operationalises the AI-on-SaaS proposal arsenal — the skills, enhancements, and references the engine needs to win and shape engagements where the buyer wants AI features (RAG, copilots, agents, AI analytics, AI-assisted workflows) built into a multi-tenant SaaS product.

## Scope of This Audit

The audit covers engagements with all five of these characteristics:

1. The deliverable is a **multi-tenant SaaS product** (control plane + application plane + tenant isolation).
2. The deliverable contains **AI features** built into the product (RAG-powered search, in-app copilots, agents, AI analytics, AI-assisted decisioning, AI-generated artefacts).
3. The buyer is **regulated, enterprise, or premium-priced** and is exposed to AI-specific compliance regimes (EU AI Act, sectoral rules, local AI guidelines such as Kenya's NCAIS, Nigeria's NAIS, South Africa's draft AI policy, Uganda's NITA-U guidance, Rwanda's National AI Policy).
4. The engagement carries **AI-distinctive risk**: model risk, hallucination liability, prompt injection, data leakage into model providers, sub-processor exposure, regulator shift, vendor lock-in to a single model family.
5. The buyer expects **investor-grade or board-grade rigour**: AI ROI that survives a sceptical CFO, eval evidence that survives a sceptical CTO, and procurement answers that survive a sceptical CISO.

## What the Engine Has Today

| Existing asset | What it covers | Gap |
|---|---|---|
| `skills/strategy-positioning/ai-transformation-proposal/SKILL.md` | AI strategy, AI use-case prioritisation, governance, eval, RAG/agent design, maintenance | Not a combined AI-on-SaaS methodology; carries only a single closing block on tenant isolation, cost attribution, lifecycle communications |
| `skills/saas-proposals/saas-implementation-methodology/SKILL.md` | Control plane / application plane / tenant isolation / cost attribution methodology | Silent on AI workstreams (eval harness, model gateway, RAG indexes per tenant, red-team, hallucination SLOs) |
| `skills/saas-proposals/saas-poc-and-pilot-scoping/SKILL.md` | POC time-box, binary success criteria, exit gates | Silent on AI-specific POC criteria (eval metric thresholds, golden dataset, hallucination ceiling, model selection criteria) |
| `skills/saas-proposals/saas-business-case-and-roi-modeling/SKILL.md` | TCO, payback, NPV, Rule of 40 | Silent on cost-of-tokens, eval-margin, AI uplift caveats, AI downside scenarios |
| `skills/saas-proposals/saas-pricing-and-packaging-proposal/SKILL.md` | Subscription / usage / hybrid / tiering | Silent on AI-credit packaging, model-by-tier, fair-use, AI-tier upsell pattern |
| `skills/saas-proposals/saas-procurement-and-security-questionnaire/SKILL.md` | DPA / MSA / SLA / sub-processor / residency / exit | Silent on AI-specific questionnaire (model providers, training-data opt-out, retention, region routing, sovereign-AI) |
| `skills/saas-proposals/saas-trust-and-compliance-credentials-section/SKILL.md` | Security, privacy, BCDR, audit, sub-processors | Silent on AI Act readiness, model-card practice, hallucination SLO, red-team practice, AI sub-processor disclosure |
| `skills/saas-proposals/saas-objection-handling-and-competitive-displacement/SKILL.md` | Price, vendor lock-in, build-vs-buy, do-nothing | Silent on AI-specific objections (accuracy, ethics, jobs, regulator, ban risk) |
| `skills/domain-delivery/risk-management/SKILL.md` | Generic risk registers | No AI risk register (model risk, hallucination liability, prompt injection, regulatory shift, reputational) |
| `skills/domain-delivery/monitoring-and-evaluation/SKILL.md` | M&E / log frames | No AI dashboards (eval drift, hallucination rate, cost per tenant, abstain rate, citation accuracy) |
| `skills/domain-delivery/change-management/SKILL.md` | OCM frameworks | No AI mindset transition (model trust, augment-vs-replace, human-in-the-loop, retraining cadence) |
| `skills/pipeline/07-team-composition/SKILL.md` | Team rosters | No AI-specific roster (ML lead, prompt engineer, AI safety lead, eval engineer, MLOps, data engineer) |

The closing block of `ai-transformation-proposal` ("SaaS-on-AI and AI-on-SaaS Lens") is hooks-only. It points at the right concerns but does not give the proposal writer methodology, deliverables, gates, acceptance criteria, risk register entries, pricing patterns, compliance subsections, or procurement answers.

## What the Engine Lacks (Synthesised)

The engine cannot today produce, end-to-end, a Bain/EY/McKinsey-grade proposal for an AI-on-SaaS engagement because eight artefact families are missing:

1. **Combined AI-on-SaaS methodology** — phases, gates, deliverables, acceptance criteria that simultaneously cover the SaaS layer and the AI layer.
2. **AI-on-SaaS discovery and qualification** — discovery questions that surface workflow-AI fit, data readiness for AI, hallucination tolerance, AI maturity, change-readiness for AI, regulatory exposure.
3. **AI ROI rigour that resists hype** — cost-of-tokens model, eval-margin model, AI uplift with caveats, downside scenarios including regulator and hallucination liability, payback that accounts for cost of running the model.
4. **AI commercial models inside SaaS pricing** — usage-based credits, included-allowance + overage, AI-tier-as-upsell, model-selection-by-tier, fair-use language.
5. **AI POC scoping** — binary eval metric thresholds, golden dataset definition, hallucination ceiling, model selection criteria, exit-to-production gates.
6. **AI risk register and Responsible-AI commitment** — model risk, vendor lock-in, hallucination liability, data leakage, prompt injection, regulatory shift, reputational, with mitigations and a Responsible-AI section evaluators can score.
7. **AI compliance credentials and procurement pack** — AI Act readiness, model-card practice, eval-harness CI, hallucination SLO, sub-processor disclosure for model providers, training-data opt-out, retention, region routing, sovereign-AI options.
8. **AI-specific change management, team composition, and vertical positioning** — model trust, escalation paths, human-in-the-loop design, retraining cadence; ML lead / prompt engineer / AI safety lead / eval engineer rosters; vertical AI plays for financial services, insurance, public sector, healthcare, education, customer support.

## NEW SKILLS

Create the following under `skills/<skill-name>/` with `SKILL.md` and `references/` where useful.

| Skill | Purpose |
|---|---|
| `skills/ai-on-saas-proposals/ai-on-saas-combined-methodology/` | Headline skill: methodology for a project that simultaneously delivers a multi-tenant SaaS AND its AI features, with phases, gates, deliverables, and acceptance criteria for both layers. |
| `skills/ai-on-saas-proposals/ai-on-saas-discovery-and-qualification/` | Discovery questions specific to AI features: workflow-AI fit, data readiness for AI, hallucination tolerance, AI maturity, change-readiness for AI, regulatory exposure (AI Act tier, sectoral rules, local AI guidelines). |
| `skills/ai-on-saas-proposals/ai-on-saas-business-case-and-roi/` | AI ROI that resists hype: cost-of-poor-quality reduction, agent productivity uplift (with caveats), revenue from AI-tier upsell, payback accounting for token costs, downside scenarios (regulator, hallucination liability). |
| `skills/ai-on-saas-proposals/ai-on-saas-pricing-and-packaging-proposal/` | AI-tier pricing: usage-based credits, hybrid, AI-tier-as-upsell, included-allowance + overage, fair-use, model-selection-by-tier. |
| `skills/ai-on-saas-proposals/ai-on-saas-poc-and-pilot-scoping/` | AI POC: binary success criteria (eval metric thresholds), golden dataset definition, model selection criteria, hallucination ceiling, exit-to-production gates. |
| `skills/ai-on-saas-proposals/ai-on-saas-risk-and-responsible-ai/` | Risk register for AI engagements (model risk, vendor lock, hallucination liability, data leakage, prompt injection, regulatory shift, reputational), with mitigations and Responsible-AI commitment section. |
| `skills/ai-on-saas-proposals/ai-on-saas-compliance-credentials/` | Proposal section showcasing: AI Act readiness, model-card practice, eval-harness CI, hallucination SLO, sub-processor disclosure, red-team practice, vendor governance — Trust & Compliance for AI block. |
| `skills/ai-on-saas-proposals/ai-on-saas-procurement-and-questionnaire/` | Handling client AI questionnaires (model providers, sub-processor list, training-data exclusion, customer-data-in-training opt-out, retention, deletion, region routing, sovereign-AI options). |
| `skills/ai-on-saas-proposals/ai-on-saas-change-management-and-adoption/` | AI-specific change management: model trust, AI-replaces-vs-AI-augments framing, escalation paths, human-in-the-loop design, retraining cadence. |
| `skills/ai-on-saas-proposals/ai-on-saas-team-composition/` | Roster: ML lead, prompt engineer, AI safety lead, data engineer for ingestion, eval engineer, MLOps engineer, plus the SaaS team (control plane, application plane); blended-rate and ramp considerations. |
| `skills/ai-on-saas-proposals/ai-on-saas-vertical-positioning/` | Vertical AI-on-SaaS plays: financial services (regulator-aware), insurance, public sector (procurement-aware), healthcare (HIPAA-aware), education, customer support — each with discriminators, named use cases, and risk-framing language. |

## ENHANCEMENTS TO EXISTING SKILLS

| Skill | What to Add |
|---|---|
| `skills/strategy-positioning/ai-transformation-proposal/SKILL.md` | Cross-link to all new `ai-on-saas-*` skills; add "when AI is delivered as a SaaS feature" branch in the workflow. |
| `skills/saas-proposals/saas-implementation-methodology/SKILL.md` | Add AI overlay reference: where the AI workstreams (eval harness, model gateway, RAG indexes per tenant, red-team, hallucination SLO) slot into the standard phases. |
| `skills/saas-proposals/saas-business-case-and-roi-modeling/SKILL.md` | AI value-and-cost-of-tokens addendum; cross-link to `ai-on-saas-business-case-and-roi`. |
| `skills/saas-proposals/saas-pricing-and-packaging-proposal/SKILL.md` | AI-pricing patterns (credits, included-allowance + overage, model-by-tier, fair-use). |
| `skills/saas-proposals/saas-procurement-and-security-questionnaire/SKILL.md` | AI questionnaire pack reference; sub-processor list now includes model providers. |
| `skills/saas-proposals/saas-trust-and-compliance-credentials-section/SKILL.md` | AI compliance subsection (AI Act readiness, model cards, eval-harness CI, hallucination SLO, red-team). |
| `skills/saas-proposals/saas-objection-handling-and-competitive-displacement/SKILL.md` | AI objection playbook (price/accuracy/lock-in/regulator/ethics/jobs/ban). |
| `skills/domain-delivery/risk-management/SKILL.md` | AI risk register entries. |
| `skills/pipeline/06-methodology/SKILL.md` | Point to `ai-on-saas-combined-methodology` when AI features are part of the SaaS build. |
| `skills/pipeline/07-team-composition/SKILL.md` | Point to `ai-on-saas-team-composition` for AI-on-SaaS rosters. |
| `skills/pipeline/10-financial-proposal/SKILL.md` | AI commercial structure block (cost of tokens, AI-tier credits, fair-use). |
| `skills/12-risk-analysis` *(if present; otherwise `risk-management`)* | AI risk register. |
| `skills/domain-delivery/monitoring-and-evaluation/SKILL.md` | AI dashboards (eval drift, hallucination rate, cost per tenant, abstain rate, citation accuracy, retraining cadence). |
| `skills/domain-delivery/change-management/SKILL.md` | AI mindset transition: trust, augment-vs-replace, HITL, retraining cadence. |
| `skills/SKILL.md` (parent) and `AGENTS.md` and `CLAUDE.md` and `README.md` | Add the new `ai-on-saas-*` skill family to routing tables. |

## REFERENCE FILES / TEMPLATES TO ADD

Place in `skills/profiles-sectors/references/` (cross-cutting) unless noted otherwise.

| Reference | Purpose |
|---|---|
| `ai-on-saas-discovery-question-bank.md` | AI-on-SaaS discovery questions across workflow fit, data, hallucination tolerance, maturity, change-readiness, regulator. |
| `ai-on-saas-business-case-template.md` | Cost-of-tokens, eval-margin, AI uplift, payback, downside scenarios. |
| `ai-on-saas-pricing-models-reference.md` | Usage credits, hybrid, AI tier, included-allowance + overage, fair-use, model-by-tier. |
| `ai-on-saas-poc-scoping-template.md` | POC with binary eval criteria, golden dataset, model selection, hallucination ceiling. |
| `ai-on-saas-risk-register-for-proposals.md` | AI-specific risk register. |
| `ai-on-saas-responsible-ai-commitment.md` | Section template for the Responsible-AI commitment. |
| `ai-on-saas-trust-and-compliance-section-template.md` | Trust & Compliance for AI section template. |
| `ai-on-saas-procurement-questionnaire-pack.md` | AI questionnaire pack: model providers, training-opt-out, region, retention, deletion. |
| `ai-on-saas-methodology-blocks.md` | Reusable Methodology blocks for AI-on-SaaS engagements. |
| `ai-on-saas-team-composition-template.md` | Roster, RACI, blended-rate considerations. |
| `ai-on-saas-change-management-playbook.md` | AI mindset, HITL, augment-vs-replace, retraining cadence. |
| `ai-on-saas-objection-handling-playbook.md` | Price, accuracy, lock-in, regulator, ethics, jobs, ban. |
| `vertical-ai-on-saas-financial-services.md` | Banking, payments, microfinance — AI plays, regulator stance. |
| `vertical-ai-on-saas-insurance.md` | Life, non-life, health — claims AI, underwriting AI. |
| `vertical-ai-on-saas-public-sector.md` | Ministries, agencies, regulators, public-service portals — AI sovereignty, procurement. |
| `vertical-ai-on-saas-healthcare.md` | Hospitals, NHIS, clinical decision-support — HIPAA, data residency. |
| `vertical-ai-on-saas-education.md` | Universities, schools, EdTech — student data, learning analytics. |
| `vertical-ai-on-saas-customer-support.md` | Support copilots, AI deflection, ticket triage. |
| `ai-on-saas-win-themes-and-discriminators.md` | Win themes for AI-on-SaaS bids. |
| `ai-on-saas-metrics-glossary.md` | Eval accuracy, F1, latency, p95, hallucination rate, abstain rate, citation accuracy, cost per call, cost per tenant, retraining cadence. |

## CRITICAL GAPS STILL OPEN (post-session)

- **Country-specific AI regulator pages**: Kenya NCAIS, Nigeria NAIS, South Africa AI policy, Uganda NITA-U AI guidance, Rwanda AI Policy, EAC AI position — referenced in verticals but not authored as standalone pages.
- **Worked AI-on-SaaS competitive displacement** examples (replacing a non-AI incumbent, replacing an AI point solution, replacing an in-house RAG, replacing a model-provider-direct deal) — requires win/loss data.
- **AI eval harness templates** at code-level (LLM-as-judge, golden-set, regression harness scripts) — these belong in the software-dev engine, not the proposal engine; flagged as a handoff.
- **Sovereign-AI pricing benchmarks** for African deployments (on-prem inference, GPU rentals, fine-tuning) — empirical data not yet gathered.
- **AI Act conformity assessment** worked example for a high-risk AI system inside an African SaaS exporting to EU customers — flagged as a future session.

## RECOMMENDED FOLLOW-UP SESSIONS

1. **Country-specific AI regulator pack** for the African regulators most relevant to the agency's pipeline (Kenya ODPC + NCAIS, Nigeria NITDA + NAIS, South Africa POPIA + AI policy, Uganda NITA-U + PDPO, Rwanda NCSA + AI Policy).
2. **Worked AI-on-SaaS competitive displacement** examples once win/loss material is available.
3. **AI eval harness code templates** in the software-dev / SRS engine (LLM-as-judge, golden-set, regression).
4. **Sovereign-AI commercial benchmarks** for African deployments.
5. **AI Act conformity assessment** worked example for export bids.
6. **Win-loss debrief skill** (carried over from the SaaS audit, still open).

## How This Audit Drove the Repository Changes in This Session

All "NEW SKILLS" and "ENHANCEMENTS" rows above are implemented in this session. All reference files in the "REFERENCE FILES / TEMPLATES TO ADD" section are created. The audit serves as the long-form index to the changes. The AI-on-SaaS arsenal complements rather than replaces the existing `ai-transformation-proposal` (which still owns generic AI strategy work where there is no SaaS layer) and the existing `saas-*` family (which still owns SaaS work where there are no AI features).
