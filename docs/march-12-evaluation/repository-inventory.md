# Repository Inventory — Complete File Audit

**Date:** 12 March 2026 (updated after Phase 1 remediation sessions 6–10)

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| SKILL.md files | 36 |
| Lines across all SKILL.md files | 6,035 |
| Reference .md files | 63 |
| Lines across all reference files | 19,700 |
| Profile files (proposer identities) | 4 |
| Lines across profile files | 399 |
| Python utility scripts | 3 |
| **Total documented knowledge** | **~26,070 lines** |

---

## 1. Proposal Section Skills (01–10)

| # | Directory | SKILL.md Lines | Reference Files | Reference Lines | Status |
|---|-----------|---------------|-----------------|-----------------|--------|
| 01 | cover-letter | 81 | 0 | 0 | No references/ directory |
| 02 | executive-summary | 97 | 0 | 0 | references/ empty (.gitkeep) |
| 03 | understanding-of-assignment | 204 | 0 | 0 | references/ empty (.gitkeep) |
| 04 | firm-profile | 87 | 0 | 0 | references/ empty (.gitkeep) |
| 05 | relevant-experience | 72 | 0 | 0 | No references/ directory |
| 06 | methodology | 177 | 0 | 0 | No references/ directory (uses external refs) |
| 07 | team-composition | 128 | 0 | 0 | references/ empty (.gitkeep) |
| 08 | work-plan | 95 | 0 | 0 | references/ empty (.gitkeep) |
| 09 | expression-of-interest | 75 | 0 | 0 | references/ empty (.gitkeep) |
| 10 | financial-proposal | 134 | 1 | 520 | budgeting-and-cost-estimation.md |
| | **Subtotal** | **1,150** | **1** | **520** | |

---

## 2. Supporting Domain Skills

| Directory | SKILL.md Lines | Reference Files | Reference Lines | Status |
|-----------|---------------|-----------------|-----------------|--------|
| project-management | 145 | 1 | 356 | project-controls-and-earned-value.md |
| risk-management | 170 | 1 | 232 | risk-quantification-and-response.md |
| business-analysis-tools | 312 | 7 | 1,509 | Full library (see below) |
| consulting-frameworks | 43 | 5 | 946 | Full library (see below) |
| change-management | 99 | 3 | 648 | 3 new reference files (see below) |
| monitoring-and-evaluation | 97 | 4 | 1,351 | 4 new reference files (see below) |
| stakeholder-engagement | 77 | 3 | 1,031 | 3 new reference files (see below) |
| capacity-building | 95 | 0 | 0 | references/ empty |
| gender-and-social-inclusion | 77 | 0 | 0 | references/ empty |
| environmental-and-social-safeguards | 105 | 0 | 0 | references/ empty |
| data-management | 102 | 0 | 0 | references/ empty |
| sustainability-planning | 103 | 0 | 0 | references/ empty |
| **Subtotal** | **1,425** | **24** | **6,073** | |

### business-analysis-tools/references/ (7 files)

| File | Lines |
|------|-------|
| strategic-analysis-frameworks.md | 423 |
| diagnostic-tools.md | ~200 |
| root-cause-analysis.md | ~150 |
| capability-assessment.md | ~120 |
| business-case-components.md | ~180 |
| portfolio-analysis.md | ~200 |
| ideation-frameworks.md | ~236 |
| **Total** | **~1,509** |

### consulting-frameworks/references/ (5 files)

| File | Lines |
|------|-------|
| problem-structuring.md | 165 |
| financial-analysis.md | 204 |
| strategy-frameworks.md | 222 |
| operations-frameworks.md | 156 |
| communication-structures.md | 202 |
| **Total** | **949** |

### change-management/references/ (3 files — NEW)

| File | Lines |
|------|-------|
| change-process-models.md | 171 |
| hard-and-soft-integration.md | 257 |
| lean-and-adaptive-change.md | 220 |
| **Total** | **648** |

### monitoring-and-evaluation/references/ (4 files — NEW)

| File | Lines |
|------|-------|
| results-frameworks-and-indicators.md | 260 |
| evaluation-design-and-methods.md | 309 |
| monitoring-systems-and-reporting.md | 248 |
| impact-evaluation-and-economic-analysis.md | 534 |
| **Total** | **1,351** |

### stakeholder-engagement/references/ (3 files — NEW)

| File | Lines |
|------|-------|
| stakeholder-analysis-and-mapping.md | 355 |
| stakeholder-engagement-and-communication.md | 330 |
| stakeholder-dynamics-and-influence.md | 346 |
| **Total** | **1,031** |

---

## 3. Cross-Cutting References

| File | Lines | Purpose |
|------|-------|---------|
| references/proposal-strategy-and-persuasion.md | 547 | Persuasion layer: S1→S2→B, P-I-P, SCQA, Cialdini, Red Team |
| references/world-class-proposal-patterns.md | 315 | McKinsey/Deloitte patterns: storyboarding, Sweet Spot, elevator test |
| references/consulting-delivery-excellence.md | 701 | 34 delivery frameworks: McKinsey process, VRM, Design Thinking |
| **Subtotal** | **1,563** | |

---

## 4. Profiles

| File | Lines | Purpose |
|------|-------|---------|
| profiles/SKILL.md | 85 | Routing: which profile to load and when |
| profiles/peter-bamuhigire.md | 124 | Individual consultant (first-person singular) |
| profiles/chwezi-core-systems.md | 125 | Company (first-person plural) |
| profiles/client-template.md | 65 | Ghostwriting template |
| **Subtotal** | **399** | |

---

## 5. Sectors

### Populated Sectors — Procurement Frameworks

| Directory | SKILL.md Lines | Reference Files | Reference Lines | Total |
|-----------|---------------|-----------------|-----------------|-------|
| sectors/SKILL.md (router) | 79 | — | — | 79 |
| sectors/world-bank | 233 | 2 | 508 | 741 |
| sectors/undp | 341 | 4 | 964 | 1,305 |
| sectors/ppda-uganda | 182 | 2 | 1,069 | 1,251 |
| sectors/afdb | 186 | 3 | 1,047 | 1,233 |
| **Framework subtotal** | **1,021** | **11** | **3,588** | **4,609** |

### Populated Sectors — Uganda Country and Industry References

| File | Lines | Purpose |
|------|-------|---------|
| sectors/uganda-country-profile.md | 161 | Cross-sector Uganda context |
| sectors/agriculture/references/uganda-agriculture-sector.md | 118 | Agriculture sector profile |
| sectors/education/references/uganda-education-sector.md | 81 | Education sector profile |
| sectors/energy/references/uganda-energy-sector.md | 82 | Energy sector profile |
| sectors/financial-services/references/uganda-financial-sector.md | 110 | Financial services sector profile |
| sectors/governance/references/uganda-governance-sector.md | 92 | Governance sector profile |
| sectors/health/references/uganda-health-sector.md | 82 | Health sector profile |
| sectors/ict/references/uganda-ict-sector.md | 101 | ICT sector profile |
| sectors/transport-infrastructure/references/uganda-transport-sector.md | 113 | Transport infrastructure sector profile |
| sectors/water-sanitation/references/uganda-wash-sector.md | 65 | WASH sector profile |
| **Industry subtotal** | **1,005** | |

**Sector total: 5,614 lines across 22 files.**

### Empty Sector Directories

**0 empty directories.** All 9 industry sectors now have at least one Uganda-specific reference file, and all 4 procurement frameworks (World Bank, UNDP/UN System, PPDA Uganda, AfDB) are fully built.

---

## 6. Language Skills

| File | Lines | Purpose |
|------|-------|---------|
| east-african-english/SKILL.md | 197 | British spelling, tone, courteous phrasing |
| language-standards/SKILL.md | 470 | English, French, Kiswahili standards + AI-language detection |
| **Subtotal** | **667** | |

---

## 7. Content Creation Skills

| Directory | SKILL.md Lines | Reference Files | Reference Lines | Total |
|-----------|---------------|-----------------|-----------------|-------|
| blog-writer | 469 | 9 | 2,618 | 3,087 |
| blog-idea-generator | 241 | 2 | 429 | 670 |
| **Subtotal** | **710** | **11** | **3,047** | **3,757** |

---

## 8. Meta/Utility Skills

| Directory | SKILL.md Lines | Reference Files | Reference Lines |
|-----------|---------------|-----------------|-----------------|
| skill-writing | 520 | 4 | 1,524 |
| skill-safety-audit | 121 | 0 | 0 |
| update-claude-documentation | 201 | 0 | 0 |
| **Subtotal** | **842** | **4** | **1,524** |

---

## 9. Root Files

| File | Lines | Purpose |
|------|-------|---------|
| SKILL.md | 136 | Parent routing skill |
| CLAUDE.md | 155 | Project instructions for Claude Code |
| README.md | 264 | Repository documentation |
| .gitignore | ~5 | Ignores proposals/ |

---

## Content Distribution

```
Sector skills + references:  5,609 lines ( 22%)  ████████████
Domain references:           6,073 lines ( 23%)  █████████████
Blog skills + references:    3,757 lines ( 14%)  ████████
Meta/utility skills:         2,366 lines (  9%)  █████
Cross-cutting references:    1,563 lines (  6%)  ███
Domain skills:               1,425 lines (  5%)  ███
Proposal section skills:     1,150 lines (  4%)  ██
Language skills:               667 lines (  3%)  ██
Profiles + routing:            535 lines (  2%)  █
Root files:                    555 lines (  2%)  █
                            ──────
                            ~26,070 lines (100%)
```

### Key Observations

1. **Sector content is now the largest category** (5,609 lines, 22%) — up from 2,125 lines (12%) before remediation. All 4 procurement frameworks are complete and all 9 industry sectors have Uganda-specific reference files.

2. **Domain references have nearly doubled** (6,073 lines, 23%) — up from 3,043 lines (18%). Change management, monitoring and evaluation, and stakeholder engagement now have comprehensive reference libraries synthesised from 67 source documents.

3. **Blog writing skills** (3,757 lines, 14%) are no longer the largest category — they have been overtaken by both domain references and sector content. This reflects the repository's shift towards proposal-centric depth.

4. **Remaining gaps:** Only 1 of 10 proposal section skills has a reference file (financial-proposal). Five of 12 domain skills still lack references: capacity-building, gender-and-social-inclusion, environmental-and-social-safeguards, data-management, and sustainability-planning. These are Phase 2 priorities.
