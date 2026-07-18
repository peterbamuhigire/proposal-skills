---
name: blog-writer
description: Use when drafting, revising, or finalising a publishable blog post, article, guide, case study, or thought-leadership piece; use blog-idea-generator when only topic discovery is required.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Blog Writer
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Turn an approved content brief and evidence set into an authored article with a clear reader promise, defensible claims, and publication-ready structure.

<!-- dual-compat-start -->
## Use When

- Draft or substantially revise a blog post, article, tutorial, opinion piece, case study, or long-form guide.
- Convert an approved topic and evidence pack into publishable content.

## Do Not Use When

- Use `blog-idea-generator` when the task ends at topic options, angles, or a content backlog.
- Do not write source-dependent claims when the evidence pack is missing or unverifiable.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Content brief, audience, and publication goal | Client or content lead | Yes | Stop and return the minimum questions needed to establish the reader promise. |
| Approved angle and evidence pack | `blog-idea-generator`, research, or subject expert | Yes for factual content | Narrow the article or flag claims as not assessed; do not invent citations or experience. |
| Voice, length, SEO, and publication constraints | Brand or editor | Conditional | State assumptions and avoid claiming brand or search compliance. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Publication-ready article | Editor and intended reader | The opening earns attention, the body fulfils one reader promise, claims are sourced or qualified, and the ending gives a useful next step. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Claim and source check | Editor | Every load-bearing factual claim maps to a source or an explicit qualification. |
| Editorial quality check | Publisher | Structure, voice, links, metadata, and unresolved edits are recorded. |

## Capability Contract

Read and search are required. Editing is allowed for authorised drafting and revision. Network research, publishing, image licensing, paid promotion, external messages, and claims of personal experience require explicit authority and evidence.

## Degraded Mode

Fallback: when research, subject expertise, brand guidance, or publishing tools are unavailable, return the narrowest useful qualified draft, mark source and publication checks `not assessed`, and do not invent facts, quotes, experience, or SEO results.

## Decision Rules

| Condition or choice | Action | Failure or risk avoided |
|---|---|---|
| Reader needs a practical sequence | Use a guide or tutorial structure with tested steps | Decorative advice with no usable path |
| Claim depends on data or current facts | Verify and cite it at the point of claim | Confident wrongness |
| Topic is opinion-led | State the thesis, evidence, countercase, and limits | Viewpoint-free filler |
| Only ideas are requested | Route to `blog-idea-generator` | Premature long-form drafting |

## Workflow

1. Confirm the audience, reader promise, angle, evidence, voice, and publication constraints.
2. Select a structure that matches the reader's job and outline only sections that advance it.
3. Draft with specific evidence, authored reasoning, varied rhythm, and explicit hard cases.
4. Stop when a load-bearing claim, quotation, case, or personal experience cannot be supported.
5. Recover by verifying, qualifying, removing, or reframing the affected passage.
6. Edit for logic, voice, scanning, links, metadata, and the anti-slop gate before handoff.

## Quality Standards

- The article makes one defensible promise and fulfils it without padded sections or search-engine mimicry.
- Sources, examples, counterarguments, edge cases, and the writer's actual point of view are visible.

## Anti-Patterns

- Opening with a generic statement about a changing world. Fix: begin with the reader's concrete problem, tension, or evidence.
- Adding statistics without a source. Fix: cite a verified source or remove the number.
- Writing five interchangeable sections to reach a word count. Fix: keep only sections that advance the reader promise.
- Presenting borrowed experience as personal. Fix: attribute the case or label it as an example.
- Optimising keywords before the argument works. Fix: establish substance and reader usefulness first.

## Worked Example

For an article on tender pricing, lead with the mismatch between proposed staff-days and fee totals, show a small traceable calculation, explain the evaluator risk, cover the case of reimbursables, and end with a pre-submission reconciliation check. Do not pad it with generic claims about competitive markets.

## References

- [Comprehensive blog-writing guide](references/comprehensive-blog-writing-guide.md)
- [Editorial standards](references/editorial-standards.md)
- [Writing craft](references/writing-craft.md)
- [Blog idea generator](../blog-idea-generator/SKILL.md)
- [Anti-slop guardrail](../../meta/anti-ai-slop/SKILL.md)
<!-- dual-compat-end -->
