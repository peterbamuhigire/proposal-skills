# SaaS Pricing Models Reference

Reference for proposing SaaS pricing models inside implementation and product-development engagements. Use for two purposes:

1. **For internal-use SaaS**: structuring how the agency prices its own implementation, customer-success, and managed-service fees that wrap around a third-party SaaS subscription.
2. **For resale SaaS**: designing the client's commercial model when the client is launching or relaunching a SaaS product to its own customers.

## Pricing Model Patterns

### Subscription (per-seat, per-period)
The default. Annual or monthly, per active user or per named user. Strong for enterprise SaaS with stable user counts and predictable use.

- **Strengths**: predictable revenue, easy procurement, simple internal allocation.
- **Risks**: ceiling once seat count saturates, poor fit for variable workloads, encourages seat-hoarding (active vs named).
- **Use when**: enterprise B2B with stable headcount; clear seat = value mapping.

### Usage-Based (per-transaction, per-API-call, per-volume)
Pay for what you use. Increasingly common in infrastructure SaaS, payments SaaS, communications SaaS, and AI-feature SaaS.

- **Strengths**: zero adoption friction, customer value tracks vendor revenue, expansion is automatic.
- **Risks**: revenue volatility, harder budgeting on the buyer side, requires accurate metering.
- **Use when**: usage is the natural value proxy; customer can self-throttle.

### Hybrid (subscription floor + usage above)
A subscription floor covers committed value; overage charges apply above the floor. Combines predictability with expansion.

- **Strengths**: predictable base + automatic expansion, both sides protected.
- **Risks**: complexity, harder to compare against competitors.
- **Use when**: usage varies materially across customers but a minimum commitment is fair.

### Enterprise Tiering (Starter / Pro / Enterprise)
Three named tiers with explicit feature, support, and integration gating between tiers.

- **Strengths**: clear upgrade path, defensible feature differentiation, supports both self-serve and sales-led motion.
- **Risks**: over-engineering the middle tier; "good-better-best" trap where middle tier is the only one that sells.
- **Use when**: the SaaS serves a broad spectrum of customer sizes and willingness-to-pay.

### Outcome-Based (per-claim-processed, per-loan-approved, per-tonne-tracked)
Vendor is paid for the business outcome delivered, not the platform. Rare but powerful in vertical SaaS where the outcome is clearly attributable.

- **Strengths**: maximum alignment, allows premium pricing.
- **Risks**: attribution disputes, longer sales cycle, requires shared instrumentation.
- **Use when**: outcome is unambiguous and instrumentable; buyer is sophisticated.

### Capacity-Based (per-CPU, per-record-stored, per-tenant)
Pay for provisioned capacity rather than usage. Common in regulated industries that pre-allocate.

- **Use when**: regulator or risk function requires reserved capacity; tenant isolation is silo-heavy.

## Tier Ladder Design (Starter / Pro / Enterprise)

| Dimension | Starter | Pro | Enterprise |
|---|---|---|---|
| Target customer | SMB / departmental | Mid-market / division | Enterprise / multi-business-unit |
| Users included | Capped low | Capped mid | Unlimited or high cap |
| Core features | Limited | Full core | Full core + advanced |
| Integrations | Standard library | Standard + custom | Standard + custom + dedicated integration support |
| Support | Self-serve + community | Business hours, email/chat | 24x7, named CSM |
| SLA | Best-effort | 99.5% | 99.9%+ with credits |
| Security | Standard | + SSO, SAML | + dedicated infrastructure, custom DPA, sub-processor restrictions |
| Data residency | Default region | Region choice | Multi-region, dedicated |
| Contract | Month-to-month | Annual | Multi-year, custom |
| Price discipline | Public | Public with discount bands | Negotiated |

## Expansion Path Design

Every SaaS commercial model proposed for a client should include an explicit expansion path:

- **Per-seat expansion**: triggers when the customer adds users.
- **Per-volume expansion**: triggers when usage crosses tier thresholds.
- **Per-feature expansion**: triggers when the customer activates feature-gated capabilities.
- **Per-integration expansion**: triggers when the customer wants integrations beyond the standard library.
- **Per-success expansion**: triggers when the customer adopts a higher-touch success package.

Each trigger has a defined commercial conversation pattern, an owner on the agency side (customer success or sales), and a measurable signal that surfaces it.

## Freemium vs Paid Trial Decision

| Question | Freemium | Paid Trial |
|---|---|---|
| Is the product valuable at low usage? | Yes → freemium possible | No → freemium will not convert |
| Does the product have viral or social loops? | Yes → freemium amplifies acquisition | No → freemium is just discounting |
| Is acquisition CAC structurally low? | Yes | No → paid trial filters better |
| Is trial-quality more important than trial-quantity? | No | Yes → paid trial |
| Does the buyer expect credit-card-up-front? | No | Yes |

Default position when uncertain: paid trial with card on file, 14–30 days, full feature access, automatic conversion to paid with explicit reminder.

## Price-Increase Clause

Every multi-year SaaS contract should include a price-increase clause to prevent erosion:

- **Cadence**: annual on contract anniversary, or every 24 months.
- **Cap**: capped at inflation + N%, where N is typically 3–5 percentage points.
- **Communication**: 90 days written notice with the new effective price.
- **Grandfathering**: optional for the first N years of an enterprise customer's tenure.
- **Operational steps**: billing system updated, customer success informs accounts in advance, sales handles escalations.

## Pricing Model Selection Decision

Use this decision sequence when designing a client's resale SaaS pricing:

1. Is usage the natural value proxy and is it cleanly metered? → consider usage or hybrid.
2. Is the buyer's procurement organisation comfortable with variable spend? → if no, default to subscription or hybrid with a strong floor.
3. Does the SaaS serve a wide range of customer sizes? → enterprise tiering is essential.
4. Is there an unambiguous outcome that all parties trust? → consider outcome-based.
5. Does the regulator pre-allocate capacity? → consider capacity-based.

Most proposed models will be hybrid (subscription floor + tiering + expansion path + price-increase clause).

## African and Regional Considerations

- Currency: USD price points for enterprise; local currency for SMB. Always state currency in every commercial table.
- Withholding tax: state assumption explicitly; some jurisdictions withhold significantly on subscription payments to foreign SaaS vendors.
- Payment infrastructure: mobile-money, USSD, and bank-transfer realities affect how SMB SaaS collects revenue. Direct debit is not universally available.
- Regulator stance on cloud-hosted SaaS varies by country and sector; tier design must accommodate dedicated-infrastructure tier for regulated customers.

## Anti-Patterns

- Single-tier pricing for a SaaS serving SMB through enterprise.
- Usage-based pricing without accurate metering or customer-facing cost-control tools.
- Freemium that converts at less than 3% — wasting infrastructure and support cost.
- Annual price increases higher than 8% without a grandfathering policy — accelerates churn.
- Hidden professional-services fees that make the headline subscription price misleading.
- "Custom enterprise pricing" with no public anchor — buyers feel they have nothing to evaluate.

## See Also

- `saas-business-case-and-roi-template.md` for the commercial-model output in proposals.
- `saas-metrics-glossary-for-proposals.md` for vocabulary.
- `premium-rate-justification-framework.md` for premium fee defence.
- `../10-financial-proposal/SKILL.md` for the financial proposal section discipline.
