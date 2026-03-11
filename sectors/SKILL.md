---
name: sectors
description: Sector and procurement framework reference index. Use when writing proposals to load sector-specific requirements, terminology, evaluation criteria, and compliance rules. Read this index first, then read the relevant sector file before drafting any proposal section.
---

# Sectors — Index

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
| `afdb/` | African Development Bank | AfDB procurement rules, shortlisting criteria, standard bid documents |
| `undp/` | United Nations Development Programme | UN procurement processes, UNGM registration, financial proposal format |

---

## Industry Sectors

These define **what** evaluators expect in terms of domain knowledge, terminology, methodology, and deliverables for bids in each sector.

| Directory | Sector | Coverage |
|---|---|---|
| `agriculture/` | Agriculture & Food Security | Crop value chains, irrigation, extension services, food security programmes, agribusiness development |
| `health/` | Health & Pharmaceutical | Public health systems, pharmaceutical supply chains, health informatics, disease surveillance, health facility assessments |
| `education/` | Education & Capacity Building | Curriculum development, e-learning platforms, institutional strengthening, TVET, teacher training |
| `ict/` | ICT & Digital Transformation | E-government, MIS/ERP implementations, digital infrastructure, cybersecurity, data systems |
| `financial-services/` | Financial Services | Banking, insurance, mobile money, microfinance, financial inclusion, payment systems |
| `energy/` | Energy & Environment | Power generation, rural electrification, renewable energy, environmental impact assessments |
| `water-sanitation/` | Water, Sanitation & Hygiene | WASH programmes, water utility management, sanitation infrastructure, community-led approaches |
| `transport-infrastructure/` | Transport & Infrastructure | Roads, logistics, urban transport planning, infrastructure assessments, PPP advisory |
| `governance/` | Governance & Public Sector Reform | Institutional reform, M&E frameworks, anti-corruption, decentralisation, public financial management |

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
