# Vertical AI-Agent — Financial Services

Vertical positioning, named agent use cases, autonomy stance, regulator framing, discriminators, and risk language for AI-agent bids in banking, payments, microfinance, capital markets, insurance-adjacent FS, and SACCOs. Pairs with `ai-agent-vertical-positioning`.

## Named Agent Use Cases (with autonomy and reversibility)

| Use case | Autonomy at go-live | Reversibility | Notes |
|---|---|---|---|
| KYC document triage and exception assembly | L3 | Reversible | Agent assembles; officer decides; never auto-onboards |
| AML alert disposition case assembly | L3 | Reversible | Agent prepares the disposition pack; named officer dispositions |
| Sanctions / watchlist triage | L3 | Reversible | Recall-prioritised eval; never auto-clears matches |
| Transaction reconciliation across systems | L3 | Reversible (read) + L1 (write) | Posts to ledger only with finance ops sign-off |
| Complaint classification and routing | L3 | Reversible | Routes to the right queue; never closes a complaint |
| Customer-facing RM copilot | L2 | Reversible | Drafts; advisor sends; bounded to non-advice replies |
| Reg-reporting drafting assistance | L1 / L2 | Irreversible at file | Drafts the figure pack; named reporting officer files |
| Credit decisioning support | L0 / L1 | Irreversible at decision | Assembles the case; the agent **never** approves or declines |
| Fraud signal explanation (post-hoc) | L3 | Reversible (read) | Explanatory only |

## Regulator Stance

Primary regulators across the agency's likely FS footprint:
- **Kenya**: CBK; Capital Markets Authority; Retirement Benefits Authority; SASRA; ODPC.
- **Uganda**: BoU; CMA; URBRA; PDPO.
- **Tanzania**: BOT; CMSA; SSRA.
- **Rwanda**: NBR; CMA; NCSA; NCDP.
- **Nigeria**: CBN; SEC; NAICOM (where group bancassurance applies); NDPC.
- **South Africa**: SARB / PA; FSCA; Information Regulator.
- **Cross-border**: Basel III / IV; FATF guidance on AI in AML; SR 11-7-style MRM for groups with US footprint; BCBS 239; PCI DSS for cards.

Vertical-specific agentic exposure:
- **Model-risk management** — the agent is added to the model inventory; independent validation cadence applies; ongoing monitoring; governance forum.
- **Algorithmic-decisioning** — credit, fraud, AML, sanctions: regulators sensitive to fairness, explainability, right to human review.
- **Sanctions** — recall-prioritised; false negatives catastrophic; the agent never auto-clears.
- **Conduct-of-business** — customer-facing agents must not mis-advise; complaints follow.
- **Adverse-decisioning rights** — affected customers can request a human review of any decision affecting their access to credit, accounts, or services.

## Discriminators for FS Bids

1. **Model-Risk Management overlay** — agent in the model inventory; independent validation cadence; ongoing monitoring; governance.
2. **HITL strict on decisioning** — the agent never approves or declines credit, fraud, AML, sanctions, or customer-facing advice; the agent assembles, an officer decides.
3. **Citation grounding on policy-Q&A and advisory** — every advisory output cites the controlling policy paragraph; auditor can trace.
4. **Region routing and sovereign-AI option** — for regulators sensitive to cross-border data on customer information.
5. **Audit access to logs** — regulator-grade access without breaking sub-processor confidentiality.
6. **Recall-prioritised eval for sanctions / AML** — proven discipline; quarterly false-negative drill.
7. **Reconciliation determinism with replay** — finance ops can reconcile what the agent did.

## Risk Framing — FS-Specific Language

- "Model risk" (not "AI quality").
- "Independent model validation" (not "we test the model").
- "Adverse-decisioning rights" (not "user override").
- "Sanctions list freshness SLA" with named cadence.
- "Suspicious-activity escalation path" for AML cases.
- "Conduct-of-business risk" for customer-facing AI.
- "Settlement reversibility" for ledger-touching agents.

## Sample Vertical Paragraph for Executive Summary

> Our financial-services agentic practice treats every agent as a model under model-risk management. Agents triage and assemble; named officers decide. The agent does not approve or decline a credit, an AML alert, a sanctions match, or a customer-facing advice on its own. The action catalogue is published, every action class is reversibility-classified, and irreversible actions — credit decisions, ledger writes, regulatory filings — are L1-gated with a named approver. The audit log is regulator-grade and replay-deterministic so an internal auditor or a supervisor can reconstruct any decision the agent influenced. A sovereign-AI option is available for the most sensitive tenants, and reconciliation agents commit to deterministic replay for finance operations.

## Pricing Pattern Notes

- Pattern D (per-agent) suits in-house operations (reconciliation, AML triage agents).
- Pattern E (hybrid) suits enterprise FS with predictable budgets and bursty volume.
- Pattern B (per-outcome) suits debt-recovery agents with attribution clauses.
- Avoid Pattern A (per-resolution) for any decisioning workflow.

## Cross-References

- `vertical-saas-positioning-financial-services.md` — base FS SaaS positioning.
- `vertical-ai-on-saas-financial-services.md` — AI-on-SaaS FS positioning.
- `ai-agent-risk-register-for-proposals.md` — R-AG-FS-01 (sanctions false negatives) and R-AG-FS-02 (settlement reversibility).
- `ai-agent-responsible-ai-commitment.md` — commitment mapped to FS regulators.
- `ai-agent-trust-and-compliance-template.md` — FS rows in compliance map.
