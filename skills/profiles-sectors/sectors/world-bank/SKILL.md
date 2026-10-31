---
name: world-bank
description: Use when a consulting-services proposal follows World Bank procurement, TECH/FIN forms, QCBS or related selection methods; use AfDB, UNDP, or PPDA skills when those rules control.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# World Bank Procurement Framework — Consulting Services
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When
- Use this skill when the solicitation clearly follows World Bank consulting procurement rules.
- Load it before drafting when you need form, scoring, threshold, or compliance guidance.

## Do Not Use When
- The task only needs sector-domain framing without procurement mechanics.
- A different procurement framework clearly applies.

## Required Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---|---|
| The solicitation package, especially instructions, forms, and evaluation criteria. | Buyer solicitation, ToR, or approved brief | Required | Stop the affected claim, request or verify the input, and label the resulting gap. |
| Any known selection method and technical threshold. | Buyer, verified sector source, or discovery | Required | Stop the affected claim, request or verify the input, and label the resulting gap. |
| The target proposal sections that must comply with the framework. | Buyer, verified sector source, or discovery | Conditional | Stop the affected claim, request or verify the input, and label the resulting gap. |

## Workflow

1. Confirm that World Bank procurement applies from explicit cues in the solicitation.
2. Read this skill and the local references to understand forms, scoring, thresholds, and constraints.
3. Map those requirements into the numbered proposal section skills before drafting.
4. Draft to maximize technical quality without creating compliance risk.
5. Check the final output against thresholds, form placement, and two-envelope rules.

**Stop condition:** Stop when proposer identity, controlling framework, mandatory form, sector fit, current rule, or load-bearing evidence remains unresolved.

**Recovery:** Record the gap and owner, seek clarification or current evidence, and return only the separable proposal content that remains supportable.

## Quality Standards
- Treat World Bank instructions as hard constraints, not optional style guidance.
- Keep terminology, form names, and scoring assumptions aligned to the actual solicitation.
- Optimize for evaluator behavior where the framework supports it.

## Anti-Patterns

- Do not infer TECH or FIN form requirements from memory when the solicitation provides exact instructions.
- Do not ignore minimum technical thresholds, conflict-of-interest rules, or pass/fail gates.
- Do not mix World Bank assumptions with PPDA, AfDB, or UN rules.
- Treating a neighbouring sector or framework as interchangeable. **Fix:** identify the controlling rule and primary outcome.
- Adding terminology without changing a delivery choice. **Fix:** link each term to method, risk, output, or evaluation criterion.
- Presenting an unverified current rule or statistic as settled. **Fix:** cite and date the source or mark it not assessed.
- Ignoring a missing mandatory input. **Fix:** stop the affected claim and assign an evidence owner.
- Letting sector or identity framing contradict methodology, staffing, schedule, or price. **Fix:** reconcile all affected sections before release.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| A World Bank-compliant drafting and scoring approach for the relevant proposal sections. | Proposal lead, section writer, and evaluator-readiness reviewer | Applied consistently, traceable to the selected source, and free of unsupported identity, framework, or sector claims. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Routing and source record | Proposal lead and reviewer | Selected identity, framework, sector, source, date, and material gaps are recorded. |
| Decision record | Section writer and delivery lead | Each material choice has rationale, owner, evidence, and a review or stop condition. |
| Conformance check | Release reviewer | Mandatory forms, identity rules, sector logic, and unresolved checks are explicitly assessed. |

## Capability Contract

This skill may read supplied profiles, solicitations, ToRs, approved references, and proposal drafts and may prepare routing guidance or draft content within the authorised workspace. Review is read-only by default. It must not invent credentials, certify compliance, submit a bid, accept terms, publish, disclose confidential information, or change source records without explicit authority.

## Degraded Mode

If the solicitation, profile, current procurement source, sector evidence, network, or reviewer is unavailable, provide the narrowest useful qualified routing or draft. Mark the missing check **not assessed**, omit unsupported credentials, thresholds, dates, or compliance claims, and identify the evidence owner. An unassessed requirement is never a pass.

## Decision Rules

| Decision | Action | Failure/risk avoided |
|---|---|---|
| World Bank selection method | Map the RFP to QCBS, QBS, FBS, LCS, CQS, or SSS and follow its TECH/FIN forms and threshold. | Non-responsive forms or misweighted technical strategy |
| Conflicting solicitation and background guidance | Follow the solicitation while recording the conflict for formal clarification. | Non-responsive interpretation |
| Missing mandatory evidence | Stop the affected claim or form, record the owner and deadline, and continue only with independent supported content. | Fabricated evidence or silent omission |
| Submission, certification, or contractual commitment | Obtain explicit authority and preserve approval evidence before acting. | Unauthorised external commitment |

## Worked Example

A solicitation requires **world bank selection method**, but one controlling input is missing. The proposal team applies this rule: Map the RFP to QCBS, QBS, FBS, LCS, CQS, or SSS and follow its TECH/FIN forms and threshold. It records the gap and owner, withholds the affected assurance, and proceeds only with content that can be verified. This avoids **non-responsive forms or misweighted technical strategy**.

## References

- [Proposal skill router](../../../SKILL.md) — orchestration, profile, reasoning, and release gates.
<!-- dual-compat-end -->
- [references/evaluation-scoring-guide.md](references/evaluation-scoring-guide.md) for scoring behavior.
- [references/tech-fin-forms-guide.md](references/tech-fin-forms-guide.md) for form-level guidance.
- [../SKILL.md](../SKILL.md) to combine framework and sector context.

This skill provides the procurement rules, evaluation methodology, and scoring intelligence that every World Bank proposal must be built around. Read this before writing any section of a World Bank-funded proposal.

## When to Read This Skill

- The ToR references World Bank Investment Project Financing (IPF)
- The RFP uses World Bank Standard Procurement Documents (SPDs)
- The assignment uses QCBS, QBS, FBS, LCS, CQS, or SSS selection
- The proposal must use TECH and FIN standard forms
- You need to understand how evaluators score to maximise points

---

## Selection Methods — Which One and Why It Matters

| Method | When Used | How It Works | Implication for Proposal |
|---|---|---|---|
| **QCBS** | Default for most consulting | Technical scored first; financial opened only for firms passing minimum. Combined weighted score. | Maximise technical quality. Price matters but less than quality. |
| **QBS** | Highly complex/specialised; scope hard to define | Only highest technical scorer negotiates. No financial weighting. | Quality is everything. Price is negotiated after selection. |
| **FBS** | Fixed budget, well-defined scope | Highest technical scorer within budget wins. | Maximise technical score while fitting within stated budget exactly. |
| **LCS** | Routine/standardised (audits, simple surveys) | All firms above technical minimum ranked by cost alone. | Meet the technical threshold comfortably, then compete on price. |
| **CQS** | Small assignments below monetary threshold | Qualifications evaluated; most qualified firm invited to negotiate. | Strong EoI and firm credentials are decisive. |
| **SSS** | Non-competitive; requires Bank justification | One firm approached directly. | Justification document is the critical output, not a competitive proposal. |

**Under QCBS (the most common method)** the RFP Data Sheet sets the quality and cost weights. The Procurement Regulations for IPF Borrowers (Seventh Edition, September 2025, Annex X, para 4.10 and Table 2) give the normal ranges: 90/10 for highly complex, specialised or high-consequence assignments (which may use QBS instead), 70-80 / 30-20 for moderate complexity, and 60-50 / 40-50 for routine assignments (which may use LCS instead). Other weights need the Bank's prior review. Work out what a price gap is worth from the weights in the RFP in front of you. At 80/20 a firm 20% above the lowest price scores 83.3 on cost and loses 3.3 combined points, which a technical lead of about 4.2 points recovers; at 60/40 the same premium loses 6.7 points and needs a lead of about 11.1.

---

## The Two-Envelope Procedure

All competitive consulting procurements use two sealed envelopes:

1. **Envelope 1: Technical Proposal** — opened first, evaluated and scored
2. **Envelope 2: Financial Proposal** — remains sealed until technical evaluation is complete; only opened for firms scoring above the minimum technical threshold

Financial envelopes of firms scoring below the minimum technical score are returned unopened after the contract is signed (Regulations, para 5.46(c), for the single-stage two-envelope process). The Data Sheet fixes that score; Annex X para 4.5 says it normally falls between 70% and 85%, depending on the nature and complexity of the assignment. Read the number first: it is the survival line for this RFP.

---

## TECH Forms — What Goes Where

This map follows the March 2025 revision of the World Bank non-supervision consulting RFP (read against the Bank's own file on 31 October 2026). The issued RFP controls: its checklist, Data Sheet and any amendment decide which forms apply, in what order and with what page limits. [references/tech-fin-forms-guide.md](references/tech-fin-forms-guide.md) holds the form-level detail.

Each TECH form maps to a proposal section skill. Read the sub-skill for content guidance; this table shows the form structure:

| Form | Content | Maps to Skill | Where the points sit |
|---|---|---|---|
| **TECH-1** | Technical Proposal Submission Form (a JV adds the attachment) | `01-cover-letter/` | Not scored |
| **TECH-2A** | Consultant's organisation | `04-firm-profile/` | Relevant experience of the firm |
| **TECH-2B** | Consultant's experience | `05-relevant-experience/` | Relevant experience of the firm |
| **TECH-3A** | Comments on the Terms of Reference (full technical proposal only; the simplified checklist omits TECH-3) | `03-understanding-of-assignment/` | Embedded in the methodology criterion |
| **TECH-3B** | Comments on counterpart staff and facilities (full technical proposal only) | `03-understanding-of-assignment/` | Embedded in the methodology criterion |
| **TECH-4** | Approach, methodology and work plan | `06-methodology/` | Methodology criterion |
| **TECH-5** | Work schedule and planning for deliverables | `08-work-plan/` | Embedded in the methodology criterion |
| **TECH-6** | Team composition, key experts' inputs and attached CVs | `07-team-composition/` | Key-staff criterion |
| **TECH-7** | Code of Conduct | The issued form; no section skill drafts it | Compliance requirement; obtain the actual commitments |
| **TECH-8** | Sexual exploitation and abuse / sexual harassment (SEA/SH) performance declaration | The issued form; no section skill drafts it | Declaration; never invent a clean record |

There is no FIN-5 in the March 2025 checklist. The financial forms are FIN-1 (submission), FIN-2 (summary of costs), FIN-3 (remuneration) and FIN-4 (reimbursable expenses).

---

## Evaluation Criteria and Point Allocations

### Indicative ranges (QCBS)

Annex X, Table 1 of the Regulations (Seventh Edition, September 2025) gives indicative ranges of merit points for the rated criteria. Para 4.3 allows adjustment for justifiable reasons with the Bank's prior review, and para 4.4 leaves the division into sub-criteria to the Borrower.

| Criterion | Indicative range | What Evaluators Look For |
|---|---|---|
| **Adequacy of methodology and work plan** | 20-50% | Tailored (not generic), credible, realistic, thorough. Identifies risks and proposes mitigations. Shows mastery of the subject. |
| **Relevant experience and qualification of key staff** | 30-60% | Each person's CV must directly match the tasks they are assigned. Senior staff on complex tasks. Regional or country experience scored separately where the RFP lists it. |
| **Relevant experience of the firm** | 0-10% | Highly analogous assignments (same type, sector, complexity). Not just quantity: similarity to THIS ToR. Do not spend pages here beyond what the points justify. |
| **Transfer of knowledge** | 0-10% | Specific, structured plan, not vague "capacity building" language. |
| **Nationals among key staff** | 0-10% | Measured as the share of key experts' person-months held by national experts (Annex X, Table 1). Named national experts with genuine roles, not token inclusions. |

Methodology, key staff and firm experience are the three criteria the Regulations require; transfer of knowledge and participation of nationals are included only "depending on the nature and needs of the assignment" (para 4.2). The total is 100.

**The exact point allocations are set per assignment in the RFP Data Sheet.** Always check the Data Sheet before writing — it tells you exactly how many points each criterion carries.

### Key Personnel Sub-scoring

The Standard RFP's Data Sheet template splits each key-expert position's points into three sub-criteria, with the Borrower inserting the weights inside these ranges (March 2025 revision, read on 31 October 2026). The Data Sheet of the issued RFP controls. For each proposed professional position:

| Sub-criterion | Typical Weight | What Scores High |
|---|---|---|
| **General qualifications** | 10-20% | Education, training and relevant experience. Qualifications and years that meet or exceed the ToR's stated minimum. |
| **Adequacy for the assignment** | 60-80% | Specific experience directly matching the ToR tasks for this position. Not general sector work — the exact type of work described in the ToR. |
| **Regional/country experience** | 0-10% (only if the Data Sheet adds it) | Named projects in the same country or region, working-level language skills and knowledge of the local administrative system, if relevant to the task. |

---

## The Scoring Scale — What Each Score Means

| Score | Meaning | What the Proposal Shows |
|---|---|---|
| **0** | Feature absent | Criterion not addressed at all |
| **1** | Present but deficient | Information provided but insufficient, unclear, or not credible |
| **2** | Meets requirements | Sufficient information demonstrating the requirement will be met |
| **3** | Marginally exceeds | Information shows the requirement will be exceeded |
| **4** | Significantly exceeds | Substantial evidence of significant value addition beyond requirements |

The 0-4 scale above comes from the Bank's evaluation guidance for rated criteria, which could not be reached on 31 October 2026. A consulting RFP awards points under the point system in its Data Sheet, so use the scale as a way to think about quality, not as the scoring rule. The practical point stands: a response that only meets the ToR earns a middling share of the points, and the proposals that win show more than compliance.

To score 3-4, a proposal must:
- Go beyond restating the ToR — show deeper understanding than the ToR itself demonstrates
- Offer specific, named tools and frameworks (not generic "we will analyse")
- Identify risks the ToR did not mention and propose credible mitigations
- Show innovation — better ways to achieve the objectives
- Demonstrate quantified value addition

---

## Combined Scoring Formula

### Technical Score
St is the sum of the points awarded across the Data Sheet's criteria, out of 100.

### Financial Score
`Sf = 100 × (Lowest Price / Firm's Price)`, using the lowest price among the financial proposals opened.

### Final Score
`S = St × T% + Sf × P%`. The Data Sheet inserts the weights T and P (T + P = 100%) and fixes the formula for the issued RFP. The highest combined score wins.

**Example (80/20 split):** A firm scoring 240/300 on technical with a price of $4.8M vs. the lowest price of $4.4M:
- Technical: (240/300) × 100 × 80% = 64.00
- Financial: (4,400,000/4,800,000) × 100 × 20% = 18.33
- Combined: **82.33**

---

## Scoring Strategy by Section

### TECH-3: Comments on the ToR (Often Underrated)

This is where most proposals lose easy points. Evaluators explicitly reward:
- **Substantive comments** that identify gaps, ambiguities, or improvements in the ToR
- **Proposals that just say "we agree with the ToR" score 1-2**
- **Proposals that propose well-reasoned improvements score 3-4**

Format each comment as: ToR Reference → Observation → Recommendation (see `03-understanding-of-assignment/SKILL.md`).

### TECH-4: Methodology (The Decisive Section)

This carries the most points and the most scoring differentiation between firms. Evaluators are instructed to look for:
- **Credible** — demonstrates the firm actually knows how to do this work
- **Realistic** — timeline, resources, and approach are achievable
- **Thorough** — all ToR tasks addressed with specific methods, not generic language
- **Tailored** — written for THIS assignment, not copy-pasted from another proposal
- **Risk-aware** — identifies risks beyond those in the ToR and proposes mitigations

Use the P-I-P structure (see `references/proposal-strategy-and-persuasion.md`) for every phase.

### TECH-6: Key Personnel (Where Most Points Are Won or Lost)

This is often the highest-weighted criterion (indicative range 30-60 points; the Data Sheet decides). Critical rules:
- Each CV must directly match the ToR tasks for that position
- Evaluators read CVs against the ToR task descriptions — mismatches score 1
- Senior, experienced staff on the most technically complex tasks
- Regional/country experience is scored separately — include it
- Availability must be confirmed for the required period
- Staff substitution after award requires Bank approval and equivalent qualifications

### FIN Forms: Strategic Pricing Under QCBS

- Financial scores are inversely proportional to price, with the lowest price scoring 100 (Annex X, para 4.8; the RFP states the formula). Price position is therefore a calculation, not a slogan: use the weights in the RFP (see the worked 80/20 and 60/40 figures above).
- Evaluation prices exclude local indirect taxes and income tax payable on non-resident experts' remuneration, unless the Bank agrees otherwise (Annex X, para 4.6). Price on the basis the RFP states.
- **Price competitively and defensibly while maximising technical quality**: the technical weight is the larger lever in every normal weighting.
- Abnormally Low Bids are identified and rejected — price must be defensible
- Unbalanced or front-loaded pricing is examined and may be rejected

---

## Minimum Technical Score — The Survival Line

The RFP Data Sheet specifies the minimum technical score; the Standard RFP leaves the number blank for the Borrower to insert. Annex X, para 4.5 of the Regulations says it "shall normally be in the range of 70-85%" depending on the nature and complexity of the assignment. It is a hard gate:
- A proposal below the number is eliminated and its financial envelope is returned unopened.
- A proposal at or above it goes to financial evaluation.
- The difference between one point below and one point above is total, not marginal.

The Regulations name this overall minimum for consulting proposals. Some RFPs may add minimums on selected criteria or on a single criterion; look for them in the Data Sheet, because the consulting annex of the Regulations does not list them as a standard category.

**Never ignore a low-weighted criterion.** Even a criterion worth 5 points can have a sub-threshold that eliminates you if you score 0-1 on it.

---

## Process Timeline

1. **General Procurement Notice (GPN)** published
2. **Request for Expressions of Interest (REoI)** issued
3. **EoIs received and shortlist compiled** (five to eight eligible firms; fewer only with the Bank's agreement; Regulations para 7.17)
4. **Request for Proposals (RFP)** issued to shortlisted firms (the Data Sheet sets the submission deadline; the 30-Business-Day minimum in Regulations para 5.36 is stated for open international competitive procurement)
5. **Proposals submitted** (two envelopes)
6. **Technical envelopes opened** publicly
7. **Technical evaluation** by Evaluation Committee
8. **Technical scores communicated** to all shortlisted firms
9. **Financial envelopes opened** publicly (only for firms above minimum threshold, and not earlier than 10 Business Days after the technical results are communicated; Regulations para 5.41)
10. **Financial evaluation and combined scoring**
11. **Notification of Intention to Award** (10 business day standstill period)
12. **Negotiations** with first-ranked firm
13. **Contract award**

---

## Conflict of Interest Rules

Critical disqualification risks:
- A firm that prepared the ToR **cannot be shortlisted** for the implementation assignment
- A firm shortlisted for consulting **cannot supply goods** for the same project if it creates a conflict
- All evaluators must sign Conflict of Interest declarations
- Firms/individuals sanctioned under Bank Anti-Corruption Guidelines are ineligible

---

## Reference Library

| Reference File | Contents |
|---|---|
| `references/evaluation-scoring-guide.md` | Detailed scoring methodology, comparative formulas, worked examples, scoring strategy per TECH form |
| `references/tech-fin-forms-guide.md` | Current form map (TECH-1 through TECH-8, FIN-1 through FIN-4, March 2025 RFP), completion rules and pre-submission checks |

Read the relevant reference file for detailed guidance beyond this summary.

---

*Based on: World Bank "A Beginner's Guide for Borrowers: Procurement under World Bank Investment Project Financing" (November 2023, 2nd Edition) and "Evaluating Bids and Proposals — Including Use of Rated Criteria" (February 2025, 3rd Edition).*

*Rules and ranges verified on 31 October 2026 against the Bank's Procurement Regulations for IPF Borrowers, Seventh Edition, September 2025 (paras 5.36, 5.41, 5.46, 5.81-5.82, 7.17 and Annex X) and the March 2025 revision of the non-supervision consulting RFP. The two guides above were not re-read on that date. The issued RFP controls.*
