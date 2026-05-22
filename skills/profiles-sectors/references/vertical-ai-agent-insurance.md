# Vertical AI-Agent — Insurance

Vertical positioning, named agent use cases, autonomy stance, regulator framing, discriminators, and risk language for AI-agent bids in life, non-life, health insurance, and reinsurance support. Pairs with `ai-agent-vertical-positioning`.

## Named Agent Use Cases (with autonomy and reversibility)

| Use case | Autonomy at go-live | Reversibility | Notes |
|---|---|---|---|
| Claims-document triage and categorisation | L3 | Reversible | Sorts and prioritises; never closes |
| First-notification-of-loss summarisation | L3 | Reversible | Drafts the FNOL pack; handler reviews |
| Fraud-signal assembly (post-hoc) | L3 | Reversible | Agent assembles; named officer decides |
| Subrogation candidate identification | L3 | Reversible | Flags; lawyer / handler reviews |
| Policy-comparison drafting for customer service | L2 | Reversible | Bounded to factual comparison; not advice |
| Underwriting evidence grounding | L2 / L3 | Reversible | Assembles evidence; underwriter decides |
| Declinature or payout decisioning | L0 / L1 | Irreversible | The agent **never** declines or pays out on its own |
| Customer communications drafting | L2 | Reversible | Drafts; handler approves and sends |

## Regulator Stance

- **Kenya**: IRA; ODPC.
- **Uganda**: IRA Uganda; PDPO.
- **Tanzania**: TIRA.
- **Rwanda**: NBR (insurance regulation); NCDP.
- **Nigeria**: NAICOM; NDPC.
- **South Africa**: FSCA; Information Regulator; Prudential Authority.
- **Cross-border**: Solvency-II-adjacent regimes where applicable; conduct-of-business rules in market.

Vertical-specific exposure:
- **Conduct of business** — fair treatment of customers; advice rules; complaint handling.
- **Claims fairness** — agent-assisted triage must not embed bias against claimant groups.
- **Adverse-decisioning rights** — claimants can request human review of any declinature or partial payout.
- **Data minimisation** — health and financial data subject to strict use rules.

## Discriminators for Insurance Bids

1. **Explainability of triage** — every flag carries a reason a handler can read and override.
2. **HITL strict on declinature and payout** — the agent never decides these; it assembles.
3. **Citation grounding on policy answers** — every customer-facing factual answer cites the policy paragraph.
4. **Complaint-channel awareness** — agent-handled cases that generate complaints surface fast; the agent is not used to deflect complaints.
5. **Sectoral retraining for claims handlers** — the doer-to-supervisor transition is funded.
6. **Audit completeness for regulator-driven reviews** — replay-deterministic for forensic review.

## Risk Framing — Insurance-Specific Language

- "Claims fairness" (not "AI quality on claims").
- "Adverse-decisioning rights" for declinatures.
- "Conduct-of-business risk" for customer-facing communications.
- "Fraud signal" (not "fraud detection") for post-hoc assembly.
- "Complaint trail" as a quality signal.

## Sample Vertical Paragraph for Executive Summary

> Our insurance agentic practice keeps claims handling honest. The agent triages, summarises, and assembles; the named claims handler decides. The agent does not decline, does not pay out, and does not communicate declinature reasons on its own. Every flag carries an explanation a handler can read and override. Customer-facing factual replies are citation-grounded to the policy paragraph. Claims handlers shift from doer to supervisor with a funded retraining curriculum; supervisor CSAT and complaint trail are tracked alongside resolution rate. The audit log is regulator-grade so that a conduct-of-business review can reconstruct any case.

## Pricing Pattern Notes

- Pattern C (per-step) or D (per-agent) suits insurance — outcome attribution is messy.
- Pattern E (hybrid) for enterprise insurers with predictable base and overage tail.
- Avoid Pattern B (per-outcome) without strong attribution clauses.

## Cross-References

- `vertical-saas-positioning-insurance.md`
- `vertical-ai-on-saas-insurance.md`
- `ai-agent-risk-register-for-proposals.md` — R-AG-INS-01 (claims fairness; conduct complaint cluster).
- `ai-agent-responsible-ai-commitment.md`
- `ai-agent-trust-and-compliance-template.md`
