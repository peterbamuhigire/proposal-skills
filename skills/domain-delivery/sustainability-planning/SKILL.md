---
name: sustainability-planning
description: Use when a proposal must explain institutional, technical, financial, or human-resource sustainability, handover, exit, or post-project support. Unlike capacity-building, this skill tests whether results continue after consultant withdrawal across all operating dimensions.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Sustainability Planning
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill when the assignment explicitly needs sustainability, exit strategy, ownership transfer, or continuity content.
- Load it when another proposal section needs this domain expertise.

## Do Not Use When
- The task only needs formatting or proposer-profile selection.
- Another supporting skill is a closer fit for the assignment.

## Required Inputs
| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Intended post-project outcomes, operating model, owners, and resources | ToR and client | required | Return a sustainability discovery checklist. |
| Recurrent costs, skills, support, governance, and asset evidence | Client budgets, teams, systems | conditional | Mark continuity assumptions and test them during inception. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Identify where sustainability or exit-planning logic matters in the assignment.
2. Read the local references only where they materially improve the output.
3. Convert the guidance into proposal-ready ownership, continuity, and institutionalization mechanisms.
4. Integrate the result into the target section and check for consistency.

## Quality Standards
- Translate sustainability concepts into practical proposal language and long-term continuity logic.
- Keep the approach specific to the client context and implementation reality.
- Preserve compatibility with existing repository workflows and file paths.

## Anti-Patterns
- Saying “the client will sustain it”. Fix: name owner, process, budget, competence, and authority.
- Treating training as the whole exit strategy. Fix: cover governance, finance, technology, people, and support.
- Hiding recurrent costs. Fix: quantify or identify cost drivers and funding decisions.
- Handover without acceptance evidence. Fix: use asset, access, document, competency, and issue registers.
- Promising indefinite support. Fix: define warranty, support term, SLA, transition, and renewal boundary.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Sustainability and exit plan | Evaluator, client owner, operations team | Covers institutional, technical, financial, human-resource, support, handover, and post-exit controls. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Sustainability test and handover register | Readiness matrix | Every continuing capability has owner, resources, evidence, gap, action, and acceptance status. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Planning is read-only by default. Transferring assets, credentials, licences, contracts, budgets, or operational responsibility requires explicit authority and recorded acceptance.

## Degraded Mode
When recurrent-cost, owner, or capability evidence is unavailable or missing, return the narrowest qualified exit plan with readiness gaps. Mark sustainability not assessed.

## Decision Rules
| Readiness | Action | Risk avoided |
|---|---|---|
| Owner, funds, skills, and support are evidenced | Proceed to phased handover | Premature exit |
| Critical capability has one person | Build redundancy and supervised practice | Single-point failure |
| Recurrent funding is unresolved | Escalate before committing continuity | Unfunded operating promise |

## Worked Example
For a new MIS, hand over administrator access, configuration records, support runbook, trained backups, licence budget, and a tested incident drill before closing the assignment.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- Local `references/` files when detailed frameworks or examples are needed.

The question every evaluator asks: "What happens when the consultants leave?" Proposals that answer this convincingly — with specific mechanisms for embedding results into the client's operations — score significantly higher than those that end at "final report delivered". This skill provides the frameworks for demonstrating that the assignment's outcomes will endure.

## When to Read This Skill

- Every consulting proposal benefits from sustainability thinking, but read this skill specifically when:
- The ToR mentions "sustainability", "exit strategy", "handover", "ownership transfer", or "institutional embedding"
- The assignment is donor-funded (donors are highly sensitive to sustainability)
- The assignment involves systems, processes, or institutional changes that must outlive the project
- When the ToR asks for a standalone sustainability plan or exit strategy

## Sustainability Dimensions

### Institutional Sustainability

The client organisation can maintain and build on the results:

- Roles and responsibilities for ongoing activities are assigned to permanent staff
- Processes are documented in standard operating procedures (SOPs)
- The function is embedded in the organisational structure (job descriptions, reporting lines)
- Management commitment is secured through formal adoption (policy, directive, board resolution)

### Technical Sustainability

The systems and tools delivered continue to function:

- System administration skills transferred to client IT staff
- Maintenance procedures documented and tested
- Licensing and hosting arrangements transferred to the client
- Technical documentation complete (system architecture, user manuals, troubleshooting guides)
- Warranty period with responsive support (typically three to six months after go-live)

### Financial Sustainability

The client can afford to continue:

- Recurrent costs identified and budgeted (hosting, licences, maintenance, consumables)
- Cost recovery or funding mechanisms in place
- No dependency on project funding for ongoing operations

### Human Resource Sustainability

The people are capable and available:

- Training of Trainers completed — internal capacity to train new staff
- Knowledge transfer verified — counterparts can perform tasks independently
- Staff retention measures discussed with client (incentives, career paths)
- Documentation accessible for self-learning by future staff

## Exit Strategy Framework

### Phased Handover

Do not wait until the end of the assignment to hand over. Structure the exit as a gradual transfer:

| Phase | Consultant Role | Client Role | Duration |
|---|---|---|---|
| **Full delivery** | Consultant leads all activities | Client observes and learns | Early phases |
| **Joint delivery** | Consultant and counterpart work side by side | Client takes increasing responsibility | Middle phases |
| **Supervised handover** | Client leads, consultant mentors and quality-checks | Client performs all tasks | Late phases |
| **Independent operation** | Consultant available for support only | Client operates independently | Post-project |

### Handover Checklist

| Item | Handed Over To | Format | Verified By |
|---|---|---|---|
| All deliverables (final versions) | Client project team | Digital + printed | Client sign-off |
| System source code and documentation | Client IT department | Repository access | Technical review |
| Training materials and facilitator guides | Client HR / training unit | Digital + printed | ToT completion |
| Standard operating procedures | Relevant departments | Approved SOPs | Management sign-off |
| Data and databases | Client data custodian | Secure transfer | Data integrity check |
| Licences and access credentials | Client IT department | Documented handover | Access verified |

### Post-Project Support

Propose a defined support period after formal project closure:

- Duration: typically three to six months
- Scope: technical support, troubleshooting, minor adjustments
- Channel: email and phone support, with defined response times
- Limitations: does not include new development or scope expansion
- Cost: included in the original bid or priced separately (state clearly)

## Generating a Standalone Section

When the ToR asks for a dedicated sustainability plan or exit strategy, generate a document covering:

1. Sustainability approach and principles
2. Analysis of sustainability risks and mitigation measures
3. Institutional embedding plan (roles, SOPs, organisational integration)
4. Technical sustainability plan (maintenance, documentation, support)
5. Financial sustainability analysis (recurrent costs, funding sources)
6. Knowledge transfer and capacity building plan (reference `capacity-building/SKILL.md`)
7. Phased handover schedule
8. Post-project support arrangements

Follow east-african-english standards throughout.

