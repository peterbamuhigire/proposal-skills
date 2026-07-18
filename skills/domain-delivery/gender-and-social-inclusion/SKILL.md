---
name: gender-and-social-inclusion
description: Use when a proposal needs gender analysis, GESI mainstreaming, disability inclusion, disaggregated indicators, or equitable participation. Unlike environmental-and-social-safeguards, this skill integrates inclusion into design and results rather than safeguard compliance instruments.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Gender and Social Inclusion
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill when the assignment explicitly needs gender, social inclusion, disability, youth, or GESI content.
- Load it when another proposal section needs this domain expertise.

## Do Not Use When
- The task only needs formatting or proposer-profile selection.
- Another supporting skill is a closer fit for the assignment.

## Required Inputs
| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Affected groups, barriers, objectives, and donor requirements | ToR and stakeholder evidence | required | Return an inclusion-analysis plan; do not invent needs. |
| Disaggregated baseline and participation evidence | Client data or verified research | conditional | Label gaps and avoid unsupported targets. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Identify where GESI or inclusion logic matters in the assignment.
2. Read the local references only where they materially improve the output.
3. Convert the guidance into proposal-ready measures, indicators, and delivery logic.
4. Integrate the result into the target section and check for consistency.

## Quality Standards
- Translate inclusion concepts into practical proposal commitments and mechanisms.
- Keep the approach specific to the client context and implementation reality.
- Preserve compatibility with existing repository workflows and file paths.

## Anti-Patterns
- Reducing GESI to counting women. Fix: analyse access, agency, safety, disability, age, and intersecting barriers.
- Setting quotas without evidence. Fix: establish and qualify the baseline and rationale.
- Consulting only organised representatives. Fix: include accessible routes for less-visible groups.
- Adding GESI only in one paragraph. Fix: integrate design, staffing, indicators, budget, and risk.
- Collecting sensitive attributes without controls. Fix: minimise data and apply consent, access, and protection.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| GESI integration plan | Evaluator, programme lead, M&E team | Names barriers, adaptations, owners, budget implications, indicators, safeguards, and feedback. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Barrier-to-response matrix | Disaggregated table | Each barrier has evidence, affected group, response, owner, and indicator. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Analysis is read-only by default. Engagement, sensitive-data collection, public claims, and programme mutation require authority, consent, safeguarding controls, and accessible methods.

## Degraded Mode
Without disaggregated evidence or accessible engagement, return a GESI evidence plan and provisional adaptations. Do not report participation, equity, or safety as assessed.

## Decision Rules
| Evidence | Action | Risk avoided |
|---|---|---|
| Specific barrier is evidenced | Fund and assign a targeted adaptation | Token inclusion |
| Evidence is absent | Conduct accessible, disaggregated analysis | Invented needs |
| Indicator could expose people | Aggregate or redesign it | Privacy or safeguarding harm |

## Worked Example
For digital trade support, test device, literacy, language, care-work, disability, and finance barriers by group; adapt channels and timing; measure access and outcomes separately.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- Local `references/` files when detailed frameworks or examples are needed.

World Bank, AfDB, UNDP, EU, and most bilateral donors now require explicit attention to gender equality and social inclusion (GESI) in all assignments. Proposals that treat GESI as a tick-box exercise score poorly — evaluators look for meaningful integration into the methodology, team composition, and data collection. This skill provides the frameworks and language to do this credibly.

## When to Read This Skill

- The ToR mentions "gender", "social inclusion", "GESI", "gender mainstreaming", "disability inclusion", or "youth engagement"
- The assignment is donor-funded (World Bank, AfDB, UNDP, EU, bilateral)
- The assignment affects communities, beneficiaries, or public service delivery
- Drafting methodology sections that need to demonstrate inclusive approaches
- When the ToR asks for a standalone gender action plan or GESI strategy

## Core Principles

- **Do no harm**: ensure the assignment does not worsen existing inequalities
- **Meaningful participation**: affected groups participate in design and decision-making, not just as beneficiaries
- **Disaggregated data**: all data collection and reporting disaggregated by sex, age, disability status, and other relevant dimensions
- **Targeted actions**: specific activities to address barriers faced by marginalised groups — not just "awareness raising"

## Gender Mainstreaming in Proposals

### Gender Analysis

During the inception or assessment phase, include:

- **Who does what**: roles and responsibilities of men, women, youth, persons with disabilities in the current situation
- **Who has access to and control over resources**: decision-making power, financial resources, land, technology
- **What are the barriers**: cultural norms, legal frameworks, institutional practices that create or perpetuate inequality
- **What are the opportunities**: entry points for promoting equality through this assignment

### Integration Across Proposal Sections

| Section | GESI Integration |
|---|---|
| Understanding of assignment | Identify gender and inclusion dimensions of the problem |
| Methodology | Include gender analysis activities, sex-disaggregated data collection, inclusive consultation methods |
| Team composition | Include a gender/GESI specialist if the assignment warrants it; ensure team diversity |
| Stakeholder engagement | Ensure women's groups, youth groups, and disability organisations are consulted |
| Capacity building | Ensure training is accessible (timing, venue, language, format) to all groups |
| M&E | Include gender-sensitive indicators, disaggregate all data |

### GESI-Sensitive Indicators

| Dimension | Example Indicators |
|---|---|
| **Participation** | % of women among training participants, % of youth in consultation workshops |
| **Access** | % of female-headed households reached, % of persons with disabilities accessing services |
| **Decision-making** | % of women in leadership/management positions, % of women on steering committees |
| **Benefit** | Income change disaggregated by sex, service satisfaction disaggregated by sex and age |

## Social Inclusion Dimensions

Beyond gender, address:

- **Disability**: physical accessibility of venues, materials in accessible formats, inclusion of persons with disabilities in consultation
- **Youth**: engagement of young people (18–35) in design and implementation, youth-specific needs and barriers
- **Ethnic and linguistic minorities**: materials in local languages, culturally appropriate consultation methods
- **Geographic remoteness**: reaching rural and hard-to-access populations

## Generating a Standalone Section

When the ToR asks for a dedicated GESI plan or gender action plan, generate a document covering:

1. Gender and social inclusion analysis methodology
2. Key findings from the analysis (barriers, opportunities, at-risk groups)
3. GESI action plan with specific activities, responsibilities, timelines, and budget
4. GESI-sensitive indicators integrated into the results framework
5. Data disaggregation plan
6. Institutional arrangements for GESI oversight (e.g., GESI focal point on the team)
7. Monitoring and reporting on GESI outcomes

Follow east-african-english standards throughout.

