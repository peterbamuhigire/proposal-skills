# SaaS Trust and Compliance Section Template

Proposal section template for the trust and compliance content that buyers expect in SaaS implementation and SaaS product-development proposals. Use as a standalone section when the ToR requires it, or as a sub-section of the Methodology and Risk Management sections.

## Section Structure

### 1. Opening Statement

"This section sets out the trust and compliance posture we propose for the engagement. Our position is that security, privacy, and operational continuity are first-class engineering concerns, not annexes. We commit to a defensible, evidenced, and regulator-aligned posture from inception through to operations, and to maintain that posture for the life of the engagement and beyond."

### 2. Information Security Management

- Information security management system standard (ISO 27001 alignment or certification, SOC 2 Type II, or sector-specific).
- Named Information Security Officer or Chief Information Security Officer for the engagement.
- Security training cadence for staff.
- Background-check policy for staff with access to client data.
- Incident response policy with tested runbook.

### 3. Tenant Isolation and Data Segregation

(Use language from `saas-multi-tenant-architecture-block.md`.)

- Isolation model chosen, layer by layer (compute, storage, identity, network, observability).
- Rationale tied to regulator stance, contractual requirements, performance, and cost.
- Tenant context propagation discipline.
- Audit logging of any cross-tenant access.

### 4. Data Residency and Sovereignty

- Where customer data is stored: country, region, named data centre operator.
- Where backups are stored.
- Where logs are stored.
- Where data may transit (CDN, anti-DDoS, observability vendors).
- Sub-processor register: name, role, data accessed, location, certifications, contractual flow-down.
- Notice mechanism for new sub-processors.
- Cross-border transfer mechanism (Standard Contractual Clauses, adequacy, BCRs).

### 5. Identity, Access, and Privilege

- Customer-facing authentication options (password + MFA, SSO/SAML, OIDC, federated, national digital ID where applicable).
- Administrative access model for agency staff.
- Privileged-access management.
- Joiner/mover/leaver process for vendor staff with access.
- Customer audit of vendor administrative access.

### 6. Encryption

- Encryption in transit (TLS version, cipher policy, mTLS where applicable).
- Encryption at rest (algorithm, key management, KMS architecture).
- Customer-managed keys option (yes / no with rationale).
- Key rotation cadence.

### 7. Application Security and Vulnerability Management

- SAST and SCA in the CI pipeline.
- DAST cadence.
- Independent penetration testing cadence and remediation SLA by severity.
- Bug-bounty programme (yes / no).
- Patching SLA by severity.

### 8. Logging, Monitoring, and Audit

- What is logged (authentication, administration, data export, configuration changes).
- Log storage location, retention period, immutability.
- Customer access to their own logs.
- Anomaly detection and alerting.
- Audit reports available to customers.

### 9. Business Continuity and Disaster Recovery

- RTO and RPO by service tier.
- DR architecture (active-active, active-standby, cold).
- DR test cadence (annual minimum).
- Backup architecture and recovery testing.
- Communication protocol during incidents.

### 10. Incident Response and Breach Notification

- Severity model.
- Response and resolution SLAs by severity.
- Customer notification SLA for personal-data breaches (typically 24–72 hours).
- Forensic readiness.
- Post-incident review and customer communication.

### 11. Compliance Certifications and Regulator Alignment

- Certifications held (SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA where applicable).
- Local regulator alignment (state regulators by name).
- GDPR alignment and the lawful basis for each processing activity.
- Sector-specific certifications.

### 12. Exit, Portability, and Termination Protections

- Data return format and timeline at termination.
- Data deletion timeline post-termination.
- Source-code escrow if applicable.
- Customer continuity during a wind-down period.

### 13. Audit Rights

- Customer audit rights and limits.
- Audit cadence and notice.
- Independent-auditor report option.
- Regulator audit support.

### 14. Insurance

- Professional indemnity (named limit).
- Cyber liability (named limit).
- General liability (named limit).
- Certificate of insurance available on signature.

### 15. SLA and Remedies

- Tier-by-tier availability target.
- Severity model.
- Credit mechanism.
- Material-breach termination rights.

### 16. Continuous Trust Posture

- Annual external penetration test.
- Annual DR test.
- Annual customer-facing trust report.
- Quarterly regulator-alignment review.
- Sub-processor change notice protocol active.

## Annex A: Sub-Processor Register

| Name | Role | Data Accessed | Location | Certifications | Flow-down |
|---|---|---|---|---|---|
| [Sub-processor 1] | [Role] | [Data category] | [Location] | [Cert] | [Yes/No] |
| [Sub-processor 2] | | | | | |

## Annex B: Compliance Mapping

| Buyer Requirement | Our Posture | Evidence |
|---|---|---|
| ISO 27001 | Certified | Certificate available |
| SOC 2 Type II | Annual report | Report available under NDA |
| GDPR / [local regulator] | Compliant | DPA available, lawful-basis register |
| Sector-specific (e.g., banking, insurance) | [Aligned / Certified] | [Evidence] |

## Annex C: Incident Response Summary

| Severity | First Response | Status Updates | Resolution Target | Customer Notification |
|---|---|---|---|---|
| Sev 1 | 15 min, 24x7 | Every 30 min | 4 hours | Per DPA |
| Sev 2 | 1 hour, 24x7 | Every 2 hours | 8 business hours | Per DPA |
| Sev 3 | 4 business hours | Daily | 5 business days | If applicable |
| Sev 4 | 1 business day | Weekly | Next release | If applicable |

## Anti-Patterns

- Stating posture without evidence.
- Listing certifications without their scope (the certified scope is what matters).
- Promising regulator alignment the agency has not validated.
- Hiding sub-processors.
- Generic language that could apply to any vendor.

## See Also

- `saas-procurement-and-security-questionnaire-playbook.md` for the underlying review pack.
- `saas-msa-dpa-sla-template-language.md` for contract-grade clauses.
- `saas-risk-register-for-proposals.md` for the linked risks.
- `saas-multi-tenant-architecture-block.md` for the isolation paragraphs.
