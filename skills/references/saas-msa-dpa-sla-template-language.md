# SaaS MSA / DPA / SLA Template Language

Proposal-grade language patterns for the commercial and contractual framing of SaaS implementation engagements. Use inside the Trust and Compliance section, the Financial Proposal narrative, and as a briefing document when the agency's legal team prepares contract drafts.

This file is *not legal advice* and does not replace counsel. It is reusable language to make the proposal credible to procurement, legal, and risk reviewers.

## Master Services Agreement (MSA) — Standard Clause Themes

### Scope of Services
- Define services by Statement of Work (SoW) appended to the MSA.
- Allow multiple SoWs under one MSA without re-negotiating the master terms.
- Each SoW names: deliverables, acceptance criteria, fees, payment milestones, change-control procedure, term.

### Term, Renewal, and Termination
- Initial term tied to the implementation engagement length, typically 12–36 months.
- Renewal: auto-renewal annually with 90-day notice of non-renewal, or fixed renewal with renegotiation window.
- Termination for cause: material breach with 30-day cure period.
- Termination for convenience: typically allowed with 90-day notice and pro-rata refund of prepaid subscription; implementation fees non-refundable past defined milestones.
- Termination for regulatory event: client right to terminate without penalty if regulator prohibits the service.

### Fees and Payment
- Implementation fees: milestone-based, defined in the SoW.
- Subscription fees: annual in advance is standard; quarterly or monthly available for SMB tiers.
- Late payment: interest at the lower of contractual rate or maximum allowed by jurisdiction.
- Dispute mechanism: notify within 30 days, pay undisputed portion, escalate the disputed portion through a defined process.

### Intellectual Property
- Vendor retains IP in the platform.
- Client retains IP in client data and client-specific configurations.
- Custom development clearly delineated: vendor IP or client IP, with licence terms either way.
- Open-source disclosures and licence compatibility maintained.

### Confidentiality
- Mutual NDA layered into MSA.
- Carve-outs for legal disclosure requirements with notice to the affected party.
- Survival of confidentiality obligations beyond contract termination (typically 3–5 years; indefinite for trade secrets).

### Warranties
- Service performs materially as described in the documentation.
- Vendor has the right to grant the licences provided.
- No malware, no known unremediated vulnerabilities at delivery.
- Disclaimer of implied warranties to the extent allowed.

### Liability
- Cap on liability: typically 12 months of fees paid; or a multiple thereof for material breaches.
- Carve-outs from the cap: IP infringement indemnity, breach of confidentiality, breach of data protection, gross negligence, wilful misconduct.
- Mutual carve-out structure where applicable.

### Indemnity
- Vendor indemnifies for third-party IP infringement claims against the platform.
- Client indemnifies for misuse, client-supplied content violations.

### Insurance
- Professional indemnity: named minimum (e.g., $5m).
- Cyber liability: named minimum (e.g., $5m).
- General liability: named minimum.
- Workers' compensation as required.
- Certificates of insurance made available to the client.

### Governing Law and Dispute Resolution
- Governing law: a neutral jurisdiction the buyer trusts (often England & Wales, Singapore, or the client's home jurisdiction).
- Dispute resolution: negotiation → mediation → arbitration; arbitral seat and rules named (e.g., LCIA, ICC, KIAC, Mauritius Arbitration Centre for African engagements).
- Carve-out for injunctive relief in any competent court.

### Force Majeure
- Standard force majeure clause with prompt notice and mitigation duty.
- Excludes financial inability to pay.

## Data Protection Addendum (DPA) — Standard Clause Themes

### Roles
- Define which party is controller and which is processor for each processing activity.
- For shared controllership scenarios, name the lawful basis and the public-facing transparency wording.

### Processing Scope
- Annex listing categories of data subjects, categories of personal data, purposes of processing, retention period, security measures.
- Restrictions on processing beyond the stated purpose.

### Sub-Processors
- List of approved sub-processors with role, location, certifications.
- Notice mechanism for new sub-processors (typically 30-day advance notice with objection right).
- Flow-down of processor obligations to sub-processors by contract.

### International Transfers
- Lawful transfer mechanism named: Standard Contractual Clauses, adequacy decision, binding corporate rules.
- Transfer impact assessment available to the client on request.
- For African engagements, identify whether the client's jurisdiction requires data residency or local copies.

### Security Measures
- Annex describing technical and organisational measures (encryption, access control, segregation, logging, BCDR).
- Commitment to maintain at least the stated measures throughout the term.

### Data Subject Rights
- Vendor assists the client in responding to data-subject requests within the relevant regulator's timeline.
- Mechanism for tagging, retrieval, and deletion at subject level.

### Breach Notification
- Vendor notifies the client of a personal data breach without undue delay and not later than [24–72] hours after becoming aware.
- Notification content: nature, categories of data subjects, likely consequences, mitigations.

### Audit
- Client audit rights, typically once per 12 months on reasonable notice, or by an independent auditor's report (SOC 2 Type II, ISO 27001 audit).
- Regulator audit support obligation.

### Return and Deletion
- On termination, vendor returns data in the agreed format and within the agreed window, then deletes copies (subject to legal retention obligations).

## Service Level Agreement (SLA) — Standard Clause Themes

### Service Tiers
| Tier | Target Availability | Measurement Window | Credits |
|---|---|---|---|
| Starter | 99.5% | Monthly | None or de minimis |
| Pro | 99.9% | Monthly | 10% of monthly fee per 0.5% miss |
| Enterprise | 99.95% | Monthly | 25% of monthly fee per 0.5% miss; right to terminate after 3 consecutive material misses |

### Severity Levels
| Severity | Definition | First Response | Status Updates | Resolution Target |
|---|---|---|---|---|
| Sev 1 | Service unavailable or material data loss; production impact across many tenants. | 15 minutes, 24x7 | Every 30 minutes | 4 hours |
| Sev 2 | Major feature unavailable; production impact on a single tenant or business unit. | 1 hour, 24x7 | Every 2 hours | 8 business hours |
| Sev 3 | Minor feature impaired; workaround available. | 4 business hours | Daily | 5 business days |
| Sev 4 | Cosmetic, documentation, or enhancement request. | 1 business day | Weekly | Next release cycle |

### Exclusions
- Scheduled maintenance windows (announced not less than 14 days in advance).
- Force majeure.
- Issues caused by client's misuse, third-party integrations outside the agency's scope, client-managed components.
- Beta or preview features.

### Credit Mechanism
- Credits apply against the next invoice after a written claim within 30 days of the SLA breach.
- Credits are the sole remedy except for material consecutive breaches that trigger termination rights.

### Reporting
- Monthly availability report to the client.
- Annual SLA review with the client's operations team.
- Real-time status page available to all clients.

### Continuity
- BCDR runbook reviewed annually.
- Annual DR test with the client's participation if requested.
- RTO and RPO stated by service tier.

## Common Negotiated Carve-Outs

| Item | Default | Common Buyer Ask |
|---|---|---|
| Liability cap | 12 months' fees | 24 months' fees or contract value, whichever higher |
| Data breach liability | Above cap with sub-cap | Uncapped for gross negligence |
| Audit frequency | Annual, on notice | Twice annually for regulated buyers |
| Sub-processor consent | Notice with objection right | Prior written consent for new processors |
| Data residency | Region | Country / data centre operator named |
| Exit data return | 30 days | 90 days with read-only access |
| Renewal | Auto with 90-day notice | Express renewal only |

## Anti-Patterns

- Promising specific contractual terms in the proposal that the agency's legal team has not approved.
- "We are flexible on contract terms" with no detail — procurement reads this as we will fold under pressure.
- Hiding important clauses (auto-renewal, price-increase, data-return, sub-processor list) in fine print at the end of the proposal.
- Mismatched MSA / DPA / SLA: the DPA promises a 24-hour breach notice, the SLA says 72 hours.
- Insurance limits stated but no certificate ever produced when asked.

## See Also

- `saas-procurement-and-security-questionnaire-playbook.md` for the security questions these clauses answer.
- `saas-trust-and-compliance-section-template.md` for the proposal section structure.
- `saas-risk-register-for-proposals.md` for the linked risks.
- `saas-mutual-action-plan-template.md` for the MAP placement (Phase 2).
