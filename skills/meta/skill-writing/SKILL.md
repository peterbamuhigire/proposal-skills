---
name: skill-writing
description: Use when creating or normalising reusable proposal skills, trigger routes, contracts, references, or authoring automation; use skill-safety-audit instead for a read-only security review.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Skill Writing
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Create concise, portable proposal procedures that another agent can route, execute, verify, and hand off without depending on one runner.

<!-- dual-compat-start -->
## Use When

- Create or upgrade an active proposal skill, its trigger description, or its directly linked resources.
- Normalise a catalogue cohort against the July 2026 authoring and composition contract.
- Add deterministic authoring or validation helpers that reduce repeatable structural errors.

## Do Not Use When

- Use `skill-safety-audit` for a read-only inspection of unsafe instructions or bundled resources.
- Do not create a new skill for a one-off request, generic knowledge, or a metric improvement.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Repeatable problem and representative prompts | User or catalogue evidence | Yes | Stop; do not invent a trigger without a demonstrated workflow. |
| Neighbouring skill descriptions | Live `skills/**/SKILL.md` catalogue | Yes | Search the catalogue before defining scope or routing. |
| Capability and permission boundary | Parent task and repository policy | Yes | Default to read-only and identify the missing authority. |
| Third-party source notes, if used | Temporary workspace outside the repository | No | Apply the source-distillation policy; never ingest a raw book or reconstructive extract. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Normalised skill entrypoint and linked resources | Routing engine and downstream agents | Local and canonical validators pass; scope and neighbour boundary are explicit. |
| Routing fixtures | Release gate | Positive, negative, collision, limited-capability, and failure paths have expected routes. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Validation and routing results | Maintainer | Results identify the skill directory, checks run, line count, and zero residual findings. |

## Capability Contract

Read and search are required. Editing and local validator execution are permitted only for an authorised authoring task. Network access, delegation, publishing, deletion, package installation, and release mutation require explicit authority.

## Degraded Mode

Without editing or execution, return the narrowest useful scored contract gap and a proposed patch, mark validation `not assessed`, and never claim compliance.

## Decision Rules

| Condition or choice | Action | Failure or risk avoided |
|---|---|---|
| Stable procedure used across proposals or roles | Create or update one skill | One-off advice masquerading as infrastructure |
| Existing skill has correct scope but incomplete contract | Normalise in place | Unnecessary taxonomy churn |
| Two skills compete for the same prompt and output | Clarify triggers, then merge or alias only with evidence and authority | Persistent routing collision |
| Detail is required only on a specialist branch | Move it to a directly linked reference | Oversized entrypoint and irrelevant context loading |

## Workflow

1. Discover the live catalogue and inspect the target skill, neighbours, and directly linked references.
2. Define the reusable problem, positive and negative triggers, capability boundary, and named outputs.
3. Stop if the change would create unjustified scope, remove domain knowledge, or alter active count without authority.
4. Write the contracts first, then preserve and reorganise the useful domain workflow around them.
5. Recover from validator or routing failure by correcting the smallest responsible contract, not weakening the gate.
6. When a book or other copyrighted source informs the work, apply [the source-distillation policy](references/source-distillation-and-copyright.md) and retain only independently written, task-specific synthesis.
7. Run local validation, routing fixtures, `python -X utf8 scripts/source_ingestion_guardrail.py`, the canonical scanner, canonical quick validation, safety review, and anti-slop audit.

## Quality Standards

- [SKILL.md](SKILL.md) stays within 500 lines, uses British English, and keeps deep detail in directly linked references.
- Frontmatter, acknowledgement, inputs, outputs, evidence, decisions, permissions, degraded mode, workflow, and acceptance conditions are independently checkable.
- Examples clarify domain judgement; they do not contain invented client facts, prices, credentials, or citations.
- Source-derived guidance is independently expressed, minimally quoted, attributed where appropriate, and cannot reconstruct the source.

## Anti-Patterns

- Copying the same canonical body into multiple engines. Fix: translate the contract into the local domain and keep one local source.
- Naming only positive triggers. Fix: identify the closest neighbour and write the negative route.
- Giving an audit skill write access. Fix: default analysis and review to read-only.
- Treating a missing tool as a pass. Fix: mark the check not assessed and return a qualified degraded result.
- Adding generic sections only to satisfy a counter. Fix: write domain inputs, decisions, evidence, outputs, and acceptance conditions.
- Moving routing or safety rules into a deep reference. Fix: keep load-bearing execution logic in [SKILL.md](SKILL.md).
- Retaining ebooks, scans, OCR output, full conversions, chapter dumps, or disguised/split copies. Fix: remove the source from the repository and keep only concise independent synthesis.

## Worked Example

When `financial-proposal` overlaps `work-plan`, keep pricing, reimbursables, fee assumptions, and separate-envelope rules in `financial-proposal`; route staffing days and activity sequencing to `work-plan`. A fixture asking for a price schedule “not the work plan” must rank the financial skill in the top three.

## References

- [Proposal skill authoring standard](../../../docs/skill-authoring-standard.md)
- [Authoring workflows](references/workflows.md)
- [Output patterns](references/output-patterns.md)
- [Skill authoring practices](references/skill-authoring-best-practices.md)
- [Source distillation and copyright boundary](references/source-distillation-and-copyright.md)
- [Skill safety audit](../skill-safety-audit/SKILL.md)
<!-- dual-compat-end -->
