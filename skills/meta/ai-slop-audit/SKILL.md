---
name: ai-slop-audit
description: Use when auditing an existing proposal artefact for AI slop after a major iteration or before submission; use anti-ai-slop instead as the live drafting guardrail.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# AI Slop Audit
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

The detector. Given any proposal artefact, it decides how strongly it reads as AI slop, names exactly why, and says how to fix each finding. Production-side prevention is the companion `anti-ai-slop` skill, and the reasoning gate is `critical-analysis-business-logic`.

<!-- dual-compat-start -->
## Use When

- Audit a completed proposal section, EoI, tender response, price narrative, or full bid after a major iteration.
- Run the final A/B/C/F gate before assembly or submission.

## Do Not Use When

- Use `anti-ai-slop` while creating content; this skill assesses a concrete artefact in read-only mode.
- Do not grade material that cannot be inspected; return an unassessed scope instead.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Proposal artefact and intended audience | Proposal lead | Yes | Stop and request the artefact or identify the inaccessible scope as not assessed. |
| Sources for factual claims | Bid evidence register or verified provider | Conditional | Mark factual verification not assessed; do not clear a blocking claim. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Graded slop audit | Author and release owner | Verdict, genericness score, evidence, fix, and unassessed checks agree with the grading rules. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Finding register and A/B/C/F verdict | Proposal release gate | Every finding cites a line, phrase, figure, source, or other observable artefact evidence. |

## Capability Contract

Default to read-only. Read and search are required; execution or network checks may verify claims when authorised. Never edit the audited artefact unless remediation is separately requested, and never submit it externally.

## Degraded Mode

When a file, source, renderer, or verification capability is unavailable, mark that check `not assessed` and return the narrowest evidence-backed grade possible. Do not lower risk or invent findings to fill the report.

## Decision Rules

| Evidence | Action or grade | Failure or risk avoided |
|---|---|---|
| Fabricated claim, citation, client, statute, or no substantive content | Grade F and block release | Unsupported submission |
| Multiple non-blocking markers or weak intent | Grade C and require rework | High reviewer burden |
| Minor isolated markers only | Grade B and list targeted fixes | Unnecessary full rewrite |
| No blockers, low genericness, clear intent | Grade A and release | Invented audit findings |

## Workflow

1. Classify the artefact and define the inspected scope.
2. Run applicable mechanical checks, then review substance, intent, specificity, and hard cases.
3. Stop and grade F when any blocking marker is evidenced.
4. Recover from incomplete access by marking checks not assessed, not by assuming a pass.
5. Issue the evidence-backed report and preserve authored material worth keeping.

## Quality Standards

- Findings are traceable, severity is consistent with the rubric, and inaccessible checks remain visible.
- A clean artefact may receive grade A; the audit never invents debt.

## Anti-Patterns

- Reporting a vague “AI feel”. Fix: cite the exact phrase, line, figure, or formatting pattern.
- Padding a clean audit with invented defects. Fix: allow a grade A result.
- Editing during a read-only audit. Fix: separate diagnosis from authorised remediation.
- Treating an inaccessible citation check as passed. Fix: mark it not assessed.
- Removing useful authored material during cleanup. Fix: record what must be preserved.

## References

- [Anti-slop production guardrail](../anti-ai-slop/SKILL.md)
- [Critical analysis and business logic gate](../../strategy-positioning/critical-analysis-business-logic/SKILL.md)
<!-- dual-compat-end -->

## When this runs

**Cadence: run after EACH proposal section or major iteration.** This is the default mode. Whenever a meaningful unit of work is finished, that is a drafted cover letter, an executive summary, an understanding-of-assignment section, a methodology, a work plan, a financial proposal, or a significant revision, run this audit on what was just produced before moving to the next section. Log the verdict. If the verdict is **F (Blocked)**, do not progress to the next section until the blocking findings are fixed. Treat it like a quality gate that runs at every checkpoint, not a one-time review the night before the deadline.

**Also auto-run on request:** when the user asks to analyse, review, evaluate, audit, critique, score, or de-slop any proposal, Expression of Interest, tender response, cover letter, executive summary, methodology, work plan, team composition, financial proposal, capability statement, or business document, or asks "does this look AI-generated?" or "why does this read off?".

**Also run as the final gate** before assembling or submitting any proposal.

The companion `anti-ai-slop` skill runs continuously while content is written; this audit runs at each checkpoint to catch what slipped through.

## What slop is (the yardstick)

Low-quality content produced in quantity by AI and pushed at people who did not ask for it (Merriam-Webster 2025 Word of the Year, verified). Three diagnostic properties (Kommers et al., arXiv 2601.06060): superficial competence, asymmetric effort, mass producibility. The human tell is absence of intent. In a proposal, slop is text that could be submitted to any client for any assignment. You are measuring how strongly an artefact exhibits these.

## Audit method, layered, cheapest first

### Step 1 — Identify the artefact and load the right checklist
Map the artefact to its proposal type: cover letter, executive summary, understanding of assignment, firm or consultant profile, relevant experience, methodology, team composition, work plan, financial proposal, or a full bid. A full proposal usually spans several. Audit each section.

### Step 2 — Automated gates (machine-checkable). Any hit is hard evidence
Run every applicable check. A hit on a blocking marker (✗) fails the artefact outright.

- 🤖 Focal-word density: delve, tapestry, realm, navigate, underscore, pivotal, intricate, leverage, foster, harness, synergy, embark, robust, vibrant, holistic, seamless, and the rest of the banned list, more than two per 500 words.
- 🤖 Em-dash density above one per paragraph; reflexive rule-of-three; "it is not X, it is Y" repetition; uniform 15 to 25 word sentences (low burstiness).
- 🤖 Transition clichés: "in today's fast-paced world", "let us dive in", "in conclusion", "world-class", "best-in-class", "cutting-edge" as unsupported self-praise.
- 🤖 Mechanical formatting: Title-Case headers everywhere, excessive bold, decorative emoji, leftover tool markup ("oaicite", "contentReference").
- ✗ 🤖 Broken or fabricated citations: dead URLs, invalid DOI or ISBN, fabricated statistics, invented client names, invented court cases or statutes, utm_source parameters copied in.
- French: "plongeons dans", "il est important de noter que", "force est de constater", filler connectors.

### Step 3 — Structural score → 0 to 100 genericness
Combine burstiness, focal-word density, duplication, and template similarity into a single genericness score. Higher means more slop-like. Report the score and its drivers.

### Step 4 — Human-judgement review (the checklist no tool replaces)
- 👁 **Substance:** what does this section assert or decide that required real work? If nothing, it is slop.
- 👁 **Intent and authored voice:** is there a point of view, or is it relentlessly positive and free of any stance?
- 👁 **Specificity:** real named clients, projects, methods, and numbers, or generic placeholders that fit any bid?
- 👁 **Hard parts:** are risks, dependencies, assumptions, and the counter-case handled?
- 👁 **Proposal-specific findings (per section):**
  - *Cover letter and executive summary:* generic value proposition that would fit any firm; inflated superlatives; no named client problem; hollow analogies.
  - *Understanding of assignment:* "we understand" without proof; no reference to the actual Terms of Reference, sector, or constraint.
  - *Relevant experience:* activities listed instead of outcomes; unverifiable or invented client references, figures, or awards.
  - *Methodology and work plan:* no visible logic (evidence → warrant → assumptions → counter-case → implication); frameworks used as decoration; methodology, staffing, timeline, and budget that do not tell one achievable delivery story.
  - *Financial proposal:* round-number filler; fees inconsistent with the staffing schedule and work plan; reimbursables that do not match the method.

Cross-check the reasoning failures with `critical-analysis-business-logic`, which is the complementary gate for evidence, business sense, feasibility, and achievability.

## Scoring and verdict

| Grade | Meaning | Trigger |
|---|---|---|
| **A — Clean** | No blocking hits; genericness low; substance and intent present | submit |
| **B — Minor slop** | A few automated hits, no blockers; some genericness | fix listed items |
| **C — Slopy** | Multiple automated hits or weak substance and intent | rework before submission |
| **F — Blocked** | Any ✗ blocker (fabricated statistic, citation, client, court case, or statute; or no substance at all) | do not submit |

## Output format (the audit report)

```
# AI Slop Audit — <artefact name> — <day-month-year>
Verdict: <A/B/C/F>   Genericness score: <0–100>
Artefact type(s): <...>

## Blocking findings (✗) — must fix
- [marker] <what was found> · evidence: <quote / line / URL> · fix: <concrete action>

## Slop findings (by severity)
- [marker] <finding> · evidence: <...> · fix: <...>

## What is good (so it is not stripped in the fix)
- <substantive, specific, authored elements worth keeping>

## Recommended next step
- <rework / targeted fixes / submit>
```

## Discipline (anti-hallucination, applies to the audit itself)

- Every finding cites concrete evidence from the artefact: a quote, a line, a figure, a URL. No finding without evidence.
- Do not invent a flaw to pad the report. "This section is clean" is a valid and wanted verdict.
- Mark inferences "(inference)"; never present a guess as a measured fact.

## See also

- `anti-ai-slop` — the prevention companion; write proposal content so slop never appears.
- `critical-analysis-business-logic` — the complementary reasoning, business-sense, feasibility, and achievability gate.
- `east-african-english` and `language-standards` — house tone and spelling, applied on top of this skill.
