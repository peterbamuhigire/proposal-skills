---
name: ppda-uganda
description: Use when a Uganda public procurement follows PPDA rules for consultancy, supplies, works, or non-consultancy services; use donor-framework skills when the solicitation explicitly makes donor rules controlling.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Uganda PPDA Procurement Framework
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When
- Use this skill when the solicitation follows Uganda PPDA procurement rules.
- Load it before drafting when you need form, scoring, threshold, or compliance guidance.

## Do Not Use When
- The task only needs sector-domain framing without procurement mechanics.
- A different procurement framework clearly applies.

## Required Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---|---|
| The solicitation package, especially instructions, forms, and evaluation criteria. | Buyer solicitation, ToR, or approved brief | Required | Stop the affected claim, request or verify the input, and label the resulting gap. |
| Any known selection method and technical threshold. | Buyer, verified sector source, or discovery | Required | Stop the affected claim, request or verify the input, and label the resulting gap. |
| The target proposal sections that must comply with the framework. | Buyer, verified sector source, or discovery | Conditional | Stop the affected claim, request or verify the input, and label the resulting gap. |

## Workflow

1. Confirm that PPDA procurement applies from explicit cues in the solicitation.
2. Read this skill and the local references to understand forms, scoring, procedures, and constraints.
3. Map those requirements into the numbered proposal section skills before drafting.
4. Draft to maximize technical quality without creating compliance risk.
5. Check the final output against thresholds, form placement, and submission rules.

**Stop condition:** Stop when proposer identity, controlling framework, mandatory form, sector fit, current rule, or load-bearing evidence remains unresolved.

**Recovery:** Record the gap and owner, seek clarification or current evidence, and return only the separable proposal content that remains supportable.

## Quality Standards
- Treat PPDA instructions as hard constraints, not optional style guidance.
- Keep terminology, form names, and evaluation assumptions aligned to the actual solicitation.
- Optimize for evaluator behavior where the framework supports it.

## Anti-Patterns

- Do not rely on generic public-procurement assumptions when the PPDA materials give exact instructions.
- Do not ignore eligibility checks, pass/fail gates, or form requirements.
- Do not mix PPDA assumptions with World Bank, AfDB, or UN rules.
- Treating a neighbouring sector or framework as interchangeable. **Fix:** identify the controlling rule and primary outcome.
- Adding terminology without changing a delivery choice. **Fix:** link each term to method, risk, output, or evaluation criterion.
- Presenting an unverified current rule or statistic as settled. **Fix:** cite and date the source or mark it not assessed.
- Ignoring a missing mandatory input. **Fix:** stop the affected claim and assign an evidence owner.
- Letting sector or identity framing contradict methodology, staffing, schedule, or price. **Fix:** reconcile all affected sections before release.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| A PPDA-compliant drafting and scoring approach for the relevant proposal sections. | Proposal lead, section writer, and evaluator-readiness reviewer | Applied consistently, traceable to the selected source, and free of unsupported identity, framework, or sector claims. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Routing and source record | Proposal lead and reviewer | Selected identity, framework, sector, source, date, and material gaps are recorded. |
| Decision record | Section writer and delivery lead | Each material choice has rationale, owner, evidence, and a review or stop condition. |
| Conformance check | Release reviewer | Mandatory forms, identity rules, sector logic, and unresolved checks are explicitly assessed. |

## Capability Contract

This skill may read supplied profiles, solicitations, ToRs, approved references, and proposal drafts and may prepare routing guidance or draft content within the authorised workspace. Review is read-only by default. It must not invent credentials, certify compliance, submit a bid, accept terms, publish, disclose confidential information, or change source records without explicit authority.

## Degraded Mode

If the solicitation, profile, current procurement source, sector evidence, network, or reviewer is unavailable, provide the narrowest useful qualified routing or draft. Mark the missing check **not assessed**, omit unsupported credentials, thresholds, dates, or compliance claims, and identify the evidence owner. An unassessed requirement is never a pass.

## Decision Rules

| Decision | Action | Failure/risk avoided |
|---|---|---|
| PPDA evaluation route | Use the solicitation's method, mandatory documents, evaluation stages, forms, and approvals; flag any ambiguity for clarification. | Administrative rejection or incorrect scoring response |
| Envelope structure, channel and securities | Take each from the BDS; use the submission table to spot a BDS that conflicts with the Regulations and raise it as a clarification. | Wrong envelope structure, a missing or unsuitable security, or a missed electronic submission |
| Conflicting solicitation and background guidance | Follow the solicitation while recording the conflict for formal clarification. | Non-responsive interpretation |
| Missing mandatory evidence | Stop the affected claim or form, record the owner and deadline, and continue only with independent supported content. | Fabricated evidence or silent omission |
| Submission, certification, or contractual commitment | Obtain explicit authority and preserve approval evidence before acting. | Unauthorised external commitment |

## Worked Example

A solicitation requires **ppda evaluation route**, but one controlling input is missing. The proposal team applies this rule: Use the solicitation's method, mandatory documents, evaluation stages, forms, and approvals; flag any ambiguity for clarification. It records the gap and owner, withholds the affected assurance, and proceeds only with content that can be verified. This avoids **administrative rejection or incorrect scoring response**.

## References

- [Proposal skill router](../../../SKILL.md) — orchestration, profile, reasoning, and release gates.
- [Weighted page budget and compliance matrix](../../../pipeline/06-methodology/references/weighted-page-budget-and-compliance-matrix.md) — use when the solicitation caps pages or weights its criteria, and to build the Bid Data Sheet or Data Sheet compliance matrix.
<!-- dual-compat-end -->
- Local `references/` files for the PPDA Act, forms, procedures, and evaluation mechanics.
- [../SKILL.md](../SKILL.md) to combine framework and sector context.

This skill provides the evaluation methodology, scoring rules, form structures, and procedural requirements that govern all public procurement in Uganda under the PPDA Act (Cap 205). Read this before writing any section of a Uganda government-funded proposal.

## When to Read This Skill

- The procurement is managed by a Ugandan Procuring and Disposing Entity (PDE)
- The RFP/bidding document references the PPDA Act, 2003 or PPDA Regulations
- The assignment uses Technical Compliance, Quality and Cost Based, Quality Based, Least Cost, or Fixed Budget selection
- You need to understand how PPDA evaluators score to maximise points
- The proposal must comply with PPDA standard forms and procedures

---

## Selection Methods for Consultancy Services

| Method | How It Works | Implication for Proposal |
|--------|-------------|-------------------------|
| **QCBS** | Technical scored first (merit points, max 100). Financial opened only for firms passing minimum qualifying mark. Combined weighted score determines winner. | Maximise technical quality. Price matters but typically less than quality. |
| **QBS** | Only highest technical scorer's financial proposal opened. No financial weighting. | Quality is everything. Price negotiated after selection. |
| **LCS** | All firms above technical minimum ranked by lowest cost. | Meet the technical threshold comfortably, then compete aggressively on price. |
| **FBS** | Proposals exceeding budget rejected. Highest technical score among those within budget wins. | Maximise technical score while staying within the stated budget. |
| **Single/Sole Source** | Single proposal evaluated against criteria. | Justification and quality of technical proposal are critical. |

---

## Evaluation Methods for Supplies, Works, and Non-Consultancy Services

| Method | How It Works | Form Used |
|--------|-------------|-----------|
| **Technical Compliance** | Pass/fail eligibility, then R/NR technical responsiveness, then lowest price wins | Form 14 |
| **Quality and Cost Based** | Pass/fail eligibility, merit-point technical scoring with minimum qualifying mark, then combined weighted tech + financial score | Form 16 (technical) + Form 15 (combined) |

---

## Bid Submission: Method, Channel and Securities

The bidding document states the submission method, the delivery channel and any security (Rules and Methods Regulations 2023, regs 63(1), 66(1)). Use the table to check that the Bid Data Sheet (BDS) is plausible and to prepare early; the BDS controls. Read on 31 October 2026 from the Regulations hosted on the PPDA website.

### Which envelope structure

| Procurement and evaluation method | Submission method in the Regulations | What to build |
|---|---|---|
| Consultancy: QCBS, LCS or FBS | One-stage, two-envelope (Consultancy Services Regulations 2023, reg 48(2)(a)) | An outer sealed envelope holding separately sealed envelopes marked "technical proposal" and "financial proposal"; no price in the technical envelope. The financial envelope stays unopened until a later public session, after the Contracts Committee approves the technical evaluation report (Consultancy Services Regulations regs 62(1), 65 and 66) |
| Consultancy: QBS | Two-envelope or two-stage, as the request for proposals states (reg 48(2)(a) and (c)) | Follow the request for proposals |
| Consultancy: direct procurement or consultants' qualifications selection | One-stage, single envelope (reg 48(2)(b)) | One sealed envelope |
| Supplies, works or non-consultancy services under the technical compliance method | One-stage, single envelope (Rules and Methods Regulations 2023, regs 66(2) and 66(6)(a)) | One sealed envelope holding the technical response and the price schedule |
| Supplies, works or non-consultancy services where the detailed technical evaluation is done without reference to price | One-stage, two-envelope (reg 66(6)(b)) | Envelopes marked "TECHNICAL" and "FINANCIAL", opened at separate bid openings |
| Design and build, textbooks and information technology systems | The buyer may choose one-stage two-envelope or two-stage (reg 66(4)) | Two-stage: a technical bid first, then a revised technical bid and a financial bid. Check which the BDS names before assembling anything |

An ICT bid is therefore not automatically single-envelope or two-envelope. Do not carry the consultancy two-envelope pattern into a supplies or non-consultancy bid, and do not put the price in a separate envelope unless the BDS says so. The BDS also fixes the outer-envelope markings (Regulations reg 66(7) and (8): plain, securely sealed outer envelope; procurement reference; bidder name; "TECHNICAL" or "FINANCIAL" where two envelopes apply; "WITHDRAWAL", "MODIFICATION" or "REPLACEMENT"; "NOT TO BE OPENED BEFORE THE DATE AND TIME OF THE BID OPENING"). An unmarked or unsealed bid leaves the entity not responsible for early opening or misplacement (reg 66(9)).

### Channel

Regulation 68(2) allows delivery "in person or electronically", through Procurement and Disposal Unit staff who acknowledge receipt or "by use of a bid box or government electronic system". Take the channel from the BDS. PPDA's home page lists a press statement dated 5 June 2026 titled "Uganda to Roll Out E-GP to all Entities on 1st July 2026"; its text could not be retrieved on 31 October 2026, so which entities require e-GP submission is **not assessed**. If the BDS names e-GP, register as a supplier on the e-GP portal before the deadline, rehearse the upload, and keep the system's submission receipt. If it names a physical bid, keep the delivery acknowledgement (a courier loss is the bidder's risk, reg 68(3)).

### Bid security, securing declaration and performance security

| Instrument | What the Regulations say | Bidder action |
|---|---|---|
| Bid security | The bidding document states any requirement; PPDA format; issuer as the PPDA guidelines allow; valid at least 28 days after the bid expires (reg 63(1), (4), (5)) | Read the BDS amount, form and validity. Order the instrument early; extend it if the BDS extends bid validity |
| Bid securing declaration | Required where restricted domestic bidding or quotation is used (reg 63(9)). For other methods the bidding document decides. A breach is reported to the Authority, which may suspend the bidder (reg 63(10) and (11)). For consultancy the entity "may require" a proposal securing declaration (Consultancy Regulations reg 47) | Sign only if the BDS requires it and the signatory can honour it |
| Performance security or performance securing declaration | The bidding documents state which is required; a bank guarantee must be acceptable to the Bank of Uganda and an insurance bond to the Insurance Regulatory Authority (Contracts Regulations 2023, reg 11) | Do not assume a declaration will be accepted in place of a guarantee |
| Advance payment | Not above 30% of the contract price without the approval of the Secretary to the Treasury, and an advance payment security is required (Contracts Regulations reg 43) | Price and structure any advance within the BDS terms |

The PPDA performance securing declaration form records a three-year suspension on default; the Act leaves the suspension period to the Authority (section 128).

---

## Three-Stage Evaluation Process

### Stage 1: Preliminary Examination (Pass/Fail)

Every bid/proposal is checked for:
- **Eligibility Criteria** — as per bidding document (C/NC per criterion)
- **Administrative Compliance Criteria** — as per bidding document (C/NC per criterion)

**Any "NC" on any criterion eliminates the bid entirely.** There is no recovery from a preliminary examination failure.

**What to ensure:**
- All eligibility documents present and valid
- Correct format, signed, and delivered on time through the channel and in the envelope structure the BDS names (see "Bid Submission" above)
- Any bid security or bid securing declaration the BDS requires, in the form and for the validity it states
- Every administrative requirement in the bidding document addressed
- Beneficial ownership declaration form completed

### Stage 2: Detailed Technical Evaluation (Merit Points or R/NR)

**For Technical Compliance method (Form 14):** Each bid assessed as Responsive (R) or Non-Responsive (NR) against the technical specification. Non-responsive bids eliminated.

**For QCBS method (Forms 16, 24):** Merit point system with:
- Up to 5 main criteria (A through E), each with sub-criteria
- Maximum total score: **100**
- **Minimum qualifying mark** stated in invitation — proposals below this are eliminated regardless of price
- Multiple evaluators score independently; the **average** is used
- Strengths and weaknesses of each proposal are formally documented
- Large differences between evaluators' scores must be justified

### Stage 3: Financial Comparison

**For Technical Compliance (Form 14):**
- Lowest price among eligible, compliant, substantially responsive bids wins
- Corrections for arithmetic errors, discounts, adjustments, currency conversion, margin of preference

**For QCBS (Forms 15, 26):**
- Lowest evaluated price receives a financial score of **100**
- All others scored: `(Lowest price / Your price) x 100 = Financial Score`
- Combined: `Total Score = (Tech Score x Tech Weight%) + (Financial Score x Financial Weight%)`
- Highest total score ranked first

---

## Financial Scoring Formula (QCBS)

```
Financial Score = (Lowest Evaluated Price / Your Evaluated Price) x 100

Total Score = (Technical Score x Technical Weight%) + (Financial Score x Financial Weight%)
```

**Example at 80/20 split:**
- Firm A: Tech 85, Price lowest → Financial 100 → Total = (85 x 0.8) + (100 x 0.2) = 88.0
- Firm B: Tech 90, Price 20% higher → Financial 83.3 → Total = (90 x 0.8) + (83.3 x 0.2) = 88.7
- Firm B wins despite higher price, because technical quality overcame the price difference

---

## Post-Qualification (where required)

The best evaluated bidder may be assessed against qualification criteria stated in the bidding document to confirm capacity and resources to execute the procurement. Outcome: qualified or not qualified.

---

## Standard Procurement Timeline (Quotation Method)

| Activity | Timeline |
|----------|----------|
| Issue of Request for Quotations | As planned |
| Bid closing date | As planned |
| Evaluation process | Within **10 working days** from bid closing |
| Display of best evaluated bidder notice | Within **5 working days** from CC award |
| Contract signature | After at least **10 working days** from display of NOBEB + Attorney General's approval |

---

## Contract Management (Form 49)

After award, a Contract Management Plan is prepared covering:

**For Consultancy Services:**
- Contract duration, start date, completion date
- Deliverables table with expected dates
- Payment schedule (percentage-based, lump sum, or time-based)
- Linked to specific deliverables

**For Supplies:**
- Deliverables, guarantees (performance + advance payment), inspection, installation, warranty
- Stage payment certificates tracked

**For Works:**
- Guarantees, interim payments, retentions, defects liability period, performance certificate
- Taking over certificate, extension of time, liquidated damages

---

## Performance Security

The bidding documents state whether the successful provider must give a performance security (a bank guarantee acceptable to the Bank of Uganda or an insurance bond acceptable to the Insurance Regulatory Authority) or a performance securing declaration (Contracts Regulations 2023, reg 11). The declaration form, where used:
- Records the provider's acceptance that failure to perform or a default-triggered termination leads to suspension from government procurement; the PPDA form text says three years, while the Act leaves the period to the Authority (section 128)
- Stays valid until completion of all obligations and the defects liability period
- Is signed by an authorised representative of the provider

---

## Negotiations (Form 45)

When negotiations are required, the PDE prepares a Negotiations Plan with:
- Issues for negotiation
- Objectives (what the entity aims to achieve)
- Negotiation parameters (acceptable ranges, limits, walk-away points)

Negotiations team is named with positions and departments; Chairperson identified.

---

## ESHS Requirements (Quotation Method)

All bidding documents must include Environmental, Social, Health and Safety requirements, evaluated on a **pass/fail** basis:
- Sustainable procurement criteria (energy saving, ISO 14001, marginalised groups support)
- H&S competence (policies, accident records, training, certifications)
- Code of Conduct (signed by each worker) covering GBV/SEA prevention, child protection, non-discrimination, community engagement

---

## Reference Files

Load these references for detailed procedural requirements:

| Reference | Content |
|-----------|---------|
| `references/ppda-evaluation-forms-and-procedures.md` | Complete content of Forms 14, 15, 16, 24, 26, 45, 49, Performance Securing Declaration, and User Guide for Quotation Method — all scoring criteria, table structures, process steps, and bidder strategy notes |
| `references/ppda-act-and-regulatory-framework.md` | PPDA Act (Cap. 205) legal framework — institutional structures (5 PDE bodies), 9 procurement methods, preference and reservation schemes (7% for Ugandan consultants), contract types, evaluation rules, bidding process, negotiations, administrative-review/complaints mechanism (two tiers since the 2021 Amendment: Accounting Officer, then PPDA Appeals Tribunal), suspension of providers, offences and penalties, conflict of interest rules, compliance audit requirements, practical tips for consulting firms |
| `references/local-government-procurement.md` | Local-government procurement — Accounting Officer = CAO / Town Clerk; LG Contracts Committee (no lawyer requirement); the Commitment Control System (no LPO/contract without an approved commitment requisition and an uncommitted balance in the quarter's limit); vote control; contract certificates and LPOs paid by crossed cheque; internal audit confirming value for money; no councillor signs council financial documents; how local-government procurement now sits under the consolidated PPDA Regulations 2023 (the former LG (PPDA) Regulations 2006 were revoked, 5 Feb 2024) while the LG (Financial and Accounting) Regulations 2007 govern the financial-control interface |
| `references/ngo-and-donor-procurement.md` | NGO/CSO and donor-funded procurement — NGOs are not bound by PPDA; the common pattern (≥3 quotations on a bid-analysis form above an org-set threshold, a Procurement Committee that is not the end user, requester cannot approve or pay, lowest responsive bid with documented exception); the Reasonable/Allocable/Allowable test and unallowable-cost list; records retention; how donor rules (World Bank, USAID ADS, EU/GIZ, AfDB, UN) layer on top with the stricter rule winning |
| `references/contract-management-and-payment-linkage.md` | Contract-management and payment linkage for Form 49 — milestone-based payment schedules tied to certified deliverables, retention, performance security and advance-payment guarantees (30% advance ceiling), and funds-flow reconciliation (delivered = certified = committed = paid) against the quarter's commitment limit |
