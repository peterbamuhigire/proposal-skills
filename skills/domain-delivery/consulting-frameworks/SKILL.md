---
name: consulting-frameworks
description: Use when a proposal methodology needs a coherent conceptual framework, problem decomposition, or phase logic. Unlike business-analysis-tools, this skill shapes the overall consulting approach rather than selecting a technique for one analytical task.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Consulting Frameworks
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill when the assignment needs consulting frameworks to shape methodology, analysis, or recommendations.
- Load it when a proposal section needs structured problem-solving logic.

## Do Not Use When
- The task only needs formatting or proposer-profile selection.
- Another supporting skill is a closer fit for the assignment.

## Required Inputs
| Artefact | Source | Required? | If absent |
|---|---|---|---|
| ToR problem, objectives, deliverables, and evaluation criteria | Client procurement pack | required | Stop framework selection and identify missing scope. |
| Sector evidence and delivery constraints | Verified sources and discovery | conditional | Qualify the model and list validation needs. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Identify which analytical problem the proposal needs to structure.
2. Decide whether the assignment also needs premium pricing, service design, technical strategy, or evaluator-story framing.
3. Read the local references only where they materially improve the output.
4. Select the frameworks that fit the assignment and turn them into proposal-ready logic.
5. Integrate the result into the relevant section and check for consistency.

## Quality Standards
- Translate frameworks into practical proposal language, sequence, and decisions.
- Use only the methods that improve the actual assignment response.
- Preserve compatibility with existing repository workflows and file paths.

## Anti-Patterns
- Listing frameworks without an assignment decision. Fix: name the question and deliverable each serves.
- Combining overlapping models for appearance. Fix: select the smallest coherent stack.
- Copying a textbook sequence over the ToR. Fix: align phases to client decisions and acceptance points.
- Hiding assumptions behind diagrams. Fix: state assumptions and their validation step.
- Using a framework as evidence. Fix: distinguish method from verified findings.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Conceptual approach and phase logic | Evaluator and methodology writer | Shows problem decomposition, evidence flow, decisions, deliverables, and ToR links. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Framework-to-requirement map | Traceability table | Every selected component serves a named requirement or is removed. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Read and search are required; proposal editing requires authority. Framework selection does not authorise client decisions, operational mutation, or claims that unperformed analysis is complete.

## Degraded Mode
If sufficient brief or evidence is unavailable, return a provisional framework with explicit assumptions, alternatives, and discovery questions. Do not imply that a diagram validates the approach.

## Decision Rules
| Need | Action | Risk avoided |
|---|---|---|
| Explain the assignment as a system | Use a conceptual model | Disconnected activities |
| Break a complex problem into testable parts | Use an issue tree | Overlapping workstreams |
| Convert diagnosis into implementation | Use staged decision gates | Recommendations without adoption path |

## Worked Example
For a service-redesign bid, structure evidence gathering, journey diagnosis, option selection, prototype, and handover, with a client decision after diagnosis.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- Local `references/` files when detailed frameworks or examples are needed.
- [../references/technical-strategy-credibility-checklist.md](../../profiles-sectors/references/technical-strategy-credibility-checklist.md) for software, SaaS, AI, cloud, API, roadmap, operations, and architecture strategy.
- [../references/service-design-methodology-module.md](../../profiles-sectors/references/service-design-methodology-module.md) for journey mapping, blueprints, co-creation, and service implementation frameworks.
- [../references/proposal-narrative-patterns-and-case-story-spine.md](../../profiles-sectors/references/proposal-narrative-patterns-and-case-story-spine.md) for evaluator journey, proof stories, and design rationale.

A library of structured analytical frameworks drawn from top-tier consulting practice. These frameworks are the building blocks of methodology sections — they determine how problems are decomposed, how analysis is structured, and how recommendations are developed.

## When to Read This Skill

- Designing the conceptual approach for a methodology section
- Structuring analytical phases for a diagnostic, strategy, or implementation proposal
- Selecting the right problem decomposition method for a given ToR
- Building quantitative analysis into a methodology
- Structuring recommendations and deliverable presentations

## How to Use

1. **Identify the assignment type** from the ToR (market entry, profitability, M&A, operational improvement, strategy, etc.)
2. **Select the matching framework** from the relevant reference file
3. **Customise** sub-activities to the specific client context
4. **Embed** quantitative analysis patterns where the ToR requires financial or feasibility analysis
5. **Structure** the final deliverable presentation using the communication frameworks

## Reference Files

| Reference File | Contents | Use When |
|---|---|---|
| `references/problem-structuring.md` | Eight first-principles structuring strategies, issue tree construction, MECE compliance, hypothesis-driven analysis, eight-bucket system, idea expansion techniques, lateral thinking toolkit, Six Thinking Hats | Designing any methodology's conceptual framework; decomposing any consulting problem |
| `references/financial-analysis.md` | Expected value, cannibalisation analysis, breakeven, profitability decomposition, market sizing, pricing toolkit, pocket pricing model, customer lifetime value, experience curve | The ToR requires financial feasibility, investment appraisal, cost-benefit analysis, or market analysis |
| `references/strategy-frameworks.md` | Market entry, competitive response, build/buy/partner, adjacent market proximity, M&A evaluation, pricing strategy, Blue Ocean ERRC, Discipline of Market Leaders, disruptive innovation, structured choice decision-making, scenario planning, Rumelt's Kernel, Innovation-Change-Learning Matrix | Strategy, market entry, growth, competitive positioning, innovation, or acquisition assignments |
| `references/operations-frameworks.md` | Process bottleneck, stakeholder-based framework, criteria-based option evaluation, situation assessment, job-to-be-done, importance × satisfaction analysis, structured decision-making | Operations improvement, process reengineering, multi-stakeholder assignments, option appraisal |
| `references/devops-delivery-diagnostics.md` | Value-stream flow, CI/CD, release governance, PHP/LAMP operations, cloud-native delivery, observability, incident response, DevSecOps, GitOps, and software delivery KPIs | Software delivery, SaaS operations, digital platforms, cloud migration, production reliability, or DevOps transformation |
| `references/communication-structures.md` | SCORE storytelling, top-down recommendation structure, exhibit interpretation, analytical sense-checking, action titles, Hero's Journey narrative, Tufte's data visualisation rules, Comma Effect | Structuring deliverables, presentations, experience narratives, and qualitative analysis |

## Relationship to Other Skills

- **`business-analysis-tools/`** — diagnostic instruments applied DURING delivery (SWOT, PESTLE, gap analysis, maturity models). Consulting frameworks here are for DESIGNING the methodology.
- **[references/consulting-delivery-excellence.md](../../profiles-sectors/references/consulting-delivery-excellence.md)** — how to deliver well (process, quality, team management). Frameworks here are what analytical approach to use.
- **[references/proposal-strategy-and-persuasion.md](../../profiles-sectors/references/proposal-strategy-and-persuasion.md)** — how to write persuasively. Frameworks here provide the analytical substance that persuasion wraps around.
- **[06-methodology/SKILL.md](../../pipeline/06-methodology/SKILL.md)** — the methodology section skill. It draws on these frameworks when building the phase-by-phase plan.

Follow east-african-english standards throughout.

