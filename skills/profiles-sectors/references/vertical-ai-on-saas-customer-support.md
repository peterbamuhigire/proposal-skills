# Vertical AI-on-SaaS — Customer Support

Vertical positioning, named AI use cases, KPI honesty, discriminators, and risk language for AI-on-SaaS bids in customer support SaaS, contact-centre platforms, and support-function AI. Pairs with `ai-on-saas-vertical-positioning`.

## Named AI Use Cases

| Use case | Hallucination tolerance | HITL stance | Risk class |
|---|---|---|---|
| Deflection / self-service copilot (in-product or on portal) | ≤ 2 % with citation; abstain when uncertain | Escalation to agent on abstain | Medium |
| Ticket triage and routing (category, priority, language, region) | F1 ≥ 0.90 on top categories | HITL on outliers | Low–Medium |
| Agent-assist copilot (suggests reply, retrieves knowledge) | ≤ 2 % advisory; agent confirms before send | Agent is named author | Medium |
| Voice-of-customer analytics (themes, sentiment, intent) | Aggregate-only; cohort verified | Analyst reviews | Low |
| Macro authoring and knowledge-base maintenance | Drafting only | KB owner curates | Low |
| Outbound message drafting (proactive support) | ≤ 2 % advisory; CS lead reviews | HITL by CS lead | Medium |

## Regulator Stance

- General data-protection regulators apply (ODPC, NDPC, Information Regulator, PDPO, NCDP, GDPR for EU customers).
- Sectoral regulators apply where the support is for regulated services (FS, insurance, healthcare).
- Consumer-protection bodies (CAK, CPC, FCCPC, NCC where relevant) on automated communications.

Vertical-specific AI exposure:
- **Containment vs deflection honesty** — the metric most vendors over-claim. Containment ≠ resolution. The proposal must distinguish "ticket closed in self-service" from "issue resolved without escalation in N days."
- **Agent-replace temptation** — agencies tempted to promise headcount reduction. The honest framing is agent-assist with mix-shift, not agent-replace.
- **Customer-facing AI disclosure** — many jurisdictions are moving toward AI-disclosure obligations on customer-facing automated communications.

## Discriminators for Customer-Support Bids

1. **Honest containment metric** — distinguish self-service-closed from issue-resolved-without-escalation; track both; report both.
2. **Agent-assist framing over agent-replace** — explicit augment framing; mix-shift modelling, not headcount-reduction modelling.
3. **Citation-grounded answers** — deflection copilot cites the knowledge-base article; agent-assist cites the macro or KB.
4. **Escalation SLA on abstain** — when the AI abstains, the customer reaches a human within a stated SLA.
5. **Language coverage with per-language eval** — name the languages and the eval method per language; do not list languages with no eval.

## Honest KPI Definitions

| KPI | Honest definition |
|---|---|
| Containment rate | Tickets closed in self-service without agent interaction |
| Resolution rate | Tickets where the underlying issue did not return within N days |
| Deflection ROI | Containment × labour saved − cost-per-call − eval cost |
| First-contact-resolution lift | FCR with AI − FCR baseline |
| Average handle time delta | AHT with AI − AHT baseline (positive = AI made it slower; check abandonment + transfer) |
| CSAT delta | CSAT with AI − CSAT baseline |
| Agent override rate | Agent-assist suggestions overridden by agent |
| Escalation SLA on abstain | Median time from AI-abstain to human-agent contact |

## Risk Framing — Support-Specific Language

- "Containment honesty."
- "Agent-assist mix-shift."
- "Customer-facing AI disclosure."
- "Macro / KB freshness SLA."
- "Escalation-on-abstain SLA."

## Sample Vertical Paragraph

> Our customer-support AI-on-SaaS practice is built on metric honesty. Containment is not resolution; we measure both. The deflection copilot is designed to abstain when it should not answer, and we publish an escalation-on-abstain SLA so the customer reaches a human within a stated time. The agent-assist copilot is named as exactly that — the agent remains the author of the reply, the AI suggests, the agent confirms. Where the engagement promises commercial impact, we model agent-assist mix-shift (more agents resolving more complex tickets faster), not headcount reduction, unless the buyer's strategy is explicit and the consultation is in place. Customer-facing AI is disclosed per the jurisdiction. Per-language eval is published per supported language. The voice-of-customer analytics surface themes and cohorts the support leadership can act on, signed off quarterly by a named analyst.

## Cross-References

- `ai-on-saas-risk-register-for-proposals.md`.
- `ai-on-saas-responsible-ai-commitment.md`.
- `ai-on-saas-trust-and-compliance-section-template.md`.
- `ai-on-saas-metrics-glossary.md` — adoption and override-rate definitions.
