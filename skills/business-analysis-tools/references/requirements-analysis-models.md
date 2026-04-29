# Requirements Analysis Models

Structured visual and textual models for examining, decomposing, and clarifying requirements. Models are the analyst's primary tool for turning elicitation results into verified, validated requirements.

---

## Model Categories

| Category | Models | What They Show |
|---|---|---|
| **Scope Models** | Context Diagram, Ecosystem Map, Feature Model, Goal Model, Use Case Diagram | Boundaries, actors, and high-level capabilities |
| **Process Models** | Process Flow, Use Case, User Story | How work is performed, actor-system interactions |
| **Rule Models** | Business Rules Catalogue, Decision Tree, Decision Table | Conditions, constraints, and decision logic |
| **Data Models** | Entity Relationship Diagram, Data Flow Diagram, Data Dictionary, State Table/Diagram | Information structure, movement, and lifecycle |
| **Interface Models** | Wireframes, Display-Action-Response, Report Table, System Interface Table, User Interface Flow | How users and systems interact with the solution |

---

## Scope Models

### Context Diagram
- Shows the system boundary and external entities with data flows
- Defines what is in scope and out of scope
- **Proposal use:** "We will develop a context diagram to map all external systems and data flows interacting with the [solution]."

### Ecosystem Map
- Shows external entities interacting with the system or organisation
- Broader view than a context diagram — includes upstream/downstream relationships
- **Proposal use:** "Our inception phase will produce an ecosystem map identifying all stakeholders and systems that interact with the [solution]."

### Feature Model
- Hierarchical decomposition of product capabilities (first, second, third level features)
- Shows what the solution will do at a high level
- **Proposal use:** "We will decompose the solution scope into a feature model with prioritised capabilities."

### Goal Model / Business Objectives Model
- Visually shows business goals and how objectives support them
- Links goals to business cases and projects
- **Proposal use:** "We will map ToR objectives to measurable business goals using a goal decomposition model."

### Use Case Diagram
- Shows all in-scope use cases and which actors participate
- Quick visual of system scope and actor relationships
- Uses ovals (use cases), stick figures (actors), arrows (associations)

---

## Process Models

### Process Flow
- Steps taken by a human user interacting with a system or performing work
- Can show as-is and to-be processes
- Useful for root cause analysis and gap identification
- **Components:** Activities, events, directional flows, decision points, roles/functions
- **Notations:** BPMN, UML Activity Diagram, Swimlane Diagrams, SIPOC

### Process Description Template

For each process, capture:

| Element | Description |
|---|---|
| **Process name** | Verb-noun format (e.g., Validate Order) |
| **Description** | Why the process is important |
| **Trigger** | What starts the process |
| **Sequence** | What processes follow |
| **Business rules** | Constraints guiding the process |
| **Data elements** | Inputs, outputs, stored data |
| **Metrics** | Time, frequency, volume |
| **Roles** | Who performs it, who benefits |

### Use Case
- Describes actor-system interactions and boundaries
- Includes trigger, actors, preconditions, postconditions
- Main success scenario (happy path) + alternate and exception flows

**Use Case Template:**

| Element | Detail |
|---|---|
| Use Case Name | Noun-verb format |
| Goal/Outcome | What the actor achieves |
| Actors | Who interacts |
| Preconditions | What must be true before |
| Trigger | What starts the use case |
| Flow of Events | Primary path (happy path) |
| Alternative Paths | Other valid paths to the goal |
| Exception Flows | Error conditions |
| Post-conditions | What is true after completion |
| Business Rules | Referenced rules (BR1, BR2...) |

**Scenario types:**
- **Main scenario** — positive flow (happy path) in normal conditions
- **Alternative scenarios** — other possible ways of achieving the same goal
- **Exception scenarios** — activities in exceptional and error conditions (must always be addressed)

### User Story
- One or two sentences from the actor's viewpoint
- **Format:** "As a [role], I want [function], so that [benefit]"
- Used in agile/adaptive life cycles
- Acceptance criteria define conditions for satisfaction

**INVEST Criteria for User Stories:**
- **I**ndependent — can be developed separately
- **N**egotiable — details can be discussed
- **V**aluable — delivers value to the user
- **E**stimable — team can estimate effort
- **S**mall — fits in one iteration
- **T**estable — can be verified

---

## Rule Models

### Business Rules Catalogue
- Documents business rules in tabular format
- Includes rule ID, description, source, type, and related requirements
- **Key insight:** Rules should be defined and maintained separately from processes, use cases, and data structures
- **Best practice:** Define rules parametrically (e.g., "commission rate" not "1 percent") using references (BR1, BR2...)
- **Finding rules:** Listen for decision words: verify, validate, check, determine, assess

### Decision Tree
- Visual representation of decision logic
- Shows conditions and resulting actions
- Useful for complex conditional logic

### Decision Table
- Tabular representation of conditions and actions
- Shows all possible combinations of conditions
- Useful for verifying completeness of business rules

---

## Data Models

### Entity Relationship Diagram (ERD)
- Shows entities, their attributes, and relationships
- Uses notation like Crow's Foot for cardinality (1-to-1, 1-to-N, N-to-N)
- Three levels: conceptual (technology-independent), logical (normalised), physical (implementation)

### Data Flow Diagram (DFD)
- Shows how data moves through a system
- Includes processes, data stores, external entities, and data flows
- Shows transformation of data — where it comes from, what processes it, where it is stored/consumed

### Data Dictionary
- Standard definition of data elements
- Includes metadata, usage, applicable values, composite values
- Facilitates data reuse and sharing

### State Table and State Diagram
- Shows all possible states of an object and valid transitions
- State diagram is visual; state table is tabular
- Helps enumerate all possible states in the lifecycle of an object

---

## Interface Models

### Wireframes and Display-Action-Response (DAR)
- **Wireframes:** Visual layout of screen elements
- **DAR:** Documents what is displayed, what action the user takes, and what the system responds with

### Report Table
- Documents all requirements for developing a single report
- Includes top-level elements and field-level elements

### System Interface Table
- Documents connections between interfacing systems
- How they connect and what information flows between them
- **Defines:** Who interacts, what information is exchanged, frequency, location, why the interface exists

### User Interface Flow
- Shows pages/screens and how users navigate between them

---

## Functional Decomposition

- Break complex systems into manageable pieces
- **Rules for building:**
  - Only one type of relationship (parent to child)
  - Only one type of requirement per diagram
  - Every parent has more than one child
  - No sequence shown (no arrows)
  - Child must be at lower level than parent
- **Tip:** Draft a diagram first, then show to SMEs for feedback

---

## Modelling Languages

| Language | Use |
|---|---|
| **BPMN** | Business Process Model and Notation — process modelling standard |
| **UML** | Unified Modeling Language — broad modelling notation |
| **SysML** | System Modeling Language — systems engineering |
| **RML** | Requirements Modeling Language |

---

## Choosing Models

**Three primary presentation approaches:**
1. **Text** — Easy to produce, anyone can review; but gets long and can be ambiguous
2. **Visuals** — Diagrams, models, mock-ups; gets stakeholders into the solution; takes more planning
3. **Combination** — Most common and most effective; diagrams with labels, annotations, and textual descriptions

**Selection criteria:**
- Know your stakeholders (accountants prefer spreadsheets; marketing prefers visual)
- Consider the project approach (waterfall requires more formal models; agile favours lightweight)
- Give SMEs small chunks to review
- Create models live with stakeholders when possible; share immediately for feedback

---

*Synthesised from: PMI Guide to Business Analysis (2017), Business Analysis for Practitioners (PMI, 2015), Business Analysis Methodology Book (Yayici, 2015), Seven Steps to Mastering Business Analysis (Champagne, 2019).*
