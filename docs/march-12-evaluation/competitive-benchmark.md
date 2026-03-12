# Competitive Benchmark — What World-Class Firms Do Differently

**Date:** 12 March 2026

---

## Purpose

This document compares the proposal-skills repository against what McKinsey, Bain, BCG, Deloitte, EY, PwC, and other top-tier consulting firms include in their proposals. The goal is not to replicate their scale but to identify the specific elements that make their proposals win — and which of those elements this repository can realistically adopt.

---

## What Top-Tier Firms Get Right

### 1. Every Claim Is Quantified

**What they do:** McKinsey never writes "significant improvement." They write "23% reduction in processing time within 6 months, saving $4.2M annually." Every differentiator, every past project outcome, every projected benefit has a number.

**Where we stand:** The Outcomes Rule in section 05 requires quantified outcomes for project cards. Section 02 mentions "every claim must be specific." But quantification discipline is not enforced across all sections — methodology claims ("our approach is thorough"), firm profile statements ("extensive experience"), and cover letter assertions often lack numbers.

**Gap:** Medium. The principle exists but enforcement is inconsistent.

---

### 2. Named Proprietary Frameworks

**What they do:** Deloitte has "Monitor Deloitte's Strategy Execution Framework." McKinsey has "OrgSolutions." Bain has "Net Promoter System." These named frameworks signal that the firm has codified intellectual property — not just borrowed generic tools.

**Where we stand:** The consulting-frameworks library contains powerful tools (Eight-Bucket System, Done-Done Standard, SCORE), but these are not positioned as Chwezi proprietary frameworks. The proposal-patterns reference mentions proprietary naming as a technique but doesn't provide guidance on creating Chwezi-branded frameworks.

**Gap:** High. This is a differentiation opportunity. Chwezi could name its own frameworks:
- "Chwezi's Dual-Assessment Risk Model" (strategic + implementation risk assessment)
- "The PCTS Constraint Framework" (Performance-Time-Scope-Cost)
- "The Three-Facet Problem Analysis" (Rational-Cognitive-Political)

These already exist in the repository — they just need branding.

---

### 3. Hypothesis-Led Methodology

**What they do:** McKinsey proposals don't say "we will assess the situation." They say "our hypothesis is that the procurement bottleneck stems from three root causes: [X, Y, Z]. Our methodology will test and refine this hypothesis through [specific activities]." This signals that the firm has already started thinking about the problem.

**Where we stand:** Section 06 (methodology) includes hypothesis-driven methodology as a core technique. The consulting-frameworks library supports it. This is one of the repository's strongest areas.

**Gap:** Low. The capability exists. Ensure it is consistently applied.

---

### 4. Storyboarding Before Writing

**What they do:** McKinsey creates a "ghost pack" — a full proposal outline with page titles, key messages per page, and evidence placeholders — before writing a single paragraph. This ensures narrative coherence and prevents section-by-section drafting that loses the thread.

**Where we stand:** The world-class-proposal-patterns reference covers storyboarding and ghost packs (section 14). The brainstorming workflow in CLAUDE.md creates a BRIEF.md that functions as a partial storyboard. But there is no explicit "create the ghost pack first" step in the proposal writing workflow.

**Gap:** Medium. The concept exists in references but is not operationalised in the workflow.

**Remediation:** Add a "Ghost Pack" step between brainstorming and section writing in CLAUDE.md. The ghost pack would be a one-line-per-page outline showing: page title, key message, evidence to include, theme to reinforce.

---

### 5. Buyer Role Awareness

**What they do:** Deloitte trains proposal teams to write for four buyer roles simultaneously: the Economic Buyer (who signs the cheque), the User Buyer (who will work with the consultants daily), the Technical Buyer (who evaluates technical compliance), and the Coach (internal champion). Different sections emphasise different roles.

**Where we stand:** Proposal-strategy-and-persuasion.md section 4 covers the four buyer roles. But no section skill explicitly guides which buyer role to prioritise.

**Gap:** Medium. The knowledge exists in references but is not operationalised in section skills.

**Remediation:** Add a "Primary Buyer Role" note to each section skill:
- Cover letter → Economic Buyer
- Executive summary → Economic Buyer + Coach
- Understanding → Technical Buyer + Coach
- Methodology → Technical Buyer
- Team composition → Technical Buyer + User Buyer
- Financial proposal → Economic Buyer

---

### 6. Theme Architecture

**What they do:** Bain identifies 3–4 "win themes" at the start (e.g., "deep sector expertise," "proven track record in East Africa," "innovative data-driven approach") and weaves them through every section. A reader should absorb the themes subconsciously by the time they reach the financial proposal.

**Where we stand:** Proposal-strategy-and-persuasion.md section 5 covers theme architecture. Section 02 defines four differentiators. But no mechanism connects themes from section 02 to their reinforcement in sections 03–10.

**Gap:** High. Identified as Critical Gap C9 in the gap analysis.

---

### 7. Red Team Review

**What they do:** McKinsey runs a formal "Red Team" review where a separate team reads the proposal as if they were the evaluator — scoring it against the published criteria and identifying weaknesses. Proposals are revised based on Red Team findings before submission.

**Where we stand:** Proposal-strategy-and-persuasion.md section 16 covers the Red Team process. But it is not operationalised as a step in the proposal workflow.

**Gap:** Medium. The concept exists but needs to be embedded as a mandatory step before final compilation.

---

### 8. Sector Depth That Signals Expertise

**What they do:** A PwC proposal for a health systems assessment uses WHO health system building blocks terminology, references the Lancet Commission findings, cites specific country health indicators, and names the relevant national health strategy. This signals "we live and breathe this sector."

**Where we stand:** All 9 industry sector directories are empty.

**Gap:** Critical. Identified as Critical Gap C5 in the gap analysis.

---

### 9. Team Narrative That Tells a Story

**What they do:** Deloitte's team section doesn't just list CVs. It opens with a narrative explaining why this specific team was assembled for this specific assignment — what each person brings that directly addresses a challenge in the ToR. The team section reads as a continuation of the methodology argument.

**Where we stand:** Section 07 covers organograms, role matrices, and CV formats. But it does not guide writing a team narrative that connects team selection to methodology logic.

**Gap:** Medium. The team section is structurally complete but lacks narrative sophistication.

---

### 10. Financial Proposal as Strategic Document

**What they do:** McKinsey's financial proposal is not just a price table. It includes a "value story" — explaining why the investment is justified by expected returns, how the fee structure reflects quality rather than cheapness, and what risks are mitigated by the pricing model. The budget architecture (Chereau's nine parts) positions the price as a strategic choice.

**Where we stand:** Section 10 has the PCTS framework, risk contingency formula, and day rate table. The world-class-proposal-patterns reference covers budget architecture. But the "value story" — the narrative around the price — is not guided.

**Gap:** Medium. Add a "Value Narrative" subsection to section 10 that explains how to justify the price rather than just present it.

---

## What Top-Tier Firms Have That We Should NOT Try to Replicate

Not every Big Four practice is worth adopting. Some depend on scale, brand, or resources that a smaller firm cannot match:

| Practice | Why Not to Replicate |
|----------|---------------------|
| **Massive case study libraries** | Big Four have thousands of past projects. Chwezi should focus on quality over quantity — 10 exceptional project cards beat 100 generic ones. |
| **Global delivery network claims** | Claims like "200 offices in 150 countries" ring hollow for a Kampala-based firm. Instead, position local presence and senior-level attention as advantages. |
| **Celebrity partner endorsements** | McKinsey can name-drop senior partners. Chwezi should instead demonstrate Peter's personal involvement and hands-on approach. |
| **Expensive proposal production** | Big Four spend $50K+ on proposal design, printing, and presentation. Chwezi should focus on content quality — a well-written .docx beats a beautifully designed but shallow proposal. |
| **Lowball pricing to win** | Big Four can afford loss leaders. Chwezi should price at fair value and justify with quality, not compete on price. |

---

## The Chwezi Advantage — What Small Firms Do Better

The competitive benchmark is not one-directional. Small firms have structural advantages that should be amplified in proposals:

| Advantage | How to Leverage |
|-----------|-----------------|
| **Senior-level attention** | "Our Managing Director will personally lead this assignment" — Big Four send junior staff after winning with senior CVs |
| **Decision speed** | "We can mobilise within 5 working days of contract signing" — Big Four need weeks of internal approvals |
| **Local context depth** | "Based in Kampala with 15 years of Uganda market experience" — Big Four fly in consultants who leave |
| **Cost efficiency** | "Our lean structure means 90% of your budget goes to delivery, not overhead" — Big Four have expensive cost structures |
| **Relationship continuity** | "The team you meet at inception is the team that delivers" — Big Four rotate staff across projects |
| **Flexibility** | "We adapt our approach based on what we find, not what our internal methodology manual prescribes" |

These advantages are partially captured in the profiles (peter-bamuhigire.md and chwezi-core-systems.md) but should be more explicitly integrated into proposal section skills.

---

## Summary: Competitive Position

| Dimension | Repository Status | vs Big Four |
|-----------|-------------------|-------------|
| Persuasion and strategy foundations | Excellent | Competitive |
| Analytical frameworks | Excellent | Competitive |
| Problem structuring | World-class | Competitive or better |
| Methodology design | Strong | Competitive |
| Financial proposal structure | Strong | Competitive |
| Project management and risk | Good | Slightly below |
| Domain skill depth (change, M&E, GESI, etc.) | Weak | Significantly below |
| Sector-specific knowledge | Missing | Significantly below |
| Theme threading and narrative coherence | Conceptual only | Below |
| Worked examples and calibration | Missing | Below |
| Evaluation scoring optimisation | Partial | Below |
| Procurement framework coverage | Partial (WB + UNDP only) | Below |

**Bottom line:** The repository's strategic and analytical foundations are genuinely competitive with the Big Four. The gap is in domain depth, sector specificity, and workflow operationalisation. Phase 1 of the remediation plan closes the most impactful gaps.
