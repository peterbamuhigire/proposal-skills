# Proposal Skills

**Proposal Skills** (repository `proposal-skills`) is a 115-skill engine, usable in Claude Code and Codex, whose purpose is to help consultants, agencies and firms win work by writing proposals that are compliant, persuasive, deliverable and written in natural professional English. It turns a real brief (terms of reference, request for proposals, tender notice or a client conversation), the evaluation model and the proposer's own evidence into a complete consulting proposal, Expression of Interest, tender response, retainer proposal or partnership proposal, focused on the East and Central African market and its donor, public-sector and private-sector buyers.

It works section by section, not as one opaque batch. The numbered pipeline drafts the cover letter, executive summary, understanding of the assignment, firm profile, relevant experience, methodology, team, work plan, EOI and a separate financial proposal. Around it sit proposer-profile and procurement-framework routing (PPDA, World Bank, AfDB, UNDP, GIZ and others), delivery-domain methods (M&E, risk, change, safeguards, consulting frameworks, business analysis), positioning and commercial skills (premium pricing, discovery and objections, key-account pursuit, tender orals, storytelling, website and marketing service proposals) and specialist families for SaaS, AI-on-SaaS and AI-agent products and their commercial terms. A section-by-section proposal phrase bank and a power-paragraph method give every section a human, specific, evidence-led voice, while anti-slop, critical-analysis and red-team gates stop unsupported claims, generic prose and delivery promises the team cannot keep.

It helps proposal teams, independent consultants, digital and marketing agencies, development-sector firms and bid reviewers in three ways: it raises win rates by making the evaluator's decision easy (the client's own words, proof beside every claim, price stated plainly next to value); it protects the firm by keeping methodology, staffing, schedule and price consistent and by refusing to invent credentials, statistics or compliance; and it builds long-term revenue through key-account planning, strategic-account negotiation, orals preparation and win-loss learning. It owns proposal content and structure; current or uncertain facts route to the Digital Research Engine, finance to the Chwezi Accounting Doctrine, visual design to Design System Skills, and delivery work to the relevant companion engines.

## Capabilities

| Category | Skills | What it covers |
|---|---|---|
| `profiles-sectors` | 18 | Proposer identity/voice, procurement framework and industry-sector routing, compliance references |
| `saas-proposals` | 14 | SaaS discovery/qualification, business case & ROI, pricing/packaging, implementation methodology, PoC/pilot scoping, procurement & security questionnaire, customer success, vertical positioning |
| `domain-delivery` | 16 | Project management, M&E, risk management, stakeholder engagement, GIZ/EU/BMZ local procurement response, EAC e-commerce BDS programme design, retail-transformation proposals |
| `ai-agent-proposals` | 11 | Eight-phase agentic methodology, autonomy-level discipline, action catalogue, kill-switch architecture, Responsible-AI Agent Commitment, agent procurement Q&A |
| `ai-on-saas-proposals` | 11 | Three-plane methodology, eval discipline, hallucination SLO, Responsible-AI commitments, AI pricing patterns, AI procurement questionnaire pack |
| `strategy-positioning` | 12 | Critical-analysis/business-logic gate, website-design proposal strategy, AI-transformation proposals, premium-client and premium-pricing strategy (offer order, strategic-account negotiation, marketing-service proposals), discovery and objections, key-account pursuit and account plans, tender orals and proposal presentation, evaluator-journey storytelling |
| `pipeline` | 10 | Numbered proposal sections |
| `meta` | 9 | kaizen-improvement-system, anti-ai-slop, ai-slop-audit, bid-red-team-dual-review, submission-proof-and-receipt-discipline, operational-readiness-and-localisation, skill-writing, skill-safety-audit, update-claude-documentation |
| `ai-agent-commercial` | 8 | Agent SLA/credit schedules, commercial packaging, contract-language pack, success-fee/outcome pricing, intervention-credit and abort-refund, MSA/SLA addendum templates |
| `writing-content` | 3 | Premium commercial writing (proposal phrase bank and power-paragraph method), blog idea generator, blog writer |
| `language` | 2 | East African English, language standards |

Total: 115 `SKILL.md` files under `skills/` (including the parent router `skills/SKILL.md`).

## Orchestration contract

For multi-phase proposal work, use the dated [runtime-agnostic orchestration contract](docs/operations/runtime-agnostic-orchestration-2026-09-07.md). It defines scoped packages, evidence and pricing checkpoints, context hygiene, least agency, and sanitised handling of external content for Claude and Codex without changing runtime capabilities.

## Installation

```
# Native Claude Code plugin
/plugin marketplace add https://github.com/peterbamuhigire/proposal-skills
/plugin install proposal@chwezi-proposal

# npm-free, from a clone
git clone https://github.com/peterbamuhigire/proposal-skills
cd proposal-skills
./install.sh --scope project      # macOS/Linux/Git Bash
.\install.ps1 -scope project      # Windows PowerShell
```

`install.sh`/`install.ps1` delegate to the vendored `scripts/install-engine.js` (Node ≥18), which also supports `--dry-run` (prints the plan, writes nothing), `--json`, and `--scope user` (default, `~/.claude`) as an alternative to `--scope project` (`.claude` under the current directory).

This engine names its sister engines directly in `AGENTS.md`'s mandatory gates — each is an independent, optional install, never a hard dependency. **`digital-research-engine`** is a *mandatory* pre-check for every Kaizen audit, skill edit, and standardisation decision ("Every Kaizen audit... MUST begin with the Digital Research Engine"), and is where current external claims route per this README's own opening. **`chwezi-accounting-doctrine`** is triggered whenever money flows, tax, payroll, grants, or any IFRS/IFRS-for-SMEs content appears in a proposal's financial or commercial sections. **`design-system-skills`** is routed to for every font, layout, colour, and visual-formatting decision on DOCX/PDF/XLSX proposal deliverables, per the engine's own design-trigger block in `AGENTS.md`. `AGENTS.md` also documents named handoffs (not sister-engine installs in the same sense) to the SRS engine once a bid is won and to a website-delivery engine for website-led work.

## Content integrity

This repository contains no client names, client data, or project-specific
work product; client and proposal workspace directories are excluded from
version control by design (see `.gitignore`). Users installing this engine
should still exercise their own due diligence — you can ask Claude Code or
Codex to run a security scan of this engine, its skills, and its reference
files before relying on it in a sensitive environment (for example: "scan
this repository for hardcoded secrets, personal paths, or unexpected
network calls").

## References

- Mustafa, A. et al. *Everything Claude Code* (ECC). GitHub: affaan-m/ECC, 2026. This engine adapts several named ECC skills: `skills/meta/bid-red-team-dual-review/SKILL.md` states its dual-review contract is "adapted from the Santa Method (origin: Ronald Skelton, Founder, RapportScore.ai), read from the ECC skill engine's `skills/santa-method/SKILL.md`"; `skills/meta/submission-proof-and-receipt-discipline/SKILL.md` states it is "distilled from the ECC skill engine's `skills/operator-approval-loop/SKILL.md` — the receipt-and-proof principle only, not its hashing/epoch/claim-token database mechanism"; and `rules/common/core.md` cites "`intent-driven-development` Rule 2 (ECC audit, report 02, §3.2)" for the rule against inferring a tender's evaluation criteria from a past, similar tender.
- Skelton, Ronald (RapportScore.ai) — named as the origin of the Santa Method underlying `skills/meta/bid-red-team-dual-review/SKILL.md`, via the ECC skill engine (year not stated in the source file).

### Books used as concept sources (2026-09-23 Kaizen)

Methods from these books were rewritten as original, task-oriented guidance; no book text, summaries or extractions are stored in the repository. Volatile figures in the books were excluded or replaced by registered current facts.

| Citation | Where it is used |
|---|---|
| Debelak, D. (2006) *Perfect Phrases for Business Proposals and Business Plans*. New York: McGraw-Hill. | `premium-commercial-writing/references/proposal-power-paragraph-method.md` and `proposal-phrase-bank.md`; pipeline 01–10 language sections |
| Marcos, J., Guesalaga, R., Hough, A. and Vincent, R. (c. 2025) *The High-Performing Key Account Manager*. London: Kogan Page. | `key-account-pursuit-and-account-plan` and its references; `premium-pricing-and-value-defense/references/strategic-account-negotiation.md` |
| Hunter, V. L. with Tietyen, D. (1997) *Business to Business Marketing: Creating a Community of Customers*. Lincolnwood, IL: NTC Business Books. | Key-account selection, client grading, Account Cube, value reasons, relationship cycle |
| Kupsh, J. and Graves, P. R. (1993) *How to Create High-Impact Business Presentations*. Lincolnwood, IL: NTC Business Books. | `tender-orals-and-proposal-presentation` and its references |
| Maltz, M., Kennedy, D. S., Brooks, W. T., Oechsli, M., Paul, J. and Yellen, P. (1998) *Zero-Resistance Selling*. New York: Prentice Hall Press. | `sales-discovery-and-objection-handling/references/objection-root-cause-and-closing-language.md` (ethics-filtered) |
| Nelson, J. (2019) *The Seven Figure Agency Roadmap*. Doral, FL: Seven Figure Agency LLC. | `premium-pricing-and-value-defense/references/offer-presentation-and-price-order.md`; marketing-service proposals |
| Plumley, G. (2011) *Website Design and Development: 100 Questions to Ask Before Building a Website*. Indianapolis: Wiley. | `website-design-proposal-strategy/references/website-ownership-care-plans-and-direction-boards.md`; care plans |
| McNeil, P. (2010; 2013) *The Web Designer's Idea Book*, Volumes 2 and 3. Cincinnati: HOW Books. | Paid direction boards and style cost tiers in website proposals |
| Johnson, G., Whittington, R., Scholes, K., Angwin, D. and Regnér, P. (2017) *Exploring Strategy: Text and Cases*, 11th edn. Harlow: Pearson. | `consulting-frameworks/references/strategic-options-evaluation.md` and `strategy-workshops-and-hypothesis-testing.md` |
| Wheelen, T. L., Hunger, J. D., Hoffman, A. N. and Bamford, C. E. (2018) *Concepts in Strategic Management and Business Policy*, 15th edn. Harlow: Pearson. | `business-analysis-tools/references/weighted-strategic-factor-analysis.md`; four criteria for alternatives |
| Lin, L. C. (2013) *Decode and Conquer*, 2nd edn. Bellevue, WA: Impact Interview. | `consulting-frameworks/references/product-reasoning-and-estimation.md`; case-study structure; orals question handling |
| Wiebe, J. (2011) *Copy Hackers: 6 Persuasion Strategies*. Copy Hackers (self-published). | Option-table organisation and price timing |
| Croll, A. and Yoskovitz, B. (2013) *Lean Analytics*. Sebastopol, CA: O'Reilly Media. | Pre-deployment baselines in `05-relevant-experience/references/case-study-and-past-performance-structure.md` |
| Brown, R. (2016) *Build Your Reputation*. Chichester: Capstone/Wiley; Serling, B. (ed.) (2002) *How to Write Million Dollar Ads, Sales Letters and Web Marketing Pieces*. The Internet Marketing Center. | Firm-profile differentiation test and earned stature (`04-firm-profile`); process guarantees (`proposal-phrase-bank.md`, `10-financial-proposal`) |
| Stutts, P. (2021) *The Undefeated Marketing System*. Lioncrest; Landa, R. (2022) *Strategic Creativity*. Routledge; Hennessy, B. (2018) *Influencer*. Citadel Press; Kelley, L. D. and Sheehan, K. B. (c. 2021) *Advertising Management in a Digital Environment*. Routledge. | `premium-client-proposal-strategy/references/marketing-and-digital-services-proposals.md` |

Earlier SaaS, AI-on-SaaS and AI-agent audit notes and the human-English and technical-proposal syntheses formerly held in `book-extractions/` were folded into task references (`saas-commercial-motion-and-close-discipline.md`, `technical-proposal-evidence-bridge.md`, `human-english-editorial-standard.md`) and the folder was removed on 2026-09-23.

## Capability map

| Need | Primary route |
|---|---|
| Proposal and tender response | `skills/pipeline/` |
| Evaluator journey, win themes, and positioning | `skills/strategy-positioning/` |
| Compliance, evidence, and profiles | `skills/profiles-sectors/` |
| Methodology, work plan, M&E, risk, and safeguards | `skills/domain-delivery/` |
| Technical, financial, SaaS, AI, and transformation proposals | Relevant domain routes with finance, research, design, or engineering handoff |
| Review, red-team, rendering, and release | `skills/meta/` (including the `ai-slop-audit` and `skill-safety-audit` quality gates) and the release gates |

## Current engine state

## Prompt-generation capability — 2026-09-17

This release adds evidence-first candidate testing, failure-slice review, and explicit `NOT_ASSESSED` handling for volatile prompt claims.

The engine generates proposal prompts that preserve the solicitation/evaluation
boundary, evidence and compliance matrix, win thesis, deliverables, risks,
assumptions, approval gates, and acceptance checks through the local [domain
prompt contract](docs/ai-prompting/domain-prompt-compilation-contract.md).

As at 23 September 2026, the filesystem contains 115 active `SKILL.md` entrypoints, including the parent router at `skills/SKILL.md`. The catalogue is discovered from the filesystem; references, templates, examples, documentation, and book material are not counted as active skills.

The engine is not a prompt collection. Each `SKILL.md` is an executable routing or production contract with inputs, outputs, evidence, boundaries, degraded mode, decision rules, quality standards, anti-patterns, and references.

## What this engine can produce

- Consulting proposals and full tender responses.
- Public-sector, donor, NGO, development-partner, and private-sector bids.
- PPDA Uganda, World Bank, AfDB, UNDP, and UN-system procurement responses, subject to verification against the controlling solicitation.
- Expressions of Interest and pre-qualification submissions.
- Technical proposals, separate financial proposals, pricing schedules, budgets, and commercial options.
- Executive summaries, cover letters, firm profiles, relevant-experience sections, methodologies, work plans, staffing plans, CV packs, risk registers, and implementation plans.
- Monitoring and evaluation frameworks, results chains, log frames, indicators, reporting plans, learning plans, and sustainability arrangements.
- Change-management, adoption, capacity-building, stakeholder-engagement, safeguards, GESI, data-management, and service-design sections.
- Website, software, SaaS, AI, agentic-product, digital-transformation, retail, finance, accounting, and operational transformation proposals.
- Proposal audits, evaluator simulations, compliance matrices, evidence registers, red-team findings, and improvement plans.

## Core operating principles

### Evidence before persuasion

Every load-bearing claim should be connected to evidence, an evidence owner, a source date, a warrant, an assumption, or an explicit limitation. Persuasive language cannot substitute for mandatory forms, verified credentials, realistic staffing, a feasible work plan, or a defensible price basis.

### Evaluator journey

The proposal should help an evaluator move through a deliberate decision path:

1. Understand the assignment and the buyer's decision context.
2. See that the proposer has correctly understood the problem.
3. Recognise the proposed response, its fit, and its differentiators.
4. Find evidence of capability, relevant experience, and delivery realism.
5. See how work, people, risks, outputs, outcomes, and measures connect.
6. Confirm compliance, value for money, safeguards, and manageable dependencies.
7. Reach a confident, supportable recommendation.

The narrative skill at `skills/strategy-positioning/proposal-storytelling-and-evaluator-journey/SKILL.md` turns this journey into a proposal spine. The compliance matrix and evidence register remain authoritative over the narrative.

### Kaizen is mandatory

For a ready-to-run product or project operation, use [`prompts/full-kaizen-operation.md`](prompts/full-kaizen-operation.md).

Every engine use and every proposal product follows the Kaizen cycle:

`Observe -> Baseline -> Select -> Experiment -> Check -> Standardise -> Teach -> Re-measure`

The proposal-specific contract is `skills/meta/kaizen-improvement-system/SKILL.md`. It applies to the engine itself and to every bid, tender, EOI, methodology, technical proposal, financial proposal, evidence pack, and consulting artefact it produces.

Audits are deliberately hard-capped:

```text
published audit score = min(raw audit score, 65)
```

The cap is a reporting ceiling, not a waiver. Every improvement plan must target 95/100 and must identify the gap, root cause, action, owner, measure, acceptance evidence, risk, rollback, and re-audit date.

## Proposal production workflow

1. **Define the deliverable.** Identify whether the request is a full bid, EOI, proposal section, financial submission, evidence pack, audit, or revision.
2. **Load proposer identity.** Read `skills/profiles-sectors/profiles/SKILL.md` and load exactly one approved proposer profile before drafting text.
3. **Route procurement and sector context.** Read `skills/profiles-sectors/sectors/SKILL.md`, identify the controlling framework, and load the smallest relevant framework and sector skills.
4. **Research what can change.** Route current laws, procurement rules, market facts, standards, country data, technology claims, and other externally verifiable material to the <a href="https://github.com/peterbamuhigire/digital-research-skills" target="_blank" rel="noopener noreferrer">Digital Research Engine</a>.
5. **Extract the evaluator contract.** Convert the ToR or RFP into requirements, evaluation criteria, mandatory forms, evidence requests, deadlines, assumptions, clarifications, and submission constraints.
6. **Build the compliance and evidence spine.** Map every requirement to a response location, evidence source, owner, status, and verification date. An unassessed requirement is never a pass.
7. **Design the evaluator journey.** Establish the problem, consequence, response, proof, delivery logic, risk treatment, value, and decision path before writing sections.
8. **Draft the proposal sections.** Use the numbered pipeline skills and only the relevant domain and strategy skills.
9. **Build a learning-oriented methodology.** Use PDCA and QC Story: define the problem, establish the baseline, analyse causes, test countermeasures, check results, standardise what works, and specify how learning will be transferred.
10. **Connect M&E to delivery.** State the result, indicator, baseline, target, data source, frequency, responsibility, verification method, decision use, and learning response.
11. **Reconcile the commercial package.** Align scope, deliverables, effort, staffing, schedule, assumptions, exclusions, risks, support, payment terms, and price. Keep technical and financial envelopes separate when required.
12. **Run quality gates.** Apply critical business-logic review, anti-slop review, AI-slop audit, compliance review, evidence review, document/render review, and the appropriate specialist-engine gates.
13. **Simulate the evaluator.** Test whether a reviewer can find the mandatory response, proof, methodology, price logic, risk treatment, and decision rationale.
14. **Release or recover.** Stop if a mandatory input, evidence item, authority, or controlling rule remains unresolved. Narrow the claim, request the source, record the gap, or return the last safe version.
15. **Capture the learning.** Record findings, standardise successful improvements, update the relevant skill or reference, and schedule re-measurement.

## Detailed capability routes

### Proposal pipeline

| Skill | Main use |
|---|---|
| `skills/pipeline/01-cover-letter/` | Client-specific opening, proposition, relevant proof, and authorised signatory closing |
| `skills/pipeline/02-executive-summary/` | Problem, response, differentiators, scope, timeline, value, and decision case |
| `skills/pipeline/03-understanding-of-assignment/` | Background, objectives, scope interpretation, constraints, and ToR understanding |
| `skills/pipeline/04-firm-profile/` | Legal identity, service areas, capability, footprint, and certifications |
| `skills/pipeline/05-relevant-experience/` | Evidence-led project cards, roles, outcomes, references, and relevance |
| `skills/pipeline/06-methodology/` | Approach, phases, deliverables, governance, QA, risks, learning, and acceptance |
| `skills/pipeline/07-team-composition/` | Organogram, role-responsibility matrix, CVs, availability, and team narrative |
| `skills/pipeline/08-work-plan/` | Activities, dependencies, milestones, effort, staffing, buffers, and realistic timing |
| `skills/pipeline/09-expression-of-interest/` | Concise pre-qualification and EOI responses |
| `skills/pipeline/10-financial-proposal/` | Fees, reimbursables, payment schedule, assumptions, and commercial separation |

### Procurement, profiles, and sectors

- `skills/profiles-sectors/profiles/` controls proposer identity, voice, signatory, credentials, experience, and branding. Load exactly one primary profile before drafting.
- `skills/profiles-sectors/sectors/` routes procurement framework and industry context. Current framework coverage includes PPDA Uganda, World Bank, AfDB, and UNDP, with sector routes for agriculture, education, energy, financial services, governance, health, ICT, manufacturing, transport, and water/sanitation.
- Sector and country material provides framing and decision context; it does not replace verification of the controlling solicitation or current external sources.

### Delivery and consulting domains

The `skills/domain-delivery/` family covers project management, change management, M&E, stakeholder engagement, capacity building, GESI, environmental and social safeguards, data management, risk management, sustainability, business analysis, consulting frameworks, finance/accounting advisory, retail transformation, GIZ/EU local procurement, and EAC e-commerce BDS programme design.

The delivery skills are designed to make the proposal implementable, not merely attractive. They connect outputs to roles, dependencies, risks, acceptance, indicators, reporting, ownership transfer, and post-award transition.

### Strategy and positioning

The `skills/strategy-positioning/` family covers:

- Critical analysis, business logic, feasibility, achievability, and evaluator reasoning.
- Proposal storytelling and evaluator journey.
- Premium client positioning and value defence.
- Sales discovery, objection root causes, closing language and win-loss debriefs.
- Key-account pursuit, GRASP stakeholder mapping, account plans, executive sponsorship and strategic-account negotiation.
- Tender orals, shortlist interviews and proposal walk-throughs.
- Marketing, digital-marketing and advertising service proposals, with handoffs to the business-plan and social-media engines.
- Service design, customer journeys, blueprints, co-creation, and implementation.
- Website design and development proposals.
- AI transformation and responsible-AI proposals.
- Embedded accounting-engine proposals.
- Customer service, maintenance, SLAs, escalation, and post-launch optimisation.

### SaaS, AI-on-SaaS, agents, and commercial packaging

The engine contains dedicated proposal families for:

- SaaS discovery, business case, ROI, pricing, implementation, POC, procurement, security, customer success, mutual action planning, vertical positioning, objections, lifecycle communications, trust and compliance, multi-tenant architecture, and pilot-to-rollout change management.
- AI-on-SaaS three-plane methodology, AI qualification, value and cost stacks, POC evaluation, model selection, hallucination limits, risk, responsible AI, compliance, procurement, change management, team composition, and vertical positioning.
- Agent discovery, autonomy levels, business case, pricing, POC staging, kill-switches, risk, procurement, change management, team composition, and vertical positioning.
- Agent SLA classes, commercial packaging, contract language, intervention credits, abort/refund mechanics, outcome pricing, MSA/SLA addenda, commercial objections, renewals, and true-ups.

These skills require explicit boundaries around autonomy, human authority, evaluation, reversibility, intervention, model-provider dependencies, data handling, and operational responsibility.

For healthcare and health-financing proposals, use the evidence-pack references in
`skills/profiles-sectors/references/`: [health IT integration and tenant evidence](skills/profiles-sectors/references/health-it-integration-and-tenant-evidence.md), [governance and budget decision pack](skills/profiles-sectors/references/healthcare-governance-budget-decision-pack.md), and [HR safety, conduct and metric evidence](skills/profiles-sectors/references/healthcare-hr-safety-and-metric-evidence.md). They define procurement questions, evidence fields, negative cases, reviewer roles, and `NOT_ASSESSED` handling; they do not certify a vendor, budget, workforce case, or clinical control.

### Writing and quality controls

- `skills/language/east-african-english/` and `skills/language/language-standards/` maintain British English and appropriate professional tone.
- `skills/meta/anti-ai-slop/` is a real-time guardrail while drafting.
- `skills/meta/ai-slop-audit/` audits each section or major iteration and blocks release on grade F.
- `skills/meta/critical-analysis-business-logic/` is the high-stakes reasoning gate.
- `skills/meta/skill-writing/` and `skills/meta/skill-safety-audit/` maintain the engine.
- `skills/meta/kaizen-improvement-system/` governs engine and product improvement.

## Book-informed improvements

The engine has been strengthened using independently synthesised, copyright-safe insights from the 16-book study. Raw books, OCR, chapter reconstructions, and long extracts do not belong in this repository.

| Book cluster | Proposal-engine improvements |
|---|---|
| Agile Processes in Software Engineering and XP 2026 | Evidence-led Agile claims, experiment design, retrospectives, AI adoption, UX pilots, decision rights, leadership, and measurable process learning |
| Platform Enterprise | Platform-as-product positioning, consumer feedback, cognitive-load reduction, sociotechnical ownership, maintenance, technical debt, and sustainable operating models |
| Designing for AI | Problem-first AI selection, separation of user/system/model/input/output concerns, human control, correction, transparency, drift, and rollback language |
| Leveling Up as a Tech Lead | Role clarity, ownership transfer, trust, transparent communication, stakeholder relationships, and implement-reflect-adjust learning loops |
| Digital Storytelling and Video Game Storytelling | Evaluator journey, narrative spine, audience fit, conflict and stakes, modular structure, proof-led case stories, and cross-disciplinary clarity |
| AI for Game Developers | Careful treatment of algorithmic claims, testable behaviour, deterministic fallbacks, telemetry, and warnings about historical APIs and practices |
| Lean: Ultimate Collection | Build-Measure-Learn, validated learning, innovation accounting, waste reduction, flow, experiments, metrics, and decision gates |
| Kaizen and the Art of Creative Thinking; Applying Kaizen in Africa | PDCA, participatory improvement, low-cost experiments, 5S, muda, QC Story, root-cause analysis, standard work, management commitment, and learning transfer |
| The Nonprofit Guide to Strategic Planning | Mission and stakeholder alignment, readiness, baseline, external scan, option trade-offs, implementation governance, KPI refresh, and quarterly/annual learning cycles |
| Facility Move Playbook | Charter, decision rights, baseline, readiness, continuity, risk, transition, cutover, stabilisation, closeout, and lessons learned |
| Paid for Your Perspective | Expert positioning, buyer needs, compliance screening, preparation, call records, boundaries of expertise, follow-up, and durable knowledge products |
| MSC Software Magazine | Model lineage, assumptions, simulation-to-test correlation, independent verification, engineering evidence, sustainability, and proof of delivery claims |
| Anatomy for Artists and Dynamic Characters | Visual storytelling, composition, gesture, readability, and design-system handoff for proposal documents and presentation assets; extracted anatomy content remains quarantined where unreadable |

These sources improve proposal reasoning and delivery framing; they do not author client-specific facts, legal claims, procurement thresholds, prices, or technical commitments. Current claims must still be researched and verified.

## September 2026 book-driven Kaizen wave

See [`docs/continuous-improvement/book-driven-kaizen-2026-09-01.md`](docs/continuous-improvement/book-driven-kaizen-2026-09-01.md) for the new civil-society cyber-resilience route and health/AI proposal references.

## Phase 1 Kaizen evidence contracts - 19 September 2026

The bounded health slice adds three proposal-owned evidence references and a
synthetic validator for normal and failure paths. The validator covers wrong-
tenant read/write, duplicate and interrupted integration cases; authority and
source requirements for governance decisions; material budget basis, period and
reviewer checks; conduct-case closure; safety-critical competency; and
second-reviewer metric reproduction. The fixture is explicitly fictional. B08-A03
remains deferred because denial/compliance review is not a proposal-owned route;
the canonical implementation surface is assigned to SRS and finance engines.
See [`docs/continuous-improvement/kaizen-phase-1-proposal-2026-09-19.md`](docs/continuous-improvement/kaizen-phase-1-proposal-2026-09-19.md).

## Compliance screening and proposal audits

Before release, the engine should be able to answer:

- Which solicitation, ToR, framework, sector, country, and deadline govern the response?
- Which mandatory forms, declarations, certificates, page limits, file formats, envelopes, and submission rules apply?
- Who is the authorised proposer and signatory?
- Which credentials, past-performance claims, staff qualifications, references, and financial statements are supported by evidence?
- Which requirements are addressed, where are they addressed, and who owns any gap?
- Do methodology, staffing, work plan, M&E, risk, assumptions, exclusions, support, and price describe the same delivery model?
- Are current technology, legal, policy, market, financial, and standards claims sourced and dated?
- Are technical and financial proposals separated where required?
- Has the proposal passed anti-slop, critical-reasoning, evidence, evaluator, document, and rendering gates?

The engine/product audit must cover at least:

1. Compliance and responsiveness.
2. Evaluator journey and findability.
3. Evidence quality and provenance.
4. Methodology and feasibility.
5. Staffing, governance, and decision rights.
6. M&E, learning, and sustainability.
7. Risk, safeguards, ethics, and responsible AI where relevant.
8. Budget, commercial assumptions, and envelope separation.
9. Document fidelity, accessibility, readability, and presentation quality.
10. Submission readiness, approvals, and rollback/recovery.

The audit produces a capped score, gap register, root-cause analysis, 95/100 improvement plan, experiment result, standardisation record, and re-audit date. Proposal audits are read-only by default. Editing, certification, submission, publishing, external communication, spending, and contractual commitment require explicit authority.

## Cross-engine routing

This repository remains the proposal-content and proposal-structure source of truth. It references sibling engines rather than copying them.

| Need | Route |
|---|---|
| Current web research, source verification, OSINT, due diligence, policy, law, market, standards, or literature review | <a href="https://github.com/peterbamuhigire/digital-research-skills" target="_blank" rel="noopener noreferrer">Digital Research Engine</a> |
| Accounting, IFRS/IAS, tax, controls, reconciliation, audit, budgets, financial statements, or finance-system doctrine | <a href="https://github.com/peterbamuhigire/chwezi-accounting-doctrine" target="_blank" rel="noopener noreferrer">Chwezi Accounting Doctrine</a> |
| Software, APIs, databases, cloud, security, AI implementation, DevOps, or production engineering | <a href="https://github.com/peterbamuhigire/chwezi-dev-engine" target="_blank" rel="noopener noreferrer">Chwezi Development Engine</a> |
| Formal requirements, architecture, testing, deployment, governance, SDLC, or standards-driven documentation | <a href="https://github.com/peterbamuhigire/srs-skills" target="_blank" rel="noopener noreferrer">SRS Skills</a> |
| Premium website strategy, website delivery, SEO, conversion, launch, and website quality gates | <a href="https://github.com/peterbamuhigire/website-skills" target="_blank" rel="noopener noreferrer">Website Skills</a> |
| Typography, visual design, UI/UX, presentation layout, document appearance, and anti-visual-slop review | <a href="https://github.com/peterbamuhigire/design-system-skills" target="_blank" rel="noopener noreferrer">Design System Skills</a> |
| Social campaigns, content calendars, community management, and marketing reporting | <a href="https://github.com/peterbamuhigire/social-media-skills" target="_blank" rel="noopener noreferrer">Social Media Skills</a> |
| Linux operations, infrastructure, Bash, hardening, services, and server runbooks | <a href="https://github.com/peterbamuhigire/linux-skills" target="_blank" rel="noopener noreferrer">Linux Skills</a> |
| Business plans, feasibility, market sizing, financial projections, bankability, or investor readiness | <a href="https://github.com/peterbamuhigire/business-plan-skills" target="_blank" rel="noopener noreferrer">Business Plan Skills</a> |

Resolve the canonical path from the current global routing instructions where a device-specific path differs. Use the smallest relevant stack and preserve each engine's source of truth.

## Source limitations and evidence discipline

- The proposal engine does not store raw book content or OCR. Book-derived material is independent synthesis only.
- The Shigeo Shingo extraction was unusable and is not treated as a source for detailed claims.
- The Anatomy for Artists extraction was unreadable and is quarantined; no anatomy-specific claims are invented from it.
- Platform Enterprise, Designing for AI, and Leveling Up as a Tech Lead were early-release/partial extracts. Their incomplete coverage is recorded, and current technology or legal claims require independent verification.
- AI for Game Developers and MSC Software Magazine are historical sources. Timeless principles may inform framing, but product APIs, tooling, standards, market facts, and implementation claims must be checked against current sources.
- Applying the Kaizen in Africa and the other readable books inform process patterns, not client-specific evidence.
- When a source, reviewer, render tool, network, or mandatory input is unavailable, mark the affected item `not assessed`, narrow the claim, identify the evidence owner, and never represent an unassessed requirement as passed.

## Repository structure

```text
proposal-skills/
|-- AGENTS.md
|-- CLAUDE.md
|-- README.md
|-- CONTRIBUTING.md
|-- quality-baseline.json
|-- scripts/
|-- docs/
|   |-- continuous-improvement/
|   |-- engine-upgrade-july-2026/
|   |-- skill-authoring-standard.md
|   `-- dual-compatibility-report.md
`-- skills/
    |-- SKILL.md              # parent router
    |-- pipeline/
    |-- profiles-sectors/
    |-- domain-delivery/
    |-- strategy-positioning/
    |-- saas-proposals/
    |-- ai-on-saas-proposals/
    |-- ai-agent-proposals/
    |-- ai-agent-commercial/
    |-- writing-content/
    |-- language/
    `-- meta/
```

Proposal workspaces are created under a gitignored `proposals/` directory. A typical proposal contains `INDEX.md`, `BRIEF.md`, numbered section files, `terms/`, `sheets/`, `team/`, `research/`, and `output/`.

## Validation and release checks

Run from the repository root before accepting engine changes:

```powershell
python -X utf8 scripts\validate_skills.py --baseline quality-baseline.json
python -X utf8 scripts\routing_smoke_test.py
python -X utf8 scripts\source_ingestion_guardrail.py
python -X utf8 scripts\encoding_link_gate.py
git diff --check
```

For changed skills, also run the canonical scanner and quick validator for each changed skill directory, the skill-safety audit, the anti-slop audit, and document/render checks when the deliverable has layout or office-file requirements. A grade F from the AI-slop audit blocks release.

The baseline must remain at zero findings. Existing baseline counts are not permission to introduce new debt. Do not bypass source-ingestion checks by renaming, compressing, splitting, or moving raw source material.

## Getting started

```powershell
git clone <repository-url> proposal-skills
cd proposal-skills
claude
```

Then provide the ToR/RFP/brief, identify the proposer, and state the required deliverable. The agent should start with `skills/SKILL.md`, then load the profile, procurement/sector router, relevant section skill, and the smallest supporting skill stack.

## Adding or improving a skill

1. Read `AGENTS.md`, `docs/skill-authoring-standard.md`, and `skills/meta/skill-writing/SKILL.md`.
2. Define the use case, neighbouring positive and negative triggers, inputs, outputs, evidence, boundaries, degraded mode, decisions, quality standards, anti-patterns, and references.
3. Apply the Kaizen improvement system: baseline the gap, run a bounded experiment, check evidence, standardise the improvement, and schedule re-measurement.
4. Keep frontmatter limited to `name`, `description`, and portable metadata.
5. Keep the exact acknowledgement immediately below the first top-level heading in every active `SKILL.md`.
6. Do not duplicate sibling-engine doctrine or store raw books, OCR, book extractions or book summaries anywhere in the repository.
7. Run the validators, routing smoke test, source-ingestion guardrail, safety and anti-slop gates, and relevant document/render checks.
8. Update the appropriate improvement record and this README when the public capability or routing model changes.

## Authority and safety boundaries

Review, research, audit, critique, routing, and planning are read-only by default. The engine must not invent credentials, certify compliance without evidence, submit a bid, accept contractual terms, publish externally, disclose confidential information, spend money, or change source records without explicit authority. When specialist engineering, finance, research, design, website, Linux, business-plan, or formal SDLC work is required, route it to the canonical sibling engine rather than recreating its doctrine here.

## September 2026 Kaizen execution update

The bounded first wave adds a synthetic commercial fixture and
`scripts/validate_p0_commercial_fixture.py`. It checks requirement-to-file
mapping, deliverable acceptance, staffing effort, timeline, price coherence,
late-envelope handling and approval-state boundaries. The full focused suite
passes 23 tests. A fixture approval is not a signatory decision, and no bid has
been submitted or accepted. The next step is independent reconciliation of one
response fragment before rendering a complete package or starting the
conditional AI/SaaS pilot.

## September 2026 book-integration Kaizen (2026-09-23)

- Added the proposal phrase bank and power-paragraph method as the engine's human-professional language standard, wired into pipeline 01–10, premium commercial writing, language skills and the anti-slop gates.
- Added `key-account-pursuit-and-account-plan` and `tender-orals-and-proposal-presentation` (115 skills; 25 routing fixtures).
- Added references for strategic-account negotiation, offer presentation and retainer design, marketing-service proposals with cross-engine handoffs, website ownership and care plans, objection root causes and win-loss debriefs, strategic options evaluation, strategy workshops, product reasoning and estimation, weighted strategic-factor analysis, and case-study structure.
- Removed the `book-extractions/` folder with a zero-loss capability map; the source-ingestion guardrail now rejects any `book-extractions/` path. Record: [`docs/continuous-improvement/kaizen-book-integration-2026-09-23.md`](docs/continuous-improvement/kaizen-book-integration-2026-09-23.md).
