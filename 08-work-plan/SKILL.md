---
name: proposal-writing/08-work-plan
description: Write the work plan and timeline section of a consulting proposal. Use when the user asks to draft the work plan, Gantt chart, project schedule, milestone table, or staffing schedule.
---

# Work Plan and Timeline

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

## Workflow
1. Read the assignment materials and confirm the timeline, milestones, and required planning outputs.
2. Load the proposer profile and any relevant procurement, sector, and methodology context.
3. Use the structure below to build a realistic sequence of activities, deliverables, and staffing effort.
4. Check the work plan against the methodology, team, and financial assumptions.
5. Verify that durations, overlaps, and milestone logic are credible before finalizing.

## Quality Standards
- Keep the plan realistic, readable, and tied to the actual scope.
- Use British English and East African professional tone unless the bid format requires otherwise.
- Prefer explicit milestones, dependencies, and staffing logic over vague timetable language.

## Anti-Patterns
- Do not create a timeline that ignores deliverables, review cycles, or client inputs.
- Do not over-compress or over-extend the plan beyond what the assignment supports.
- Do not let the work plan contradict the methodology, team, or budget.

## Outputs
- A proposal-ready work plan, timeline, and related staffing or milestone structures.

## References
- `../profiles/SKILL.md` for proposer selection and voice.
- `../sectors/SKILL.md` for procurement and sector routing.
- Root and local `references/` files for delivery logic and scheduling support.

The work plan translates the methodology into a time-bound schedule. It must be realistic, account for client review periods and approval gates, and show that the firm has thought through the sequencing of activities. Evaluators check whether the timeline is achievable — overly compressed or suspiciously padded plans both raise concerns.

## What to Gather Before Writing

- The overall assignment duration from the ToR
- The phases and activities from the methodology section (06-methodology)
- Client review and approval periods required for key deliverables
- Any fixed dates — start date, end date, mid-term review, final presentation
- Public holidays or known unavailability periods in the client's country
- Team member availability and any part-time allocations
- Dependencies — which activities cannot start until others are complete

## Structure

### Work Plan Narrative

Half a page. Briefly explain the logic of the schedule:

- Why the work is sequenced this way
- Where the critical path lies (the longest dependency chain — any slip here delays the project)
- What assumptions underpin the timeline (e.g., client provides data within two weeks of request)
- Where buffer has been built in and why
- How estimates were derived — reference PERT three-point estimation for credibility: `te = (optimistic + 4 × most likely + pessimistic) / 6`

### Gantt-Style Activity Schedule

A table showing all activities by phase, mapped to weeks or months. Use "X" or shading to indicate when each activity is active.

| Phase / Activity | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 |
|---|---|---|---|---|---|---|---|---|
| **Phase 1: Inception** | | | | | | | | |
| Kick-off meeting | X | | | | | | | |
| Document review | X | X | | | | | | |
| Inception report | | X | | | | | | |
| _Client review_ | | | X | | | | | |
| **Phase 2: [Name]** | | | | | | | | |

Rules for the Gantt:

- Show client review periods as distinct rows in italics — these are not the firm's activities but they consume calendar time
- Include approval gates as milestones
- Do not overlap activities that have dependencies
- Build in at least one week of buffer for every three months of assignment duration

### Milestone and Deliverables Table

A table linking each milestone to its deliverable and target date:

| # | Milestone | Deliverable | Target Date |
|---|---|---|---|
| 1 | Inception complete | Inception Report | Week 2 |
| 2 | [Phase name] complete | [Deliverable name] | Week [N] |

Every deliverable from the methodology section must appear here with a date.

### Staffing Schedule

A table showing when each team member is deployed and their level of effort per phase:

| Team Member | Role | Phase 1 | Phase 2 | Phase 3 | Total Days |
|---|---|---|---|---|---|
| [Name] | Team Leader | [N] | [N] | [N] | [Total] |
| [Name] | [Role] | [N] | [N] | [N] | [Total] |
| **Total** | | **[N]** | **[N]** | **[N]** | **[Total]** |

The total person-days here must match the financial proposal. Any discrepancy will be flagged by evaluators.

## Scheduling Principles

- **Critical Path Method (CPM):** Identify the longest dependency chain through the work plan. Activities on the critical path have zero float — any delay extends the project. Non-critical activities have float that can absorb delays.
- **Resource levelling:** After building the schedule, check that no team member is over-allocated. Delay non-critical tasks within their float to resolve conflicts.
- **Schedule contingency:** Build in buffer days for context disruptions (rainy season, election periods, public holidays). Do NOT plan overtime into the baseline — keep it in reserve.
- **The time-cost trade-off:** There is an optimum project duration where costs are minimised. Compressing below this increases costs exponentially (overtime, coordination overhead, rework). Never compress timelines to impress — evaluators know how long things take.

## Reference Library

| Reference File | Contents |
|---|---|
| `../project-management/references/project-controls-and-earned-value.md` | WBS construction, PERT estimation (formula), CPM/critical path, resource levelling, earned value tracking, change control, stagegate process |

## Tone Rules

- Two to three pages
- Realistic timelines — do not compress to impress; evaluators know how long things take
- Always include client review windows — omitting them signals inexperience
- The work plan must be consistent with the methodology (section 06) and the financial proposal (section 10)
- The total person-days in the staffing schedule must match the financial proposal — any discrepancy will be flagged
- Follow east-african-english standards throughout
