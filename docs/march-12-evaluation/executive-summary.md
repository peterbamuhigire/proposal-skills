# Executive Summary — Repository Completeness Evaluation

**Date:** 12 March 2026
**Repository:** proposal-skills
**Owner:** Peter Bamuhigire / Chwezi Core Systems Limited

---

## The Verdict

**Overall readiness: 65–70% of what is needed for consistent million-dollar wins.**

The repository has an **excellent architecture and strong strategic foundations** — the persuasion layer, consulting frameworks, and proposal section skills are genuinely world-class in design. However, **significant depth gaps in domain skills and empty sector directories** mean the firm cannot yet produce proposals that consistently match the depth and specificity of McKinsey, Bain, EY, or Deloitte across all assignment types.

### What Is World-Class Today

| Area | Lines | Assessment |
|------|-------|------------|
| Proposal architecture (10 numbered sections) | 1,150 | Sound structure, good cross-linking, clear procurement awareness |
| Persuasion and strategy references | 1,560 | Exceptional — synthesises 22 books into actionable frameworks |
| Consulting frameworks library | 946 | Best-in-class problem structuring, financial analysis, communication |
| Business analysis tools | 1,509 | Comprehensive strategic analysis from SWOT through Power Curve |
| Financial proposal + budgeting reference | 654 | Practical day rates, risk contingency formula, budget methodology |
| Project management + earned value | 501 | Solid PM frameworks with quantitative project controls |
| Risk management + quantification | 402 | Strong risk register, FMEA/RPN scoring, East African risk examples |
| Profile system | 396 | Excellent — three profiles with clear voice rules and routing |
| World Bank procurement | 720 | Exceptional scoring strategy and form-by-form guidance |
| UNDP/UN system procurement | 1,373 | Comprehensive across 5 UN modalities |
| Language standards | 667 | Thorough British English, French, Kiswahili with AI-language detection |
| Blog writing skills | 3,757 | Mature and production-ready (separate from proposals) |

**Total documented knowledge: ~17,000 lines across 34 skills and 39 reference files.**

### What Falls Short

| Gap | Current State | Impact on $1M+ Proposals |
|-----|---------------|--------------------------|
| **8 domain skills lack reference files** | SKILL.md only (77–103 lines each) | Sections on change management, M&E, GESI, safeguards read as competent but not compelling |
| **9 of 11 industry sectors are empty** | Directory stubs only | Cannot tailor proposals to sector-specific evaluation criteria or terminology |
| **PPDA Uganda and AfDB procurement** | Empty directories | Cannot optimise scoring for Uganda's national procurement or AfDB-funded work |
| **No worked proposal examples** | Templates exist but no full walkthrough | Cannot demonstrate end-to-end quality or train Claude on what "excellent" looks like |
| **Weak-vs-strong language comparisons** | Absent across all sections | Cannot calibrate quality beyond "follow the rules" |
| **Evaluation scoring guidance** | Partial (only sections 05 and 07 have explicit weighting) | Cannot optimise point allocation across proposal sections |

### The Gap Between "Competent" and "Compelling"

A McKinsey or Deloitte proposal for a $1M+ assignment includes:

- **Change management** sections citing specific organisational readiness assessment tools, resistance pattern analysis, and change saturation models — not just "we will use ADKAR"
- **M&E frameworks** with impact evaluation designs, counterfactual analysis, and mixed-methods rigour — not just a logframe
- **GESI** with intersectionality analysis, gender budgeting, and women's agency measurement — not just "we will disaggregate data by sex"
- **Stakeholder engagement** with political economy analysis, conflict mapping, and salience assessment — not just a power-interest matrix
- **Sector-specific language** that shows the firm lives and breathes that sector — not generic consulting speak

This repository gives Claude the *architecture* to produce such proposals but not always the *depth*. The SKILL.md files tell Claude what sections to write; they do not always give Claude enough substance to write them at the level that wins against top-tier competition.

---

## Readiness by Proposal Type

| Proposal Type | Readiness | Notes |
|---------------|-----------|-------|
| **World Bank QCBS** (consulting services) | **80%** | Strong TECH-form guidance, scoring strategy, good methodology skill. Missing: FIN-1–4 form templates |
| **UNDP/UN system** (consulting RFPs and grants) | **75%** | Good coverage of 5 modalities, scoring bands. Missing: sector-specific content |
| **PPDA Uganda** (national procurement) | **40%** | No PPDA-specific skill. Generic proposal structure applies but cannot optimise for PPDA evaluation criteria |
| **AfDB** | **35%** | Empty directory. ESF standards mentioned in safeguards skill but no procurement-specific guidance |
| **Direct client RFPs** (private sector, NGOs) | **70%** | Flexible proposal structure works well. Missing: client-type tone differentiation |
| **ICT sector assignments** | **55%** | Methodology skill has ICT phase variants. Missing: sector skill with ICT terminology, frameworks, evaluation patterns |
| **Health, agriculture, governance sectors** | **40%** | No sector-specific content. Generic frameworks only |
| **Capacity building-focused assignments** | **55%** | Capacity building skill exists but lacks depth. No learning outcomes framework or ROI measurement |
| **M&E-focused assignments** | **50%** | Basic logframe and ToC covered. No impact evaluation designs or mixed-methods rigour |

---

## Recommendation

### Phase 1 — Critical (closes the gap to 85%)
1. Create reference files for all 8 domain skills that lack them (200–350 lines each)
2. Populate the 3 most common sector directories (ICT, Health, Governance)
3. Create the PPDA Uganda procurement skill
4. Add evaluation weighting guidance to all 10 proposal section skills

### Phase 2 — Competitive (closes the gap to 92%)
5. Create worked proposal examples (weak vs strong) for each section
6. Populate remaining sector directories (Agriculture, Education, Energy, Water, Transport, Financial Services)
7. Create AfDB procurement skill
8. Add World Bank FIN-1–4 form templates

### Phase 3 — World-Class (closes the gap to 98%)
9. Build a complete anonymised example proposal showing all 10 sections
10. Create sector-specific project card libraries
11. Add Monte Carlo simulation guidance to risk management
12. Create a proposal quality scoring checklist that mirrors evaluator rubrics

**Estimated effort for Phase 1:** 8–12 focused sessions.
**Impact:** Moves the repository from "competent mid-tier" to "credibly competing with the Big Four for $1M+ work."
