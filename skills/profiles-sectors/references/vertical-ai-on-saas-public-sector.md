# Vertical AI-on-SaaS — Public Sector

Vertical positioning, named AI use cases, regulator stance, discriminators, and risk language for AI-on-SaaS bids in ministries, agencies, regulators, judiciary, and public-service portals. Pairs with `ai-on-saas-vertical-positioning` and extends `vertical-saas-positioning-public-sector.md`.

## Named AI Use Cases

| Use case | Hallucination tolerance | HITL stance | Risk class |
|---|---|---|---|
| Citizen-FAQ copilot on a government portal | ≤ 2 % with citations | Trusted reference; complaint channel | Medium |
| Case routing and triage (e.g. complaint inbox, judicial filings, procurement) | F1 ≥ 0.85 | HITL on assignment | Medium |
| Multilingual translation / accessibility | Domain-checked | Reviewer for legal text | Medium |
| Document understanding (procurement, regulator filings, judicial documents) | ≤ 1 % on extracted fields | HITL on adverse decisioning | High |
| Policy-Q&A copilot for internal staff (with citations) | ≤ 0.5 % with citations | Trusted internal reference | Medium |
| Procurement-evaluation assistance (scoring assistance only) | Recommendation only | HITL strict; no auto-scoring | High |

## Regulator Stance

- **Kenya**: NCAIS principles (National AI Strategy); ODPC; ICTA / Ministry of ICT; NCIC where applicable.
- **Uganda**: NITA-U AI guidance; PDPO; sector ministries.
- **Tanzania**: e-Government Authority; Personal Data Protection Commission.
- **Rwanda**: National AI Policy (NCSA); NCDP.
- **Nigeria**: NAIS; NDPC; NITDA.
- **South Africa**: draft AI policy (DCDT); Information Regulator.
- **Cross-border / EAC**: EAC AI position (emerging); AU Continental AI Strategy.

Vertical-specific AI exposure:
- **AI sovereignty** — many African public-sector buyers are actively discussing sovereign-AI requirements; on-prem or in-country inference is a common ask.
- **Procurement-grade AI** — public-sector procurement is sensitive to transparency, fairness, and the right to audit; black-box AI is rejected.
- **Citizen-facing AI** — accessibility (language, disability) and complaint mechanisms are required, not optional.
- **Public-record exposure** — outputs of AI features may become public records subject to access-to-information laws.

## Discriminators for Public-Sector Bids

1. **Sovereign-AI option from day one** — open-weight models, in-country hosting partner, GPU sourcing readiness, pricing differential.
2. **Procurement-grade transparency** — model cards published; sub-processor list public; eval methodology auditable.
3. **Local-language coverage** — Swahili, Kinyarwanda, Luganda, Yoruba, Hausa, Igbo, isiZulu, isiXhosa, Afrikaans, Amharic — name the languages, name the eval method per language.
4. **Citizen-redress mechanism** — public complaint channel; first-response SLA; published quarterly redress summary.
5. **No-decisioning framing on adverse outcomes** — AI does not deny benefits, decline applications, or score citizens; AI assembles and recommends; the named civil servant decides.

## Risk Framing — Public-Sector-Specific Language

- "Sovereignty of data and inference."
- "Right to administrative justice" (no automated adverse decisions).
- "Access-to-information exposure" on AI outputs.
- "Accessibility obligation" per disability and language coverage.
- "Procurement transparency."

## Sample Vertical Paragraph

> Public-sector AI-on-SaaS engagements require an architecture and a commitment that procurement, audit, and the regulator can trace. We design every public-sector AI feature with a sovereign-AI option — open-weight models, in-country hosting, and GPU sourcing — so that the buyer's choice between multi-tenant cloud and sovereign deployment is real, not theoretical. We publish model cards, sub-processor lists, and eval methodology so that the buyer's procurement team can audit the AI behaviour as readily as it audits any other public-service control. We do not write AI features that decide adverse outcomes; the AI assembles, recommends, and explains, and the named civil servant decides — preserving the citizen's right to administrative justice. Local-language coverage is named per feature with the eval method per language.

## Cross-References

- `vertical-saas-positioning-public-sector.md`.
- `ai-on-saas-risk-register-for-proposals.md` — R-AI-PS-01 sovereign mandate.
- `ai-on-saas-responsible-ai-commitment.md`.
- `ai-on-saas-trust-and-compliance-section-template.md`.
