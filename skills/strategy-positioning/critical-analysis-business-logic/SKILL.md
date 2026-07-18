---
name: critical-analysis-business-logic
description: Use when testing a proposal's evidence, logic, feasibility, commercial sense, or achievability before drafting or final review; use section skills to produce the actual proposal text.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Critical Analysis Business Logic
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Overview

Use this skill as the proposal suite's thinking gate. It prevents persuasive writing from becoming unsupported sales language. A proposal should win because its logic is clear: the client problem is understood, the solution fits the evidence, the work plan can be delivered, the budget matches the methodology, and risks are handled honestly.

<!-- dual-compat-start -->

## Use When

- Drafting or reviewing any proposal section that makes claims, promises outcomes, recommends a method, explains value, or justifies price.
- Turning research into an evaluator-facing argument.
- Writing methodology, implementation, risk, M&E, sustainability, team, or financial sections.
- Preparing high-value advisory, transformation, digital, operational-improvement, or donor proposals.

## Do Not Use When

- The task is only file maintenance, formatting, or profile lookup.
- The user only needs a grammar pass and the proposal logic has already been tested.

## Required Inputs

- RFP, ToR, advert, or client brief where available.
- Target evaluation criteria and buyer type.
- Proposer profile and relevant evidence.
- Methodology, work plan, staffing, budget, risks, and assumptions where available.

## Domain Method

1. State the evaluator's real decision: why should this proposer be trusted for this assignment?
2. Convert each major section into claim, evidence, warrant, assumption, countercase, and implication.
3. Use [reasoning-and-business-sense-gate](references/reasoning-and-business-sense-gate.md) to test essential questions, logic, business sense, feasibility, and achievability.
4. Apply ethical persuasion and evaluator psychology checks so strong writing does not become manipulation or unsupported confidence.
5. Check technical strategy where software, SaaS, AI, cloud, integrations, data, or operations are central.
6. Check that methodology, staffing, timeline, risk controls, M&E, sustainability, support, and budget tell the same delivery story.
7. Rewrite claims into evaluator-facing language: specific, evidenced, measurable, and proportionate.
8. Flag any proof gaps that cannot be solved by wording.

## Quality Bar

- Every major claim is backed by evidence, named experience, a method, or a clearly labelled assumption.
- The proposal makes logical sense to technical evaluators and business sense to economic buyers.
- The methodology can be delivered with the proposed team, time, tools, and budget.
- The value proposition is specific enough to be scored.
- Risks and constraints are not hidden.
- Premium pricing, support promises, and technical claims are defensible under the stated scope.

## Domain Risks

- Writing "we understand" without proving understanding.
- Listing activities without explaining why they solve the client's problem.
- Making outcome promises that depend on client actions, political support, data access, or budget not yet secured.
- Treating price as separate from scope, staffing, and implementation logic.
- Using frameworks as decoration instead of analytical structure.
- Calling an approach innovative when it is not tested, funded, staffed, or feasible.

## Existing Deliverables

- Stronger proposal argument.
- Proof-gap list.
- Assumption and risk notes.
- Section-level rewrite guidance.
- Final logic, feasibility, and achievability gate.

## Do Not Use When

- Do not use this skill when a neighbouring specialist named in the description owns the primary decision; route there first and use this skill only as a supporting layer.
- Do not use it to invent buyer facts, evidence, legal positions, statutory rules, delivery capacity, or current external claims.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| proposal draft, ToR, evidence register, work plan, team, and budget | Buyer, ToR, approved project record, accountable owner, or verified evidence source | Yes | Stop the affected decision, name the missing source, and return only a qualified outline or assumption register. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| reasoning-gate findings and release decision | Proposal owner and red-team reviewer | Claims trace to supplied evidence; assumptions, owners, exclusions, decisions, and observable acceptance tests are explicit. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Decision and source trace for the output | Reviewer and release owner | Each load-bearing choice identifies its source, rationale, accountable owner, and any unassessed check. |

## Capability Contract

Default to read-only for analysis, critique, discovery, and review. Minimum capability is access to the supplied artefacts and permission to inspect or calculate relevant evidence. Edit only the requested working copy. Do not publish, send, spend, change production systems, certify compliance, make a statutory claim, or approve a commercial concession without explicit authority.

## Degraded Mode

If required files, interviews, finance doctrine, search evidence, calculation tools, network access, or specialist review are unavailable, return the narrowest useful qualified result. Mark unavailable checks as not assessed, separate facts from assumptions, and state what is needed to resume. An unassessed gate is never a pass.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Accept, revise, or block a load-bearing claim | Test claim, evidence, warrant, assumption, countercase, and delivery implication. | Persuasive language masking weak feasibility. |
| Evidence conflicts or authority is absent | Stop the affected recommendation, record the conflict, and seek the named owner’s decision. | Invented facts or unauthorised commitments. |
| Evidence and approval are complete | Proceed within scope and retain the decision trace. | Irreproducible approval or scope drift. |

## Workflow

1. Confirm the consumer, decision, neighbouring-skill route, authority, and required inputs; stop if the primary route or accountable owner is unknown.
2. Inspect supplied evidence and record facts, assumptions, conflicts, and unavailable checks; stop on a load-bearing contradiction.
3. Apply the domain method and decision rules, preserving the repository’s proposal voice and specialist constraints.
4. Draft the contracted output with observable acceptance conditions and an evidence trace.
5. Review alignment with scope, work plan, team, pricing, risk, and dependent proposal sections; recover by revising the affected choice and rerunning the check.
6. Run the critical-analysis and anti-slop gates; block release on unsupported claims, failed safety or finance gates, or an F slop grade.

## Quality Standards

- Every load-bearing claim is verified or explicitly qualified, and the output distinguishes fact, assumption, recommendation, and commitment.
- Scope, method, work plan, staffing, pricing, risks, dependencies, and acceptance conditions remain mutually consistent.
- The output preserves domain constraints, names accountable owners, covers failure paths, and blocks unsupported or unauthorised promises.
- British English and the repository’s East African professional tone are used unless the buyer requires another standard.
- The critical-analysis and anti-slop gates pass before release, with no unassessed check represented as passed.

## Anti-Patterns

- Inventing a buyer fact or proof point. Fix: cite the supplied source or mark the statement as an assumption requiring confirmation.
- Treating an unavailable check as passed. Fix: mark it not assessed and name the evidence needed to resume.
- Copying a neighbouring skill’s method without routing. Fix: use the specialist for the primary decision and retain only the supporting layer here.
- Writing acceptance as “satisfactory” or “appropriate”. Fix: state an observable measure, evidence record, and decision owner.
- Adding premium or technical claims without delivery capacity. Fix: reconcile the claim with named people, time, budget, dependencies, and authority.

## Worked Example

A six-week rollout claim conflicts with a twelve-week dependency lead time. Block the claim, identify the dependency owner, and revise the plan or scope before drafting continues.

<!-- dual-compat-end -->

## References

- [reasoning-and-business-sense-gate](references/reasoning-and-business-sense-gate.md) - essential questions, argument map, business-sense gate, achievability checks, and final reviewer checklist.
- [proposal-strategy-and-persuasion](../../profiles-sectors/references/proposal-strategy-and-persuasion.md) - win themes, SCQA, Pyramid of Ideas, P-I-P, and red-team review.
- [ethical-persuasion-and-evaluator-psychology-gate](../../profiles-sectors/references/ethical-persuasion-and-evaluator-psychology-gate.md) - ethical persuasion, evaluator concerns, risk perception, and red flags.
- [technical-strategy-credibility-checklist](../../profiles-sectors/references/technical-strategy-credibility-checklist.md) - SaaS, AI, software, cloud, architecture, operations, and maintainability checks.
- [premium-rate-justification-framework](../../profiles-sectors/references/premium-rate-justification-framework.md) - premium value, price defence, options, and commercial proof ladder.
- [problem-structuring](../../domain-delivery/consulting-frameworks/references/problem-structuring.md) - issue trees, MECE, and hypothesis-driven analysis when the methodology needs deeper structure.
