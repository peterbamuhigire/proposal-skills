# Proposal Skills

Proposal Skills is a dual-compatible Claude Code and Codex skill engine for producing, reviewing, improving, and governing consulting proposals and procurement responses. It supports bids, tenders, Expressions of Interest (EOIs), donor responses, technical and financial proposals, methodologies, implementation plans, monitoring and evaluation plans, change-management plans, and proposal evidence packs.

The engine is designed for East and Central African consulting work and uses British English, an East African professional tone, evaluator-facing reasoning, evidence discipline, and explicit compliance controls.

## Current engine state

As at 4 August 2026, the filesystem contains 108 active `SKILL.md` entrypoints, including the parent router at `skills/SKILL.md`. The catalogue is discovered from the filesystem; references, templates, examples, documentation, and book material are not counted as active skills.

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
4. **Research what can change.** Route current laws, procurement rules, market facts, standards, country data, technology claims, and other externally verifiable material to `digital-research-skills`.
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

## Capability map

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
- Sales discovery and objection handling.
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
| Current web research, source verification, OSINT, due diligence, policy, law, market, standards, or literature review | `C:\wamp64\www\digital-research-skills` |
| Accounting, IFRS/IAS, tax, controls, reconciliation, audit, budgets, financial statements, or finance-system doctrine | `C:\Users\Peter\source\repos\chwezi-accounting-doctrine` |
| Software, APIs, databases, cloud, security, AI implementation, DevOps, or production engineering | `C:\wamp64\www\skills-web-dev` |
| Formal requirements, architecture, testing, deployment, governance, SDLC, or standards-driven documentation | `C:\wamp64\www\srs-skills` |
| Premium website strategy, website delivery, SEO, conversion, launch, and website quality gates | `C:\wamp64\www\website-skills` |
| Typography, visual design, UI/UX, presentation layout, document appearance, and anti-visual-slop review | `C:\wamp64\www\design-system-skills` |
| Social campaigns, content calendars, community management, and marketing reporting | `C:\Users\Peter\source\repos\social-media-skills` |
| Linux operations, infrastructure, Bash, hardening, services, and server runbooks | `C:\wamp64\www\linux-skills` |
| Business plans, feasibility, market sizing, financial projections, bankability, or investor readiness | `C:\Users\Peter\source\repos\business-plan-skills` |

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
|-- book-extractions/        # legacy source records; never add raw books or OCR
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
6. Do not duplicate sibling-engine doctrine or store raw books/OCR.
7. Run the validators, routing smoke test, source-ingestion guardrail, safety and anti-slop gates, and relevant document/render checks.
8. Update the appropriate improvement record and this README when the public capability or routing model changes.

## Authority and safety boundaries

Review, research, audit, critique, routing, and planning are read-only by default. The engine must not invent credentials, certify compliance without evidence, submit a bid, accept contractual terms, publish externally, disclose confidential information, spend money, or change source records without explicit authority. When specialist engineering, finance, research, design, website, Linux, business-plan, or formal SDLC work is required, route it to the canonical sibling engine rather than recreating its doctrine here.
