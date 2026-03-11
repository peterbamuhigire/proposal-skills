# Requirements Documentation

Standards, formats, and quality criteria for documenting requirements. Relevant to proposal sections that describe how the firm will capture and manage client requirements (methodology, work plan).

---

## Requirement Types

| Type | Description | Responsibility |
|---|---|---|
| **Business Requirements** | Higher-level needs of the organisation; reasons for the initiative; measurable goals | Defined before or during project initiation |
| **Stakeholder Requirements** | Needs of a stakeholder or stakeholder group that may affect or be affected by the solution | Identified through elicitation |
| **Solution Requirements — Functional** | Observable behaviours of the product; what the system does | Defined during analysis |
| **Solution Requirements — Nonfunctional** | Environmental conditions or qualities (performance, security, usability, scalability) | Defined during analysis |
| **Transition Requirements** | Temporary capabilities needed to move from current to future state (training, data migration, communication) | Often missed — flag these in proposals |
| **Technical Requirements** | Detailed specifications for architecture, databases, interfaces, security | Developed from functional and nonfunctional requirements |

### Nonfunctional Requirements Checklist

Accessibility, auditability, availability, certification, compatibility, compliance, effectiveness, efficiency, extensibility, legal/licensing, maintainability, performance/response time, portability, quality, reliability, resource constraints, safety, scalability (horizontal and vertical), security, stability, system availability, usability and learnability.

---

## Requirements Hierarchy (Agile)

| Level | Description |
|---|---|
| **Themes** | Areas of focus across the organisation |
| **Initiatives** | Collections of epics achieving a common goal |
| **Epics** | Larger elements broken down into user stories |
| **User Stories** | Simple, concise descriptions of functionality |
| **Acceptance Criteria** | Definition of "done" for each story |

---

## Documentation Formats

### Use Case Document

**Template:**

| Element | Content |
|---|---|
| **Use Case ID and Name** | Verb-noun format (e.g., Place Order) |
| **Triggering Event** | What starts the use case |
| **Actors** | Who interacts with the system |
| **Preconditions** | What must be true before the use case begins |
| **Postconditions** | What is true after the use case completes |
| **Normal Flow** | Step-by-step actor-system interactions (happy path) |
| **Alternate Flows** | Valid deviations from the normal flow |
| **Exception Flows** | Error conditions |
| **Business Rules** | Referenced rules (BR1, BR2...) |
| **Nonfunctional Requirements** | Performance, security, usability constraints |
| **Assumptions** | Conditions where the user has no control |

**Best practices:**
- Each scenario step corresponds to a functional requirement
- Separate main, alternative, and exception scenarios
- Answer "what" and "how" questions, not "technically how"
- Write scenarios from the user's point of view without UI details
- Define business rules parametrically (e.g., "commission rate" not "1 percent")
- Define nonfunctional requirements in a verifiable way (e.g., "within two seconds" not "fast")

### User Story

**Format:** "As a [role], I want [function], so that [benefit]"

**Components:**
- **Card** — Brief description of the functionality
- **Conversation** — Discussion with the team about intent and scope
- **Confirmation** — Acceptance criteria that define when the story is done

**INVEST Criteria:**
- **I**ndependent — can be developed separately
- **N**egotiable — details can be discussed
- **V**aluable — delivers value to the user
- **E**stimable — team can estimate effort
- **S**mall — fits in one iteration
- **T**estable — can be verified

### Business Rules Catalogue

| Rule ID | Rule Description | Source | Type | Related Requirements |
|---|---|---|---|---|
| BR-001 | [Condition and action] | [Policy/regulation/SME] | [Constraint/action/computation] | [Req IDs] |

**Characteristics of well-defined rules:** Stand alone, specific, testable (verifiable whether followed or not).

**Finding rules during elicitation:** Listen for decision words — verify, validate, check, determine, assess. Listen for "always", "never", "if", "when", "only when".

---

## Documentation Principles

### "Just Enough" Principle

- Requirements documents should be concise without information overload
- Use diagrams (use case diagrams, flowcharts, context diagrams) to reduce text
- Objective is creating products that meet needs, not producing fancy documents
- Calibrate detail level to project needs
- Too little detail risks incomplete requirements and "gold plating"
- More detail needed for distributed/outsourced teams

### "Just in Time" Principle

Questions answered in order, on separate documents:

| Question | Document | Content |
|---|---|---|
| **Why** | Business case / Vision & Scope | Business requirements |
| **What** | Use case documents / User stories | User and functional requirements |
| **How** | Use case documents / User stories | Nonfunctional requirements, business rules |
| **Technically How** | Technical design documents | System requirements, architecture |

### Formality Ranges

| Deliverable | Informal Format | Formal Format |
|---|---|---|
| Situation Statement | Verbal discussion | Documented analysis |
| Business Case | Elevator pitch | Full business case document |
| Stakeholder Register | Informal list | Detailed register with analysis |
| Requirements | User stories on cards | Requirements specification document |
| Models | Whiteboard sketches | Formal UML diagrams |
| Traceability | Story map | Requirements traceability matrix |

---

## Quality Criteria for Requirements

Requirements must be:

| Quality | Description |
|---|---|
| **Unambiguous** | Only one interpretation possible |
| **Precise** | Avoid vague terms like "fast", "user-friendly", "easy" |
| **Consistent** | Terminology used uniformly throughout |
| **Correct** | No inclusion of design or implementation details unless intended |
| **Complete** | Contains all necessary information to implement |
| **Measurable/Testable** | Can be verified with specific criteria |
| **Traceable** | Can be linked back to a business need |
| **Feasible** | Can realistically be implemented |
| **Independent** | Not dependent on the design of the solution |
| **Necessary** | Each requirement traces to deliverables and objectives |
| **Prioritised** | Analysis of value has been done |

---

## Verification and Validation

| Activity | Question | Methods |
|---|---|---|
| **Verification** | "Are we building the product right?" | Peer reviews, inspections, checklists, INVEST criteria |
| **Validation** | "Are we building the right product?" | Structured walkthroughs with stakeholders, traceability to business requirements |

---

## Requirements Package Contents

A complete requirements package includes:
- Table of contents
- Executive summary
- Reviewer instructions
- Requirements in various formats (text, diagrams, models)
- Glossary of terms
- Links/references to electronic requirements
- Customised cover page indicating focus areas per stakeholder

### Glossary Best Practices

- Begin jotting down important terms from first meetings
- Define and gain agreement from all stakeholders
- Always include a glossary when requirements go to external entities (vendors, consultants)
- Eliminates ambiguous requirements from inconsistent terminology

---

## Key Document Types

| Document | Purpose |
|---|---|
| **Business Requirements Document (BRD)** | Higher-level business needs, goals, objectives |
| **Software Requirements Specification (SRS)** | Functional and nonfunctional requirements |
| **Business Case** | Comprehensive justification for project investment |
| **Vision and Scope Document** | Medium/small project scope definition |
| **Statement of Work (SOW)** | One-page business need for enhancements |
| **Requirements Traceability Matrix** | Link requirements to origin, design, test, implementation |

---

*Synthesised from: PMI Guide to Business Analysis (2017), Business Analysis for Practitioners (PMI, 2015), Business Analysis Methodology Book (Yayici, 2015), Seven Steps to Mastering Business Analysis (Champagne, 2019).*
