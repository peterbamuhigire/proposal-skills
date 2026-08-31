---
name: civil-society-cyber-resilience
description: Use when writing or reviewing a proposal for NGO or civil-society cybersecurity, digital resilience, incident readiness, or shared protection capacity; use risk-management for generic risk design and the ICT sector profile for technology-sector positioning.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Civil-Society Cyber Resilience
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Build a fundable, mission-aware cyber-resilience response for organisations that
may lack dedicated security staff. The proposal must connect people, mission,
systems, partners, prevention, detection, response, and recovery.

<!-- dual-compat-start -->
## Use When

- An NGO, CSO, research institution, or human-rights organisation needs a cyber-resilience programme.
- A donor wants a proportionate investment case for staff, identity, data, domain, endpoint, and recovery controls.
- The proposal must cover phishing, ransomware, spyware, impersonation, or information manipulation.
- A consortium or shared-service model is needed because the organisation cannot defend itself alone.

## Do Not Use When

- The assignment is a single technical host change; route to the technical delivery owner.
- Attribution, criminal investigation, or legal advice is requested; state the boundary and refer to the authorised authority.
- The proposal needs a generic risk register without a civil-society mission or people-risk context; use `risk-management`.

## Required Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---|---|
| Mission, affected people, programmes, and critical services | NGO leadership and programme owners | Required | Stop the affected harm claim and request the missing context |
| Systems, identities, data, domains, partners, and incident history | Technology and incident owners | Required | Label exposure as unassessed and issue a focused evidence request |
| Current controls and operating evidence | Administrators and service owners | Required | Separate policy from practice and do not claim maturity |
| Budget, staff capacity, and trusted support options | Board, donor, or delivery owner | Conditional | Stage the treatment and record the dependency |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Mission-aware cyber-resilience proposal section or intervention design | Proposal lead and evaluator | Harm, people, systems, controls, partners, and outcomes are connected |
| Phased work plan | Delivery and donor teams | Controls, owners, evidence, training, partners, recovery, and dependencies are staged |
| Monitoring, incident, safeguarding, and sustainability measures | Programme and risk owners | Measures show changed capability and name residual risk |

## Quality Standards

- Protect people and programme continuity, not only infrastructure.
- Prioritise likely high-harm paths and show the evidence that will prove improvement.
- Preserve privacy, dignity, incident evidence, and safe communication.
- Do not promise a tool, certification, or awareness campaign as complete security.
<!-- dual-compat-end -->

## Decision Rules

| Condition | Proposal choice | Failure/risk avoided |
|---|---|---|
| High mission harm and an executable control exists | Fund and stage it with an owner and operating evidence | Spending without reducing material mission harm |
| Control is policy-only | Fund an operating test, training, or managed support before claiming maturity | Confusing written policy with protection |
| Organisation lacks specialist capacity | Include a trusted partner or collective-defence model | An unowned control failing in practice |
| Incident is active or evidence is incomplete | Fund containment, preservation, recovery, and learning before expansion | Reinfection, evidence loss, or unsafe expansion |

## Workflow

1. Establish mission, people, services, data, and decision-makers.
2. Identify threat paths and consequences: phishing, ransomware, spyware,
   impersonation, manipulation, lost access, and third-party failure.
3. Design the treatment across leadership, capacity, identification, protection,
   detection, response, and recovery.
4. Stage delivery with baseline, pilot, operating test, exercise, and re-measure.
5. Specify evidence: control results, staff reporting, recovery time, backup
   integrity, privileged-access review, incident packet, and residual risk.
6. Hand off owners, dependencies, escalation, communications, and sustainability.
   Stop the proposal route when a load-bearing claim cannot be supported; recover
   by revising that claim or returning it to the evidence-request stage.

## Anti-patterns

- Selling a tool before mapping mission harm. Fix: show the attack path, consequence, owner, and evidence.
- Making awareness training the only intervention. Fix: pair training with identity, host, data, backup, and response controls.
- Promising incident prevention. Fix: promise measurable reduction, faster detection, and recoverable operations.
- Hiding limited capacity to appear mature. Fix: fund the partner and operating model that closes the gap.
- Treating donor reporting as security evidence. Fix: retain technical, behavioural, and recovery proof separately.

## Read next

- `risk-management` for general treatment and residual-risk logic.
- `profiles-sectors/sectors/health` for health-sector proposal context.
- `saas-procurement-and-security-questionnaire` for buyer control questions where applicable.
- `change-management` for adoption and operating change.

## References

- [NGO cyber-resilience proposal pack](references/ngo-cyber-resilience-proposal-pack.md)

## Capability Contract

Read and search are required. Proposal drafting is permitted within the authorised
engagement. Do not perform live incident response from this skill.

## Degraded Mode

When threat, control, budget, or impact evidence is missing, label the affected
claim as a hypothesis, mark it not assessed, and issue a focused evidence
request. Return to the affected stage after the evidence is recovered.

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Intervention logic | Proposal lead | Mission harm, treatment, measure, owner, and dependency are linked |
| Resilience work plan | Delivery lead | Prevention, detection, response, recovery, and learning are staged |
| Proposal assurance record | Reviewer and donor | Privacy, safeguarding, uncertainty, and residual risk are visible |

## Worked Example

For a small NGO facing phishing and lost-account risk, propose a named board
owner, MFA and least-privilege rollout, staff reporting, trusted-domain controls,
tested backups, and a partner-supported incident exercise. Stage a baseline,
operating test, recovery exercise, and re-measurement, and withhold any maturity
claim until the evidence packet shows the controls work in practice.
