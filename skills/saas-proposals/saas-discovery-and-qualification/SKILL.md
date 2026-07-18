---
name: saas-discovery-and-qualification
description: Use when a SaaS bid needs buyer qualification through ICP fit, critical event, pain chain, role-level impact, decision process, and no-bid signals; use AI-on-SaaS discovery when AI data, model, or hallucination questions apply.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Discovery and Qualification
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- A SaaS bid needs ICP articulation, Critical Event naming, pain-chain construction, impact quantification per role, and decision-process mapping.
- The buyer is enterprise, regulated-industry, or premium-priced, and a Bain/EY/McKinsey-grade Understanding of the Assignment section is expected.
- The ToR is incomplete and the agency must surface buyer logic through declared assumptions and clarification requests.
- The agency must produce an evaluator-ready proposal that demonstrates qualified, defensible, buyer-aware thinking.

## Do Not Use When

- The engagement is not SaaS-related (use `sales-discovery-and-objection-handling/` for general discovery).
- The proposal is purely a price response with no buyer-logic content.

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| ToR, RFP, advert, or proposal brief. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| Any prior discovery notes, sponsor conversations, or sales-team intelligence. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The proposer profile (loaded from `profiles/SKILL.md`). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The vertical (financial services, insurance, public sector, healthcare, education, etc.). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Identify the ICP the proposed approach is tuned for, in one sentence.
2. Name the Critical Event that makes the engagement urgent now (regulatory deadline, system end-of-life, audit finding, M&A integration, growth ceiling, competitor move, customer-experience failure, board mandate).
3. Construct the pain chain: surface → operational → financial → strategic.
4. Quantify Impact per Role for the buyer's executive sponsor, finance owner, operations owner, technology owner, security owner, frontline user, customer/beneficiary, and procurement owner.
5. Map the Decision Process: consensus or hierarchy; named individuals who can say yes; named individuals who can say no; the path from shortlist to signature with named owners and target dates.
6. Translate the decision-process map into the win-plan annex (sponsor / champion / blocker map) — kept internal unless the buyer asks for it.
7. Run the MEDDPICC / CHAMP qualification gate before submission.
8. Convert findings into:
   - Understanding of the Assignment section (pain chain, ICP, Critical Event, value at stake).
   - Executive Summary leadership (one-line pain chain + Critical Event + measurable value).
   - Methodology phase opening paragraphs (P-I-P "P" component for each phase).
   - Win-plan annex (sponsor, champion, blocker, decision process, path to award).


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Pain-chain links must each have at least one piece of evidence (analytics, audit, support log, interview, observation, or named comparable).
- Impact figures must have a baseline and a source; "improves significantly" without numbers is rejected.
- Decision-process map names individuals where the agency knows them; states the gap explicitly where it does not.
- Never name MEDDPICC, CHAMP, or Command of Message in the client-facing proposal — these are internal qualification mnemonics.
- Premium SaaS proposals open with the buyer's pain, not the agency's biography.

## Anti-Patterns

- A proposal that opens with the agency's history rather than the buyer's pain. **Fix:** Open with the buyer's critical event, diagnosed pain, affected roles, consequence, and desired outcome before agency credentials.
- Pain-chain that stops at surface symptoms (slow report) without going through operational, financial, and strategic links. **Fix:** Trace each symptom through workflow cause, operational effect, financial consequence, strategic risk, and measurable baseline.
- Impact stated only for the technology owner — premium buyers want CFO, COO, CISO, and frontline impact. **Fix:** Map impact for sponsor, economic buyer, operational owner, security or compliance owner, administrators, and frontline users.
- Decision-process described as "we will work with stakeholders" rather than naming individuals and gates. **Fix:** Name decision participants, criteria, evidence, procurement steps, approvals, dates, and the consequence of delay.
- Listing every pain in the market rather than the diagnosed pain for this buyer. **Fix:** Prioritise only buyer-validated pains by severity, urgency, evidence, strategic fit, and willingness to act.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Pain-chain table for the Understanding of the Assignment section. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Impact-per-role table for the Executive Summary. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Decision-process map for the win-plan annex. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Critical Event statement. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Clarification requests where discovery gaps remain. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Inputs to the Mutual Action Plan, the business case, and the win-themes selection. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Input-and-assumption record | Proposal lead and reviewer | Every load-bearing claim maps to a source, approved assumption, or explicit gap. |
| Decision and review record | Buyer owner and delivery lead | The selected option, rationale, owner, stop condition, and approval status are visible. |
| Section acceptance check | Evaluator-readiness reviewer | Each output meets its stated acceptance condition and unresolved checks are not presented as passed. |

## Capability and Permission Boundaries

This skill may read supplied tender, discovery, architecture, commercial, security, and operating evidence and draft proposal artefacts within the authorised workspace. It must not publish, send, certify compliance, accept contractual terms, change production systems, spend funds, or disclose confidential evidence without explicit authority. Review and analysis remain read-only by default.

## Degraded Mode

If files, current legal or technical evidence, calculation tools, network access, or reviewers are unavailable, produce the narrowest useful qualified draft. Label assumptions and checks as **not assessed**, omit unsupported assurances or figures, and state the exact evidence and owner needed to complete the work. An unavailable check never becomes a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Critical unknown | Pause solution claims and issue a targeted discovery question or no-bid condition | Proposal built on untested buyer or operating assumptions |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

Discovery confirms a month-end reporting delay but no measured baseline. Record the affected finance and operations roles, ask for the last three close-cycle records, and withhold the time-saving claim until the evidence owner supplies them.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/saas-discovery-question-bank.md](../../profiles-sectors/references/saas-discovery-question-bank.md) — pain chain, impact, decision process, critical event.
- [../references/meddic-and-command-of-message-for-saas.md](../../profiles-sectors/references/meddic-and-command-of-message-for-saas.md) — qualification gate and Six-Lens Value Claim.
- [../references/saas-mutual-action-plan-template.md](../../profiles-sectors/references/saas-mutual-action-plan-template.md) — output that incorporates decision-process map.
- [../references/saas-business-case-and-roi-template.md](../../profiles-sectors/references/saas-business-case-and-roi-template.md) — value-at-stake quantification.
- [../references/saas-win-themes-and-discriminators.md](../../profiles-sectors/references/saas-win-themes-and-discriminators.md) — converting discovery into win themes.
- [../sales-discovery-and-objection-handling/SKILL.md](../../strategy-positioning/sales-discovery-and-objection-handling/SKILL.md) — broader discovery and objection handling.
- [../premium-client-proposal-strategy/SKILL.md](../../strategy-positioning/premium-client-proposal-strategy/SKILL.md) — executive and premium buyer positioning.
- [../03-understanding-of-assignment/SKILL.md](../../pipeline/03-understanding-of-assignment/SKILL.md) — section discipline.
