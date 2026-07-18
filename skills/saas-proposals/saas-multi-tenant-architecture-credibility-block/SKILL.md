---
name: saas-multi-tenant-architecture-credibility-block
description: Use when a SaaS proposal needs a concise architecture credibility block covering control and application planes, tenant isolation, context propagation, onboarding, and cost attribution; use implementation methodology for the full delivery sequence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Multi-Tenant Architecture Credibility Block
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- The buyer is sophisticated about SaaS architecture (CTO, head of digital, regulator).
- The bid competes against vendors who treat SaaS as multi-customer single-tenant software.
- The vertical (financial services, insurance, healthcare, public sector) has heightened tenant-isolation expectations.
- The proposal must defend a premium implementation fee with architectural depth.

## Do Not Use When

- The Methodology section is for a non-SaaS engagement.
- The buyer has explicitly forbidden architectural detail (rare).

## Required Inputs

| Artefact or fact | Required? | Source/provider | If absent |
|---|---|---|---|
| The expected number of tenants (year 1, year 3, year 5). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The variation across tenants (branding, workflows, data schema, regulators, languages, currencies). | Required | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The regulator stance on tenant isolation and data residency. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The performance expectations under load. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |
| The buyer's current architecture posture. | Conditional | Buyer, ToR, approved records, or discovery | Mark unavailable, request it, and qualify any affected claim or artefact. |

## Workflow

1. Open the Methodology section with the Two-Plane Mental Model paragraph: control plane vs application plane, shared tenant model, tenant context propagation.
2. Decide the tenant isolation model layer by layer (compute, storage, identity, network, observability): silo, pool, or bridge. Document in an Architecture Decision Record.
3. State the rationale for the chosen model: regulator stance, contractual requirements, performance, cost.
4. Write the Tenant Context Propagation paragraph: tenant identity carried explicitly through every request, enforced at boundaries, audited.
5. Write the Cost Attribution and Noisy-Neighbour paragraph: per-tenant telemetry from day one, defensible pricing, detection-and-response runbook.
6. Write the Onboarding Pattern paragraph: automated technical onboarding; only commercial onboarding remains human.
7. If migration is in scope, write the Migration of Install-Base to Multi-Tenant paragraph: tenant-by-tenant migration, parallel run, cutover, deprecation.
8. Write the SaaS Mindset paragraph: per-tenant operations, continuous release, customer success replaces install services, recurring revenue model.
9. Include the ADR headings if the engagement requires an ADR.


**Stop condition:** Stop before asserting scope, compliance, value, acceptance, or readiness when a load-bearing input is missing or contradicted.

**Recovery:** Record the gap, owner, and next evidence step; then return the narrowest qualified proposal content that remains supportable.

## Quality Standards

- Tenant isolation model stated explicitly per layer, with rationale.
- Tenant context propagation discipline stated as a first-class concern.
- Cost attribution designed from day one, not deferred.
- Onboarding automated, not operations-assisted.
- Vendor-neutral language (AWS, GCP, Azure, on-prem cloud-native all valid).

## Anti-Patterns

- "We use a multi-tenant architecture" with no isolation model. **Fix:** Name the isolation model by component and data class, enforcement points, tenant-context propagation, and verification tests.
- Promising silo isolation everywhere. **Fix:** Reserve silo isolation for justified regulatory, security, performance, or commercial needs and price its operational cost.
- Promising pool isolation for regulated data. **Fix:** Use stronger isolation for regulated data unless a documented threat model and controls support pooling.
- Manual operations described as a feature. **Fix:** Automate onboarding, provisioning, upgrades, support, and offboarding; label any manual exception and its retirement gate.
- "Cost attribution will be addressed later." **Fix:** Define metering, allocation, budgets, alerts, and tenant profitability reporting before architecture sign-off.
- Re-using the install-base mental model. **Fix:** Design one configurable product and shared operating model with tenant-aware controls rather than customer-specific installs.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Two-Plane Mental Model paragraph for Methodology. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Tenant Isolation Models table. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Tenant Context Propagation paragraph. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Cost Attribution and Noisy-Neighbour paragraph. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Onboarding Pattern paragraph. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Migration paragraph (when applicable). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| SaaS Mindset paragraph. | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |
| Architecture Decision Record (when required). | Proposal evaluator, buyer owner, and delivery team | Content is complete, traceable to named inputs, and usable in its stated proposal section without an unsupported claim. |

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
| Isolation model | State the chosen boundary, enforcement point, and verification evidence | Multi-customer software misrepresented as SaaS |
| Missing load-bearing evidence | Stop the affected claim, record the gap and owner, and continue only with separable supported content. | Fabricated assurance or hidden dependency |
| Conflicting buyer and supplier evidence | Surface the conflict for decision; do not silently choose the favourable version. | Misaligned scope, price, or acceptance |
| Irreversible, contractual, publishing, or production action | Obtain explicit authority and preserve an approval record before acting. | Unauthorised commitment or mutation |

## Worked Example

When the buyer asks how tenant data is isolated, describe the evidenced identity, authorisation, storage, encryption, logging, and test controls; mark any untested isolation claim not assessed instead of asserting architectural safety.

## References

- [Proposal skill router](../../SKILL.md) — routing, profile, reasoning, and final quality gates.
<!-- dual-compat-end -->
- [../references/saas-multi-tenant-architecture-block.md](../../profiles-sectors/references/saas-multi-tenant-architecture-block.md) — primary content block.
- [../references/saas-implementation-methodology-blocks.md](../../profiles-sectors/references/saas-implementation-methodology-blocks.md) — full methodology context.
- [../references/saas-risk-register-for-proposals.md](../../profiles-sectors/references/saas-risk-register-for-proposals.md) — architectural risks.
- [../references/saas-trust-and-compliance-section-template.md](../../profiles-sectors/references/saas-trust-and-compliance-section-template.md) — trust posture link.
- [../06-methodology/SKILL.md](../../pipeline/06-methodology/SKILL.md) — methodology section discipline.
- [../saas-implementation-methodology/SKILL.md](../saas-implementation-methodology/SKILL.md) — companion methodology skill.
- [../references/technical-strategy-credibility-checklist.md](../../profiles-sectors/references/technical-strategy-credibility-checklist.md) — broader technical strategy checks.
