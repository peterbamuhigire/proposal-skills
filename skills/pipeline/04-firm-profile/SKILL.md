---
name: 04-firm-profile
description: Use when drafting the proposer or individual consultant profile, service areas, geographic presence, organisation, or credentials. Unlike 05-relevant-experience, this skill establishes enduring capability rather than assignment-by-assignment proof.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Firm Profile
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill to draft or revise the firm profile or consultant profile section of a proposal.
- Load it after the proposer identity is fixed.

## Do Not Use When
- The task is unrelated to proposer credentials or profile content.
- The user only needs supporting domain knowledge rather than this section.

## Required Inputs
- The selected proposer profile from `../profiles/`.
- The assignment brief and any relevant procurement-form constraints.
- Current credential, service, footprint, and differentiator information for the proposer.

| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Legal identity, services, footprint, credentials, capacity, and authorised profile | Proposer records | required | Omit or mark unverified; do not fabricate organisational facts. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Confirm who is proposing before drafting anything in this section.
2. Read the assignment materials and determine which profile elements matter most to the evaluator.
3. Use the structure below to tailor the profile to the actual bid instead of reusing a generic corporate description.
4. Align the profile with the experience, methodology, and team sections.
5. Verify that the voice, evidence, and entity details match the selected proposer profile.

## Quality Standards
- Keep the section relevant to the assignment rather than encyclopedic.
- Use British English and East African professional tone unless the bid format requires otherwise.
- Emphasize evidence, capability fit, and credibility over broad marketing language.

## Anti-Patterns
- Releasing the section with an unresolved mandatory input. Fix: block release and name the evidence owner.
- Hiding a contradiction with another proposal section. Fix: reconcile the source sections before drafting resumes.
- Treating an unavailable check as passed. Fix: mark it not assessed and return a qualified draft.
- Do not write a generic company brochure in place of a bid-specific profile.
- Do not mix individual and company identities or voice.
- Do not include claims that the rest of the proposal cannot support.
- Do not confuse memberships with certification. Fix: use the exact verified status.
- Do not mix firm and individual experience. Fix: attribute every capability to its proper owner.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Firm or consultant profile | Evaluator and compliance reviewer | Correct identity and only relevant, verified capability evidence. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Profile claim register | Source map | Legal, credential, footprint, staffing, and service claims each have evidence. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Read and draft only. Do not alter legal identity, claim certification, publish personal data, or represent the entity without authority.

## Degraded Mode
If verified profile records are unavailable, return a structured draft with omissions and evidence requests. Do not fill gaps from memory.

## Decision Rules
| Profile fact | Action | Risk avoided |
|---|---|---|
| Directly relevant and verified | Include with concise proof | Generic brochure |
| Relevant but unverified | Hold or qualify | Misrepresentation |
| Belongs to a partner or expert | Attribute explicitly | False firm capability |

## Worked Example
A profile states the verified legal entity, three relevant service lines, actual regional presence, and evidenced delivery capacity; project outcomes remain in relevant experience.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- [../profiles/SKILL.md](../../profiles-sectors/profiles/SKILL.md) for proposer selection and voice.
- [../sectors/SKILL.md](../../profiles-sectors/sectors/SKILL.md) for procurement and sector routing.
- Relevant proposal-wide references when positioning or proof structure needs reinforcement.

This section establishes the firm's credentials and eligibility. It must convince the evaluator that the firm is legally registered, technically capable, financially stable, and experienced in the relevant sector and geography.

## What to Gather Before Writing

- Legal name, registration number, and country of incorporation
- Year established
- Core service areas (three to five, not a long undifferentiated list)
- Sector expertise with specific examples
- Geographic footprint — offices, countries of operation, regional reach
- Number of permanent staff (and any specialist pool or associate network)
- Key certifications, accreditations, or quality standards (ISO, professional body memberships)
- For joint ventures or consortia: each partner's profile and the division of responsibilities
- For individual consultants: qualifications, years of experience, areas of specialisation

## Structure — Firm Format

### Company Overview

One paragraph. State the firm's name, year of establishment, legal registration, headquarters location, and core positioning in one to two sentences. Follow with a brief description of what the firm does and for whom.

### Core Service Areas

A concise list or short table of three to five service areas. For each, one sentence describing the firm's capability.

| Service Area | Description |
|---|---|
| [e.g. ICT Systems] | [One sentence — what the firm delivers in this area] |

### Sector Expertise

One page. Describe the sectors the firm has worked in, with emphasis on the sector relevant to this bid. Name specific clients, projects, or programmes — not just sector labels.

### Geographic Footprint

Half a page. List countries of operation, office locations, and any regional partnerships. If the firm has worked in the client's country before, state this explicitly.

### Organisational Capacity

Half a page. Cover:

- Number of permanent professional staff
- Associate or specialist network (if used)
- Quality management system or standards followed
- Professional indemnity insurance (if applicable)
- Financial stability — years of continuous operation, annual turnover range (if required by the ToR)

### Certifications and Memberships

A short list of relevant certifications, accreditations, and professional body memberships. Only include those that are relevant to the assignment or demonstrate quality standards.

## Structure — Individual Consultant Format

For solo consultants or individual assignments, replace the firm structure with:

### Professional Summary

One paragraph. Name, nationality, years of experience, primary area of expertise, and highest relevant qualification.

### Areas of Specialisation

Three to five bullet points. Each specialisation with one sentence of supporting evidence.

### Key Qualifications

- Academic qualifications (institution, year)
- Professional certifications
- Language proficiency

### Selected Experience

A summary table of four to six most relevant assignments, following the format in `05-relevant-experience/SKILL.md`. For individual consultants, emphasise the specific role played, not just the project.

## Tone Rules

- One to two pages for the firm profile (longer for consortia)
- One page for individual consultant profiles
- Factual and verifiable — evaluators may check registration numbers and references
- Do not exaggerate staff numbers or geographic reach
- If the firm is small, position this as an advantage: senior attention, no delegation to juniors, direct access to decision-makers
- Follow east-african-english standards throughout

