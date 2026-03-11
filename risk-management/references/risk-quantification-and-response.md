# Risk Quantification and Response Reference

Synthesised from: Lewis (*Project Planning, Scheduling & Control*, 6th ed.), Bielefeld & Schneider (*Basics Budgeting*, 2014).

This reference provides quantitative risk assessment tools for use in proposal methodology sections, risk management plans, and financial proposals that require risk-adjusted budgeting.

---

## 1. Risk Priority Number (RPN) — FMEA-Based Scoring (Lewis)

The standard industrial method for quantifying risks. Produces a single score that enables objective prioritisation.

```
RPN = Probability (P) × Severity (S) × Detection (D)
```

Each factor scored 1-10. Maximum RPN = 1,000.

### Probability of Occurrence

| Rating | Probability | Possible Rate |
|---|---|---|
| 10 | Very high: almost certain | ≥ 1 in 2 |
| 9 | Very high | 1 in 3 |
| 8 | High: repeated occurrences | 1 in 8 |
| 7 | High | 1 in 20 |
| 6 | Moderate: occasional | 1 in 80 |
| 5 | Moderate | 1 in 400 |
| 4 | Moderate | 1 in 2,000 |
| 3 | Low: relatively few | 1 in 15,000 |
| 2 | Low | 1 in 150,000 |
| 1 | Remote: unlikely | ≤ 1 in 1,500,000 |

### Severity of Effect

| Rating | Effect | Description |
|---|---|---|
| 10 | Hazardous (no warning) | Project severely impacted, possible cancellation, no warning |
| 9 | Hazardous (with warning) | Project severely impacted, possible cancellation, with warning |
| 8 | Very high | Major impact on schedule, budget, or performance |
| 7 | High | Significant impact; deliverable completable but client very dissatisfied |
| 6 | Moderate | Some impact; client dissatisfied |
| 5 | Low | Slight impact; client mildly dissatisfied |
| 4 | Very low | Some impact; client aware |
| 3 | Minor | Small impact; average client aware |
| 2 | Very minor | Impact noticed only by close observers |
| 1 | None | No effect |

### Detection Capability

How likely is it that the risk will be detected before it causes damage?

| Rating | Detection | Description |
|---|---|---|
| 10 | Absolute uncertainty | No known monitoring mechanism |
| 9 | Very remote | Monitoring exists but is unreliable |
| 8 | Remote | Monitoring has low probability of detection |
| 7 | Very low | Monitoring has limited effectiveness |
| 6 | Low | Monitoring may detect the issue |
| 5 | Moderate | Monitoring has reasonable chance of detection |
| 4 | Moderately high | Good monitoring in place |
| 3 | High | Monitoring will likely detect early |
| 2 | Very high | Monitoring will almost certainly detect |
| 1 | Almost certain | Detection is virtually guaranteed |

### Critical Severity Rule

**Regardless of the RPN value, when severity is 8-10, you MUST take action.** Never ignore high-severity risks even when probability is low. The Challenger disaster is the canonical example: low probability but severity = 10.

### RPN Example for a Consulting Assignment

| Risk | P | S | D | RPN | Action Required |
|---|---|---|---|---|---|
| Key client counterpart transferred mid-assignment | 5 | 7 | 6 | 210 | Knowledge transfer to role, not person; maintain documentation |
| Data quality insufficient for analysis | 6 | 8 | 4 | 192 | **Severity ≥ 8 — mandatory action.** Plan primary data collection as fallback |
| Consultant illness during fieldwork | 3 | 6 | 3 | 54 | Backup consultant identified; cross-train on methodology |
| Scope creep from client additions | 7 | 5 | 2 | 70 | Formal change control process; baseline scope in inception report |
| Currency depreciation affects budget | 4 | 7 | 5 | 140 | Quote in stable currency; include exchange rate assumption |

**Proposal application:** Use simplified RPN in risk registers for sophisticated clients. For standard proposals, use the likelihood-impact matrix from the parent SKILL.md but apply the severity override rule.

---

## 2. Five Risk Response Strategies (Lewis)

| Strategy | Description | When to Apply |
|---|---|---|
| **Avoidance** | Eliminate the risk entirely | Feasibility study before commitment; pilot before full rollout; alternative design |
| **Mitigation** | Reduce probability or impact | Second-sourcing procurement; keeping overtime in reserve; backup personnel |
| **Transfer** | Shift risk to another party | Insurance; performance bonds; subcontracting to specialists; fixed-price contracts |
| **Acceptance** | Knowingly live with the risk | Low RPN risks; risks inherent to the context that cannot be avoided |
| **Ignore** | Pretend risk does not exist | **Never appropriate in professional consulting** |

**Avoidance is always the best option when feasible.** Design processes so that errors cannot occur (the Japanese manufacturing principle of "foolproofing").

**Proposal application:** For each risk in the register, state the response strategy explicitly: "Mitigation — we will second-source all critical data collection tools to avoid single-point-of-failure risk."

---

## 3. Risk Budget Calculation (Bielefeld)

For financial proposals that need a quantified contingency line, use the square-root-sum-of-squares method.

### Formula

```
Risk Budget = √(C₁² + C₂² + C₃² + ...)
```

Where C = individual risk cost = Cost Effect × Probability.

### Worked Example

| Risk | Cost Effect | Probability | Risk Cost (C) |
|---|---|---|---|
| Additional field visits required | $12,000 | 30% | $3,600 |
| Key expert replacement recruitment | $8,000 | 15% | $1,200 |
| Extended stakeholder consultation | $6,000 | 40% | $2,400 |
| Equipment failure/replacement | $4,000 | 20% | $800 |

```
Risk Budget = √(3,600² + 1,200² + 2,400² + 800²)
           = √(12,960,000 + 1,440,000 + 5,760,000 + 640,000)
           = √20,800,000
           ≈ $4,561
```

**Why square root, not simple sum?** Simple summing ($8,000) assumes all risks materialise simultaneously — overly conservative. The square-root method accounts for the improbability of all risks co-occurring, producing a statistically reasonable contingency.

**Proposal application:** Use this method to justify contingency amounts in the financial proposal: "The contingency of $4,561 (approximately 5% of professional fees) is calculated using risk-adjusted probability weighting across the four identified cost risks."

---

## 4. ALARP Method — As Low As Reasonably Practicable (Bielefeld)

Limit risk to a tolerable and financially viable level. Balance due diligence expense against potential damage cost.

**Three zones:**
1. **Broadly acceptable** — no measures needed
2. **ALARP zone** — reduce risk as far as reasonably practicable; tolerate residual risk
3. **Intolerable** — must be eliminated before proceeding

**Principle:** Continue investing in risk reduction until the cost of further reduction exceeds the benefit. This is the point of diminishing returns.

**Proposal application:** When clients question risk mitigation costs: "Our risk management approach follows the ALARP principle — we invest in mitigation up to the point where further investment would exceed the potential cost of the risk itself."

---

## 5. Riskograph — Visual Risk Assessment (Bielefeld)

A two-dimensional matrix for visual risk classification.

**X-axis:** Incidence rate (incalculable → improbable → rare → occasional → regular → frequent)

**Y-axis:** Extent of damage (trivial → minor → noticeable → critical → catastrophic)

**Three zones:**
- **Green:** No measures needed
- **Yellow (ALARP):** Reduce as far as reasonably practicable
- **Red:** Must be excluded in advance

**Proposal application:** Use the riskograph in risk management plans for visual communication. Evaluators appreciate visual risk displays that make the assessment accessible to non-technical readers.

---

## 6. Risk Categories for Consulting Assignments (Bielefeld, adapted)

| Category | Examples in Consulting Context |
|---|---|
| **Market risks** | Economic cycle affecting client budgets; donor funding shifts |
| **Business risks** | Key personnel unavailability; subcontractor failure; firm capacity constraints |
| **Data risks** | Missing baseline data; unreliable statistics; inadequate records |
| **Institutional risks** | Staff transfers; political changes; restructuring; inter-departmental conflict |
| **Costing risks** | Early estimates set on insufficient data; quality descriptions too vague; "average quality" left open to interpretation |
| **External risks** | Regulatory changes; election periods; security situations; public health emergencies |

### Costing Risk — The Vagueness Problem

A specific and common risk in consulting budgets: vague scope descriptions ("conduct a comprehensive assessment", "provide capacity building") allow interpretation that can vary by 50% or more in cost. Mitigate by:

1. Defining scope precisely in the inception report
2. Specifying quantities (number of workshops, number of respondents, number of sites)
3. Agreeing unit costs with the client before execution
4. Documenting assumptions explicitly in the financial proposal

---

## 7. Buffer Scheduling for Risk Management (Bielefeld)

Identify cost modules that can serve as buffers if risks materialise. This provides a structured alternative to flat contingency percentages.

### Requirements for Valid Buffers

- Client agreement obtained in advance
- Selected elements must be cost-relevant (meaningful savings potential)
- Contract or commitment for those elements must not yet be finalised
- Alternative delivery approach must still meet the assignment objectives

### Buffer Schedule Template

| Cost Module | Full Specification | Reduced Specification | Saving | Available Until |
|---|---|---|---|---|
| Regional workshops (4 locations) | 4 × 2-day workshops, 30 pax each | 2 workshops + virtual sessions | $8,500 | Week 6 |
| Printed final report (100 copies) | Professional printing and binding | Digital distribution + 10 printed copies | $3,800 | Week 14 |
| International benchmarking | 3-country study visit | Desk-based review + video interviews | $15,000 | Week 4 |
| Stakeholder validation workshop | Full-day conference, 60 pax | Half-day workshop, 25 pax | $4,200 | Week 12 |

**Principle:** Compare risk exposure against available buffers on a timeline. If the total buffer available at any point is less than the risk exposure at that point, the budget has a coverage gap that must be addressed.

---

## 8. Dual Risk Assessment Points (Lewis)

Risk assessment occurs at TWO points in the project lifecycle, not once:

1. **Strategic-level** (early planning): Assess risks to the overall approach. Can the strategy succeed? Are there fundamental obstacles? If risks are unacceptable, revise the strategy.

2. **Implementation-level** (detailed planning): Using the WBS, assess risks at the task level. For each work package: "What could go wrong?" If risks are unacceptable, revise the implementation plan.

**Proposal application:** Show evaluators that risk management is embedded in the methodology, not bolted on: "Risk assessment is conducted at two levels — strategic risks are evaluated during inception and may trigger methodology adjustments; task-level risks are identified during detailed planning using our Work Breakdown Structure and are tracked in the project risk register throughout execution."

---

## 9. Schedule Contingency (Lewis)

Three approaches to building schedule contingency:

1. **Weather/context days:** Build in buffer days based on historical disruption patterns (rainy season, election periods, public holidays)
2. **Overtime reserve:** Do NOT plan overtime into the baseline schedule — keep it in reserve as contingency. If used from the start, there is nothing left when problems arise.
3. **Scope reserve:** Identify non-essential deliverables that can be deferred if the timeline is threatened. Deliver core scope on time; defer remaining work.

**Proposal application:** In work plan narratives, describe the contingency approach: "Our timeline includes [N] buffer days to accommodate disruptions. Overtime capacity is held in reserve for critical-path recovery only."
