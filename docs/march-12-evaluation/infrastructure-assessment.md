# Infrastructure Assessment — Profiles, Sectors, Language, Procurement

**Date:** 12 March 2026

---

## 1. Proposer Profile System — EXCELLENT

**Directory:** `profiles/`

### Files

| File | Lines | Purpose |
|------|-------|---------|
| SKILL.md | 85 | Routing: determines which profile to load |
| peter-bamuhigire.md | 124 | Individual consultant (first-person singular) |
| chwezi-core-systems.md | 125 | Company (first-person plural) |
| client-template.md | 65 | Ghostwriting for clients |

### Assessment

The profile system is well-designed and comprehensive:

- **Routing logic** is clear — SKILL.md explains when to use each profile
- **Peter Bamuhigire profile** has substantial detail: education, 7 professional positions, 12 key projects with quantified outcomes, qualifications, 9 differentiators
- **Chwezi Core Systems profile** mirrors Peter's structure with institutional depth: legal status, service areas, 3 proprietary SaaS products, 11 key projects, 9 differentiators
- **Client template** is thorough and fill-in-ready
- **Voice rules** are clear (singular for Peter, plural for Chwezi)
- **Growth mechanism** included — profiles are living documents
- **Association arrangements** section for future teaming

### Minor Gaps

- No guidance on updating profiles mid-proposal (if new project completes during drafting)
- No conflict-of-interest checking rules
- No ethical limits guidance (overstating experience, hiding bad references)
- Associates/sub-consultant pool not populated — this matters for large assignments requiring team augmentation

### Verdict

**Production-ready.** The profile system would work for any proposal type today.

---

## 2. Sector Procurement Frameworks — PARTIAL

### Populated Frameworks

#### World Bank (720 total lines) — EXCELLENT

**SKILL.md (233 lines):**
- Selection methods (QCBS, QBS, FBS, LCS, CQS, SSS) with implications for each
- Two-envelope procedure and 75-point survival threshold
- TECH forms 1–8 mapping to proposal sections
- Evaluation criteria and point allocations
- Scoring scale (0–4 per sub-criterion with descriptors)
- Combined scoring formula with worked example
- Scoring strategy per section (TECH-3, TECH-4, TECH-5/6, FIN)
- Minimum threshold rules
- Process timeline (GPN → REoI → RFP → submission → evaluation → award)
- Conflict of interest rules

**Reference files:**
- `evaluation-scoring-guide.md` (206 lines) — point allocation, sub-criteria weighting, scoring examples
- `tech-fin-forms-guide.md` (304 lines) — form-by-form completion guidance

**Verdict:** Exceptional. Detailed, formulaic, with worked examples. Directly usable as a scoring maximisation guide. This is the gold standard for how sector procurement skills should be built.

#### UNDP/UN System (1,373 total lines) — EXCELLENT

**SKILL.md (341 lines):**
- Key differences from World Bank (standardisation, instruments, scoring, price formulas)
- UN system instrument types (5 modalities: competitive grants, GEF SGP, UN Trust Funds, consulting RFPs, direct procurement)
- UN system-wide rules (tax exemption, IPR ownership, sanctions, conflict of interest)
- Evaluation criteria patterns (methodology 40–50%, experience 20–30%, GESI 5–15%)
- Three-tier scoring bands (Band 1: somewhat, Band 2: mostly, Band 3: fully)
- Scoring strategy by section
- Administrative compliance as pass/fail gate
- Co-financing as strategic differentiator
- Government endorsement for NGO applicants
- Page limits and formatting

**Reference files (4):**
- `competitive-grants-guide.md` (184 lines)
- `gef-sgp-guide.md` (253 lines)
- `un-trust-funds-guide.md` (267 lines)
- `un-consulting-rfp-guide.md` (260 lines)

**Verdict:** Excellent. Comprehensive across 5 modalities. Three-tier scoring explanation is particularly actionable. Note: directory named `undp/` but SKILL.md covers the full UN system.

### Empty Procurement Frameworks

| Directory | Impact | Priority |
|-----------|--------|----------|
| **ppda-uganda/** | **High** — PPDA is the most common procurement framework for Uganda government work. Cannot optimise for PPDA evaluation criteria without this. | **Critical** |
| **afdb/** | **Medium** — AfDB-funded projects are significant in East Africa. ESF standards mentioned in safeguards skill but no procurement guidance. | **High** |

### Missing Procurement Frameworks

Not currently in the directory structure but relevant:

- **EU/EuropeAid** — Significant funder in East Africa; different procurement rules (PRAG)
- **JICA** — Active in East African infrastructure; own procurement guidelines
- **DFID/FCDO** — British aid procurement; relevant for Uganda/Kenya/Tanzania
- **GIZ** — German development cooperation; active in East Africa

---

## 3. Industry Sector Skills — EMPTY

All 9 industry sector directories contain only .gitkeep:

| Directory | Common Assignment Types | Impact of Gap |
|-----------|------------------------|---------------|
| **ict/** | Systems assessment, digital transformation, MIS design | **High** — Chwezi's core sector |
| **health/** | Health systems strengthening, HMIS, supply chain | **High** — major donor-funded sector |
| **governance/** | Public sector reform, PFM, anti-corruption, decentralisation | **High** — common in Uganda |
| **agriculture/** | Value chain, food security, extension services | **Medium** — frequent ToRs |
| **education/** | Education management, teacher training, EMIS | **Medium** |
| **water-sanitation/** | WASH, utility management, water resource planning | **Medium** |
| **energy/** | Rural electrification, solar, grid extension | **Medium** |
| **financial-services/** | Fintech, microfinance, financial inclusion | **Medium** |
| **transport-infrastructure/** | Roads, logistics, urban transport | **Low** — less core to Chwezi |

### What Each Sector Skill Should Contain

Each populated sector skill should include:

1. **Sector terminology and concepts** — key terms evaluators expect to see
2. **Common assignment types** — what ToRs in this sector typically ask for
3. **Sector-specific frameworks** — analytical tools specific to this domain
4. **Key stakeholders** — typical institutional landscape
5. **Common challenges** — sector-specific risks and constraints
6. **Evaluation criteria patterns** — what donors weigh in this sector
7. **Sample deliverables** — what outputs look like in this sector
8. **Regional context** — East African sector-specific considerations

### Priority Order

1. **ICT** — core sector for Chwezi; most proposals will be here
2. **Governance** — common in Uganda government procurement
3. **Health** — largest donor-funded sector in East Africa
4. **Agriculture** — frequent ToRs from World Bank, UNDP, FAO
5. **Education** — significant sector with specific requirements
6. Remaining sectors as needed by specific proposals

---

## 4. Language Standards — EXCELLENT

### East African English (197 lines)

**Covers:**
- British English spelling rules (organisation, programme, centre, colour, travelling)
- Date format (17 February 2026, never American format)
- Tone by country (Uganda warm/relational, Kenya efficient/business, Tanzania calm/measured)
- 10 courteous phrases
- Vocabulary standards (preferred words, marketing hype to avoid, AI-sounding words to ban)
- Sentence style (full sentences, professional indirectness)
- Openings and closings
- Reference paragraph for tone benchmarking

### Language Standards (470 lines)

**Three-language coverage:**

1. **English** — British spelling, East African tone, dates/numbers, country-specific variations, assertive language, three-tier AI language ban (Tier 1 banned, Tier 2 overused, Tier 3 flagged combinations), hedging language, CTAs
2. **French** — Formal francophone (not Québécois), vous throughout, grammar rules, formal registers, courtesy phrases, francophone African terminology, text expansion factor (1.3x), in-country reviewer requirement
3. **Kiswahili** — Standard East African Kiswahili (not dialects), formal register, tense selection, courtesy phrases, text expansion (1.2x), in-country reviewer requirement

### Assessment

**The three-tier AI language detection system is particularly strong:**
- Tier 1 (Banned): delve, tapestry, landscape (metaphor), leverage, foster, realm, harness, synergy, embark, robust, vibrant, holistic, seamless
- Tier 2 (Overused): navigate (metaphor), comprehensive, innovative, cutting-edge
- Tier 3 (Flagged combinations): "in today's rapidly evolving…", "it is worth noting that…"

**Verdict:** Excellent. The language standards are thorough, practical, and enforce the East African professional tone that distinguishes Chwezi's proposals from generic consulting output.

### Minor Gaps

- No tone differentiation by client type (government vs private sector vs NGO vs donor)
- No comparison examples showing "East African tone" vs "generic professional" vs "marketing hype"
- Kiswahili speaker pool not pre-identified for review

---

## 5. Parent Routing Skill — GOOD

**File:** `SKILL.md` (136 lines, root directory)

### Assessment

The parent skill routes correctly to sub-skills based on document type and section requested. It defines cross-cutting standards that all sub-skills inherit:

- British English, East African tone
- First-person plural (or singular per profile)
- .docx output
- Profile loading requirement

### Minor Gaps

- No "pre-submission checklist" that validates all sections are consistent
- No guidance on section ordering or what to do when ToR requests non-standard sections
- No "quality gate" before compilation — nothing ensures methodology is consistent with work plan or that financial proposal matches staffing schedule

---

## Summary: Infrastructure Readiness

| Component | Status | Readiness |
|-----------|--------|-----------|
| Proposer profiles | 3 complete profiles + routing | **Production-ready** |
| World Bank procurement | SKILL.md + 2 references (720 lines) | **Production-ready** |
| UNDP/UN system procurement | SKILL.md + 4 references (1,373 lines) | **Production-ready** |
| PPDA Uganda procurement | Empty | **Not ready** |
| AfDB procurement | Empty | **Not ready** |
| Industry sectors (9) | All empty | **Not ready** |
| East African English | 197 lines | **Production-ready** |
| Language standards (EN/FR/SW) | 470 lines | **Production-ready** |
| Parent routing skill | 136 lines | **Production-ready** |
| Proposal workspace system | Defined in CLAUDE.md | **Production-ready** |
