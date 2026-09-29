---
name: skill-writing
description: Use when creating or normalising reusable proposal skills, trigger routes, contracts, references, or authoring automation under the canonical chwezi-dev-engine skill-writing standard; use skill-safety-audit instead for a read-only security review.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# Skill Writing
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Pointer stub. The canonical standard is `chwezi-dev-engine/skills/sdlc-meta/skill-writing` ([canonical on GitHub](https://github.com/peterbamuhigire/chwezi-dev-engine/blob/main/skills/sdlc-meta/skill-writing/SKILL.md); local path `C:\wamp64\www\chwezi-dev-engine\skills\sdlc-meta\skill-writing\SKILL.md`). Load it first; this file keeps a portable minimum and this engine's delta.
<!-- dual-compat-start -->
## Use When
- Creating or upgrading an active proposal skill, its trigger description or its directly linked resources.
## Do Not Use When
- Use `skill-safety-audit` for a read-only inspection of unsafe instructions or bundled resources.
## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Reusable problem, trigger prompts and neighbour descriptions | Requester and live catalogue | Yes | Stop; search the catalogue before drafting. |
| Canonical skill-writing standard | chwezi-dev-engine checkout or GitHub | Yes | Apply the portable minimum and mark canonical-only checks `NOT ASSESSED`. |
## Workflow
1. Read the canonical standard, then this engine's delta; inspect the closest neighbours.
2. Write the input, output, evidence, capability, degraded-mode and decision contracts before the procedure.
3. Run `python -X utf8 scripts/validate_skills.py`, `python -X utf8 scripts/routing_smoke_test.py`, `python -X utf8 scripts/source_ingestion_guardrail.py` and `git diff --check`, then `python -X utf8 skills/meta/skill-writing/scripts/quick_validate.py <skill-dir>`.
4. Stop on any finding or routing collision; recover by fixing the named contract and rerun, never by weakening the gate.
## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Skill directory and routing fixtures | Maintainer and router | Validators pass and the expected skill ranks in the top three. |
## Evidence Produced
| Evidence | Artefact and format | Consumer | Acceptance condition |
|---|---|---|---|
| Validation and routing record | Command output | Release owner | Zero findings; unrun checks marked `NOT ASSESSED`. |
<!-- dual-compat-end -->
## Quality Standards
- Portable minimum, applied even when the canonical is unreachable: frontmatter uses only approved keys and `name` matches the folder.
- The description starts `Use when`, stays within 350 characters and names a neighbour, with no workflow steps.
- `SKILL.md` stays within 500 lines; deep detail sits in references one level deep, linked directly.
- Every new or changed skill gets positive, negative and collision routing fixtures.
- Bundled scripts run through their interpreter, for example `python -X utf8 scripts/<name>.py`.
- No book extractions or copied third-party text; paraphrase and attribute.
- British English, the imperative mood, and `NOT ASSESSED` for any check not run.
## Engine-Local Delta
- Follow the [proposal authoring standard](../../../docs/skill-authoring-standard.md); frontmatter holds only `name`, `description` and `metadata`, and the acknowledgement sits under the title.
- Run the source-ingestion guardrail whenever a book or other copyrighted source informs the work, and apply [anti-AI slop](../anti-ai-slop/SKILL.md) before release.
## Capability Contract
Read and search are required. Editing files and running validators need explicit permission for the authoring task; publishing, deletion and release changes need separate authorisation.
## Degraded Mode
If the canonical standard is unavailable, apply the portable minimum, return the narrowest qualified result, and mark each canonical-only check `NOT ASSESSED`; never report it as passed.
## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| An existing skill owns the trigger and output | Normalise it in place; put branch-only detail in a linked reference | Duplicate routes and oversized entrypoints |
## Anti-Patterns
- Copying the canonical body into this engine. Fix: link the canonical and keep only the delta here.
- Writing only positive triggers. Fix: name the neighbour and add a collision fixture.
- Treating an unrun validator as a pass. Fix: record `NOT ASSESSED` with the reason.
- Granting edit rights to a review procedure. Fix: default review and audit to read-only.
- Weakening a baseline to clear a finding. Fix: repair the named contract instead.
## Worked Example
When `financial-proposal` overlaps `work-plan`, keep pricing and fee assumptions in `financial-proposal` and route staffing days to `work-plan`; a fixture asking for a price schedule must rank the financial skill in the top three.
## References
- [Canonical skill-writing standard](https://github.com/peterbamuhigire/chwezi-dev-engine/blob/main/skills/sdlc-meta/skill-writing/SKILL.md)
- [Proposal authoring standard](../../../docs/skill-authoring-standard.md)
- [Skill safety audit](../skill-safety-audit/SKILL.md)
- [Anti-AI slop](../anti-ai-slop/SKILL.md)
