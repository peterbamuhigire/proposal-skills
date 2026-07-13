---
name: environmental-and-social-safeguards
description: Use when a proposal requires environmental or social screening, ESIA, ESMP, resettlement, donor safeguards, or national environmental compliance. Unlike gender-and-social-inclusion, this skill governs safeguard instruments, risk controls, and compliance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Environmental and Social Safeguards
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill when the assignment explicitly needs safeguards, ESF, ESIA, or environmental and social risk content.
- Load it when another proposal section needs this domain expertise.

## Do Not Use When
- The task only needs formatting or proposer-profile selection.
- Another supporting skill is a closer fit for the assignment.

## Required Inputs
| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Activities, locations, affected people, and funder requirements | ToR and client | required | Stop instrument selection and request screening inputs. |
| National law and donor safeguard standard | Authoritative current sources | required for compliance claims | Mark legal and policy fit unassessed. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Identify where safeguards logic matters in the assignment and which framework applies.
2. Read the local references only where they materially improve the output.
3. Convert the guidance into proposal-ready instruments, controls, and implementation logic.
4. Integrate the result into the target section and check for consistency.

## Quality Standards
- Translate safeguards knowledge into practical proposal language and compliance-ready actions.
- Keep the approach specific to the client context and the actual donor or regulator.
- Preserve compatibility with existing repository workflows and file paths.

## Anti-Patterns
- Naming standards without screening activities and receptors. Fix: show risk pathways and evidence needs.
- Choosing an instrument before categorisation. Fix: screen first against verified rules.
- Copying legal thresholds from memory. Fix: verify jurisdiction, date, regulator, and funder standard.
- Treating consultation as one meeting. Fix: plan accessible, documented engagement and grievances.
- Claiming approval or compliance. Fix: reserve certification for authorised authorities.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Safeguards approach or instrument plan | Evaluator and client safeguards lead | Links screening, instruments, consultations, mitigations, monitoring, ownership, and approvals. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Screening and compliance register | Referenced table | Each risk cites its basis, receptor, instrument, owner, and status. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Assessment defaults to read-only. Site entry, interviews, filing, disclosure, and certification require explicit authority and the responsible professional or institution.

## Degraded Mode
Without site, stakeholder, legal, or donor-standard evidence, produce a screening plan and provisional risk hypotheses. Mark categorisation and compliance unassessed.

## Decision Rules
| Screening result | Action | Risk avoided |
|---|---|---|
| Material impacts need formal assessment | Specify instrument and approval path | Under-scoped compliance |
| Displacement is plausible | Trigger resettlement-specialist review | Unaddressed livelihood harm |
| Standard not verified | Stop compliance claim and research | False legal assurance |

## Worked Example
For a market redevelopment, screen construction, waste, worker, vendor, and livelihood impacts; verify national and funder rules; then scope ESMP and resettlement work.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- Local `references/` files when detailed frameworks or examples are needed.

Infrastructure, agriculture, energy, water, and natural resource assignments increasingly require compliance with environmental and social safeguard frameworks. Proposals must demonstrate that the firm understands the applicable framework and can integrate safeguard requirements into the methodology — not treat them as a separate add-on.

## When to Read This Skill

- The assignment involves infrastructure, construction, agriculture, energy, water, or natural resources
- The ToR mentions "environmental and social impact assessment", "ESIA", "environmental management plan", "safeguards", "resettlement", or "ESF"
- The project is funded by the World Bank, AfDB, or another multilateral development bank
- Drafting methodology sections that need to address environmental or social risks
- When the ToR asks for a standalone ESIA, ESMP, or safeguards instrument

## Frameworks

### World Bank Environmental and Social Framework (ESF)

The current standard for World Bank-funded projects (replaced the Safeguard Policies in 2018):

| Standard | Title | Key Requirements |
|---|---|---|
| ESS1 | Assessment and Management of Environmental and Social Risks and Impacts | Risk screening, ESIA, ESMP, monitoring |
| ESS2 | Labour and Working Conditions | Worker rights, OHS, grievance mechanism |
| ESS3 | Resource Efficiency and Pollution Prevention | Waste management, emissions, hazardous materials |
| ESS4 | Community Health and Safety | Infrastructure safety, security personnel, emergency preparedness |
| ESS5 | Land Acquisition, Restrictions on Land Use, and Involuntary Resettlement | Resettlement Action Plan, compensation, livelihood restoration |
| ESS6 | Biodiversity Conservation and Sustainable Management of Living Natural Resources | Protected areas, habitat assessment, ecosystem services |
| ESS7 | Indigenous Peoples / Sub-Saharan African Historically Underserved Traditional Local Communities | Free, Prior and Informed Consent (FPIC), cultural heritage |
| ESS8 | Cultural Heritage | Chance finds procedure, tangible and intangible heritage |
| ESS9 | Financial Intermediaries | Sub-project screening, E&S management systems |
| ESS10 | Stakeholder Engagement and Information Disclosure | Stakeholder engagement plan, disclosure requirements, grievance mechanism |

### AfDB Integrated Safeguards System (ISS)

Five Operational Safeguards:

| Safeguard | Coverage |
|---|---|
| OS1 | Environmental and Social Assessment |
| OS2 | Involuntary Resettlement: Land Acquisition, Population Displacement and Compensation |
| OS3 | Biodiversity, Renewable Resources and Ecosystem Services |
| OS4 | Pollution Prevention and Control, Hazardous Materials and Resource Efficiency |
| OS5 | Labour Conditions, Health and Safety |

### National Environmental Legislation (East Africa)

| Country | Key Legislation | Lead Agency |
|---|---|---|
| Uganda | National Environment Act, 2019 | NEMA |
| Kenya | Environmental Management and Coordination Act (EMCA), 1999 (amended 2015) | NEMA Kenya |
| Tanzania | Environmental Management Act, 2004 | NEMC |
| Rwanda | Law on Environment, 2018 | REMA |

Proposals must reference both the donor framework and the applicable national legislation. Where they conflict, the more stringent standard applies.

## Common Safeguard Instruments

### Environmental and Social Impact Assessment (ESIA)

Full assessment required for high-risk (Category A) projects:

- Screening and scoping
- Baseline data collection (physical, biological, socio-economic)
- Impact identification and significance assessment
- Analysis of alternatives
- Mitigation measures
- Environmental and Social Management Plan (ESMP)
- Public consultation and disclosure

### Environmental and Social Management Plan (ESMP)

| Impact | Mitigation Measure | Responsibility | Monitoring Indicator | Frequency |
|---|---|---|---|---|
| [Dust generation] | [Water spraying, covered transport] | [Contractor] | [Visible dust levels] | [Daily during construction] |

### Resettlement Action Plan (RAP)

Required when the project involves involuntary displacement or land acquisition:

- Census of affected persons
- Asset inventory and valuation
- Compensation framework (replacement cost)
- Livelihood restoration plan
- Grievance mechanism
- Monitoring and evaluation of resettlement outcomes

## Generating a Standalone Section

When the ToR asks for a dedicated safeguards instrument, generate the relevant document covering the applicable framework's requirements. Always include:

1. Applicable legal and policy framework (donor + national)
2. Screening and categorisation
3. Baseline conditions
4. Impact assessment
5. Mitigation and management measures
6. Monitoring plan
7. Stakeholder consultation and disclosure
8. Grievance mechanism
9. Institutional arrangements and budget

Follow east-african-english standards throughout.

