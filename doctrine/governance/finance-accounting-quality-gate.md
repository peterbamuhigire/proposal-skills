# Finance & Accounting Quality Gate

The release gate run on every artefact where money, inventory, payroll, tax, grants, banking, POS, mobile money, statutory compliance, or accounting records are in scope. Applies to: proposals, SRS, SDS, test plans, business plans, strategies, implementation plans, reports, software artefacts (commits, PRs, releases), dashboards, prints, and exports.

The gate returns one of three states: `pass`, `pass-with-caveats`, `fail`.

## States

| State | Meaning |
|---|---|
| `pass` | No blockers. All required checks complete. All verifications current. Ready for operational use. |
| `pass-with-caveats` | No blockers. Named professional review or current-rate / template verification remains before operational use. Allowed for internal drafts, non-statutory proposals, and design documents. Not allowed for statutory filings, client-facing financial statements, or production releases that affect the ledger. |
| `fail` | One or more blockers remain. The artefact is not released. |

## Automatic blockers

A finding in any of these categories returns `fail`:

### Doctrine and framework

- B-001: Framework not identified (no `Framework:` header).
- B-002: US GAAP applied without explicit client selection.
- B-003: LIFO presented as IFRS or IFRS for SMEs compliant.
- B-004: Mixed framework across the same entity / period without policy-change documentation.

### Ledger

- B-010: Direct write path to `journal_lines` or equivalent outside an approved posting service.
- B-011: Single-sided ledger effects in scope of double entry.
- B-012: Edit or delete of posted accounting history through normal application paths.
- B-013: Posting service that allows posting into a locked period without the reopen workflow.
- B-014: Missing audit-log fields (actor, timestamp, source document, evidence, lineage).
- B-015: Reposting after edit (only reversal + new posting permitted).

### CoA

- B-020: Free-text accounts.
- B-021: Tax amounts stored in line memos rather than on tax control accounts.
- B-022: Control accounts without subledger tie-out.
- B-023: Migration suspense non-zero at cutover without sign-off / waiver.

### Tax and statutory

- B-030: Hardcoded VAT / PAYE / NSSF / WHT / income-tax / customs value in any final artefact.
- B-031: VAT-inclusive postings without net / tax / gross decomposition.
- B-032: Tax codes without an effective period.
- B-033: Authority return templates referenced without verified version.
- B-034: Tax filing claimed as automated when only a return pack is produced.

### Live-rate

- B-040: Final output uses a value without a `verified-current` source-register entry.
- B-041: Source-register entry past expiry / recheck date still referenced.
- B-042: Verification logged without named verifier and date.

### Migration

- B-050: Cutover without opening-balance and subledger tie-out sign-off.
- B-051: Trial-balance-only migration where open subledgers exist.

### Reconciliation

- B-060: Bank, POS, cash drawer, or mobile-money scope without a reconciliation plan.
- B-061: Reconciliation rendered as a downloadable report rather than a triage UI.
- B-062: Imported feed committed to the ledger before matching.

### UX

- B-070: `Delete` / `Remove` verb on posted records.
- B-071: Gross-only transaction display.
- B-072: Dashboard summary numbers without drilldown affordance.
- B-073: Green or red used for non-state purposes.
- B-074: Status text not drawn from the controlled taxonomy.
- B-075: Report without a print stylesheet.
- B-076: Login flow that grants accounting power without role check.

### Proposals and business plans

- B-080: Vendor-replacement claim without professional-review caveats and acceptance criteria.
- B-081: Country-context rate values shipped as permanent facts.
- B-082: Business-plan financials without framework header.
- B-083: Third-party-product-first language without a Chwezi-specific accounting standard backing it.

### Reviewers

- B-090: Required reviewer role missing in the role registry.
- B-091: Final release without required reviewer sign-off in the audit log.

## Required checks (non-blocking but must be completed)

- R-100: Doctrine version referenced.
- R-101: Adopted doctrine version recorded in the consumer engine's `ADOPTION.md`.
- R-102: Quality-gate run logged in the artefact manifest.
- R-103: Reconciliation evidence pack attached where applicable.
- R-104: Migration cutover pack attached where applicable.
- R-105: Tax-return pack attached where applicable.
- R-106: Print preview validated where applicable.
- R-107: Accessibility check (WCAG AA) recorded for UI artefacts.
- R-108: Source-register snapshot attached.

## How to invoke the gate

### Consumer engine — software (skills-web-dev)

```
1. Load doctrine/accounting-finance-doctrine.md.
2. Load governance/finance-accounting-quality-gate.md (this file).
3. Detect finance scope on the prompt / commit / PR.
4. If finance scope present:
   a. Load relevant skill from skills/.
   b. Run blockers list (B-001…B-091).
   c. Run required checks list (R-100…R-108).
   d. Emit gate result with finding register.
5. If blocker found → state = fail; halt release.
6. If only required checks pending → state = pass-with-caveats; allow internal draft only.
7. Else → state = pass.
```

### Consumer engine — SRS (srs-skills)

Insert the gate as a generation-time check in SRS / SDS / test-plan outputs. Every requirement that touches finance scope carries a `gate-state` attribute and a finding register appendix.

### Consumer engine — proposals (proposal-skills)

Run the gate before final assembly. Proposals failing the gate go back to the writer with the finding register. Vendor-replacement language without caveats fails B-080 by construction.

### Consumer engine — business plans (business-plan-skills)

Run the gate before final assembly of every business plan. Country context blocks failing B-081 must be reworked into verification-gated assumptions before final.

### Cross-cutting — `finance-module-audit` skill

The `finance-module-audit` skill is the standard implementation harness for the gate against software systems. It produces the finding register, scorecard, and master plan. See `../skills/<engine>/skills/finance-module-audit/SKILL.md` after mirror.

## Finding register format

```yaml
- id: B-031
  category: tax-and-statutory
  severity: blocker
  title: "VAT-inclusive postings without net / tax / gross decomposition"
  evidence: "src/services/posting.service.php:142-178"
  observation: "Sale recorded as single line on Sales — Goods at gross amount."
  required-fix: "Decompose at posting; route tax to Output VAT Control; preserve gross as document reference."
  acceptance-evidence: "Test case TC-VAT-001 passes; example posting reviewed."
  owner: "Backend Engineer"
  reviewer: "Accountant"
  due: "2026-06-15"
```

## Gate manifest

Every gate run produces a manifest stored with the artefact:

```yaml
gate-version: "1.0.0"
doctrine-version: "1.0.0"
ran-at: "YYYY-MM-DDTHH:MM:SS+03:00"
ran-by: "<named human or named agent>"
artefact: "<artefact-name>"
artefact-version: "<semver or commit>"
state: pass | pass-with-caveats | fail
blockers: 0
caveats: 2
required-checks-passed: 8
required-checks-pending: 1
finding-register: "<path>"
evidence-pack: "<path>"
reviewers:
  - role: Accountant
    name: "..."
    signed-at: "..."
  - role: Controller
    name: "..."
    signed-at: "..."
```

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
