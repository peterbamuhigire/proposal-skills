---
name: proposer-profiles
description: Proposer identity system. Read this skill before writing any proposal to determine WHO is proposing. The profile controls voice (I/we), signatory, firm profile content, experience references, and branding throughout the document. Every proposal must load exactly one profile.
---

# Proposer Profiles
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When
- Use this skill whenever proposal content needs the correct proposer identity, signatory, or voice.
- Load it when the user asks to write as a person, company, consortium, or client.

## Do Not Use When
- The task is unrelated to proposal authorship or identity.
- A proposer profile has already been selected and does not change.

## Required Inputs
- The proposer name or relationship structure.
- Any existing profile file or details needed to adapt `client-template.md`.
- The proposal type so the selected identity can be applied consistently.

## Workflow
1. Determine who the proposal is being written for before drafting any section.
2. Load exactly one primary profile unless the engagement explicitly requires a consortium or joint venture.
3. Apply the selected profile to voice, signatory, experience framing, team composition, and branding.
4. Create or adapt a client profile if no existing file fits.
5. Re-check downstream sections for profile consistency before finalizing.

## Quality Standards
- Use one clear proposer identity across the proposal unless a multi-entity arrangement is explicit.
- Keep voice, credentials, and experience evidence aligned to the selected profile.
- Treat profile files as living records that can be updated after successful proposals.

## Anti-Patterns
- Do not draft proposal content before resolving the proposer identity.
- Do not mix individual and company voices inside the same section unless the structure requires it.
- Do not reference Peter or Chwezi when ghostwriting for a client unless they are genuinely part of the team.

## Outputs
- A selected proposer profile and a clear voice rule for the rest of the proposal.

## References
- Profile markdown files in this directory.
- `../SKILL.md` for proposal-level orchestration.

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
- Load `peter-bamuhigire.md` as primary profile
- List associates in team composition with their roles
- Voice remains first-person singular with "supported by" language

### Company + Sub-Consultants
- Load `chwezi-core-systems.md` as primary profile
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

