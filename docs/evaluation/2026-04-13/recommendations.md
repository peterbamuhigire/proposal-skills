# Recommendations

## Current Priority View

After the 13 April remediation pass, the repository no longer most urgently needs more generic domain content.

The highest-value next moves are:

1. stronger brief-driven orchestration
2. evaluator and score alignment
3. cross-section control and evidence reuse
4. adversarial review and packaging before submission

## Completed In This Round

These items were materially improved today and should move down the queue:

- business analysis governance and requirements structure
- project controls and work-plan control logic
- financial modelling rigour inside the pricing workflow

## Highest-Priority Skill-Level Improvements

### 1. Strengthen Root `SKILL.md` Into A True Orchestrator

Add a mandatory workflow between intake and section drafting:

- bid / no-bid decision
- procurement and sector routing
- brief generation
- win-theme selection
- score-map creation
- storyboard / ghost-pack generation
- section drafting
- red-team review
- final packaging

This remains the most important system upgrade.

### 2. Add A Formal `BRIEF.md` Schema

Standardise `BRIEF.md` with fields such as:

- bid summary
- procurement method
- due date
- proposer profile
- client problem
- overriding question
- S1 / S2 / B
- evaluation criteria map
- 3-4 win themes
- likely evaluator objections
- differentiators
- evidence to reuse
- pricing posture
- mandatory forms and compliance risks
- section message map

This should become the canonical control file for every later section.

### 3. Upgrade `06-methodology`

This is already strong, but it should now add:

- explicit phase scoring against evaluation criteria
- workstream-to-deliverable matrix
- method-to-role matrix
- deliverable-to-payment linkage note
- guidance for when to use proprietary named frameworks versus donor-safe standard frameworks

### 4. Upgrade `07-team-composition`

Add:

- role-to-task traceability matrix
- score-by-position logic
- CV mismatch red flags
- availability-risk checks
- capability matrix pattern, not just organogram and CV formatting

### 5. Extend `10-financial-proposal` From Modelling To Pricing Strategy

The modelling layer is stronger now. The remaining financial gap is strategic pricing:

- QCBS price positioning
- fixed-budget strategy
- least-cost threshold strategy
- visible versus embedded contingency
- when to trade margin for shortlist or award probability
- alternative commercial packaging by phase or option

## New Skills To Add

### 1. `proposal-brief-builder/`

Purpose:

- convert ToR/RFP into a formal `BRIEF.md`
- extract evaluation logic
- identify gaps, assumptions, and must-win themes

### 2. `bid-no-bid-strategy/`

Purpose:

- assess whether the bid is worth pursuing
- identify incumbent risks, relationship gaps, and scoreability
- decide the most likely win path

### 3. `evaluator-scoring-simulator/`

Purpose:

- simulate a technical committee
- score each section against criteria
- identify likely score leakage
- produce a priority rewrite list

### 4. `red-team-review/`

Purpose:

- adversarially test claims, compliance, differentiation, and coherence
- identify contradictions and weak claims
- issue a go / no-go readiness assessment

### 5. `win-theme-generator/`

Purpose:

- derive 3-4 defensible win themes from the ToR, client context, and proposer strengths
- define how each theme appears in each section

### 6. `ghost-pack-builder/`

Purpose:

- create the page-by-page message architecture before drafting
- define exhibits, proof points, and narrative flow

### 7. `pricing-strategy-optimizer/`

Purpose:

- recommend pricing posture by procurement type
- align commercial offer with win strategy
- check sustainability of price against proposed staffing

### 8. `compliance-matrix-builder/`

Purpose:

- turn solicitation instructions into a submission checklist
- map every form, annex, attachment, declaration, and pass/fail requirement

## System-Level Improvements

### 1. Make The Workflow Bid-Stage Based

Instead of mostly section-based routing, add mandatory stages:

- Stage 0: Qualification
- Stage 1: Brief
- Stage 2: Win strategy
- Stage 3: Storyboard
- Stage 4: Drafting
- Stage 5: Red Team
- Stage 6: Packaging

### 2. Introduce A Proposal Control File

Create a machine-readable control file per proposal containing:

- criteria
- themes
- staffing assumptions
- budget assumptions
- required forms
- key proof points
- critical dates

This gives the engine a reliable state object rather than a loose markdown note.

### 3. Build Cross-Section Dependency Rules

Examples:

- every methodology phase must map to a deliverable
- every key expert must map to tasks
- every person-day total must match pricing
- every differentiator in the executive summary must be proved elsewhere
- every benefit claim must trace back to methodology or experience

### 4. Create A Submission Readiness Gate

Before final output, require pass / fail checks on:

- compliance
- evidence sufficiency
- coherence
- score simulation
- commercial viability

### 5. Develop A Private-Sector Branch

Add a separate operating path for:

- corporate RFPs
- transformation proposals
- managed services bids
- executive business cases

This branch should emphasise:

- ROI
- operating model change
- executive storytelling
- business case logic
- differentiator-led commercial framing
