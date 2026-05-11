# Vertical AI-Agent — Healthcare

Vertical positioning, named agent use cases, autonomy stance, regulator framing, discriminators, and risk language for AI-agent bids in healthcare — hospital systems, payers / schemes (SHA / NHIF / NHIS), provider networks, and digital-health platforms. Pairs with `ai-agent-vertical-positioning`. **Admin-only by default.**

## Named Agent Use Cases (with autonomy and reversibility)

| Use case | Autonomy at go-live | Reversibility | Notes |
|---|---|---|---|
| Clinical-documentation drafting (summary, discharge letter, referral) | L2 | Reversible | Clinician signs every artefact; agent never finalises |
| Prior-authorisation triage | L3 | Reversible | Agent prepares the pack; payer-side officer decides |
| Claims and billing reconciliation | L3 | Reversible (read) + L1 (post) | Posts only with finance ops sign-off |
| Appointment scheduling and follow-up | L3 | Reversible | Routine scheduling; cancellation > value-bound requires HITL |
| Hospital-operations triage (bed, supply, theatre) | L3 | Reversible | Operational signals; supervisor decides allocation |
| Patient-FAQ retrieval (non-clinical) | L2 / L3 | Reversible | Bounded to admin / wayfinding / billing |
| Clinical decisioning (diagnosis, treatment, dose, acuity) | **L0** | Irreversible | The agent **does not do this** under our methodology |

## Regulator Stance

- **Kenya**: Ministry of Health; KMPDC; Nursing Council of Kenya; SHA / SHIF; ODPC; KEMRI for research.
- **Uganda**: Ministry of Health; UMDPC; UNMC; NHIS-Uganda emerging; PDPO.
- **Tanzania**: Ministry of Health; MCT; NHIF.
- **Rwanda**: Ministry of Health; Rwanda Medical and Dental Council; RSSB-Medical; NCDP.
- **Nigeria**: Ministry of Health; MDCN; NHIS; NDPC.
- **South Africa**: National Department of Health; HPCSA; Council for Medical Schemes; Information Regulator.
- **Cross-border**: HIPAA where US-linked; clinical-decision-support classification (e.g. SaMD).

Vertical-specific exposure:
- **Clinical-decision-support classification** — the line where AI becomes a medical device.
- **Clinical confidentiality** — POPIA / DPA Kenya / NDPA Nigeria / DPPA Uganda / DPL Rwanda; data minimisation; retention rules.
- **Professional standards** — clinicians remain professionally responsible.
- **Insurance / payer interactions** — fraud / waste / abuse rules.

## Discriminators for Healthcare Bids

1. **Explicit admin-only scope** — the action catalogue makes the non-clinical boundary explicit and auditable.
2. **Clinician-in-the-loop on every drafted clinical artefact** — discharge summaries, referrals, summaries; the clinician signs.
3. **Audit-log retention matched to clinical record-keeping rules** — typically seven years minimum, longer where the rule applies.
4. **Residency and on-prem** — sovereign-AI option where the buyer requires.
5. **Multilingual** — patient and clinician languages.
6. **Strict tenant confinement** — no cross-facility memory; per-tenant memory and audit.

## Risk Framing — Healthcare-Specific Language

- "Non-clinical scope" (not "AI quality").
- "Clinician-final" on every clinical artefact.
- "Patient confidentiality" (not "data privacy" generic).
- "Clinical-decision-support classification" — discussed honestly.
- "Adverse-event reporting" — readiness to report.

## Sample Vertical Paragraph for Executive Summary

> Our healthcare agent practice is explicitly admin-only. Agents draft discharge summaries, route prior-authorisations, reconcile claims, schedule follow-ups; agents do not diagnose, do not triage clinical acuity for life-critical care, and do not recommend treatment. Every drafted clinical artefact is signed by the responsible clinician. The action catalogue makes the non-clinical boundary explicit and auditable. Any expansion across that boundary is classified as a regulated-device decision that pauses the engagement until the regulator concurs. Patient confidentiality is honoured by per-tenant memory, in-country audit log, and a sovereign-AI deployment for tenants whose data must not leave the country.

## Pricing Pattern Notes

- Pattern D (per-agent) suits hospital operations and payer admin.
- Pattern E (hybrid) for payer networks with predictable volume + bursty claims periods.
- Avoid Pattern A (per-resolution) on anything touching a clinical decision.

## Cross-References

- `vertical-saas-positioning-healthcare.md`
- `vertical-ai-on-saas-healthcare.md`
- `ai-agent-risk-register-for-proposals.md` — R-AG-HEALTH-01 (clinical-scope drift).
- `ai-agent-responsible-ai-commitment.md`
- `ai-agent-trust-and-compliance-template.md`
