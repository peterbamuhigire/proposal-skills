# Cleanup Backlog

Cross-engine remediation backlog. Findings are not auto-applied. Each item carries owner, severity, and acceptance evidence. The user approves each change before it is applied.

## Categories

| Category | Severity ladder |
|---|---|
| LIFO removal | blocker / major / minor |
| US GAAP language to mark as non-IFRS | major / minor |
| Hardcoded tax rates / NSSF / PAYE / VAT thresholds | blocker / major |
| Stale exchange rates | major |
| Third-party-product-first language | major / minor |
| Direct journal-line writes in code | blocker |
| Status taxonomy violations | major |
| Missing reviewer roles | major |
| Missing print stylesheet | major |
| Missing drilldown affordance | major |
| Disclosure dumped as modal | minor |

## Items

### LIFO

| # | Engine | File | Lines | Severity | Proposed replacement |
|---|---|---|---|---|---|
| L-01 | business-plan-skills | `skills/industry-guides/restaurant/references/cost-controls-advanced.md` | TBD | blocker | Remove LIFO; rewrite section to use FIFO / weighted average, with note "LIFO not permitted under IFRS or IFRS for SMEs". |
| L-02 | srs-skills | `skills/skills/inventory-management/SKILL.md` lines around `:326`, `:329`, `:343`, `:384` (from research) | TBD | blocker | Replace LIFO references with FIFO / weighted average; mark legacy LIFO data as "non-IFRS — do not apply unless explicitly requested". |
| L-03 | srs-skills | `skills/skills/modular-saas-architecture/examples/module-config-example.php:230` (from research) | 230 | blocker | Remove LIFO from selectable config; if retained, gate behind a non-IFRS jurisdiction profile. |
| L-04 | all engines | grep `\bLIFO\b` | various | blocker / major | Per occurrence: keep if in a "non-IFRS" or "legacy" context; remove if in an IFRS-compliant default. |

### US GAAP

| # | Engine | File | Severity | Action |
|---|---|---|---|---|
| G-01 | all engines | grep `\bUS GAAP\b`, `\bASC \d+\b`, `\bFAS \d+\b` | major | Mark each occurrence as "non-IFRS — do not apply unless explicitly requested". |
| G-02 | business-plan-skills | Any default templates that import US-GAAP-style classifications | major | Convert to IFRS for SMEs / IFRS classifications per `chart-of-accounts.md` statement-group taxonomy. |

### Hardcoded statutory and FX values

| # | Engine | File | Severity | Action |
|---|---|---|---|---|
| H-01 | business-plan-skills | `country-context/uganda/SKILL.md:75`, `:76`, `:293`, `:294` (from research) | blocker | Convert "always use" FX language to a dated assumption referencing the source register. |
| H-02 | business-plan-skills | `country-context/uganda/SKILL.md:124`-`:134` (from research) | blocker | Convert Uganda VAT / PAYE / NSSF / WHT / EFRIS / tax-band content to verification-gated assumptions with `state: draft` until verified. |
| H-03 | business-plan-skills | `country-context/tanzania/SKILL.md:175`-`:178`, `:196`, `:378`-`:387` | high | Use as template for the country-context verification-gap pattern. |
| H-04 | all engines | grep for currency values, rates, percentages in code and copy | blocker / major | Per occurrence: confirm it is illustrative ("planning default — verify before final output") or convert to source-register reference. |
| H-05 | srs-skills | Design lines referencing `tax_rates`, `exchange_rates` tables | high | Add current-rate verification owner field; document recheck cadence. |

### Stale exchange rates

| # | Engine | File | Severity | Action |
|---|---|---|---|---|
| F-01 | business-plan-skills | Any FX assumption with a date older than the verification cadence window | major | Mark as `expired` until re-verified; block final output. |
| F-02 | all engines | Any FX caching layer | major | Confirm cache TTL ≤ verification cadence; expose source and timestamp. |

### Third-party-product-first language

| # | Engine | File | Severity | Action |
|---|---|---|---|---|
| T-01 | proposal-skills | Any "replaces QuickBooks / Sage / Tally / Xero" claim | major | Pair with professional-review caveat, acceptance criteria, named scope. |
| T-02 | proposal-skills | Marketing copy that compares features to a named third-party product | minor | Reframe in Chwezi-positive terms; back claims with our standard. |
| T-03 | business-plan-skills | Any pricing argument based on competing third-party-product pricing | minor | Allowed where the competitor is named for comparison; not allowed as the basis of the Chwezi accounting standard. |

### Direct journal-line writes

| # | Engine | File | Severity | Action |
|---|---|---|---|---|
| D-01 | skills-web-dev (Chwezi product code, where applicable) | grep `INSERT INTO journal_lines`, `UPDATE journal_lines`, `DELETE FROM journal_lines` | blocker | Route through posting service. |
| D-02 | srs-skills | Any SRS example showing direct ledger writes | blocker | Replace example with a posting-service call. |

### Status taxonomy

| # | Engine | File | Severity | Action |
|---|---|---|---|---|
| S-01 | all engines | grep free-text statuses (`'active'`, `'pending'`, `'done'`, …) on finance records | major | Map to controlled taxonomy in `status-taxonomy.md`. |
| S-02 | all engines | Boolean status fields on finance records | major | Replace with the taxonomy plus chip rendering. |

### Reviewer roles

| # | Engine | File | Severity | Action |
|---|---|---|---|---|
| V-01 | srs-skills | Finance required-review file | major | Add Accountant, Controller, CFO / finance lead, Tax reviewer to the role list. |
| V-02 | all engines | Audit-log schema | major | Confirm reviewer role recorded on every approval action. |

### Print stylesheet

| # | Engine | File | Severity | Action |
|---|---|---|---|---|
| P-01 | skills-web-dev | Any report page in finance scope | major | Add print stylesheet per `print-fidelity.md`. |

### Drilldown

| # | Engine | File | Severity | Action |
|---|---|---|---|---|
| K-01 | skills-web-dev | Any dashboard tile / summary card | major | Add drilldown affordance; click to source. |

### Disclosures as modals

| # | Engine | File | Severity | Action |
|---|---|---|---|---|
| M-01 | skills-web-dev | Modal compliance disclosures | minor | Move into the relevant field's helper text or adjacent panel. |

## Workflow

1. Run the grep / search per item.
2. List each occurrence with file path and line.
3. Propose the replacement.
4. Ask the user to approve each change before applying.
5. Apply, commit, and update this backlog with status.

## Status

Backlog is seeded from the research project's `cross-repo-cleanup-backlog.md`, `cross-repo-remediation-master-plan.md`, and the cross-repo Wave-1 repo sweep. Concrete line numbers above marked TBD are to be resolved by per-engine grep at adoption time.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
