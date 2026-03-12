# Prioritised Gap Analysis and Remediation Plan

**Date:** 12 March 2026

---

## Gap Classification

| Level | Meaning | Action |
|-------|---------|--------|
| **Critical** | Blocks ability to win $1M+ assignments in common scenarios | Must fix before bidding |
| **High** | Reduces competitiveness against Big Four firms | Fix within Phase 1 |
| **Medium** | Limits depth in specific assignment types | Fix within Phase 2 |
| **Low** | Polish and differentiation | Fix within Phase 3 |

---

## Critical Gaps (12 items)

### C1. Eight Domain Skills Lack Reference Files

**Gap:** Change management, M&E, stakeholder engagement, capacity building, GESI, safeguards, data management, and sustainability planning each have only a SKILL.md (77–103 lines) with no supporting reference documentation.

**Impact:** These domains appear in nearly every donor ToR as scored criteria. Without reference files, Claude generates competent but generic content — "we will use ADKAR" rather than "we will conduct a three-stage organisational readiness assessment using the Prosci methodology, beginning with a change saturation analysis."

**Remediation:** Create one reference file per domain skill (200–350 lines each). See `domain-skills-assessment.md` for specific content requirements per skill.

**Effort:** ~2,200 lines across 8 files. Estimated 4–6 focused sessions.

---

### C2. PPDA Uganda Procurement Skill Missing

**Gap:** No SKILL.md or reference files for Uganda's Public Procurement and Disposal of Public Assets Act. This is the most common procurement framework for Uganda government contracts.

**Impact:** Cannot optimise proposal structure, evaluation criteria, or scoring for PPDA-governed work. Generic proposal structure applies but misses PPDA-specific requirements (standard bidding documents, evaluation committee composition, debriefing rights, administrative review).

**Remediation:** Create `sectors/ppda-uganda/SKILL.md` (~200 lines) covering:
- PPDA Act 2003 (as amended) procurement methods
- Standard evaluation criteria and point allocations
- Bid document structure requirements
- Preference and reservation schemes
- Administrative review process
- Common PPDA compliance mistakes

**Effort:** 1 focused session.

---

### C3. No Evaluation Scoring Guidance Across Sections

**Gap:** Only sections 05 (relevant experience) and 07 (team composition) mention evaluation weighting. The remaining 8 sections provide no guidance on what percentage of total score they carry or what evaluators prioritise.

**Impact:** Cannot optimise effort allocation across proposal sections. A firm might spend equal time on all sections when, in a QCBS evaluation, methodology (section 06) might carry 40% while the cover letter (section 01) carries 0%.

**Remediation:** Add an "Evaluation Scoring" subsection to every section SKILL.md with:
- Typical weight range by procurement framework (World Bank QCBS, PPDA, UNDP)
- What evaluators look for in this specific section
- Common point-losing mistakes
- How to maximise score within page/time constraints

**Effort:** ~15 lines per section × 10 sections = ~150 lines. 1 session.

---

### C4. No Worked Weak-vs-Strong Examples

**Gap:** No section skill contains side-by-side examples of weak vs strong writing. Templates exist but calibration examples do not.

**Impact:** Claude cannot distinguish between "adequate" and "excellent" output. Without calibration examples, the skill says "be specific" but doesn't show what specific looks like compared to generic.

**Remediation:** Add 2–3 weak-vs-strong comparison pairs per section skill. Focus on sections where quality variance is highest: 02 (executive summary), 03 (understanding), 05 (relevant experience), 06 (methodology).

**Effort:** ~30 lines per section × 10 sections = ~300 lines. 2 sessions.

---

### C5. Three Core Sector Skills Empty (ICT, Health, Governance)

**Gap:** The three most common sectors for East African consulting assignments have no content.

**Impact:** Proposals cannot use sector-specific terminology, frameworks, or evaluation patterns. A health systems assessment proposal reads like a generic consulting proposal, not one written by a firm that understands health system building blocks, HMIS, essential medicines, or UHC.

**Remediation:** Create SKILL.md (~150 lines) + 1 reference file (~200 lines) for each:
- `sectors/ict/` — ICT terminology, digital transformation frameworks, systems assessment methodology, MIS design patterns, East African digital landscape
- `sectors/health/` — WHO building blocks, HMIS, health financing, supply chain, UHC, East African health landscape
- `sectors/governance/` — PFM, decentralisation, anti-corruption, public service reform, East African governance context

**Effort:** ~1,050 lines across 6 files. 3 sessions.

---

### C6. World Bank FIN-1–4 Form Templates Missing

**Gap:** Section 10 (financial proposal) references World Bank FIN forms but does not include their structure. The `sectors/world-bank/` skill covers TECH forms but not FIN forms.

**Impact:** Cannot generate World Bank-compliant financial proposals without external reference.

**Remediation:** Add FIN-1–4 form structures to either `10-financial-proposal/references/` or `sectors/world-bank/references/`.

**Effort:** ~100 lines. 1 session (partial).

---

### C7. No Procurement Framework Decision Tree

**Gap:** No guidance on which procurement framework applies to a given ToR, or how to detect the framework from document cues.

**Impact:** A consultant receiving a ToR must manually determine whether it follows World Bank, PPDA, UNDP, AfDB, or direct client rules. Wrong framework = wrong format = disqualification.

**Remediation:** Add a "Procurement Framework Detection" section to the parent SKILL.md or create a standalone reference file with:
- Document cues that indicate each framework (logo, standard clauses, form numbers)
- Decision tree: funding source → procurement framework → template set
- Compliance checklist per framework

**Effort:** ~80 lines. 1 session (partial).

---

### C8. No Pre-Submission Quality Gate

**Gap:** No cross-section consistency check. Nothing ensures the methodology is consistent with the work plan, that the financial proposal matches the staffing schedule, or that all ToR requirements are addressed.

**Impact:** Internal inconsistencies are the most common reason proposals lose points. A methodology that promises 5 phases but a work plan showing 4 phases signals sloppiness.

**Remediation:** Add a "Pre-Submission Checklist" to the parent SKILL.md covering:
- Section-to-section consistency checks (methodology ↔ work plan ↔ financial ↔ staffing)
- ToR requirement traceability (every ToR item addressed)
- Formatting compliance (page limits, required forms, annexes)
- Language quality check (run east-african-english standards)
- Red Team review trigger

**Effort:** ~60 lines. 1 session (partial).

---

### C9. No Cross-Section Theme Consistency

**Gap:** Each section skill operates independently. No mechanism ensures that the "win themes" identified in section 02 (executive summary) are woven through sections 03, 06, 07, and the cover letter.

**Impact:** McKinsey and Deloitte proposals have 3–4 themes that appear in every section. Without theme threading, each section reads as standalone rather than as part of a coherent argument.

**Remediation:** Add "Theme Threading" guidance to:
- Section 02 (executive summary) — define the 3–4 win themes
- Parent SKILL.md — require theme list to be established before writing any section
- Each section SKILL.md — add a "Theme Integration" note showing how themes manifest in that section

**Effort:** ~100 lines spread across files. 1 session.

---

### C10. M&E Scoring Criterion Depth

**Gap:** M&E is a mandatory scored criterion in World Bank, UNDP, and most donor ToRs. The current M&E skill (97 lines, no references) cannot generate content that scores in the top band.

**Impact:** A proposal with a weak M&E section loses 5–15% of available points — often the difference between winning and losing.

**Remediation:** (Covered by C1 — M&E reference file creation is priority #1 in domain skill remediation.)

---

### C11. GESI Scoring Criterion Depth

**Gap:** GESI is increasingly a mandatory scored criterion (5–15% of total score in UNDP, rising in World Bank). The current GESI skill (77 lines, no references) produces generic commitments rather than substantive analysis.

**Impact:** Weak GESI = automatic point loss in donor-funded work. Evaluators specifically check for intersectionality, gender budgeting, and measurable gender outcomes.

**Remediation:** (Covered by C1 — GESI reference file creation is priority #3 in domain skill remediation.)

---

### C12. AfDB Procurement Skill Missing

**Gap:** No SKILL.md or references for African Development Bank procurement. AfDB is a major funder of infrastructure, energy, and governance projects in East Africa.

**Impact:** Cannot optimise for AfDB evaluation criteria or comply with AfDB-specific requirements (ISS, country strategy alignment, additionality).

**Remediation:** Create `sectors/afdb/SKILL.md` (~200 lines) covering:
- AfDB procurement methods and selection criteria
- Integrated Safeguards System requirements
- Country strategy alignment signalling
- Standard evaluation point allocations
- Common AfDB compliance requirements

**Effort:** 1 focused session.

---

## High Gaps (6 items)

### H1. Remaining 6 Sector Skills Empty

Agriculture, education, energy, water/sanitation, financial services, transport/infrastructure directories are stubs.

**Remediation:** Populate each with SKILL.md (~100 lines) covering terminology, frameworks, stakeholders, and East African context. Agriculture and education first (most frequent in ToRs).

---

### H2. Thin Sections in Cross-Cutting References

Sections 9–13 in world-class-proposal-patterns.md and sections 11–15 in consulting-delivery-excellence.md average ~6 lines each.

**Remediation:** Expand each thin section to ~15–20 lines. Total ~100 lines of additions.

---

### H3. Section 01 (Cover Letter) Underdeveloped

At 81 lines with no references, cross-references, or procurement variants, this is the weakest numbered section skill.

**Remediation:** Expand to ~150 lines with procurement-specific guidance, strong-vs-weak opener examples, and compliance statement templates.

---

### H4. Section 09 (EoI) Lacks Procurement Variants

EoI structure varies significantly by procurement framework (World Bank shortlisting, PPDA two-stage, UNDP RFP). Current skill is generic.

**Remediation:** Add procurement variant structures (~50 lines).

---

### H5. No Sector-Specific Project Card Libraries

Relevant experience (section 05) requires project cards, but there is no pre-built library of cards by sector.

**Remediation:** Create sector-specific project card templates showing what "excellent" outcomes statements look like in each domain.

---

### H6. Operations Frameworks File Lighter Than Siblings

`consulting-frameworks/references/operations-frameworks.md` (156 lines) is thinner than the other 4 framework files (165–222 lines).

**Remediation:** Add 2–3 frameworks: activity-based costing, customer journey mapping, lean/continuous improvement basics. ~60 lines.

---

## Medium Gaps (5 items)

### M1. No Full Worked Proposal Example

No anonymised example showing all 10 sections applied to a realistic assignment.

### M2. No Multi-Currency Pricing Guidance

Financial proposal has no guidance on when to quote UGX vs USD vs mixed.

### M3. No Joint Venture / Consortium Guidance

Team composition and firm profile skills do not address JV structures.

### M4. No EU/JICA/FCDO Procurement Frameworks

Missing procurement skills for European, Japanese, and British aid procurement.

### M5. No Proposal Formatting and Layout Guide

No guidance on visual design, page layout, font selection, or branding standards for the final document.

---

## Low Gaps (3 items)

### L1. No Monte Carlo Simulation Guidance in Risk Management

### L2. No Client Relationship Management / CRM Integration

### L3. Blog Skills Disproportionately Large (22% of content vs 7% for proposal sections)

---

## Remediation Roadmap

### Phase 1 — Critical (target: 85% readiness)

| # | Action | Files | Lines | Sessions |
|---|--------|-------|-------|----------|
| C1 | Create 8 domain skill reference files | 8 new files | ~2,200 | 4–6 |
| C2 | Create PPDA Uganda procurement skill | 1 new file | ~200 | 1 |
| C3 | Add evaluation scoring to all 10 sections | 10 edits | ~150 | 1 |
| C4 | Add weak-vs-strong examples to sections | 10 edits | ~300 | 2 |
| C5 | Create ICT, Health, Governance sector skills | 6 new files | ~1,050 | 3 |
| C6 | Add World Bank FIN-1–4 templates | 1 new file | ~100 | 0.5 |
| C7 | Create procurement detection guide | 1 new/edit | ~80 | 0.5 |
| C8 | Add pre-submission quality gate | 1 edit | ~60 | 0.5 |
| C9 | Add theme threading guidance | ~6 edits | ~100 | 0.5 |
| | **Phase 1 Total** | | **~4,240** | **~14** |

### Phase 2 — Competitive (target: 92% readiness)

| # | Action | Files | Lines | Sessions |
|---|--------|-------|-------|----------|
| C12 | Create AfDB procurement skill | 1 new file | ~200 | 1 |
| H1 | Create 6 remaining sector skills | 6 new files | ~600 | 3 |
| H2 | Expand thin reference sections | 2 edits | ~100 | 0.5 |
| H3 | Expand section 01 (cover letter) | 1 edit | ~70 | 0.5 |
| H4 | Add EoI procurement variants | 1 edit | ~50 | 0.5 |
| H5 | Create project card libraries | 3 new files | ~300 | 1.5 |
| H6 | Expand operations frameworks | 1 edit | ~60 | 0.5 |
| | **Phase 2 Total** | | **~1,380** | **~7.5** |

### Phase 3 — World-Class (target: 98% readiness)

| # | Action | Files | Lines | Sessions |
|---|--------|-------|-------|----------|
| M1 | Create full worked proposal example | 10 new files | ~3,000 | 5 |
| M2 | Add multi-currency pricing guidance | 1 edit | ~30 | 0.5 |
| M3 | Add JV/consortium guidance | 2 edits | ~60 | 0.5 |
| M4 | Create EU/JICA/FCDO procurement skills | 3 new files | ~600 | 3 |
| M5 | Create formatting and layout guide | 1 new file | ~150 | 1 |
| L1-3 | Polish items | Various | ~200 | 2 |
| | **Phase 3 Total** | | **~4,040** | **~12** |

---

## Total Remediation Effort

| Phase | New Lines | Sessions | Cumulative Readiness |
|-------|-----------|----------|---------------------|
| Current state | 17,200 | — | 65–70% |
| Phase 1 | +4,240 | ~14 | 85% |
| Phase 2 | +1,380 | ~7.5 | 92% |
| Phase 3 | +4,040 | ~12 | 98% |
| **Total** | **+9,660** | **~33.5** | **98%** |

Final repository size after all phases: ~27,000 lines of documented knowledge.
