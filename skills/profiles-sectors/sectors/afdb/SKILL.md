---
name: afdb
description: Use when an assignment is funded or governed by African Development Bank procurement, including ADB, ADF, or NTF windows; use World Bank, UNDP, or PPDA skills when those rules control.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# African Development Bank Procurement Framework
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When
- Use this skill when the solicitation follows African Development Bank consulting procurement rules.
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

1. Confirm that AfDB procurement applies from explicit cues in the solicitation.
2. Read this skill and the local references to understand forms, scoring, safeguards, and constraints.
3. Map those requirements into the numbered proposal section skills before drafting.
4. Draft to maximize technical quality without creating compliance risk.
5. Check the final output against thresholds, form placement, and submission rules.

**Stop condition:** Stop when proposer identity, controlling framework, mandatory form, sector fit, current rule, or load-bearing evidence remains unresolved.

**Recovery:** Record the gap and owner, seek clarification or current evidence, and return only the separable proposal content that remains supportable.

## Quality Standards
- Treat AfDB instructions as hard constraints, not optional style guidance.
- Keep terminology, form names, and evaluation assumptions aligned to the actual solicitation.
- Optimize for evaluator behavior where the framework supports it.

## Anti-Patterns

- Do not rely on generic donor assumptions when the AfDB solicitation gives exact instructions.
- Do not ignore minimum thresholds, safeguards expectations, or eligibility rules.
- Do not mix AfDB assumptions with World Bank, PPDA, or UN rules.
- Treating a neighbouring sector or framework as interchangeable. **Fix:** identify the controlling rule and primary outcome.
- Adding terminology without changing a delivery choice. **Fix:** link each term to method, risk, output, or evaluation criterion.
- Presenting an unverified current rule or statistic as settled. **Fix:** cite and date the source or mark it not assessed.
- Ignoring a missing mandatory input. **Fix:** stop the affected claim and assign an evidence owner.
- Letting sector or identity framing contradict methodology, staffing, schedule, or price. **Fix:** reconcile all affected sections before release.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| An AfDB-compliant drafting and scoring approach for the relevant proposal sections. | Proposal lead, section writer, and evaluator-readiness reviewer | Applied consistently, traceable to the selected source, and free of unsupported identity, framework, or sector claims. |

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
| AfDB selection method | Map the notice and RFP to the stated selection method, forms, technical threshold, and financial treatment. | Non-responsive AfDB submission |
| Conflicting solicitation and background guidance | Follow the solicitation while recording the conflict for formal clarification. | Non-responsive interpretation |
| Missing mandatory evidence | Stop the affected claim or form, record the owner and deadline, and continue only with independent supported content. | Fabricated evidence or silent omission |
| Submission, certification, or contractual commitment | Obtain explicit authority and preserve approval evidence before acting. | Unauthorised external commitment |

## Worked Example

A solicitation requires **afdb selection method**, but one controlling input is missing. The proposal team applies this rule: Map the notice and RFP to the stated selection method, forms, technical threshold, and financial treatment. It records the gap and owner, withholds the affected assurance, and proceeds only with content that can be verified. This avoids **non-responsive afdb submission**.

## References

- [Proposal skill router](../../../SKILL.md) — orchestration, profile, reasoning, and release gates.
<!-- dual-compat-end -->
- Local `references/` files for selection methods, safeguards, project cycle, and financial terms.
- [../SKILL.md](../SKILL.md) to combine framework and sector context.

This skill provides the procurement rules, evaluation methodology, safeguard requirements, and scoring intelligence that every AfDB-funded proposal must be built around. Read this before writing any section of an AfDB-funded proposal.

## When to Read This Skill

- The ToR references African Development Bank, AfDB, ADB (African Development Bank window), or ADF (African Development Fund)
- The RFP uses AfDB Standard Procurement Documents
- The assignment uses QCBS, QBS, FBS, LCS, CQS, or SSS selection
- The proposal must comply with AfDB's Integrated Safeguards System (ISS)
- The assignment is funded through an AfDB lending operation or grant
- You need to understand how AfDB evaluators score to maximise points

---

## AfDB Overview

The African Development Bank Group comprises three entities:
- **ADB** (African Development Bank) — sovereign-guaranteed lending to creditworthy RMCs at near-market rates
- **ADF** (African Development Fund) — concessional lending and grants to low-income RMCs
- **NTF** (Nigeria Trust Fund) — concessional lending to lower-income RMCs

All three windows use the same procurement framework and safeguard requirements.

**Regional Member Countries (RMCs):** All 54 African countries are RMCs and eligible for AfDB financing. Non-regional member countries (28 countries including G7 nations, China, India, Brazil) contribute capital but are not borrowers.

---

## Selection Methods for Consulting Services

| Method | When Used | How It Works | Implication for Proposal |
|---|---|---|---|
| **QCBS** | Default for most consulting | Technical scored first (max 100); financial opened only for firms passing minimum. Combined weighted score. | Maximise technical quality. Price matters but typically less than quality. |
| **QBS** | Highly complex/specialised; scope hard to define | Only highest technical scorer's financial proposal opened. No financial weighting. | Quality is everything. Price negotiated after selection. |
| **FBS** | Fixed budget, well-defined scope | Highest technical scorer within budget wins. Proposals exceeding budget rejected. | Maximise technical score while staying within stated budget. |
| **LCS** | Routine/standardised assignments (audits, standard surveys) | All firms above technical minimum ranked by lowest cost. | Meet the technical threshold comfortably, then compete aggressively on price. |
| **CQS** | Small assignments below monetary threshold | Consultant selected based on qualifications for the assignment. | Strong EoI and firm credentials are decisive. |
| **SSS** | Non-competitive; requires AfDB justification | One firm approached directly. | Justification and quality of technical proposal are critical. |

**Under QCBS (the most common method):** Technical weighting is typically 70-80%, financial 20-30%. The formula mirrors World Bank practice: winning on technical quality is almost always more decisive than winning on price.

---

## Two-Envelope Procedure

All competitive consulting procurements use two sealed envelopes:

1. **Envelope 1: Technical Proposal** — opened first, evaluated and scored
2. **Envelope 2: Financial Proposal** — remains sealed until technical evaluation is complete; only opened for firms scoring above the minimum technical threshold

Financial envelopes of firms scoring below the minimum technical threshold (typically **70-80 out of 100**, specified in RFP) are returned unopened.

---

## Evaluation Criteria and Point Allocations

### Standard Criteria (QCBS)

| Criterion | Typical Points | What Evaluators Look For |
|---|---|---|
| **Specific Experience of the Firm** | 10-20 | Highly analogous assignments: same type, sector, region, complexity. Quality over quantity. |
| **Adequacy of Methodology and Work Plan** | **30-50** | Tailored approach, realistic timeline, risk awareness, innovation, thorough coverage of all ToR tasks. |
| **Key Professional Staff** | **30-60** | Each CV must match the ToR tasks for that position. Senior staff on complex tasks. Regional experience scored separately. |
| **Transfer of Knowledge / Capacity Building** | 0-10 | Specific, structured training plan — not vague capacity building language. |
| **Participation of Nationals / Africans** | 0-10 | Named national or regional experts with genuine roles. AfDB promotes use of African consultants. |
| **TOTAL** | **100** | |

### Financial Scoring Formula (QCBS)

```
Financial Score = (Lowest Evaluated Price / Your Evaluated Price) x 100

Total Score = (Technical Score x Technical Weight%) + (Financial Score x Financial Weight%)
```

**Example at 80/20 split:**
- Firm A: Tech 82, Price lowest → Financial 100 → Total = (82 x 0.8) + (100 x 0.2) = 85.6
- Firm B: Tech 88, Price 15% higher → Financial 87.0 → Total = (88 x 0.8) + (87.0 x 0.2) = 87.8
- Firm B wins despite higher price

---

## AfDB Project Cycle

Understanding the project cycle helps consultants identify where their services fit:

| Phase | Key Activities | Consultant Opportunities |
|---|---|---|
| **Country Strategy Paper (CSP)** | 5-year strategy per RMC, sector diagnostics | Country/sector analysis, strategy development |
| **Project Identification** | Concept note, preliminary feasibility | Pre-feasibility studies, sector assessments |
| **Project Preparation** | Detailed feasibility, ESIA, design | Feasibility studies, environmental assessments, detailed design |
| **Appraisal** | AfDB reviews project, negotiates with borrower | Independent reviews, due diligence |
| **Board Approval** | Board approves loan/grant | — |
| **Implementation** | Procurement, construction, supervision | Implementation support, supervision, capacity building |
| **Completion** | Project Completion Report (PCR) | Completion evaluation, impact assessment |
| **Post-Evaluation** | Independent evaluation by IDEV | Independent evaluations |

---

## Project Categorisation (Environmental and Social)

AfDB classifies all projects into four categories that determine safeguard requirements:

| Category | Description | Safeguard Requirements |
|---|---|---|
| **Category 1** | Likely to cause significant adverse E&S impacts that are irreversible, cumulative, or unprecedented | Full ESIA required, extensive consultation, Environmental and Social Management Plan (ESMP) |
| **Category 2** | Likely to cause adverse E&S impacts that are less severe, site-specific, and largely reversible | Targeted ESIA or ESMP, proportionate consultation |
| **Category 3** | Minimal or no adverse E&S impacts | No ESIA required; screening report sufficient |
| **Category 4** | AfDB-financed intermediary operations (financial intermediaries, equity funds) | Environmental and Social Management System (ESMS) for the intermediary |

**Proposal implication:** If the assignment involves safeguard compliance work (ESIA, ESMP, RAP), demonstrate knowledge of the correct category requirements. Reference AfDB's Integrated Safeguards System (ISS), not World Bank ESF, even where the concepts overlap.

---

## Domestic Preference and African Consultants

AfDB actively promotes the use of African consulting firms:

- **Shortlisting preference:** At least one African firm should be included on shortlists where qualified firms exist
- **Margin of preference:** AfDB may apply a preference margin for national/regional firms in certain procurement methods
- **Joint ventures encouraged:** AfDB encourages JVs between international and African firms for knowledge transfer
- **African consultants database:** Firms should register on AfDB's procurement portal

**Proposal application:** Highlight African team members, local partnerships, and knowledge transfer components. AfDB evaluators view African participation favourably.

---

## Key Differences from World Bank Procurement

| Feature | World Bank | AfDB |
|---|---|---|
| Standard forms | TECH-1 through TECH-8, FIN-1 through FIN-5 | Similar structure but AfDB-specific templates |
| Minimum technical score | Typically 75/100 | Typically 70-80/100 (varies by RFP) |
| Safeguard framework | ESF (10 Environmental and Social Standards) | ISS 2023 (10 Operational Safeguards) |
| African firm preference | No specific preference | Active promotion of African consulting firms |
| Project rating scale | 6-point IEG scale | 4-point IDEV scale |
| Complaints mechanism | Procurement review by Bank | Independent Review Mechanism (IRM) |
| Evaluation approach | OECD-DAC 5+1 criteria | OECD-DAC 6 criteria (including Coherence) |

---

## Conflict of Interest Rules

Critical disqualification risks (similar to World Bank):
- A firm that prepared the ToR **cannot be shortlisted** for the implementation assignment
- A firm shortlisted for consulting **cannot supply goods** for the same project if it creates a conflict
- All evaluators must declare absence of conflicts of interest
- Firms/individuals debarred under AfDB Sanctions Procedures are ineligible
- Cross-debarment: AfDB participates in mutual enforcement of debarment with other MDBs (World Bank, IDB, EBRD, ADB-Asia)

---

## Anti-Corruption and Integrity

AfDB's Integrity and Anti-Corruption Department (PIAC) investigates fraud and corruption in Bank-funded operations. Five sanctionable practices:

1. **Corrupt practice** — offering, giving, receiving, or soliciting anything of value to influence action
2. **Fraudulent practice** — misrepresentation of facts to influence procurement
3. **Collusive practice** — arrangement between bidders to establish artificial prices
4. **Coercive practice** — impairing or harming to influence participation
5. **Obstructive practice** — destroying, falsifying, or concealing evidence; threatening witnesses

**Sanctions:** Reprimand, conditional non-debarment, debarment (1-indefinite years), debarment with conditional release, restitution/financial remedy.

---

## Reference Files

Load these references for detailed procedural requirements:

| Reference | Content |
|---|---|
| `references/procurement-and-consultant-selection.md` | Detailed procurement methods, shortlisting, proposal evaluation, financial scoring formulas, negotiation procedures, contract types, AfDB procurement portal registration, procurement notices |
| `references/safeguards-and-financial-terms.md` | ISS 2023 (all 10 Operational Safeguards), project categorisation, ESIA requirements, ADB/ADF lending terms, climate screening, gender mainstreaming |
| `references/project-cycle-and-evaluation.md` | Project cycle phases, PCR structure, IDEV independent evaluation framework, OECD-DAC criteria, 4-point rating scale, sustainability assessment, PAR template |

Read the relevant reference file for detailed guidance beyond this summary.

---

*Based on: AfDB Procurement Policy for Bank Group Funded Operations (2015, revised 2023), Rules and Procedures for Procurement of Goods, Works, and Non-Consulting Services (2023), Rules and Procedures for the Use of Consultants (2023), Integrated Safeguards System (ISS, 2023), Independent Evaluation Policy (IDEV), AfDB Financial Products and Terms.*
