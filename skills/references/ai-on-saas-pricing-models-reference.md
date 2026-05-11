# AI-on-SaaS Pricing Models Reference

Pricing pattern library for AI features inside a multi-tenant SaaS, with worked examples and ready-to-paste clauses. Pairs with `ai-on-saas-pricing-and-packaging-proposal` and extends `saas-pricing-models-reference.md`.

## The Five AI Pricing Patterns

### Pattern 1 — Bundled in Tier (AI as part of the base licence)
- AI features included at no marginal price inside an existing tier.
- Fits low-cost-per-call features (lightweight classification, light RAG) with predictable usage.
- Requires fair-use clause to protect against P99 tenants.
- Risk: cost-of-tokens at P99 swamps the licence; agency-side margin compression.
- When to use: AI is a "must-have" feature competitors give away; bundled AI defends churn rather than driving expansion revenue.

### Pattern 2 — AI-Tier as Upsell (Premium tier gates AI)
- A separate premium tier (Pro, Premium, Enterprise+) includes AI; standard tier does not.
- Fits when the AI is a clear value driver and the buyer can pay for it.
- Clean attach-rate economics: track who upgrades, who churns, who stays.
- Risk: split product, perception of "tax for AI."
- When to use: AI is a discriminator that earns its own tier; the buyer has a price ladder culture.

### Pattern 3 — Included Allowance + Overage (X credits, then $Y per K calls)
- Each tier includes a monthly AI allowance (calls, tokens, credits); usage above the allowance is metered.
- Fits variable-usage AI features where most tenants are below allowance and a few exceed.
- Allowance reset monthly; rollover policy stated explicitly.
- Worked example: Pro tier = 5 000 AI calls / month included; overage $0.06 / call. P99 tenant pays $480 / month overage on top of $299 licence — defensible.

### Pattern 4 — Pure Usage Credits (Pay per use)
- No included AI; tenant tops up credits and burns them.
- Fits very-large-enterprise tenants, sandbox / dev tier, or use cases with extreme volume variation.
- Risk: psychological pricing — tenants hate variable bills.
- Mitigation: prepay discount, soft caps, alerting.

### Pattern 5 — Hybrid Floor + Overage
- Combines a subscription floor (predictable) with usage overage above a threshold.
- Fits AI features where some predictable value justifies a floor and incremental usage adds variable value.
- Most defensible pattern for regulated mid-market.

## Model-by-Tier Matrix

| Tier | Models available | Region routing | Sovereign option |
|---|---|---|---|
| Standard | Cost-efficient open model (Llama family, Mistral) or value-tier frontier (Haiku, GPT-4o mini) | Default region per residency policy | No |
| Pro | Above + premium frontier (Sonnet, GPT-4o) | Buyer-pinned region | Optional add-on |
| Enterprise | Buyer-selected from approved list including BYO-model | Buyer-pinned region | Yes — on-prem or sovereign cloud |
| Regulated | Locked to approved sovereign or in-region inference; model registry under buyer's CISO control | Buyer-pinned region | Default |

The model-gateway architecture must exist in the methodology; do not promise model-by-tier without it.

## Fair-Use Clause — Sample Language

> The Pro tier includes 5 000 AI-feature calls per tenant per month. Calls above this allowance are billed at $0.06 per call. The Customer's authorised usage is fair, ordinary-course business usage. Where the Customer's tenant usage exceeds 25 000 calls per month or 10 × the tier median, whichever is lower, the Supplier will notify the Customer within five business days and the parties will agree a commercial structure suitable to the new usage profile within thirty days. The Supplier will not throttle service during this notice period.

## Price-Increase Clause — Sample Language

> AI-feature pricing is subject to annual revision at the Customer's renewal date. Increases will not exceed (a) CPI in the Customer's billing country plus three percentage points, or (b) the weighted change in the Supplier's underlying model-provider list price plus a five-percent margin, whichever is the lower. The Supplier will provide ninety days' written notice of any revision. Where the underlying model-provider list price falls, the Supplier will pass through the reduction at the next renewal.

## Rollover and Forfeit Policy — Sample Language

> Unused AI-feature calls in any monthly billing period roll over for one billing period and are forfeit thereafter. Rollover credits are consumed before fresh-allowance credits in any month where both are present.

## Tier-Switch Language — Sample Language

> A tenant moving from the Standard tier to the Pro tier obtains immediate access to Pro-tier AI features including model selection within the Pro-tier model list. A tenant moving from Pro to Standard retains access to Pro-tier features until the end of the then-current billing period; at the next renewal, Standard-tier features apply and Pro-tier credits expire.

## FX Clause — Sample Language

> Where the Customer is billed in [local currency] and the Supplier's underlying model-provider cost is USD-denominated, the Supplier reserves the right to adjust AI-feature pricing where the prevailing exchange rate moves more than ten per cent against the agreed reference rate during any billing year. Adjustments will be capped at the proportional FX movement net of the Supplier's hedge benefit, and will be notified to the Customer no fewer than thirty days in advance.

## Worked Examples

### Worked Example A — Premium Tier as AI Upsell
Standard tier $99 / month, no AI; Pro tier $249 / month, AI included up to 5 000 calls; Enterprise tier $899 / month, AI included up to 25 000 calls plus model-by-tier. Attach 35 % at Pro, 12 % at Enterprise on 1 000 tenants. Annual AI-tier revenue = (350 × $150 ARPU uplift × 12) + (120 × $800 ARPU uplift × 12) = $630 000 + $1 152 000 = $1 782 000. Token cost at P90 = $64 / month / tenant × 350 = $22 400 / month × 12 = $269 000. Gross margin contribution $1 513 000.

### Worked Example B — Bundled with Fair-Use
$199 / month tier includes AI with 4 000 call fair-use. P99 tenant exceeds, triggers commercial conversation. Median tenant cost-of-tokens $9 / month — bundled is profitable. Without fair-use, a single 30 000-call tenant would consume $129 / month in tokens against $199 licence — margin damaged. Fair-use saves it.

### Worked Example C — Hybrid Floor + Overage
$129 / month floor includes 1 000 AI calls; $0.04 / call overage. Median tenant 800 calls — floor covered. Heavy tenant 6 500 calls — bills $129 + (5 500 × $0.04) = $129 + $220 = $349. Token cost $280 — healthy margin.

## Anti-Patterns Catalogue

- "Premium AI tier" with no defined model difference, no rate-limit difference, no fair-use difference. The tier is marketing, not pricing.
- "Usage-based credits" without a per-credit price or overage rate.
- "Industry-standard fair-use" without a number.
- "Subject to change with 30 days' notice" without an index or cap — procurement rejects.
- Volatile FX exposure held entirely by the agency without a clause.

## Cross-References

- `saas-pricing-models-reference.md` — base SaaS pricing patterns.
- `ai-on-saas-business-case-template.md` — cost-of-tokens at P50 / P90 / P99 inputs.
- `ai-on-saas-procurement-questionnaire-pack.md` — model-by-tier consistency in procurement answers.
- `ai-on-saas-objection-handling-playbook.md` — price objection plays.
