# Solution Evaluation

Tools and methods for validating that a solution (implemented or about to be implemented) delivers expected business value and meets stakeholder needs. Relevant to methodology sections covering acceptance, testing, benefits realisation, and post-implementation review.

---

## Evaluation Principles

1. **Evaluate early and often** — do not wait until the end
2. **Treat requirements analysis, traceability, testing, and evaluation as complementary activities**
3. **Evaluate with context of usage and value in mind**
4. **Confirm expected values for solutions**

---

## What to Evaluate

| Evaluation Area | Description | Example Metrics |
|---|---|---|
| **Business Goals and Objectives** | Does the solution contribute to stated goals? | % of strategic objectives addressed |
| **Key Performance Indicators (KPIs)** | Organisation-level metrics for progress | Revenue, cost reduction, efficiency gains |
| **Customer Metrics** | Customer satisfaction, adoption, usage | NPS score, adoption rate, active users |
| **Operational Metrics** | Process efficiency, error rates, cycle times | Processing time, error rate, throughput |
| **Functionality** | Does the solution do what it is supposed to do? | Features delivered vs. requirements |
| **Nonfunctional Requirements** | Performance, security, usability, reliability | Response time, uptime, user satisfaction |

---

## Acceptance Criteria

### Defining Acceptance Criteria

Acceptance criteria define the conditions under which stakeholders will accept the solution. They must be:
- **Specific** — clear, unambiguous conditions
- **Measurable** — can be objectively verified
- **Agreed** — confirmed by stakeholders before evaluation

### Acceptance Criteria Evaluation Format

| Criteria | Expected Value | Min Acceptable | Actual Value | Pass/Fail |
|---|---|---|---|---|
| [Feature/Metric] | [Target] | [Minimum] | [Measured] | [Result] |

### Key Practices
- Compare expected vs. actual results
- Examine tolerance ranges and exact numbers
- Log and address defects found during evaluation
- Analyse cause of any discrepancy

### Behaviour-Driven Development (BDD) Format
- **Given** [precondition]
- **When** [action]
- **Then** [expected result]

### Definition of Done
A checklist of criteria that must be satisfied for a requirement/story to be considered complete. Typically includes:
- Code complete and reviewed
- Unit tests pass
- Integration tests pass
- Acceptance criteria verified
- Documentation updated
- Deployed to test environment

---

## Validation Methods

| Method | Description | When to Use |
|---|---|---|
| **User Acceptance Testing (UAT)** | End users verify the solution against acceptance criteria | Before go-live; final validation gate |
| **Day-in-the-Life (DITL) Testing** | Simulate real-world usage scenarios end-to-end | Complex solutions with many process interactions |
| **Exploratory Testing** | Unscripted testing to discover unexpected issues | Supplement to structured testing |
| **Integration Testing** | Verify system interactions and data flows | Multi-system solutions |
| **Surveys and Focus Groups** | Gather user feedback on usability and satisfaction | Post-implementation or during pilot |
| **Structured Walkthroughs** | Step-through with stakeholders to confirm understanding | Requirements validation; design review |

### UAT Best Practices

- Business analysts should coordinate and guide business units during UAT
- UAT is the final stage for validating requirements

**Two-cycle approach:**
1. **Cycle 1:** Experience-based tests (without running formal test cases) — users explore freely
2. **Cycle 2:** Structured UAT using formal test cases derived from requirements

**Training timing:**
- If replacing an existing product: user training after UAT (users already know the domain)
- If new product: user training before UAT (users need familiarity first)

---

## Go/No-Go Decision

The business analyst facilitates the go/no-go decision based on:

| Factor | Assessment |
|---|---|
| **Evaluation results** | Do actual results meet acceptance criteria? |
| **Outstanding defects** | What is the severity and count of unresolved issues? |
| **Stakeholder readiness** | Are users trained and prepared? |
| **Organisational readiness** | Are support processes, documentation, and infrastructure in place? |
| **Risk assessment** | What are the risks of going live vs. delaying? |

---

## Long-Term Solution Performance

After implementation, continue evaluation through:

1. **Determine metrics** for ongoing measurement
2. **Obtain metrics / measure performance** over time
3. **Analyse results** against expected outcomes
4. **Assess limitations** of the solution and organisation
5. **Recommend improvements** to solution performance

### Benefits Realisation

| Element | Description |
|---|---|
| **Benefits register** | Catalogue of expected benefits with owners and timelines |
| **Measurement plan** | How and when each benefit will be measured |
| **Baseline data** | Pre-implementation metrics for comparison |
| **Tracking cadence** | Regular review (monthly, quarterly) of benefits realisation |
| **Variance analysis** | Comparison of expected vs. actual benefits with root cause of variance |

**Proposal language:** "We will establish a benefits realisation framework with baseline metrics, target values, and a measurement schedule to track value delivery over [N] months post-implementation."

---

## Solution Performance Assessment

### Assessment of Business Value

Uses:
- **Cost-Benefit Analysis** — Compare actual costs and benefits against projections
- **Product Portfolio Matrix** — Evaluate products across market growth and share dimensions
- **Root Cause and Opportunity Analysis** — Understand variance between expected and actual performance
- **Prioritisation Schemes** — Rank improvement opportunities

### Readiness Assessment

Evaluation of organisational preparedness for transition:
- **Process readiness** — Are new processes documented and communicated?
- **People readiness** — Are staff trained? Is change resistance addressed?
- **Technology readiness** — Is infrastructure in place and tested?
- **Data readiness** — Is data migrated, validated, and accessible?

### Transition Planning

| Element | Content |
|---|---|
| **Migration strategy** | How to move from old to new solution |
| **Data conversion** | Data mapping, cleansing, migration, validation |
| **Parallel running** | Period where old and new systems run simultaneously |
| **Cutover plan** | Specific steps for the switch, with rollback procedures |
| **Support plan** | Post-go-live support structure and escalation paths |

---

## Lean KPIs (Outcome vs. Output)

| Anti-Pattern (Output KPI) | Best Practice (Outcome KPI) |
|---|---|
| Number of requirements documented | Number of user requirements satisfied at release |
| Number of defects found | Percent of business requirement targets met at first release |
| Lines of code built | Customer satisfaction metrics per release |

**Key insight:** Output-oriented KPIs create suboptimisation. Outcome-oriented KPIs optimise whole-team objectives and focus on value delivery.

---

## Solution Replacement / Phase-Out

When a solution no longer meets business needs:
- **Migration strategy** — Plan for moving to replacement solution
- **Data archival** — Retain data per regulatory and business requirements
- **Transition support** — User training, communication, parallel running
- **Decommissioning** — Formal retirement of old solution

---

*Synthesised from: PMI Guide to Business Analysis (2017), Business Analysis for Practitioners (PMI, 2015), Business Analysis Methodology Book (Yayici, 2015), Seven Steps to Mastering Business Analysis (Champagne, 2019).*
