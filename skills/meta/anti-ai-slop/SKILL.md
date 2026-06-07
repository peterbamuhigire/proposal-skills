---
name: anti-ai-slop
description: Non-negotiable real-time guardrail. Apply while writing EVERY proposal section, cover letter, executive summary, Expression of Interest, methodology, procurement response, or financial proposal, so the output cannot be recognised as AI slop. Carries the verified definition, the seven universal slop markers each paired with an avoidance rule, the merged banned-vocabulary list, and a ship-gate checklist. Load first; it overrides stylistic preferences.
---

# Anti AI Slop
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

The guardrail that governs production. You write, structure, and price proposal content so slop never appears in the first place. Detection lives in the companion `ai-slop-audit` skill, and the reasoning gate lives in `critical-analysis-business-logic`.

## Real-time application (this is a LIVE constraint, not only a final gate)

Apply these rules continuously, as you write, to every sentence, table, claim, and section the moment it is drafted, not only in one pass at the end. The moment you reach for a banned word, a generic value statement, an unverified figure, or a template default, stop and correct it in place. The ship-gate checklist at the end is the final confirmation, not the first time these rules are consulted. If you are mid-draft and notice slop accumulating in an executive summary or a methodology, fix it then. Do not defer to a cleanup pass before submission.

## What AI slop is (so you know what you are preventing)

AI slop is low-quality content produced in quantity by generative AI and pushed at people who did not ask for it (Merriam-Webster 2025 Word of the Year, verified). Its three diagnostic properties (Kommers et al., "Why Slop Matters", arXiv 2601.06060, verified):

1. Superficial competence. Looks fine on the surface, no substance underneath.
2. Asymmetric effort. Cheap to produce, costly for an evaluator to read, score, and trust.
3. Mass producibility. Generated at volume.

The human tell named in every domain studied is absence of intent: the sense that no one meant anything by it. In a proposal this reads as a document that could have been submitted to any client for any assignment. Your task is to re-internalise effort, through specificity, verification, and authored choices, before the proposal reaches an evaluator.

## The seven universal guardrails (apply to EVERY section)

| # | Marker to prevent | Avoidance rule you MUST follow |
|---|---|---|
| **U1** | Genericness and averaging | Every section carries at least one concrete, named, assignment-specific element (a real past project, a named client, a number, a named method, a decision) that a generic template could not produce. Forbid boilerplate value statements. |
| **U2** | Superficial competence | Enforce a substance floor: include a claim, a named experience, a number, or a decision the section could not exist without. If you cannot, the section is filler. Cut it or replace it. |
| **U3** | Confident wrongness and hallucination | Verify every statistic, citation, quote, named client, court case, statute, and certification before you write it. Cite at the point of claim. Flag uncertainty rather than inventing. |
| **U4** | Volume over substance | Prefer one substantive paragraph over three hollow ones. Do not pad to fill a page limit. |
| **U5** | Absence of authored voice and intent | State a point of view, a rationale, or a named decision. Ban relentless positivity and sycophancy. Allow honest trade-offs, constraints, and assumptions. |
| **U6** | Skipping the hard parts | Cover risks, dependencies, edge cases, and the counter-case, not only the winning narrative. An evaluator trusts a proposal that names what could go wrong. |
| **U7** | Mechanical uniformity | Vary sentence length and structure. Break the template. No rule-of-three reflex, no "it is not X, it is Y" formula, no em-dash flood. |

## Banned and high-risk vocabulary (the lexical tells)

These words and constructions are statistically over-produced by language models (FSU / COLING-2025; PubMed "delve" +400%). Do not use them as default register. A word here is allowed only when it is the genuinely precise term, never as filler. This list merges the engine's existing ban with the canonical slop lexicon.

- **Engine-banned words (already enforced here):** delve, tapestry, landscape (as metaphor), navigate (as metaphor), leverage, foster, realm, harness, synergy, embark, robust, vibrant, holistic, seamless.
- **Additional banned words:** intricate, commendable, meticulous, pivotal, underscore, testament, resonate, elevate, paramount, unwavering, multifaceted.
- **Phrases:** "in today's fast-paced world", "in the ever-evolving landscape of", "it is important to note that", "it is worth mentioning", "let us dive in", "at the end of the day", "in conclusion", "studies show" without a named study, "world-class" and "cutting-edge" as unsupported self-praise, "we are passionate about", "best-in-class".
- **Constructions:** the "it is not just X, it is Y" antithesis; reflexive rule-of-three lists; the em-dash used to manufacture drama; triplet adjectives such as "robust, scalable, and reliable".
- **French equivalents (for Francophone procurement):** "plongeons dans", "il est important de noter que", "force est de constater", "dans un monde en constante évolution", "par ailleurs / de plus / en outre" as filler connectors, "au cœur de", "pierre angulaire".

## Drop-in guardrail block (inherit in dependent skills)

```
ANTI-SLOP GUARDRAIL (inherit in every proposal section):
1. SPECIFICITY FLOOR — every section carries at least one concrete, named,
   assignment-specific element. No boilerplate value statements, no placeholder copy.
2. VERIFY-BEFORE-WRITE — no statistic, citation, named client, court case, statute,
   or certification appears unverified; cite at point of claim; flag uncertainty.
3. AUTHORED VOICE — state a point of view and a rationale; no relentless positivity,
   no sycophancy; allow honest trade-offs and assumptions.
4. COVER THE HARD PARTS — risks, dependencies, edge cases, and the counter-case.
5. BREAK THE TEMPLATE — vary rhythm and structure; forbid the banned-vocabulary
   list above and generic procurement boilerplate.
```

## Proposal-specific avoidance (apply to bid content)

- **Cover letters and executive summaries:** no generic value proposition that would fit any firm or any client; name the client problem and the proposer's specific fit; one stated point of view; vary sentence length, mixing short clauses with fuller 25 to 40 word sentences; no more than one em-dash per paragraph.
- **Understanding of the assignment:** prove understanding with named context, not the phrase "we understand". Reference the actual Terms of Reference, the sector, and the constraint.
- **Relevant experience:** every project card states what was achieved, not only what was done. Outcomes, not activities. No invented client names, figures, or references.
- **Methodology and work plan:** show visible logic. Every high-stakes claim carries evidence, warrant, assumptions, counter-case, and practical implication. Methodology, staffing, timeline, risk controls, monitoring and evaluation, and budget must tell one mutually achievable delivery story, not five well-written but disconnected ones.
- **Inflated superlatives and hollow analogies:** strike "world-class", "revolutionary", "game-changing", and decorative metaphors that carry no information. Replace each with a verifiable specific.
- **Unverifiable claims:** any market statistic, certification, ranking, or "studies show" line needs a named, real source or it is removed.
- **Financial proposals:** day rates, fee breakdowns, and reimbursables must be internally consistent with the staffing schedule and the work plan. No round-number filler.

## Ship gate (run before delivering ANY section)

- [ ] Every section has at least one concrete, named, assignment-specific element (U1 and U2).
- [ ] Every statistic, quote, citation, named client, court case, statute, and certification is verified (U3).
- [ ] No banned vocabulary used as filler; the section was scanned against the list above.
- [ ] The section states a point of view and a rationale; no sycophancy (U5).
- [ ] Risks, dependencies, and the counter-case are addressed (U6).
- [ ] Sentence length and structure are varied; no rule-of-three reflex, no antithesis formula, no em-dash flood (U7).
- [ ] Outcomes-not-activities rule applied to experience; visible-logic chain applied to high-stakes claims.
- [ ] British English, East African professional tone, and day-month-year dates throughout.
- [ ] When in doubt, run the `ai-slop-audit` skill on the draft.

If any box is unticked, the section is not ready to submit.

## See also

- `ai-slop-audit` — the detection and audit companion; run it after each section and as the final gate.
- `critical-analysis-business-logic` — the complementary reasoning, business-sense, feasibility, and achievability gate.
- `east-african-english` and `language-standards` — house tone and spelling, applied on top of this skill.
