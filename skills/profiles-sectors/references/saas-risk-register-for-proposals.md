# SaaS Risk Register for Proposals

Risk register specific to SaaS implementation and SaaS product-development engagements. Use inside the Methodology section's risk table and as the basis for the Risk Management section when the ToR requires one.

## How to Use

- Select the entries that apply to the engagement; do not include every entry by default.
- Adjust likelihood and impact to the engagement context.
- Name owners on both sides (agency and client).
- Tie mitigation actions to specific phases of the methodology and the MAP.
- Re-score the register at every steering committee meeting; track residual risk.

## Risk Entries

### Architecture and Platform

| Risk | Likelihood | Impact | Trigger | Mitigation | Owner |
|---|---|---|---|---|---|
| Tenant isolation model incompatible with regulator expectation | M | H | Regulator review or audit finding | Architecture Decision Record in Phase 1; regulator dry-run in Phase 4; isolation upgrade path designed | CTO + DPO |
| Tenant context propagation gap allows cross-tenant access | L | H | Code review or penetration test finding | Tenant-context audit pass in Phase 3; integration tests enforce isolation | Architecture lead |
| Noisy-neighbour incident degrades shared-tier customers | M | M | Tenant usage spike | Per-tenant telemetry from day one; tier-aware throttling; capacity headroom | Reliability lead |
| Performance under realistic multi-tenant load below target | M | H | Load test miss | Load test in Phase 3 with realistic multi-tenant pattern; capacity plan | Reliability lead |
| Data partitioning model creates hot-spot at scale | M | M | Storage performance degradation | Partition-key design review in Phase 1; load test in Phase 3 | Architecture lead |

### Data and Privacy

| Risk | Likelihood | Impact | Trigger | Mitigation | Owner |
|---|---|---|---|---|---|
| Data residency requirement changes mid-engagement | M | H | Regulator update | Multi-region design from Phase 1; residency map in DPA | DPO |
| Sub-processor change rejected by client | L | M | Sub-processor swap notification | Notice and objection protocol in MSA / DPA; backup sub-processor identified | Legal + Solution lead |
| Data migration produces reconciliation breaks | M | H | Parallel-run reconciliation gap | Tenant-by-tenant migration; daily reconciliation; rollback plan | Data lead |
| Personal data breach in a sub-processor | L | H | Sub-processor incident | Contractual flow-down of obligations; incident notification protocol | CISO |
| Lawful basis for processing challenged by data subject | L | M | DSAR or complaint | Lawful basis recorded in DPA Annex; DSAR runbook | DPO |

### Commercial and Procurement

| Risk | Likelihood | Impact | Trigger | Mitigation | Owner |
|---|---|---|---|---|---|
| Procurement adds new evaluation criteria mid-process | M | M | Clarification or addendum | Written clarification request; recompute compliance | Bid manager |
| BAFO requires deeper discount than sustainable | M | M | Procurement-led BAFO | Trade options prepared (scope, term, payment); no pure discount | Account director |
| Sponsor changes before contract signature | M | H | Departure or reorganisation | Account map maintained; secondary sponsor identified | Account director |
| Withholding tax or currency rule changes the commercial model | L | M | Tax authority guidance | Tax clause in MSA; payment-on-net protection | Finance lead |
| Renewal not secured at end of initial term | M | H | Sponsor change, dissatisfaction, competitive entry | Customer-success engagement; renewal proposal 90 days out | Account director |

### Security and Compliance

| Risk | Likelihood | Impact | Trigger | Mitigation | Owner |
|---|---|---|---|---|---|
| Security questionnaire pass takes longer than projected | M | M | Slow CISO review cycle | Pre-emptive security questionnaire pack; CISO briefing | Solution lead |
| Penetration test finds material vulnerability close to go-live | M | H | Pen-test report | Pen-test in Phase 4 with 4-week remediation window; severity-based SLA | Security lead |
| Compliance certification not inherited from cloud provider | L | M | Buyer asks for evidence | Certification scope confirmed in Phase 1; remediation plan | CISO |
| Incident response runbook untested at go-live | L | H | Real incident exposes gaps | DR test in Phase 4; incident response tabletop | Reliability lead |

### Adoption and Change

| Risk | Likelihood | Impact | Trigger | Mitigation | Owner |
|---|---|---|---|---|---|
| Active-user adoption below threshold at 60 days | M | H | Adoption dashboard miss | Lifecycle communications live from go-live; customer-success engagement intense | CSM |
| Frontline resistance from displaced workflow | M | M | Frontline survey, complaint volume | Change-management workstream; champion network; training waves | Change lead |
| Sponsor disengages after go-live | M | M | Sponsor missing two QBRs | Executive sponsor outreach; revised success plan | Account director + Managing partner |
| Operating model not adopted (per-tenant operations, continuous release) | M | M | Operations behaving as install-services | Mindset workstream; OCM measurement; senior coaching | Change lead + CTO |

### Vendor and Operating

| Risk | Likelihood | Impact | Trigger | Mitigation | Owner |
|---|---|---|---|---|---|
| Cloud provider outage affects service availability | L | M | Cloud incident | Multi-AZ design; tier-appropriate DR; status comms | Reliability lead |
| Third-party API or data provider deprecation | M | M | Provider notice | Abstraction layer; backup provider; deprecation playbook | Architecture lead |
| Key staff loss on agency side mid-engagement | M | M | Resignation | Two-of-everything; cross-training; documented runbooks | Delivery lead |
| Currency / FX exposure in multi-region pricing | L | M | FX move | Currency clause in commercial model; quarterly review | Finance lead |

### Exit and Lock-In

| Risk | Likelihood | Impact | Trigger | Mitigation | Owner |
|---|---|---|---|---|---|
| Client perceives vendor lock-in | M | M | Procurement or board question | Exit clause in MSA; data-return commitment; escrow for custom configurations | Account director + Legal |
| Termination dispute on data return | L | H | Termination notice | DPA includes data-return format, timeline, deletion certificate | Legal + DPO |
| Custom configurations not portable | M | M | Discovery during exit planning | Configuration documentation; standards-based config formats | Solution lead |

## Risk Scoring Convention

- L (Low): probability ≤ 10% over the engagement window or 10% annual post-go-live.
- M (Medium): probability 10–40%.
- H (High): probability ≥ 40%.
- Impact bands tuned to the engagement value: financial, reputational, regulatory, operational.

## Anti-Patterns

- A risk register with no owner per risk — there is no risk register, only a list.
- Risks scored once and never re-scored as new information arrives.
- Mitigation actions with no link to a specific phase or MAP step.
- "We will manage" as a mitigation — not specific enough to defend.
- Hiding regulator-related risks because they are uncomfortable — they always surface during review.

## See Also

- `saas-implementation-methodology-blocks.md` for phase placement of mitigation actions.
- `saas-procurement-and-security-questionnaire-playbook.md` for security and compliance risks.
- `saas-msa-dpa-sla-template-language.md` for contractual mitigations.
- `saas-customer-success-engagement-package.md` for adoption mitigations.
- `saas-mutual-action-plan-template.md` for the MAP that turns mitigation into dated tasks.
- `../risk-management/SKILL.md` for the risk-management skill itself.
