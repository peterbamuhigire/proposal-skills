# SaaS Procurement and Security Questionnaire Playbook

Playbook for navigating procurement, legal, and security review for SaaS implementation engagements. Used inside the Trust and Compliance section of the proposal, the Risk Management section, and as an internal checklist when running the security questionnaire pass.

The bar: the agency should answer every reasonable security questionnaire item before it is asked, and should make the answers easy to find. Procurement and security reviews are where premium SaaS bids most often slip — the playbook is engineered to remove that slip.

## Procurement Path Mapping

| Step | Typical Buyer Owner | Typical Duration | Agency Response |
|---|---|---|---|
| RFI / RFP issuance | Procurement | T0 | Mark all required fields, calendar all deadlines |
| Clarification window | Procurement | 5–10 days | Submit clarifications in writing; expect responses to take similar time |
| Submission | Procurement | T+30 to T+45 | Compliance pass; envelope separation where required |
| Technical evaluation | Technical committee | 2–4 weeks | Bid manager available for clarifications |
| Reference checks | Technical committee | 1–2 weeks | Reference list ready, references warmed |
| Oral / demo | Evaluation committee | 1 week | Demo script tuned to diagnosed pain |
| Security review | CISO / IT security | 2–6 weeks | Pre-emptive security questionnaire pack |
| Legal review | General counsel | 2–4 weeks | MSA, DPA, SLA templates ready |
| BAFO | Procurement + CFO | 1–2 weeks | Trade options prepared (not pure discount) |
| Award decision | Steering committee | 1–2 weeks | Win plan executed |
| Contract negotiation | Legal + procurement | 2–6 weeks | Standard redline patterns prepared |
| Contract signature | CEO / general counsel | 1 week | Signature ceremony scheduled |

## Security Questionnaire Pack — What Buyers Typically Ask

Group answers around these categories. The agency maintains a master security questionnaire response pack and tailors per engagement.

### 1. Organisational Security
- Information security management system in place (ISO 27001 or equivalent).
- Named Information Security Officer or Chief Information Security Officer.
- Security training cadence for all staff.
- Background-check policy for new staff.
- Incident response policy and tested runbook.

### 2. Tenant Isolation and Data Segregation
- Logical isolation model used (silo, pool, bridge) and rationale.
- How tenant context propagates through services.
- How a tenant's data is guaranteed not to leak to another tenant.
- Cryptographic separation if applicable (per-tenant keys).
- Audit logging of cross-tenant access (which should be none in normal operations).

### 3. Data Residency, Sovereignty, and Sub-Processors
- Where customer data is stored (country, region, named data centre operator).
- Where backups are stored.
- Where logs are stored.
- Where customer data may transit through (CDN, anti-DDoS, observability vendors).
- Full sub-processor register with: name, role, data accessed, location, certifications, contractual flow-down of obligations.

### 4. Identity, Access, and Privilege
- Customer-facing authentication options (password + MFA, SSO/SAML, OIDC, IdP federation).
- Administrative access model for agency / vendor staff.
- Privileged-access management.
- Joiner/mover/leaver process for vendor staff with access.
- Customer audit of vendor administrative access.

### 5. Encryption
- Encryption in transit (TLS version, ciphers, mutual TLS where applicable).
- Encryption at rest (algorithm, key management, KMS architecture).
- Customer-managed keys option if needed.
- Key rotation cadence.

### 6. Vulnerability Management and Application Security
- SAST and SCA in the CI pipeline.
- DAST cadence on production-equivalent environments.
- Independent penetration testing cadence and remediation SLA.
- Bug-bounty programme if applicable.
- Patching SLA by severity.

### 7. Logging, Monitoring, and Audit
- What is logged (auth, admin, data export, configuration changes).
- Where logs are stored, retention period, immutability.
- Customer access to their own logs.
- Anomaly detection and alerting.
- Audit reports available to customers (SOC 2 Type II, ISO 27001, regulator-specific).

### 8. Business Continuity and Disaster Recovery
- RTO and RPO for each tier of the service.
- DR architecture (active-active, active-standby, cold).
- DR tests cadence (typically annual minimum).
- Backup architecture and recovery testing.
- Communication protocol during incidents.

### 9. Incident Response and Breach Notification
- Incident severity model.
- Response and resolution SLAs by severity.
- Customer notification SLA (typically 72 hours for material breaches; faster for regulated sectors).
- Forensic readiness.
- Post-incident review and customer communication.

### 10. Compliance Certifications
- SOC 2 Type II.
- ISO 27001, ISO 27017, ISO 27018 (cloud and PII extensions).
- PCI DSS where applicable.
- HIPAA where applicable.
- Local regulator certifications (NITA-U for Uganda data, NDPR for Nigeria, POPIA registration for South Africa, sector-specific approvals for banking and insurance regulators).
- GDPR alignment and the lawful basis declared for each processing activity.

### 11. Exit, Portability, and Termination
- Data return format and timeline at termination.
- Data deletion timeline post-termination.
- Source-code escrow if applicable.
- Customer ability to continue operating during a wind-down period.
- No data hostage clauses.

### 12. Contractual Flow-Down
- DPA terms aligned to applicable data protection law.
- SCCs or equivalent for cross-border data flows.
- Sub-processor consent and notification.
- Audit rights for the customer (and limits).
- Insurance: professional indemnity, cyber liability — with named limits.

## Standard Proposal Paragraphs (Patterns)

### Tenant Isolation Statement
"The proposed platform is designed with tenant isolation as a first-class architectural concern. Each tenant operates within its own logical boundary, with tenant context propagated through every service. For [client name]'s vertical, the recommended isolation model is [silo / pool / bridge] for the following reasons: [regulator stance, customer contractual requirements, performance reasons]. Cross-tenant access is auditable, and the operating runbook treats any cross-tenant access event as a security incident."

### Data Residency Statement
"Customer data is stored, processed, and backed up exclusively within [region/jurisdiction]. Log telemetry is stored within the same jurisdiction. Sub-processors are listed in Annex [N] with their role, location, and contractual flow-down. Any change to the sub-processor list will be notified [N] days in advance with an opportunity for the customer to object."

### Exit Clause Statement
"At any time during or after the contract, the client may request a full export of its data in [defined format], at no charge for the first request per twelve-month period. On contract termination, the client may continue read-only access for up to [90] days at no charge to facilitate transition. The agency commits to defined deletion of all client data within [30] days of the transition window closing, with a written certificate of deletion provided. Source code for client-specific configurations is held in escrow with [named escrow agent]."

### SLA and Remedies Statement
"The service operates under a tier-appropriate SLA. For the Enterprise tier, the committed availability is 99.9%, measured monthly, with credit-based remedies as set out in Annex [N]. The SLA excludes scheduled maintenance windows (announced not less than 14 days in advance) and force-majeure events. Material SLA breaches in three consecutive months entitle the client to a contract review with proportionate remedies up to and including termination without further liability."

## Anti-Patterns

- Answering security questions with marketing language ("industry-leading", "world-class") — the security reviewer wants specifics or evidence.
- Promising certifications the agency does not hold and cannot inherit from its cloud provider.
- Treating the security questionnaire as a procurement formality — security reviewers can and do veto.
- Hiding sub-processors — discovery during legal review is a frequent deal-killer.
- "We will commit to X SLA" with no penalty structure — buyers read this as bluff.

## See Also

- `saas-msa-dpa-sla-template-language.md` for contract-grade language patterns.
- `saas-trust-and-compliance-section-template.md` for the proposal section structure.
- `saas-risk-register-for-proposals.md` for the risk register entries this playbook supports.
- `saas-mutual-action-plan-template.md` for Phase 2 (contract, security, mobilisation) detail.
