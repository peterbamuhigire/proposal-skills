---
name: saas-poc-and-pilot-scoping
description: Use when a SaaS proposal needs a time-boxed POC or pilot with explicit scope, success measures, exit criteria, and a decision gate to implementation; use the AI-on-SaaS pilot skill when evaluation datasets or hallucination controls apply.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS POC and Pilot Scoping
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The buyer requires evidence before committing to a full SaaS implementation.
- The bid is competitive and a tight POC is a discriminator.
- The integration or regulatory risk is material and must be tested early.
- The buyer has had unsuccessful POC or pilot experiences and needs disciplined structure.

## Do Not Use When

- The bid is a fixed-scope full implementation with no POC requirement.
- The proposal scope is too large for a POC to be meaningful (use phased implementation instead).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The single risk hypothesis the POC must test (or the adoption hypothesis the pilot must validate). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The integration, data, and regulator context. | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The named users or customers who will participate. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The decision the POC / pilot result must support. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The time-box and budget available. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Decide the right artefact: Discovery POC (test a single risk), Technical POC (validate in buyer's environment), or Pilot (validate in production with a defined cohort).
2. State the single hypothesis the artefact tests. POCs with three hypotheses prove none.
3. Define written success criteria with binary pass/fail thresholds.
4. Define written exit criteria: pass, partial-pass-with-mitigation, fail.
5. Define the time-box. Discovery POC: 2–6 weeks. Technical POC: 4–8 weeks. Pilot: 8–16 weeks.
6. Define the scope (in / out) explicitly. Production data, production users, custom development beyond configuration are typically out of scope for POC.
7. Define the named cohort for a pilot — by branch, region, business unit, or customer segment.
8. Define the team and effort on both sides.
9. Define the commercial block: fixed fee, payment schedule, creditability against full implementation, and refundability rules.
10. Produce the POC / Pilot block for the Methodology and Work Plan.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- One artefact, one hypothesis.
- Success criteria are binary and measurable.
- Time-box is non-negotiable (extensions only with revised criteria).
- The agency does not offer a "free POC" — it destroys trade discipline.
- Pilot success criteria are co-authored with the buyer's named owner.

## Anti-Patterns

- POC with no exit criteria (becomes an open sandbox). **Fix:** Define hypothesis, users, tenants, data, integrations, measures, thresholds, duration, exclusions, and a written exit decision.
- Pilot that quietly becomes the full rollout. **Fix:** Cap the pilot boundary and require a separate approved rollout plan, security review, budget, and cutover gate.
- POC run on a non-representative cohort. **Fix:** Select a cohort representative of target roles, data, load, integrations, risks, and operating conditions.
- "Free POC" — destroys the value defence. **Fix:** Charge or explicitly value the POC, tie it to buyer commitment, and credit fees only under stated conversion terms.
- POC budget that is invisible inside the implementation fee. **Fix:** Show POC labour, infrastructure, third-party, support, and contingency as a separate priced line or transparent allocation.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| POC scoping block for Methodology. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Pilot scoping block for Methodology. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Success / exit criteria tables. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Effort and commercial block for the POC / pilot. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

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
| Success threshold | Set the metric, dataset, owner, deadline, and production exit rule before work starts | Open-ended pilot or subjective acceptance |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

For a claims-processing pilot, define the sample, baseline, error tolerance, user group, time box, exit evidence, and abort rule before pricing or promising rollout.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/saas-poc-scoping-template.md](../../profiles-sectors/references/saas-poc-scoping-template.md) — the template this skill operationalises.
- [../references/saas-demo-script-template.md](../../profiles-sectors/references/saas-demo-script-template.md) — the demo that precedes the POC.
- [../references/saas-mutual-action-plan-template.md](../../profiles-sectors/references/saas-mutual-action-plan-template.md) — placement of POC / pilot in the MAP.
- [../references/saas-business-case-and-roi-template.md](../../profiles-sectors/references/saas-business-case-and-roi-template.md) — the value case the pilot validates.
- [../saas-implementation-methodology/SKILL.md](../saas-implementation-methodology/SKILL.md) — full implementation methodology after pilot success.
- [../06-methodology/SKILL.md](../../pipeline/06-methodology/SKILL.md) — methodology section discipline.
