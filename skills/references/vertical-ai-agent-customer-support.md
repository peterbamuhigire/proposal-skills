# Vertical AI-Agent — Customer Support

Vertical positioning, named agent use cases, autonomy stance, regulator framing, discriminators, and risk language for AI-agent bids in customer support. Pairs with `ai-agent-vertical-positioning`.

## Named Agent Use Cases (with autonomy and reversibility)

| Use case | Autonomy at go-live | Reversibility | Notes |
|---|---|---|---|
| Ticket triage and routing | L3 | Reversible | Agent classifies, routes, tags; misrouting is reversible |
| FAQ deflection (self-serve) | L3 | Reversible | Agent answers from cited KB; user can always reach a human |
| Agent-assist (suggest reply, draft macro, find article) | L2 | Reversible | Human-agent (CS rep) reviews and sends |
| End-to-end resolution within bounded value | L2 / L3 | Mixed | Refund up to value bound (L1), status update (L3), ticket close (L3) |
| Refund or chargeback authorisation | L1 | Irreversible | Named human approval; value-bound dual approval above threshold |
| Cancellation or account closure | L1 | Irreversible | Named human approval; cooling-off where applicable |
| Voice-of-customer summarisation | L3 | Reversible | Analytical, no customer-facing action |

## Discriminators for Customer-Support Bids

1. **Containment-vs-deflection honesty** — deflection is good if the user is helped; containment is bad if the user gave up. We measure resolution, not containment.
2. **Agent-assist before agent-replace framing** — Stage 2 of trust staging is human-agent + AI; full agentic resolution is staged and bounded.
3. **Escalation SLA with named human** — every customer can reach a human; the escalation SLA is named and measured.
4. **Multilingual depth** — support for the buyer's customer languages (English, Swahili, Luganda, Kinyarwanda, French, Arabic, Yoruba, Igbo, Hausa, Zulu, Afrikaans as relevant).
5. **Supervisor retraining curriculum** — funded; agents shift from doer to supervisor with new authority.
6. **Transparency UX** — every agent message discloses; voice agents identify at the start.

## Risk Framing — Customer-Support Language

- **Resolution quality** (not "AI quality").
- **Containment-vs-resolution** (not just deflection).
- **Reopen rate** as a quality signal.
- **Escalation rate** as an agent-confidence signal.
- **Customer-satisfaction post-agent** (CSAT specifically on agent-handled tickets).
- **First-contact resolution** as the gold metric.

## Sample Vertical Paragraph for Executive Summary

> Our customer-support agentic practice optimises for resolution, not containment. The agent triages, routes, and resolves the routine within published value bounds; the human supervises the queue and handles the exception. Every customer reaches a human at any moment by replying HUMAN or by clicking the route in the agent's signed reply. Refunds, cancellations, and account closures require named human approval; the agent never authorises money out on its own. The supervisor's role is reskilled with a funded curriculum, and adoption is tracked by supervisor CSAT and queue headroom alongside resolution rate and customer satisfaction.

## Pricing Pattern Notes

- Pattern A (per-resolution) suits high-volume defined-outcome work; define "resolution" with the no-reopen-for-N-days rule.
- Pattern E (hybrid) for enterprise buyers with predictable budgets.
- Pattern F (success-based) for trust-building return engagements with mature buyers.

## Cross-References

- `vertical-saas-positioning-customer-support.md` if SaaS context exists.
- `ai-agent-risk-register-for-proposals.md` — R-AG-CS-01 (containment-without-resolution complaints) where applicable.
- `ai-agent-change-management-playbook.md` — supervisor retraining; union consultation.
- `ai-agent-pricing-models-reference.md` — pattern selection and clauses.
