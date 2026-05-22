# SaaS Sales Method for Account Executives — Proposal Extraction (2026)

Internal synthesis for the proposal-skills engine. Source: Winning by Design, *The SaaS Sales Method for Account Executives: How to Win Customers* (2018, Revision 5.0). Use as audit trail and implementation source for the proposal-skills repository, not for redistribution.

## Source Awareness

The book frames the SaaS account executive's closing motion as an eight-stage relationship process: Identify, Diagnose, Prescribe, Select, Propose, Pause/Go Dark, Trade, and Commit. It is rooted in customer-impact thinking rather than feature selling. The book contains exercises, account-mapping diagrams, a "Crazy Ivan" closing pattern, and disciplined objection-handling sequences.

## Copyright Boundary

- No book text, distinctive diagrams, named exercises, or long paraphrases are reproduced in skills, references, proposals, or public-facing material.
- Distill principles into original, execution-oriented proposal guidance.
- Keep the repository useful without the source book.

## Proposal-Relevant Synthesis

### Stage 1: Identify — Ideal Customer Profile and Critical Event
Translate to proposal: every SaaS implementation proposal must declare the Ideal Customer Profile that the proposed approach is tuned for, and the Critical Event in the client's business that justifies acting now. In proposal language: a paragraph in the executive summary and understanding-of-assignment section that names the trigger (regulatory deadline, system end-of-life, M&A integration, growth ceiling, audit finding, customer-experience failure) and the cost of inaction.

### Stage 2: Diagnose — Pain Chain, Impact, Decision Process
The Diagnose stage drives most of what becomes a proposal's value case. Three components are load-bearing:

- **Pain chain**: connect surface-level symptom (slow report) to operational pain (analyst overtime, missed quarter-close), to financial pain (compliance penalty, working-capital cost), to strategic pain (loss of investor confidence). Proposals must articulate at least three links of the chain, not just the surface complaint.
- **Impact quantification**: per role, name the metric that improves, the baseline, the target, and the dollar/time/risk equivalent. Without an impact figure per role, the price is undefended.
- **Decision process**: distinguish *consensus* decisions (multiple veto holders, IT, Finance, Security each block independently) from *hierarchy* decisions (a single executive owns the call). The proposal's evaluator journey, win plan, and pricing options must be designed against the actual decision shape — including the "3x3" orchestration model where three roles on the vendor side cover three counterpart roles on the buyer side.

### Stage 3: Prescribe — Story, Demo, Provocation, Objections
A proposal earns the right to prescribe only after it shows it has diagnosed. The prescription block should include: a relevant customer story (named comparable engagement, baseline, intervention, measurable outcome), a demo or POC plan tied to the diagnosed pain, a provocation that surfaces unconsidered risk (the "what you are not measuring" angle), and an objection map prepared in advance.

### Stage 4: Select — Decision Criteria, Impact Prioritisation, Competitive Strategy
The proposal should help the evaluator build their own decision matrix. List candidate decision criteria, weight them against impact (not feature parity), and address competitive positioning by category (incumbent renewal, point solution, build-in-house, do-nothing) rather than vendor-by-vendor.

### Stage 5: Propose — Quote, Impact Proposal, Business Case
The Winning by Design framing separates three artefacts:
- **Quote**: line-item pricing for procurement.
- **Impact proposal**: client-language summary of value, paid back, and risk reduced.
- **Business case**: NPV, payback, ROI uplift, sensitivity, and break-even — the document Finance defends internally.
For the engine, each premium SaaS proposal should produce all three layers, not a single price sheet.

### Stage 6: Pause / Go Dark — Disciplined Silence
When the buyer goes dark, do not chase. The proposal's follow-up plan should include an alert layer (trigger-based outreach: news, hiring signals, regulatory events), a continued-education sequence (insight emails, not chase emails), and a defined re-engagement protocol with the executive sponsor.

### Stage 7: Trade — Negotiation, Price Objections, Crazy Ivan, Accelerated Close
Discipline: never give without getting. Every concession must be paired with a trade — scope, term length, payment terms, references, case-study rights, expanded user count, or earlier start. The "Crazy Ivan" pattern (unexpected pivot that resets stalled negotiation) and the accelerated close (time-bound mutual incentive) are useful patterns to surface in the close-plan deliverable inside the proposal.

### Stage 8: Commit — Mutual Action Plan and Signing
The commit stage produces a Mutual Action Plan (MAP): named tasks, owners, dates, decision gates, and the path to signature. For SaaS implementation proposals this becomes the joint plan from contract signature through go-live, with explicit client obligations.

### Stage 9: Not-a-Fit Discipline
A premium proposal explicitly states the conditions under which the engagement should *not* proceed. This builds executive credibility and removes the "we will say yes to anything" anti-pattern.

## Repository Changes Driven

- New skill: `skills/saas-proposals/saas-discovery-and-qualification/` — diagnose, impact, decision-process mapping, pain chain.
- New skill: `skills/saas-proposals/saas-mutual-action-planning-and-close-plans/` — MAP, close plan, commit logic.
- New skill: `skills/saas-proposals/saas-objection-handling-and-competitive-displacement/` — competitive strategy, price objections, trade discipline.
- New reference: `saas-discovery-question-bank.md` — pain chain, impact, decision process.
- New reference: `meddic-and-command-of-message-for-saas.md` — qualification overlay.
- New reference: `saas-mutual-action-plan-template.md`.
- New reference: `saas-business-case-and-roi-template.md`.
- New reference: `saas-objection-handling-playbook.md`.
- Enhancement: `skills/strategy-positioning/sales-discovery-and-objection-handling/SKILL.md` adds SaaS lens.
- Enhancement: `skills/pipeline/02-executive-summary/` and `skills/pipeline/03-understanding-of-assignment/` get pain-chain and critical-event guidance.

## Quality Guardrails

- Never copy the book's named diagrams, sentiment icons, or distinctive exercises.
- Convert account-mapping logic into proposal-grade sponsor/champion/blocker tables in the engine's own language.
- Pain-chain examples in skills must be original, drawn from East African and global SaaS contexts the engine already covers.
