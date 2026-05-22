# AI-on-SaaS Business Case Template

Template, formulas, and worked examples for an AI-on-SaaS business case that survives CFO and investment-committee scrutiny. Pairs with `ai-on-saas-business-case-and-roi` and extends `saas-business-case-and-roi-template.md`.

## Section 1 — AI Value Stack

For each AI feature, size four value components with a baseline, a target, and a confidence band.

### 1.1 Cost-of-Poor-Quality Reduction
- Baseline error rate × volume × cost-per-error = current cost of poor quality (CCPQ).
- Target error rate (post-AI) × volume × cost-per-error = future cost of poor quality (FCPQ).
- Annualised saving = CCPQ − FCPQ.

### 1.2 Agent / Worker Productivity Uplift
- Workflow time saved per case × case volume × loaded labour rate × adoption rate × realisation rate.
- Realisation rate is the percentage of saved time that converts to value (typical 30–60 % for knowledge work; lower if the freed time cannot be redeployed).

### 1.3 Revenue from AI-Tier Upsell
- AI-tier price uplift × number of upgrading tenants × attach rate × retention.
- Sensitivity on attach rate (the single most volatile assumption).

### 1.4 Revenue from AI-Driven Activation / Retention
- AI-driven activation lift (basis points) × monthly cohort size × LTV.
- AI-driven retention lift (basis points) × tenant base × ARR per tenant.
- Where activation and retention move together, isolate the AI contribution from base lifecycle programmes to avoid double-count.

### Worked Example — Value Stack
A regulated mid-market SaaS adds an RM copilot to its premium tier. Baseline error rate on response drafting is 8 %, cost per error $40, volume 60 000 cases / month. Target error rate 3 %. CCPQ = 0.08 × 60 000 × 40 = $192 000 / month. FCPQ = 0.03 × 60 000 × 40 = $72 000 / month. Monthly saving $120 000; annualised $1.44 M. Productivity uplift: 6 minutes saved per case, 60 000 cases / month, $40 / hour loaded, 50 % adoption, 40 % realisation = 60 000 × 0.1 × 40 × 0.5 × 0.4 = $48 000 / month, annualised $576 000. AI-tier upsell: 220 tenants × $12 000 ARR uplift × 35 % attach = $924 000. Total value stack $2.94 M (base case).

## Section 2 — AI Cost Stack

For each AI feature, size the four cost components:

### 2.1 Model and Embedding Cost
- Tokens-in per call × token-in price + tokens-out per call × token-out price = cost per call.
- Calls per case × cases per month × cost per call = monthly model cost.
- Embedding cost: chunks × embedding price + re-embedding × refresh cadence.
- Worked at P50, P90, P99 tenant volume.

### 2.2 Eval Cost
- Golden-set size × refresh cadence × labelling cost per case (human) = annual eval-labelling cost.
- LLM-as-judge calls × cost per judge call × CI runs × refresh cadence.
- Human review (sampling rate × monthly calls × per-review cost).
- Red-team scope × frequency × red-team day-rate.

### 2.3 AI Operations and Cloud
- MLOps engineer FTE × salary + on-call.
- Vector store ($/month for tenant volume).
- GPU rental or sovereign inference (if applicable).

### 2.4 AI Engineering Payroll (Build Phase)
- Sized once (build) and amortised across the value horizon.

### Worked Example — Cost Stack
Same RM copilot. 1 800 tokens-in × $5 / M + 350 tokens-out × $15 / M = $0.0144 / call. Two RAG calls + one synthesis per case = three calls. Cost per case ≈ $0.043. 60 000 cases / month × $0.043 = $2 580 / month model cost (P50). P99 tenant: a single tenant pushing 25 % of volume can double cost-per-tenant — track and meter. Embedding cost: 1.2 M chunks × $0.0001 + monthly 5 % re-embed = $120 + $6 = $126. Eval: golden set 400 cases × quarterly refresh × $8 / case labelling = $12 800 / year. LLM-as-judge × CI: 400 × 12 deploys × $0.005 = $24 / year. Human review: 2 % sampling × 60 000 × 12 × $2.50 = $36 000 / year. Red-team: quarterly × 5 days × $1 200 = $24 000 / year. MLOps 0.4 FTE × $90 000 = $36 000. Vector store $400 / month. AI engineering build $180 000 amortised. Annual cost ≈ $190 000 (operating) + $180 000 / 3 (amortised build) = $250 000.

## Section 3 — Eval-Margin

Eval-margin = annual eval cost ÷ annual gross margin contribution of the AI feature.

In the worked example: $72 800 ÷ $2 940 000 = 2.5 %. Healthy (target ≤ 15 %).

If the AI feature is small and eval is heavy, eval-margin can reach 30–50 %; that is a flag that either eval can be lighter (judge-graded with smaller golden set) or the feature is not earning its keep.

## Section 4 — Cost-of-Tokens per Tenant

| Tenant volume cohort | Cases / month | Model cost / month | Cost / case |
|---|---|---|---|
| P50 (median tenant) | 200 | $8.60 | $0.043 |
| P90 (heavy tenant) | 1 500 | $64.50 | $0.043 |
| P99 (whale tenant) | 8 000 | $344 | $0.043 |

P99 cost-per-tenant matters most for pricing fair-use. If the AI feature is bundled in a $99 / month tier, a P99 tenant has token cost > 3 × the licence — fair-use must trigger.

## Section 5 — Three-Scenario ROI

| Scenario | Value (annual) | Cost (annual) | Net | Caveat |
|---|---|---|---|---|
| Downside | $1.20 M | $0.31 M | $0.89 M | Attach rate 18 %, adoption 30 %, hallucination drives manual review up |
| Base | $2.94 M | $0.25 M | $2.69 M | Attach 35 %, adoption 50 %, realisation 40 % |
| Upside | $4.30 M | $0.27 M | $4.03 M | Attach 50 %, adoption 65 %, realisation 55 % |

Never quote a single ROI. The three-scenario table is what survives the CFO.

## Section 6 — Payback and NPV

- Payback (base case): build cost $180 000 ÷ net monthly value $224 000 ≈ < 1 month (this is the canonical sign that the feature is earning).
- NPV over 36 months at 12 % discount rate: $5.6 M base case.
- Sensitivity: token price ±30 %, adoption ±20 pp, attach rate ±15 pp.

## Section 7 — Downside Scenarios

| Scenario | Trigger | Financial impact | Mitigation (anchored in methodology) |
|---|---|---|---|
| Regulator changes tier classification | AI Act / NCAIS reclassification | $400 K conformity + 3-month delay | Quarterly regulator scan, conformity readiness, modular controls |
| Hallucination liability event | Untrue output causes customer harm | $200 K incident response + reputational | Hallucination ceiling, abstain logic, citation grounding, professional indemnity |
| Model-provider price increase or ban | Provider raises 50 %, sanctions ban | $90 K / year if no gateway; near-zero with gateway | Multi-provider gateway, fall-back model, contractual notice |
| Eval drift not caught | Golden-set pass slips below threshold | $120 K rework + customer credits | Drift watch, monthly eval refresh, alerting |
| AI-tier upsell flops | Attach < 12 % | $660 K revenue shortfall | Pricing pattern shift (hybrid floor), AI-tier price reduction |
| Sovereign-AI mandate | Public-sector tenant requires on-prem | $300 K capex + 4-month delay | Sovereign-AI option in roadmap, GPU sourcing readiness |

## Section 8 — FX

If revenue is local-currency (KES, NGN, ZAR, UGX, RWF) and model cost is USD-denominated, name the FX assumption and the hedge.

Worked example: 60 % USD revenue, 40 % local-currency revenue; model cost 100 % USD. FX assumption: NGN / USD ±15 % year-on-year. Mitigation: quarterly price reset clause indexed to FX > 10 % movement; reserve buffer 8 %.

## Section 9 — Output

- AI Business Case Memo (CFO one-pager or board memo).
- AI Value Stack and AI Cost Stack tables.
- Eval-Margin number.
- Cost-of-Tokens per Tenant table.
- Three-scenario ROI.
- Payback, NPV, sensitivity.
- Downside Scenarios table.
- FX assumption and hedge.

## Cross-References

- `ai-on-saas-pricing-models-reference.md` — pricing patterns that drive revenue inputs.
- `ai-on-saas-risk-register-for-proposals.md` — risks that drive downside scenarios.
- `ai-on-saas-metrics-glossary.md` — metric definitions used in the case.
- `saas-business-case-and-roi-template.md` — base SaaS template.
