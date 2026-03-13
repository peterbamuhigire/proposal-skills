# Prioritised Gap Analysis and Remediation Plan

**Date:** 12 March 2026
**Last updated:** 12 March 2026 (post-Session 10 progress review)

---

## Gap Classification

| Level | Meaning | Action |
|-------|---------|--------|
| **Critical** | Blocks ability to win $1M+ assignments in common scenarios | Must fix before bidding |
| **High** | Reduces competitiveness against Big Four firms | Fix within Phase 2 |
| **Medium** | Limits depth in specific assignment types | Fix within Phase 3 |
| **Low** | Polish and differentiation | Fix within Phase 3 |

---

## Progress Summary

After 6 remediation sessions (Sessions 5–10), the repository has grown from 17,200 lines to ~26,070 lines (+8,870 lines). Of the original 12 critical gaps, 4 are fully closed, 2 are partially closed, and 6 remain open.

| Category | Total | Closed | Partially Closed | Open |
|----------|-------|--------|-------------------|------|
| Critical | 12 | 4 | 2 | 6 |
| High | 6 | 0 | 1 | 5 |
| Medium | 5 | 0 | 0 | 5 |
| Low | 3 | 0 | 0 | 3 |

---

## Critical Gaps (12 items)

### C1. Eight Domain Skills Lack Reference Files — PARTIALLY CLOSED

**Gap:** Change management, M&E, stakeholder engagement, capacity building, GESI, safeguards, data management, and sustainability planning each had only a SKILL.md (77–103 lines) with no supporting reference documentation.

**Progress:** 3 of 8 domains now have full reference libraries:
- **Change Management** — 3 reference files (change-process-models.md, hard-and-soft-integration.md, lean-and-adaptive-change.md)
- **Monitoring & Evaluation** — 4 reference files (results-frameworks-and-indicators.md, evaluation-design-and-methods.md, monitoring-systems-and-reporting.md, impact-evaluation-and-economic-analysis.md)
- **Stakeholder Engagement** — 3 reference files (stakeholder-analysis-and-mapping.md, stakeholder-engagement-and-communication.md, stakeholder-dynamics-and-influence.md)

**Remaining:** 5 domains still have no reference files:
1. Capacity Building
2. Gender and Social Inclusion (GESI)
3. Environmental and Social Safeguards
4. Data Management
5. Sustainability Planning

**Effort remaining:** ~1,500 lines across 5–10 files. Estimated 5 sessions.

---

### C2. PPDA Uganda Procurement Skill Missing — CLOSED

**Gap:** No SKILL.md or reference files for Uganda's Public Procurement and Disposal of Public Assets Act.

**Resolution:** Created `sectors/ppda-uganda/SKILL.md` + 2 reference files (ppda-evaluation-forms-and-procedures.md, ppda-act-and-regulatory-framework.md). Total: 1,251 lines covering procurement methods, 3-stage evaluation procedures, scoring formulae, two-envelope process, contract management, preference schemes, complaints mechanism, and detailed guidance for Forms 14/15/16/24/26/45/49.

---

### C3. No Evaluation Scoring Guidance Across Sections — OPEN

**Gap:** Only sections 05 (relevant experience) and 07 (team composition) mention evaluation weighting. The remaining 8 sections provide no guidance on what percentage of total score they carry or what evaluators prioritise.

**Impact:** Cannot optimise effort allocation across proposal sections. A firm might spend equal time on all sections when, in a QCBS evaluation, methodology (section 06) might carry 40% while the cover letter (section 01) carries 0%.

**Remediation:** Add an "Evaluation Scoring" subsection to every section SKILL.md with:
- Typical weight range by procurement framework (World Bank QCBS, PPDA, UNDP, AfDB)
- What evaluators look for in this specific section
- Common point-losing mistakes
- How to maximise score within page/time constraints

**Effort:** ~15 lines per section x 10 sections = ~150 lines. 0.5 session.

---

### C4. No Worked Weak-vs-Strong Examples — OPEN

**Gap:** No section skill contains side-by-side examples of weak vs strong writing. Templates exist but calibration examples do not.

**Impact:** Claude cannot distinguish between "adequate" and "excellent" output. Without calibration examples, the skill says "be specific" but does not show what specific looks like compared to generic.

**Remediation:** Add 2–3 weak-vs-strong comparison pairs per section skill. Focus on sections where quality variance is highest: 02 (executive summary), 03 (understanding), 05 (relevant experience), 06 (methodology).

**Effort:** ~30 lines per section x 10 sections = ~300 lines. 1 session.

---

### C5. Three Core Sector Skills Empty (ICT, Health, Governance) — PARTIALLY CLOSED

**Gap:** The three most common sectors for East African consulting assignments had no content.

**Progress:** All three sectors now have Uganda-specific reference data (created during the sector population work). However, they still lack generic sector SKILL.md files with methodology guidance, standard terminology, key stakeholders, and evaluation criteria patterns.

**Re-scoped:** This gap now applies to all 9 sectors (ICT, Health, Governance, Agriculture, Education, Energy, Water/Sanitation, Financial Services, Transport/Infrastructure). Each needs a SKILL.md (~200 lines) covering:
- Sector terminology and standard frameworks
- Common assignment types and methodology patterns
- Key stakeholders and institutional landscape
- Evaluation criteria specific to the sector
- East African context and regional considerations

**Effort remaining:** ~1,800 lines across 9 files. 3–4 sessions.

---

### C6. World Bank FIN-1–4 Form Templates Missing — OPEN

**Gap:** Section 10 (financial proposal) references World Bank FIN forms but does not include their structure. The `sectors/world-bank/` skill covers TECH forms but not FIN forms.

**Impact:** Cannot generate World Bank-compliant financial proposals without external reference.

**Remediation:** Add FIN-1–4 form structures to either `10-financial-proposal/references/` or `sectors/world-bank/references/`.

**Effort:** ~100 lines. 0.5 session.

---

### C7. No Procurement Framework Decision Tree — OPEN

**Gap:** No guidance on which procurement framework applies to a given ToR, or how to detect the framework from document cues.

**Impact:** A consultant receiving a ToR must manually determine whether it follows World Bank, PPDA, UNDP, AfDB, or direct client rules. Wrong framework = wrong format = disqualification.

**Remediation:** Add a "Procurement Framework Detection" section to the parent SKILL.md or create a standalone reference file with:
- Document cues that indicate each framework (logo, standard clauses, form numbers)
- Decision tree: funding source → procurement framework → template set
- Compliance checklist per framework

**Effort:** ~80 lines. 0.5 session.

---

### C8. No Pre-Submission Quality Gate — OPEN

**Gap:** No cross-section consistency check. Nothing ensures the methodology is consistent with the work plan, that the financial proposal matches the staffing schedule, or that all ToR requirements are addressed.

**Impact:** Internal inconsistencies are the most common reason proposals lose points. A methodology that promises 5 phases but a work plan showing 4 phases signals sloppiness.

**Remediation:** Add a "Pre-Submission Checklist" to the parent SKILL.md covering:
- Section-to-section consistency checks (methodology <> work plan <> financial <> staffing)
- ToR requirement traceability (every ToR item addressed)
- Formatting compliance (page limits, required forms, annexes)
- Language quality check (run east-african-english standards)
- Red Team review trigger

**Effort:** ~60 lines. 0.5 session.

---

### C9. No Cross-Section Theme Consistency — OPEN

**Gap:** Each section skill operates independently. No mechanism ensures that the "win themes" identified in section 02 (executive summary) are woven through sections 03, 06, 07, and the cover letter.

**Impact:** McKinsey and Deloitte proposals have 3–4 themes that appear in every section. Without theme threading, each section reads as standalone rather than as part of a coherent argument.

**Remediation:** Add "Theme Threading" guidance to:
- Section 02 (executive summary) — define the 3–4 win themes
- Parent SKILL.md — require theme list to be established before writing any section
- Each section SKILL.md — add a "Theme Integration" note showing how themes manifest in that section

**Effort:** ~100 lines spread across files. 1 session.

---

### C10. M&E Scoring Criterion Depth — CLOSED

**Gap:** M&E was a mandatory scored criterion in World Bank, UNDP, and most donor ToRs. The M&E skill (97 lines, no references) could not generate content that scores in the top band.

**Resolution:** Created 4 comprehensive reference files totalling 1,351 lines:
- results-frameworks-and-indicators.md — results chains, problem trees, ToC, CREAM indicators, RRF, sector indicators
- evaluation-design-and-methods.md — evaluation types, OECD-DAC criteria, impact evaluation designs, sampling, data quality
- monitoring-systems-and-reporting.md — monitoring plans, M&E governance, digital tools, RAG reporting, adaptive management, costed M&E plans
- impact-evaluation-and-economic-analysis.md — ATE/ITT/ATT/LATE, RCT designs, quasi-experimental methods, CBA, shadow pricing, distributional analysis

M&E is now one of the strongest domain skills in the repository.

---

### C11. GESI Scoring Criterion Depth — OPEN

**Gap:** GESI is increasingly a mandatory scored criterion (5–15% of total score in UNDP, rising in World Bank and AfDB). The current GESI skill (77 lines, no references) produces generic commitments rather than substantive analysis.

**Impact:** Weak GESI = automatic point loss in donor-funded work. Evaluators specifically check for intersectionality, gender budgeting, and measurable gender outcomes. AfDB's gender marker system (GG/GM/SGI/NGE) and UNDP's gender mainstreaming requirements make this the most critical remaining domain gap.

**Remediation:** Create 1–2 reference files (~300 lines) covering:
- Gender analysis frameworks (Harvard, Moser, Gender at Work)
- Intersectionality and disability inclusion
- Gender budgeting and gender-responsive M&E
- AfDB gender marker alignment
- UNDP/World Bank gender mainstreaming requirements
- Youth inclusion and age-disaggregated indicators

**Effort:** ~300 lines. 1 session (priority #1 in remaining domain work).

---

### C12. AfDB Procurement Skill Missing — CLOSED

**Gap:** No SKILL.md or references for African Development Bank procurement.

**Resolution:** Created `sectors/afdb/SKILL.md` + 3 reference files totalling 1,233 lines:
- procurement-and-consultant-selection.md — procurement methods (OCB/LCB/direct/community), QCBS/QBS/FBS/LCS/CQS/SSS detailed procedures, EoI requirements, RFP structure, contract types, negotiation, complaints, eligibility
- safeguards-and-financial-terms.md — ISS 2023, all 10 Operational Safeguards, project categorisation, ESIA process, ADB/ADF lending terms, climate finance (40% target), gender mainstreaming
- project-cycle-and-evaluation.md — project cycle phases, PCR structure, IDEV framework, OECD-DAC criteria, 4-point rating scale, sustainability sub-factors

---

## High Gaps (6 items)

### H1. Remaining 6 Sector Skills Empty — PARTIALLY CLOSED

Agriculture, education, energy, water/sanitation, financial services, and transport/infrastructure directories were stubs.

**Progress:** All 9 sector directories (including ICT, Health, Governance) now have Uganda-specific reference data. However, none have generic SKILL.md files with methodology guidance, terminology, and evaluation criteria.

**Reclassified:** This gap is now merged with the re-scoped C5. The 9 sector SKILL.md files are tracked there.

---

### H2. Thin Sections in Cross-Cutting References — OPEN

Sections 9–13 in world-class-proposal-patterns.md and sections 11–15 in consulting-delivery-excellence.md average ~6 lines each.

**Remediation:** Expand each thin section to ~15–20 lines. Total ~100 lines of additions.

---

### H3. Section 01 (Cover Letter) Underdeveloped — OPEN

At 81 lines with no references, cross-references, or procurement variants, this is the weakest numbered section skill.

**Remediation:** Expand to ~150 lines with procurement-specific guidance, strong-vs-weak opener examples, and compliance statement templates.

---

### H4. Section 09 (EoI) Lacks Procurement Variants — OPEN

EoI structure varies significantly by procurement framework (World Bank shortlisting, PPDA two-stage, UNDP RFP, AfDB). Current skill is generic.

**Remediation:** Add procurement variant structures (~50 lines).

---

### H5. No Sector-Specific Project Card Libraries — OPEN

Relevant experience (section 05) requires project cards, but there is no pre-built library of cards by sector.

**Remediation:** Create sector-specific project card templates showing what "excellent" outcome statements look like in each domain.

---

### H6. Operations Frameworks File Lighter Than Siblings — OPEN

`consulting-frameworks/references/operations-frameworks.md` (155 lines) is thinner than the other 4 framework files (164–222 lines).

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

### L3. Blog Skills Disproportionately Large

Originally 22% of content vs 7% for proposal sections. Now approximately 14% — the proportion has naturally improved as total content grew by 52% (+8,870 lines) while blog content stayed constant. No longer a priority concern.

---

## Remediation Roadmap

### Completed Work (Sessions 5–10)

| # | Action | Result | Lines |
|---|--------|--------|-------|
| C1 (partial) | Change Management reference files | 3 files created | ~720 |
| C1 (partial) | M&E reference files | 4 files created (incl. impact evaluation) | ~1,351 |
| C1 (partial) | Stakeholder Engagement reference files | 3 files created | ~930 |
| C2 | PPDA Uganda procurement skill | SKILL.md + 2 reference files | ~1,251 |
| C10 | M&E scoring criterion depth | Resolved via C1 M&E work | (counted above) |
| C12 | AfDB procurement skill | SKILL.md + 3 reference files | ~1,233 |
| — | Financial proposal references | budgeting-and-cost-estimation.md | ~500 |
| — | Project management references | project-controls-and-earned-value.md | ~450 |
| — | Risk management references | risk-quantification-and-response.md | ~270 |
| — | Consulting frameworks enhancement | 5 reference files expanded | ~400 |
| — | Cross-cutting references | consulting-delivery-excellence.md, business-analysis-tools expanded | ~1,765 |
| | **Completed Total** | | **~8,870** |

### Phase 2 — Competitive (target: 92% readiness)

| # | Action | Files | Lines | Sessions |
|---|--------|-------|-------|----------|
| C1 | 5 remaining domain skill reference files (Capacity Building, GESI, Safeguards, Data Management, Sustainability) | 5–10 new files | ~1,500 | 5 |
| C5 | 9 sector SKILL.md files (generic methodology, terminology, stakeholders, evaluation criteria) | 9 new files | ~1,800 | 3–4 |
| C3 | Evaluation scoring guidance across all 10 section skills | 10 edits | ~150 | 0.5 |
| C4 | Weak-vs-strong examples for key sections | 10 edits | ~300 | 1 |
| C6+C7+C8 | WB FIN-1–4 templates + procurement decision tree + quality gate | 2–3 new/edits | ~240 | 1 |
| | **Phase 2 Total** | | **~3,990** | **~10** |

Phase 2 priority order:
1. GESI reference files (C11 — most critical remaining domain gap)
2. Remaining 4 domain skill reference files (C1)
3. 9 sector SKILL.md files (C5)
4. Evaluation scoring guidance (C3)
5. Weak-vs-strong examples (C4)
6. WB FIN-1–4, procurement decision tree, quality gate (C6/C7/C8)

### Phase 3 — World-Class (target: 98% readiness)

| # | Action | Files | Lines | Sessions |
|---|--------|-------|-------|----------|
| C9 | Cross-section theme threading mechanism | ~6 edits | ~100 | 1 |
| M1 | Full worked proposal example | 10 new files | ~1,500 | 4 |
| M2 | Multi-currency pricing guidance | 1 edit | ~30 | 0.5 |
| M3 | JV/consortium guidance | 2 edits | ~60 | 0.5 |
| M4 | EU/JICA/FCDO procurement frameworks | 3 new files | ~600 | 3 |
| H2 | Expand thin reference sections | 2 edits | ~100 | 0.5 |
| H3 | Expand cover letter skill | 1 edit | ~70 | 0.5 |
| H4 | EoI procurement variants | 1 edit | ~50 | 0.5 |
| H5 | Project card libraries | 3 new files | ~300 | 1.5 |
| H6 | Expand operations frameworks | 1 edit | ~60 | 0.5 |
| M5 | Formatting and layout guide | 1 new file | ~150 | 1 |
| L1–3 | Polish items | Various | ~100 | 1 |
| | **Phase 3 Total** | | **~3,120** | **~10** |

---

## Total Remediation Effort

| Phase | New Lines | Sessions | Cumulative Readiness |
|-------|-----------|----------|---------------------|
| Original state | 17,200 | — | 65–70% |
| **Completed (Sessions 5–10)** | **+8,870** | **6** | **80–82%** |
| Phase 2 (remaining) | +3,990 | ~10 | 92% |
| Phase 3 | +3,120 | ~10 | 98% |
| **Total target** | **~33,180** | — | **98%** |

Final repository size after all phases: ~33,000 lines of documented knowledge.
