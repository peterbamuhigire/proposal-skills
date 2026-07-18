# NGO / CSO and Donor-Funded Procurement

Parent skill: [Uganda PPDA Procurement Framework](../SKILL.md).

Reference material for the ppda-uganda sector skill. Covers procurement by NGOs, CSOs, faith-based and member-based organisations, and procurement under donor fiduciary rules. Use when the buyer is **not** a public PDE bound by the PPDA Act — that is, an NGO/CSO buyer or a donor-funded grant — so the PPDA mechanics do not apply but a different fiduciary discipline does.

Sources: observed Ugandan NGO finance-and-accounting manuals (illustrative sector practice, not statute); donor fiduciary frameworks — World Bank Procurement Regulations for IPF Borrowers, USAID ADS (notably ADS 302/303 and the cost principles in 2 CFR 200), EU/GIZ grant and procurement rules (PRAG-style), AfDB and UN/UNDP procurement rules.

**Status note:** NGOs/CSOs are **not** bound by the PPDA Act. Their procurement discipline comes from (a) their own board-approved manual and (b) the fiduciary rules of whichever donor funds the activity. The thresholds, floats, and committee tiers below are **organisational-policy patterns and benchmarks**, not legal mandates — confirm each against the client's board-approved manual and the specific grant agreement. Do not assert any figure here as law.

---

## 1. The common NGO procurement pattern

Most Ugandan NGO manuals share a recognisable shape:

1. **Threshold-triggered competition.** Below an organisation-set value, obtain supplier pricing and raise an LPO. **At or above the threshold, obtain at least three quotations** and compare them on a **bid-analysis (comparative-bid) form**. (The trigger is entity-set; manuals reviewed used roughly UGX 0.5–1.0M — treat as a benchmark, not a rule.)
2. **A Procurement Committee — not the end user — evaluates and signs.** The committee that scores the bids and signs the contract is separate from the requester. The **requester cannot approve or pay**, and the procurer cannot also keep the inventory.
3. **Lowest responsive bid is the default.** The lowest bid that meets the specification wins unless a documented exception (best value / total cost of ownership / sole technically responsive supplier) is recorded in the purchase file.
4. **Full record retention.** Keep the requisition, solicitation, the three quotations, the bid-analysis form, evaluation minutes, the award, the contract, and correspondence — the donor audit trail.

---

## 2. Segregation of duties (the control chain)

NGO procurement runs as a control chain in which no person occupies two adjacent roles and no one approves or signs in their own favour:

`request → check → approve → disburse → prepare accountability → review → approve accountability`

- The **requester** cannot approve, cannot pay, and cannot sit as the sole evaluator.
- The **Procurement Committee** evaluates and recommends/signs the award.
- Payment runs through the bank mandate (commonly **three named signatories, any two transacting**, with a principal signatory — ED / Country Coordinator / National Treasurer — on all accounts), with an **approval matrix keyed to amount** (operational tier → management tier → board tier above the top threshold).

This is the NGO analogue of the PPDA separation between User Department, PDU, Evaluation Committee, and Contracts Committee.

---

## 3. Cost eligibility — the Reasonable / Allocable / Allowable test

Donor-funded spend must pass a three-part eligibility test before it is charged to a grant:

| Test | Question |
|---|---|
| **Reasonable** | Would a prudent person incur this cost, at this price, in the circumstances? |
| **Allocable** | Does the cost actually benefit the grant/project it is charged to (wholly or by a defensible basis of allocation)? |
| **Allowable** | Is the cost permitted under the grant terms and not on the unallowable list? |

Maintain a standing **unallowable-cost list** for donor work, typically including: fines and penalties, fundraising costs, entertainment, bad debts, interest, alcohol, political/lobbying costs, donations made by the grantee, and costs already funded by another donor (no double-charging). Confirm the exact list against the specific donor cost principles (e.g. 2 CFR 200 Subpart E for USAID).

---

## 4. How donor rules layer on top — stricter rule wins

The organisation's own manual is the floor. The funding donor's rules sit on top, and **where they differ, the stricter requirement governs**.

| Donor | Where its procurement rules sit |
|---|---|
| **World Bank** | Procurement Regulations for IPF Borrowers; for on-granted funds, the agreed procurement method and prior/post-review thresholds in the financing/grant agreement |
| **USAID** | ADS 302/303 and the cost principles and procurement standards in 2 CFR 200 (incl. 200.317–327 for non-federal entities) |
| **EU / GIZ** | Grant contract general conditions and PRAG-style procurement rules; nationality/origin rules; see also the `giz-eu-local-procurement-response` skill |
| **AfDB** | Bank procurement framework and the specific grant agreement |
| **UN / UNDP** | UN/agency procurement rules and the project/responsible-party agreement |

Practical rule: read the **grant agreement first**, then the donor's procurement framework, then the organisation's manual, and apply the most demanding of the three (number of quotations, thresholds for committee approval, prior-review points, nationality/eligibility, record retention).

---

## 5. Records retention

Retain the full procurement and accountability record. NGO manuals commonly set retention at **5–7 years**, but **donor terms frequently extend this** (some require retention for a fixed period after the final disbursement or project closure, which can be longer). Apply the longer of the manual period and the grant requirement.

---

## 6. Implications for proposal writers

1. **Do not apply PPDA mechanics to an NGO buyer.** There is no Contracts Committee award notice, no PPDA two-envelope rule by default, and no PPDA complaints tribunal — the discipline is the manual plus the donor framework.
2. **Mirror the buyer's own committee and threshold structure** in how you present compliance: three-quote competition, Procurement Committee evaluation, lowest responsive bid, documented exceptions.
3. **Surface the governing donor early** and align your eligibility, origin/nationality, and documentation to that donor's framework, not to PPDA.
4. **Build the Reasonable/Allocable/Allowable trail** into any cost you expect a grant to bear, and keep clear of the unallowable list.
5. For the underlying finance substance (fund accounting, deferred income, approval matrices, the procurement control chain, the RAA test, unallowable costs), the authoritative engine reference is the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine` — `doctrine/references/uganda-ngo-financial-management-patterns.md` (Procurement section) and the skill `skills/05-receivables-payables-and-treasury/accounts-payable-and-supplier-management`.

---

## 7. Related references

| Reference | Use |
|---|---|
| `contract-management-and-payment-linkage.md` | Milestone payments, retention, security, and funds-flow reconciliation |
| `ppda-act-and-regulatory-framework.md` | Contrast with the public-PDE regime (when a buyer is in fact a PDE) |
| Finance engine `uganda-ngo-financial-management-patterns.md` | Fund accounting, approval tiers, RAA test, unallowable costs (authoritative) |
| `../../../domain-delivery/giz-eu-local-procurement-response/SKILL.md` | EU/GIZ-specific tender mechanics where the donor is GIZ |
