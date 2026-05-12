# Policy Hierarchy

## Rule

Every finance-touching artefact identifies its reporting framework explicitly. There is no implicit framework.

## Selection logic

Order of consideration:

1. **Client explicitly selects a framework.** Honour it, but log the selection with date, selector role, and reason.
2. **No selection, but client profile matches an SME profile** (private company, no listed debt or equity, no fiduciary capacity for a broad group of outsiders, no public-interest characteristics): default to **IFRS for SMEs**.
3. **No selection, but client profile matches a public-interest entity** (listed, banking, insurance, pension fund, large utility, regulated): default to **full IFRS**.
4. **No selection, and client is a not-for-profit / NGO / faith-based / community organisation**: default to **IFRS for SMEs** unless donor or regulator mandates full IFRS, in which case full IFRS.
5. **No selection, and client is a microenterprise / family business / sole trader**: default to **IFRS for SMEs** in simplified application (Sections 1–7, 11, 13, 14, 18, 23, 28); flag that statutory filing obligations may be minimal.
6. **No selection at all**: refuse to ship final output. Mark `fail` on the quality gate.

## Local statutory overlay

Local statutory, tax, payroll, filing, regulator, and exchange-rate requirements override generic IFRS / IFRS for SMEs treatments only **after** current-source verification logged in the source register. Verification protocol: `live-rate-verification-protocol.md`.

## Client-specific policy choices

Where IFRS or IFRS for SMEs permits a policy choice (cost vs revaluation model for PPE, weighted average vs FIFO for inventory, percentage-of-completion vs completed-contract, …), the choice is documented with:

- Owner role (Accountant or Controller)
- Effective date
- Affected books and entities
- Reviewer role
- Professional-review status
- Report-impact note

The choice is recorded against the entity in the accounting configuration store and surfaced on every report that depends on it.

## Professional review trigger

Required for: complex IFRS judgement (revenue allocation, lease classification, ECL, impairment indicators, deferred-tax recognition); statutory sign-off; audit positions; tax positions taken in returns; first-time framework adoption; change in accounting policy; reorganisations, business combinations, discontinued operations; going-concern conclusions.

The reviewer role must exist in the system, be assigned a named human, and sign off in the audit log before the output is released.

## US GAAP exclusion

US GAAP is **not** a default anywhere in the Chwezi system. If a client genuinely requires US GAAP (US-listed parent, US-investor covenant), it is treated as a client-specific overlay with:

- Explicit selection logged
- Reviewer with US GAAP qualification or attestation of competence
- Mark on every relevant artefact: "US GAAP overlay — non-default"
- No silent application of US-GAAP-only concepts (LIFO inventory, extraordinary items as a line, completed-contract for short-term contracts, FAS-13-style lease split, ASC 606 vs IFRS 15 differences) without express selection.

## Framework note on every artefact

Every SRS, SDS, test plan, proposal, business plan, strategy, implementation report, financial statement, dashboard, and management pack carries a header line:

```
Framework: IFRS for SMEs | IFRS | local statutory basis | client-specific | N/A
Selected by: <role / name>     Effective: YYYY-MM-DD     Reviewer: <role / name>
```

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
