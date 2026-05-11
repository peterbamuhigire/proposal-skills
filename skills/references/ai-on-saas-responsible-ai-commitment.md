# AI-on-SaaS Responsible AI Commitment

Section template for the Responsible-AI commitment in an AI-on-SaaS proposal. Pairs with `ai-on-saas-risk-and-responsible-ai`. The commitment is a section of the proposal, signed by a named accountable role, anchored in the methodology.

## Why a Commitment Rather than Principles

Generic Responsible-AI principles (accountability, transparency, fairness) are universally agreed and universally unevidenced. The commitment converts the principles into engineered controls, named owners, measurement methods, and escalation paths the buyer's auditor can verify.

## Section Structure

### 1. Scope
- Which AI features the commitment covers (named).
- Which features are out of scope (named, with rationale).
- Which jurisdictions the commitment applies to (EU, KE, NG, ZA, UG, RW, US).
- The duration (engagement length plus a post-engagement support window).

### 2. Principles
Stated briefly, then immediately operationalised:

- **Accountability** — a named role, escalation path, governance cadence.
- **Transparency** — model cards, sub-processor list, eval methodology, incident disclosure.
- **Fairness** — fairness metric per feature where the use case touches a protected class; mitigation when breached.
- **Safety** — hallucination SLO, abstain logic, red-team harness.
- **Privacy** — data minimisation, retention, deletion, training-exclusion.
- **Human oversight** — HITL design per feature with named human authority.
- **Redress** — affected-party redress mechanism with response SLA.

### 3. Governance Forum
- **Body**: AI Governance Forum.
- **Parties**: Buyer-side AI Safety Sponsor, Agency-side AI Safety Lead, Buyer DPO, Buyer CISO, Buyer product owner, Agency engagement lead. Optional: regulator observer.
- **Cadence**: Monthly during build; quarterly thereafter; ad-hoc for incidents.
- **Decisions**: Eval threshold changes; model approval / deprecation; sub-processor changes; incident outcomes; sign-off on quarterly Responsible-AI report.
- **Records**: Decisions minuted; retention for the engagement life plus three years.

### 4. Accountable Role
- **Role**: AI Safety Lead.
- **Owner**: Named individual on the agency side.
- **Buyer-side counterpart**: Named individual on the buyer side; trained-up under the two-of-everything rule by go-live.
- **Authority**: Approve / refuse model deployments; trigger rollback; sign quarterly report.
- **Escalation**: To the SteerCo; to the General Counsel for legal events; to the regulator liaison for regulatory events.

### 5. Eval Discipline (Operationalised)
- Golden datasets per feature, signed off by buyer SME.
- Metric thresholds per feature, signed off by SteerCo.
- Eval CI gate — threshold breach blocks deploy.
- Drift watch in production — daily for high-stakes features, weekly for others.
- Monthly eval refresh; quarterly golden-set refresh.

### 6. Transparency Commitments
- **Model cards** published per AI feature with: training-data summary, intended use, evaluation summary, limitations, risks, contact.
- **Sub-processor list** published, with notice to the buyer on changes (typically 30 days).
- **Eval methodology** described, with refresh cadence and metric definitions visible to the buyer's auditor on request.
- **Incident disclosure policy** — disclose to the buyer within 24 hours of agency awareness; disclose to affected users per the regulator timeline.

### 7. Redress Mechanism
- Channel for affected users (in-app + dedicated email + escalation phone).
- SLA: first response 1 business day; resolution target by severity.
- Named owner.
- Quarterly redress-log review at the AI Governance Forum.

### 8. Sign-Off Frequency
- Quarterly Responsible-AI report signed by the AI Safety Lead, received by the SteerCo.
- Annual SteerCo-level Responsible-AI declaration to the buyer's board.
- On-incident report within the timelines above.

## Sample Paragraph for the Proposal — Opening of the Commitment

> Our Responsible-AI commitment is the engineered counterpart to the principles every party agrees to in the abstract. Across the AI features in this engagement, we operate under a named AI Safety Lead, an AI Governance Forum chaired jointly with the Customer's nominated AI Safety Sponsor, an eval discipline that gates deploys on numeric thresholds, a sub-processor disclosure refreshed quarterly, a hallucination SLO measured monthly, a red-team cadence on a quarterly scorecard, and a redress mechanism with a published SLA. The commitment is not a marketing document. It is an auditable obligation under the engagement letter, with the controls visible to the Customer's auditor on request, and the failure modes connected to the methodology, the risk register, and the trust and compliance section of this proposal.

## Regulator Mapping — Sample Block

| Regulator / standard | Coverage in this commitment |
|---|---|
| EU AI Act (Articles 9, 10, 13, 14, 15 — where applicable to high-risk classification) | Risk-management system; data governance; logging; transparency; human oversight |
| Kenya NCAIS principles | Accountability, transparency, fairness, privacy mapped to commitment sections |
| Nigeria NAIS | Sectoral application stated; data-protection interface with NDPA |
| South Africa AI policy (draft) | Principles addressed; sovereignty option offered |
| Uganda NITA-U AI guidance | Principles addressed; DPPA interface stated |
| Rwanda AI Policy | Principles addressed; sectoral application stated |
| ISO 42001 / ISO 23894 | Alignment statement with gap pack on request |
| NIST AI RMF | Govern / Map / Measure / Manage functions cross-referenced |

## Cross-References

- `ai-on-saas-risk-register-for-proposals.md` — risk register the commitment mitigates.
- `ai-on-saas-trust-and-compliance-section-template.md` — trust section that contains a summary of this commitment.
- `ai-on-saas-procurement-questionnaire-pack.md` — answers consistent with this commitment.
- `ai-on-saas-methodology-blocks.md` — methodology that operationalises this commitment.
