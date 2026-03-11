# Traceability and Change Control

Tools and processes for tracking requirements from origin to deliverable, managing the requirements lifecycle, and controlling changes. Relevant to methodology sections that describe quality assurance, governance, and requirements management approaches.

---

## Requirements Traceability

### What Is Traceability?

Traceability provides the ability to track product requirements from their origin to the deliverables that satisfy them. It creates linkages between different levels and types of requirements.

### Benefits of Tracing Requirements

- Ensures all requirements map to business needs
- Identifies out-of-scope requirements (those not traced to a business need)
- Identifies gaps (business needs without corresponding requirements)
- Enables impact analysis for proposed changes
- Supports test coverage verification
- Facilitates change management
- Prevents scope creep
- Validates all deliverables are completely delivered

### Requirements Traceability Matrix (RTM)

A grid linking product requirements from their origin to the deliverables that satisfy them.

| Req ID | Description | Source | Business Need | Priority | Status | Design Component | Test Case | V&V Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | [Description] | [Source] | [BN-ID] | [H/M/L] | [State] | [Component] | [TC-ID] | [Pass/Fail] |

### Requirements Attributes

Common attributes stored in the traceability matrix:

| Attribute | Purpose |
|---|---|
| Requirement ID | Unique identifier |
| Description | What the requirement specifies |
| Source | Where it originated (stakeholder, document, regulation) |
| Priority | Relative importance (MoSCoW, H/M/L) |
| Status/State | Current lifecycle state |
| Author | Who documented it |
| Date created/modified | Audit trail |
| Complexity | Implementation difficulty |
| Acceptance criteria | How to verify it is met |
| Requirement type | Business, stakeholder, solution, transition |
| Associated test cases | Verification linkage |

### What to Trace

**Predictive (waterfall) projects:**
- Business needs, goals, objectives
- Project objectives and scope / WBS deliverables
- Product design components
- Product development components
- Test strategy and test scenarios
- High-level to detailed requirements (and reverse)
- Related functional requirements across different areas

**Adaptive (agile) projects:**
- Epics or user stories to features and acceptance tests
- Kanban boards may provide some traceability
- Product roadmaps for traceability across releases
- Backlogs trace requirements to goals

**Proposal language:** "We will establish a Requirements Traceability Matrix linking ToR objectives → requirements → design components → test cases, ensuring full coverage and auditability throughout the assignment."

---

## Requirements Lifecycle

Requirements move through defined states:

| State | Description |
|---|---|
| **In-Process** | Being developed/elicited |
| **Drafted** | Initial version complete |
| **Approved** | Accepted by stakeholders |
| **Baselined** | Part of the formal baseline; changes require change control |
| **Deferred** | Postponed to future iteration/release |
| **Rejected** | Not accepted |
| **Implemented** | Built into the solution |
| **Verified** | Tested and confirmed correct |

### Baselining Requirements

A **requirements baseline** is the approved set of requirements that serves as the foundation for product development. Changes after baselining must go through formal change control.

**Relationship:** Requirements Baseline ↔ Product Scope ↔ Project Scope

---

## Change Control

### When Changes Are Proposed

Assess impact on:
1. **Requirements baseline** — Does it change approved requirements?
2. **Other requirements** — Does it conflict with existing requirements?
3. **Business analysis deliverables** — What BA artifacts need updating?
4. **Project management** — Schedule, cost, resources, risk impacts

Then recommend a course of action with full scope, risk, schedule, and cost implications.

### Change Control Tools

| Tool | Purpose |
|---|---|
| **Configuration Management System (CMS)** | Manages and controls changes to project deliverables; ensures consistency and traceability |
| **Version Control System (VCS)** | Tracks history of revisions; maintains audit trail of who changed what and when |
| **Change Request Log** | Records all proposed changes with status, impact assessment, and decision |
| **Impact Analysis** | Evaluates how a change affects requirements, product, and project |

### Impact Analysis Process

1. Receive change request
2. Trace affected requirements using the RTM
3. Identify all upstream and downstream impacts (the "butterfly effect" — a minor change can cascade through multiple components)
4. Assess impact on scope, schedule, cost, risk, and quality
5. Present impact assessment to decision-makers
6. Document decision and update baseline if approved

### Change Request Prevention

Change requests are a primary source of waste because they:
- Cannot be planned
- Result in scope creep
- Cause analysis paralysis
- Generate hidden costs
- Are mostly urgent
- Have direct and indirect impacts on various components
- May bring regression-testing burden

**Root cause of most CRs:** Problems and deficiencies in requirements gathering, documentation, and management process.

**Prevention strategies:**
- Invest in thorough upfront elicitation
- Use multiple elicitation techniques for validation
- Include diverse stakeholders early
- Verify and validate requirements before baselining
- Define acceptance criteria clearly
- Maintain traceability to catch gaps early

---

## Relationships and Dependencies

### Establishing Relationships

Use these tools to map how requirements relate to each other:

| Tool | Purpose |
|---|---|
| **Feature Model** | Hierarchical decomposition of capabilities |
| **Story Mapping** | Visual layout of user stories by workflow and priority |
| **Story Slicing** | Breaking stories into smaller, implementable pieces |
| **Requirements Management Tool** | Automated relationship tracking |

### Selecting and Approving Requirements

Tools for approval decisions:

| Tool | Purpose |
|---|---|
| **Backlog Management** | Prioritising and grooming the product backlog |
| **Definition of Ready** | Criteria a requirement must meet before development |
| **Definition of Done** | Criteria a requirement must meet to be considered complete |
| **Facilitated Workshops** | Group review and approval sessions |
| **Prioritisation Schemes** | MoSCoW, weighted ranking, multivoting |

---

## Governance and Sign-Off

### Formal Approach (Predictive Projects)
- Structured walkthroughs with stakeholders
- Official sponsor signature on requirements document
- Formal change control board for post-baseline changes

### Informal Approach (Adaptive Projects)
- Team reviews together; product owner prioritises
- Iteration/sprint planning serves as the sign-off equivalent
- Continuous approval through each iteration

### Requirements Review Process (8 Steps)
1. Have a clear objective for the review
2. Schedule time with participants
3. Distribute review materials in advance
4. Have participants review materials prior to session
5. Conduct the review session
6. Record feedback and changes; update material
7. Share material for awareness and final confirmations
8. Conduct second review only if absolutely necessary

**Key principle:** "Getting sign-off should be about validating the stakeholders' understanding of how they will be achieving the desired value."

---

*Synthesised from: PMI Guide to Business Analysis (2017), Business Analysis for Practitioners (PMI, 2015), Business Analysis Methodology Book (Yayici, 2015), Seven Steps to Mastering Business Analysis (Champagne, 2019).*
