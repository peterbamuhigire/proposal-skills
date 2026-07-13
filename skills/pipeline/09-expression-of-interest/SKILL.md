---
name: 09-expression-of-interest
description: Use when drafting an EoI, REOI response, prequalification, or shortlisting submission focused on eligibility and relevant capability. Unlike a full proposal pipeline, this skill omits detailed methodology unless the notice explicitly requires it.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Expression of Interest
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill to draft or revise an Expression of Interest or similar short-form prequalification response.
- Load it when the procurement stage is about being shortlisted rather than submitting the full proposal.

## Do Not Use When
- The task is unrelated to an EoI or prequalification document.
- The user only needs supporting domain knowledge rather than this document.

## Required Inputs
- The EoI notice, shortlist request, or brief.
- The selected proposer profile.
- Relevant experience, staffing readiness, and qualification evidence suitable for shortlist evaluation.

| Artefact | Source | Required? | If absent |
|---|---|---|---|
| REOI criteria, eligibility forms, page rules, verified profile, experience, and key staff evidence | Official notice and proposer records | required | Return a compliance/evidence gap list; do not draft unsupported qualifications. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Read the EoI requirements and identify what the issuer needs to be convinced of at shortlist stage.
2. Load the proposer profile and any relevant procurement or sector context.
3. Use the structure below to produce a concise, evidence-led response tailored to the request.
4. Emphasize relevance, credentials, and readiness over unnecessary detail.
5. Verify consistency with any future full-proposal positioning if the bid will continue.

## Quality Standards
- Keep the document concise, relevant, and evaluator-aware.
- Use British English and East African professional tone unless the bid format requires otherwise.
- Prefer directly relevant proof and shortlisting logic over broad narrative.

## Anti-Patterns
- Releasing the section with an unresolved mandatory input. Fix: block release and name the evidence owner.
- Hiding a contradiction with another proposal section. Fix: reconcile the source sections before drafting resumes.
- Treating an unavailable check as passed. Fix: mark it not assessed and return a qualified draft.
- Do not turn the EoI into an overlong full technical proposal.
- Do not include unsupported claims or irrelevant experience.
- Do not ignore page, format, or evidence constraints in the request.
- Do not include full-proposal detail unless requested. Fix: prioritise shortlisting criteria and proof.
- Do not merge firm, consortium, and expert experience. Fix: attribute each reference and role accurately.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| EoI or prequalification response | Shortlisting evaluator and signatory | Meets eligibility, page, form, evidence, attribution, and submission requirements without unnecessary methodology. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Shortlisting criterion-to-evidence map | Compliance matrix | Every criterion has verified evidence, location, owner, and status. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Review and drafting only. Do not sign, contact references, disclose confidential evidence, form a consortium, or submit without explicit authority.

## Degraded Mode
If the complete REOI or evidence is unavailable, return a shortlist-readiness assessment and exact evidence requests. Do not infer eligibility.

## Decision Rules
| Requirement | Action | Risk avoided |
|---|---|---|
| Pass/fail eligibility | Verify before narrative | Knockout submission |
| Scored experience | Lead with closest verified assignments | Diluted relevance |
| Detailed methodology not requested | Omit or summarise | Page-limit waste |

## Worked Example
A five-page REOI opens with eligibility, presents four verified comparable assignments against the shortlist criteria, names available key roles, and leaves detailed methodology for the RFP stage.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- [../profiles/SKILL.md](../../profiles-sectors/profiles/SKILL.md) for proposer selection and voice.
- [../sectors/SKILL.md](../../profiles-sectors/sectors/SKILL.md) for procurement and sector routing.
- Relevant proposal-wide references when positioning or proof structure needs reinforcement.

An Expression of Interest is shorter than a full technical proposal. Its purpose is to get the firm shortlisted — not to win the contract. The evaluator is assessing eligibility and relevance, not detailed methodology. Every sentence must demonstrate that the firm meets the stated criteria and has done this type of work before.

## What to Gather Before Writing

- The EoI notice or Request for Expressions of Interest (REOI)
- Shortlisting criteria — what the client will score (typically: relevant experience, qualifications, geographic coverage)
- The firm's most relevant past projects (four to six, matching the assignment type and geography)
- Key staff who would be proposed (names, qualifications, years of experience)
- The firm's legal registration, core service areas, and geographic footprint
- Any specific eligibility requirements (e.g., registration with PPDA, UN Global Compact membership, minimum years of operation)

## Structure

### Cover Letter

One page. Follow the same structure as `01-cover-letter/SKILL.md` but shorter:

- Client-focused opening — reference the specific assignment
- One paragraph on why the firm is qualified
- Confirm eligibility and interest
- Courteous closing with contact details

### Firm Profile

One page. A condensed version of `04-firm-profile/SKILL.md`:

- Legal name, registration, year established, headquarters
- Core service areas (three to five, relevant to this assignment)
- Geographic presence in the client's country or region
- Number of professional staff

### Relevant Experience

One to two pages. The most critical section of an EoI. Present four to six past projects using a compact format:

| # | Client | Country | Assignment Title | Year | Value | Key Outcome |
|---|---|---|---|---|---|---|

Follow with a brief paragraph for each project (three to four sentences) covering scope and outcomes. Order by relevance, not date.

Apply the outcomes rule from `05-relevant-experience/SKILL.md` — every project must state what was achieved.

### Key Staff

One page. A summary table of proposed key experts — not full CVs:

| Name | Proposed Role | Qualifications | Years of Experience | Relevant Expertise |
|---|---|---|---|---|

For each person, add one to two sentences highlighting their most relevant assignment. Full CVs are not expected at EoI stage unless the notice specifically requests them.

### Eligibility and Compliance

Half a page. A checklist or brief statement confirming:

- Legal registration and eligibility to participate
- No conflict of interest
- Not debarred by any procurement authority or international organisation
- Any specific compliance requirements stated in the REOI

## Tone Rules

- Four to six pages total — concise by design
- Every sentence must relate to the shortlisting criteria
- Do not include methodology or a work plan unless the REOI explicitly asks for it
- Do not include a financial proposal — EoIs never include pricing
- Focus on proving eligibility and relevance, not on persuasion
- Follow east-african-english standards throughout

