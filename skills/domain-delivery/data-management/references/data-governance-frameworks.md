# Data Governance Frameworks

> Synthesised from Ladley (Data Governance, 2nd ed.), Ladley (Advanced Data Governance, 2024), African Union Data Policy Framework (2022), Ndemo et al. (Data Governance and Policy in Africa, 2023), and Ford Foundation Uganda DG Study (2023).

---

## 1. Data Governance Foundations

### Definition and Scope

Data governance is the exercise of authority, control, and shared decision-making over the management of data assets (Ladley, 2nd ed.). It is an enterprise-wide discipline — not an IT function, not a project, and not a one-off compliance exercise. Governance determines *who* may make *what* decisions about *which* data, under *what* conditions, using *what* methods.

Three distinctions matter in proposals:

| Concept | Meaning |
|---------|---------|
| **Data governance** | Strategy, oversight, accountability, policy — the *what* and *why* |
| **Data management** | Execution of processes, tools, architecture — the *how* |
| **Data administration** | Operational custody of databases, infrastructure, backups |

### Data as an Asset

Organisations routinely treat data as a by-product of operations rather than a managed asset. Two framings help clients see the shift:

- **Resource view**: data supports decisions, reporting, and compliance — a cost centre.
- **Financial-asset view**: data has measurable value, can be monetised, and carries liabilities (storage costs, breach risk, regulatory fines). It should appear in strategic planning alongside human capital and physical assets.

The business case for governance rests on closing the gap between these two views.

### The Governance "V"

Ladley's Governance "V" model separates governance (left arm) from data management (right arm), joined at the bottom by shared artefacts:

```
Governance (Strategy & Oversight)          Data Management (Execution)
  ├─ Vision & principles                    ├─ Architecture & design
  ├─ Policies & standards                   ├─ Data quality processes
  ├─ Accountability structures              ├─ Metadata management
  └─ Compliance monitoring                  └─ Technology operations
                    ╲                      ╱
                     ╲                    ╱
                      Shared Artefacts
                      ├─ Data dictionary
                      ├─ Business glossary
                      ├─ Quality rules
                      └─ RACI matrices
```

This separation is critical in methodology sections: propose governance structures *and* management processes, but keep the two workstreams distinct so the client understands who owns what.

### Six Ways Data Creates Value

Ladley identifies six modes through which data generates organisational value:

1. **Process enabler** — data drives operational workflows (e.g., patient registration, supply chain tracking).
2. **Competitive weapon** — proprietary data creates market advantage (e.g., customer analytics, pricing models).
3. **Product** — data is packaged and sold or shared as a deliverable (e.g., market research, credit scoring datasets).
4. **Asset / intellectual property** — data has balance-sheet value, is protected, and may be licensed.
5. **Enabler of other assets** — data underpins the value of systems, algorithms, and trained models.
6. **Risk** — ungoverned data creates legal liability, reputational damage, and decision errors.

Use these six modes in stakeholder workshops to help clients articulate *why* governance matters to their specific context.

---

## 2. Data Governance Programme Design

### Five-Area Delivery Framework

Ladley structures DG programme delivery across five sequential-but-iterative areas:

| # | Area | Key Activities |
|---|------|----------------|
| 1 | **Engagement** | Identify sponsors, secure mandate, build awareness, assess readiness |
| 2 | **Strategy** | Define vision, principles, scope, business case, roadmap |
| 3 | **Architecture & Design** | Data models, metadata standards, quality rules, technology selection |
| 4 | **Implementation** | Deploy tools, train stewards, operationalise policies, pilot domains |
| 5 | **Operation & Changes** | Monitor compliance, measure value, iterate, expand to new domains |

Map proposal phases to these five areas. A typical 12-month engagement might allocate: Engagement (weeks 1-3), Strategy (weeks 4-8), Architecture & Design (weeks 9-16), Implementation (weeks 17-36), Operation & Changes (weeks 37-48+).

### Plan-Do-Act Approach

Governance programmes fail when treated as waterfall projects. Ladley advocates a Plan-Do-Act cycle (adapted from Deming):

- **Plan**: assess current state, define needs, establish definitions and vocabulary, articulate vision, identify quick wins.
- **Do**: define policies, build awareness, execute pilots, stand up governance bodies.
- **Act**: integrate governance into business-as-usual, operate monitoring, measure outcomes, adjust and expand.

Each domain (e.g., customer data, financial data, health data) cycles through Plan-Do-Act independently. This allows parallel progress and early value demonstration.

### Big G vs Little g Spectrum

Ladley (2024) introduces a spectrum of governance intensity:

| End | Description | When Appropriate |
|-----|-------------|------------------|
| **Little g** | Targeted, non-invasive, embedded in existing processes, minimal new structures | Early maturity, low buy-in, single-system scope |
| **Medium g** | Formalised roles, defined policies, governance council, measured compliance | Growing maturity, regulatory pressure, multi-system integration |
| **Big G** | Mandated enterprise-wide, CDO-led, budget authority, enforcement powers | High maturity, large data estates, regulatory mandates, data monetisation |

Most East African organisations start at little g. Propose a progression path, not a Big G landing zone on day one.

Five common DG programme themes that shape scope (Ladley 2024):

1. **Compliance-driven** — triggered by PDPA, GDPR, sector regulations.
2. **MDM-driven** — master data management as the entry point.
3. **Analytics-driven** — data quality for dashboards, BI, and AI.
4. **Architecture-driven** — data migration, system integration, cloud transition.
5. **Formalise-the-informal** — documenting and scaling ad hoc practices that already work.

### Business Case Components

Structure the DG business case around four value categories (Ladley):

1. **Direct contributions** — improved decision quality, faster reporting, better service delivery.
2. **Efficiency gains** — reduced data reconciliation effort, fewer duplicate records, lower rework.
3. **Data monetisation** — new revenue from data products, partnerships, or analytics services.
4. **Risk reduction** — compliance with data protection law, reduced breach probability, lower audit findings.

Add a fifth for public sector clients: **data debt retirement** — the accumulated cost of years of ungoverned data (inconsistent definitions, orphaned databases, undocumented transformations).

### Maturity Model

Data governance maturity progresses through stages — evolution, not revolution:

| Level | Name | Characteristics |
|-------|------|-----------------|
| 1 | **Initial / Ad hoc** | No formal governance, tribal knowledge, reactive data fixes |
| 2 | **Aware** | Recognised need, pilot initiatives, informal stewards |
| 3 | **Defined** | Policies documented, governance bodies established, roles assigned |
| 4 | **Managed** | Metrics tracked, compliance measured, issues escalated and resolved |
| 5 | **Optimised** | Governance embedded in culture, continuous improvement, data valued as asset |

Assess the client's current level during inception. Most government ministries and NGO programme units in East Africa operate at Level 1-2. Propose a realistic target of Level 3-4 within the engagement period.

---

## 3. Operating Models and Roles

### Four-Layer Operating Model

Ladley's operating model organises governance authority in four layers:

```
Layer 1: Leadership (Board / Permanent Secretary / CEO)
  └─ Sets data strategy, approves policy, allocates budget

Layer 2: Executive Sponsors (CDO / CIO / Director-level)
  └─ Chairs governance council, resolves cross-department conflicts

Layer 3: Subject Area Steering (Domain leads / Data Owners)
  └─ Governs specific data domains (HR, finance, health, agriculture)

Layer 4: Local Stewards (Operational staff embedded in units)
  └─ Enforces standards, reports issues, maintains metadata
```

For public sector proposals in Uganda and the region, map these layers to existing structures: Layer 1 = Accounting Officer; Layer 2 = Director of ICT or Planning; Layer 3 = Department heads; Layer 4 = Records officers and M&E officers.

### Key Roles

| Role | Responsibility | Typical Holder |
|------|---------------|----------------|
| **Chief Data Officer (CDO)** | Enterprise data strategy, governance programme leadership, board reporting | Director-level or dedicated appointment |
| **Data Owner** | Accountable for a data domain; approves policies, quality targets, access rules | Department head or senior manager |
| **Data Steward** | Day-to-day governance execution; defines business rules, resolves quality issues, maintains dictionary | Subject matter expert within a unit |
| **Data Custodian** | Technical custody; implements access controls, backups, security, infrastructure | IT / database administrator |

In many East African organisations, these roles are implicit. A governance programme makes them explicit, documented, and resourced.

### Data Councils

Cross-departmental data councils provide the forum for governance decision-making (Ndemo et al., 2023). Structure:

- **Composition**: one representative per major data domain or department, plus IT, legal, and M&E.
- **Chair**: CDO or senior executive sponsor.
- **Frequency**: monthly for operational councils; quarterly for strategic steering.
- **Mandate**: approve standards, prioritise data quality initiatives, resolve cross-departmental data sharing disputes, review compliance metrics.
- **Secretariat**: a small governance office that prepares agendas, tracks decisions, and maintains the governance register.

### Separation of Duties

Ladley (2024) emphasises separation of duties as a governance design principle:

- Those who **create** data should not be the sole validators.
- Those who **govern** policy should not also **enforce** compliance without independent review.
- **Data owners** (business) set rules; **data custodians** (IT) implement them; **auditors** verify adherence.

This prevents conflicts of interest and strengthens accountability — particularly important in public sector and donor-funded environments.

### Principles, Policies, Standards, Controls Hierarchy

Governance artefacts cascade from abstract to specific:

| Level | Description | Example |
|-------|-------------|---------|
| **Principles** | High-level beliefs that guide all decisions | "Data is a shared organisational asset" |
| **Policies** | Mandatory rules derived from principles | "All datasets must have a designated data owner" |
| **Standards** | Specific technical or procedural requirements | "Date fields use ISO 8601 (YYYY-MM-DD) format" |
| **Controls** | Mechanisms that enforce standards | "System validation rejects non-ISO date entries" |
| **Processes** | Step-by-step procedures for governance activities | "Data quality issue escalation workflow" |

Propose the full hierarchy as a deliverable set. Many organisations jump to controls (buying tools) without establishing principles and policies first — a common failure pattern.

---

## 4. Implementation and Change Management

### ADKAR Change Model Applied to Data Governance

Ladley advocates ADKAR (Prosci) as the change management backbone for DG programmes:

| ADKAR Stage | DG Application |
|-------------|---------------|
| **Awareness** | Communicate why governance matters; share data quality horror stories; quantify cost of poor data |
| **Desire** | Build personal motivation — show stewards how governance makes their work easier, not harder |
| **Knowledge** | Train on policies, tools, standards; build data literacy across the organisation |
| **Ability** | Provide tools, templates, and support so people *can* follow governance processes |
| **Reinforcement** | Recognise good practice, publish metrics, celebrate quick wins, embed in performance reviews |

Build ADKAR milestones into the project plan — governance without change management is policy without practice.

### Root Causes for Data Governance Failure

Ladley (2024) identifies eight recurring failure patterns:

1. **Competency gaps** — governance team lacks business knowledge or political skill.
2. **Hubris** — assuming governance is self-evidently valuable; failing to sell it internally.
3. **Sincerity gap** — leadership endorses governance but does not fund it, attend meetings, or enforce compliance.
4. **Premature implementation** — deploying tools and standards before culture and buy-in are ready.
5. **IT mindset** — treating governance as a technology project rather than a business programme.
6. **Ignorance** — stakeholders do not understand what governance means or requires.
7. **Data illiteracy** — staff lack the skills to interpret, manage, or question data.
8. **Scope overreach** — trying to govern everything at once instead of starting with priority domains.

Address each explicitly in risk registers and mitigation strategies.

### Data Leader Transformations

Ladley (2024) outlines the transformations required of data leaders as governance matures:

- **Strategic shift**: from reactive data firefighting to proactive data strategy.
- **Changing roles**: from technical expert to cross-functional leader and influencer.
- **New behaviours**: facilitation, negotiation, coalition-building, executive communication.
- **New capabilities**: business case development, benefits realisation, stakeholder management.
- **New skills**: change management, organisational design, programme governance.
- **Transformation management**: leading the governance programme as an organisational change initiative, not a technical deployment.

### Culture Change Requirements

Data governance is fundamentally a culture change programme. Key interventions:

- **Executive sponsorship** — visible, sustained, and resourced (not ceremonial).
- **Quick wins** — demonstrate value within 60-90 days (e.g., resolve a persistent data quality issue, publish a business glossary for one domain).
- **Incentive alignment** — include data quality metrics in performance agreements.
- **Communication** — regular updates on governance progress, using language the business understands.
- **Communities of practice** — peer networks of data stewards who share challenges and solutions.

### Training and Literacy Programmes

Propose data literacy as a core deliverable in any governance engagement:

- **Tier 1 — Awareness** (all staff): what is data governance, why it matters, basic data handling.
- **Tier 2 — Practitioner** (stewards, analysts): data quality assessment, metadata management, policy application.
- **Tier 3 — Leadership** (owners, executives): data strategy, business case interpretation, governance decision-making.

Use Training of Trainers (ToT) for sustainability. Pair with the capacity-building skill for detailed training design.

---

## 5. African Data Governance Context

### AU Data Policy Framework (February 2022)

The African Union adopted the AU Data Policy Framework to guide member states in building inclusive, sovereign data economies. Key elements:

**Vision**: harness data for Africa's socio-economic transformation while ensuring data sovereignty, privacy, and equitable benefit-sharing.

**Seven guiding principles**:

1. **Common African Data** — data generated in Africa should primarily benefit African people and economies.
2. **Transparency** — data collection, use, and sharing practices must be open and understandable.
3. **Accountability** — clear responsibility chains for data handling across public and private sectors.
4. **Privacy** — protection of personal data as a fundamental right.
5. **Fairness** — equitable access to data and its benefits, preventing monopolisation.
6. **Non-discrimination** — data practices must not reinforce bias, exclusion, or inequality.
7. **Interconnected** — data systems should be interoperable across sectors and borders.

**Data categorisation** (five types with differentiated governance requirements):

| Category | Governance Emphasis |
|----------|-------------------|
| Personal data | Consent, minimisation, purpose limitation, breach notification |
| Community data | Collective rights, benefit-sharing, indigenous knowledge protection |
| Business / proprietary data | IP protection, competition law, trade secrets |
| Sensitive data | Enhanced safeguards (health, biometric, financial, children's data) |
| Public sector data | Open data presumption, interoperability standards, transparency |

**Five enablers** for an African data economy:

1. **Infrastructure** — data centres, connectivity, cloud services, energy access.
2. **Human capital** — data literacy, STEM education, professional development.
3. **Innovation** — local AI/ML development, start-up ecosystems, research institutions.
4. **Finance** — investment in data infrastructure, PPPs, venture capital.
5. **Regulatory** — harmonised legal frameworks, data protection authorities, cross-border agreements.

### Malabo Convention

The African Union Convention on Cyber Security and Personal Data Protection (Malabo Convention, 2014) provides the continental legal baseline:

- Requires member states to establish data protection authorities.
- Mandates legal frameworks for personal data protection, electronic transactions, and cybersecurity.
- Ratification has been slow (entered into force June 2023 after 15th ratification).
- Reference the Convention in proposals as the continental anchor for national data protection law.

### East African Data Protection Legislation

| Country | Primary Law | Authority | Key Provisions |
|---------|------------|-----------|----------------|
| **Uganda** | Data Protection and Privacy Act (PDPA), 2019 | Personal Data Protection Office (NITA-U) | Consent-based processing, data minimisation, cross-border transfer restrictions, 72-hour breach notification |
| **Kenya** | Data Protection Act, 2019 | Office of the Data Protection Commissioner (ODPC) | Comprehensive GDPR-influenced framework, data protection impact assessments, registration of data controllers/processors |
| **Rwanda** | Law Relating to the Protection of Personal Data and Privacy, 2021 | National Cyber Security Authority (NCSA) | Consent requirements, data localisation provisions, sector-specific guidance |
| **Tanzania** | Personal Data Protection Act, 2023 (building on Electronic and Postal Communications Act, 2010) | Tanzania Data Protection Authority | Emerging framework, data localisation requirements, penalties for non-compliance |

All four countries have enacted or are implementing data protection legislation. However, enforcement capacity, institutional readiness, and public awareness remain significant gaps across the region.

### Uganda Data Governance Study Findings

The Ford Foundation study (2023) on data governance in Uganda's economic and labour sectors found:

- **Fragmented policies**: multiple agencies collect overlapping data with inconsistent standards.
- **Low data literacy**: limited understanding of data governance concepts among public servants.
- **Inadequate infrastructure**: unreliable connectivity, limited storage, ageing systems.
- **PDPA compliance gaps**: many organisations unaware of their obligations under the 2019 Act.
- **Weak data sharing**: public-private data exchange hampered by distrust, unclear protocols, and technical incompatibility.

**Recommendations**:
- Develop a national data governance strategy with cross-sector coordination.
- Invest in data literacy programmes for public servants.
- Establish interoperability standards for government data systems.
- Strengthen the Personal Data Protection Office with funding and technical capacity.
- Create incentive structures for data sharing between government agencies.

These findings directly inform how to position DG interventions in Uganda proposals — lead with practical, incremental improvements rather than ambitious enterprise-wide programmes.

### Cross-Border Data Flows and Data Sovereignty

Key considerations for proposals involving multi-country data:

- **Data sovereignty**: the AU framework asserts that African data should be governed under African law, even when processed abroad.
- **Data localisation**: Uganda and Rwanda have provisions requiring certain data categories to be stored on servers within national borders.
- **Cross-border transfer mechanisms**: adequacy decisions, standard contractual clauses, and binding corporate rules — largely modelled on GDPR but with African-specific requirements.
- **EAC harmonisation**: the East African Community has initiated (but not completed) harmonisation of ICT and data protection frameworks.

### AfCFTA Digital Trade Provisions

The African Continental Free Trade Area (AfCFTA) includes digital trade provisions relevant to data governance (Ndemo et al., 2023):

- Protocol on Digital Trade (under negotiation) will address cross-border data flows, e-commerce, and digital services.
- Potential for mutual recognition of data protection standards across member states.
- Implications for consulting assignments involving regional data platforms, trade data systems, and cross-border M&E.

Reference AfCFTA when proposing data governance for regional programmes or multi-country assignments.

---

## 6. Proposal Strategy Notes

### When to Propose Data Governance

Include a DG component when the assignment involves any of the following:

- **MIS design or upgrade** — governance structures must accompany any new information system.
- **M&E system development** — data quality, indicator definitions, and reporting standards require governance.
- **E-government / digital transformation** — interoperability, data sharing, and citizen data protection demand formal governance.
- **Health informatics** — patient data sensitivity, DHIS2 implementations, and sector reporting standards.
- **Agricultural data systems** — farmer registries, market information systems, weather data platforms.
- **Financial sector assignments** — KYC data, credit bureau data sharing, mobile money transaction records.
- **Donor programme management** — results data quality, beneficiary data protection, reporting compliance.
- **Institutional capacity building** — data governance is a cross-cutting capacity that strengthens all other functions.

### Key Terminology for Methodology Sections

Use these terms precisely in proposals:

| Term | Meaning |
|------|---------|
| Data governance charter | Founding document establishing governance authority, scope, and structures |
| Data dictionary | Catalogue of all data elements with definitions, formats, owners, and quality rules |
| Business glossary | Plain-language definitions of business terms to ensure shared understanding |
| Data quality framework | Rules, metrics, and processes for measuring and improving data quality |
| Metadata management | Systematic documentation of data about data — lineage, definitions, relationships |
| Master data management (MDM) | Single authoritative source for core entities (clients, locations, products) |
| Data lineage | Tracing data from origin through transformations to final use |
| Data classification scheme | Categorisation of data by sensitivity, value, and governance requirements |
| RACI matrix | Responsible-Accountable-Consulted-Informed assignment for governance activities |

### Common Deliverables

Structure DG deliverables as a progressive set:

| Phase | Deliverable | Description |
|-------|------------|-------------|
| Inception | Data governance readiness assessment | Current-state maturity, stakeholder mapping, gap analysis |
| Inception | Data governance charter | Mandate, scope, principles, roles, escalation procedures |
| Design | Data governance operating model | Council structure, role descriptions, meeting cadences, decision rights |
| Design | Data dictionary and business glossary | For priority data domains (start with 2-3 domains, not everything) |
| Design | Data quality framework | Quality dimensions, measurement rules, thresholds, remediation processes |
| Implementation | Policy and standards suite | Data classification, access control, retention, sharing, breach response |
| Implementation | RACI matrix | Role assignments for all governance processes |
| Implementation | Training programme | Tiered curriculum (awareness, practitioner, leadership) with ToT |
| Operation | Monitoring dashboard | Compliance metrics, quality scores, issue tracking, stewardship activity |
| Operation | Sustainability plan | Handover, institutional embedding, budget provisions, annual review cycle |

### Linking DG to Sustainability and Institutional Capacity

Data governance is inherently a sustainability intervention. Frame it as such:

- **Institutional embedding**: governance structures (councils, stewards, policies) persist beyond the project if integrated into existing organisational structures and budgets.
- **Capacity building**: data literacy and stewardship skills are transferable capabilities that strengthen the organisation's overall competence.
- **Risk reduction**: governance reduces dependence on individual knowledge holders — documented standards survive staff turnover.
- **Donor alignment**: most development partners now require data quality assurance and data protection compliance in programme designs.

In the methodology, explicitly connect DG activities to the client's sustainability and exit strategy requirements. Reference the sustainability-planning skill for detailed exit strategy frameworks.

---

## Quick-Reference: Framework Selection Guide

| Client Context | Recommended Entry Point | Governance Intensity |
|---------------|------------------------|---------------------|
| No existing governance, low awareness | Awareness campaign + single-domain pilot | Little g |
| Regulatory pressure (PDPA, sector regulation) | Compliance-driven programme with policy suite | Medium g |
| New MIS or system implementation | Architecture-driven governance embedded in system design | Medium g |
| Analytics or AI initiative | Analytics-driven governance focused on data quality and lineage | Medium g |
| Large public-sector data estate | Enterprise-wide programme with CDO appointment | Big G |
| Multi-country / regional programme | Harmonised framework with national adaptation | Big G |

---

*Sources: Ladley, J. (2020) Data Governance, 2nd ed.; Ladley, J. (2024) Advanced Data Governance (conference); African Union (2022) AU Data Policy Framework; Ndemo, B. et al. (2023) Data Governance and Policy in Africa, Palgrave Macmillan; Ford Foundation (2023) Understanding Data Governance in Uganda.*
