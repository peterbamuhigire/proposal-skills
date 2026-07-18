---
name: 07-team-composition
description: Use when drafting staffing, roles, organograms, expert fit, CV framing, availability, or responsibility allocation. Unlike 08-work-plan, this skill proves that the proposed people can execute the methodology; it does not schedule their effort.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Team Composition
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill to draft or revise the team composition, staffing, role-allocation, or CV framing section.
- Load it when the evaluator will score people, roles, or organizational fit.

## Do Not Use When
- The task is unrelated to team structure or CV presentation.
- The user only needs supporting domain knowledge rather than this section.

## Required Inputs
- The assignment brief and any staffing or CV-format requirements.
- The selected proposer profile.
- Verified role definitions, expert biographies, availability, and staffing assumptions.

| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Staffing criteria, verified CVs, roles, availability, effort, and permissions | Tender pack and authorised expert records | required | Use role requirements only; do not nominate or claim availability. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Read the assignment materials and identify which roles, qualifications, and forms matter most.
2. Load the proposer profile and any relevant procurement framework before drafting.
3. Use the structure below to align the proposed team with the actual work and scoring logic.
4. Check the team narrative against the methodology, work plan, and relevant experience sections.
5. Verify role fit, terminology, and CV framing before finalizing.

## Quality Standards
- Keep the section tightly matched to the assignment tasks and evaluation criteria.
- Use British English and East African professional tone unless the bid format requires otherwise.
- Prefer clear role logic, evidence of fit, and credible staffing assumptions.

## Anti-Patterns
- Releasing the section with an unresolved mandatory input. Fix: block release and name the evidence owner.
- Hiding a contradiction with another proposal section. Fix: reconcile the source sections before drafting resumes.
- Treating an unavailable check as passed. Fix: mark it not assessed and return a qualified draft.
- Do not propose roles that are disconnected from the methodology or work plan.
- Do not overstate qualifications, availability, or organizational depth.
- Do not ignore mandatory CV formats or staffing forms.
- Do not hide role overlap or gaps. Fix: map every methodology workstream and approval to an accountable role.
- Do not expose unnecessary personal data. Fix: include only authorised, bid-relevant CV evidence.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Team structure, role matrix, and CV framing | Evaluator and mobilisation lead | Every role maps to work, effort, qualification evidence, accountability, and verified availability. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Role-to-task and CV evidence map | Traceability matrix | No task lacks accountable ownership and no scored CV claim lacks evidence. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Read and draft only. Do not nominate, publish personal data, promise availability, or commit subcontractors without explicit authority and consent.

## Degraded Mode
Without verified CVs or availability, return the required team shape and evidence gaps. Do not attach names to unconfirmed roles.

## Decision Rules
| Need | Action | Risk avoided |
|---|---|---|
| Criterion mandates a qualification | Evidence it in the assigned CV | Unsupported score claim |
| Critical role has no backup | Add deputy or continuity control | Single-person dependency |
| Effort conflicts with work plan | Reconcile allocation before release | Paper team |

## Worked Example
For a data-system assignment, map the team lead, data lead, change lead, trainer, and QA reviewer to phases and days; verify CV evidence and avoid double-booked critical roles.

## SaaS Engagement Team Patterns

For SaaS implementation and SaaS product-development engagements, layer on these team-shape patterns:

- **Two-of-everything principle**: for client-side critical operating roles after handover (admin, support, customer success, billing operations), the engagement designs in redundancy from day one. Single-point-of-failure operating roles after cutover are unacceptable.
- **Customer success roles**: name the Customer Success Manager (CSM), Customer Success Engineer (CSE), Account Director, Executive Sponsor (Agency Side), and Customer Success Operations function — separate from the Support function (different goals, different staffing).
- **SaaS sales roles** (when in scope): never propose a one-rep sales team; minimum viable is two AEs + one SDR + shared Sales Engineering.
- **Sales capacity plan** (when in scope): AEs × quota × productivity factor; productivity factor in year 1 typically 0.5–0.7 of stated quota.
- **Architecture and engineering roles**: name an Architecture Lead, a Solution Lead, an Integration Lead, a Data Lead, a Reliability Lead, a Configuration Lead, and a Security Lead for premium SaaS bids.

## AI-on-SaaS Engagement Team Patterns

For AI-on-SaaS engagements (multi-tenant SaaS + AI features), the SaaS roster is supplemented with the AI-side roster. The irreducible AI trio is:

- **AI Safety Lead** — Responsible-AI commitment owner; chairs the AI Governance Forum on the agency side; quarterly Responsible-AI report; red-team scorecard owner.
- **Eval Engineer** — golden-dataset owner; metric-threshold owner; eval CI gate; monthly eval refresh; drift watch.
- **MLOps Engineer** — model gateway operator; model registry; region routing; fallback; AI observability.

Beyond the trio, the AI roster names: AI Solution Architect / ML Lead, Prompt Engineer, Data Engineer (AI), RAG / Retrieval Engineer, AI Change and Adoption Lead. The two-of-everything rule applies to client-side counterparts (Eval Owner, Prompt Owner, AI Safety Sponsor, Model Gateway Operator). AI safety, eval, and red-team roles ramp at Phase 1, not at hardening. Reference `../ai-on-saas-team-composition/SKILL.md` and `../references/ai-on-saas-team-composition-template.md` for the full roster, RACI, ramp curve, and blended-rate considerations.

## Embedded Accounting Engine Team Patterns

For embedded accounting-engine engagements, add finance-qualified roles early rather than treating accounting as late QA:

- **Accounting Solution Architect**: owns ledger architecture, chart of accounts design, posting-rule model, and report traceability.
- **Finance SME / Accountant**: validates accounting treatment, posting matrices, close workflow, report outputs, and statutory caveats.
- **Data Migration Lead**: owns opening balances, customer/supplier balances, stock values, fixed assets, and historical source-document migration.
- **Integration Lead**: owns bank, mobile-money, tax, payroll, inventory, and payment-provider interfaces.
- **QA/Test Lead**: owns invariant tests for balanced journals, period locks, idempotency, reversals, report rebuilds, and subledger reconciliation.
- **Reporting Lead**: owns financial statements, management reports, drill-down, exports, and audit evidence pack.
- **Client-side Finance Owner**: approves mappings, opening balances, reports, and first-close acceptance.

## Finance And Accounting Section Team Patterns

When a proposal includes project financial management, donor/grant finance, accounting controls, audit evidence, or financial reporting, name the finance capability explicitly:

- **Finance Lead / Financial Management Specialist**: owns budget governance, funds-flow controls, reporting cadence, and financial close-out.
- **Accountant / Bookkeeping Specialist**: owns transaction recording, reconciliations, supporting schedules, and source-document discipline.
- **Grants / Donor Compliance Specialist** where restricted funds, donor formats, advance liquidation, or eligible-cost rules apply.
- **Tax / Statutory Compliance Adviser** where VAT, WHT, PAYE/NSSF, LST, duties, or local filing obligations affect the assignment.
- **Internal Controls / Audit Readiness Specialist** where the proposal must withstand board, donor, government, or auditor review.
- **Client-side Finance Focal Person**: approves budget reallocations, expenditure evidence, financial reports, and audit-file handover.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- [../profiles/SKILL.md](../../profiles-sectors/profiles/SKILL.md) for proposer selection and voice.
- [../sectors/SKILL.md](../../profiles-sectors/sectors/SKILL.md) for procurement and sector routing.
- [../references/saas-customer-success-engagement-package.md](../../profiles-sectors/references/saas-customer-success-engagement-package.md) for customer success role definitions and effort allocations.
- [../references/saas-gtm-motion-design-reference.md](../../profiles-sectors/references/saas-gtm-motion-design-reference.md) for sales-team design and capacity planning.
- [../references/saas-implementation-methodology-blocks.md](../../profiles-sectors/references/saas-implementation-methodology-blocks.md) for engineering-role naming inside Methodology.
- [../references/ai-on-saas-team-composition-template.md](../../profiles-sectors/references/ai-on-saas-team-composition-template.md) for the AI-on-SaaS roster, RACI, ramp curve, and blended-rate table.
- [../ai-on-saas-team-composition/SKILL.md](../../ai-on-saas-proposals/ai-on-saas-team-composition/SKILL.md) for the companion AI-on-SaaS team-composition skill.
- [../embedded-accounting-engine-proposal/SKILL.md](../../strategy-positioning/embedded-accounting-engine-proposal/SKILL.md) for accounting-engine staffing, caveats, and acceptance criteria.
- [../accounting-finance-advisory/SKILL.md](../../domain-delivery/accounting-finance-advisory/SKILL.md) for finance/accounting section staffing and financial-management roles.
- Relevant proposal-wide references when positioning or proof structure needs reinforcement.

Evaluators assess whether the proposed team has the qualifications, experience, and availability to deliver the assignment. This section typically carries 30–40% of the technical score in QCBS evaluations. Every person named must be credible for the role assigned.

## What to Gather Before Writing

- Names, titles, and roles of all proposed team members
- For each person: qualifications, years of experience, nationality, language skills
- For each person: three to five most relevant past assignments (client, role, duration, outcomes)
- The team leader's specific credentials and why they are suited to lead this assignment
- Team structure — who reports to whom, who is on site versus remote
- Level of effort — person-days or person-months per team member
- Whether the ToR specifies World Bank TECH-6 format or allows narrative CVs

## Structure

### Team Organisation

One page. Start with a brief narrative explaining the team structure and the rationale for the composition — why these roles, why this mix of senior and junior, why this balance of international and local expertise.

### Organogram

A simple organisational chart showing:

- Client focal point / steering committee at the top
- Team leader reporting line
- Team members grouped by function or workstream
- Any sub-consultants or support staff

Present as a text-based chart or describe the structure clearly for rendering in the final document.

```
[Client Focal Point / Steering Committee]
            |
    [Team Leader — Name]
            |
    -------------------------
    |           |           |
[Stream 1]  [Stream 2]  [Stream 3]
[Name]      [Name]      [Name]
```

### Role and Responsibility Matrix

A table mapping each team member to their role, responsibilities, and level of effort:

| Name | Role | Key Responsibilities | Person-Days |
|---|---|---|---|
| [Name] | Team Leader | Overall delivery, client liaison, quality assurance | [N] |
| [Name] | [Role] | [Two to three responsibilities] | [N] |

### Individual CVs

One CV per team member. The format depends on the procurement framework:

#### World Bank TECH-6 Format

Use this format for World Bank and most donor-funded assignments:

```
CURRICULUM VITAE (CV)

Position:           [Role in this assignment]
Name:               [Full name]
Date of Birth:      [DD/MM/YYYY]
Nationality:        [Country]
Education:          [Degree, Institution, Year]
                    [Degree, Institution, Year]
Languages:          [Language — Level (native/fluent/working)]

Membership in Professional Associations:
- [Association name and membership type]

Countries of Work Experience:
[List of countries]

Employment Record:

Period:      [Month/Year – Month/Year]
Employer:    [Organisation]
Position:    [Title]
Description: [Two to three sentences on responsibilities]

[Repeat for last three to five positions]

Detailed Tasks Assigned on This Assignment:
[Bulleted list of specific tasks this person will perform]

Relevant Experience:

Assignment:  [Project title]
Client:      [Organisation, Country]
Period:      [Month/Year – Month/Year]
Position:    [Role held]
Description: [Three to four sentences — scope, activities, outcomes]

[Repeat for three to five most relevant assignments]

Certification:
I certify that the above information is correct to the best of my knowledge.

Signature: ___________________  Date: [DATE]
```

#### Narrative CV Format

For PPDA, private sector, and smaller bids where TECH-6 is not required:

- **Name and Role** — one line
- **Professional Summary** — two to three sentences: years of experience, core expertise, highest qualification
- **Key Qualifications** — bulleted list of degrees, certifications, language skills
- **Relevant Experience** — three to five past assignments in a compact table:

| Assignment | Client | Role | Year | Key Outcome |
|---|---|---|---|---|

## Tone Rules

- Three to six pages depending on team size
- Every person named must have a credible CV — do not include team members who cannot be verified
- Match qualifications to ToR requirements explicitly — if the ToR asks for "10 years of experience in public financial management", state exactly how many years the proposed person has
- For key experts, emphasise the specific experience that matches this assignment, not a full career history
- Follow east-african-english standards throughout

