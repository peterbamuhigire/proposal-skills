# Financial Analysis Frameworks

Quantitative analysis patterns for consulting methodologies. Use when the ToR requires financial feasibility, investment appraisal, cost-benefit analysis, market sizing, or profitability diagnosis.

---

## 1. Profitability Decomposition

The standard decomposition tree for financial diagnosis:

```
Profit
├── Revenue
│   ├── Quantity sold
│   └── Price per unit
└── Costs
    ├── Variable costs (cost per unit × quantity)
    └── Fixed costs
```

**Gross vs. operating profit distinction:**
- **Gross profit margin** = (Revenue − Cost of Goods Sold) / Revenue — production-level profitability only
- **Operating profit margin** = (Revenue − Total Costs) / Revenue — includes overhead and administration

A business can have high gross margins but low operating margins, indicating the problem is overhead, not production economics. This distinction determines where to focus cost reduction.

**Methodology language:** "We will first assess gross margins to determine production-level profitability, then assess operating margins to understand the impact of overhead and administrative costs."

---

## 2. Breakeven Analysis

**Profit Equation:** Profit = (Quantity × Price) − [(Quantity × Variable Costs) + Fixed Costs]

**Breakeven Equation:** Quantity × (Price − Variable Costs) = Fixed Costs

Three variables are given; solve for the fourth. Use when a methodology includes financial feasibility, investment appraisal, or sustainability assessment.

### One-Time vs. Recurring Cost Separation

When evaluating investments or operational changes, explicitly separate:
- **One-time costs** — setup, installation, replacement, migration
- **Recurring costs** — annual maintenance, salaries, licences, leases

**Methodology language:** "Costs will be categorised as one-time implementation costs and recurring operational costs, with the breakeven analysis accounting for both."

---

## 3. Expected Value Decision Framework

For decisions with uncertain outcomes, calculate expected value:

**Formula:** EV = Σ (Probability of Scenario × Financial Outcome)

| Step | Action |
|---|---|
| 1 | Identify discrete scenarios (e.g., market growth vs. decline) |
| 2 | Assign probabilities to each scenario |
| 3 | Within each scenario, identify sub-outcomes |
| 4 | Assign probabilities and financial outcomes to sub-outcomes |
| 5 | Calculate expected value for each path |
| 6 | Weight by scenario probability for overall expected value |
| 7 | Decision rule: positive EV = proceed; negative EV = do not |

**Methodology language:** "Financial feasibility will be assessed using expected value analysis across [N] scenarios, weighted by probability of occurrence, to provide a risk-adjusted basis for the investment decision."

---

## 4. Sales Cannibalisation Analysis

When a new product or service may take sales from existing offerings:

**Formula:**
```
Net Profit Impact = [New Product Volume × (Price − Variable Cost)]
                  − Additional Fixed Costs
                  − Σ [Cannibalised Volume per Product × Margin per Product]
```

**Key insight:** A new product can appear profitable in isolation but destroy value when cannibalisation of higher-margin existing products is accounted for.

**Methodology language:** "The financial analysis will account for potential cannibalisation of existing revenues, isolating the net incremental profit contribution of the proposed [product/service]."

---

## 5. Market Sizing (Top-Down Method)

The standard structure for demand estimation:

1. Start with total population (national or regional)
2. Segment by relevant demographic (age, income, geography, industry)
3. Estimate percentage of each segment that is a potential customer
4. Estimate consumption frequency per customer
5. Estimate average price or spend per transaction
6. Multiply across to derive market size

**Key principle:** Structure the approach first (no numbers), get alignment, then populate with data. In proposals: describe the analytical framework in the methodology, explain data sources separately.

---

## 6. Weighted Average / Mix Analysis

Overall profitability can decline even when individual product margins hold steady, if the sales mix shifts towards lower-margin products.

**Methodology language:** "The analysis will explicitly isolate mix effects from margin effects — determining whether profitability changes are driven by shifts in service composition or by changes in unit economics."

---

## 7. Promotion and Initiative Financial Modelling

For evaluating marketing programmes, subsidy schemes, voucher systems, or incentive mechanisms:

**Formula:**
```
Average cost per incentive = Face Value × Usage Rate × (Average Redemption / Face Value)
Net profit impact = Incremental Sales × (Price − Variable Cost − Average Incentive Cost) − Programme Fixed Costs
```

**Methodology language:** "The financial model will account for redemption rates and partial utilisation, providing a realistic assessment of the programme's net economic impact."

---

## 8. Pricing Strategy Toolkit

Three pricing methods, each with distinct data requirements:

| Method | Approach | Data Required |
|---|---|---|
| **Customer willingness-to-pay** | Survey/focus group based | Primary data from target customers |
| **Competitive benchmarking** | Price against competitor offerings | Comparable products/services |
| **Cost-plus pricing** | Production cost plus target margin | Internal cost data |

**Methodology language:** "Pricing analysis will triangulate across three methods — customer willingness-to-pay, competitive benchmarking, and cost-plus analysis — to identify the optimal pricing strategy."

---

## 9. Revenue Growth and Cost Reduction Strategies

### Revenue Growth
- **Organic growth:** Increase revenue from existing products (volume or price) or sell new products
- **Inorganic growth:** Mergers, acquisitions, partnerships

### Cost Reduction
- **Variable cost reduction:** Switch suppliers, use substitutes, reduce material per unit, renegotiate prices
- **Fixed cost reduction:** Renegotiate contracts, invest in efficient equipment, consolidate facilities
- Variable costs are generally easier to reduce than fixed costs

### Synergy Analysis
- **Revenue synergies:** Access to new customer bases, cross-selling, shared distribution channels
- **Cost synergies:** Headcount reduction, reduced overhead, increased buying power
- Always assess: Are synergies actually realisable? What is the timeline?

---

*Synthesised from: Hacking the Case Interview (Warfield), The Ultimate Case Interview Workbook (Warfield), The 1%: Conquer Your Consulting Case Interview (Smeritschnig).*
