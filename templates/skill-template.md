---
name: example-skill
description: Use when [specific trigger] requires [domain output]; use [neighbour-skill] instead for [nearest excluded case].
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Example Skill
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

State the repeatable proposal procedure and the decision it supports in one or two sentences.

## Use When

- Use when [concrete positive trigger].
- Use when [second trigger that produces the same output contract].

## Do Not Use When

- Use `[neighbour-skill]` when [nearest excluded scenario].
- Stop when [missing authority or evidence would make execution unsafe].

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| [Named source artefact] | [ToR, client, profile, upstream skill, or verified source] | Yes | Stop or return a qualified gap; do not invent it. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| [Named deliverable] | [Evaluator, proposal lead, or downstream skill] | [Observable completeness, consistency, or approval condition] |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| [Decision record, source register, calculation, or checklist] | [Reviewer or release gate] | [Traceable source, result, and unresolved gap] |

## Capability Contract

Read and search are required. Editing is permitted only when the task authorises drafting or revision. Publishing, spending, destructive changes, external messages, and certification claims require explicit authority.

## Degraded Mode

When a required file, tool, network source, rendering capability, or item of evidence is unavailable, return the narrowest useful qualified result, mark the affected check `not assessed`, and state what would clear the gap. Never convert an unassessed check into a pass.

## Decision Rules

| Condition or choice | Action | Failure or risk avoided |
|---|---|---|
| [Domain condition] | [Specific action] | [Named wrong-choice failure] |

## Workflow

1. Inspect the inputs and route to the correct neighbour.
2. Apply the domain decision rules and record evidence gaps.
3. Produce the named output and test its acceptance conditions.
4. Stop if a mandatory source, authority, or release gate is missing.
5. Recover by correcting the output, obtaining the missing input, or returning the qualified degraded result.

## Quality Standards

- The output is evaluator-facing, internally consistent, evidence-backed, and usable by its named consumer.
- Assumptions, exclusions, risks, and unassessed checks are visible.

## Anti-Patterns

- [Concrete failure]. Fix: [specific correction].
- [Concrete failure]. Fix: [specific correction].
- [Concrete failure]. Fix: [specific correction].
- [Concrete failure]. Fix: [specific correction].
- [Concrete failure]. Fix: [specific correction].

## References

- [Proposal skill authoring standard](../docs/skill-authoring-standard.md)
- [Parent or neighbouring skill](../skills/SKILL.md)
