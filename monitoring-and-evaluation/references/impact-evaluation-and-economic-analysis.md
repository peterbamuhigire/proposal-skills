# Impact Evaluation and Economic Analysis

Reference material for the monitoring-and-evaluation skill. Provides detailed guidance on impact evaluation designs, counterfactual analysis, statistical methods, power calculations, data collection, cost-benefit analysis, and economic impact assessment. Use when proposals require impact evaluation components, economic analysis, or rigorous evaluation methodology.

Sources: White & Raitzer (Impact Evaluation of Development Interventions, ADB, 2017), Davis (Regional Economic Impact Analysis and Project Evaluation, UBC Press, 2001).

---

## 1. Impact Evaluation — Core Concepts

### What Impact Evaluation Is

Impact evaluation (IE) empirically estimates the causal effects attributable to a specific intervention and their statistical significance. It is based on **counterfactual analysis**: comparing what actually happened with what would have happened in the absence of the intervention.

**Impact = Y1(t+1) - Y0(t+1)**, where Y1 is the factual outcome and Y0 is the counterfactual.

IE is fundamentally different from:
- **Process evaluation** — how projects were implemented
- **Impact assessment** — structural modelling with untestable assumptions
- **Monitoring** — tracking inputs, activities, and outputs

### Two Generations of IE Questions

| Generation | Question | Purpose |
|---|---|---|
| **First** | "Does it work?" | Did the intervention make a statistically significant difference? |
| **Second** | "How to make it work better?" | Which design is most effective? What factors condition effectiveness? |

### Five Impact Measures

| Measure | Definition | When Used |
|---|---|---|
| **ATE** (Average Treatment Effect) | Average impact on the entire eligible population | Overall programme effect |
| **ITT** (Intention to Treat) | Average impact of exposure (all in programme area) | Programme-level accountability |
| **ATT** (Average Treatment Effect on the Treated) | Average impact on those who actually participate | Impact on compliers |
| **ATU** (Average Treatment Effect on the Untreated) | Average potential impact on non-participants if treated | Programme expansion decisions |
| **LATE** (Local Average Treatment Effect) | Average impact on subgroup at eligibility threshold | Regression discontinuity designs |

**Key relationship:** ATT ≥ ATE ≥ ATU ≥ LATE (if targeting is purposive and logical).

**Link between ITT and ATT:** ITT = ATT × participation rate. Low participation drives a wedge between the two.

### Internal vs External Validity

- **Internal validity** — are estimates valid for the assessed sample? Function of rigour of design.
- **External validity** — can findings be generalised? Enhanced by: (i) strong theory of change, (ii) representative sample, (iii) widely implemented intervention, (iv) broadly applicable economic logic.

---

## 2. Theory of Change for Impact Evaluation

### Seven Steps to Construct a Theory of Change (White & Raitzer)

1. **Define the problem** — what the intervention addresses
2. **Identify interventions and outputs** — make as specific as possible
3. **Lay out main steps in causal chain** — link inputs to outcomes through activities, outputs, intermediate outcomes
4. **Conceptualise indicators along the causal chain** — trace causal connections and identify obstacles
5. **Identify underlying assumptions** — no assumptions taken for granted
6. **Distinguish among outcome channels** — separate pathways for different beneficiary groups
7. **Validate and revise** — through stakeholder consultation (programme staff, beneficiaries, peer agencies)

### Funnel of Attrition

For every 100 intended beneficiaries, how many actually benefit? Key checkpoints:

- Are beneficiaries **aware** of the programme?
- Do they **want** to take part?
- Are they **able** to take part? (time, place, cost, social barriers)
- Is **knowledge transfer** effective?
- Does **behaviour change** occur as expected?
- Are **conditions for sustained effect** present?

**Proposal application:** Include the funnel of attrition in methodology sections to show you understand why programmes underperform — and how your design addresses each drop-off point.

### Behavioural Change Model

For each link in the causal chain, specify:
- Assumed behaviour
- Evidence for and against the assumption
- Data needed for IE
- Evaluation question

---

## 3. Impact Evaluation Designs — Complete Taxonomy

### 3.1 Experimental Design: Randomised Controlled Trials (RCTs)

With sufficient sample size, random assignment ensures balance on both observable and unobservable characteristics. Any difference in outcomes must be attributable to the intervention.

**Types of RCT Designs:**

| Design | Description | When to Use |
|---|---|---|
| **Simple RCT** | Unit of assignment = unit of treatment = unit of measurement | Individual-level programmes |
| **Cluster RCT** | Unit of assignment contains multiple treatment units | Community-level interventions (most common in development) |
| **Random selection (lottery)** | Random choice among oversubscribed eligible applicants | Excess demand programmes |
| **Altered threshold** | Slightly relax eligibility threshold, randomise within expanded pool | Targeted programmes |
| **Pipeline/step-wedge** | Randomise order of treatment, not treatment itself | Phased rollout programmes |
| **Encouragement** | Universally available; treatment group gets encouragement to participate | Voluntary adoption programmes |
| **Multi-treatment arm** | Multiple treatment combinations tested | Testing interaction effects |
| **Factorial** | All combinations of multiple treatments tested | Isolating treatment components |
| **Crossover** | Treatment and control switch at midpoint | When all must eventually receive treatment |

**Seven Common RCT Pitfalls:**

1. Underpowered studies (actual power often only ~50%)
2. Attrition (differential dropout between treatment and control)
3. Non-compliance/crossovers (treatment group untreated, control group treated)
4. Getting standard errors wrong (not adjusting for clustering)
5. Not getting buy-in or sufficient oversight for randomisation
6. Researcher capture (academic agenda diverges from policy questions)
7. Not testing along the causal chain (missing the "why")

### 3.2 Quasi-Experimental Methods

#### Difference-in-Differences (DiD)

- Impact = (Change in treatment group) − (Change in comparison group)
- Removes baseline differences and general trends
- Requires **parallel trends assumption** (can be tested with pre-intervention data)
- Fixed effects models combine DiD with multivariate regression
- Generates ATT

#### Synthetic Controls

- Builds counterfactual by weighting comparison units to match pre-treatment trends
- Relaxes parallel trends assumption
- Uses placebo tests for significance
- Applicable to small-n interventions (e.g., large infrastructure)
- Requires balanced panel data with long pre-treatment periods

#### Propensity Score Matching (PSM)

- Estimates probability of treatment given observable characteristics
- Matches treated to untreated with similar propensity scores
- Matching types: nearest neighbour (1 or k), caliper, kernel
- Region of common support: discard non-overlapping observations
- Balance test: no significant differences after matching
- "Method of last resort" — always possible if sufficient data
- Can be done ex post without baseline
- Cannot account for selection on unobservables

#### Propensity Score Weighting (IPW) and Double Robust

- IPW: weight by inverse probability of participation
- Double robust (augmented IPW): combines propensity score with outcome regression
- Unbiased if either propensity score OR outcome regression is correctly specified

#### Regression Discontinuity Design (RDD)

- Used when there is a threshold rule for eligibility
- **Sharp RDD:** threshold perfectly applied
- **Fuzzy RDD:** threshold imperfectly applied (use IV approach)
- More completely controls unobservables than other quasi-experimental methods
- Can leverage administrative data
- Generates LATE

#### Interrupted Time Series (ITS)

- Special case of RDD where threshold is a point in time
- Best when intervention effectiveness is sudden
- Requires sufficient pre- and post-intervention observations

#### Instrumental Variables (IV)

- Replaces endogenous participation variable with an instrument
- Instrument must satisfy: (1) relevance (correlated with treatment), (2) exclusion restriction (affects outcome only through treatment)
- Controls both observable and unobservable selection bias
- Main challenge: finding valid instruments

### 3.3 Design Selection Decision Tree (White & Raitzer)

Use this sequence to select the appropriate design:

1. Is the programme being rolled out in stages? → **Pipeline RCT**
2. Is there oversubscription? → **Lottery RCT**
3. Can the eligibility threshold be altered? → **Altered threshold RCT**
4. Is the programme universally available but not universally adopted? → **Encouragement design**
5. Is there a clear eligibility cutoff? → **RDD**
6. Are baseline data available? → **DiD with matching**
7. Is there a valid instrument? → **IV estimation**
8. Are there sufficient pre-treatment observations? → **Synthetic controls**
9. Is treatment binary with sufficient data? → **PSM or double robust**
10. None of the above → **Endogenous treatment/switching regression**

**Always have a backup identification strategy in case the primary fails.**

**Proposal application:** When the ToR mentions "impact evaluation," specify which design you will use and why, following this decision tree. If a full RCT is not feasible (as is often the case), propose a quasi-experimental approach and explain the rationale. This demonstrates methodological sophistication that distinguishes your proposal.

---

## 4. Key Assumptions by Method

| Method | Key Assumption | Generates |
|---|---|---|
| **RCT** | Random assignment (SUTVA — no spillovers) | ATE |
| **DiD** | Parallel trends | ATT |
| **Synthetic controls** | Factor model with weighted comparison | ATT |
| **PSM** | Conditional independence / selection on observables | ATT, ATE |
| **RDD** | Continuity of potential outcomes at threshold | LATE |
| **IV** | Exclusion restriction + relevance | LATE |
| **Fixed effects** | Time-invariant unobservables | ATT |

### Selection Bias Components

- **Placement bias** — programmes placed in locations correlated with outcomes
- **Self-selection bias** — participants differ from non-participants on unobservables
- **Identification strategy** — the approach to dealing with selection bias

---

## 5. Sample Size and Power Calculations

### Power Calculation Framework

| | Find No Significant Impact | Find Significant Impact |
|---|---|---|
| **Intervention has no impact** | Correct | Type I Error (false positive) |
| **Intervention has impact** | Type II Error (false negative) | Correct |

- **Power** = 1 − P(Type II error) = probability of finding impact when it exists
- Standard target: **80% power** at **5% significance**

### Simple Power Formula

n = 2(t_α/2 + t_β)² × σ² / MES²

Where:
- n = sample size per group
- σ = standard deviation of outcome
- MES = minimum effect size to detect
- t values: α=5% → t=1.96; β=20% → t=0.84

**Key insight:** Halving the MES quadruples the required sample size.

### Cluster Design Power Adjustment

n_cluster = n_simple × [1 + (m−1) × ICC]

Where:
- m = number of observations per cluster
- ICC = intracluster correlation coefficient
- **Number of clusters matters more than observations per cluster**
- Minimum recommended: **15 clusters per arm** (30+ preferred)

### Rules of Thumb for Development Evaluations

- 200–400 respondents per comparison group for quantitative impact measurement
- For qualitative methods: aim for saturation (typically 15–30 interviews per stakeholder group)
- Minimum for focus groups: 6–10 participants per group; 4–8 groups per stakeholder category

### Common Reasons for Underpowered Studies

1. No power calculations performed
2. Clustering not considered
3. ICC assumed too low
4. Expected effect size too optimistic
5. Participation rate overestimated
6. Attrition not accounted for
7. R-squared of covariates overestimated

### Power Calculation Software

- **Optimal Design** (Raudenbush et al.) — free, multilevel designs
- **3ie Sample Size Calculator** — Excel-based, development-specific
- **STATA power commands** — built-in

**Proposal application:** Include power calculations in evaluation methodology sections. State the minimum detectable effect size, assumed ICC, number of clusters, and total sample size. This is expected in World Bank, ADB, and bilateral donor IE proposals and is a major differentiator.

---

## 6. Data Collection for Impact Evaluation

### Data Sources (Hierarchy)

1. Existing surveys (national household surveys, DHS, LSMS)
2. Administrative data (Education MIS, billing data, school census)
3. Geographic information systems / remote sensing
4. Real-time data (traffic flows, pollution sensors, mobile phone apps)
5. Purpose-built surveys (most common for IE)

### Survey Data Collection Rounds

| Round | Timing | Purpose |
|---|---|---|
| **Baseline** | Before intervention | Establish starting values; check balance |
| **Midline** | Midway through | Process and intermediate outcomes |
| **Endline** | At or near completion | Measure final values for comparison |
| **Post-endline** | Years after closure | Test sustainability |

Panel data (same units across rounds) produces the strongest designs.

### Six Types of Survey Instruments

1. **Household survey** — welfare, consumption, health, education
2. **Enterprise survey** — employment, sales, credit, risk attitudes
3. **Facility survey** — schools, clinics, service quality
4. **Community survey** — village facilities, development projects, livelihoods
5. **Agency survey** — implementing organisation resources, procedures
6. **Worker survey** — teachers, health workers, skills, practices

### Electronic Data Collection Platforms

| Platform | Provider | Advantages |
|---|---|---|
| **CSPro** | US Census Bureau | Oldest CAPI platform; robust |
| **ODK / KoboToolbox** | Open source | Android, GPS, offline capability |
| **Survey Solutions** | World Bank | Cloud-based, real-time monitoring |
| **SurveyCTO** | Dobility | Skip logic, encryption, field management |

### Mixed Methods Integration

Qualitative data serves three roles in IE:
1. **Formative** — inform evaluation and survey design
2. **Interpretive** — capture barriers, implementation problems, sensitive issues
3. **Generalisation** — help interpret and generalise quantitative findings

---

## 7. Managing the IE Process

### Evaluability Assessment

Before committing to IE, assess:
- Clarity of intervention logic
- Data availability
- Feasibility of comparison group
- Stakeholder readiness
- Timing alignment

### Illustrative Timeline

| Phase | Duration | Activities |
|---|---|---|
| **Design** | 3–6 months | ToC, method selection, power calculations, survey design |
| **Baseline** | 3–6 months | Instrument testing, enumeration, data entry/cleaning |
| **Implementation monitoring** | Ongoing | Track rollout, contamination, compliance |
| **Midterm** (optional) | 2–4 months | Process data, intermediate outcomes |
| **Endline** | 3–6 months | Enumeration, data entry/cleaning |
| **Analysis** | 3–6 months | Impact estimation, reporting |
| **Total** | 3–7 years | Depending on intervention timeline |

### Budget Benchmarks

- Average survey round: ~$200,000
- Average full IE study: ~$400,000–$450,000
- Large World Bank/USAID IEs: frequently exceed $1,000,000

### IE Team Composition

- Prior IE design and execution experience (essential)
- Sector expertise
- Fieldwork experience in developing country settings
- Advisory group: minimum 3–4 members (IE expert + sector expert + local institution)

### Mitigating Researcher Capture

1. Clearly defined scope of work before contracting
2. Unambiguous evaluation questions in ToR
3. Advisory group with IE technical expert
4. Close monitoring of implementation
5. Final review process ensuring questions are answered

---

## 8. IE Quality Checklists

### IE Design Quality Checklist (White & Raitzer)

1. Theory of change clearly articulated with testable assumptions
2. Evaluation questions derived from ToC and evidence gaps
3. Identification strategy addresses selection bias
4. Power calculations performed and independently verified
5. Baseline data collected before intervention effects begin
6. Balance demonstrated between treatment and comparison groups
7. Multiple survey instruments cover full causal chain
8. Backup identification strategy specified
9. Ethical approvals obtained and informed consent documented
10. Data archiving and public access planned
11. Advisory group established with IE and sector expertise
12. Analysis plan pre-specified before endline data collection

### Data Collection Quality Checklist

1. Survey instruments pretested (team, enumerators, field pilot)
2. Enumerator training includes role play and field testing
3. Electronic data collection with built-in consistency checks
4. GPS coordinates recorded for validation
5. Independent field supervision during enumeration
6. Data validation through resurvey of subsample
7. Seasonal timing consistent across rounds
8. Panel attrition tracking protocols in place
9. Data cleaning protocol documented
10. Original questionnaires retained until analysis complete

---

## 9. Cost-Benefit Analysis for Development Projects (Davis)

### Core Framework

**Net Present Value (NPV):** P₀ = Σ (Bₜ − Cₜ) / (1+r)ᵗ

### Three Investment Criteria

| Criterion | Decision Rule | Strength | Limitation |
|---|---|---|---|
| **NPV** | Accept if NPV > 0 | Recommended; maximises total value | Requires discount rate selection |
| **Benefit-Cost Ratio (B/C)** | Accept if B/C > 1.0 | Useful for ranking under budget constraints | Sensitive to cost/benefit classification |
| **Internal Rate of Return (IRR)** | Accept if IRR > opportunity cost | Widely understood | Multiple roots; computational difficulty |

### Shadow Pricing for Distorted Markets

In development contexts where markets are distorted:

| Distortion | Adjustment |
|---|---|
| **Imperfect competition** | Use marginal cost, not market price |
| **Taxation** | Use pre-tax price (tax is a transfer, not social cost) |
| **Subsidies** | Add subsidy back to market price |
| **Unemployment** | Shadow wage = 0 or fraction of market wage for unemployed resources |
| **Externalities** | Social marginal cost diverges from private marginal cost |

**Proposal application:** Shadow pricing is essential for development project appraisal where markets are distorted. The treatment of unemployment shadow wages is directly relevant to labour-surplus East African economies.

### Valuation of Non-Market Goods

| Method | Approach | Best For |
|---|---|---|
| **Travel cost** | Infer value from what people spend to visit a site | Recreation, tourism |
| **Hedonic pricing** | Extract value from property price differentials | Environmental goods |
| **Contingent valuation** | Direct surveys asking willingness to pay | Any non-market good |

### Discount Rate Selection

| Approach | Basis | Typical Rate |
|---|---|---|
| **Social Opportunity Cost (SOC)** | Pre-tax return in private sector | Higher (8–12%) |
| **Social Time Preference (STP)** | Rate to induce sacrifice of present for future | Lower (3–5%) |
| **Weighted average** | Blend of SOC and STP based on funding source | Middle (7–10%) |

**Always conduct sensitivity analysis** with upper and lower bounds (e.g., 5% and 15% around central estimate).

### Risk and Uncertainty in CBA

**Risk (probabilities known):**
- Expected value approach: E(NPV) = Σ (probability × NPV) for each outcome
- Consider variance — risk-averse decision-makers may prefer lower-expected-value projects with less variance

**Uncertainty (probabilities unknown) — Decision strategies:**

| Strategy | Approach | Orientation |
|---|---|---|
| **Maximax (Hurwicz)** | Choose project with highest potential payoff | Optimistic |
| **Maximin (Wald)** | Maximise the minimum return | Pessimistic |
| **Laplace** | Assign equal probabilities to all states | Neutral |
| **Savage (minimax regret)** | Minimise the maximum potential regret | Regret-minimising |

---

## 10. Distributional Analysis (Davis)

### Incidence Matrix

Shows distribution of NPV across geography and social cohorts:

| | Group A | Group B | Group C | Total |
|---|---|---|---|---|
| **Region 1** | +X | −Y | +Z | Net |
| **Region 2** | −X | +Y | +Z | Net |
| **Total** | Net | Net | Net | Overall NPV |

### Five Methods for Equity Analysis

1. **Income weighting** — weight benefits by inverse of income class (aᵢ = Y_avg / Yᵢ)
2. **Public sector decision weights** — derive from marginal tax rates
3. **Constrained maxima** — maximise NPV subject to minimum benefits to target group
4. **Variable project design** — multiple designs meeting different equity objectives
5. **Incidence presentation** (recommended) — matrix of net benefits by group; leave weighting to decision-makers

**Proposal application:** Include an incidence matrix in economic analysis sections to show distributional effects across regions and social groups. This aligns with GESI requirements and donor emphasis on equity.

---

## 11. Multi-Criteria Evaluation Frameworks (Davis)

### Planning Balance Sheet (Lichfield)

- Records ALL impacts (economic, social, environmental) in monetary, physical, or qualitative terms
- Double-entry: assigns every cost/benefit to "producers" and "consumers"
- Includes transfers (unlike CBA which nets them out)

### Goals Achievement Matrix (Hill)

- Explicitly states and weights multiple goals (not just efficiency)
- Assigns relative weights to social groups
- Costs/benefits can be monetary, non-monetary, or qualitative
- Overcomes CBA's bias toward efficiency over other objectives

**Proposal application:** When donors require evaluation beyond pure economic efficiency — including social, environmental, and equity objectives — reference these multi-criteria frameworks. They align well with OECD-DAC evaluation criteria.

---

## 12. How IE Informs the Project Cycle (White & Raitzer)

| Area | IE Contribution |
|---|---|
| **Sector analysis** | Evidence on most important investments |
| **Economic rationale** | Evidence on constraint alleviation |
| **Demand analysis** | Revealed willingness to pay |
| **Design and monitoring framework** | Evidence on critical assumptions |
| **Alternative analysis** | Comparative effectiveness evidence |
| **Cost-benefit analysis** | Quantified effect magnitudes |
| **Sustainability** | Evidence on adoption and scale-up |
| **Risk analysis** | Evidence on why interventions fail |
| **Distribution analysis** | Evidence on uptake and distributional impacts |

---

## 13. Ethical Considerations for IE

1. Obtain ethical review board approval (institutional + country)
2. Informed consent (cluster-level consent acceptable for cluster RCTs)
3. Remunerate respondents appropriately (small in-kind gifts)
4. Report treatment of ethical issues in IE report
5. Control group members may feel unfairly treated — address through benefits at study end

### Interpreting Results — What to Watch For

- **Effect size matters as much as significance** — large-n studies can make tiny effects significant
- Report effects in understandable units (e.g., 0.2 SD in learning ≈ one year of schooling)
- Always include **cost-effectiveness analysis**: cost per standardised unit of outcome improvement
- **Threats to validity:** Hawthorne effects, John Henry effects, placebo effects, differential attrition, omitted variable bias
