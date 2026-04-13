# Requirements Documentation

Standards, formats, and quality criteria for documenting requirements. Relevant to proposal sections that describe how the firm will capture, test, trace, and package client requirements for delivery teams and decision-makers.

Synthesised from PMI business analysis guidance and Robertson & Robertson's requirements practice.

---

## 1. Requirement Types

| Type | Description | Responsibility |
|---|---|---|
| **Business Requirements** | Higher-level needs of the organisation; reasons for the initiative; measurable goals | Defined before or during project initiation |
| **Stakeholder Requirements** | Needs of a stakeholder or stakeholder group that may affect or be affected by the solution | Identified through elicitation |
| **Solution Requirements - Functional** | Observable behaviours of the product or service; what it must do | Defined during analysis |
| **Solution Requirements - Nonfunctional** | Performance, security, usability, scalability, reliability, and similar qualities | Defined during analysis |
| **Transition Requirements** | Temporary capabilities needed to move from current to future state | Often missed; capture explicitly |
| **Technical Requirements** | Detailed specifications for architecture, interfaces, databases, controls, and infrastructure | Developed from solution requirements |

### Discovery Sequence

When the assignment is still problem-heavy, document requirements in this order:
1. business problem and value sought
2. goals and scope
3. context diagram and external interfaces
4. stakeholder groups and customer segments
5. business events and major workflows
6. functional, nonfunctional, transition, and technical requirements

This reduces the risk of documenting features before the team understands the work.

### Nonfunctional Requirements Checklist

Accessibility, auditability, availability, compatibility, compliance, efficiency, extensibility, maintainability, performance, portability, reliability, resilience, safety, scalability, security, service continuity, usability, and learnability.

---

## 2. Requirements Hierarchy

| Level | Description |
|---|---|
| **Themes** | Broad areas of focus across the organisation or programme |
| **Initiatives** | Groupings of work that achieve a common outcome |
| **Epics** | Larger capability statements that must be broken down |
| **User Stories / Use Cases** | Implementable slices of behaviour or workflow |
| **Acceptance / Fit Criteria** | Conditions that prove the requirement has been met |

Use higher-level structures for executive alignment and lower-level structures for delivery and testing.

---

## 3. Core Documentation Formats

### Use Case Document

| Element | Content |
|---|---|
| **Use Case ID and Name** | Verb-noun format, e.g. Approve Payment |
| **Triggering Event** | What starts the use case |
| **Actors** | Who interacts with the system or process |
| **Preconditions** | What must be true before the use case begins |
| **Postconditions** | What is true after the use case completes |
| **Normal Flow** | Step-by-step actor and system interaction |
| **Alternate Flows** | Valid deviations from the normal flow |
| **Exception Flows** | Error conditions and failed paths |
| **Business Rules** | Referenced rules, constraints, and calculations |
| **Nonfunctional Requirements** | Performance, security, usability, and quality constraints |
| **Assumptions** | Conditions outside the user's control |

Best practices:
- make each scenario step correspond to a functional requirement
- separate normal, alternative, and exception flows
- describe user and business behaviour, not screen design
- define business rules parametrically where possible
- make nonfunctional requirements verifiable

### User Story

Format: "As a [role], I want [function], so that [benefit]"

Use the `Card / Conversation / Confirmation` pattern:
- **Card** for the short requirement statement
- **Conversation** for clarification with stakeholders and the team
- **Confirmation** for the acceptance criteria

Apply INVEST:
- **Independent**
- **Negotiable**
- **Valuable**
- **Estimable**
- **Small**
- **Testable**

### Business Event Catalogue

Use this when discovery is organised around triggers rather than screens or departments.

| Event ID | Trigger | Actor/Source | Expected Outcome | Priority | Related Use Case/Story |
|---|---|---|---|---|---|
| BE-001 | [What happens] | [Who or what triggers it] | [What the business must achieve] | [H/M/L] | [Link] |

This is especially useful in service delivery, workflow automation, and case-management assignments.

### Business Rules Catalogue

| Rule ID | Rule Description | Source | Type | Related Requirements |
|---|---|---|---|---|
| BR-001 | [Condition and action] | [Policy/regulation/SME] | [Constraint/action/computation] | [Req IDs] |

Listen for phrases such as `always`, `never`, `if`, `when`, `only when`, `validate`, `assess`, and `determine`.

---

## 4. Documentation Principles

### Just Enough

- keep documentation concise without starving delivery teams of needed detail
- use diagrams to reduce text where they improve clarity
- calibrate detail to project risk, complexity, and sourcing model
- add more structure when work is distributed, outsourced, or regulated

### Just in Time

| Question | Document | Content |
|---|---|---|
| **Why** | Business case / vision and scope | Business requirements |
| **What** | Use case set / user stories | Stakeholder and functional requirements |
| **How** | Requirement package / rules catalogue | Nonfunctional requirements and business rules |
| **Technically How** | Technical design documents | Architecture and system design |

### Formality Ranges

| Deliverable | Informal Format | Formal Format |
|---|---|---|
| Situation Statement | Verbal discussion | Documented analysis |
| Business Case | Elevator pitch | Full business case document |
| Stakeholder Register | Informal list | Detailed register with analysis |
| Requirements | User stories on cards | Requirements specification document |
| Models | Whiteboard sketches | Formal UML/BPMN diagrams |
| Traceability | Story map | Requirements traceability matrix |

### Context and Scope Models

Use lightweight visual models early:

| Model | Purpose |
|---|---|
| **Context diagram** | Define the boundary of the work and the major external interfaces |
| **Stakeholder map** | Show who can supply, approve, block, or use the solution |
| **Process model** | Show work sequence, handoffs, and exceptions |
| **Data model** | Define key business objects and relationships |

These models reduce ambiguity faster than prose alone.

---

## 5. Quality Criteria for Requirements

| Quality | Description |
|---|---|
| **Unambiguous** | Only one interpretation is possible |
| **Precise** | Avoid vague terms such as fast, user-friendly, and easy |
| **Consistent** | Terminology is used uniformly |
| **Correct** | No unintended design or implementation detail |
| **Complete** | Contains the information needed to implement and verify |
| **Measurable/Testable** | Can be checked against objective criteria |
| **Traceable** | Links back to a business need or decision |
| **Feasible** | Can realistically be implemented |
| **Independent** | Not locked to a premature design choice |
| **Necessary** | Each requirement serves an agreed objective |
| **Prioritised** | Value and urgency are explicit |

### Fit Criteria

Attach a fit criterion to important requirements so they can be measured and tested.

| Requirement Type | Example Requirement | Fit Criterion |
|---|---|---|
| **Functional** | The system shall notify supervisors of overdue approvals | Notification sent within 5 minutes of breach and logged in the audit trail |
| **Nonfunctional** | The portal shall be easy to use | 90% of first-time users complete registration unaided in usability testing |
| **Transition** | Staff shall be ready for go-live | 100% of targeted users complete role-based training before cutover |

Fit criteria are the strongest defence against vague words such as `easy`, `fast`, `robust`, and `user-friendly`.

---

## 6. Verification and Validation

| Activity | Question | Methods |
|---|---|---|
| **Verification** | Are we building the product right? | Peer reviews, inspections, checklists, INVEST, fit criteria |
| **Validation** | Are we building the right product? | Structured walkthroughs, prototypes, traceability to business needs |

---

## 7. Requirements Package Contents

A complete requirements package includes:
- table of contents
- executive summary
- reviewer instructions
- requirements in text and model form
- glossary of terms
- assumptions, constraints, and out-of-scope items
- links to electronic records or repositories
- fit criteria or acceptance criteria for critical requirements
- transition requirements where rollout, migration, or training matters

### Glossary Best Practices

- start capturing key terms from the first discovery sessions
- agree terminology across stakeholders early
- always include a glossary when requirements go to vendors, consultants, or external reviewers

---

## 8. Key Document Types

| Document | Purpose |
|---|---|
| **Business Requirements Document (BRD)** | Higher-level business needs, goals, and objectives |
| **Software Requirements Specification (SRS)** | Functional and nonfunctional requirements |
| **Business Case** | Justification for investment and change |
| **Vision and Scope Document** | Scope definition for small or medium assignments |
| **Statement of Work (SOW)** | Concise statement of business need and work to be done |
| **Requirements Traceability Matrix** | Link requirements to origin, design, test, and implementation |
