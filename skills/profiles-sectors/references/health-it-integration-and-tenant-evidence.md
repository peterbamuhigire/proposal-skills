# Health IT Integration and Tenant Evidence

Use this reference when a health, health-financing, or health-operations proposal includes an integration, shared platform, hosted service, or multi-tenant data boundary. It prepares procurement questions and an evidence handoff. It does not certify an implementation, clinical safety, privacy compliance, or a vendor control.

## Outcome and boundary

The proposal evaluator should be able to answer three questions:

1. What data crosses which system or tenant boundary, and who owns the source of truth?
2. What evidence supports the supplier's isolation, integration, audit, subprocessor, and exit answers?
3. Which checks remain `NOT_ASSESSED`, `DENIED`, or dependent on a named technical or legal reviewer?

Keep the following separate:

- a supplier assertion;
- an artefact that supports the assertion;
- a synthetic or observed test result; and
- a human acceptance decision.

Do not infer conformance from a product name or protocol label. If a buyer mentions FHIR, PACS, SaaS, a national health system, a regulator, or a security standard, capture the exact version, scope, jurisdiction, and source supplied by the buyer or vendor. Current conformance remains `NOT_ASSESSED` until the current authoritative source and an appropriate reviewer are recorded.

## Required inputs

| Input | Minimum fields | If missing |
|---|---|---|
| Buyer data and integration scope | tenants, systems, data classes, source of truth, direction, lifecycle | Stop the affected assurance and return an evidence request. |
| Supplier architecture and control evidence | tenant-context enforcement, identity, authorisation, logging, export, deletion, incident and recovery evidence | Mark the affected answer `NOT_ASSESSED`; do not substitute a generic control statement. |
| Version and currentness record | product/interface version, source ID, source scope, publication or revision date, access date, verification date, review date | Quarantine the version or conformance claim. |
| Independent acceptance oracle | named security/architecture reviewer and observable test cases | The proposal may describe the test plan, but cannot call the control passed. |

## Procurement question set

Ask for an answer, evidence ID, owner, and review state for every applicable question.

| Area | Question | Minimum evidence |
|---|---|---|
| Tenant isolation | How is tenant context established, propagated, checked, and logged on every read, write, export, and administrative path? | Architecture or control description plus a wrong-tenant test result. |
| Data scope | Which data classes, identifiers, attachments, metadata, logs, backups, and support copies are in scope? | Data-flow or processing inventory with source and version. |
| Integration | Which interfaces, mappings, identifiers, retries, duplicate rules, and failure recovery apply? | Versioned mapping, test result, and owner. |
| Source of truth | Which system wins when records conflict, and who approves reconciliation? | Decision record and reconciliation evidence. |
| Audit | What events are retained, for how long, and who can inspect them? | Log-field sample or approved control evidence. |
| Subprocessors | Which parties receive data, for what purpose, in which region, under which notice and exit terms? | Named register, data scope, region, and approval record. |
| Export and exit | Can each tenant export its records and audit history in a usable format, with deletion and handover steps? | Export sample, deletion/retention runbook, and acceptance owner. |
| Incident and recovery | What happens after an isolation, integration, availability, or data-integrity failure? | Incident route, recovery objective supplied by the buyer, and exercise evidence if available. |

## Evidence record

Every answer should point to an evidence record with at least:

`evidence_id`, `claim`, `source_ids`, `source_scope`, `source_version`, `publication_or_revision_date`, `access_date`, `verification_date`, `freshness_class`, `review_date`, `support_status`, `uncertainty`, `owner`, `reviewer`, `data_scope`, `rights_or_access_basis`, and `evidence_location`.

Use the Digital Research source-verification semantic states: `supported`, `partial`, `inference`, `unsupported`, `no-source`, or `NOT_ASSESSED`. Use `DENIED` when the supplier or buyer has explicitly withheld the evidence or access. `DENIED` is an observed access state, not proof that the control fails or passes.

`source_ids` must be a list. Use an empty list only for `no-source`; all other states require a known source ID. A source being reachable does not prove that it supports the claim.

## Minimum negative and recovery cases

Retain a case ID, input scope, expected result, observed result, evidence IDs, reviewer, and review date.

| Case | Expected result | Release consequence |
|---|---|---|
| Wrong-tenant read | Denied and logged; no record or metadata from another tenant is returned. | Any observed cross-tenant data is a release blocker. |
| Wrong-tenant write | Denied and logged; no record is created or changed in another tenant. | Any cross-tenant mutation is a release blocker. |
| Duplicate integration event | Idempotent handling or an explicit reconciliation hold; no silent duplicate. | Missing duplicate rule blocks the integration answer. |
| Interrupted transfer | Resume or reconcile without loss, duplication, or silent partial success. | A test not run is `NOT_ASSESSED`. |
| Tenant export and exit | Export is attributable to the tenant and includes the agreed records and audit data. | Missing scope or owner blocks the exit answer. |

The independent oracle is a named security or architecture reviewer who can inspect the fixture or test evidence without relying on the supplier's prose. A proposal team may describe the oracle and acceptance threshold; it may not sign the buyer's production certification.

## Currentness and reviewer boundary

This reference makes `NO_TIME_SENSITIVE_CLAIMS`: it provides a durable question and evidence structure, not a current law, standard, product feature, or clinical rule. Any such claim must carry source scope, publication or revision date, access date, verification date, freshness class, review date, support status, uncertainty, confidence, and owner. A missing current source or reviewer remains `NOT_ASSESSED`.

Required human review is role-based:

- security or solution architecture reviewer: tenant boundary, identity, logging, integration and recovery evidence;
- privacy or legal reviewer: data scope, residency, retention, subprocessors and exit terms; and
- buyer-authorised owner: acceptance, risk disposition, and any contractual commitment.

The proposal engine can assemble the evidence map and draft qualified questions. It cannot approve a vendor, certify isolation, accept a subprocessor, or make a clinical or statutory assurance.

## Synthetic example

For a fixture only: `wrong-tenant-read-01` has expected result `deny`, observed result `deny`, state `supported`, and an evidence ID that points to the fixture assertion and the independent reviewer. Label all such records `FICTIONAL TEST DATA`; do not present them as supplier evidence or a penetration test.

