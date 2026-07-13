---
name: change-management
description: Use when a proposal must address adoption, resistance, readiness, communications, transition, or organisational reform. Unlike capacity-building, this skill governs behaviour and operating-model change rather than teaching competencies alone.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Change Management
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill when the assignment explicitly needs change-management, adoption, transition, or resistance-management content.
- Load it when another proposal section needs this domain expertise.

## Do Not Use When
- The task only needs formatting or proposer-profile selection.
- Another supporting skill is a closer fit for the assignment.

## Required Inputs
| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Defined change, affected groups, sponsor, and implementation plan | Client or proposal lead | required | Stop detailed planning and return discovery questions. |
| Readiness, incentives, constraints, and prior-change evidence | Interviews, surveys, client records | conditional | State hypotheses and propose a readiness assessment. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Identify where change-management logic matters in the assignment.
2. Identify adoption risks across leaders, managers, frontline staff, users, customers, beneficiaries, and support teams.
3. Read the local references only where they materially improve the output.
4. Convert the guidance into proposal-ready activities, controls, and adoption mechanisms.
5. Integrate the result into the target section and check for consistency.

## Quality Standards
- Translate theory into practical proposal language, outputs, and roles.
- Keep the approach specific to the client context and implementation reality.
- Preserve compatibility with existing repository workflows and file paths.

## Anti-Patterns
- Naming ADKAR or Kotter without actions. Fix: map each activity to a group, owner, timing, and measure.
- Treating communication as adoption. Fix: add readiness, practice, reinforcement, and support.
- Describing resistance as a staff defect. Fix: identify incentives, workload, trust, and process causes.
- Launching all users at once without evidence. Fix: stage pilots and define go/no-go criteria.
- Promising human review without an accountable queue. Fix: name authority, SLA, escalation, and audit evidence.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Change and adoption plan | Evaluator, sponsor, line managers | Identifies groups, readiness, interventions, owners, measures, decision gates, and reinforcement. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Readiness and adoption register | Segmented table | Each material adoption risk has evidence, owner, response, indicator, and review point. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Analysis is read-only by default. Draft or edit artefacts only when authorised; do not send staff communications, change access, or activate operational changes without named client approval.

## Degraded Mode
If interviews, surveys, usage data, or sponsor access are unavailable, provide a provisional stakeholder hypothesis and readiness-assessment plan. Do not claim readiness or adoption.

## Decision Rules
| Change condition | Action | Risk avoided |
|---|---|---|
| Individual system or process adoption | Apply ADKAR by affected group | Generic organisation-wide activity |
| Institution-wide reform | Apply Kotter with governance gates | Sponsor-free programme |
| High uncertainty or trust risk | Pilot, measure, and stage authority | Premature full rollout |

## Worked Example
For a case-management system, segment clerks, supervisors, and administrators; pilot one office; measure task completion and override causes; then expand after support capacity is evidenced.

## SaaS Mindset Transition

For SaaS implementation engagements, the change management workstream must address four substantive operating-model shifts beyond the standard ADKAR/Kotter material:

- **Per-customer to per-tenant operations**: operations no longer manages dedicated environments per customer; it manages tenant lifecycles inside a shared platform.
- **Scheduled per-customer releases to continuous releases for all tenants**: release management becomes continuous; per-customer release waivers are not granted.
- **Installation services to customer success engagement**: the team that used to install software for each new customer becomes the customer-success team that engineers adoption, value realisation, and expansion.
- **Perpetual licence to recurring subscription**: finance, sales, and contracts reorganise around recurring revenue, deferred revenue recognition, renewal forecasting, and expansion planning.

Each shift is named, measured, communicated, trained, and reinforced through the change-management workstream. Reference `../saas-pilot-to-rollout-change-management/SKILL.md` for the SaaS-specific change skill.

## AI Mindset Transition

For AI-on-SaaS engagements, layer on the AI mindset transition alongside the SaaS shifts:

- **Trust before authority**: AI authority is staged — shadow, confirm, supervised auto, full auto — not granted at launch. Trust-building activities are designed into adoption.
- **Augment vs replace, honestly**: the framing is agreed before user communications. Honest framing protects adoption; sugar-coated "augment" framing breaks trust irreversibly when the intent is to replace.
- **Human-in-the-loop is engineered, not promised**: HITL names the human, the authority (approve, decline, modify), the SLA, the queue, the audit, and the escalation. "Human review" is not HITL.
- **Retraining cadence is communicated**: when models / prompts are updated, what users see change, what the rollback path is, who signed off. Silent retraining destroys trust.
- **Override and abstain are measured, not feared**: override rate (5–25 % healthy) and abstain-correctness (≥ 0.95) are dashboard metrics signed off at the AI Governance Forum.

Reference `../ai-on-saas-change-management-and-adoption/SKILL.md` for the companion skill and `../references/ai-on-saas-change-management-playbook.md` for the long-form playbook.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- Local `references/` files when detailed frameworks or examples are needed.
- [../references/service-design-methodology-module.md](../../profiles-sectors/references/service-design-methodology-module.md) for co-creation, prototype validation, service implementation, and frontline adoption.
- [../references/discovery-question-bank-for-proposals.md](../../profiles-sectors/references/discovery-question-bank-for-proposals.md) for change-readiness, adoption, and implementation assumption questions.
- [../references/saas-multi-tenant-architecture-block.md](../../profiles-sectors/references/saas-multi-tenant-architecture-block.md) for the SaaS mindset paragraph and the four substantive shifts.
- [../references/saas-customer-success-engagement-package.md](../../profiles-sectors/references/saas-customer-success-engagement-package.md) for the customer-success function that replaces installation services.
- [../references/saas-lifecycle-email-program-proposal-template.md](../../profiles-sectors/references/saas-lifecycle-email-program-proposal-template.md) for the lifecycle communications that support adoption.
- [../customer-service-and-maintenance-proposals/SKILL.md](../../strategy-positioning/customer-service-and-maintenance-proposals/SKILL.md) when adoption depends on support, issue handling, and post-launch confidence.
- [../saas-pilot-to-rollout-change-management/SKILL.md](../../saas-proposals/saas-pilot-to-rollout-change-management/SKILL.md) - SaaS-specific change management skill.
- [../ai-on-saas-change-management-and-adoption/SKILL.md](../../ai-on-saas-proposals/ai-on-saas-change-management-and-adoption/SKILL.md) - AI-on-SaaS change and adoption skill.
- [../references/ai-on-saas-change-management-playbook.md](../../profiles-sectors/references/ai-on-saas-change-management-playbook.md) - AI adoption playbook (trust staging, augment-vs-replace, HITL, retraining cadence).

Most consulting assignments — ICT implementations, institutional reform, process improvement — require people to change how they work. Proposals that address this explicitly score higher than those that treat change as an afterthought. This skill provides the OCM frameworks and structures that proposal sections draw from.

## When to Read This Skill

- The assignment involves a new system, process, or institutional structure
- The ToR mentions "change management", "adoption", "transition", or "organisational readiness"
- Drafting methodology sections for ICT implementations, reform programmes, or restructuring
- When the ToR asks for a standalone change management plan

## Frameworks

### ADKAR (Preferred for System and Process Changes)

The most practical framework for East African consulting proposals — easy to explain to non-specialists and maps directly to proposal activities:

- **Awareness** — why the change is happening (stakeholder communication, town halls, leadership messaging)
- **Desire** — willingness to participate (early adopter engagement, addressing "what's in it for me", involving staff in design)
- **Knowledge** — how to change (training programmes, user guides, help desks)
- **Ability** — demonstrated capability (hands-on practice, mentoring, supervised go-live)
- **Reinforcement** — sustaining the change (performance monitoring, recognition, feedback loops, corrective action)

When to use: ICT system rollouts, process redesign, new policy implementation, any assignment where end-user adoption determines success.

### Kotter's 8-Step Model (Preferred for Large Institutional Reform)

More suited to multi-year reform programmes and institutional transformation:

1. Create urgency — evidence of need for change
2. Build a guiding coalition — senior champions and change agents
3. Form a strategic vision — clear picture of the desired future state
4. Enlist a volunteer army — broad engagement beyond the project team
5. Enable action — remove barriers, provide resources and authority
6. Generate short-term wins — visible early results to build momentum
7. Sustain acceleration — build on wins, do not declare victory too early
8. Institute change — embed in policies, procedures, job descriptions, performance metrics

When to use: public sector reform, institutional restructuring, multi-ministry programmes, assignments where the change is cultural and structural, not just procedural.

### Bridges' Transition Model (Complementary)

Useful for addressing the human side of change — particularly in contexts where staff fear job losses or role changes:

- **Ending** — acknowledge what is being lost (old processes, familiar tools, established routines)
- **Neutral zone** — support people through the uncertainty (clear communication, temporary support structures)
- **New beginning** — reinforce the benefits of the new state (quick wins, recognition, career development)

When to use: as a complementary lens alongside ADKAR or Kotter, particularly when the assignment involves staff retrenchment, role redefinition, or significant cultural shift.

## Common Change Management Activities for Proposals

### Stakeholder Readiness Assessment

- Identify stakeholder groups affected by the change
- Assess current readiness (awareness, willingness, capability) per group
- Map resistance factors and enablers
- Design targeted interventions per group

### Change Champion Network

- Identify and recruit change champions from within the client organisation
- Train champions on the change narrative and their role
- Establish regular champion meetings for feedback and issue escalation
- Champions serve as the bridge between the project team and end users

### Communication Plan

| Audience | Message | Channel | Frequency | Responsible |
|---|---|---|---|---|
| Senior management | Strategic progress, decisions needed | Steering committee | Monthly | Team Leader |
| Middle management | Operational impact, timeline, support available | Workshops, email | Bi-weekly | Change Lead |
| End users | What is changing, when, and how to prepare | Town halls, posters, SMS | Weekly during transition | Change Champions |

### Resistance Management

- Identify sources of resistance early — do not wait for go-live
- Distinguish between resistance due to lack of information (address with communication) and resistance due to genuine concerns (address with participation and design adjustments)
- Never dismiss resistance as "people don't like change" — there is always a specific reason
- Document resistance patterns and responses for the client's future reference

## Reference Files

Load these reference files for deeper guidance when writing change management sections:

- [references/change-process-models.md](references/change-process-models.md) — Satir Change Model, Lewin, Kübler-Ross change curve, force field analysis, Nadler-Tushman congruence model, Burke-Litwin diagnostic, complexity and emergence (Hearsum), Silver Bullet lifecycle, Adams and Straw's Seven Fundamental Shifts, types-of-change classification
- [references/hard-and-soft-integration.md](references/hard-and-soft-integration.md) — hard/soft integration principle, project charter for change, four-team model (core project, change management, transition monitoring, red team), RACI matrix, communication plan framework, training plan framework (four-level evaluation), resistance management plan (seven sources of resistance, change saturation analysis, resistance patterns), action review, organisational readiness assessment (eight dimensions with scoring)
- [references/lean-and-adaptive-change.md](references/lean-and-adaptive-change.md) — Lean Change Management cycle (Insights→Options→Experiments), improvement canvas, strategic change canvas, one-page change plan, change agent network design, digital change management (adoption curve, six practices), feedback-driven vs plan-driven comparison, measuring change success (qualitative, quantitative, leading vs lagging indicators)

## Generating a Standalone Section

When the ToR asks for a dedicated change management plan, generate a document covering:

1. Change management approach and framework
2. Organisational readiness assessment methodology (see `references/hard-and-soft-integration.md` section 9)
3. Stakeholder readiness assessment and change saturation analysis
4. Communication plan (see `references/hard-and-soft-integration.md` section 5)
5. Training and capability development plan (reference `capacity-building/SKILL.md` and `references/hard-and-soft-integration.md` section 6)
6. Change champion or change agent network design (see `references/lean-and-adaptive-change.md` section 3)
7. Resistance management strategy (see `references/hard-and-soft-integration.md` section 7)
8. Adoption measurement framework (see `references/lean-and-adaptive-change.md` section 6)
9. Change sustainability and reinforcement plan

Follow east-african-english standards throughout.

