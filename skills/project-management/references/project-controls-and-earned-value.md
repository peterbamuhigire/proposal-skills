# Project Controls and Earned Value Reference

Synthesised from: Lewis (*Project Planning, Scheduling & Control*, 6th ed.), Weiler & Serna (*Practical Strategies for Applied Budgeting and Fiscal Administration*, 2016).

This reference covers project tracking, performance measurement, scheduling techniques, and control frameworks for use in methodology sections, work plans, and project management plans.

---

## 1. The Lewis Method of Project Management (10 Steps)

A comprehensive methodology conforming to the five PMBOK process groups. Use as a named framework in methodology sections.

**INITIATION**
1. **Define the problem** — a project is "a problem scheduled for solution" (Juran). Develop shared understanding.
2. **Develop vision and mission** — Vision = what the end result looks like; Mission = what you are going to do.

**PLANNING: STRATEGY**
3. **Develop project strategy** — overall game plan (not tactics). Compare alternatives before selecting approach.
4. **Evaluate SWOT and risks** — strategic-level risk assessment. If unacceptable, revise strategy.
5. **Develop objectives** — specific, measurable objectives derived from strategy.

**PLANNING: IMPLEMENTATION**
6. **Detailed implementation planning:**
   - 6a. Develop the Work Breakdown Structure (WBS)
   - 6b. Estimate activity durations and resource requirements
   - 6c. Develop the project schedule (network diagram, critical path)
   - 6d. Identify and assign resources; perform resource levelling
   - 6e. Assess implementation risks; if unacceptable, revise plan
   - 6f. Develop the project budget baseline
   - 6g. Get plan sign-off from stakeholders

**EXECUTION AND CONTROL**
7. **Execute the plan**
8. **Monitor and control** — compare actual to planned; take corrective action
9. **Review project status** — status, design, and process reviews

**CLOSEOUT**
10. **Close out the project** — lessons learned, documentation, formal acceptance

**Key principles:**
- People who must do the work should do the planning (commitment + collective intelligence)
- Common failure: jumping from concept (Step 1) directly to execution (Step 7), skipping all planning

---

## 2. Work Breakdown Structure (WBS)

A hierarchical decomposition of project scope into manageable work packages.

**Construction rules:**
- Break work down until tasks are small enough to estimate with reasonable accuracy
- Tasks at the lowest level should be short enough to monitor meaningfully (typically 1-2 weeks)
- WBS is the basis for: scheduling, budgeting, risk identification, resource assignment, and progress tracking
- For each task, ask: "What could go wrong?" — this drives risk identification

**Proposal application:** Reference the WBS as a planning tool: "During inception, we will develop a detailed Work Breakdown Structure decomposing the assignment into manageable work packages, each with defined deliverables, resource requirements, and risk assessments."

### WBS Dictionary

Use a short WBS dictionary to define what each work package actually means.

| Field | Purpose |
|---|---|
| WBS code | Unique identifier |
| Work package name | Short deliverable-oriented label |
| Description | What is included |
| Owner | Responsible lead |
| Inputs | What must be available before work starts |
| Completion rule | How the team knows the package is done |
| Dependencies | Upstream and downstream links |

This is valuable in proposals because it converts the WBS from a list into a control mechanism.

### Task Responsibility Matrix

After the WBS is defined, map responsibility explicitly.

| Work Package | Responsible | Support | Review | Approve |
|---|---|---|---|---|
| [WP-1] | [Lead] | [Support roles] | [Reviewer] | [Approver] |

Use this where the evaluator needs confidence that work packages, experts, and approvals are aligned.

---

## 3. Estimation Techniques

### PERT Three-Point Estimation

Uses three estimates for a weighted average duration:

```
Expected Duration (te) = (o + 4m + p) / 6
```

Where:
- o = optimistic estimate (everything goes well)
- m = most likely estimate
- p = pessimistic estimate (everything goes badly)

**Standard deviation:**
```
σ = (p − o) / 6
```

**Project duration confidence:** Sum the variances (σ²) along the critical path, then take the square root for project standard deviation. Use normal distribution to determine the probability of finishing by a given date.

**Practical guidelines:**
- All estimates are person-specific — what one person can do has no bearing on what another can do
- Estimates improve with organisational maturity and historical data
- Deadlines are the most motivating factor in creative work (de Bono)
- Always present estimates as ranges, not single figures

---

## 4. Scheduling Frameworks

### Schedule Hierarchy

Build the schedule in layers:
1. major phases and contractual milestones
2. work-package schedule under each phase
3. detailed task network only where control is needed

This keeps proposal schedules readable while preserving enough structure for execution planning.

### Critical Path Method (CPM)

**Key concepts:**
- **Critical path** = longest path through the network; any slip on this path delays the project
- **Float/Slack** = amount of time a non-critical task can slip without affecting project end date
- **Total Float** = Latest Start − Earliest Start
- **Free Float** = Earliest Start of successor − Earliest Finish of current activity
- Activities with zero total float are on the critical path

**Network computation:**
1. **Forward pass:** Calculate Earliest Start (ES) and Earliest Finish (EF) for each activity
2. **Backward pass:** Calculate Latest Start (LS) and Latest Finish (LF) for each activity
3. Identify the critical path (all activities where ES = LS)

**Two universal network rules:**
1. Before a task can begin, all tasks immediately preceding it must be completed
2. Arrows denote logical precedence only, not time

### Resource Levelling

Initial schedule computation ignores resource constraints. After computing the critical path:
1. Allocate resources to tasks
2. Identify over-allocation (resource conflicts)
3. Level by delaying non-critical tasks within their float
4. If levelling extends the project, escalate — additional resources or scope reduction required

**Proposal application:** In work plan narratives, describe the scheduling approach: "Activities are sequenced using critical path analysis. Non-critical activities are scheduled with float to absorb delays without affecting the overall timeline."

### Decision-Gate Calendar

For review-heavy assignments, show client decisions as part of the schedule, not side notes.

| Gate | Trigger | Required Input | Decision |
|---|---|---|---|
| Gate 1 | Inception report submitted | Scope confirmation, work plan, stakeholder list | Approve or refine mobilisation basis |
| Gate 2 | Diagnostic findings completed | Current-state evidence and gap summary | Confirm solution direction |
| Gate 3 | Draft deliverable submitted | Draft report or design package | Approve, revise, or hold |

This is a strong pattern for donor, regulatory, and public-sector assignments where client review time determines the real critical path.

---

## 5. Earned Value Analysis (EVA) — Complete System

The standard method for tracking project cost and schedule performance simultaneously.

### Three Core Measures

| Term | Abbreviation | Meaning |
|---|---|---|
| Planned Value | PV | What was supposed to be done (budgeted cost of work scheduled) |
| Earned Value | EV | What has actually been done, valued at budget rates |
| Actual Cost | AC | What has been spent to do the work |

### Variance Formulas

| Variance | Formula | Interpretation |
|---|---|---|
| **Schedule Variance (SV)** | EV − PV | Negative = behind schedule |
| **Cost Variance (CV)** | EV − AC | Negative = over budget |
| **Budget Variance (BV)** | PV − AC | Spending versus plan |

### Performance Indices

| Index | Formula | Meaning |
|---|---|---|
| **Schedule Performance Index (SPI)** | EV / PV | Work efficiency (< 1.0 = behind) |
| **Cost Performance Index (CPI)** | EV / AC | Spending efficiency (< 1.0 = over budget) |
| **Critical Ratio (CR)** | SPI × CPI | Combined performance index |

### Estimate at Completion (EAC) — Forecasting Final Cost

```
EAC = AC + (BAC − EV) / cumulative CPI
```

Where BAC = Budget at Completion (original total budget).

### Critical Ratio Control Limits

| CR Range | Status | Action |
|---|---|---|
| 0.8 − 1.2 | Green | Acceptable deviation |
| 0.6 − 0.8 or 1.2 − 1.3 | Yellow | Investigate; identify corrective action |
| Below 0.6 | Red | Inform management; candidate for re-planning or cancellation |
| Above 1.3 | Red | Validate data; possible sandbagged estimates; reallocate funds |

### The 15% Rule

If a project is 15% into its timeline and in trouble, it will stay in trouble. A study of 800 defence contracts found that not a single project in trouble at the 15% mark ever recovered (Fleming and Koppelman, 1996).

**Proposal application:** Reference early warning indicators: "We apply the 15% checkpoint principle — if schedule or cost performance indices fall below 0.8 within the first 15% of the project timeline, we initiate a formal corrective action review with the client."

### Four Earned Value Scenarios

| Scenario | Status | Most Likely Cause | Response |
|---|---|---|---|
| EV < PV, AC > PV | Behind and overspent | Inefficiency or bad estimates | Scope reduction or re-planning |
| EV > PV, AC = EV | Ahead, spending correctly | More resources applied than planned | Monitor cash flow |
| EV < PV, AC = EV | Behind, spending correctly | Lack of resources | Catching up will almost certainly blow the budget |
| EV > PV, AC < EV | Ahead and underspent | Sandbagged estimates | Reallocate surplus |

---

## 6. Project Control Framework

### Definition

Control = comparing where you are to where you are supposed to be, and taking corrective action when there is a deviation.

**Fundamental principle:** If you have no plan, you have no control.

### Three Monitoring Questions

1. What is the actual status of the work?
2. When there is a deviation, what caused it?
3. What should be done to correct for any deviation?

### Four Possible Responses to Deviations

1. **Ignore** the deviation (only if within tolerance and no trend)
2. **Correct** — take action to get back on track
3. **Revise** — update the plan to accept the new reality
4. **Cancel** the project or workstream

---

## 7. Change Control Process

**The problem:** Scope creep — stakeholders ask for "small" changes that accumulate into major cost and schedule overruns.

**Formal change control process:**
1. Assess the impact of the requested change on schedule, cost, and performance
2. Communicate the impact to the requestor
3. If the requestor accepts the impact, initiate the formal change procedure
4. Change Approval Board reviews all possible effects
5. Only required reviewers sign off
6. Log all scope changes and their effect on work budget, reserve, and margin

**Proposal application:** Include change control in the governance section: "All scope changes will be assessed for impact on timeline, budget, and deliverable quality before approval. No change will be implemented without written agreement from the client."

---

## 8. Three Types of Project Reviews

| Review Type | Focus | Key Questions |
|---|---|---|
| **Status Review** | PCTS targets | On schedule? On budget? Scope correct? Performance acceptable? |
| **Design Review** | Product/deliverable design | Meets requirements? Fit for purpose? Stakeholder-approved? |
| **Process Review (Lessons Learned)** | How work is being done | What are we doing well? What do we want to improve? |

### Lessons Learned Facilitation Method (Lewis)

**Two questions only:**
1. What are we doing well? (labelled "Done Well")
2. What do we want to improve? (labelled "Do Better")

**Never ask:** "What did we do wrong?" — raises defences, kills participation.

**Process:**
- Two flipcharts: "Done Well" and "Do Better"
- Comments must be specific and verifiable by direct observation
- Multivoting: each person gets 10 votes to cast for priority items
- Select no more than 4 items at a time for resolution
- Assign action owner and target date for each item

**Resolution priority order:**
1. Goals (unclear goals may cause all other problems)
2. Roles and responsibilities
3. Procedures
4. Relationships (often caused by issues in categories 1-3)

---

## 9. Stoplight Reporting

Display project status using traffic-light colours at the task level:

| Colour | Status | Backed by |
|---|---|---|
| **Green** | On track | CR 0.8 − 1.2 |
| **Yellow** | Needs attention | CR in warning range |
| **Red** | Problem | CR outside acceptable limits |

Show transitions between reporting periods (yellow-to-red = worsening; yellow-to-green = improving). Must be backed by earned value data, not subjective assessment.

---

## 10. Stagegate Process (Cooper)

Decision gates between project phases to prevent continuing projects that should be stopped.

**Stages:** Conception → Formulating vision → Screening → Planning → Execution

Between each stage sits a **Gate** — a decision point where the project is evaluated for continuation, redirection, or cancellation.

**Proposal application:** Reference stagegate as a governance mechanism: "Our methodology incorporates decision gates between each phase. At each gate, the steering committee reviews deliverables, assesses progress, and decides whether to proceed, adjust, or stop."

---

## 11. Variance Analysis Tools (Weiler)

### Mean Absolute Deviation (MAD)
```
MAD = Σ|Actual − Forecast| / n
```
Average absolute forecast error. Weights error linearly.

### Root Mean Squared Error (RMSE)
```
RMSE = √[Σ(Actual − Forecast)² / (n − 1)]
```
Gives heavier weight to larger errors.

### Mean Absolute Percentage Error (MAPE)
```
MAPE = (1/n) × Σ(|error| / Actual × 100)
```
Expresses accuracy in percentage terms. Less than 5% = generally good.

### Control Chart Method

1. Calculate RMSE
2. Set acceptable standard deviation limits (1 SD = 68%, 2 SD = 95%, 3 SD = 99%)
3. Plot variance values over time against upper and lower control limits
4. Look for: values outside limits, trends, cycling patterns, bias

**Proposal application:** When a methodology involves monitoring performance indicators, reference the control chart approach: "Key performance indicators will be tracked using control charts with 2-sigma limits, enabling early detection of systemic deviations."

---

## 12. High-Performance Project Management Maturity Model (Lewis)

Five levels of project management maturity:

| Level | Name | Description |
|---|---|---|
| 1 | Bare Awareness | Ad hoc; no standard processes |
| 2 | Minimal Performance | Basic processes; inconsistent application |
| 3 | Bronze | Standardised processes; consistent application |
| 4 | Silver | Processes measured with performance data |
| 5 | Gold | Continuous improvement embedded |

**Key insight:** Most organisations require approximately one year per level. Experience cannot be accelerated beyond certain limits.

**Proposal application:** When assessing client PM capability, use this maturity model to frame the current state and define a realistic target state.

---

## 13. The Multitasking Problem (Lewis)

Organisations try to do too many projects with limited resources. Constant task-switching incurs "setup time" (reorientation) that adds no value.

**Solution:** Prioritise projects. Give each person a priority-one project and a backup. Work on priority-one whenever possible; use backup to fill dead time.

**Result:** One company nearly doubled productivity by eliminating multitasking.

**Proposal application:** When designing team deployment plans, avoid splitting team members across too many concurrent assignments. Show dedicated resource allocation in the staffing schedule.

---

## 14. Quality Tracking Indicators (Lewis)

Track these metrics during project execution:

- Rework hours (expect 5-40% rework; should decline with process improvement)
- Documentation changes
- Design revisions
- Client complaints or change requests
- Test failures
- Scope changes (track dollar impact, not just count)

**Run chart interpretation:**
- Seven consecutive points on one side of the average = something significant is happening
- Seven or more intervals steadily increasing/decreasing = systemic change, not chance

**Proposal application:** Reference quality monitoring in the QA section: "We track rework rates, change request volumes, and client feedback scores as leading indicators of deliverable quality. Trends are reviewed weekly and acted upon before they affect outcomes."
