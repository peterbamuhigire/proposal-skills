# Proposal Skills

Proposal Skills is the Chwezi engine for winning consulting and technology work in East and Central Africa. Its 115 skills plan, draft, review and assemble consulting proposals, Expressions of Interest, tender and request-for-proposal responses, donor grant applications and commercial offers, from the cover letter and executive summary through methodology, team, work plan and financial proposal. The engine reads the actual solicitation, the buyer's evaluation criteria and the proposer's evidence; it does not infer tender requirements from earlier bids or invent credentials, compliance or delivery capacity. Procurement routes follow the frameworks the engine cites directly: Uganda's PPDA Act (Cap. 205) and PPDA Regulations 2023, the World Bank Procurement Regulations for IPF Borrowers and Environmental and Social Framework, the AfDB Procurement Policy and Integrated Safeguards System 2023, UNDP and UN-system rules, EU PRAG and GIZ local procurement, and OECD-DAC evaluation criteria for results and M&E. Technology bids are checked against the assurance standards buyers ask about, including ISO/IEC 27001, ISO/IEC 42001, SOC 2, the NIST AI RMF, the EU AI Act, GDPR and East African data-protection law.

The engine produces submission-ready proposal sections and full bid packages, EOI and prequalification responses, compliance matrices and evidence maps, logframes and results frameworks, risk registers, staffing plans and Gantt-style work plans, fee schedules and pricing narratives, SaaS, AI-on-SaaS and AI-agent business cases, pilots, SLAs and contract exhibits, oral-presentation packs, and independent red-team and anti-slop review findings. All writing follows its professional British English and East African English standards and every claim must trace to evidence. It serves consulting firms, independent consultants, software and AI vendors, agencies, NGOs and bid teams responding to government, donor, development-bank and enterprise buyers. Current facts, finance, visual design and software delivery hand off to the relevant sister engines rather than being improvised.

## Installation

**Prerequisites.** Claude Code for the plugin route. The clone installer needs Node.js 18 or newer. The validators and tests need Python 3.11 or newer and PyYAML (`python3 -m pip install PyYAML`); there is no requirements file, and `pytest` is optional because the suite runs under `unittest`. The installer and every check were last run together on 31 October 2026 with Python 3.14, PyYAML 6.0 and Node.js 22 on Linux; the Windows route (`install.ps1`) was not run there.

**Claude Code plugin (recommended).** The repository ships a marketplace (`chwezi-proposal`) and a plugin (`proposal`) in `.claude-plugin/`:

```text
/plugin marketplace add https://github.com/peterbamuhigire/proposal-skills
/plugin install proposal@chwezi-proposal
```

**Clone and install.** `install.sh` and `install.ps1` delegate to `scripts/install-engine.js`, which copies the skills, rules and hooks into `~/.claude` (`--scope user`, the default) or into `.claude` under the current directory (`--scope project`) and records ownership in `.chwezi/install-state.json`. Add `--dry-run` to preview the plan. Run `install.sh` through `bash`: git stores it without the executable bit, so `./install.sh` stops with `Permission denied` on a fresh clone. Project scope writes to the directory you run it from, so run it inside the project that should receive the skills, not inside this checkout.

```text
git clone https://github.com/peterbamuhigire/proposal-skills
cd proposal-skills
bash install.sh --scope project --dry-run    # Linux, macOS, Git Bash: preview
bash install.sh --scope project              # install
node scripts/install-engine.js doctor --scope project
node scripts/install-engine.js uninstall --engine proposal-skills --scope project
.\install.ps1 --scope project                # Windows PowerShell instead of install.sh
```

The Linux sequence above (preview, install, `doctor`, uninstall) was run on 31 October 2026 into a throwaway project directory: `doctor` reported every installed file present and unmodified, and the install held all 115 `SKILL.md` files.

**Codex.** Codex reads `AGENTS.md` as the repository policy. Before substantive Codex work, run the model-policy check in `.codex/` (Python 3.11+), and apply it only when drift is reported:

```text
python3 <engine-root>/.codex/ensure_model_policy.py --runtime codex --check
python3 <engine-root>/.codex/ensure_model_policy.py --runtime codex --apply
```

`--check` prints `PASS: Codex model policy is correct` and exits 0 when the settings match, prints a `DRIFT:` line and exits 1 when they do not (an empty Codex home gives `DRIFT: Codex config.toml is missing`), and exits 2 on an error. `--apply` uses `CODEX_HOME` (default `~/.codex`), preserves unrelated settings and backs up what it touches (see [`.codex/README.md`](.codex/README.md)); it was not run for this update. With `--runtime claude` the helper reports `NOT_APPLICABLE` and changes nothing.

**Manual route (any runner).** Clone the repository, read [`AGENTS.md`](AGENTS.md) and the [proposal router](skills/SKILL.md), then load the routed `skills/<category>/<skill-name>/SKILL.md` directly with `rules/common/core.md`. Claude Code picks up `CLAUDE.md`, which imports `AGENTS.md`.

## Capabilities

115 active `SKILL.md` files across 11 categories plus the parent router, generated from the `skills/` tree.

| Category | Count |
|---|---:|
| Proposal pipeline | 10 |
| Profiles and sectors | 18 |
| Domain delivery | 16 |
| Strategy and positioning | 12 |
| SaaS proposals | 14 |
| AI-on-SaaS proposals | 11 |
| AI-agent proposals | 11 |
| AI-agent commercial terms | 8 |
| Writing and content | 3 |
| Language | 2 |
| Quality and operations | 9 |
| Router | 1 |
| **Total** | **115** |

| Category | Skill | What it does |
|---|---|---|
| Router | [`skills`](skills/SKILL.md) | Routes, sequences and assembles a complete proposal, EOI, bid or tender response. |
| Proposal pipeline | [`01-cover-letter`](skills/pipeline/01-cover-letter/SKILL.md) | Signed transmittal letter confirming assignment, authority, validity and intent. |
| Proposal pipeline | [`02-executive-summary`](skills/pipeline/02-executive-summary/SKILL.md) | Evaluator-facing summary of problem, response, differentiators, scope and value. |
| Proposal pipeline | [`03-understanding-of-assignment`](skills/pipeline/03-understanding-of-assignment/SKILL.md) | Interprets context, objectives, scope, constraints and ToR gaps. |
| Proposal pipeline | [`04-firm-profile`](skills/pipeline/04-firm-profile/SKILL.md) | Proposer or individual consultant profile, presence and credentials. |
| Proposal pipeline | [`05-relevant-experience`](skills/pipeline/05-relevant-experience/SKILL.md) | Project sheets, references, similarity evidence and experience matrix. |
| Proposal pipeline | [`06-methodology`](skills/pipeline/06-methodology/SKILL.md) | Technical approach, phases, methods, QA and deliverables. |
| Proposal pipeline | [`07-team-composition`](skills/pipeline/07-team-composition/SKILL.md) | Staffing, organogram, expert fit, CV framing and availability. |
| Proposal pipeline | [`08-work-plan`](skills/pipeline/08-work-plan/SKILL.md) | Activities, dependencies, milestones, Gantt tables and staffing schedule. |
| Proposal pipeline | [`09-expression-of-interest`](skills/pipeline/09-expression-of-interest/SKILL.md) | EOI, REOI and prequalification submissions on eligibility and capability. |
| Proposal pipeline | [`10-financial-proposal`](skills/pipeline/10-financial-proposal/SKILL.md) | Budget, fee schedule, reimbursables, payment schedule and price forms. |
| Profiles and sectors | [`profiles`](skills/profiles-sectors/profiles/SKILL.md) | Fixes one proposer identity, voice, signatory and credential set. |
| Profiles and sectors | [`sectors`](skills/profiles-sectors/sectors/SKILL.md) | Routes a bid to the right procurement-framework and sector skills. |
| Profiles and sectors | [`afdb`](skills/profiles-sectors/sectors/afdb/SKILL.md) | African Development Bank procurement, consultant selection and safeguards. |
| Profiles and sectors | [`world-bank`](skills/profiles-sectors/sectors/world-bank/SKILL.md) | World Bank consulting procurement, TECH/FIN forms and QCBS. |
| Profiles and sectors | [`undp`](skills/profiles-sectors/sectors/undp/SKILL.md) | UNDP and UN-system procurement, grants and evaluation rules. |
| Profiles and sectors | [`ppda-uganda`](skills/profiles-sectors/sectors/ppda-uganda/SKILL.md) | Uganda PPDA public procurement for consultancy, supplies, works and services. |
| Profiles and sectors | [`agriculture`](skills/profiles-sectors/sectors/agriculture/SKILL.md) | Agriculture, agribusiness, value chains and food systems bids. |
| Profiles and sectors | [`civil-society-cyber-resilience`](skills/profiles-sectors/sectors/civil-society-cyber-resilience/SKILL.md) | NGO and civil-society cybersecurity and digital resilience bids. |
| Profiles and sectors | [`education`](skills/profiles-sectors/sectors/education/SKILL.md) | Education systems, TVET, curriculum and skills programmes. |
| Profiles and sectors | [`energy`](skills/profiles-sectors/sectors/energy/SKILL.md) | Power, electrification, renewables, clean cooking and utilities. |
| Profiles and sectors | [`financial-services`](skills/profiles-sectors/sectors/financial-services/SKILL.md) | Banking, insurance, payments, mobile money and financial inclusion. |
| Profiles and sectors | [`governance`](skills/profiles-sectors/sectors/governance/SKILL.md) | Institutional reform, decentralisation, PFM and public services. |
| Profiles and sectors | [`health`](skills/profiles-sectors/sectors/health/SKILL.md) | Health systems, programmes, facilities and health informatics. |
| Profiles and sectors | [`hospitality-hotel-restaurant`](skills/profiles-sectors/sectors/hospitality-hotel-restaurant/SKILL.md) | Hotel, lodge, restaurant, catering and event-venue proposals. |
| Profiles and sectors | [`ict`](skills/profiles-sectors/sectors/ict/SKILL.md) | Software, MIS, ERP, digital transformation and e-government. |
| Profiles and sectors | [`manufacturing-industrial`](skills/profiles-sectors/sectors/manufacturing-industrial/SKILL.md) | Manufacturing, production planning, warehousing, ERP and MES. |
| Profiles and sectors | [`transport-infrastructure`](skills/profiles-sectors/sectors/transport-infrastructure/SKILL.md) | Roads, mobility, logistics, asset management and PPP advisory. |
| Profiles and sectors | [`water-sanitation`](skills/profiles-sectors/sectors/water-sanitation/SKILL.md) | WASH programmes, sanitation services and water utilities. |
| Domain delivery | [`accounting-finance-advisory`](skills/domain-delivery/accounting-finance-advisory/SKILL.md) | Accounting, finance operations, controls, tax and audit-readiness proposals. |
| Domain delivery | [`business-analysis-tools`](skills/domain-delivery/business-analysis-tools/SKILL.md) | Diagnostic, requirements, options-appraisal and process tools. |
| Domain delivery | [`capacity-building`](skills/domain-delivery/capacity-building/SKILL.md) | Training, coaching, ToT and institutional capacity development. |
| Domain delivery | [`change-management`](skills/domain-delivery/change-management/SKILL.md) | Adoption, resistance, readiness, communications and transition. |
| Domain delivery | [`consulting-frameworks`](skills/domain-delivery/consulting-frameworks/SKILL.md) | Conceptual frameworks, problem decomposition and phase logic. |
| Domain delivery | [`data-management`](skills/domain-delivery/data-management/SKILL.md) | Data collection, quality, governance, MIS, protection and migration. |
| Domain delivery | [`eac-ecommerce-bds-programme-design`](skills/domain-delivery/eac-ecommerce-bds-programme-design/SKILL.md) | Donor-funded EAC e-commerce business-development-services programmes. |
| Domain delivery | [`environmental-and-social-safeguards`](skills/domain-delivery/environmental-and-social-safeguards/SKILL.md) | E&S screening, ESIA, ESMP, resettlement and donor safeguards. |
| Domain delivery | [`gender-and-social-inclusion`](skills/domain-delivery/gender-and-social-inclusion/SKILL.md) | Gender analysis, GESI mainstreaming and disability inclusion. |
| Domain delivery | [`giz-eu-local-procurement-response`](skills/domain-delivery/giz-eu-local-procurement-response/SKILL.md) | GIZ local procurement and EU/BMZ/GIZ tender packs. |
| Domain delivery | [`monitoring-and-evaluation`](skills/domain-delivery/monitoring-and-evaluation/SKILL.md) | Theory of change, logframe, indicators, baselines and evaluation. |
| Domain delivery | [`project-management`](skills/domain-delivery/project-management/SKILL.md) | Delivery governance, reporting, RACI, change control and escalation. |
| Domain delivery | [`retail-transformation-proposal`](skills/domain-delivery/retail-transformation-proposal/SKILL.md) | Retail, omnichannel, e-commerce, POS and merchandising proposals. |
| Domain delivery | [`risk-management`](skills/domain-delivery/risk-management/SKILL.md) | Risk identification, scoring, ownership, treatment and registers. |
| Domain delivery | [`stakeholder-engagement`](skills/domain-delivery/stakeholder-engagement/SKILL.md) | Stakeholder mapping, consultation, feedback and grievance handling. |
| Domain delivery | [`sustainability-planning`](skills/domain-delivery/sustainability-planning/SKILL.md) | Institutional, technical and financial sustainability, handover and exit. |
| Strategy and positioning | [`ai-transformation-proposal`](skills/strategy-positioning/ai-transformation-proposal/SKILL.md) | Shapes proposals for AI applications, analytics and automation. |
| Strategy and positioning | [`critical-analysis-business-logic`](skills/strategy-positioning/critical-analysis-business-logic/SKILL.md) | Tests evidence, logic, feasibility and commercial sense before release. |
| Strategy and positioning | [`customer-service-and-maintenance-proposals`](skills/strategy-positioning/customer-service-and-maintenance-proposals/SKILL.md) | Post-launch support, maintenance, SLA and managed-service proposals. |
| Strategy and positioning | [`embedded-accounting-engine-proposal`](skills/strategy-positioning/embedded-accounting-engine-proposal/SKILL.md) | Embedded bookkeeping inside SaaS, ERP, POS or sector systems. |
| Strategy and positioning | [`key-account-pursuit-and-account-plan`](skills/strategy-positioning/key-account-pursuit-and-account-plan/SKILL.md) | Strategic account selection, pursuit and one-page account plans. |
| Strategy and positioning | [`premium-client-proposal-strategy`](skills/strategy-positioning/premium-client-proposal-strategy/SKILL.md) | Positions bids for executives, enterprise and high-ticket buyers. |
| Strategy and positioning | [`premium-pricing-and-value-defense`](skills/strategy-positioning/premium-pricing-and-value-defense/SKILL.md) | Prices and defends premium consulting, software and service offers. |
| Strategy and positioning | [`proposal-storytelling-and-evaluator-journey`](skills/strategy-positioning/proposal-storytelling-and-evaluator-journey/SKILL.md) | Narrative spine, evaluator journey and case-study stories. |
| Strategy and positioning | [`sales-discovery-and-objection-handling`](skills/strategy-positioning/sales-discovery-and-objection-handling/SKILL.md) | Buyer needs, discovery questions, decision criteria and objections. |
| Strategy and positioning | [`service-design-proposal-strategy`](skills/strategy-positioning/service-design-proposal-strategy/SKILL.md) | Service design, CX, journey mapping and blueprint proposals. |
| Strategy and positioning | [`tender-orals-and-proposal-presentation`](skills/strategy-positioning/tender-orals-and-proposal-presentation/SKILL.md) | Tender orals, shortlist interviews and proposal walkthroughs. |
| Strategy and positioning | [`website-design-proposal-strategy`](skills/strategy-positioning/website-design-proposal-strategy/SKILL.md) | Website, e-commerce, portal and web front-end proposals. |
| SaaS proposals | [`saas-business-case-and-roi-modeling`](skills/saas-proposals/saas-business-case-and-roi-modeling/SKILL.md) | CFO-grade SaaS business case with TCO and time to value. |
| SaaS proposals | [`saas-customer-success-and-adoption-proposal`](skills/saas-proposals/saas-customer-success-and-adoption-proposal/SKILL.md) | Scopes and prices onboarding, activation and success cadence. |
| SaaS proposals | [`saas-discovery-and-qualification`](skills/saas-proposals/saas-discovery-and-qualification/SKILL.md) | ICP fit, critical event, pain chain and decision process. |
| SaaS proposals | [`saas-implementation-methodology`](skills/saas-proposals/saas-implementation-methodology/SKILL.md) | End-to-end SaaS implementation across control and application planes. |
| SaaS proposals | [`saas-lifecycle-communications-as-deliverable`](skills/saas-proposals/saas-lifecycle-communications-as-deliverable/SKILL.md) | Lifecycle communications scoped as a costed deliverable. |
| SaaS proposals | [`saas-multi-tenant-architecture-credibility-block`](skills/saas-proposals/saas-multi-tenant-architecture-credibility-block/SKILL.md) | Concise multi-tenant architecture credibility section. |
| SaaS proposals | [`saas-mutual-action-planning-and-close-plans`](skills/saas-proposals/saas-mutual-action-planning-and-close-plans/SKILL.md) | Buyer-and-supplier mutual action plan to signature and go-live. |
| SaaS proposals | [`saas-objection-handling-and-competitive-displacement`](skills/saas-proposals/saas-objection-handling-and-competitive-displacement/SKILL.md) | Price, risk, lock-in and sovereignty objections; displacement. |
| SaaS proposals | [`saas-pilot-to-rollout-change-management`](skills/saas-proposals/saas-pilot-to-rollout-change-management/SKILL.md) | Operating-model change from pilot to per-tenant operations. |
| SaaS proposals | [`saas-poc-and-pilot-scoping`](skills/saas-proposals/saas-poc-and-pilot-scoping/SKILL.md) | Time-boxed POC or pilot with success measures and exit gate. |
| SaaS proposals | [`saas-pricing-and-packaging-proposal`](skills/saas-proposals/saas-pricing-and-packaging-proposal/SKILL.md) | Chooses and defends subscription, usage or hybrid pricing. |
| SaaS proposals | [`saas-procurement-and-security-questionnaire`](skills/saas-proposals/saas-procurement-and-security-questionnaire/SKILL.md) | Procurement, legal, privacy, security, DPA, MSA and SLA answers. |
| SaaS proposals | [`saas-trust-and-compliance-credentials-section`](skills/saas-proposals/saas-trust-and-compliance-credentials-section/SKILL.md) | Evidence-qualified trust and compliance credentials section. |
| SaaS proposals | [`saas-vertical-positioning`](skills/saas-proposals/saas-vertical-positioning/SKILL.md) | Adapts a SaaS bid to a named vertical's buyers and regulators. |
| AI-on-SaaS proposals | [`ai-on-saas-business-case-and-roi`](skills/ai-on-saas-proposals/ai-on-saas-business-case-and-roi/SKILL.md) | ROI model including model usage, evaluation cost and risk. |
| AI-on-SaaS proposals | [`ai-on-saas-change-management-and-adoption`](skills/ai-on-saas-proposals/ai-on-saas-change-management-and-adoption/SKILL.md) | Adoption plan for trust, oversight, escalation and retraining. |
| AI-on-SaaS proposals | [`ai-on-saas-combined-methodology`](skills/ai-on-saas-proposals/ai-on-saas-combined-methodology/SKILL.md) | Integrates multi-tenant SaaS delivery with RAG, copilots and agents. |
| AI-on-SaaS proposals | [`ai-on-saas-compliance-credentials`](skills/ai-on-saas-proposals/ai-on-saas-compliance-credentials/SKILL.md) | AI-specific trust and compliance controls inside SaaS. |
| AI-on-SaaS proposals | [`ai-on-saas-discovery-and-qualification`](skills/ai-on-saas-proposals/ai-on-saas-discovery-and-qualification/SKILL.md) | Qualifies AI features by workflow fit and data readiness. |
| AI-on-SaaS proposals | [`ai-on-saas-poc-and-pilot-scoping`](skills/ai-on-saas-proposals/ai-on-saas-poc-and-pilot-scoping/SKILL.md) | AI feature POC with golden dataset and evaluation thresholds. |
| AI-on-SaaS proposals | [`ai-on-saas-pricing-and-packaging-proposal`](skills/ai-on-saas-proposals/ai-on-saas-pricing-and-packaging-proposal/SKILL.md) | Credits, allowances, overages and model-tier pricing. |
| AI-on-SaaS proposals | [`ai-on-saas-procurement-and-questionnaire`](skills/ai-on-saas-proposals/ai-on-saas-procurement-and-questionnaire/SKILL.md) | Model-provider, data-transfer and AI procurement questions. |
| AI-on-SaaS proposals | [`ai-on-saas-risk-and-responsible-ai`](skills/ai-on-saas-proposals/ai-on-saas-risk-and-responsible-ai/SKILL.md) | Owned AI risk register and auditable responsible-AI commitment. |
| AI-on-SaaS proposals | [`ai-on-saas-team-composition`](skills/ai-on-saas-proposals/ai-on-saas-team-composition/SKILL.md) | Justifies the combined AI, data, safety, platform and SRE team. |
| AI-on-SaaS proposals | [`ai-on-saas-vertical-positioning`](skills/ai-on-saas-proposals/ai-on-saas-vertical-positioning/SKILL.md) | Vertical use cases, regulator stance and evidence expectations. |
| AI-agent proposals | [`ai-agent-business-case-and-roi`](skills/ai-agent-proposals/ai-agent-business-case-and-roi/SKILL.md) | Task-based agent business case with intervention-adjusted benefits. |
| AI-agent proposals | [`ai-agent-change-management-and-adoption`](skills/ai-agent-proposals/ai-agent-change-management-and-adoption/SKILL.md) | Workforce adoption, trust staging and affected-party disclosure. |
| AI-agent proposals | [`ai-agent-compliance-credentials`](skills/ai-agent-proposals/ai-agent-compliance-credentials/SKILL.md) | Verified agent credentials: action logs and irreversibility gates. |
| AI-agent proposals | [`ai-agent-discovery-and-qualification`](skills/ai-agent-proposals/ai-agent-discovery-and-qualification/SKILL.md) | Tests agent-versus-workflow fit, autonomy and reversibility. |
| AI-agent proposals | [`ai-agent-methodology`](skills/ai-agent-proposals/ai-agent-methodology/SKILL.md) | End-to-end delivery method for single and multi-agent systems. |
| AI-agent proposals | [`ai-agent-poc-and-pilot-scoping`](skills/ai-agent-proposals/ai-agent-poc-and-pilot-scoping/SKILL.md) | Shadow, supervised and agentic pilot stages with gates. |
| AI-agent proposals | [`ai-agent-pricing-and-packaging-proposal`](skills/ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md) | Per-resolution, per-outcome, per-agent or hybrid pricing. |
| AI-agent proposals | [`ai-agent-procurement-and-questionnaire`](skills/ai-agent-proposals/ai-agent-procurement-and-questionnaire/SKILL.md) | Answers agent procurement questionnaires on autonomy and scope. |
| AI-agent proposals | [`ai-agent-risk-and-responsible-ai`](skills/ai-agent-proposals/ai-agent-risk-and-responsible-ai/SKILL.md) | Agent risk register and responsible-AI commitment. |
| AI-agent proposals | [`ai-agent-team-composition`](skills/ai-agent-proposals/ai-agent-team-composition/SKILL.md) | Agent delivery team, RACI, mobilisation and safety coverage. |
| AI-agent proposals | [`ai-agent-vertical-positioning`](skills/ai-agent-proposals/ai-agent-vertical-positioning/SKILL.md) | Adapts agent bids to support, finance, public sector and more. |
| AI-agent commercial terms | [`ai-agent-commercial-packaging`](skills/ai-agent-commercial/ai-agent-commercial-packaging/SKILL.md) | Included, add-on or standalone agent packaging. |
| AI-agent commercial terms | [`ai-agent-contract-language-pack`](skills/ai-agent-commercial/ai-agent-contract-language-pack/SKILL.md) | Agent-specific contract exhibits for proposal, MSA or SOW. |
| AI-agent commercial terms | [`ai-agent-intervention-credit-and-abort-refund`](skills/ai-agent-commercial/ai-agent-intervention-credit-and-abort-refund/SKILL.md) | Intervention credits, abort rights and refund mechanics. |
| AI-agent commercial terms | [`ai-agent-msa-and-sla-addendum-templates`](skills/ai-agent-commercial/ai-agent-msa-and-sla-addendum-templates/SKILL.md) | Agent MSA and SLA addendums: accountability, logs, kill switch. |
| AI-agent commercial terms | [`ai-agent-procurement-objections-on-commercials`](skills/ai-agent-commercial/ai-agent-procurement-objections-on-commercials/SKILL.md) | Answers challenges on agent pricing, liability and audit rights. |
| AI-agent commercial terms | [`ai-agent-renewal-and-true-up`](skills/ai-agent-commercial/ai-agent-renewal-and-true-up/SKILL.md) | Renewal, volume true-up, ramp-down protection and indexation. |
| AI-agent commercial terms | [`ai-agent-sla-and-credit-schedule`](skills/ai-agent-commercial/ai-agent-sla-and-credit-schedule/SKILL.md) | Agent SLA and service-credit schedule. |
| AI-agent commercial terms | [`ai-agent-success-fee-and-outcome-pricing`](skills/ai-agent-commercial/ai-agent-success-fee-and-outcome-pricing/SKILL.md) | Gain-share, success-fee and performance-corridor pricing. |
| Writing and content | [`premium-commercial-writing`](skills/writing-content/premium-commercial-writing/SKILL.md) | Proof-led revision of proposals, summaries and case studies. |
| Writing and content | [`blog-idea-generator`](skills/writing-content/blog-idea-generator/SKILL.md) | Generates and prioritises blog topics and editorial angles. |
| Writing and content | [`blog-writer`](skills/writing-content/blog-writer/SKILL.md) | Drafts and finalises publishable articles and case studies. |
| Language | [`east-african-english`](skills/language/east-african-english/SKILL.md) | English for Ugandan, Kenyan, Tanzanian and regional evaluators. |
| Language | [`language-standards`](skills/language/language-standards/SKILL.md) | French and Kiswahili sections, translation checks and terminology. |
| Quality and operations | [`anti-ai-slop`](skills/meta/anti-ai-slop/SKILL.md) | Live guardrail against generic, unverified drafting. |
| Quality and operations | [`ai-slop-audit`](skills/meta/ai-slop-audit/SKILL.md) | Grades a finished artefact for AI slop before submission. |
| Quality and operations | [`bid-red-team-dual-review`](skills/meta/bid-red-team-dual-review/SKILL.md) | Adversarial two-reviewer verification of high-stakes bids. |
| Quality and operations | [`submission-proof-and-receipt-discipline`](skills/meta/submission-proof-and-receipt-discipline/SKILL.md) | Fixes the submitted artefact and captures formal receipt proof. |
| Quality and operations | [`operational-readiness-and-localisation`](skills/meta/operational-readiness-and-localisation/SKILL.md) | Proves local banking, tax, licensing, payroll and FX readiness. |
| Quality and operations | [`kaizen-improvement-system`](skills/meta/kaizen-improvement-system/SKILL.md) | Audits and improves the engine and the proposals it produces. |
| Quality and operations | [`skill-safety-audit`](skills/meta/skill-safety-audit/SKILL.md) | Reviews skills for unsafe installers, credential capture or hidden execution. |
| Quality and operations | [`skill-writing`](skills/meta/skill-writing/SKILL.md) | Pointer to the canonical chwezi-dev-engine skill-authoring standard. |
| Quality and operations | [`update-claude-documentation`](skills/meta/update-claude-documentation/SKILL.md) | Keeps README, AGENTS, CLAUDE and CONTRIBUTING in step with changes. |

## Operating contract and cross-engine routes

- **Router and policy.** The [proposal router](skills/SKILL.md) sets workflow order and cross-cutting routes; [`AGENTS.md`](AGENTS.md) holds the model-neutral policy and [`rules/common/core.md`](rules/common/core.md) the always-on baseline.
- **Multi-phase work.** The [runtime-agnostic orchestration contract](docs/operations/runtime-agnostic-orchestration-2026-09-07.md) (`runtime-agnostic-orchestration-2026-09-07.md`) governs scoped work packages, evidence and pricing checkpoints, context hygiene, least agency and sanitised handling of external content for Claude Code and Codex alike.
- **Sister engines.** [Business Plan Skills](https://github.com/peterbamuhigire/business-plan-skills) supplies feasibility, projections and investor readiness; [Social Media Skills](https://github.com/peterbamuhigire/social-media-skills) supplies campaigns, content calendars and marketing reporting. Current facts route to the Digital Research Engine (catalogue id `digital-research-skills`), finance to [`chwezi-accounting-doctrine`](https://github.com/peterbamuhigire/chwezi-accounting-doctrine), visual formatting to [`chwezi-design-engine`](https://github.com/peterbamuhigire/chwezi-design-engine), software specification to [`chwezi-sdlc-documentation`](https://github.com/peterbamuhigire/chwezi-sdlc-documentation), engineering to [`chwezi-dev-engine`](https://github.com/peterbamuhigire/chwezi-dev-engine) and website delivery to [Website Skills](https://github.com/peterbamuhigire/website-skills). Website Skills keeps no copy of this engine; it resolves it through the catalogue like every other sibling. Four checkouts may still sit under their earlier folder names (`design-system-skills`, `srs-skills`, `skills-web-dev` and `chwezi-research-engine`); the portfolio catalogue in `chwezi-engine-agents` lists each as an alias. The full routing list is in [`AGENTS.md`](AGENTS.md).
- **Validation.** Seven registered checks and the on-demand helpers are listed, with their dependencies and expected results, under [Validation](#validation).

## Validation

Run every command from the repository root. The checks use `python3` (use `python` where only that name exists), need PyYAML, and leave tracked files unchanged (Python writes only ignored `__pycache__` folders).

| Command | What it checks | Expected result |
|---|---|---|
| `python3 -X utf8 scripts/validate_skills.py --baseline quality-baseline.json` | The skill contract for every `SKILL.md`, marketplace parity, the 5,000-file ceiling, the dated source register and retired World Bank form labels | Exit 0, `findings: 0` |
| `python3 -X utf8 scripts/routing_smoke_test.py` | The routing fixtures in `tests/fixtures/routing-fixtures.json` against skill descriptions | Exit 0, top-three hit rate 100%; precision@1 and owned negatives are reported and are a lexical proxy, not a model run |
| `python3 -X utf8 scripts/encoding_link_gate.py` | UTF-8, mojibake markers, broken local Markdown links, machine-specific paths outside dated records, portable sibling routes | Exit 0, `findings: 0` |
| `python3 -X utf8 scripts/source_ingestion_guardrail.py` | The ban on book extractions and reconstructive book content | Exit 0, `findings: 0` |
| `python3 scripts/proposal_fixture_check.py` | The structure of the fictional bid package in `tests/fixtures/` | `result: PASS` |
| `python3 -X utf8 -m unittest discover -s tests` | The test suite: 117 tests, also collected and passed by `pytest` | `OK` |
| `git diff --check` | Whitespace errors in the working tree | Exit 0, no output |

All seven were run on 31 October 2026 and exited 0. None of them needs `pwsh`, Pandoc, Mermaid, a browser, LibreOffice or a container. PyYAML is the only third-party Python package the checks import. `pytest` is optional: a real `pytest` run collected the same 117 tests and passed them.

Helpers and checks outside that list:

- `python3 scripts/proposal_fixture_check.py --input <package>/validator-input.json --check-content` scans a package's technical and financial envelope files, including `.docx`, for the other envelope's markers; the sanitised example in `examples/uganda-eoi-sanitised/` passes. Add `--allow-unscanned-types` to accept a file type the scan cannot read, such as PDF.
- `python3 -X utf8 scripts/page_budget_check.py <spec.json>` proposes or checks a weighted page allocation (`--propose` for a proportional split); `tests/fixtures/page-budget-example.json` is a worked input.
- `python3 -X utf8 scripts/check_form_labels.py`, `scripts/check_marketplace.py` and `scripts/check_source_currency.py` are the three gates that `validate_skills.py` calls; each also runs alone.
- `python3 -X utf8 scripts/validate_p0_commercial_fixture.py tests/fixtures/p0-commercial-fixture.json` and `python3 -X utf8 scripts/validate_healthcare_evidence_packs.py tests/fixtures/healthcare-evidence-packs.json` take a fixture path and print `PASS`; called without one they fail.
- `node hooks/test-destructive-bash-gate.js` (61 checks) and `node hooks/test-plugin-hook-config.js` (7 checks) test the plugin hooks. They need Node.js only and are not in CI.
- `python3 tests/agent-integration/test_proposal_agent_contract.py` checks the engine manifest against the portfolio catalogue and needs PyYAML. It is not part of `unittest` discovery or CI, and it looks for `chwezi-engine-agents` next to this checkout; where that folder is absent it prints `NOT ASSESSED` instead of failing.
- The canonical engine audit and quick validator in `chwezi-dev-engine` are listed in [`CONTRIBUTING.md`](CONTRIBUTING.md); both ran on Linux and passed for this engine.

The workflow `.github/workflows/skill-quality.yml` runs the first six commands above on `ubuntu-latest` with Python 3.12; it was not run here. `git diff --check` is the release gate declared in `.skills-engine/engine-manifest.yaml`, which lists no other check.

## References

Citations only, as recorded in the repository's skills, references and Kaizen records. No book content is stored here (see `copyright-safe-source-use.md`). Where the repository gives only an author, year or title, only that is listed.

### Books

- Aaron — *Profitable Blog Topics*.
- Abou-Zeid — *Knowledge Management and Business Strategies*.
- Al-Hakim — *Innovation in Business and Enterprise*.
- Anastasi — *The Seven Principles of Professional Services*.
- Bielefeld, W. and Schneider (2014) *Basics Budgeting*.
- Bly — *How to Write Simple Information*.
- Bohnet, I. (2016) *What Works*.
- Bosenberg (2023) *Stakeholder Mapping Deep Dive*.
- Bradley, C., Hirt, M. and Smit, S. — *Strategy Beyond the Hockey Stick*.
- Braganza, A. — *Looks Good to Me: Constructive Code Reviews*.
- Bria, F. — *Punch the Elephant*.
- Brown, R. (2016) *Build Your Reputation*, Capstone/Wiley.
- Champagne (2019) *Seven Steps to Mastering Business Analysis*.
- Chatterjee, A., Kiao, U., Keng, C. C. et al. — *System Design at Google*.
- Chereau, P. and Meschi, P.-X. — *Strategic Consulting*.
- Cialdini, R. — *Influence*.
- Cohen — *Consulting Drucker*.
- Cook, Harris and Barber (2022) *Management Consulting Projects*, 6th edn.
- Cotton, B. — *Hacking SaaS*.
- Croll, A. and Yoskovitz, B. (2013) *Lean Analytics*, O'Reilly Media.
- Davis (2001) *Regional Economic Impact Analysis and Project Evaluation*, UBC Press.
- Debelak, D. (2006) *Perfect Phrases for Business Proposals and Business Plans*, McGraw-Hill.
- Earl, S., Carden, F. and Smutylo, T. — *Outcome Mapping*.
- Eddy — *Blog It Right*.
- Foster and Grannell — *Essential Management Models*.
- Freed, R., Romano and Freed, S. (2011) *Writing Winning Business Proposals*, 3rd edn.
- Garbugli, É. — *The SaaS Email Marketing Playbook*.
- Golding, T. (2024) *Building Multi-Tenant SaaS Architectures*, O'Reilly.
- Graves — *Writing for Profit*.
- Harrin, E. (2020) *Engaging Stakeholders on Projects*.
- Hattori — *The McKinsey Edge*.
- Hennessy, B. (2018) *Influencer: Building Your Personal Brand in the Age of Social Media*, Citadel Press.
- Hester and Harrison (eds) (2005), chapters by Pretty, Osborn, Butler and Smith.
- Hoskins, D. — *The Product-Minded Engineer*.
- Huemann, M. (2016) *Rethink Project Stakeholder Management*.
- Hunter, V. L. with Tietyen, D. (1997) *Business to Business Marketing: Creating a Community of Customers*, NTC Business Books.
- Iny, D. — *Blog Post Ideas: 21 Proven Ways*.
- Johnson, G., Whittington, R., Scholes, K., Angwin, D. and Regnér, P. (2017) *Exploring Strategy: Text and Cases*, 11th edn, Pearson.
- Karpavičius, A. — *Software Craftsmanship Using AI*.
- Kavanaugh — *Consulting Essentials*.
- Kelley, L. D. and Sheehan, K. B. (c. 2021) *Advertising Management in a Digital Environment*, Routledge.
- King (2020) *The Fix*.
- Kirkpatrick, D. and Kirkpatrick, J. (2006) *Evaluating Training Programs*, 3rd edn, Berrett-Koehler.
- Knowles, M. (1984) *The Adult Learner: A Neglected Species*, Gulf Publishing.
- Kothand — *One Hour Content Plan*.
- Kupsh, J. and Graves, P. R. (1993) *How to Create High-Impact Business Presentations*, NTC Business Books.
- Ladley, J. (2020) *Data Governance*, 2nd edn.
- Landa, R. (2022) *Strategic Creativity*, Routledge.
- Lewis — *Project Planning, Scheduling and Control*, 6th edn.
- Lima — *Fundamentals of Writing*.
- Lin, L. C. (2013) *Decode and Conquer*, 2nd edn, Impact Interview.
- Livermore, R. — *Blogger's Quick Guide*.
- Maltz, M., Kennedy, D. S., Brooks, W. T., Oechsli, M., Paul, J. and Yellen, P. (1998) *Zero-Resistance Selling*, Prentice Hall Press.
- Marcos, J., Guesalaga, R., Hough, A. and Vincent, R. (c. 2025) *The High-Performing Key Account Manager*, Kogan Page.
- McNeil, P. (2010, 2013) *The Web Designer's Idea Book*, Volumes 2 and 3, HOW Books.
- Mellon (2018) *The Case Interview Workbook*.
- Mersch, E. (2023) *How to Run a SaaS Business*.
- Minto, B. — *The Pyramid Principle*.
- Ndemo, B. et al. (2023) *Data Governance and Policy in Africa*, Palgrave Macmillan.
- Nelson, J. (2019) *The Seven Figure Agency Roadmap*, Seven Figure Agency LLC.
- Nordic APIs — *Identity and APIs*.
- Painter-Morland (2012) *Leadership, Gender, and Organization*.
- Plumley, G. (2011) *Website Design and Development: 100 Questions to Ask Before Building a Website*, Wiley.
- PMI (2015) *Business Analysis for Practitioners*; PMI (2017) *The PMI Guide to Business Analysis*.
- Proctor — *Building Financial Models with Microsoft Excel*.
- Rasiel, E. and Friga, P. — *The McKinsey Mind*.
- Rendtorff (2016) *Stakeholder Theory*.
- Robertson, S. and Robertson, J. — *Mastering the Requirements Process*.
- Senge, P. (2006) *The Fifth Discipline*, revised edn, Doubleday; Senge, P. et al. (1994) *The Fifth Discipline Fieldbook*, Currency Doubleday.
- Serling, B. (ed.) (2002) *How to Write Million Dollar Ads, Sales Letters and Web Marketing Pieces*, The Internet Marketing Center.
- Shander (2025) *Stakeholder Whispering*.
- Smeritschnig — *The 1%: Conquer Your Consulting Case Interview*.
- Stutts, P. (2021) *The Undefeated Marketing System*, Lioncrest (Scribe Media).
- Ubels, J., Acquaye-Baddoo, N.-A. and Fowler, A. (2010) *Capacity Development in Practice*, Earthscan/SNV.
- von Halle, B. and Goldberg, L. — *The Decision Model*.
- Walling, R. (2023) *The SaaS Playbook*.
- Warfield — *Hacking the Case Interview*; *The Ultimate Case Interview Workbook*.
- Weiler and Serna (2016) *Practical Strategies for Applied Budgeting and Fiscal Administration*.
- WetFeet — *Deloitte Consulting*.
- Wheelen, T. L., Hunger, J. D., Hoffman, A. N. and Bamford, C. E. (2018) *Concepts in Strategic Management and Business Policy*, 15th edn, Pearson.
- White and Raitzer (2017) *Impact Evaluation of Development Interventions*, Asian Development Bank.
- Wickham, P. and Wickham, L. (2008) *Management Consulting: Delivering an Effective Project*, 3rd edn.
- Wiebe, J. (2011) *Copy Hackers: 6 Persuasion Strategies*, Copy Hackers.
- Winning by Design (2018) *The SaaS Sales Method for Account Executives*; *The SaaS Sales Method Fundamentals*.
- Worsley, L. (2020) *Stakeholder-led Project Management*, 2nd edn.
- Yayici (2015) *Business Analysis Methodology Book*.
- Titles cited without author: *Consulting Management EXPLAINED*; *Strategic DevOps*; *DevOps for PHP Developers*; *The DevOps Handbook*, 2nd edn; *Modern DevOps Practices*; *Growth Engineering*; *Remarkable Business Growth*; *Make Phenomenal Profits*; *Dare to Disrupt*; *Think Deeper*; *The Bezos Letters*; *Yes!*; *Buyology*; *The Adweek Copywriting Handbook*.
- Authors cited by name or year only: Adams and Straw (2016); Hattula and Köhler (2023); Hayes (2002); Hearsum (2024); Little (2014); Seasons (2020); Zukof (2021); Levinger and McLeod; Rogers and Coates (FANTA); Cooley and Linn (SUM framework); Edwards; Forde and Stevens (AWAI); Godin; Duguin; Rubinelli; Cassani; Diamond; Gujral; Mohan; and, as presented in the books above, Fred David, Hambrick and Fredrickson, Webster and Wind, Rackham, Lax and Sebenius, Malhotra and Bazerman, and Kahneman.
- Listed as recommended reading in the July 2026 upgrade record: Block, P. *Flawless Consulting*; Tammemagi, H. *Winning Proposals*; APMP *Body of Knowledge*; PMI *Project Management Body of Knowledge*.

### Repositories

- [Proposal Skills](https://github.com/peterbamuhigire/proposal-skills) — this engine's source, skills and validators.
- [Business Plan Skills](https://github.com/peterbamuhigire/business-plan-skills) and [Social Media Skills](https://github.com/peterbamuhigire/social-media-skills) — sister engines for commercial inputs (portable routes checked by `encoding_link_gate.py`).
- [chwezi-dev-engine](https://github.com/peterbamuhigire/chwezi-dev-engine/blob/main/skills/sdlc-meta/skill-writing/SKILL.md) — canonical skill-authoring standard; this engine's `skill-writing` is a pointer stub with byte-mirrored scripts.
- [chwezi-accounting-doctrine](https://github.com/peterbamuhigire/chwezi-accounting-doctrine/blob/main/doctrine/accounting-finance-doctrine.md) — finance doctrine and [finance quality gate](https://github.com/peterbamuhigire/chwezi-accounting-doctrine/blob/main/governance/finance-accounting-quality-gate.md) cited by the financial-services sector skill.
- [Everything Claude Code (ECC)](https://github.com/affaan-m/ECC) — licence not recorded here; adapted: installer scope and Git Bash path handling (`install.sh`, `install.ps1`, `install-engine.js`), plugin-manifest constraints, the Santa Method dual review in `bid-red-team-dual-review`, the submission-proof discipline, and the scoped-worker guidance in the [shortform](https://raw.githubusercontent.com/affaan-m/ECC/main/the-shortform-guide.md), [longform](https://raw.githubusercontent.com/affaan-m/ECC/main/the-longform-guide.md) and [security](https://raw.githubusercontent.com/affaan-m/ECC/main/the-security-guide.md) guides.
- [donvito/codex-astra-luna-orchestrator](https://github.com/donvito/codex-astra-luna-orchestrator) — concept reference for the `.codex/` model-policy helper (commit `21f4561`), independently implemented.
- [tt-a1i/archify](https://github.com/tt-a1i/archify) — MIT, commit `0e4949f`; the diagram-IR and render-evidence pattern behind the technical-approach figures reference in `06-methodology` (my-10-kaizen AR-15, via the SRS renderer).
- [obra/superpowers](https://github.com/obra/superpowers) — MIT; the single canonical skill-writing standard with drift check (my-10-kaizen SP-04), which turned this engine's `skill-writing` into a pointer stub.
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — MIT, commit `2686b62`; the cross-engine routing-collision gate (my-10-kaizen M10-03) that led to the differentiated `language-standards` description.
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) — Apache-2.0, commit `114ea1d`; the portfolio `PROJECT.md` context contract (my-10-kaizen IM-11) now read by the router before planning.
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) — MIT, commit `e3ba2aa`; the drift-detection pattern behind the host-file single-source check (my-10-kaizen M10-02) that aligned this engine's `CLAUDE.md` bridge.

### Standards and official sources

- **Uganda.** Public Procurement and Disposal of Public Assets Act (Cap. 205, as amended by Act 15/2021 and S.I. 96/2023); PPDA Regulations 2023; PPDA standard forms, Form 49 (Contract Management Plan), FAQs and [standard bidding documents](https://www.ppda.go.ug/standard-bidding-documents/); [PPDA](https://www.ppda.go.ug/) and its [procurement legislation](https://www.ppda.go.ug/download-reports/resource-center/procurement-legislation/); Local Governments (Financial and Accounting) Regulations 2007 (SI 25/2007); Local Governments Act 1997; Data Protection and Privacy Act 2019.
- **World Bank.** Procurement Regulations for IPF Borrowers; [procurement framework](https://www.worldbank.org/ext/en/what-we-do/project-procurement/framework) and [procurement](https://www.worldbank.org/procurement); Standard RFP for Consulting Services; *A Beginner's Guide for Borrowers* (November 2023, 2nd edn); *Evaluating Bids and Proposals, Including Use of Rated Criteria* (February 2025, 3rd edn; [rated criteria](https://www.worldbank.org/en/about/rated-criteria)); Environmental and Social Framework (2018, updated 2024); Gender Data Portal.
- **African Development Bank.** Procurement Policy for Bank Group Funded Operations (2015, revised 2023); Rules and Procedures for the Use of Consultants (2023) and for Goods, Works and Non-Consulting Services (2023); [Integrated Safeguards System (2023)](https://www.afdb.org/en/documents/african-development-bank-groups-integrated-safeguards-system-2023) and [its effectiveness notice](https://www.afdb.org/en/news-and-events/announcement-effectiveness-bank-groups-updated-integrated-safeguards-system-iss-71365); ESAP; Operations Manual; IDEV Evaluation Policy and Guidelines; PCR Guidelines; Financial Products; Climate Change and Green Growth Strategy; Country Diagnostic Note for Uganda (December 2025).
- **United Nations.** UNDP Handbook on Planning, Monitoring and Evaluating for Development Results (2009); [UNDP procurement strategy](https://www.undp.org/procurement/strategy); UNDP/EU Guidelines for Submitting Project Proposals for CSOs (January 2025); UNDP Capacity Development Practice Notes; UNDP Human Development Report 2024; GEF Small Grants Programme proposal template (GEF-7); UN Trust Fund proposal guidelines; UNICEF technical and financial proposal format (Annex E, 2021); UNFCCC technical proposal template (Annex 9); UNGM [Code of Conduct](https://www.ungm.org/Public/CodeOfConduct) and [Procurement Practitioner's Handbook](https://www.ungm.org/Shared/KnowledgeCenter/Pages/PPH2); UNDG UNDAF Companion Guidance; UN Women Intersectionality Resource Guide (2022); ECOSOC (1997); UN Country Analysis and Uganda SDG Analysis Report Summary (2025).
- **Other development partners.** OECD-DAC evaluation criteria (2019 revision) and capacity-development guidelines; EU PRAG; GIZ and EU/BMZ procurement rules; USAID ADS 302/303, 2 CFR 200 and the HICD Handbook (2010); ILO Basic Principles of Monitoring and Evaluation; IFRC Handbook for Monitoring and Evaluation (2002); ECDPM 5Cs framework; Oxfam Gender Analysis Frameworks (1999); Ford Foundation (2023) *Understanding Data Governance in Uganda*; Uzbekistan M&E Guide (2025); DHS survey rounds.
- **Data protection and AI governance.** African Union Data Policy Framework (2022); AU Convention on Cyber Security and Personal Data Protection (Malabo Convention, 2014); Kenya Data Protection Act 2019; Rwanda personal data protection law (2021); GDPR; EU AI Act; NIST AI RMF; ISO/IEC 42001 and ISO/IEC 23894.
- **Assurance and quality standards.** ISO/IEC 27001, 27017 and 27018; SOC 2; ISO 9001; ISO 14001; ISO 20400; ISO 8601; WCAG 2.2.

### Websites and articles

- [Shipley proposal assessment](https://www.shipleywins.com/consulting/proposal-assessment) — premium promise-to-proof benchmark (accessed 22 September 2026).
- Eleken: [validating product ideas](https://www.eleken.co/blog-posts/how-to-validate-product-ideas), [mobile app onboarding](https://www.eleken.co/blog-posts/mobile-app-onboarding-best-practices), [AI design workflow](https://www.eleken.co/blog-posts/ai-design-workflow) and [launching a SaaS business](https://www.eleken.co/blog-posts/how-to-launch-a-saas-business) — practitioner cross-checks in the SaaS discovery and pilot skills.
- OpenAI: [release notes](https://openai.com/products/release-notes/), [API models](https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4), [GPT-5.6](https://openai.com/index/gpt-5-6/), [GPT-6 Astra safety overview](https://openai.com/index/safety-overview-gpt-6-astra/), [image generation](https://developers.openai.com/api/docs/guides/image-generation) and [image prompting](https://developers.openai.com/api/docs/guides/image-prompting) — model-currentness and prompt-compilation evidence in the Kaizen and AI-prompting records.

## Quality and improvement

The engine audits itself under the Portfolio Kaizen Standard: a published score is capped at 65 out of 100, and every plan targets 95 with evidence and a re-audit date. The evidence is committed in the repository:

- [`docs/kaizen/2026-10-engine-kaizen/`](docs/kaizen/2026-10-engine-kaizen/05-final-report.md), the 29 October 2026 cycle: World Bank form crosswalk, hard package ceiling, routing measures, scoped source register.
- [`docs/kaizen/2026-10-engine-kaizen-pass-2/`](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md), the 31 October 2026 cycle, with the open backlog in [`06-next-cycle.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/06-next-cycle.md) and the documentation follow-ups in [`07-docs-followups.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md).
- Earlier cycles and reviews are indexed in [`docs/README.md`](docs/README.md).

**Latest score.** The pass 2 report records a raw score of 61.4 and a published score of `min(61.4, 65)` = 61.4 for 31 October 2026. The baseline measured before its changes was raw 54.5, and the 29 October final was raw 58.5. The target of 95 is not met. Scores are reviewer judgements, not bid-win probabilities, and a missing mandatory live-bid requirement blocks release whatever the score.

**Open findings that matter to a user.**

- No real solicitation, bidder evidence pack, evaluator or submission receipt has been used. The tools prove their mechanics on fictional data only.
- PPDA: the scope of the e-GP mandate, the monetary thresholds and the bid and performance security amounts are `NOT_ASSESSED`; the PPDA reference labels its UGX figures as unverified.
- AfDB, UNDP, PRAG and Uganda data-protection claims are unverified. The skills label the AfDB figures and the 0 to 4 scoring scale as such.
- Routing is measured with a lexical proxy over skill descriptions. The 41 fixtures name 27 of the 115 skills, and no model-judged run has been made.
- The World Bank form map follows the March 2025 Standard RFP; the issued RFP controls where it differs.
- Accessibility is unchanged at 40 out of 100: no assistive-technology run has been made.

**Calendar of date-triggered gates.** One gate in this engine depends on the calendar. No other check compares anything with today's date, and no unit test depends on it.

| Date | Gate | Effect | How it was verified |
|---|---|---|---|
| 2026-11-30 | Source register [`docs/source-registers/2026-10-currentness.json`](docs/source-registers/2026-10-currentness.json): 14 records (10 `SCOPED`, 4 `NOT_ASSESSED`), all volatile, all with review date 2026-11-30 | The gate passes through 2026-11-30. From 2026-12-01 `scripts/validate_skills.py` and `scripts/check_source_currency.py` exit 1 with `review expired` for all 14 records, and the CI validation step fails with them | The scripts have no `--as-of` option, because they read `date.today()`. The gate was run with that call replaced: 0 errors on 2026-11-29 and 2026-11-30, 14 on 2026-12-01 and 2027-01-01; `validate_skills.py` run the same way exits 0 on 2026-11-30 and 1 on 2026-12-01 |

To renew the gate, re-read each `SCOPED` source, then update its `access_date`, `verified_date` and `review_date`. A volatile record may be reviewed at most 45 days after it was verified. A claim that cannot be re-read stays `NOT_ASSESSED`: it carries no verified date, but its `review_date` must still move forward, because the gate checks all 14 records. The re-audit is due on 30 November 2026, or before a live bid if that is sooner.

### What the October 2026 kaizen improved

This lists the kept changes of the 29 October cycle, the 31 October pass 2 and the 31 October documentation wave. Both cycle reports record that no experiment was reverted. Every commit named below is on `main`. The sources are the [29 October report](docs/kaizen/2026-10-engine-kaizen/05-final-report.md) and [experiment log](docs/kaizen/2026-10-engine-kaizen/03-experiment-log.md), and the pass 2 [backlog](docs/kaizen/2026-10-engine-kaizen-pass-2/02-improvement-backlog.md), [experiment log](docs/kaizen/2026-10-engine-kaizen-pass-2/03-experiment-log.md), [validation record](docs/kaizen/2026-10-engine-kaizen-pass-2/04-validation-record.md) and [final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md). "Measured" means the figure was re-run on 31 October 2026 for this section, by unpacking the earlier commit into a scratch directory; anything else is copied from the cited record. All proof is on fictional fixtures, a lexical routing proxy, or text read from sources on 31 October. No real bid, evaluator or model-judged routing run has been used.

**Defects fixed, most serious first**

- **Critical: the stale World Bank form map survived in the skill the router loads first.** The 29 October fix had corrected only the reference guide. `world-bank/SKILL.md`, its scoring guide and `afdb/SKILL.md` still taught TECH-5 as team composition, TECH-7 as the staffing schedule, TECH-8 as the work schedule and a FIN-5 form that the March 2025 RFP does not have. `6efc922` corrects all three files and adds `scripts/check_form_labels.py`, which `validate_skills.py` now runs. Measured: the scanner reports 12 findings on 8 lines in the pre-fix files and 0 now. The 12 form ids were also checked against the downloaded RFP text (validation record). Limit: a paragraph that carries a recorded warning phrase is exempt from the scan as a whole.
- **Critical: the World Bank forms guide itself.** `references/tech-fin-forms-guide.md` described the retired form order and an invented FIN-5 "Miscellaneous Expenses" form. `5a4e39e` rewrote it from 306 to 89 lines against the inspected March 2025 RFP and says the issued RFP controls; `09c8adc` completed the form names in the fixture it is tested against. Three regression tests cover the current map, a stale staffing or extra financial form and a duplicate form (experiment log); the unit suite went from 52 tests (measured) to 55 (log) with this change.
- **Major: World Bank scoring norms that no issued document states.** The skill and scoring guide gave "typically 75" as the pass mark, 10 to 20 points for firm experience, 30 to 50 for methodology and a shortlist of 3 to 6. `3db28f3` replaces them with the ranges in the Procurement Regulations (Seventh Edition, September 2025, Annex X) and the RFP Data Sheet: pass mark set by the Data Sheet with an indicative 70 to 85, firm experience 0 to 10, methodology 20 to 50, shortlist 5 to 8. The scoring guide's worked example was recomputed. Measured: the retired phrases are in the old skill (lines 136 and 277) and absent now. Not changed, and labelled unverified: the 0 to 4 scale and the AfDB figures, because the Bank's rated-criteria guidance and the AfDB pages could not be fetched.
- **Major: PPDA submission guidance contradicted the 2023 Regulations.** The skill applied the consultancy two-envelope rule to every method, said a bid securing declaration is always included and said PPDA uses a performance securing declaration instead of guarantees. `a8cac10` adds a decision table for method, envelopes, delivery channel and the four securities, each tied to a regulation (Rules and Methods regs 63, 66 and 68; Consultancy reg 47; Contracts reg 11), with four tests that refuse the retired claims. The scope of the e-GP mandate, the monetary thresholds and the security amounts stay `NOT_ASSESSED`.
- **Major: no method for a capped, weighted brief.** The section skills' default lengths add up to at least 9.5 pages for a six-page cap, and `06-methodology` said its section should be the longest. `aa49a51` adds a weighted page-budget and compliance-matrix reference, a router rule that the solicitation's caps and weights override default lengths, and `scripts/page_budget_check.py` (13 tests). Measured on the fictional six-page brief: the script proposes 2.0, 1.5, 1.5 and 1.0 pages, and the old habit of 5.0, 0.25, 0.25 and 0.5 exits 1 with floor errors. It is allocation arithmetic and predicts no evaluator score.
- **Major: envelope separation was checked by file name only.** `00ef43d` adds `proposal_fixture_check.py --check-content`, which scans text and `.docx` files (body, headers, footers, footnotes) of each envelope for the other envelope's markers. Measured: with a line "UGX 45,000,000" planted in the technical file of the sanitised example, the previous checker returned PASS (exit 0) and the new option returns FAIL (exit 1) with file, line and marker; the clean example passes. The option is opt-in, 13 tests cover it, other file types are `NOT_ASSESSED` unless accepted, and the live-package part stays open.
- **Major: Windows checkout paths in shipped content.** `CONTRIBUTING.md`, `docs/skill-authoring-standard.md`, `skills/meta/skill-writing/SKILL.md` and the example submission manifest carried drive-letter paths, and the link gate matched only an older pattern. `7ad4f13` replaces them with catalogue wording and adds a gate rule (URLs, install-scope text, dated records, scripts and tests are exempt; 4 tests). Measured: the gate reports 6 lines in 4 files before the fix and 0 after; the pass 2 log says five files, but the six lines it lists are in four. About 18 lines remain in dated records, which the gate exempts on purpose. `4066815` had already replaced the same kind of path in the router `AGENTS.md`.

**New checks and tests**

- **Hard file ceiling and package parity** (`4066815`, `f0e5234`). `scripts/check_marketplace.py`, run by `validate_skills.py`, fails when the checkout or the package passes 5,000 entries, when marketplace identity, version or source drift from the plugin, when the plugin's skill list differs from the `SKILL.md` files on disk, or when a skill path escapes or is a symlink; a traversal error fails closed. Five tests include both boundary counts. Measured at `b608bcb`: 870 checkout files (the count includes `.git`, so it grows with every commit) and 530 package files, against the limit of 5,000.
- **Source currency register and its gate** (`be2c774`, `affb97f`). A dated register of volatile procurement, AI and data-protection claims, with a gate that rejects expired, malformed and future-verified rows. Pass 2 grew it from 11 records (7 `SCOPED`, 4 `NOT_ASSESSED`) to 14 (10 and 4) after reading the primary sources, corrected the GIZ record to the 1 September 2025 version, and made the gate refuse a `NOT_ASSESSED` row that carries a verified date, a non-https URL, an unknown freshness class and a volatile review window over 45 days (7 tests, was 3). Measured: both counts; `check_source_currency.py` exits 0. By design the gate fails from 2026-12-01 until the records are re-verified, as the calendar above says. It checks metadata only and verifies no claim.
- **CI runs every registered check** (`7ad4f13`). `.github/workflows/skill-quality.yml` ran 2 commands and now runs 6: skill validator, routing, link gate, ingestion guardrail, fixture check and the unit suite. Measured: the workflow lists 2 commands at `9089c0a` and 6 now, and the same commands exit 0 locally. It was not run on a GitHub runner (`NOT_ASSESSED`).

**Routing and discoverability**

- **Routing metrics that show first-rank accuracy** (`feea230`). The runner reported only whether the expected skill was in the top three (100%), which hid that it ranked first for 19 of 26 fixtures. It now reports first-rank accuracy and checks forbidden primary routes (owned negatives), and the fixtures grew from 26 to 31. Measured: 19/26 (new runner over the earlier tree) before, 23/31 after. One collision stays visible: the World Bank FTP prompt ranks UNDP first.
- **Bidder wording and three-plus-two fixtures** (`635e76a`). The descriptions of `ppda-uganda`, `world-bank`, `afdb` and `06-methodology` gained the words bidders use, for example "open domestic bidding" and "bid data sheet", and each now has three positive and two owned-negative fixtures (it was one skill, per the pass 2 log). Measured: the original 31 fixtures move from 23 to 24 first-rank hits; the 41-fixture set scores 32/41 first-rank, 41/41 in the top three and 7/7 owned negatives. This is a lexical proxy over descriptions, and 111 of 115 skills still lack that fixture coverage.

**Documentation and portability**

- **Commands that run on Linux** (`dbc2f88`, `31c3cc9`, `49f1c5a`). Contributor docs, the router and the README replaced PowerShell blocks and backslash paths with `python3` commands, and the README gained the Validation section (seven checks, dependencies, expected results). Install goes through `bash install.sh`, because git stores the file without the executable bit. A router path to a skill that does not exist (`skills/ai-agent-pricing-and-packaging-proposal`) now points to `skills/ai-agent-proposals/ai-agent-pricing-and-packaging-proposal`. Measured: the seven registered checks exit 0 on this Linux host; the preview, install, `doctor` and uninstall sequence into a scratch project installed 353 files including 115 `SKILL.md`, `doctor` reported 0 missing and 0 modified, and uninstall removed 353. `install.ps1` was not run (no `pwsh`).
- **Documentation index and gate calendar** (`c28f206`, `81caeef`, `b608bcb`). `docs/README.md` groups the 16 entries of `docs/`; [`07-docs-followups.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md) records what the wave left alone and the cross-engine mismatches; the calendar above names the one date-triggered gate. The behaviour on 2026-11-30 and 2026-12-01 was checked by replacing `date.today` for one process, as recorded in that file; it was not re-run for this section.

**Before and after**

| Measure | 29 Oct before (`8eddd70`) | 29 Oct after (`9089c0a`) | Now (`b608bcb`) |
|---|---:|---:|---:|
| Raw score; published `min(raw, 65)` (reports) | 53; 53 | 58.5; 58.5 | 61.4; 61.4 |
| Unit tests (measured) | 52 | 63 | 117 |
| Routing fixtures (measured) | 26 | 31 | 41 |
| First-rank hits (measured) | 19/26 | 23/31 | 32/41 |
| Owned-negative checks passing (measured) | not checked | 2/2 | 7/7 |
| Dated source records (measured) | none | 11 | 14 |
| Stale form-label findings, current scanner over each tree (measured) | 22 | 12 | 0 |
| Commands run by CI (measured) | 2 | 2 | 6 |

Pass 2 re-scored the engine with a stricter inspection before changing anything and got raw 54.5, so its 61.4 should be compared with 54.5, not with 58.5. Every score is below the cap of 65, so raw and published are equal, and the target of 95 is not met. The scores are reviewer judgements, not measurements of bid-win probability.

### Local marketplaces

Both Codex and Claude can install the local `proposal@chwezi-proposal` marketplace plugin. In the catalogue-resolved checkout, use `codex plugin marketplace add .` then `codex plugin add proposal@chwezi-proposal`; Claude uses `claude plugin marketplace add .` then `claude plugin install proposal@chwezi-proposal`. Native offline installation was tested in a disposable container on 29 October 2026 and was not repeated on 31 October; public directory approval and model behaviour remain unassessed. `scripts/validate_skills.py` enforces a hard limit of 5,000 files per engine for both the full checkout (including Git and caches) and the package inventory; on 31 October 2026 they held 838 and 528. Keep build dependencies and disposable artefacts outside the checkout.
