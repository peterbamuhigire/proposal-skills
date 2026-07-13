---
name: risk-management
description: Use when a proposal requires risk identification, scoring, ownership, treatment, monitoring, or a risk register. Unlike project-management, this skill develops the assignment risk model and response thresholds rather than the full governance system.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Risk Management
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When
- Use this skill when the assignment explicitly needs risk-management, mitigation, contingency, or escalation content.
- Load it when another proposal section needs this domain expertise.

## Do Not Use When
- The task only needs formatting or proposer-profile selection.
- Another supporting skill is a closer fit for the assignment.

## Required Inputs
| Artefact | Source | Required? | If absent |
|---|---|---|---|
| Scope, assumptions, dependencies, constraints, and risk appetite | ToR and delivery plan | required | Return a risk-discovery plan rather than a generic register. |
| Existing incidents and control evidence | Client records and verified research | conditional | Mark likelihood and residual risk provisional. |

## Workflow

Stop or block the workflow when a required input, permission, or acceptance basis is missing. Recover by revising the scope, obtaining evidence, or returning the narrowest qualified draft before proceeding.
1. Identify where risk-management logic matters in the assignment.
2. Separate actual delivery risks from evaluator objections so both are answered properly.
3. Read the local references only where they materially improve the output.
4. Convert the guidance into proposal-ready risks, controls, and response mechanisms.
5. Integrate the result into the target section and check for consistency.

## Quality Standards
- Translate risk frameworks into practical proposal language, scoring, and mitigation logic.
- Keep the approach specific to the client context and implementation reality.
- Preserve compatibility with existing repository workflows and file paths.

## Anti-Patterns
- Copying a generic risk list. Fix: tie cause, event, impact, and response to the assignment.
- Calling an issue a risk. Fix: track occurred events as issues with recovery actions.
- Giving every risk a medium score. Fix: define scales and justify ratings from evidence.
- Naming mitigation without an owner or trigger. Fix: assign ownership, due date, indicator, and contingency.
- Hiding risk to sound confident. Fix: state material uncertainty and the decision it affects.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Risk management plan and register | Evaluator, project manager, risk owners | Each material risk has cause, event, impact, score, owner, treatment, trigger, contingency, and review date. |

## Evidence Produced
| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Scored risk register and treatment trace | Versioned table | Ratings use declared scales and residual risk reflects evidenced controls. |

## Capability and Permission Boundaries

Read and search are required; any edit or external action remains within the explicit authority and permission boundary stated below.
Risk review is read-only by default. Editing the register requires authority; accepting risk, spending contingency, changing scope, or executing recovery requires the named owner.

## Degraded Mode
Without incident, control, or stakeholder evidence, provide a provisional risk hypothesis register and evidence requests. Do not report residual risk as assessed.

## Decision Rules
| State | Action | Risk avoided |
|---|---|---|
| Threat has not occurred | Track as risk with trigger | Confusing prevention and recovery |
| Event has occurred | Move to issue and activate response | Passive monitoring |
| Residual exposure exceeds appetite | Escalate, redesign, transfer, or stop | Unauthorised acceptance |

## Worked Example
For delayed client data, record the dependency, early-warning date, responsible client owner, schedule effect, fallback sample, and escalation threshold instead of writing only “data delays”.

## SaaS-Specific Risks

For SaaS implementation and SaaS product-development engagements, the standard risk categories must include SaaS-specific entries: tenant isolation failure, noisy-neighbour, data residency change, sub-processor rejection, data-migration reconciliation breaks, regulator stance shift, sponsor change before signature, BAFO pressure, security questionnaire pass time, penetration test late finding, adoption miss at 60 days, operating-model not adopted, cloud-provider outage, exit-clause dispute, custom-configuration portability. Reference `../references/saas-risk-register-for-proposals.md` for the full register.

## AI-on-SaaS Risks

For engagements that build AI features into a multi-tenant SaaS, layer the ten-entry AI risk register on top of the SaaS register: model risk, hallucination liability, prompt injection, data leakage into model providers, sub-processor exposure (model providers), regulatory shift (AI Act, NCAIS, NAIS, sectoral), vendor lock-in to a single model family, training-data contamination, drift (eval / performance / cost), and reputational. Each entry carries trigger, mitigation, owner, escalation. Reference `../references/ai-on-saas-risk-register-for-proposals.md` for the full register and `../ai-on-saas-risk-and-responsible-ai/SKILL.md` for the companion skill (risk register + Responsible-AI commitment).

## AI-Agent Risks

For agentic engagements (LLM systems that plan, call tools, decide, and act on the buyer's behalf), use the twelve-entry agent risk register from `../references/ai-agent-risk-register-for-proposals.md` and the companion skill `../ai-agent-risk-and-responsible-ai/SKILL.md`. The agent register adds: autonomy-action incident; irreversibility incident; accountability dispute; scope-creep; multi-agent collusion / failure cascade; prompt injection via tool output; memory poisoning; regulator action on agentic system; kill-switch failure; identity / impersonation breach; escalation overload; legacy-system damage. Mitigations are anchored in the action catalogue, autonomy commitment, kill-switch architecture with quarterly drill, action audit log with 99 % completeness SLA, and the Responsible-AI Agent Commitment with a named Agent Safety Lead.

<!-- dual-compat-end -->

## References

- [Proposal skills router](../../SKILL.md) for repository-wide routing and mandatory quality gates.
- Local `references/` files when detailed frameworks or examples are needed.
- [../references/proposal-objection-handling.md](../../profiles-sectors/references/proposal-objection-handling.md) for price, risk, timeline, staffing, technology, local-context, support, AI, and procurement concerns.
- [../references/ethical-persuasion-and-evaluator-psychology-gate.md](../../profiles-sectors/references/ethical-persuasion-and-evaluator-psychology-gate.md) for risk perception and ethical risk framing.
- [../references/technical-strategy-credibility-checklist.md](../../profiles-sectors/references/technical-strategy-credibility-checklist.md) for technical, SaaS, AI, software, cloud, API, operations, and maintainability risks.
- [../references/saas-risk-register-for-proposals.md](../../profiles-sectors/references/saas-risk-register-for-proposals.md) for the SaaS-specific risk register (architecture, data, commercial, security, adoption, vendor, exit).
- [../references/saas-procurement-and-security-questionnaire-playbook.md](../../profiles-sectors/references/saas-procurement-and-security-questionnaire-playbook.md) for security and compliance risks.
- [../references/saas-msa-dpa-sla-template-language.md](../../profiles-sectors/references/saas-msa-dpa-sla-template-language.md) for contractual mitigations.
- [../references/ai-on-saas-risk-register-for-proposals.md](../../profiles-sectors/references/ai-on-saas-risk-register-for-proposals.md) for the AI-on-SaaS risk register.
- [../references/ai-on-saas-responsible-ai-commitment.md](../../profiles-sectors/references/ai-on-saas-responsible-ai-commitment.md) for the Responsible-AI commitment that pairs with the AI risk register.
- [../references/ai-agent-risk-register-for-proposals.md](../../profiles-sectors/references/ai-agent-risk-register-for-proposals.md) for the agent risk register (twelve entries).
- [../references/ai-agent-responsible-ai-commitment.md](../../profiles-sectors/references/ai-agent-responsible-ai-commitment.md) for the Responsible-AI Agent Commitment.

A strong risk section demonstrates that the firm has thought beyond the ideal scenario. Proposals that identify specific, credible risks — and propose practical mitigations — show maturity and experience. Generic risk tables ("risk: delays; mitigation: monitor closely") signal that the firm has not thought deeply about the assignment.

## When to Read This Skill

- Every proposal methodology section includes a risk subsection — always read this skill
- The ToR mentions "risk management", "risk register", "risk assessment", or "risk mitigation"
- The assignment has significant complexity, dependencies, or political sensitivity
- When the ToR asks for a standalone risk management plan

## Risk Identification

### Categories of Risk

| Category | Examples |
|---|---|
| **Technical** | System integration failures, data quality issues, technology obsolescence, scope creep |
| **Operational** | Staff turnover (client or consultant side), logistics failures, connectivity issues, venue unavailability |
| **Institutional** | Political changes, leadership turnover, restructuring during the assignment, inter-departmental conflicts |
| **Financial** | Currency fluctuation, budget cuts, delayed payments affecting delivery |
| **Stakeholder** | Resistance to change, low participation in consultations, competing priorities |
| **External** | Regulatory changes, election periods, public health emergencies, security situations |
| **Data and privacy** | Data breaches, non-compliance with data protection law, inadequate consent processes |
| **Environmental** | Weather disruptions to fieldwork, environmental permit delays |

### Risk Identification Methods

- Review of the ToR for stated constraints, dependencies, and assumptions
- Lessons learned from comparable past assignments
- Stakeholder analysis — which stakeholders may resist or create obstacles
- Environmental scan — political calendar, security situation, seasonal factors
- Technical assessment — integration complexity, data availability, infrastructure readiness

## Risk Assessment

### Likelihood and Impact Matrix

| | Low Impact | Medium Impact | High Impact |
|---|---|---|---|
| **High Likelihood** | Medium risk | High risk | Critical risk |
| **Medium Likelihood** | Low risk | Medium risk | High risk |
| **Low Likelihood** | Low risk | Low risk | Medium risk |

### Scoring

| Score | Likelihood | Impact |
|---|---|---|
| 1 — Low | Unlikely to occur | Minor delay or cost, easily managed |
| 2 — Medium | May occur during the assignment | Noticeable delay, quality impact, or cost overrun |
| 3 — High | Likely to occur | Significant delay, deliverable failure, or budget overrun |

## Risk Register

The standard format for proposal risk tables:

| # | Risk | Category | L | I | Score | Mitigation | Owner |
|---|---|---|---|---|---|---|---|
| 1 | Key client staff reassigned during assignment | Institutional | 2 | 3 | 6 | Secure commitment from Permanent Secretary; document all knowledge transfer; maintain relationship with successor | Team Leader |
| 2 | Poor internet connectivity at field sites | Technical | 3 | 2 | 6 | Use offline-capable data collection tools; pre-download all materials; test connectivity before fieldwork | Technical Lead |
| 3 | Low attendance at stakeholder workshops | Stakeholder | 2 | 2 | 4 | Early engagement with department heads; send invitations through client leadership; offer flexible scheduling | Engagement Lead |

### Risk Register Rules

- Include five to ten risks — fewer looks superficial, more becomes unmanageable
- Every risk must have a specific mitigation action — not "monitor and manage"
- Every risk must have an owner — a named role on the team
- Risks must be specific to this assignment — not generic consulting risks
- Include at least one risk per major category relevant to the assignment
- Score risks honestly — a proposal with no high risks looks naive

## Risk Monitoring and Reporting

Propose how risks will be tracked during implementation:

- Risk register reviewed and updated at every team meeting (weekly)
- New risks added as they emerge
- Risk status reported in monthly progress reports
- Critical risks escalated to steering committee immediately
- Risk register is a living document — shared with the client throughout

## Common East African Consulting Risks

These are frequently relevant and can be adapted to specific assignments:

| Risk | Context | Typical Mitigation |
|---|---|---|
| Election period disruption | Government clients become unavailable during campaign and transition periods | Schedule intensive fieldwork outside election windows; build buffer into timeline |
| Delayed client approvals | Sign-off processes in government can take weeks | Define approval timeframes in inception; escalation path via steering committee |
| Staff transfers | Government staff frequently transferred between postings | Transfer knowledge to roles (not just individuals); maintain documentation |
| Procurement delays | Equipment, venues, or sub-contracts delayed by procurement rules | Start procurement processes early; identify alternative suppliers |
| Currency fluctuation | Assignments quoted in local currency but with USD-denominated costs | Quote in stable currency where possible; include exchange rate assumption and adjustment clause |
| Data unavailability | Expected baseline data does not exist or is unreliable | Plan for primary data collection as contingency; state data assumptions in inception report |

### Project Shock Management
Based on Wickham's framework, consulting projects routinely face shocks that threaten delivery. Common shock types in East African development consulting:

| Shock Type | Examples |
|---|---|
| **Changes in client interests** | Government reshuffle, policy change, donor reprioritisation, election cycle |
| **Changes in project context** | Conflict, drought, pandemic, economic shock, currency devaluation |
| **Budget cuts** | Mid-project budget revision by donor, exchange rate losses |
| **Loss of key people** | Government counterpart transfers, consultant illness, high staff turnover in partner organisations |
| **Misinterpretation of information** | Baseline data errors, population estimates, market size assumptions |
| **Scope creep** | Client expanding expectations beyond the ToR without adjusting timeline or budget |

**Response Protocol:**
1. **Refer back to objectives** — many shocks affect tasks but not the overall aim
2. **Evaluate resource implications** — what does the shock cost in time, money, or quality?
3. **Modify plans accordingly** — adjust methodology, timeline, or deliverables
4. **Communicate proactively** — never hide problems; present problems alongside proposed solutions

**Proposal application:** Include a "Risk and Mitigation" subsection in the methodology or work plan that identifies 3-5 likely project risks with specific mitigation strategies. This signals experience and preparedness.

**Crisis communication rule** (Wickham): "When communicating a problem, try to communicate its solution as well."

## Quantitative Risk Assessment (Advanced)

For complex assignments or clients that expect quantitative rigour, use the FMEA-based Risk Priority Number:

```
RPN = Probability (1-10) × Severity (1-10) × Detection (1-10)
```

**Critical severity rule:** Regardless of the RPN value, when severity is 8-10, you MUST take action. Never ignore high-severity risks even when probability is low.

### Five Risk Response Strategies (Lewis)

1. **Avoidance** — eliminate the risk entirely (best option when feasible)
2. **Mitigation** — reduce probability or impact
3. **Transfer** — shift to another party (insurance, fixed-price subcontracts)
4. **Acceptance** — knowingly live with the risk (low RPN only)
5. **Ignore** — never appropriate in professional consulting

### Dual Assessment Points

Risk assessment occurs at TWO points: strategic-level (can the approach succeed?) and implementation-level (what could go wrong at the task level?). Show evaluators that risk management is embedded in the methodology, not bolted on.

## Reference Library

| Reference File | Contents |
|---|---|
| `references/risk-quantification-and-response.md` | FMEA-based RPN scoring (complete P/S/D tables with 10-point scales), five risk response strategies, risk budget calculation (√ formula), ALARP method, riskograph (visual assessment), risk categories for consulting, costing risk (the vagueness problem), buffer scheduling for risk management, dual assessment points, schedule contingency approaches |

Read the reference file when:
- The assignment requires quantitative risk assessment beyond the standard likelihood-impact matrix
- The financial proposal needs a risk-adjusted contingency calculation
- The client expects FMEA or similar industrial risk methods
- Writing a standalone risk management plan

## Generating a Standalone Section

When the ToR asks for a dedicated risk management plan, generate a document covering:

1. Risk management approach and methodology
2. Risk identification (categories, methods)
3. Risk assessment framework (likelihood, impact, scoring — or RPN for complex assignments)
4. Risk register (complete table with all identified risks)
5. Risk monitoring and reporting process
6. Risk escalation and decision-making framework
7. Risk appetite statement (what level of risk is acceptable)
8. Contingency planning for critical risks
9. Risk budget calculation (for financial proposals)

Follow east-african-english standards throughout.

