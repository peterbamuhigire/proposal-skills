# Data Governance Frameworks

Parent skill: [Data Management](../SKILL.md).

> Organised by this engine's governance-engagement workflow and synthesised across Ladley (Data Governance, 2nd ed.), Ladley (Advanced Data Governance, 2024), African Union Data Policy Framework (2022), Ndemo et al. (Data Governance and Policy in Africa, 2023), and Ford Foundation Uganda DG Study (2023).

---

## 1. Frame the Governance Problem With the Client

Work through these framing tasks in the first inception workshop. The task order is this engine's own; concepts are attributed where they come from a named source.

### 1.1 Agree the vocabulary

Data governance is the exercise of authority, control and shared decision-making over data assets: it settles who may decide what about which data, under which conditions and by which method (definition after Ladley). It is an organisation-wide discipline, not an IT function, a project or a one-off compliance exercise. Keep three terms apart in every proposal:

| Term | Covers |
|---|---|
| **Data governance** | Direction, oversight, accountability and policy (the what and why) |
| **Data management** | Processes, tools and architecture that execute the rules (the how) |
| **Data administration** | Operational custody of databases, infrastructure and backups |

### 1.2 Separate the two workstreams, then join them

Propose governance structures and management processes as two distinct workstreams so that ownership is clear, joined by shared artefacts both sides maintain. This mirrors Ladley's "V" model:

| Governance workstream | Management workstream | Shared artefacts |
|---|---|---|
| Vision and principles; policies and standards; accountability structures; compliance monitoring | Architecture and design; data quality processes; metadata management; technology operations | Data dictionary; business glossary; quality rules; RACI matrices |

### 1.3 Surface why data matters to this client

Many organisations treat data as a by-product and a cost centre; governance becomes fundable when the client sees data as an asset that carries both value and liability (storage cost, breach risk, regulatory fines). In a stakeholder workshop, ask which of these roles data plays for the client today, and which it should play:

- Does data run daily operations (registration, dispatch, supply tracking)?
- Does it give the client an advantage others lack (customer analytics, pricing)?
- Is it, or could it be, a product or service in its own right (research sets, credit scoring)?
- Is it protected, licensable intellectual property?
- Do systems, algorithms or trained models depend on it for their value?
- Where does ungoverned data expose the client to legal, reputational or decision risk?

(The six value roles are adapted from Ladley.)

## 2. Size and Stage the Programme

### 2.1 Choose the intensity

Governance intensity runs along a spectrum (Ladley, 2024, "little g" to "Big G"):

| Intensity | Looks like | Fits when |
|---|---|---|
| Light ("little g") | Targeted, embedded in existing processes, few new structures | Early maturity, low buy-in, one system |
| Formal ("medium g") | Named roles, written policies, a council, measured compliance | Growing maturity, regulatory pressure, several systems |
| Enterprise ("Big G") | Organisation-wide mandate, a chief data officer with budget and enforcement powers | High maturity, large data estate, regulatory mandate or data monetisation |

Most East African public bodies and NGO programme units start light. Propose a progression path, not an enterprise landing on day one.

### 2.2 Identify the entry point

Programmes usually start from one of five triggers; name the client's trigger because it shapes scope and quick wins: compliance (data-protection law, sector rules); master data; analytics and AI quality; architecture change (migration, integration, cloud); or formalising informal practices that already work.

### 2.3 Place the client on the maturity scale

| Level | Name | Signs |
|---|---|---|
| 1 | Initial | No formal governance; tribal knowledge; reactive fixes |
| 2 | Aware | Need recognised; pilots; informal stewards |
| 3 | Defined | Policies written; bodies established; roles assigned |
| 4 | Managed | Metrics tracked; compliance measured; issues escalated and resolved |
| 5 | Optimised | Governance part of the culture; continuous improvement |

Assess at inception. Most ministries and NGO programme units in the region sit at levels 1 to 2; a realistic target within one engagement is level 3, reaching 4 in well-resourced settings.

### 2.4 Phase the work and run domains in cycles

Phase a typical twelve-month engagement as: engage sponsors and assess readiness (weeks 1–3); set vision, principles, scope, business case and roadmap (weeks 4–8); design models, metadata standards, quality rules and tooling choices (weeks 9–16); implement with trained stewards and pilot domains (weeks 17–36); operate, measure, adjust and extend to new domains (weeks 37–48 and beyond). This follows the delivery areas Ladley describes, re-sequenced for proposal phasing.

Avoid a single waterfall. Run each data domain (for example finance, HR, health) through its own plan–do–act cycle (after Deming): assess, define vocabulary and quick wins; set policies, pilot and stand up bodies; embed in business as usual, monitor and expand. Domains progress in parallel and show value early.

## 3. Design Authority, Roles and Rules

### 3.1 Map authority to existing structures

| Authority layer | Role | Uganda public-sector mapping |
|---|---|---|
| Leadership | Sets data strategy, approves policy, allocates budget | Accounting Officer, board or Permanent Secretary |
| Executive sponsorship | Chairs the council, resolves cross-department conflicts | Director of ICT or Planning |
| Domain steering | Governs a data domain (HR, finance, health, agriculture) | Heads of department (data owners) |
| Local stewardship | Applies standards, reports issues, maintains metadata | Records officers, M&E officers |

(Layered operating model adapted from Ladley.)

### 3.2 Make implicit roles explicit

| Role | Accountable for | Typical holder |
|---|---|---|
| Chief data officer | Data strategy, programme leadership, board reporting | Director-level or dedicated appointment |
| Data owner | A domain's policies, quality targets and access rules | Head of department |
| Data steward | Business rules, quality issues, dictionary upkeep | Subject expert in the unit |
| Data custodian | Access controls, backups, security, infrastructure | IT or database administrator |

### 3.3 Set up a data council

Cross-departmental councils are the decision forum (Ndemo et al., 2023): one member per major domain plus IT, legal and M&E; chaired by the chief data officer or executive sponsor; monthly for operations and quarterly for strategy; mandated to approve standards, prioritise quality work, settle data-sharing disputes and review compliance; supported by a small secretariat that keeps the governance register.

### 3.4 Separate duties

Those who create data are not the only validators; those who write policy do not also enforce it without independent review; owners set rules, custodians implement them and auditors verify. This matters most in public-sector and donor-funded settings (principle emphasised by Ladley, 2024).

### 3.5 Deliver the rule hierarchy in order

| Level | Purpose | Example |
|---|---|---|
| Principles | Beliefs that guide decisions | "Data is a shared organisational asset" |
| Policies | Mandatory rules derived from principles | "Every dataset has a named owner" |
| Standards | Specific technical or procedural requirements | "Dates use ISO 8601 (YYYY-MM-DD)" |
| Controls | Mechanisms that enforce standards | "The system rejects non-ISO dates" |
| Processes | Procedures for governance activities | "Quality-issue escalation workflow" |

Propose the full hierarchy as a deliverable set. Buying tools (controls) before principles and policies exist is a common failure.

## 4. Build the Business Case

Structure value in five categories: better decisions, faster reporting and service delivery; efficiency (less reconciliation, fewer duplicates, less rework); data products or partnerships where appropriate; risk reduction (data-protection compliance, lower breach probability, fewer audit findings); and, for public bodies, retiring "data debt" (inconsistent definitions, orphaned databases, undocumented transformations). The first four categories follow Ladley; the fifth is this engine's addition for public-sector clients.

## 5. Implement Through Change, Not Just Policy

### 5.1 Plan adoption stage by stage

Use Prosci's ADKAR model as the adoption backbone and put its milestones in the work plan:

| Stage | What the programme does |
|---|---|
| Awareness | Explain why governance matters; quantify the cost of poor data with the client's own examples |
| Desire | Show stewards how governance makes their work easier |
| Knowledge | Train on policies, tools and standards; build data literacy |
| Ability | Provide templates, tools and support so people can follow the process |
| Reinforcement | Publish metrics, recognise good practice, include data quality in performance reviews |

### 5.2 Pre-empt the usual failure causes in the risk register

For each risk, name a mitigation: a governance team without business knowledge or political skill; assuming governance sells itself; leaders who endorse but do not fund or attend; tools and standards deployed before buy-in; treating governance as an IT project; stakeholders who do not understand what governance requires; low data literacy; and trying to govern everything at once instead of priority domains. (Failure causes synthesised from Ladley, 2024, and engine delivery experience.)

### 5.3 Develop the data leaders

As maturity grows, data leaders must move from firefighting to strategy, from technical expert to cross-functional influencer, and add facilitation, negotiation, business-case, benefits-realisation, organisational-design and change-leadership skills. Treat the programme as organisational change led by them, not a technical deployment.

### 5.4 Change the culture deliberately

Visible and resourced executive sponsorship; quick wins within 60 to 90 days (fix one persistent quality issue, publish one domain glossary); data-quality measures in performance agreements; regular progress updates in business language; a community of practice for stewards.

### 5.5 Build literacy in three tiers

All staff (awareness and basic handling); stewards and analysts (quality assessment, metadata, policy application); owners and executives (data strategy, business-case reading, governance decisions). Use training of trainers for sustainability and the capacity-building skill for detailed design.

---

## 6. African Data Governance Context

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

## 7. Proposal Strategy Notes

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
