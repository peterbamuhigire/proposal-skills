# Proposal Full Kaizen Operation Prompt

Paste this prompt at the root of a bid, tender, EOI, methodology, technical/financial proposal, or consulting-deliverable project.

## Configuration

```text
Opportunity/client and submission type: [DISCOVER]
RFP/ToR and addenda locations: [DISCOVER]
Deadline, timezone, portal, and envelope rules: [DISCOVER]
Evaluation criteria and mandatory requirements: [DISCOVER]
Consortium, team, evidence, and pricing locations: [DISCOVER]
Known evaluator feedback or compliance concerns: [NONE OR LIST]
Cycle ID: [YYYY-MM-DD-short-name]
Improvement authority: draft-local reversible edits are authorised; submission is not
```

## Prompt

Run a full evaluator-facing Kaizen operation on this proposal product. Treat compliance and proof as constraints, not copywriting suggestions. Freeze a capped baseline, fix root causes through controlled revisions and red-team tests, validate the complete submission package, and retain a reproducible evidence trail.

### Route and authority

Read project instructions. Resolve Proposal Skills and read its `AGENTS.md`, `skills/SKILL.md`, the primary proposal router, the matched proposal/product skills, and `skills/meta/kaizen-improvement-system/SKILL.md`. Read the Digital Research portfolio standard and verify current procurement, client, legal, sector, technical, and market claims. Route financial logic to Chwezi and Business Plan Skills; route document rendering and visual hierarchy to the document and Design System engines.

This prompt authorises reversible edits to the current draft and its local evidence artefacts. It does not authorise portal access, submission, client communication, signatures, declarations, pricing approval, partner commitments, or canonical engine changes. Stop if the controlling RFP/ToR, addenda, deadline/timezone, mandatory forms, envelope rules, authority, or rollback copy is missing. Mark missing evidence or review `NOT ASSESSED` and withhold submission readiness.

### Evidence pack and inventory

Create `docs/kaizen/<cycle-id>/` with `00-scope-and-evidence.md`, `01-baseline-scorecard.md`, `02-improvement-backlog.md`, `03-experiment-log.md`, `04-validation-record.md`, `05-final-report.md`, and `06-next-cycle.md`. Inventory every controlling document, addendum, instruction, criterion, form, declaration, page/word limit, file rule, deadline, portal step, technical/financial separation rule, deliverable, team requirement, evidence item, assumption, dependency, approval, and prior evaluator comment. Build or repair a requirement-to-section-to-evidence compliance matrix before scoring.

### Capped baseline

Score ten equal dimensions with concrete evidence and status:

1. Opportunity decision, bid/no-bid logic, eligibility, instructions, addenda, and scope.
2. Mandatory compliance matrix, forms, declarations, limits, envelopes, and submission mechanics.
3. Evaluator journey, criterion mapping, answer-first structure, and navigation.
4. Claim quality, organisational evidence, references, past performance, and source provenance.
5. Understanding of need, context, differentiators, outcomes, and client-specific value.
6. Methodology, activities, deliverables, quality control, assumptions, and feasibility.
7. Workplan, staffing, roles, availability, governance, partners, and mobilisation.
8. Risks, safeguarding/ethics, M&E, indicators, reporting, sustainability, and handover.
9. Budget/commercial coherence, pricing support, value for money, and technical-financial separation.
10. Writing quality, visual/document fidelity, accessibility, final packaging, approvals, and submission readiness.

Calculate raw overall and publish `min(raw_overall, 65)`. Freeze it. A missed mandatory requirement, unsupported eligibility/capability claim, unresolved conflict, unsigned form, envelope breach, or deadline risk is a blocker independent of score.

### Improve toward 95

Create a P0/P1/P2 backlog. Each action names criterion/requirement, evidence, root cause, exact section/file, hypothesis, owner, evaluator-facing measure, guardrails, reversible revision, rollback, stop rule, acceptance proof, target contribution, and re-audit date. Fix compliance and proof before polish. Never inflate credentials, invent evidence, or paste a generic methodology.

Run one bounded revision at a time, preserving the prior version and a change log. Use blind evaluator scoring, compliance red-team, evidence spot checks, cross-section consistency checks, and packaging rehearsals. Test whether a fresh reviewer can find and score the answer quickly. Reject revisions that sound stronger but reduce accuracy, feasibility, compliance, or trust.

### Strict anti-AI-slop gate

Apply proposal anti-slop rules while drafting and audit after every major section/iteration and at final release. Grade F blocks release. Reject invented credentials, projects, staff availability, references, client facts, certifications, partners, results, prices, sources, or compliance; generic methodology pasted from another bid; ToR mirroring without a delivery model; buzzword chains; repetitive benefit claims; unowned workplans; decorative risk tables; vague M&E; implausible mobilisation; uniform AI cadence; and polished filler that does not earn evaluator points.

Every paragraph must map to a requirement, evaluator concern, proof item, delivery decision, risk, or transition. Every capability claim must link to evidence; every activity must connect to output, owner, timing, quality control, dependency, measure, and budget where applicable. Do not hide gaps with persuasive language. A visually polished submission remains blocked when compliance, proof, feasibility, or authority is synthetic.

### Validate the complete package

Run applicable source-ingestion, anti-slop, critical-logic, compliance, pricing/model, document render, accessibility, file/package, virus/security, and release gates. Reconcile scope, method, workplan, staffing, CVs, deliverables, M&E, risks, assumptions, budget, and forms. Inspect native DOCX/PDF/XLSX/PPTX outputs page by page where relevant. Rehearse filenames, limits, envelope separation, upload order, deadline/timezone, signatures, and approvals without submitting.

Record exact commands, reviewer scores, requirement coverage, failures, render locations, and unavailable checks. Standardise successful learning in the project compliance matrix, evidence register, template, checklist, fixture, or review record. Re-score using new evidence; do not claim 95 or submission readiness unless proved.

Write the final report with baseline/final scores, changes, evaluator impact, red-team results, unresolved blockers, submission verdict, and next review. Return the evidence-pack path and links. Do not submit or communicate externally.
