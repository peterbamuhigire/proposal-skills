# Vertical AI-Agent — Public Sector

Vertical positioning, named agent use cases, autonomy stance, regulator framing, discriminators, and risk language for AI-agent bids in public sector — ministries, agencies, parastatals, county / local government, judiciary administration, revenue authorities, and citizen-service hubs. Pairs with `ai-agent-vertical-positioning`. **Extreme caution applies.**

## Named Agent Use Cases (with autonomy and reversibility)

| Use case | Autonomy at go-live | Reversibility | Notes |
|---|---|---|---|
| Citizen-FAQ and information retrieval (cited) | L2 / L3 | Reversible | Cited answers from controlled regulation / policy |
| Case routing inside ministries | L3 | Reversible | Triage; routing; never closes a case |
| Multilingual translation of forms / responses | L2 / L3 | Reversible | Translates; officer reviews where legally consequential |
| Complaint triage and routing | L3 | Reversible | Categorises; never resolves |
| Document understanding (procurement, judiciary admin) | L2 / L3 | Reversible | Extracts; officer adjudicates |
| Non-decisioning support to caseworkers | L2 / L3 | Reversible | Drafts; caseworker decides |
| Benefit / status / immigration / tax / criminal-justice decisioning | **L0** | Irreversible | The agent **does not decide** on citizen rights or entitlements |

## Regulator Stance

- **Kenya**: NCAIS principles; ODPC; sectoral ministries; County governments where devolved.
- **Uganda**: NITA-U guidance; PDPO; sectoral ministries.
- **Tanzania**: ZICTA; sectoral.
- **Rwanda**: RGB; National AI Policy; NCDP.
- **Nigeria**: NAIS; NDPC; sectoral.
- **South Africa**: ICASA / DCDT; Information Regulator; sectoral.
- **EAC and AU**: emerging frameworks; sovereign-AI expectations.

Vertical-specific exposure:
- **Administrative-law fairness** — citizens have a right to a reasoned decision and to human review.
- **Right to be heard** — affected citizens can contest before adverse decisions where the rule provides.
- **Transparency-to-affected-party** — citizens are informed they are interacting with or being acted upon by an agent.
- **Sovereign-AI expectations** — many public-sector buyers expect on-prem or in-country inference.
- **Local-language obligations** — services in the country's official and major working languages.

## Discriminators for Public-Sector Bids

1. **Sovereign-AI option** — open-weight model hosted on dedicated GPU; on-prem inference; in-country audit log; mirror to ministry SOC where required.
2. **Local-language depth** — English, Swahili, Luganda, Kinyarwanda, French, Arabic, Yoruba, Igbo, Hausa, Zulu, Afrikaans as relevant; not machine-translated as an afterthought.
3. **Administrative-law literacy** — agents do not decide; the action catalogue makes this explicit and auditable.
4. **Transparency-to-affected-party UX** — every external communication discloses; contestability is published.
5. **Published action catalogue** — citizens, civil society, and the regulator can read what the agent will do.
6. **Quarterly kill-switch drill with regulator observer** — public confidence requires it.
7. **Public-sector procurement literacy** — alignment with PPDA / KPPRA / KPPRB equivalents; appropriate framework agreements.

## Risk Framing — Public-Sector-Specific Language

- "Administrative-law fairness" (not "AI quality").
- "Right to a reasoned decision".
- "Right to human review".
- "Transparency-to-citizen".
- "Sovereign-AI" or "data sovereignty".
- "Inclusion" — language coverage, accessibility, digital-divide.
- "Procurement integrity" — the agent supports procurement, never decides procurement.

## The Honesty Principle

The proposal does not promise citizen-service agents that take decisions on citizens. Public-sector buyers reward this honesty; competitors who over-promise lose to enforcement or to public backlash. If the buyer asks for autonomous benefit determinations or immigration decisions, the agency declines politely and proposes the assemble-then-decide model with a named officer.

## Sample Vertical Paragraph for Executive Summary

> Our public-sector agent practice begins with what an agent must not do. Agents do not decide on benefits, status, tax, or justice; agents assemble the case, in the language the citizen speaks, with citations to the controlling regulation, and a named officer decides. The action catalogue is published. Every external communication discloses the agent and offers an immediate route to a human. A sovereign-AI deployment is supported where the ministry requires data and inference to remain in country. The kill-switch drill runs quarterly, and we welcome a regulator observer where invited. Adoption is engineered through a funded caseworker retraining curriculum and a published contestability channel.

## Pricing Pattern Notes

- Pattern D (per-agent) is the recommended starting point — outcome pricing on citizen services is politically inappropriate.
- Hybrid with included case volume can work for high-volume citizen-FAQ.
- Sovereign-AI deployments carry a premium and longer sales cycle.

## Cross-References

- `vertical-saas-positioning-public-sector.md`
- `vertical-ai-on-saas-public-sector.md`
- `ai-agent-risk-register-for-proposals.md` — R-AG-PUB-01 (administrative-law fairness); R-AG-PUB-02 (sovereign-AI; data residency).
- `ai-agent-responsible-ai-commitment.md`
- `ai-agent-trust-and-compliance-template.md`
- `sectors/SKILL.md` — public-sector procurement frameworks.
