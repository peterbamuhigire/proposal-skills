---
name: saas-mutual-action-planning-and-close-plans
description: Use when a SaaS bid needs a buyer-and-supplier Mutual Action Plan from selection through signature, go-live, and value realisation, with owners and decision gates; use implementation methodology for delivery activities after award.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Mutual Action Planning and Close Plans
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The buyer values predictability and shared accountability through the award and implementation journey.
- The bid is competitive and the MAP creates a tangible discriminator.
- The procurement path is long or complex (public sector, regulated industries) and the buyer benefits from a shared plan.
- The buyer has signalled hesitation about "what happens after we sign."

## Do Not Use When

- The proposal is a pure compliance response with no buyer-engagement value.
- The procurement framework forbids unsolicited annexes.

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The expected procurement path (dates, owners, gates). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The expected implementation phases and durations. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The expected adoption and value-realisation cadence. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The named buyer owners on each side (where the agency knows them). | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The agency's bid manager, account director, solution lead, delivery lead, and customer success lead. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Identify the right placement of the MAP: Executive Summary annex, standalone annex, BAFO supplement, or oral presentation document.
2. Build the MAP in five phases:
   - Phase 1: Selection and Award (clarifications, references, demo, BAFO, award, NTP).
   - Phase 2: Contract, Security, Mobilisation (MSA/DPA/SLA, security review, sub-processors, contract signature, kick-off).
   - Phase 3: Build and Configure (tenant model decision, integration discovery, data implementation plan, configuration walkthroughs, UAT entry).
   - Phase 4: Pilot and Cutover (pilot cohort, pilot launch, 30-day review, cutover plan, cutover, stabilisation).
   - Phase 5: Adoption and Value Realisation (30/60/90-day reviews, first QBR, expansion conversation).
3. For each phase, name task, buyer owner, agency owner, target date, decision gate.
4. Define decision gates: decider, evidence, escalation if slipped > 5 working days.
5. Define operating rules for MAP maintenance.
6. Build a separate Close Plan covering the path from BAFO to signature.
7. Brief the agency team and the buyer's owner on the MAP before submission.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Every task names a buyer owner and an agency owner.
- Every decision gate names a decider and evidence.
- No "passed conditionally" — gates are binary: passed, held, or passed-with-named-risks.
- Phases have outcome statements that determine when the phase is done.
- The MAP is reviewed weekly during build, daily during cutover, and at QBR cadence after stabilisation.

## Anti-Patterns

- A MAP that lists only the agency's tasks. **Fix:** Include buyer and supplier tasks, dependencies, owners, dates, evidence, and consequences in one jointly maintained plan.
- Dates without owners. **Fix:** Assign one accountable owner for every date and record the escalation path for missed dependencies.
- Decision gates without evidence (turns the gate into a meeting). **Fix:** Define the document, approval, test result, or decision record required to pass each gate.
- "Passed conditionally" status that becomes forgotten technical debt. **Fix:** Time-box conditional status, assign remediation and owner, and block the dependent gate until evidence closes it.
- Phases without outcome statements. **Fix:** State the buyer-visible outcome and acceptance evidence for every phase, not only its activities.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Mutual Action Plan (table per phase + operating rules). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Close Plan (BAFO to signature). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Decision-gate register with deciders, evidence, and escalation rules. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Brief for the agency team and the buyer's owner. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

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
| Buyer dependency | Name the buyer owner, due date, evidence, and consequence in the shared plan | Supplier-only schedule that cannot reach award |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

If legal review has no named owner or date, show it as an unresolved dependency in the mutual action plan and do not present the target signature date as committed.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/saas-mutual-action-plan-template.md](../../profiles-sectors/references/saas-mutual-action-plan-template.md) — primary template.
- [../references/saas-procurement-and-security-questionnaire-playbook.md](../../profiles-sectors/references/saas-procurement-and-security-questionnaire-playbook.md) — Phase 2 detail.
- [../references/saas-customer-success-engagement-package.md](../../profiles-sectors/references/saas-customer-success-engagement-package.md) — Phase 5 detail.
- [../references/meddic-and-command-of-message-for-saas.md](../../profiles-sectors/references/meddic-and-command-of-message-for-saas.md) — qualification logic.
- [../08-work-plan/SKILL.md](../../pipeline/08-work-plan/SKILL.md) — work plan section discipline.
- [../saas-discovery-and-qualification/SKILL.md](../saas-discovery-and-qualification/SKILL.md) — inputs to the MAP from discovery.
