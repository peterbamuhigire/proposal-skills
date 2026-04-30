---
name: data-management
description: Data management, data governance, and data collection frameworks for consulting proposals. Use as a reference when drafting methodology sections that involve MIS design, data systems, surveys, data quality, or data protection compliance. Can generate a standalone data management plan when a ToR requires one.
---

# Data Management
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When
- Use this skill when the assignment explicitly needs data-management, governance, privacy, or information-system content.
- Load it when another proposal section needs this domain expertise.

## Do Not Use When
- The task only needs formatting or proposer-profile selection.
- Another supporting skill is a closer fit for the assignment.

## Required Inputs
- The assignment brief or target proposal section.
- The sector, client, geography, and any donor or regulatory constraints that matter.

## Workflow
1. Identify where data collection, governance, quality, or protection matters in the assignment.
2. Read the local references only where they materially improve the output.
3. Convert the guidance into proposal-ready controls, activities, and ownership logic.
4. Integrate the result into the target section and check for consistency.

## Quality Standards
- Translate theory into practical proposal language, outputs, and safeguards.
- Keep the approach specific to the client context and implementation reality.
- Preserve compatibility with existing repository workflows and file paths.

## Anti-Patterns
- Do not mention governance or privacy frameworks without showing how they apply.
- Do not overload the proposal with jargon or academic summary.
- Do not ignore referenced files when they are needed for accuracy.

## Outputs
- Domain-informed data-management content aligned to this skill.

## References
- Local `references/` files when detailed frameworks or examples are needed.
- Use `references/data-analytics-methodology-for-proposals.md` when the proposal
  involves dashboards, MIS analytics, BI, AI analytics, survey analysis, data platforms,
  routine monitoring, forecasting, or evidence-based decision support.

Assignments involving system implementations, M&E frameworks, surveys, or institutional assessments all require a data management component. Proposals that demonstrate a structured approach to data collection, storage, quality, governance, and protection score higher — particularly with donors who have been burned by projects that produced unusable data.

## When to Read This Skill

- The assignment involves designing or implementing a management information system (MIS)
- The ToR mentions "data collection", "data management", "data quality", "data governance", or "data protection"
- The methodology includes surveys, assessments, or monitoring activities that generate data
- The assignment must comply with data protection legislation
- When the ToR asks for a standalone data management plan

## Data Collection

### Method Selection

| Method | Best For | Tools |
|---|---|---|
| Mobile data collection | Field surveys, facility assessments, beneficiary registration | ODK, KoBoToolbox, SurveyCTO |
| Paper-based forms | Low-connectivity environments, sensitive data, legal requirements | Standardised forms with clear coding |
| System-generated data | Routine monitoring, transaction records, service delivery | MIS, ERP, HMIS, EMIS |
| Administrative records | Baseline data, historical trends, coverage statistics | Government databases, reports |
| Key informant interviews | Qualitative data, expert perspectives | Interview guides, recording equipment |

### Data Collection Standards

- **Standardised tools**: all data collection instruments piloted before deployment
- **Enumerator training**: minimum two days of training including field practice
- **Quality checks**: real-time validation in mobile tools, supervisor spot-checks for paper-based
- **Consent**: informed consent obtained and documented for all respondent data
- **Unique identifiers**: every record has a unique ID; no reliance on names alone

## Data Quality Framework

### The Five Dimensions of Data Quality

| Dimension | Definition | How to Verify |
|---|---|---|
| **Validity** | Data measures what it is intended to measure | Review instrument design, pilot testing |
| **Reliability** | Consistent results across enumerators and time | Inter-rater reliability tests, re-interviews |
| **Completeness** | All required fields populated, no missing records | Automated completeness checks, dashboard monitoring |
| **Timeliness** | Data available when needed for decision-making | Submission deadlines, real-time dashboards |
| **Integrity** | Data protected from unauthorised alteration | Access controls, audit trails, version control |

### Data Quality Assurance Activities

- Pre-collection: instrument design review, pilot testing, enumerator certification
- During collection: daily data quality reports, supervisor verification, back-checks on 10% of submissions
- Post-collection: cleaning protocols (outlier detection, consistency checks, duplicate removal), validation against secondary sources

## Data Governance

For system implementation and institutional assignments, propose a data governance structure:

- **Data owner**: the client department or unit responsible for each data set
- **Data steward**: the person responsible for data quality within each unit
- **Access control**: role-based access — who can view, edit, approve, and export
- **Data dictionary**: standardised definitions for all fields and indicators
- **Retention and archival**: how long data is kept, in what format, and when it is archived or destroyed

## Data Protection Compliance

### East African Data Protection Legislation

| Country | Legislation | Key Requirements |
|---|---|---|
| Uganda | Data Protection and Privacy Act, 2019 | Registration with PDPO, consent for processing, data minimisation, cross-border transfer restrictions |
| Kenya | Data Protection Act, 2019 | Registration with ODPC, consent, data subject rights, breach notification within 72 hours |
| Tanzania | Personal Data Protection Act (under development) | Follow emerging requirements; apply Kenya/Uganda standards as minimum |
| Rwanda | Law Relating to the Protection of Personal Data and Privacy, 2021 | Consent, purpose limitation, data subject rights, cross-border transfer restrictions |

### Proposal Commitments

When processing personal data, the proposal should commit to:

- Data collection limited to what is necessary for the assignment (data minimisation)
- Informed consent obtained from all data subjects
- Data stored securely (encrypted at rest and in transit)
- Access restricted to authorised project personnel
- Data not transferred outside the country without appropriate safeguards
- Data retained only for the duration necessary, then securely destroyed
- Compliance with the applicable national data protection law

## Generating a Standalone Section

When the ToR asks for a dedicated data management plan, generate a document covering:

1. Data management approach and principles
2. Data collection methods and tools
3. Data quality assurance framework
4. Data governance structure (roles, access controls, data dictionary)
5. Data storage and security measures
6. Data protection compliance (applicable legislation, consent, retention, destruction)
7. Data analysis and reporting plan
8. Data handover and sustainability

Follow east-african-english standards throughout.

