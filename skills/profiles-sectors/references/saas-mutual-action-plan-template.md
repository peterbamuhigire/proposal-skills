# SaaS Mutual Action Plan Template

A Mutual Action Plan (MAP) is a shared, dated, owner-attributed plan from the proposal stage through to go-live. For SaaS implementation engagements it is both a closing artefact (it accelerates the decision because the buyer can see exactly what happens after award) and a delivery artefact (it becomes the joint operating plan with the client).

## When to Include the MAP in a Proposal

- Premium SaaS implementation bids where the buyer values predictability and shared accountability.
- Bids competing against incumbents — the MAP creates a tangible difference between the agency and a vendor who simply "responds to the RFP."
- Public sector and regulated bids where the path through procurement, legal, and security review is itself a risk factor.
- Bids where the buyer has signalled hesitation about "what happens after we sign."

## Where the MAP Lives in the Proposal

- A summary MAP table in the Executive Summary or as an annex to the Work Plan.
- The full MAP as a standalone annex.
- For some procurement frameworks the MAP is presented at the BAFO or oral presentation stage, not in the written submission.

## MAP Structure

Five phases. Each phase has a stated outcome, named owner from each side, dated tasks, and a decision gate.

### Phase 1: Selection and Award

| # | Task | Buyer Owner | Agency Owner | Target Date | Decision Gate |
|---|---|---|---|---|---|
| 1.1 | Clarification questions received and answered | Procurement | Bid manager | T+5 days | Clarifications closed |
| 1.2 | Reference calls completed | Technical evaluator | Account director | T+10 days | References cleared |
| 1.3 | Oral presentation / demo | Evaluation committee | Solution lead + delivery lead | T+15 days | Presentation scored |
| 1.4 | Best and final offer | CFO + procurement | Account director | T+20 days | BAFO submitted |
| 1.5 | Award decision | Steering committee | — | T+25 days | Letter of award |
| 1.6 | Notice to proceed | Legal | Legal | T+30 days | NTP issued |

### Phase 2: Contract, Security, and Mobilisation

| # | Task | Buyer Owner | Agency Owner | Target Date | Decision Gate |
|---|---|---|---|---|---|
| 2.1 | MSA, DPA, SLA review | Legal + DPO | Account director + legal | T+10 days post-award | Redlines closed |
| 2.2 | Security questionnaire and review | CISO + IT security | Solution lead | T+15 days | Security cleared |
| 2.3 | Sub-processor approvals | DPO | Solution lead | T+15 days | Sub-processors registered |
| 2.4 | Contract signature | CEO + General counsel | Managing partner | T+20 days | Contract executed |
| 2.5 | Kick-off and inception | Sponsor + PMO | Delivery lead | T+25 days | Inception report accepted |

### Phase 3: Build and Configure

| # | Task | Buyer Owner | Agency Owner | Target Date | Decision Gate |
|---|---|---|---|---|---|
| 3.1 | Tenant model and isolation decision | CTO + DPO | Architecture lead | Week 2 | Architecture decision record signed |
| 3.2 | Integration discovery (core, IdP, payment, reporting) | Heads of integrated systems | Integration lead | Weeks 3–4 | Integration map approved |
| 3.3 | Data implementation plan (custom fields, events, segments) | Head of data | Data lead | Weeks 4–5 | Data plan approved |
| 3.4 | Configuration walkthrough 1 | Product owner | Configuration lead | Week 6 | Walkthrough 1 sign-off |
| 3.5 | Configuration walkthrough 2 | Product owner | Configuration lead | Week 8 | Walkthrough 2 sign-off |
| 3.6 | UAT entry gate | Test manager | Delivery lead | Week 9 | UAT entry approved |

### Phase 4: Pilot and Cutover

| # | Task | Buyer Owner | Agency Owner | Target Date | Decision Gate |
|---|---|---|---|---|---|
| 4.1 | Pilot cohort selection | Operations head | Delivery lead | Week 10 | Pilot cohort approved |
| 4.2 | Pilot launch | Pilot owner | Delivery lead | Week 11 | Pilot go-live |
| 4.3 | Pilot review at 30 days | Steering committee | Delivery lead | Week 15 | Go / no-go to full rollout |
| 4.4 | Full cutover plan agreed | Operations + IT | Delivery lead | Week 16 | Cutover plan signed |
| 4.5 | Cutover | Operations + IT | Delivery lead + reliability lead | Week 18 | Cutover complete |
| 4.6 | Stabilisation review | Steering committee | Delivery lead | Week 22 | Project closure declared |

### Phase 5: Adoption and Value Realisation

| # | Task | Buyer Owner | Agency Owner | Target Date | Decision Gate |
|---|---|---|---|---|---|
| 5.1 | 30-day adoption review | Sponsor + product owner | Customer success lead | Week 26 | Adoption thresholds met |
| 5.2 | 60-day value review (metrics vs baseline) | CFO + sponsor | Customer success lead | Week 30 | Value targets on track |
| 5.3 | 90-day QBR | Steering committee | Account director | Week 34 | First QBR closed |
| 5.4 | Expansion planning conversation | Sponsor + business owner | Account director | Week 36 | Expansion path agreed |

## Decision Gates and Escalation

Each decision gate names: who decides, on what evidence, and what triggers escalation if the decision slips.

| Gate | Decider | Evidence | Escalation if slipped > 5 working days |
|---|---|---|---|
| Inception report accepted | Sponsor | Inception report, risk register, BRIEF.md | Steering committee |
| Architecture decision record signed | CTO + DPO | ADR document, isolation rationale, residency map | Sponsor + CTO |
| UAT entry approved | Test manager | Test plan, environment readiness, exit criteria from build | Sponsor + steering |
| Pilot go / no-go | Steering committee | Pilot metrics, defect register, user feedback | Sponsor + CEO |
| Cutover plan signed | Operations + IT | Cutover runbook, rollback plan, comms plan | Steering + COO |
| First QBR closed | Steering committee | Adoption metrics, value scorecard, expansion plan | Account director + sponsor |

## Operating Rules

- The MAP is reviewed weekly during the build phase, daily during cutover week, and at QBR cadence after stabilisation.
- A task slipping its date by more than 5 working days triggers a written escalation to the named escalation owner.
- Decision gates are binary: passed, or passed with named risks accepted, or held. "Passed conditionally" is not allowed.
- The buyer and the agency each name one person who owns the MAP from their side. These two people are accountable for keeping it current.

## Anti-Patterns

- A MAP that lists only the agency's tasks — defeats the "mutual" purpose.
- Dates without a named owner on each side.
- Decision gates without named evidence — the gate then becomes a meeting, not a decision.
- Phases without an outcome statement, so the team cannot tell when the phase is done.
- Allowing "passed conditionally" — the conditions become forgotten technical debt.

## How to Customise

- Adjust phase count to match the engagement length: 3 phases for sub-3-month engagements, 5–6 for typical SaaS implementation, 7+ for multi-vertical platform rollouts.
- Adjust decision-gate evidence to procurement framework: World Bank, AfDB, UNDP, and PPDA Uganda have specific documentation rules.
- Add a regulator gate when the vertical requires regulator sign-off (banking, insurance, healthcare, public sector data).

## See Also

- `saas-discovery-question-bank.md` for the inputs to Phase 1 tasks.
- `meddic-and-command-of-message-for-saas.md` for the qualification logic behind the MAP.
- `saas-procurement-and-security-questionnaire-playbook.md` for Phase 2 detail.
- `saas-customer-success-engagement-package.md` for Phase 5 detail.
