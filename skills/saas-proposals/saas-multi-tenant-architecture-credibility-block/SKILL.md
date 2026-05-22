---
name: saas-multi-tenant-architecture-credibility-block
description: Use when a SaaS proposal's Methodology section must demonstrate SaaS architectural literacy — control plane vs application plane, tenant isolation model, tenant context propagation, cost attribution, onboarding automation, and SaaS mindset. Distinguishes the agency from vendors who rebrand multi-customer single-tenant software as SaaS.
---

# SaaS Multi-Tenant Architecture Credibility Block
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- The buyer is sophisticated about SaaS architecture (CTO, head of digital, regulator).
- The bid competes against vendors who treat SaaS as multi-customer single-tenant software.
- The vertical (financial services, insurance, healthcare, public sector) has heightened tenant-isolation expectations.
- The proposal must defend a premium implementation fee with architectural depth.

## Do Not Use When

- The Methodology section is for a non-SaaS engagement.
- The buyer has explicitly forbidden architectural detail (rare).

## Required Inputs

- The expected number of tenants (year 1, year 3, year 5).
- The variation across tenants (branding, workflows, data schema, regulators, languages, currencies).
- The regulator stance on tenant isolation and data residency.
- The performance expectations under load.
- The buyer's current architecture posture.

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

## Quality Standards

- Tenant isolation model stated explicitly per layer, with rationale.
- Tenant context propagation discipline stated as a first-class concern.
- Cost attribution designed from day one, not deferred.
- Onboarding automated, not operations-assisted.
- Vendor-neutral language (AWS, GCP, Azure, on-prem cloud-native all valid).

## Anti-Patterns

- "We use a multi-tenant architecture" with no isolation model.
- Promising silo isolation everywhere.
- Promising pool isolation for regulated data.
- Manual operations described as a feature.
- "Cost attribution will be addressed later."
- Re-using the install-base mental model.

## Outputs

- Two-Plane Mental Model paragraph for Methodology.
- Tenant Isolation Models table.
- Tenant Context Propagation paragraph.
- Cost Attribution and Noisy-Neighbour paragraph.
- Onboarding Pattern paragraph.
- Migration paragraph (when applicable).
- SaaS Mindset paragraph.
- Architecture Decision Record (when required).

## References

- `../references/saas-multi-tenant-architecture-block.md` — primary content block.
- `../references/saas-implementation-methodology-blocks.md` — full methodology context.
- `../references/saas-risk-register-for-proposals.md` — architectural risks.
- `../references/saas-trust-and-compliance-section-template.md` — trust posture link.
- `../06-methodology/SKILL.md` — methodology section discipline.
- `../saas-implementation-methodology/SKILL.md` — companion methodology skill.
- `../references/technical-strategy-credibility-checklist.md` — broader technical strategy checks.
