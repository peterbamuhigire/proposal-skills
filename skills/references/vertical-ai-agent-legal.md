# Vertical AI-Agent — Legal

Vertical positioning, named agent use cases, autonomy stance, regulator framing (bar rules), discriminators, and risk language for AI-agent bids in law firms, in-house legal teams, judicial administration, and legal-tech operations. Pairs with `ai-agent-vertical-positioning`. **Lawyer remains the responsible party.**

## Named Agent Use Cases (with autonomy and reversibility)

| Use case | Autonomy at go-live | Reversibility | Notes |
|---|---|---|---|
| Contract first-draft generation and clause comparison | L2 | Reversible | Lawyer reviews and edits |
| Due-diligence document review | L3 | Reversible | Agent flags; lawyer adjudicates |
| Legal-research synthesis with citations | L2 / L3 | Reversible | Citation-grounded; lawyer verifies |
| Filing assembly (briefs, motions, regulatory) | L1 / L2 | Irreversible at file | Agent assembles; lawyer files |
| E-discovery triage | L3 | Reversible | Categorises and prioritises |
| Client-intake drafting | L2 | Reversible | Drafts; lawyer reviews; client sees only lawyer-approved output |
| Legal advice to clients | **L0** | Irreversible | The agent **does not advise**; the lawyer advises |
| Filings, court communications, or any communication purporting to bind a client | **L0** | Irreversible | Lawyer-final always |

## Regulator Stance

- **Kenya**: Law Society of Kenya; bar admission and practice rules.
- **Uganda**: Uganda Law Society; advocates' professional conduct rules.
- **Tanzania**: Tanganyika Law Society; Zanzibar Law Society.
- **Rwanda**: Rwanda Bar Association.
- **Nigeria**: NBA; Rules of Professional Conduct for Legal Practitioners.
- **South Africa**: LPC; rules under the Legal Practice Act.
- **Cross-border**: SRA (UK-aligned), ABA Model Rules (US-aligned), bar association rules in target jurisdictions.

Vertical-specific exposure:
- **Lawyer responsibility / unauthorised practice** — agents cannot give legal advice in the lawyer's name without lawyer sign-off.
- **Client confidentiality and privilege** — tenant scope must enforce confidentiality; no shared memory across firms or clients.
- **Filing accuracy** — hallucinated citations are professional misconduct.
- **Conflicts of interest** — agents must not introduce conflicts via shared memory or cross-tenant context.

## Discriminators for Legal Bids

1. **Confidentiality by tenant scope** — no shared memory across firms; per-firm and where relevant per-matter memory.
2. **Citation grounding** — every cited case, statute, or regulation is verified by a verifier component before output reaches a lawyer.
3. **Lawyer-final on every filing and communication** — the agent never sends to court or to a client without lawyer sign-off.
4. **Conflict-check awareness** — agent operates within the firm's conflict-check rules; surface flags.
5. **Audit log to bar-defensible standard** — the firm can show what the agent did in any professional-conduct review.
6. **Insurance alignment** — agency E&O aligned to firm's professional indemnity.

## Risk Framing — Legal-Specific Language

- "Lawyer responsibility" (not "AI quality").
- "Privilege and confidentiality" (not "data privacy" generic).
- "Citation accuracy" (not "hallucination rate" generic).
- "Professional conduct" — the gold standard.
- "Conflict of interest" — managed explicitly.

## Sample Vertical Paragraph for Executive Summary

> Our legal agent practice keeps the lawyer at the centre of every filing and every client communication. Agents draft, compare, triage e-discovery, and synthesise research; lawyers verify, edit, advise, and file. Citations are verified by a component before any output reaches a lawyer's screen, eliminating hallucinated cases from the workflow. Confidentiality is enforced by tenant scope — no shared memory across firms — and conflict-check rules are surfaced as flags inside the agent's reasoning. The audit log is bar-defensible so a professional-conduct review can reconstruct what the agent did on any matter.

## Pricing Pattern Notes

- Pattern D (per-agent or per-matter-agent) suits firms.
- Pattern C (per-step) suits e-discovery and large-scale review.
- Avoid per-outcome (Pattern B) — outcomes belong to the lawyer, not the agent.

## Cross-References

- `ai-agent-risk-register-for-proposals.md` — R-AG-LEGAL-01 (citation hallucination); R-AG-LEGAL-02 (privilege / confidentiality breach across tenants).
- `ai-agent-responsible-ai-commitment.md`
- `ai-agent-trust-and-compliance-template.md`
