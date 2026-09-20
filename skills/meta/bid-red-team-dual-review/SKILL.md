---
name: bid-red-team-dual-review
description: Use when a high-stakes bid, tender response, EOI, or compliance-sensitive proposal section needs adversarial two-reviewer verification with a compliance rubric before it ships; use kaizen-improvement-system for the full engine/product audit and ai-slop-audit for the routine per-section gate.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Bid Red Team Dual Review
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178. Dual-review contract adapted from the Santa Method (origin: Ronald Skelton, Founder, RapportScore.ai), read from the ECC skill engine's `skills/santa-method/SKILL.md`, and scoped to this engine's tender/EOI/compliance context.

<!-- dual-compat-start -->
## Use When

- A bid, tender response, EOI, or proposal section will be submitted to a buyer, evaluator, donor, or regulator and a single self-review is not enough assurance for the stakes involved (large value, regulated sector, legal/financial commitments, reputational exposure).
- The routine `ai-slop-audit` per-section gate has passed but the content still carries compliance, legal, financial, or outcome-guarantee risk that a style/slop audit does not test.
- `kaizen-improvement-system` step 6 ("run one time-boxed evaluator simulation or compliance red-team") calls for a red-team pass and the stakes justify two independent reviewers instead of one.
- Content makes claims that, if wrong or unsubstantiated, would trigger a compliance knockout, a legal exposure, or a false outcome guarantee (financial services, health, public-sector, donor-funded, or regulated-industry proposals).

## Do Not Use When

- The content is an internal draft, exploratory outline, or working note not yet intended for evaluator eyes — use `anti-ai-slop` as the real-time guardrail instead.
- The check is purely mechanical (page limits, price tokens in the technical folder, file naming) — use the relevant submission checklist, e.g. `skills/domain-delivery/giz-eu-local-procurement-response/references/submission-pack-checklist.md`, or `submission-proof-and-receipt-discipline` for what-was-sent evidence.
- No second reviewer context (a genuinely isolated second pass, human or agent) is available — see Degraded Mode.

## Required Inputs

| Artefact | Source/provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| The content under review, in near-final form | Proposal draft | Yes | Fixed target for both reviewers | Stop; nothing to review |
| The evaluation rubric (base + compliance-sensitive extension, below) | This skill | Yes | Objective pass/fail criteria for both reviewers | Stop; do not improvise criteria mid-review |
| ToR/RFP mandatory requirements and evaluation criteria | Buyer documents | Yes for compliance checks | Anchors "approved terminology" and "jurisdiction-appropriate language" checks in the actual tender, not a past one | Mark compliance checks `NOT_ASSESSED`, per the never-infer-evaluation-criteria rule in `rules/common/core.md` |
| Evidence register / claim sources | Proposal working papers | Conditional | Supports the factual-accuracy and hallucination checks | Flag unverifiable claims as findings, do not silently pass them |

## Workflow

### Phase 1 — Fix the target

Freeze the exact text/version under review. Santa Method is a post-generation verification layer, not a drafting technique — do not revise while reviewers are working.

### Phase 2 — Independent dual review

Spawn two reviewers with **no shared context**:

1. Neither reviewer sees the other's assessment, prompt, or existence.
2. Both receive the identical rubric (below) and the identical content under review.
3. Each reviewer returns a structured verdict per criterion: `PASS` or `FAIL` with the specific issue cited — not prose impressions.
4. Each reviewer's brief is explicitly adversarial: "your job is to find problems, not approve." Rubber-stamping both reviewers defeats the method.

In this engine, run reviewers as separate `Agent` tool invocations (or, if agents are unavailable, as fully context-reset sequential passes — see Degraded Mode) so isolation is real, not simulated.

### Phase 3 — Base rubric

| Criterion | Pass condition | Failure signal |
|---|---|---|
| Factual accuracy | Every claim verifiable against the evidence register or the ToR/RFP | Invented statistics, wrong dates, misstated buyer requirements |
| Hallucination-free | No fabricated entities, quotes, credentials, or citations | Attributed quotes with no source, invented reference projects |
| Completeness | Every ToR/RFP requirement and scored criterion is addressed | Missing sections, skipped mandatory items, unanswered evaluation questions |
| Internal consistency | No contradictions across technical, financial, and annex content | Methodology promises what the work plan or budget does not support |
| Compliance (base) | Passes this engine's own gates already run (anti-ai-slop, ai-slop-audit) | Slop-audit grade F content reaching this review unresolved |

### Phase 4 — Compliance-sensitive rubric extension

Apply this extension whenever the content is regulated, legal, or financial — the default assumption for tender and EOI submissions:

| Criterion | Pass condition | Failure signal |
|---|---|---|
| No outcome guarantees or unsubstantiated claims | Results are stated as targets, ranges, or evidenced track record — never as guaranteed outcomes | "We will guarantee a 30% cost reduction" with no basis |
| Required disclaimers present | Every place the ToR/RFP or sector norm requires a disclaimer, qualification, or assumption statement has one | A financial projection with no assumptions stated; a health/safety claim with no scope limit |
| Approved terminology only | Language matches the buyer's own terms (from the ToR/RFP, evaluation grid, or sector skill) rather than the proposer's marketing vocabulary | Renaming a buyer's defined deliverable, inventing a certification name |
| Jurisdiction-appropriate language | Legal, tax, licensing, and regulatory statements match the jurisdiction named in the ToR/RFP, sourced per `operational-readiness-and-localisation` and Digital Research, not assumed from another market | A claim correct in one country asserted without qualification in another |

### Phase 5 — Verdict gate

Both reviewers must return `PASS` on every criterion for the content to ship. One reviewer catching an issue the other misses means the issue is real — that asymmetry is exactly what independent review exists to surface, not a tie-break to resolve by majority.

### Phase 6 — Fix and reconverge

1. Merge and deduplicate both reviewers' findings.
2. Fix only the flagged issues — no unrequested rewriting.
3. Re-run **both** reviewers as fresh instances with no memory of the previous round, on the same rubric, against the fixed content.
4. Repeat for a maximum of 3 iterations total.
5. If round 3 still fails, stop and escalate to the accountable reviewer/signatory named in the relevant pipeline or domain skill — do not ship on a fourth attempt or on partial credit.

## Decision Rules

| Condition | Action |
|---|---|
| Both reviewers PASS all criteria | Ship — record the result as this skill's evidence artefact |
| Either reviewer FAILs any criterion | Fix and reconverge (Phase 6); never ship on one PASS and one FAIL |
| 3 iterations exhausted without full PASS | Stop, escalate to a human signatory, do not submit |
| No genuinely isolated second reviewer available | Downgrade to Degraded Mode and label the result accordingly — never present a single-reviewer pass as a dual-review PASS |
| Compliance-sensitive extension criterion fails | Treat as a knockout-equivalent finding — same severity as a `kaizen-improvement-system` compliance blocker |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Dual-review verdict record (both reviewers' structured checks, iteration count, final verdict) | Proposal lead, reviewer, release owner | Shows both reviewers' criteria-by-criteria results and the round they converged on, or the escalation |
| Findings register (deduplicated, with fix applied per item) | Bid lead | Every FAIL traces to a specific fix or an explicit accepted-risk note from the accountable owner |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Reviewer A and Reviewer B structured verdicts | Reviewer and release owner | Independently reproducible — a third party could re-run the same rubric against the same content and reach a comparable verdict |
| Iteration log | Release owner | States round count, what changed each round, and whether convergence or escalation occurred |

## Capability Contract

Read and search are required. Running two independent reviewer agents requires the `Agent` tool or an equivalent isolated second pass; fixing flagged content requires the same drafting authority as the section being reviewed. Final submission remains gated by `kaizen-improvement-system` and this engine's own release rules — this skill produces one input to that gate, not a standalone ship decision.

## Degraded Mode

Without a genuinely isolated second reviewer (no `Agent` tool, no second human), simulate isolation with an explicit context reset between passes: record Reviewer A's findings verbatim, clear context completely, then run Reviewer B fresh against the same rubric and content with no visibility into Reviewer A's output. Label the result "single-session simulated dual review" rather than a true dual review, since context bleed risk is real even with a reset, and flag this limitation to the release owner.

## Domain Anti-Patterns

- Letting one reviewer see the other's findings before completing their own pass (anchoring bias).
- Treating a compliance-sensitive rubric failure as a style note rather than a knockout-equivalent finding.
- Reusing the same reviewer instance across fix rounds instead of spawning fresh reviewers each round.
- Inferring "approved terminology" or "jurisdiction-appropriate language" from a similar past tender instead of the current ToR/RFP (see `rules/common/core.md`).
- Shipping on a fourth iteration instead of escalating after round 3.
- Presenting a single-reviewer or self-review pass as a dual-review PASS.
