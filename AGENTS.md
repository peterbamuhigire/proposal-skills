# Proposal Skills Repository

This repository is a dual-compatible skill system for consulting proposals, procurement responses, and related writing workflows. Active skills live under `skills/`; load the relevant `skills/<skill-name>/SKILL.md` file directly.

## Baseline Rules
- Treat each `SKILL.md` as the execution contract and nearby `references/` files as deeper supporting material loaded only when needed.
- Every `SKILL.md` must include this exact acknowledgement line immediately below the first top-level `# ...` heading, not in frontmatter: `Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.`
- Load `skills/profiles-sectors/profiles/SKILL.md` before drafting any proposal text so voice, signatory, and proposer identity stay consistent.
- Use `skills/profiles-sectors/sectors/SKILL.md` to decide which procurement framework and industry sector skills apply.
- Use `skills/strategy-positioning/critical-analysis-business-logic/SKILL.md` as the reasoning, business-sense, feasibility, and achievability gate for high-stakes proposal content and final review.
- Apply `skills/meta/anti-ai-slop/SKILL.md` as a real-time guardrail while writing every proposal section, then run `skills/meta/ai-slop-audit/SKILL.md` after each section or major iteration and as the final gate before submission; a grade of F (Blocked) blocks submission until the blocking findings are fixed.
- Keep technical and financial proposal content separate when the procurement process requires separate envelopes or forms.

## Task Routing
- Full proposal orchestration or section drafting: start at [skills/SKILL.md](/C:/wamp64/www/proposal-skills/skills/SKILL.md)
- Proposal identity and voice: [skills/profiles-sectors/profiles/SKILL.md](/C:/wamp64/www/proposal-skills/skills/profiles-sectors/profiles/SKILL.md)
- Procurement and sector routing: [skills/profiles-sectors/sectors/SKILL.md](/C:/wamp64/www/proposal-skills/skills/profiles-sectors/sectors/SKILL.md)
- Proposal sections: use the numbered section skills under `skills/01-` through `skills/10-`
- Supporting proposal domains: use unnumbered skills such as `skills/domain-delivery/project-management/`, `skills/domain-delivery/monitoring-and-evaluation/`, `skills/domain-delivery/risk-management/`, `skills/domain-delivery/stakeholder-engagement/`, and related folders when the ToR or methodology needs that domain
- GIZ / EU / BMZ local procurement responses: use `skills/domain-delivery/giz-eu-local-procurement-response/` when a tender includes GIZ AVB/local application requirements, two technical/financial zip folders, a GIZ assessment grid, self-declaration, price schedule, technical threshold, or GIZ clarification protocol.
- EAC e-commerce BDS / digital trade programme design: use `skills/domain-delivery/eac-ecommerce-bds-programme-design/` for donor-funded company selection, needs assessments, tailored technical assistance, expert-pool deployment, results-based monitoring, and lessons-learned/scaling methods.
- Website design and development proposals: use `skills/strategy-positioning/website-design-proposal-strategy/` whenever a proposal includes a website, SEO-ready site, landing page, ecommerce, portal, web app frontend, content hub, or website costing component
- AI and technical transformation proposals: use `skills/strategy-positioning/ai-transformation-proposal/` plus `skills/profiles-sectors/references/technical-strategy-credibility-checklist.md` for AI, SaaS, software, cloud, API, integration, data, or operations claims
- Premium, executive, and high-ticket proposals: use `skills/strategy-positioning/premium-client-proposal-strategy/` and `skills/strategy-positioning/premium-pricing-and-value-defense/` when value, proof, pricing confidence, or premium-rate defence matters
- Premium commercial writing: use `skills/writing-content/premium-commercial-writing/` when proposals, cover letters, executive summaries, case studies, business documents, or blogs need stronger proof, evaluator-friendly structure, premium-fee-worthy language, or SEO/AI-search friendliness where relevant
- Discovery and objections: use `skills/strategy-positioning/sales-discovery-and-objection-handling/` when buyer assumptions, clarification questions, price objections, risk concerns, timeline objections, or follow-up logic matter
- SaaS implementation and SaaS product-development proposals: use the `skills/saas-*` skill family (saas-discovery-and-qualification, saas-business-case-and-roi-modeling, saas-pricing-and-packaging-proposal, saas-implementation-methodology, saas-poc-and-pilot-scoping, saas-procurement-and-security-questionnaire, saas-customer-success-and-adoption-proposal, saas-mutual-action-planning-and-close-plans, saas-vertical-positioning, saas-objection-handling-and-competitive-displacement, saas-lifecycle-communications-as-deliverable, saas-trust-and-compliance-credentials-section, saas-multi-tenant-architecture-credibility-block, saas-pilot-to-rollout-change-management) for control plane / application plane methodology, tenant isolation, MEDDPICC qualification, MAP, business case, customer success, lifecycle communications, trust and compliance, and vertical positioning
- AI-on-SaaS proposals (multi-tenant SaaS + AI features such as RAG, copilots, agents, AI analytics): use the `skills/ai-on-saas-*` skill family (ai-on-saas-combined-methodology, ai-on-saas-discovery-and-qualification, ai-on-saas-business-case-and-roi, ai-on-saas-pricing-and-packaging-proposal, ai-on-saas-poc-and-pilot-scoping, ai-on-saas-risk-and-responsible-ai, ai-on-saas-compliance-credentials, ai-on-saas-procurement-and-questionnaire, ai-on-saas-change-management-and-adoption, ai-on-saas-team-composition, ai-on-saas-vertical-positioning) for the three-plane methodology, eval discipline, hallucination SLO, Responsible-AI commitment, AI pricing patterns, AI procurement questionnaire pack, and AI vertical positioning. The headline skill is `skills/ai-on-saas-proposals/ai-on-saas-combined-methodology/`. Use `skills/strategy-positioning/ai-transformation-proposal/` for generic AI strategy where there is no SaaS layer.
- AI-agent / multi-agent product proposals (autonomous LLM systems that plan, call tools, decide, and act — as stand-alone products, multi-agent systems, or agentic layers inside SaaS): use the `skills/ai-agent-*` skill family (ai-agent-discovery-and-qualification, ai-agent-business-case-and-roi, ai-agent-pricing-and-packaging-proposal, ai-agent-poc-and-pilot-scoping, ai-agent-methodology, ai-agent-risk-and-responsible-ai, ai-agent-compliance-credentials, ai-agent-procurement-and-questionnaire, ai-agent-change-management-and-adoption, ai-agent-team-composition, ai-agent-vertical-positioning) for the eight-phase agentic methodology (Discover → Action-Catalogue → Architecture → Build → Shadow → Supervised → Agentic → Operate), autonomy-level discipline, action catalogue with reversibility classification, kill-switch architecture and drill, action audit log to regulator-grade, agent pricing patterns (per-resolution / per-outcome / per-step / per-agent / hybrid / success-based), Responsible-AI Agent Commitment with named Agent Safety Lead, agent procurement Q&A, trust staging, and agent vertical positioning. Headline skill is `skills/ai-agent-proposals/ai-agent-methodology/`. Load alongside the `ai-on-saas-*` family when the agent lives inside a multi-tenant SaaS product. Use `skills/strategy-positioning/ai-transformation-proposal/` for generic AI strategy where there is no agentic deliverable.
- AI-agent commercial, SLA, and contractual layer (agent SLA classes with credit schedules, refund and abort mechanics, MSA / SLA addendums, outcome-pricing structures, packaging shapes, procurement-objection responses on commercials, renewal mechanics): use the `skills/ai-agent-sla-and-credit-schedule`, `skills/ai-agent-commercial-packaging`, `skills/ai-agent-contract-language-pack`, `skills/ai-agent-success-fee-and-outcome-pricing`, `skills/ai-agent-intervention-credit-and-abort-refund`, `skills/ai-agent-msa-and-sla-addendum-templates`, `skills/ai-agent-procurement-objections-on-commercials`, and `skills/ai-agent-renewal-and-true-up` skills. Load alongside `skills/ai-agent-pricing-and-packaging-proposal` when the proposal moves from value narrative to contract-grade exhibits (Pricing Exhibit, SLA Exhibit, Credit and Refund Exhibit, MSA Addendum, Abandonment-and-Refund Policy, Dispute Resolution and Audit Rights, Vendor Cost Pass-Through, Renewal Clauses, Outcome-Pricing Clauses). Vertical SLA variants for financial services, public sector, and healthcare live under `skills/profiles-sectors/references/ai-agent-sla-financial-services.md`, `ai-agent-sla-public-sector.md`, and `ai-agent-sla-healthcare.md`.
- Service design and support: use `skills/strategy-positioning/service-design-proposal-strategy/` for journeys, blueprints, co-creation, and service implementation; use `skills/strategy-positioning/customer-service-and-maintenance-proposals/` for SLAs, support, escalation, maintenance, and post-launch optimisation
- Proposal narrative: use `skills/strategy-positioning/proposal-storytelling-and-evaluator-journey/` when the proposal needs an evaluator journey, case-story spine, design rationale, or presentation/sign-off flow
- Serious analysis and business logic: use [skills/strategy-positioning/critical-analysis-business-logic/SKILL.md](/C:/wamp64/www/proposal-skills/skills/strategy-positioning/critical-analysis-business-logic/SKILL.md) before methodology, work plan, financial, transformation, and final-review outputs
- Language and tone: use [skills/language/east-african-english/SKILL.md](/C:/wamp64/www/proposal-skills/skills/language/east-african-english/SKILL.md), [skills/language/language-standards/SKILL.md](/C:/wamp64/www/proposal-skills/skills/language/language-standards/SKILL.md), and `skills/writing-content/premium-commercial-writing/` as cross-cutting review layers when commercial polish, proof, or premium value matters
- Skill maintenance: use [skills/meta/skill-writing/SKILL.md](/C:/wamp64/www/proposal-skills/skills/meta/skill-writing/SKILL.md), [skills/meta/skill-safety-audit/SKILL.md](/C:/wamp64/www/proposal-skills/skills/meta/skill-safety-audit/SKILL.md), and [skills/meta/update-claude-documentation/SKILL.md](/C:/wamp64/www/proposal-skills/skills/meta/update-claude-documentation/SKILL.md)
- Anti-slop quality gate: use `skills/meta/anti-ai-slop/SKILL.md` as a real-time guardrail on every section while writing, and `skills/meta/ai-slop-audit/SKILL.md` to grade each section or iteration (A/B/C/F) and as the final gate before submission; grade F blocks submission. These pair with `skills/strategy-positioning/critical-analysis-business-logic/SKILL.md`, which tests the reasoning
- Blog workflows: use `skills/writing-content/blog-idea-generator/` and `skills/writing-content/blog-writer/` only for content publishing tasks, not for proposal work

## Document and Spreadsheet Tooling

- Before promising `.docx`, `.pdf`, `.xlsx`, application registers, scoring matrices, price schedules, budgets, dashboards, CV packs, or annexes, check whether document and spreadsheet tooling is available on the machine.
- Prefer available Codex/Claude document and spreadsheet plugins. If unavailable, use local Python libraries such as `openpyxl`, `XlsxWriter`, `pandas`, `python-docx`, `docxtpl`, `docxcompose`, `pypandoc`, `markdown`, `PyMuPDF`, `pypdf`, `pdfplumber`, and `reportlab`.
- Check binaries such as `pandoc`, LibreOffice/`soffice`, `wkhtmltopdf`, and `tesseract` where the output route needs them.
- Run a minimal DOCX/XLSX smoke test on a new machine before production export.
- Never claim a generated Word, PDF, or Excel file exists unless it was actually written and opened or validated.

## Cross-Engine Handoffs

- Proposal to SRS: when a bid is won or a proposal becomes delivery scope, hand off the ToR, final technical proposal, methodology, assumptions, exclusions, support promises, pricing options, evaluation criteria, and clarification responses to the SRS engine for PRD/SRS, governance, acceptance criteria, evidence, and rollout planning.
- Proposal to website delivery: for website-only or website-led work, hand off approved scope, discovery notes, sitemap/content/SEO assumptions, design rationale, launch commitments, acceptance criteria, support package, and commercial boundaries to the website engine.
- Proposal to implementation: route software, SaaS, AI, cloud, integration, API, security, data, and operations promises through the SRS engine first where formal requirements are needed, then to the master engineering engine for production implementation.
- Implementation to maintenance/support: ensure the proposal's support, SLA, escalation, warranty, maintenance, and optimisation language matches the final runbooks, release evidence, incident process, and retainer model.
- Website launch to growth/retention: renewal, QBR, experimentation, observability, retention, and support findings can become proposal inputs for retainers, enhancements, and change requests.

## Working Model
1. Identify the user's actual deliverable.
2. Load `skills/SKILL.md` when the deliverable spans multiple proposal sections or domains.
3. Load only the directly relevant section, domain, sector, and framework skills.
4. Read local `references/` files only when they add material value to the current task.
5. Draft or revise the output, then run a final pass for tone, consistency, and compliance.

## Quality Expectations
- Prefer concrete, evaluator-facing language over generic corporate boilerplate.
- Make the logic visible: claim, evidence, warrant, assumption, countercase, and implication should be clear for load-bearing proposal claims.
- Do not call a proposed approach convincing, innovative, or high-value unless it is feasible under the team, time, budget, client data, approvals, and country constraints.
- Use British English and East African professional tone for proposal work unless the active skill says otherwise.
- Keep outputs aligned across profile, methodology, work plan, staffing, and pricing.
- When a skill exposes `Use When`, `Do Not Use When`, `Required Inputs`, `Workflow`, `Quality Standards`, `Anti-Patterns`, and `Outputs`, follow those sections as the default contract.

## Change Safety
- Keep active skills under `skills/` unless the repository architecture is explicitly changed.
- Do not duplicate logic into parallel Claude-only and Codex-only files when one `SKILL.md` can serve both.
- If you modify or add skills, keep frontmatter limited to `name` and `description`, keep the body execution-oriented, and prefer moving heavy detail into `references/`.


## Finance & Accounting Trigger

For finance/accounting/IFRS/IAS work, use the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine` whenever the user's request, the artefact being generated, or the code being edited touches **any** of:

- Money flows: sales, purchases, payments, refunds, credit notes, expenses
- Stock and inventory
- Payroll
- Tax (VAT, PAYE, WHT, NSSF, income tax, customs, excise, EFRIS, eTIMS)
- Grants, donations, donor restrictions
- Banking, mobile money, POS, card settlement, cash drawer
- Fixed assets
- Financial reports, management accounts, statutory returns
- Chart of Accounts, journals, ledger, posting services, period state, audit trail
- Reconciliation, close, migration, opening balances
- Internal controls, audit, evidence packs
- Any IFRS or IFRS for SMEs section

When the trigger fires:

1. For finance/accounting/IFRS/IAS work, use the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine`.
2. Read the relevant doctrine reference file in the finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`).
3. Read the corresponding finance skill `SKILL.md` in the finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`).
4. Apply the **finance & accounting quality gate** from the finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`).
6. Record the gate run in the artefact manifest.

The `finance-module-audit` skill (the corresponding skill in the finance engine, `C:\wamp64\www\chwezi-accounting-doctrine`) auto-runs whenever the user asks to analyse, review, audit, build, propose, or replace any software system with even a slight finance element.

