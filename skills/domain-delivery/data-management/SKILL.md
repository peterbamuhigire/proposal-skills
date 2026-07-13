---
name: data-management
description: Use when a proposal covers data collection, quality, governance, MIS, surveys, protection, retention, or migration. Route outcome measurement to monitoring-and-evaluation; this skill governs the data lifecycle and controls.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Data Management
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill when the assignment explicitly needs data-management, governance, privacy, or information-system content.
- Load it when another proposal section needs this domain expertise.

## Do Not Use When
- The task only needs formatting or proposer-profile selection.
- Another supporting skill is a closer fit for the assignment.

## Required Inputs
| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Data purpose, sources, subjects, flows, and outputs | ToR and system owners | required | Stop detailed design and issue a data-discovery request. |
| Law, consent, retention, access, and quality evidence | Authoritative rules and client controls | conditional | Mark compliance and quality controls unassessed. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Identify where data collection, governance, quality, or protection matters in the assignment.
2. Read the local references only where they materially improve the output.
3. Convert the guidance into proposal-ready controls, activities, and ownership logic.
4. Integrate the result into the target section and check for consistency.

## Quality Standards
- Translate theory into practical proposal language, outputs, and safeguards.
- Keep the approach specific to the client context and implementation reality.
- Preserve compatibility with existing repository workflows and file paths.

## Anti-Patterns
- Naming governance or privacy frameworks without operational controls. Fix: name sources, owners, flows, access, and outputs.
- Collecting data without a decision use. Fix: map every dataset to a stated purpose.
- Promising compliance from memory. Fix: verify the jurisdiction and client policy.
- Treating missing values as zero. Fix: define validation, exception, and remediation rules.
- Migrating before reconciliation. Fix: profile, map, test, reconcile, and approve before cutover.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Data management plan | Evaluator, data owner, delivery team | Covers flows, ownership, quality, protection, retention, access, migration, and acceptance. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Data inventory and quality-control matrix | Traceable register | Every material source has owner, purpose, checks, exceptions, and disposition. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Default to read-only inspection. Editing requires authority; personal or client data access must be least-privilege. Do not move, delete, publish, or certify data without explicit approval.

## Degraded Mode
Without datasets, system access, or verified law, return a data-discovery and control plan with unassessed items. Never report unavailable quality or compliance checks as passed.

## Decision Rules
| Condition | Action | Risk avoided |
|---|---|---|
| Existing data may answer the question | Profile and assess fitness first | Unnecessary collection |
| Decision needs new primary data | Design proportionate collection and consent | Data without purpose |
| Migration changes records | Reconcile samples and require owner sign-off | Silent loss or duplication |

## Worked Example
For a beneficiary MIS, inventory enrolment, service, and outcome data; assign stewards; validate identifiers and dates; and reconcile migrated totals before acceptance.

## SaaS Data Implementation Plan

For SaaS lifecycle-communications scope and for any SaaS implementation that depends on segmentation, behavioural triggers, identity resolution, and operating-rule governance, scope and price a dedicated Data Implementation Plan workstream:

- **Identify schema**: customer, account, user, role, segment, lifecycle stage, lifecycle program flags.
- **Event schema**: signup, activation, in-product actions, billing events, support events, customer-success events.
- **Custom fields**: vertical-specific fields (insurance: policy count; banking: customer count, transaction volume; healthcare: facility, provider category).
- **Identity resolution**: linking the same user across product, marketing automation, CRM, support.
- **Consent and preference management**: lawful basis, opt-in records, channel preferences, frequency caps.
- **Segmentation**: standard segments at launch (by tier, lifecycle stage, health, industry).
- **Data hygiene**: bounce handling, suppression, decay, re-verification.

This is engineering-grade work — price it as such, not inside a bundled "email setup" line.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- Local `references/` files when detailed frameworks or examples are needed.
- Use [references/data-analytics-methodology-for-proposals.md](references/data-analytics-methodology-for-proposals.md) when the proposal
  involves dashboards, MIS analytics, BI, AI analytics, survey analysis, data platforms,
  routine monitoring, forecasting, or evidence-based decision support.
- [../references/saas-lifecycle-email-program-proposal-template.md](../../profiles-sectors/references/saas-lifecycle-email-program-proposal-template.md) for the Data Implementation Plan workstream framing.
- [../references/saas-multi-tenant-architecture-block.md](../../profiles-sectors/references/saas-multi-tenant-architecture-block.md) for tenant-context and data-partitioning concerns.
- [../saas-lifecycle-communications-as-deliverable/SKILL.md](../../saas-proposals/saas-lifecycle-communications-as-deliverable/SKILL.md) for the lifecycle communications skill.

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

