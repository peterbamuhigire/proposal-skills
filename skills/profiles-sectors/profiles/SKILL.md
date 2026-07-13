---
name: profiles
description: Use when proposal drafting must select and enforce one proposer identity, voice, signatory, credential set, and branding rule; use the sector router separately for procurement and industry context.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Proposer Profiles
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When
- Use this skill whenever proposal content needs the correct proposer identity, signatory, or voice.
- Load it when the user asks to write as a person, company, consortium, or client.

## Do Not Use When
- The task is unrelated to proposal authorship or identity.
- A proposer profile has already been selected and does not change.

## Required Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---|---|
| The proposer name or relationship structure. | Buyer solicitation, ToR, or approved brief | Required | Stop the affected claim, request or verify the input, and label the resulting gap. |
| Any existing profile file or details needed to adapt `client-template.md`. | Buyer, verified sector source, or discovery | Required | Stop the affected claim, request or verify the input, and label the resulting gap. |
| The proposal type so the selected identity can be applied consistently. | Buyer, verified sector source, or discovery | Conditional | Stop the affected claim, request or verify the input, and label the resulting gap. |

## Workflow

1. Determine who the proposal is being written for before drafting any section.
2. Load exactly one primary profile unless the engagement explicitly requires a consortium or joint venture.
3. Apply the selected profile to voice, signatory, experience framing, team composition, and branding.
4. Create or adapt a client profile if no existing file fits.
5. Re-check downstream sections for profile consistency before finalizing.

**Stop condition:** Stop when proposer identity, controlling framework, mandatory form, sector fit, current rule, or load-bearing evidence remains unresolved.

**Recovery:** Record the gap and owner, seek clarification or current evidence, and return only the separable proposal content that remains supportable.

## Quality Standards
- Use one clear proposer identity across the proposal unless a multi-entity arrangement is explicit.
- Keep voice, credentials, and experience evidence aligned to the selected profile.
- Treat profile files as living records that can be updated after successful proposals.

## Anti-Patterns

- Do not draft proposal content before resolving the proposer identity.
- Do not mix individual and company voices inside the same section unless the structure requires it.
- Do not reference Peter or Chwezi when ghostwriting for a client unless they are genuinely part of the team.
- Treating a neighbouring sector or framework as interchangeable. **Fix:** identify the controlling rule and primary outcome.
- Adding terminology without changing a delivery choice. **Fix:** link each term to method, risk, output, or evaluation criterion.
- Presenting an unverified current rule or statistic as settled. **Fix:** cite and date the source or mark it not assessed.
- Ignoring a missing mandatory input. **Fix:** stop the affected claim and assign an evidence owner.
- Letting sector or identity framing contradict methodology, staffing, schedule, or price. **Fix:** reconcile all affected sections before release.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| A selected proposer profile and a clear voice rule for the rest of the proposal. | Proposal lead, section writer, and evaluator-readiness reviewer | Applied consistently, traceable to the selected source, and free of unsupported identity, framework, or sector claims. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Routing and source record | Proposal lead and reviewer | Selected identity, framework, sector, source, date, and material gaps are recorded. |
| Decision record | Section writer and delivery lead | Each material choice has rationale, owner, evidence, and a review or stop condition. |
| Conformance check | Release reviewer | Mandatory forms, identity rules, sector logic, and unresolved checks are explicitly assessed. |

## Capability Contract

This skill may read supplied profiles, solicitations, ToRs, approved references, and proposal drafts and may prepare routing guidance or draft content within the authorised workspace. Review is read-only by default. It must not invent credentials, certify compliance, submit a bid, accept terms, publish, disclose confidential information, or change source records without explicit authority.

## Degraded Mode

If the solicitation, profile, current procurement source, sector evidence, network, or reviewer is unavailable, provide the narrowest useful qualified routing or draft. Mark the missing check **not assessed**, omit unsupported credentials, thresholds, dates, or compliance claims, and identify the evidence owner. An unassessed requirement is never a pass.

## Decision Rules

| Decision | Action | Failure/risk avoided |
|---|---|---|
| Proposer identity | Select one primary profile and document any consortium or sub-consultant relationship before drafting. | Mixed voice, false credentials, or wrong signatory |
| Conflicting solicitation and background guidance | Follow the solicitation while recording the conflict for formal clarification. | Non-responsive interpretation |
| Missing mandatory evidence | Stop the affected claim or form, record the owner and deadline, and continue only with independent supported content. | Fabricated evidence or silent omission |
| Submission, certification, or contractual commitment | Obtain explicit authority and preserve approval evidence before acting. | Unauthorised external commitment |

## Worked Example

A solicitation requires **proposer identity**, but one controlling input is missing. The proposal team applies this rule: Select one primary profile and document any consortium or sub-consultant relationship before drafting. It records the gap and owner, withholds the affected assurance, and proceeds only with content that can be verified. This avoids **mixed voice, false credentials, or wrong signatory**.

## References

- [Proposal skill router](../../SKILL.md) — orchestration, profile, reasoning, and release gates.
<!-- dual-compat-end -->
- Profile markdown files in this directory.
- [Proposal-level orchestration](../../SKILL.md).

Every proposal is written on behalf of a specific entity. The profile determines the voice, credentials, experience, and branding used throughout the document. **Load exactly one profile before generating any proposal content.**

## How It Works

1. **User specifies the proposer** — "write this as Peter", "write this for Chwezi", "write this for [client name]"
2. **Load the matching profile** from this directory
3. **Apply the profile** to every section: voice, signatory, experience, team, references
4. **If no profile exists** for the specified proposer, copy `client-template.md`, fill it in with the user, and save it for future use

## Available Profiles

| Profile | File | Proposer Type | Voice |
|---|---|---|---|
| **Peter Bamuhigire** | `peter-bamuhigire.md` | Individual consultant | First-person singular ("I propose…") |
| **Chwezi Core Systems** | `chwezi-core-systems.md` | Company | First-person plural ("We propose…") |
| **Client template** | `client-template.md` | Any (copy and customise) | As specified by client |

## Profile Selection Rules

| User Says | Profile to Load |
|---|---|
| "Write as Peter" / "individual consultant" / "as me" | `peter-bamuhigire.md` |
| "Write as Chwezi" / "as the company" / "as our firm" | `chwezi-core-systems.md` |
| "Write for [client name]" / "on behalf of [name]" | Load `[client-name].md` if it exists, otherwise create from `client-template.md` |
| No proposer specified | **Ask before proceeding.** The profile affects every section. |

## What the Profile Controls

| Proposal Element | Individual Consultant | Company | Client |
|---|---|---|---|
| **Voice** | "I propose…", "My approach…" | "We propose…", "Our team…" | As specified in profile |
| **Cover letter signatory** | Name only | Name + Title + Company | Per profile |
| **Firm profile section** | "Consultant Profile" — individual credentials, qualifications, track record | "Firm Profile" — legal status, structure, staff, offices, capabilities | Per profile |
| **Team composition** | Consultant as lead + any associates/sub-consultants | Named staff with organisational depth | Per profile |
| **Experience section** | Personal assignments with individual role emphasised | Corporate assignments with firm as contracting entity | Per profile |
| **References** | Personal professional references | Corporate client references | Per profile |
| **Value statement** | Individual expertise and track record | Organisational capability and depth | Per profile |
| **Branding** | Full name at first mention, then "the Consultant" | Full company name at first mention, then short name or "the firm" | Per profile |

## Combination Scenarios

Proposals sometimes involve multiple entities:

### Individual Consultant + Associates
- Load [peter-bamuhigire.md](peter-bamuhigire.md) as primary profile
- List associates in team composition with their roles
- Voice remains first-person singular with "supported by" language

### Company + Sub-Consultants
- Load [chwezi-core-systems.md](chwezi-core-systems.md) as primary profile
- Sub-consultants appear in team composition and association arrangements
- Voice remains first-person plural

### Company as Lead + Peter as Named Expert
- Load the company profile as primary
- Peter appears in team composition with his CV
- Voice follows the company profile

### JV or Consortium
- Load both company profiles
- Cover letter references the JV/consortium arrangement
- Voice: "The Consortium proposes…" or "The Joint Venture will…"
- Lead firm identified; each firm's role described

### Writing for a Client
- Load the client's profile (or create one)
- **Do not reference Peter Bamuhigire or Chwezi Core Systems** unless the client is explicitly associating with you as a team member or sub-consultant
- You are the invisible proposal writer — the document speaks entirely in the client's voice

## Keeping Profiles Current

After each successful proposal, update the profile with:
- New experience entries (project name, client, country, year, outcome)
- New team members or associates
- Updated qualifications or certifications
- New differentiators or branded frameworks

Profiles are living documents — they grow with every assignment.
