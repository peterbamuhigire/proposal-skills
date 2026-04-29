---
name: sectors
description: Sector and procurement framework reference index. Use when writing proposals to load sector-specific requirements, terminology, evaluation criteria, and compliance rules. Read this index first, then read the relevant sector file before drafting any proposal section.
---

# Sectors — Index
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When
- Use this skill when a proposal needs both procurement-framework guidance and sector-domain context.
- Load it when you must decide which procurement and sector skills to read before drafting.

## Do Not Use When
- The task is only language editing or proposer-profile selection.
- A specific sector and framework skill have already been chosen and no routing help is needed.

## Required Inputs
- The ToR, RFP, advert, or client brief.
- Known donor, geography, industry, and form requirements.
- Any clues about evaluation criteria, selection method, and terminology.

## Workflow
1. Identify the procurement framework first because it controls forms, scoring, and compliance rules.
2. Identify the industry sector next because it shapes terminology, methodology, and evaluator expectations.
3. Load one procurement skill and one or more sector skills as needed for the assignment.
4. Read country context where it materially improves the proposal.
5. Carry those assumptions into the numbered proposal section skills.

## Quality Standards
- Use procurement skills for compliance logic and sector skills for domain logic.
- Prefer the smallest relevant set of context files so the proposal stays focused.
- Treat sector references as evidence and framing support, not text to paste verbatim.

## Anti-Patterns
- Do not assume the donor framework from sector keywords alone.
- Do not load every sector reference when only one or two are relevant.
- Do not ignore country context when the bid is explicitly country-specific.

## Outputs
- A routing decision to the relevant procurement and sector skills.

## References
- Local framework and sector subdirectories.
- `uganda-country-profile.md` when Uganda context matters.

This directory contains reference documentation for procurement frameworks and industry sectors. Each file defines the specifics that apply when writing proposals for that context — mandatory forms, evaluation weightings, compliance requirements, terminology, and sector-specific content expectations.

## How to Use

1. Identify the procurement framework (how the bid must be structured)
2. Identify the industry sector (what the bid is about)
3. Read both files before drafting any proposal section
4. A single proposal may reference one framework + one or more sectors

---

## Procurement Frameworks

These define **how** bids must be packaged, what forms are required, and how they are evaluated.

| Directory | Framework | Coverage |
|---|---|---|
| `ppda-uganda/` | Public Procurement and Disposal of Public Assets Authority | Ugandan public sector bids — mandatory forms, evaluation criteria, reserved schemes, domestic preference rules |
| `world-bank/` | World Bank Procurement | TECH-1–6 and FIN-1–4 standard forms, QCBS/QBS/FBS/LCS selection methods, conflict of interest rules |
| `afdb/` | African Development Bank | AfDB consultant selection methods (QCBS/QBS/FBS/LCS/CQS/SSS), Integrated Safeguards System (ISS 2023, 10 Operational Safeguards), project categorisation, IDEV evaluation framework, ADB/ADF lending terms, climate and gender mainstreaming |
| `undp/` | United Nations Development Programme | UN procurement processes, UNGM registration, financial proposal format |

---

## Country Profile

| File | Coverage |
|---|---|
| `uganda-country-profile.md` | Cross-cutting Uganda development context from AfDB CDN December 2025 and UN Country Analysis 2025 — demographics, macroeconomic indicators (GDP USD 53.7bn, pop 45.9m), development frameworks (Vision 2040, NDP IV), structural transformation, poverty/inequality (HDI 0.582, multidimensional poverty 42.1%), employment, gender (GII 0.524), climate (41% land degraded, INFORM 12/191), governance, financial sector, trade, statistics, fragility, and 10 SDG acceleration pathways. Load this before writing any Uganda-targeted proposal. |

---

## Industry Sectors

These define **what** evaluators expect in terms of domain knowledge, terminology, methodology, and deliverables for bids in each sector. Each sector now includes Uganda-specific reference data from the AfDB Country Diagnostic Note (December 2025) and the UN Uganda SDG Analysis Report Summary (2025), including SDG pathway alignment.

| Directory | Sector | Coverage | Uganda Reference |
|---|---|---|---|
| `agriculture/` | Agriculture & Food Security | Crop value chains, irrigation, extension services, food security programmes, agribusiness development | `references/uganda-agriculture-sector.md` — 24.3% of GDP, 70% of workforce, GHI 27.3, undernourishment 36.9%, post-harvest losses 40%, food insecurity 71.2%, SDG Pathways 1 & 3 |
| `health/` | Health & Pharmaceutical | Public health systems, pharmaceutical supply chains, health informatics, disease surveillance, health facility assessments | `references/uganda-health-sector.md` — UHC index 49, MMR 189/100K, life expectancy 68.2, GBV data, nutrition indicators, SDG Pathway 4 |
| `education/` | Education & Capacity Building | Curriculum development, e-learning platforms, institutional strengthening, TVET, teacher training | `references/uganda-education-sector.md` — NER 78% primary, NEET 50.9% (worsening), literacy 74%, GII 124/139, SDG Pathways 2 & 4 |
| `ict/` | ICT & Digital Transformation | E-government, MIS/ERP implementations, digital infrastructure, cybersecurity, data systems | `references/uganda-ict-sector.md` — 4,387 km fibre, 10.3% internet, mobile phone ownership 43%, GII 124/139, SDG Pathway 8 |
| `financial-services/` | Financial Services | Banking, insurance, mobile money, microfinance, financial inclusion, payment systems | `references/uganda-financial-sector.md` — 22 banks, financial inclusion 68% (gender gap), FDI USD 2.99bn, SDG Pathways 1 & 10 |
| `energy/` | Energy & Environment | Power generation, rural electrification, renewable energy, environmental impact assessments | `references/uganda-energy-sector.md` — 2,048 MW installed, 53% access (25% grid/28% off-grid), clean cooking 4%, SDG Pathway 8 |
| `water-sanitation/` | Water, Sanitation & Hygiene | WASH programmes, water utility management, sanitation infrastructure, community-led approaches | `references/uganda-wash-sector.md` — 81.1% improved but only 18% safely managed water, 20% safely managed sanitation, urban waste, SDG Pathway 7 |
| `transport-infrastructure/` | Transport & Infrastructure | Roads, logistics, urban transport planning, infrastructure assessments, PPP advisory | `references/uganda-transport-sector.md` — 159,366 km roads, 28.9 road fatalities/100K, urbanisation 8.8%, housing deficit 7.3M, SDG Pathways 1 & 9 |
| `manufacturing-industrial/` | Manufacturing & Industrial Operations | Manufacturing, processing, warehousing, inventory, production planning, facilities layout, material handling, ERP/MES/WMS/TMS, and green production | `../consulting-frameworks/references/industrial-operations-diagnostics.md` — MRP, capacity, warehouse, quality, traceability, and resource-efficiency diagnostic domains |
| `governance/` | Governance & Public Sector Reform | Institutional reform, M&E frameworks, anti-corruption, decentralisation, public financial management | `references/uganda-governance-sector.md` — IIAG 49.1/100, CPI 26, INFORM 12/191, birth registration 40.4%, women in Cabinet 45%, SDG Pathway 5 |

---

## File Structure

Each sector or framework directory contains:

```
sectors/
├── INDEX.md                          ← this file
├── ppda-uganda/
│   ├── README.md                     ← overview and compliance checklist
│   ├── evaluation-criteria.md        ← scoring weights, mandatory requirements
│   ├── forms-and-templates.md        ← required submission forms
│   └── terminology.md                ← PPDA-specific terms and definitions
├── agriculture/
│   ├── README.md                     ← sector overview
│   ├── methodology-notes.md          ← common frameworks and approaches
│   ├── terminology.md                ← sector-specific vocabulary
│   └── sample-deliverables.md        ← typical deliverables and formats
└── ...
```

Not every directory needs every file from day one. Start with a `README.md` and add reference files as the sector knowledge builds.

---

## Adding a New Sector or Framework

1. Create a subdirectory under `sectors/`
2. Add a `README.md` with an overview, key requirements, and a compliance checklist
3. Add reference files as needed (terminology, evaluation criteria, methodology notes)
4. Update this INDEX.md with the new entry

