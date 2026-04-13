# System Reconstruction

## What The Repository Is Trying To Be

The repository is designed as a modular proposal engine with four layers:

1. **Routing layer**
2. **Strategy and persuasion layer**
3. **Section-generation layer**
4. **Procurement, sector, and domain support layer**

In concept, the engine should convert:

`ToR / RFP / REOI -> BRIEF.md -> section drafts -> tables/forms -> compiled technical and financial submissions`

That is the intended operating model.

## The Intended Proposal Lifecycle

### 1. Intake

The user starts from the root `SKILL.md`, which routes the task by document type.

Expected intake inputs:

- ToR, RFP, advert, or EOI notice
- proposer identity
- procurement framework
- sector context
- templates, deadlines, and submission rules

The repository expects proposal materials to sit in a local, gitignored proposal workspace described in `CLAUDE.md`:

- `proposals/INDEX.md`
- per-bid folder
- `terms/`
- `team/`
- `research/`
- `sheets/`
- `output/`

### 2. Proposal Workspace Creation

`CLAUDE.md` describes an operating pattern where each bid gets a folder such as:

- `proposals/YYYY-MM-DD-short-name/`

with:

- `BRIEF.md`
- one markdown file per section
- support folders for terms, CVs, research, sheets, and outputs

This signals the intended architecture: proposals are supposed to be managed as projects, not one-off prompts.

### 3. Brief Creation

This is the conceptual heart of the system.

The repository says the engine should:

- read the terms
- run a brainstorming workflow
- ask focused questions
- identify themes, frameworks, and the proposal approach
- write the result into `BRIEF.md`

In theory, `BRIEF.md` is the design spec that drives everything after that.

In practice, this is where the first major gap appears:

- the repository references a brainstorming workflow
- but there is no explicit brainstorming skill in the repo
- there is no formal `BRIEF.md` template or schema
- there is no system logic that forces later sections to inherit from the brief in a structured way

So the brief is **described**, but not yet **operationalised**.

### 4. Identity And Voice Selection

Before drafting, the system requires loading `profiles/SKILL.md`.

This layer controls:

- proposer identity
- voice (`I` vs `we`)
- signatory
- whether experience is framed as individual, company, consortium, or ghostwritten client content

This is a real strength. Many proposal systems blur proposer identity; this one does not.

### 5. Procurement And Sector Routing

The system then loads `sectors/SKILL.md` to determine:

- procurement framework
- sector domain
- country context if needed

Procurement skills shape compliance logic:

- World Bank
- PPDA Uganda
- AfDB
- UN / UNDP

Sector skills shape domain logic:

- ICT
- health
- agriculture
- governance
- education
- energy
- and others

This means the system separates:

- **how the bid is evaluated** from
- **what technical content evaluators expect**

That is the correct architecture for a serious proposal engine.

### 6. Strategy And Persuasion Layer

Before or during drafting, the repository expects use of three core reference files:

- `references/proposal-strategy-and-persuasion.md`
- `references/world-class-proposal-patterns.md`
- `references/consulting-delivery-excellence.md`

These files contain the system's strategic doctrine:

- S1 -> S2 -> B logic
- SCQA
- P-I-P
- Pyramid Principle
- buyer psychology
- theme architecture
- objection neutralisation
- Cialdini principles
- hypothesis-driven consulting logic
- ghost packs
- prewiring
- Red Team review

This is where the repository most clearly tries to move beyond writing and become a proposal engine.

### 7. Section Generation

The numbered section skills form the main production layer:

- `01-cover-letter`
- `02-executive-summary`
- `03-understanding-of-assignment`
- `04-firm-profile`
- `05-relevant-experience`
- `06-methodology`
- `07-team-composition`
- `08-work-plan`
- `09-expression-of-interest`
- `10-financial-proposal`

Each section skill provides:

- use conditions
- required inputs
- workflow
- quality standards
- anti-patterns
- output expectations

The best way to understand the engine is this:

- the brief is supposed to define the strategy
- the cross-cutting references define the persuasion architecture
- the section skills translate that architecture into section-level output

### 8. Supporting Domain Injection

Unnumbered skills act as targeted enrichers when the ToR requires them:

- project management
- stakeholder engagement
- M&E
- risk management
- GESI
- safeguards
- data management
- sustainability
- change management
- capacity building
- consulting frameworks
- business analysis tools

These are intended to upgrade section realism, especially methodology and work plan sections.

### 9. Tables, Schedules, And Commercial Outputs

The repo expects quantitative or tabular outputs to be generated separately:

- staffing schedules
- Gantt charts
- budget breakdowns
- deliverables matrices

This is sensible because high-scoring proposals often fail on table quality rather than prose quality.

### 10. Compilation And Delivery

The intended end state is:

- technical proposal compiled into `.docx`
- financial proposal compiled separately into `.docx`

The separation logic is explicit and generally donor-correct.

Again, the workflow is described more clearly than it is implemented in-repo.

## What Defines The Winning Strategy In This System

From the repository's internal logic, a winning strategy is supposed to be defined by:

- identifying the real client problem, not merely restating tasks
- expressing the bid through S1 -> S2 -> B
- selecting 3-4 proposal themes
- using SCQA and Pyramid Principle for narrative control
- using a named methodology with explicit phases and deliverables
- proving relevance through quantified experience
- matching CVs tightly to scored positions
- keeping technical and financial submissions separate

This is sound.

What is missing is a workflow step that converts those ideas into an explicit, scored bid strategy document that all later sections must obey.

## How Consistency Is Supposed To Be Enforced

Consistency is currently enforced in three ways:

1. Through instruction
2. Through repeated references to profile/sector/procurement routing
3. Through cross-cutting strategy files

That means the system depends heavily on the operator or model remembering to:

- reuse the same themes
- align scope, methodology, staffing, work plan, and budget
- avoid contradictions
- keep the same underlying story

That is not yet strong enough for a world-class engine.

World-class consistency would require explicit artefacts such as:

- win themes
- score map
- evidence map
- section message map
- staffing-to-methodology matrix
- deliverable-to-budget matrix
- contradiction checks

Those artefacts are not yet built into the workflow.

## Real-World Usage Flow Today

In practice, the repository likely works like this:

1. A consultant reads the ToR.
2. They choose the proposer profile.
3. They choose the procurement framework and sector.
4. They manually infer a strategy from the references.
5. They draft sections using the numbered skills.
6. They enrich sections with selected support skills.
7. They assemble tables and a pricing breakdown.
8. They manually reconcile inconsistencies.

That makes the system a **consultant-assist engine**, not yet a **self-coordinating proposal engine**.

## Practical Reconstruction Verdict

The repository already has the skeleton of a serious proposal OS:

- intake
- context routing
- section generation
- procurement adaptation
- domain enrichment
- tone control

But two core layers are still weak:

- the **strategic control layer** between ToR and section drafting
- the **quality control layer** between drafted sections and final submission

That is why the system can produce strong sections, but is not yet reliably a winning end-to-end proposal machine.
