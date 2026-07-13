---
name: project-management
description: Use when a proposal needs delivery governance, reporting, RACI, change control, escalation, or a project management plan. Unlike 08-work-plan, this skill governs how delivery is controlled, not merely when activities occur.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Project Management
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill when the assignment explicitly needs project-management, governance, controls, or reporting content.
- Load it when another proposal section needs this domain expertise.

## Do Not Use When
- The task only needs formatting or proposer-profile selection.
- Another supporting skill is a closer fit for the assignment.

## Required Inputs
| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Scope, deliverables, timeline, team, approvals, and reporting rules | ToR and proposal sections | required | Stop governance design and reconcile scope first. |
| Client decision rights and escalation contacts | Client governance evidence | conditional | Use role placeholders and flag them for mobilisation. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Identify where project-management logic matters in the assignment.
2. Identify decision gates, support windows, incident escalations, prototype reviews, and technical strategy checkpoints where relevant.
3. Read the local references only where they materially improve the output.
4. Convert the guidance into proposal-ready governance, controls, and reporting mechanisms.
5. Integrate the result into the target section and check for consistency.

## Quality Standards
- Translate PM frameworks into practical proposal language, outputs, and escalation logic.
- Keep the approach specific to the client context and implementation reality.
- Show how scope, schedule, responsibility, reporting, and decisions will be controlled visually and operationally.
- Preserve compatibility with existing repository workflows and file paths.

## Anti-Patterns
- Naming PRINCE2, PMBoK, or Agile without controls. Fix: specify decisions, owners, artefacts, and cadence.
- Scheduling status meetings with no output. Fix: require an artefact and decision from each forum.
- Giving every issue to the steering committee. Fix: set thresholds and delegated authority.
- Omitting client dependencies. Fix: register inputs, due dates, owners, and schedule consequences.
- Treating change control as bureaucracy. Fix: connect scope decisions to time, cost, quality, and acceptance.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Project management and governance plan | Evaluator, sponsor, project manager | Defines forums, decision rights, RACI, reporting, change, escalation, acceptance, and records. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Governance, decision, and reporting register | Controlled tables | Every recurring control has an owner, cadence, artefact, threshold, and decision route. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Planning and review default to read-only. Editing plans requires authority; approving scope, cost, schedule, access, production changes, or client communications requires the named decision owner.

## Degraded Mode
When confirmed governance or client contacts are unavailable or missing, return a narrow, qualified governance model with unresolved gaps. Mark decision rights not assessed; do not treat silence as approval.

## Decision Rules
| Delivery condition | Action | Risk avoided |
|---|---|---|
| Donor/government assignment with formal stage gates | Use controlled stage governance | Informal acceptance |
| Iterative technical delivery | Use hybrid cadence with fixed approval gates | Uncontrolled iteration |
| Issue exceeds delegated threshold | Escalate with options and consequence | Decision drift |

## Worked Example
A monthly steering committee approves material scope and risk decisions; the weekly delivery forum resolves operational blockers and updates the RAID log rather than forwarding every issue.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- Local `references/` files when detailed frameworks or examples are needed.
- [../references/technical-strategy-credibility-checklist.md](../../profiles-sectors/references/technical-strategy-credibility-checklist.md) for software, SaaS, AI, cloud, API, operations, and roadmap governance.
- [../references/customer-service-and-escalation-commitments.md](../../profiles-sectors/references/customer-service-and-escalation-commitments.md) for issue escalation, incident updates, and service recovery commitments.
- [../references/website-software-maintenance-support-language.md](../../profiles-sectors/references/website-software-maintenance-support-language.md) for support windows, maintenance cycles, and SLA planning.

This skill provides the PM knowledge base that proposal sections draw from — particularly methodology (06), work plan (08), and team composition (07). It covers the frameworks, governance models, and reporting standards that make proposals credible on project delivery.

## When to Read This Skill

- Drafting the project management and governance subsection of the methodology
- Defining reporting structures in the work plan
- Structuring steering committee and escalation paths
- When the ToR asks for a standalone project management plan as a deliverable

## Frameworks

### PRINCE2 (Preferred for Government and Donor Projects)

Most common in East African public sector and donor-funded assignments. Key elements to reference in proposals:

- **Defined roles**: Project Board (steering committee), Project Manager, Team Managers
- **Stage-gate approach**: each stage has defined products and approval gates before the next stage begins
- **Exception management**: tolerances defined for time, cost, scope, quality, risk, and benefit — escalation triggers when tolerances are exceeded
- **Product-based planning**: deliverables (products) drive the plan, not activities

When to use: government assignments, World Bank, AfDB, UNDP, any ToR that references "stage-gate" or "product-based" delivery.

### PMBoK / PMP (Preferred for Private Sector and Large Programmes)

More common in private sector, large infrastructure, and multi-year programmes:

- **Five process groups**: Initiating, Planning, Executing, Monitoring & Controlling, Closing
- **Ten knowledge areas**: Integration, Scope, Schedule, Cost, Quality, Resource, Communications, Risk, Procurement, Stakeholder
- **Earned Value Management**: for cost and schedule performance tracking on larger programmes

When to use: private sector clients, large-scale programmes, assignments where the client uses PMBoK terminology.

### Systems and Visual PM Patterns

Use these when the assignment involves multiple workstreams, many interfaces, or complex delivery dependencies:

- **Work Breakdown Structure (WBS)** — decomposes the assignment into controllable work packages
- **WBS dictionary** — defines the deliverable, owner, assumptions, and completion rule for each package
- **Task responsibility matrix** — shows who is responsible, supports, reviews, or approves each work package
- **Schedule hierarchy** — programme milestones at the top, detailed task networks underneath
- **Decision-gate calendar** — shows when the client must review, approve, or redirect the work

These patterns are especially useful when the proposal must convince evaluators that the team can manage complexity, not just draft a high-level timeline.

### Agile / Hybrid (Preferred for ICT and Software)

For ICT system implementations and software development assignments:

- **Sprint-based delivery**: two to four week iterations with demonstrable outputs
- **Hybrid approach**: Agile delivery within a PRINCE2 or PMBoK governance wrapper — most appropriate for public sector ICT projects where the client needs stage-gate approvals but the development team works iteratively
- **Ceremonies**: sprint planning, daily stand-ups, sprint reviews, retrospectives
- **Backlog management**: prioritised requirements managed through a product backlog

When to use: software development, system configuration, digital transformation, any assignment with iterative delivery of working outputs.

## Governance Structure

### Steering Committee

- **Composition**: client senior management (chair), project sponsor, firm's project director, key stakeholder representatives
- **Frequency**: monthly for assignments under six months; quarterly for longer programmes
- **Function**: strategic oversight, issue resolution, approval of stage/phase transitions, scope change decisions
- **Deliverable**: meeting minutes with decisions and action items

### Project Management Office (for large programmes)

Only propose a PMO for assignments exceeding 12 months or involving multiple workstreams:

- Programme coordinator, M&E officer, communications officer
- Consolidated reporting across workstreams
- Resource allocation and conflict resolution
- Quality assurance and standards compliance

### Matrix Delivery Pattern

For multi-disciplinary assignments, describe the project office realistically:
- keep the central project office lean
- assign delivery responsibility to work-package owners
- use the PMO to consolidate reporting, dependency management, and issue escalation
- avoid implying a heavyweight bureaucracy for short assignments

## Reporting Standards

### Weekly Status Report

For active delivery phases:

- Activities completed this week
- Activities planned for next week
- Issues and risks (new or escalated)
- Decisions required from the client

### Monthly Progress Report

- Progress against the work plan (percentage complete per phase)
- Deliverables submitted and their approval status
- Budget expenditure versus plan (if applicable)
- Updated risk register
- Key achievements and challenges

### Inception Report

The first major deliverable in most consulting assignments. Must include:

- Confirmed understanding of the assignment
- Finalised methodology and work plan (refined from the proposal)
- Stakeholder mapping and engagement plan
- Confirmed team deployment schedule
- Updated risk register
- Any clarifications or scope refinements agreed with the client

## Escalation Framework

| Level | Trigger | Who Decides | Timeframe |
|---|---|---|---|
| Team level | Day-to-day operational issues | Team Leader | Same day |
| Project level | Delays, resource conflicts, quality issues | Project Manager + Client Focal Point | Within 3 working days |
| Steering committee | Scope changes, budget overruns, strategic risks | Steering Committee | Next scheduled meeting or emergency session |

### Visual Control Toolkit

When the ToR expects strong controls, reference these artefacts explicitly:
- milestone ladder showing major approvals and delivery gates
- dependency network for critical deliverables
- task responsibility matrix linked to the WBS
- issue, risk, and decision logs with named owners
- stoplight dashboard backed by schedule and cost data

## Earned Value Management

For assignments exceeding three months or involving significant budgets, include earned value tracking:

- **Three measures:** Planned Value (PV), Earned Value (EV), Actual Cost (AC)
- **Key indices:** Schedule Performance Index (SPI = EV/PV), Cost Performance Index (CPI = EV/AC), Critical Ratio (CR = SPI × CPI)
- **15% Rule:** If the project is 15% into its timeline and performance indices are below 0.8, initiate a formal corrective action review — projects in trouble at 15% almost never recover
- **Stoplight reporting:** Green (CR 0.8-1.2), Yellow (CR in warning range), Red (CR outside limits) — backed by earned value data, not subjective assessment

### Change Control

All scope changes must be assessed for impact on schedule, cost, and performance before approval. Log all changes and their effect on work budget, reserve, and margin. No change is implemented without written client agreement.

### Lessons Learned (Lewis Method)

Two questions only: "What are we doing well?" and "What do we want to improve?" Never ask "What did we do wrong?" Use multivoting for prioritisation; resolve in order: goals → roles → procedures → relationships.

## Reference Library

| Reference File | Contents |
|---|---|
| `references/project-controls-and-earned-value.md` | Lewis Method (10-step PM methodology), WBS construction, WBS dictionary, schedule hierarchy, task responsibility matrices, PERT three-point estimation, CPM/critical path scheduling, resource levelling, complete earned value system (all formulas), 15% rule, four EV scenarios, project control framework, change control process, three types of project reviews, lessons learned facilitation, stoplight reporting, stagegate process, variance analysis tools (MAD/RMSE/MAPE), control charts, PM maturity model (5 levels), multitasking problem, quality tracking indicators |

Read the reference file when writing methodology sections that describe project management approaches, when designing governance frameworks, or when the assignment involves assessing client PM capability.

## Generating a Standalone Section

When the ToR asks for a dedicated project management plan, generate a document covering:

1. Project governance structure (organogram with roles)
2. Reporting framework (types, frequency, recipients)
3. Quality management approach
4. Issue and change management process
5. Communication plan
6. Escalation framework
7. Earned value tracking approach (for assignments > 3 months)
8. Change control process

Follow east-african-english standards throughout.

