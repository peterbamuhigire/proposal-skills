---
name: 08-work-plan
description: Use when drafting activities, dependencies, milestones, review gates, Gantt tables, or staffing schedules. Unlike 06-methodology, this skill converts the approach into an executable sequence and tests it against staffing and pricing.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Work Plan and Timeline
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill to draft or revise the work plan, schedule, staffing schedule, or timeline section.
- Load it when the evaluator needs a realistic delivery sequence and timing logic.

## Do Not Use When
- The task is unrelated to work planning or scheduling.
- The user only needs supporting domain knowledge rather than this section.

## Required Inputs
- The ToR, deliverables, milestones, and assignment duration.
- The selected proposer profile and any relevant procurement requirements.
- Staffing assumptions, dependencies, and known schedule constraints.

| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Methodology activities, deliverables, duration, team effort, dependencies, approvals, and price basis | Aligned proposal sections | required | Return an unresolved dependency map; do not invent dates or effort. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Read the assignment materials and confirm the timeline, milestones, and required planning outputs.
2. Load the proposer profile and any relevant procurement, sector, and methodology context.
3. Use the structure below to build a realistic sequence of activities, deliverables, dependencies, and staffing effort.
4. Add explicit review, prototype, support, launch, escalation, and optimisation windows where the scope requires them.
5. Check the work plan against the methodology, team, and financial assumptions.
6. Verify that durations, overlaps, milestones, and approval logic are credible before finalising.

## Quality Standards
- Keep the plan realistic, readable, and tied to the actual scope.
- Use British English and East African professional tone unless the bid format requires otherwise.
- Prefer explicit milestones, dependencies, review gates, and staffing logic over vague timetable language.

## Anti-Patterns
- Releasing the section with an unresolved mandatory input. Fix: block release and name the evidence owner.
- Hiding a contradiction with another proposal section. Fix: reconcile the source sections before drafting resumes.
- Treating an unavailable check as passed. Fix: mark it not assessed and return a qualified draft.
- Do not create a timeline that ignores deliverables, review cycles, or client inputs.
- Do not over-compress or over-extend the plan beyond what the assignment supports.
- Do not let the work plan contradict the methodology, team, or budget.
- Do not omit client review time. Fix: show submission, review, revision, approval, and recovery windows.
- Do not overlap one expert impossibly. Fix: reconcile person-days and concurrent tasks.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Work plan, milestones, dependencies, and staffing schedule | Evaluator and project manager | Dates or periods, owners, effort, gates, client inputs, recovery, and price basis reconcile. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Schedule reconciliation and critical-path trace | Checked tables | All deliverables, person-days, reviews, and dependencies match methodology, team, and budget. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Planning is read-only by default. Do not commit client dates, book resources, alter calendars, or approve schedule changes without authority.

## Degraded Mode
Without confirmed duration, dependencies, or effort, return a relative sequence with assumptions and decision dates. Do not claim the plan is feasible.

## Decision Rules
| Constraint | Action | Risk avoided |
|---|---|---|
| Approval gates the next phase | Put it on the critical path | Hidden delay |
| Activities can safely overlap | Show dependency and separate resources | False compression |
| Delay consumes contingency | Escalate replan or scope decision | Silent schedule failure |

## Worked Example
A twelve-week diagnostic shows data access in week one, analysis after validated extracts, client review time, revision, approval, and non-overlapping effort for the same specialist.

## SaaS Work Plan Patterns

For SaaS implementation engagements, the work plan must reflect:

- **Mutual Action Plan integration**: the work plan is the operational view of the MAP, with phases (selection, contract/security/mobilisation, build, pilot, cutover, adoption, optimisation) and named decision gates.
- **Recurring-meeting discipline**: every recurring meeting in the SaaS implementation has a stated purpose, a named artefact produced, and a decision required by close. Status meetings without artefact or decision are removed.
- **Pilot-to-rollout sequencing**: pilot cohort, 30-day pilot review, go/no-go to full rollout, waved rollout by business unit or region, stabilisation.
- **Lifecycle program build cadence**: data implementation plan, content production, automation engineering, operating rules sign-off, measurement plan — sequenced before each lifecycle program goes live.
- **Customer success operating cadence**: weekly during implementation, monthly during stabilisation, quarterly QBR, annual renewal review.

## Embedded Accounting Engine Work Plan Patterns

For embedded accounting-engine engagements, the work plan must show accounting-specific dependencies:

- Posting-rule workshops before build of money-moving workflows.
- Chart-of-accounts and mapping sign-off before UAT.
- Opening-balance migration, customer/supplier balance migration, stock valuation, and fixed-asset migration as explicit activities.
- Parallel run against existing books or sample periods before go-live where feasible.
- Reconciliation gates for AR, AP, inventory, payroll, tax, bank/mobile money, and fixed assets.
- Month-end close simulation before production cutover.
- First-close support after go-live.
- Client finance-owner approval at mapping, migration, report, and close gates.

## Finance And Accounting Work Plan Patterns

When the assignment must manage accounts, budgets, donor funds, project advances, reimbursements, taxes, or audit evidence, schedule finance activities explicitly:

- Inception finance-control setup: budget lines, approval thresholds, bank/mobile-money handling, procurement/payment evidence, reporting format.
- Monthly or milestone financial reporting cycles.
- Bank/mobile-money reconciliation windows.
- Advance/imprest liquidation checkpoints.
- Budget-variance review and approval gates.
- Tax/statutory verification checkpoints.
- Donor/client financial report review cycles.
- Audit-file assembly and close-out financial report.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- [../profiles/SKILL.md](../../profiles-sectors/profiles/SKILL.md) for proposer selection and voice.
- [../sectors/SKILL.md](../../profiles-sectors/sectors/SKILL.md) for procurement and sector routing.
- [../service-design-proposal-strategy/SKILL.md](../../strategy-positioning/service-design-proposal-strategy/SKILL.md) for journey research, blueprinting, co-creation, prototype, pilot, and implementation sequencing.
- [../customer-service-and-maintenance-proposals/SKILL.md](../../strategy-positioning/customer-service-and-maintenance-proposals/SKILL.md) for support windows, incident response, maintenance cycles, and post-launch optimisation scheduling.
- [../references/technical-strategy-credibility-checklist.md](../../profiles-sectors/references/technical-strategy-credibility-checklist.md) for SaaS, AI, software, API, cloud, and operations roadmap checks.
- [../references/saas-mutual-action-plan-template.md](../../profiles-sectors/references/saas-mutual-action-plan-template.md) for the MAP that the work plan operationalises.
- [../references/saas-implementation-methodology-blocks.md](../../profiles-sectors/references/saas-implementation-methodology-blocks.md) for the SaaS implementation phases.
- [../references/saas-poc-scoping-template.md](../../profiles-sectors/references/saas-poc-scoping-template.md) for POC / pilot time-boxing.
- [../references/saas-customer-success-engagement-package.md](../../profiles-sectors/references/saas-customer-success-engagement-package.md) for operating cadence.
- [../saas-mutual-action-planning-and-close-plans/SKILL.md](../../saas-proposals/saas-mutual-action-planning-and-close-plans/SKILL.md) for the SaaS MAP skill.
- [../embedded-accounting-engine-proposal/SKILL.md](../../strategy-positioning/embedded-accounting-engine-proposal/SKILL.md) for posting-rule, migration, reconciliation, close-simulation, and first-close work-plan patterns.
- [../accounting-finance-advisory/SKILL.md](../../domain-delivery/accounting-finance-advisory/SKILL.md) for project financial-management, donor/grant finance, budget-control, and audit-file work-plan patterns.
- Root and local `references/` files for delivery logic and scheduling support.

The work plan translates the methodology into a time-bound schedule. It must be realistic, account for client review periods and approval gates, and show that the firm has thought through the sequencing of activities. Evaluators check whether the timeline is achievable; overly compressed or suspiciously padded plans both raise concerns.

## What to Gather Before Writing

- The overall assignment duration from the ToR
- The phases and activities from the methodology section (`06-methodology`)
- Client review and approval periods required for key deliverables
- Any fixed dates such as start date, end date, mid-term review, and final presentation
- Public holidays or known unavailability periods in the client's country
- Team member availability and any part-time allocations
- Dependencies showing which activities cannot start until others are complete

## Structure

### Work Plan Narrative

Half a page. Explain the logic of the schedule:

- why the work is sequenced this way
- where the critical path lies
- what assumptions underpin the timeline
- where buffer has been built in and why
- how estimates were derived, referencing PERT where useful: `te = (optimistic + 4 x most likely + pessimistic) / 6`
- which milestones are internal delivery points versus client decision gates

### Gantt-Style Activity Schedule

Show all activities by phase, mapped to weeks or months. Use `X` or shading to show activity windows.

| Phase / Activity | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 |
|---|---|---|---|---|---|---|---|---|
| **Phase 1: Inception** | | | | | | | | |
| Kick-off meeting | X | | | | | | | |
| Document review | X | X | | | | | | |
| Inception report | | X | | | | | | |
| _Client review_ | | | X | | | | | |
| **Phase 2: [Name]** | | | | | | | | |

Rules for the Gantt:
- show client review periods as distinct rows in italics
- include approval gates as milestones
- do not overlap activities that have hard dependencies
- build in at least one week of buffer for every three months of assignment duration

### Dependency and Approval Table

Add this when the assignment has review-heavy delivery or multiple workstreams:

| Activity / Deliverable | Depends On | Client Input Required | Approval Gate |
|---|---|---|---|
| [Item] | [Predecessor] | [Data/decision/access] | [Yes/No or gate name] |

This helps evaluators see that the team has planned around real dependencies rather than drawing an optimistic timeline.

### Milestone and Deliverables Table

Link each milestone to its deliverable and target date:

| # | Milestone | Deliverable | Target Date |
|---|---|---|---|
| 1 | Inception complete | Inception Report | Week 2 |
| 2 | [Phase name] complete | [Deliverable name] | Week [N] |

Every deliverable from the methodology section must appear here with a date.

### Staffing Schedule

Show when each team member is deployed and their level of effort per phase:

| Team Member | Role | Phase 1 | Phase 2 | Phase 3 | Total Days |
|---|---|---|---|---|---|
| [Name] | Team Leader | [N] | [N] | [N] | [Total] |
| [Name] | [Role] | [N] | [N] | [N] | [Total] |
| **Total** | | **[N]** | **[N]** | **[N]** | **[Total]** |

The total person-days here must match the financial proposal. Any discrepancy will be flagged by evaluators.

### Work Package Responsibility Matrix

For complex assignments, include a compact responsibility matrix beneath the staffing schedule:

| Work Package | Lead | Support | Review / Approval |
|---|---|---|---|
| [Package] | [Expert] | [Support roles] | [Client or QA role] |

This links the schedule to named accountability and reduces the risk that timelines appear detached from the proposed team.

## Scheduling Principles

- **Critical Path Method (CPM):** Identify the longest dependency chain through the work plan. Activities on the critical path have zero float; any delay extends the project.
- **Schedule hierarchy:** Show high-level phase milestones in the proposal and keep detailed task logic underneath. This preserves scannability while proving the team has thought through execution.
- **Resource levelling:** After building the schedule, check that no team member is over-allocated. Delay non-critical tasks within their float to resolve conflicts.
- **Schedule contingency:** Build in buffer days for context disruptions such as rainy season, election periods, public holidays, or slow approvals. Do not plan overtime into the baseline.
- **Time-cost trade-off:** There is an optimum project duration where costs are minimised. Compressing below this increases costs through overtime, coordination overhead, and rework.
- **Decision gates matter:** Client reviews, approvals, and access decisions are part of the actual schedule. Treat them as explicit timeline events, not hidden assumptions.
- **Industrial site work:** For manufacturing, warehouse, ERP/MES/WMS/TMS, or inventory assignments, schedule data extraction, site walk-throughs, stock or record sampling, process observation, validation workshops, and client review gates as separate activities. Do not hide site access, system access, or stock-reconciliation dependencies inside generic "assessment" rows.
- **Service and digital work:** Schedule journey research, prototype validation, content approval, QA, security review, launch readiness, support window, incident review, and optimisation backlog as separate activities where relevant.

## Reference Library

| Reference File | Contents |
|---|---|
| `../project-management/references/project-controls-and-earned-value.md` | WBS construction, WBS dictionary, task responsibility matrices, PERT estimation, CPM/critical path, schedule hierarchy, resource levelling, earned value tracking, change control, and stagegate process |
| `../consulting-frameworks/references/industrial-operations-diagnostics.md` | Industrial assessment work packages for material planning, capacity, warehouse, facility flow, quality, and green-production assignments |
| `../references/service-design-methodology-module.md` | Service design work packages, artefacts, prototypes, implementation steps, and acceptance criteria |
| `../references/website-software-maintenance-support-language.md` | Maintenance cycles, SLA windows, support responsibilities, incident handling, and optimisation backlog planning |

## Tone Rules

- Two to three pages
- Realistic timelines; do not compress to impress
- Always include client review windows
- Keep the work plan consistent with methodology (`06`) and the financial proposal (`10`)
- Ensure total person-days in the staffing schedule match the financial proposal
- Follow `east-african-english` standards throughout

