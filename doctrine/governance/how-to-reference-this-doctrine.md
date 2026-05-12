# How to Reference This Doctrine

Each of the four consumer engines references the doctrine in a slightly different way. This file gives the exact pattern.

## Common pattern across all four engines

After the mirror, every engine has:

```
<engine-root>/
├── doctrine/                                  # mirrored from _chwezi-doctrine
│   ├── accounting-finance-doctrine.md
│   ├── references/...
│   ├── examples/...
│   ├── ADOPTION.md                            # records adopted version
│   └── governance/
│       ├── finance-accounting-quality-gate.md
│       ├── cleanup-backlog.md
│       └── how-to-reference-this-doctrine.md
├── skills/                                    # mirrored finance skills
│   └── ...                                    # see skill list
└── (existing engine content)
```

Every consumer engine adds a "Finance & Accounting trigger" block to its `CLAUDE.md` and `AGENTS.md`.

## `CLAUDE.md` block (paste verbatim into each engine)

```markdown
## Finance & Accounting Trigger

Load `doctrine/accounting-finance-doctrine.md` whenever the user's request, the artefact being generated, or the code being edited touches **any** of:

- Money flows: sales, purchases, payments, refunds, credit notes, expenses
- Stock and inventory
- Payroll
- Tax (VAT, PAYE, WHT, NSSF, income tax, customs, excise, EFRIS, eTIMS)
- Grants, donations, donor restrictions
- Banking, mobile money, POS, card settlement, cash drawer
- Fixed assets
- Financial reports, management accounts, statutory returns
- Chart of Accounts, journals, ledger, posting services, period state, audit trail
- Reconciliation, close, migration, opening balances
- Internal controls, audit, evidence packs
- Any IFRS or IFRS for SMEs section

When the trigger fires:

1. Read `doctrine/accounting-finance-doctrine.md`.
2. Read the relevant doctrine reference file under `doctrine/references/`.
3. Read the relevant skill `SKILL.md` under `skills/`.
4. Apply the **finance & accounting quality gate** from `doctrine/governance/finance-accounting-quality-gate.md` to the generated artefact.
5. Record the gate run in the artefact manifest.

The `finance-module-audit` skill is the standard implementation harness for analysing any software system that has a finance / accounting element. It auto-runs whenever such a system is the subject of an analysis request. See `skills/finance-module-audit/SKILL.md`.
```

## `AGENTS.md` block (paste verbatim into each engine)

```markdown
## Finance & Accounting Trigger (for Codex / generic agents)

Identical trigger conditions to the CLAUDE.md block above. Codex and other agents that do not natively read SKILL.md files must explicitly load the doctrine and relevant reference files into their context before generating finance-touching output.

For Codex specifically: include this block in any system prompt that operates inside this engine. Where the engine has a `skill-loader` script, run it with the relevant skill key before generation; otherwise read the SKILL.md and references inline.
```

## Per-engine specifics

### `skills-web-dev` (at `C:\Users\Peter\.claude\skills`)

- Doctrine mirrored to `skills/_doctrine/` (this engine uses the `skills/` root for skill folders, so the doctrine sits alongside).
- The existing `accounting-engine`, `accounting-finance-controller`, and `finance-module-audit` skills are updated to reference the doctrine at the new path.
- The `finance-module-audit` skill is given an autorun trigger directive (see its updated `SKILL.md`).

### `srs-skills` (at `C:\wamp64\www\srs-skills`)

- Doctrine mirrored to `doctrine/`.
- Finance skills mirrored to `skills/finance/` (this engine groups its skills by domain).
- Every SRS / SDS / test-plan template adds the "Finance & Accounting Trigger" block to its preamble.
- The accountant / controller / CFO / tax reviewer roles are added to the required-review list.

### `proposal-skills` (at `C:\wamp64\www\proposal-skills`)

- Doctrine mirrored to `doctrine/`.
- Finance skills mirrored to `skills/finance/`.
- Sector annexes (schools, clinics, NGOs, retail/POS, manufacturing, agribusiness, hospitality) reference the doctrine and the relevant IFRS / IFRS for SMEs section.
- Vendor-replacement language is paired with the standard caveat block.

### `business-plan-skills` (at `C:\wamp64\www\business-plan-skills`)

- Doctrine mirrored to `doctrine/`.
- Finance skills mirrored to `skills/finance/`.
- Country-context files reference the doctrine and the live-rate verification protocol.
- Financial-projection templates add a framework header and consume the CoA statement-group taxonomy.

## Adoption check

When an engine adopts a new doctrine version:

1. Run the mirror script.
2. Update `doctrine/ADOPTION.md` with the new version, the adoption date, the owner, the reviewer, and the affected engine files.
3. Run the engine's local quality-gate self-test (where available).
4. Commit with the conventional commit message: `doctrine: adopt v<semver>`.

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
