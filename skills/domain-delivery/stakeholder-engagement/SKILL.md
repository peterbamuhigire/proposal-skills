---
name: stakeholder-engagement
description: Use when a proposal needs stakeholder mapping, consultation, participation, feedback, grievance handling, or engagement planning. Unlike change-management, this skill governs who must be heard and how their input is recorded, not adoption of a defined change.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Stakeholder Engagement
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill when the assignment explicitly needs stakeholder mapping, engagement, consultation, or communication content.
- Load it when another proposal section needs this domain expertise.

## Do Not Use When
- The task only needs formatting or proposer-profile selection.
- Another supporting skill is a closer fit for the assignment.

## Required Inputs
| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Stakeholder groups, decisions, impacts, and engagement obligations | ToR and client records | required | Produce a discovery map; do not claim representation. |
| Access, language, accessibility, safeguarding, and grievance constraints | Client and stakeholder evidence | conditional | Flag participation risks and provisional channels. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Identify where stakeholder logic matters in the assignment.
2. Map the evaluator, sponsor, frontline, user, support, and approval groups separately where their concerns differ.
3. Read the local references only where they materially improve the output.
4. Convert the guidance into proposal-ready stakeholder, consultation, and feedback mechanisms.
5. Integrate the result into the target section and check for consistency.

## Quality Standards
- Translate stakeholder theory into practical proposal language, activities, and governance.
- Keep the approach specific to the client context and implementation reality.
- Preserve compatibility with existing repository workflows and file paths.

## Anti-Patterns
- Describing engagement as communications. Fix: name decisions, influence, methods, and feedback closure.
- Consulting only senior stakeholders. Fix: include frontline users and affected groups.
- Treating one representative as the whole group. Fix: test representation and dissent.
- Using inaccessible channels. Fix: adapt language, timing, venue, format, and support.
- Collecting feedback without response. Fix: log, decide, communicate disposition, and preserve grievances.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Stakeholder engagement plan and register | Evaluator, engagement lead, client sponsor | Maps groups to interests, influence, decisions, methods, cadence, access measures, owners, and feedback closure. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Consultation and feedback register | Traceable log | Records who was engaged, method, issue, response, owner, and unresolved matter. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Mapping is read-only by default. Contacting people, recording personal data, publishing views, resolving grievances, or making commitments requires explicit authority and safeguarding controls.

## Degraded Mode
Without stakeholder access or verified representation, return a provisional map and engagement plan. Do not claim consultation, consent, or consensus.

## Decision Rules
| Stakeholder position | Action | Risk avoided |
|---|---|---|
| High influence and high impact | Engage in decisions and close feedback | Late veto or harm |
| Low formal power but high impact | Use accessible direct consultation | Elite-only evidence |
| Complaint alleges harm or retaliation | Activate protected grievance route | Unsafe public handling |

## Worked Example
For a municipal service redesign, separately engage officials, frontline staff, vendors, residents, and persons with disabilities; record conflicting needs and show which design decision each informed.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- Local `references/` files when detailed frameworks or examples are needed.
- [../references/ethical-persuasion-and-evaluator-psychology-gate.md](../../profiles-sectors/references/ethical-persuasion-and-evaluator-psychology-gate.md) for evaluator concerns, risk perception, and ethical influence.
- [../references/service-design-methodology-module.md](../../profiles-sectors/references/service-design-methodology-module.md) for stakeholder mapping across service journeys, touchpoints, and backstage roles.
- [../proposal-storytelling-and-evaluator-journey/SKILL.md](../../strategy-positioning/proposal-storytelling-and-evaluator-journey/SKILL.md) for audience-specific narrative and sign-off logic.

Every consulting assignment involves multiple stakeholders with different interests, influence, and expectations. Proposals that demonstrate a structured approach to stakeholder engagement — not just a list of "consultation meetings" — score higher because they show the firm understands the political and institutional landscape.

## When to Read This Skill

- The assignment involves multiple government agencies, departments, or ministries
- The ToR mentions "stakeholder engagement", "consultation", "participatory approach", or "communication strategy"
- The assignment affects end users, beneficiaries, or communities
- Drafting methodology sections that require stakeholder analysis
- When the ToR asks for a standalone stakeholder engagement plan

## Stakeholder Analysis

### Identification

Map all stakeholders across four categories:

- **Primary stakeholders**: directly affected by the assignment (end users, beneficiaries, staff whose roles change)
- **Secondary stakeholders**: indirectly affected (partner organisations, regulators, suppliers)
- **Key stakeholders**: with authority or influence over the assignment (decision-makers, budget holders, political leaders)
- **Implementing stakeholders**: involved in delivering the assignment (client project team, counterpart staff)

### Power-Interest Matrix

Classify each stakeholder group to determine engagement strategy:

| | Low Interest | High Interest |
|---|---|---|
| **High Power** | Keep satisfied — regular updates, consult on decisions that affect them | Manage closely — active engagement, co-design, steering committee membership |
| **Low Power** | Monitor — general communications, no active engagement needed | Keep informed — regular updates, feedback channels, town halls |

### Stakeholder Register

| Stakeholder Group | Category | Power | Interest | Key Concerns | Engagement Strategy |
|---|---|---|---|---|---|
| [Ministry leadership] | Key | High | High | Budget, timelines, political visibility | Steering committee, monthly briefings |
| [End users / field staff] | Primary | Low | High | Job security, workload, training | Workshops, change champions, help desk |

## Consultation Methods

| Method | Purpose | When to Use |
|---|---|---|
| One-on-one interviews | Understand individual perspectives, sensitive issues | Senior stakeholders, political figures |
| Workshops | Co-design, validation, capacity building | Technical stakeholders, user groups |
| Focus group discussions | Community perspectives, qualitative feedback | Beneficiaries, field-level staff |
| Town halls | Broad awareness, transparency, Q&A | All-staff sessions, community briefings |
| Surveys | Quantitative data from large groups | Baseline assessments, satisfaction measurement |
| Steering committee | Governance, strategic decisions, issue resolution | Senior management, project sponsors |

## Reference Files

Load these reference files for deeper guidance when writing stakeholder engagement sections:

- [references/stakeholder-analysis-and-mapping.md](references/stakeholder-analysis-and-mapping.md) — stakeholder identification methods (role-based, agenda-based, snowball), classification systems (primary/secondary/key, voluntary/involuntary, normative/derivative), hidden stakeholders (sleepers, spoilers, lurkers), analysis frameworks (power-interest matrix, Mitchell-Agle-Wood salience model with 7 types, sociodynamics model with 8 attitudes, expectations matrix), stakeholder project continuum (neutral/sensitive/led), sources of power (overt/influence/covert), RACI as stakeholder tool, sustainable development integration
- [references/stakeholder-engagement-and-communication.md](references/stakeholder-engagement-and-communication.md) — engagement life cycle (4 stages), relationship management process (Huemann), engagement journey (resistant→indifferent→supportive→proactive), whispering evolution (Shander), engagement formula, purposeful communication framework (6 types), communication by quadrant, 10 engagement techniques, expectation alignment, consultation design (6 requirements), questioning techniques (Five Whys, Six Ws, diverge/converge, premortem), facilitation and meetings, group engagement, 7 principles of engagement
- [references/stakeholder-dynamics-and-influence.md](references/stakeholder-dynamics-and-influence.md) — resistance management (indicators, root causes, 10 strategies), Thomas-Kilmann conflict modes, 6-step conflict resolution, difficult stakeholder protocol, barriers to engagement (13 types), Cialdini's 6 principles applied to stakeholders, cognitive biases catalogue (17 biases), active listening framework, emotional intelligence model, 10 competencies, relationship building (8 practices), Freeman's 10 ethical principles, systemic constellation methods, Ashby's Law of Requisite Variety

## Grievance and Feedback Mechanism

For assignments affecting communities or large staff populations:

- Dedicated feedback channel (phone line, email, suggestion box)
- Clear process for logging, categorising, and responding to complaints
- Response timeframe commitment (e.g., acknowledgement within 48 hours, resolution within 10 working days)
- Regular reporting on grievances received and resolved

## Generating a Standalone Section

When the ToR asks for a dedicated stakeholder engagement plan, generate a document covering:

1. Stakeholder identification methodology — role-based and agenda-based approaches, snowball sampling (see `references/stakeholder-analysis-and-mapping.md` section 1)
2. Stakeholder classification — primary/secondary/key, hidden stakeholders (sleepers, spoilers, lurkers) (see `references/stakeholder-analysis-and-mapping.md` sections 2–3)
3. Stakeholder analysis — power-interest matrix and salience model with engagement strategy per type (see `references/stakeholder-analysis-and-mapping.md` sections 4–5)
4. Stakeholder project continuum assessment — classify assignment as neutral, sensitive, or stakeholder-led (see `references/stakeholder-analysis-and-mapping.md` section 5)
5. Engagement strategy per stakeholder group — lifecycle stages, engagement journey (see `references/stakeholder-engagement-and-communication.md` sections 1–3)
6. Communication plan — purposeful communication framework with six communication types (see `references/stakeholder-engagement-and-communication.md` section 6)
7. Consultation design — six requirements for genuine consultation, extended management process (see `references/stakeholder-engagement-and-communication.md` section 9)
8. Resistance management strategy — indicators, root causes, ten strategies for engaging resisters (see `references/stakeholder-dynamics-and-influence.md` sections 1, 4)
9. Conflict resolution approach — Thomas-Kilmann modes, six-step process (see `references/stakeholder-dynamics-and-influence.md` section 2)
10. Influence and persuasion framework — Cialdini's six principles applied to stakeholder contexts (see `references/stakeholder-dynamics-and-influence.md` section 5)
11. Grievance and feedback mechanism
12. Stakeholder engagement monitoring — four evaluation approaches, engagement effectiveness tracking (see `references/stakeholder-engagement-and-communication.md` section 15)

Follow east-african-english standards throughout.

