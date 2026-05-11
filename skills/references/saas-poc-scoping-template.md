# SaaS Proof-of-Concept and Pilot Scoping Template

Tight POC and pilot scoping for SaaS implementation engagements. Used inside the proposal's Methodology and Work Plan when the buyer requires evidence before committing to a full implementation.

## POC vs Pilot — When Each Applies

| Stage | Purpose | Duration | Population | Decision at Exit |
|---|---|---|---|---|
| Discovery POC | Test a single risk hypothesis (integration feasibility, performance, regulator stance) before scoping the full implementation. | 2–6 weeks | Single workflow or interface in a sandbox. | Proceed to full proposal / re-scope / no-fit. |
| Technical POC | Validate the SaaS works in the buyer's actual technical environment under realistic load. | 4–8 weeks | Sandbox connected to a copy of production data; non-production users. | Sign full implementation contract / negotiate scope. |
| Pilot | Run the SaaS in production for a defined cohort to validate adoption, value, and operating model. | 8–16 weeks | A specific branch, region, business unit, or customer cohort. | Go / no-go to full rollout / extend pilot / abandon. |

## Scope Rules

- One POC, one risk hypothesis. POCs that try to prove three things prove none.
- Pilots have a named cohort with a named owner. Pilots without a named owner are not pilots; they are uncontrolled production rollouts.
- Both POC and pilot have written exit criteria with binary pass/fail logic.
- Both have a time-box that everyone in the room agrees to before kick-off.

## POC Scoping Block (for inclusion in proposal Methodology)

### POC Purpose
State the single risk hypothesis the POC will test. Examples:

- "Can the SaaS integrate with the core banking system within the latency and reconciliation tolerance the operations team requires?"
- "Does the tenant isolation model meet the regulator's expectation for data segregation in this jurisdiction?"
- "Can the model-driven configuration handle the policy-product variation across the insurer's three business lines?"

### POC Scope (Included)
- Specific workflow(s) to exercise.
- Specific integration(s) to test.
- Specific users to involve (named or roles).
- Specific data to use (de-identified, synthetic, or production-copy with masking).

### POC Out of Scope (Explicit)
- Production data, production users, production traffic.
- Custom development beyond configuration.
- Other workflows, other integrations, other regulators.
- Performance testing beyond the agreed scope.
- Security and compliance certification beyond what already exists.

### POC Success Criteria

| # | Criterion | Measurement | Pass Threshold |
|---|---|---|---|
| 1 | Integration round-trip | Average latency over 1,000 test transactions | ≤ 2 seconds |
| 2 | Reconciliation accuracy | Reconciliation breaks over 7-day test window | ≤ 0.1% |
| 3 | User acceptance | Survey of 12 pilot users on usability and trust | ≥ 4/5 mean |
| 4 | Regulator dry-run | Compliance reviewer assessment against checklist | Pass |

### POC Exit Criteria (Binary)
- All success-criteria thresholds met → proceed to full implementation contract.
- Any threshold missed by ≤ 20% → re-scope, identify mitigation, re-run for an agreed extension.
- Any threshold missed by > 20% → no-fit, debrief, capture lessons.

### POC Timeline (Time-Boxed)
| Week | Activity | Deliverable |
|---|---|---|
| 1 | Kick-off, environment setup, test-data preparation | POC plan signed, environment ready |
| 2 | Integration build, configuration walkthrough | Configuration approved |
| 3 | Test execution, defect capture, user sessions | Daily test reports |
| 4 | Results compilation, success-criteria scoring, debrief | POC report and go/no-go decision |

### POC Team and Effort
| Role | Agency | Buyer |
|---|---|---|
| Solution lead | 0.5 FTE for 4 weeks | — |
| Integration engineer | 1.0 FTE for 3 weeks | 0.5 FTE for 3 weeks |
| Domain SME | 0.25 FTE | 0.5 FTE for 2 weeks |
| Test users | — | 12 named users for 1 week |
| Sponsor | 0.1 FTE | 0.2 FTE for 4 weeks |

### POC Commercial Block
- Fixed fee, payable in two tranches: 50% on POC plan signature, 50% on POC report acceptance.
- Fee is creditable against the full implementation fee if the buyer proceeds within 90 days of POC completion.
- POC fee is not refundable if the POC succeeds but the buyer does not proceed for non-POC reasons.

## Pilot Scoping Block (for inclusion in proposal Methodology)

### Pilot Purpose
State the adoption, value, and operating-model hypotheses the pilot will validate.

### Pilot Cohort
- Named cohort: which branch, region, business unit, customer segment.
- Cohort size: number of users, customers, transactions.
- Cohort representativeness: why this cohort is a fair predictor of full rollout.

### Pilot Success Criteria
- **Adoption metrics**: active-user rate, feature-adoption rate, time-to-first-value.
- **Value metrics**: target metric uplift vs baseline (with confidence interval where measurable).
- **Operating metrics**: support tickets per active user, mean time to resolve, escalation rate.
- **Risk metrics**: defect rate, security incidents, regulator concerns raised.

### Pilot Operating Model
- Dedicated pilot owner from the buyer side, named in the contract.
- Dedicated customer-success lead from the agency, named in the contract.
- Weekly pilot review, monthly steering review.
- A clear "stop the pilot" trigger if a risk metric breaches threshold.

### Pilot Exit Decision
- **Go** — all success criteria met, operating model proven, proceed to full rollout.
- **Extend** — most criteria met, one or two need more data; agreed extension with revised criteria.
- **Abandon** — material miss on adoption or value; structured debrief; partial credit applied.

### Pilot Commercial Block
- Pilot fee distinct from implementation fee.
- Pilot fee may be creditable against full rollout fee on a defined schedule.
- Pilot fee includes the customer-success engagement for the pilot cohort, not separately priced.

## Anti-Patterns

- "Free POC" — destroys the trade discipline; either the POC is valuable enough to be paid or it should not happen.
- POC with no exit criteria — becomes an open-ended sandbox.
- Pilot that quietly becomes the full rollout — undermines decision-gate discipline.
- Pilot success criteria written by the agency alone — must be co-authored with the buyer's owner.
- Pilot run on a non-representative cohort — produces misleading evidence.

## See Also

- `saas-demo-script-template.md` for the demo that precedes the POC.
- `saas-mutual-action-plan-template.md` for placement in the MAP.
- `saas-business-case-and-roi-template.md` for the value case the pilot validates.
- `saas-implementation-methodology-blocks.md` for full-implementation methodology after pilot success.
