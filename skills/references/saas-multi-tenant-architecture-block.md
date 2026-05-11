# SaaS Multi-Tenant Architecture Credibility Block

Architecture-grade paragraphs and tables that prove SaaS literacy inside the proposal's Methodology and Understanding-of-Assignment sections. Use to distinguish the agency from vendors who are rebranding multi-customer single-tenant software as "SaaS."

## The Two-Plane Mental Model (Standard Paragraph)

"A SaaS solution comprises two planes that we design, build, and operate as distinct disciplines. The control plane handles tenant lifecycle: onboarding, tenant management, identity, billing integration, observability, audit, and cost attribution. The application plane is the product the tenants actually use. The two planes share a single tenant model, and every service in the application plane carries tenant context as a first-class concern. This separation is what distinguishes a SaaS solution from a multi-customer single-tenant solution. We use it as a design lens from inception through to operations."

## Tenant Isolation Models (Standard Table)

| Isolation Layer | Silo | Pool | Bridge |
|---|---|---|---|
| Compute | Dedicated containers, VMs, or clusters per tenant. Highest isolation, highest cost. | Shared compute with strict tenant context. Lowest cost, requires disciplined enforcement. | Shared compute for most tenants, dedicated for premium or regulated tenants. |
| Storage (relational) | Database per tenant. Strong isolation, operational complexity at scale. | Shared schema with tenant_id column on every table. Most scalable, requires strict row-level security. | Shared schema with separate database for premium/regulated tenants. |
| Storage (object) | Bucket per tenant. | Shared bucket with tenant-prefixed paths and IAM. | Hybrid. |
| Identity | Tenant-specific IdP. | Shared IdP with tenant claim. | Tenant choice with IdP federation. |
| Network | VPC or subnet per tenant. | Shared network with tenant-aware routing. | Hybrid. |
| Observability | Per-tenant telemetry stream. | Shared telemetry tagged with tenant_id. | Hybrid. |

For each engagement, the proposal names the chosen model layer-by-layer in the Architecture Decision Record. The choice is driven by regulator stance, customer contractual requirements, performance, and cost — not by ideology.

## Tenant Context Propagation (Standard Paragraph)

"Every service in our application plane treats tenant context as a first-class concern. Tenant identity is carried explicitly through every request (typically as a signed claim in the request context), enforced at service boundaries, and audited in logs. Cross-tenant data access is impossible by construction in services that handle tenant data, and is treated as a security incident in services that legitimately operate across tenants (typically billing aggregation and platform observability). This discipline is the foundation of our trust posture and the underlying mechanism by which we make data-residency and contractual segregation commitments enforceable rather than aspirational."

## Cost Attribution and Noisy-Neighbour Management (Standard Paragraph)

"Per-tenant cost attribution is a design concern, not an afterthought. From day one, the control-plane observability layer captures compute, storage, and request-volume telemetry tagged with tenant identity. This produces three operating capabilities: defensible pricing (tier-cost mapping), noisy-neighbour detection (a tenant whose usage spikes beyond their fair share of pooled resources), and tenant-level capacity planning (which tenants warrant dedicated infrastructure). The detection and response mechanisms are documented in the operations runbook and tested under load before cutover."

## Onboarding Pattern (Standard Paragraph)

"Tenant onboarding is automated from contract signature through to first user productive. For commercial onboarding (contract, KYC where applicable, security review for enterprise tier) we accept that human steps remain. For technical onboarding (tenant provisioning, identity setup, initial configuration, sample data, admin invitation, first-value-moment instrumentation) we automate completely. A SaaS implementation that requires manual operations team involvement for each new tenant is not SaaS in the modern sense — and the proposal makes this commitment explicit."

## Migration of Install-Base to Multi-Tenant (Standard Paragraph for Legacy-Replacement Bids)

"For [client]'s installed-software base, we propose a tenant-by-tenant migration to the multi-tenant platform. The sequence is: tenant model selection (silo / pool / bridge by customer tier), data-migration discipline (extract, transform, validate, load with reconciliation), parallel-run window (two to four weeks with both systems live, with daily reconciliation), cutover (with a defined rollback), and legacy-installation deprecation (with a defined sunset window and customer communication). The migration is engineered to be resumable per tenant — a failed migration of one tenant does not block others — and to preserve customer-facing service continuity throughout."

## SaaS Mindset and Operating Model Change (Standard Paragraph)

"A SaaS architecture is only effective if the operating organisation adopts the SaaS mindset. The change-management workstream addresses the four substantive shifts: from per-customer operations to per-tenant operations, from scheduled per-customer releases to continuous releases for all tenants, from installation services to customer-success engagement, and from perpetual-licence-plus-maintenance to recurring-subscription commercial models. The change is staffed, measured, and reinforced through the change-management workstream rather than treated as a communications exercise."

## Common Architecture Decision Record (ADR) Headings

When the engagement requires an ADR for the tenant model, the standard headings are:

1. Decision title.
2. Status (proposed / accepted / superseded).
3. Context (what is the engagement, what is the regulatory and commercial situation).
4. Decision (the model chosen per layer).
5. Consequences (cost shape, performance shape, regulator alignment, operational complexity).
6. Alternatives considered and why rejected.
7. Sign-offs (CTO, DPO, CFO, sponsor).

## Anti-Patterns

- "We use a multi-tenant architecture" with no statement of isolation model. This is the most common credibility error.
- Promising silo isolation everywhere — usually unaffordable at scale, and unnecessary.
- Promising pool isolation for regulated data — usually unacceptable to regulators.
- Manual operations involvement for each new tenant described as a feature.
- "Cost attribution will be addressed later" — by then it is unsalvageable.
- Re-using the install-base mental model: per-customer environments, scheduled per-customer releases, installation services.

## See Also

- `saas-implementation-methodology-blocks.md` for the full methodology these blocks slot into.
- `saas-procurement-and-security-questionnaire-playbook.md` for the trust posture these blocks describe.
- `saas-risk-register-for-proposals.md` for the risks introduced and managed by these architectural choices.
