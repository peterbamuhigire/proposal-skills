# Technical Strategy Credibility Checklist

Derived from local HTML extractions on engineering strategy, SaaS architecture, cloud operations, impact mapping, customer development, and software maintenance.

## Strategy Kernel

Every technical strategy proposal should show:

- Diagnosis: the current technical, operational, user, data, and business constraints.
- Guiding policy: the few decisions that will focus delivery and trade-offs.
- Coherent actions: roadmap, architecture, governance, delivery cadence, operations, and support.

## Credibility Checks

| Area | Check |
|---|---|
| Business goal | Is every major technical decision tied to a measurable client outcome? |
| Assumptions | Which assumptions will be tested first, and how cheaply can they be tested? |
| Architecture | Are integrations, data flows, APIs, tenancy, security, observability, and ownership clear? |
| Scale | Does the proposal explain current load, expected growth, elasticity, performance, and cost control? |
| Maintainability | Are documentation, handover, upgrade path, dependency management, and support budget included? |
| Operations | Are monitoring, incident response, backups, release controls, and rollback included? |
| Governance | Are decision rights, standards, approvals, audit logs, and change control clear? |
| Roadmap | Are phases sequenced by value, risk, dependency, and learning? |
| Trade-offs | Does the proposal explain why alternatives were accepted or rejected? |

## SaaS and Cloud Notes

- Address multi-tenancy, customer-specific configuration, isolation, scaling, measured usage, security, and operational support where relevant.
- State how customisation will avoid breaking shared upgrades or other customers.
- Include billing, usage reporting, uptime, monitoring, maintenance windows, and data portability if the scope implies SaaS.

## AI Notes

- Tie use cases to business outcomes and accepted human workflows.
- Include evaluation datasets, thresholds, monitoring, human approval, fallback, prompt/model update process, and incident handling.
- Price model/API usage, testing, governance, and maintenance explicitly.

## Roadmap Pattern

1. Stabilise critical risks and data/access dependencies.
2. Validate user value with the smallest credible pilot or prototype.
3. Build the production foundation with security, observability, and support.
4. Scale only after evidence from usage, performance, quality, and adoption.
5. Institutionalise ownership through documentation, training, governance, and continuous improvement.

## Red Flags

- Roadmap is a feature list with no policy or trade-off logic.
- Architecture is presented as a diagram without operations or ownership.
- API, data, security, maintenance, or support assumptions are missing.
- SaaS customisation ignores upgrades, isolation, or support cost.
- AI promises accuracy without evaluation and monitoring.
