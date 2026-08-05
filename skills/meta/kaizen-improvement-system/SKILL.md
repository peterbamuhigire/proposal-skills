---
name: kaizen-improvement-system
description: Use when auditing or improving the proposal engine or any bid, tender, EOI, methodology, technical/financial proposal, or consulting product it produces.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Kaizen Improvement System
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Auditing a proposal engine, bid, tender response, EOI, or consulting deliverable.
- Converting evaluator feedback, compliance misses, delivery lessons, or new evidence into a tested improvement.

## Do Not Use When

- The task is only single-skill safety review.
- Current procurement, legal, market, finance, or technical claims lack verified source or evidence routing.

## Required Inputs

| Artefact | Source/provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| ToR/RFP, evaluation criteria, audience, proposal artefact, evidence register, compliance matrix, assumptions, and current score | Client brief and proposal project | yes | Set audit scope and evaluator bar | Stop or mark unassessed |

## Workflow

1. Read the local adoption plan, proposal router, profile/sector rules, and portfolio standard.
2. Inventory section routes, references, templates, examples, visual/document handoffs, and release gates.
3. Score every applicable dimension and product output. Publish `min(raw score, 65)` and record blockers.
4. Audit compliance, evaluator journey, evidence, methodology, feasibility, staffing, risk, M&E, budget separation, document fidelity, ethics, and submission readiness.
5. Create a P0/P1/P2 plan targeting 95/100. Every action names a file, owner, measure, acceptance proof, and rollback.
6. Run one time-boxed evaluator simulation or compliance red-team. If the result fails, stop, recover the last safe version, and revise.
7. Run source-ingestion, anti-slop, document/render, and release gates; standardise successful learning and record the next review.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Capped audit, evaluator/evidence gap register, 95/100 plan, experiment result, and standardisation record | Proposal lead, reviewer, and release owner | Every finding has evidence, action, owner, acceptance proof, and re-audit date |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Compliance matrix, evaluator score, red-team findings, source register, render review, and revision diff | Reviewer and release owner | Another reviewer can reproduce the decision and confirm the correction |

<!-- dual-compat-end -->
## Capability Contract

Read and search are required. Proposal audits are read-only by default; edits, submissions, or external communication require explicit authority and permission. Route current facts to Digital Research.

## Degraded Mode

If the ToR, evaluation grid, evidence, source, render, or reviewer is unavailable, return a qualified result, mark the gap not assessed, and withhold submission readiness.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A value claim lacks evaluator-relevant proof | Narrow the claim or add evidence before release | Unsupported promise |
| A technical or financial envelope is required separately | Preserve the separation and re-check the submission package | Disqualification |
| A red-team finding remains unresolved | Block release or obtain a documented decision | Hidden compliance risk |

## Quality Standards

A persuasive narrative never substitutes for compliance or proof. Keep technical and financial envelopes separate when required. Expert advice must stay within verified competence and compliance boundaries.

## Anti-Patterns

- Storytelling without evaluator evidence. Fix: link each value claim to proof.
- Generic methodology pasted into a ToR. Fix: map activities, outputs, risks, measures, and context.
- Inflated capability claims. Fix: scope, qualify, and verify.
- Improvement plans with only language edits. Fix: add fixture, test, or reviewer evidence.
- Uncontrolled book or OCR ingestion. Fix: retain independent synthesis only.

## Worked Example

If a draft scores well on narrative but fails two mandatory ToR requirements, keep the score capped, block release, repair the compliance matrix and evidence, then repeat the evaluator simulation.

## References

- [Local adoption plan](../../../docs/continuous-improvement/kaizen-adoption-2026-08.md)
- [Portfolio standard](C:/wamp64/www/digital-research-skills/docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md)
- `skills/meta/ai-slop-audit/`
- `skills/strategy-positioning/critical-analysis-business-logic/`
