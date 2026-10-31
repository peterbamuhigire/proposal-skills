# Proposal Skills

Proposal Skills is the Chwezi engine for winning consulting and technology work in East and Central Africa. Its 115 skills plan, draft, review and assemble proposals, Expressions of Interest (EOIs), tender and request-for-proposal (RFP) responses, donor grant applications and commercial offers.

The engine reads the real solicitation, the buyer's evaluation criteria and the proposer's evidence. It does not infer tender requirements from earlier bids. It does not invent credentials, compliance or delivery capacity.

**Who it is for.** Consulting firms, independent consultants, software and AI vendors, agencies, NGOs and bid teams that answer government, donor, development-bank or enterprise buyers.

**Use it when** you hold a solicitation, terms of reference (ToR) or brief and must write, review or assemble the response.

## Start here

### At a glance

- **115 skills** in 11 categories plus a router, counted from `skills/**/SKILL.md`.
- **7 registered checks**, one of them a suite of 117 unit tests. All exited 0 on 31 October 2026 (Linux, Python 3.14, PyYAML 6.0.3, Node.js 22).
- **41 routing fixtures.** The expected skill is in the top three for all 41 and first for 32. This is a lexical proxy, not a model run.
- **14 dated source records** for volatile claims. The register's review gate falls on 2026-11-30.
- **Score 61.4 out of 100** on 31 October 2026. The published cap is 65 and the target is 95.
- **Works in** Claude Code, Codex and any runner that reads Markdown.

### Three steps

1. **Install** in Claude Code:

   ```text
   /plugin marketplace add https://github.com/peterbamuhigire/proposal-skills
   /plugin install proposal@chwezi-proposal
   ```

2. **Check** a clone against the engine's own gate. You need Python 3.11 or newer and PyYAML. Expect exit 0 and `findings: 0`:

   ```text
   git clone https://github.com/peterbamuhigire/proposal-skills
   cd proposal-skills
   python3 -X utf8 scripts/validate_skills.py --baseline quality-baseline.json
   ```

3. **Use it.** Open the project that holds your solicitation in Claude Code or Codex. Name the router and the task, for example "Use `skills/SKILL.md` to plan a response to this RFP."

   The router asks for one proposer profile before it drafts. It stops when a mandatory form, fact or authority is missing.

## Contents

- [When to use it](#when-to-use-it)
- [Capabilities](#capabilities)
- [Find the right skill](#find-the-right-skill)
- [How it works](#how-it-works)
- [What is inside](#what-is-inside)
- [Installation](#installation)
- [Validation](#validation)
- [Quality and improvement](#quality-and-improvement)
- [Date-triggered gates](#date-triggered-gates)
- [What the October 2026 kaizen improved](#what-the-october-2026-kaizen-improved)
- [Other kept changes: checks, routing and documentation](#other-kept-changes-checks-routing-and-documentation)
- [Sources and references](#sources-and-references)
- [Contributing, author and licence](#contributing-author-and-licence)

## When to use it

- **Use it for** consulting proposals, EOIs and prequalification responses, tenders and RFP responses, donor grant applications, SaaS, AI-on-SaaS and AI-agent bids, pilots, contract exhibits and oral presentations.
- **Do not use the router for** blog writing on its own, skill maintenance, or work unrelated to proposals. The blog skills serve content publishing only, and the maintenance skills sit in the Quality and operations category.
- **Hand off** current facts, finance, visual design and software delivery to the sister engines listed under [Sister engines](#sister-engines).

### What it produces

- Submission-ready proposal sections, full bid packages, and EOI and prequalification responses.
- Compliance matrices, evidence maps, logframes and results frameworks.
- Risk registers, staffing plans and Gantt-style work plans.
- Fee schedules and pricing narratives.
- SaaS, AI-on-SaaS and AI-agent business cases, pilots, SLAs and contract exhibits.
- Oral-presentation packs, and independent red-team and anti-slop review findings.

All writing follows the engine's professional British English and East African English standards. Every claim must trace to evidence.

### Procurement frameworks and standards it follows

- **Uganda:** the Public Procurement and Disposal of Public Assets (PPDA) Act (Cap. 205) and the PPDA Regulations 2023.
- **World Bank:** the Procurement Regulations for IPF Borrowers and the Environmental and Social Framework.
- **African Development Bank (AfDB):** the Procurement Policy and the Integrated Safeguards System 2023.
- **Others:** UNDP and UN-system rules, EU PRAG and GIZ local procurement, and OECD-DAC evaluation criteria for results and monitoring and evaluation (M&E).
- **Technology bids** are checked against the assurance standards that buyers ask about: ISO/IEC 27001, ISO/IEC 42001, SOC 2, the NIST AI RMF, the EU AI Act, GDPR and East African data-protection law.

## Capabilities

The engine holds 115 skills in 11 categories plus a router, grouped under [What is inside](#what-is-inside). The [skill catalogue](docs/skill-catalogue.md) lists each one. The table under Find the right skill is the capability map: common tasks and the skill that handles each.

### Find the right skill

Start from the router for a whole bid. Go straight to a skill when you need one section or one topic. The [skill catalogue](docs/skill-catalogue.md) lists all 115 skills.

| Task | Skill |
|---|---|
| Plan and assemble a whole tender response | [`skills`](skills/SKILL.md), the router |
| Write the cover letter or the executive summary | [`01-cover-letter`](skills/pipeline/01-cover-letter/SKILL.md), [`02-executive-summary`](skills/pipeline/02-executive-summary/SKILL.md) |
| Write the technical approach, or split pages by scoring weight | [`06-methodology`](skills/pipeline/06-methodology/SKILL.md) |
| Write the work plan with milestones and Gantt tables | [`08-work-plan`](skills/pipeline/08-work-plan/SKILL.md) |
| Prepare the separate financial proposal | [`10-financial-proposal`](skills/pipeline/10-financial-proposal/SKILL.md) |
| Respond to a Uganda PPDA tender | [`ppda-uganda`](skills/profiles-sectors/sectors/ppda-uganda/SKILL.md) |
| Prepare World Bank or AfDB consulting forms | [`world-bank`](skills/profiles-sectors/sectors/world-bank/SKILL.md), [`afdb`](skills/profiles-sectors/sectors/afdb/SKILL.md) |
| Respond to a GIZ local procurement tender | [`giz-eu-local-procurement-response`](skills/domain-delivery/giz-eu-local-procurement-response/SKILL.md) |
| Propose a SaaS implementation, AI features in SaaS, or an AI agent | [`saas-implementation-methodology`](skills/saas-proposals/saas-implementation-methodology/SKILL.md), [`ai-on-saas-combined-methodology`](skills/ai-on-saas-proposals/ai-on-saas-combined-methodology/SKILL.md), [`ai-agent-methodology`](skills/ai-agent-proposals/ai-agent-methodology/SKILL.md) |
| Draft agent SLA classes and service credits | [`ai-agent-sla-and-credit-schedule`](skills/ai-agent-commercial/ai-agent-sla-and-credit-schedule/SKILL.md) |
| Prepare for a shortlist interview | [`tender-orals-and-proposal-presentation`](skills/strategy-positioning/tender-orals-and-proposal-presentation/SKILL.md) |
| Grade a finished section for AI slop, or red-team a high-stakes bid | [`ai-slop-audit`](skills/meta/ai-slop-audit/SKILL.md), [`bid-red-team-dual-review`](skills/meta/bid-red-team-dual-review/SKILL.md) |

## How it works

The router sends each task to one proposer profile and then to only the skills the task needs. The steps are:

1. Identify the deliverable: a whole bid or one section.
2. Load the [proposal router](skills/SKILL.md) for any job that spans several sections.
3. Load exactly one proposer profile before drafting, so voice and identity stay consistent.
4. Load the numbered section skill, then add sector, procurement and domain skills where they help.
5. Read a skill's `references/` files only when they add value.
6. Draft, then run the anti-slop and business-logic gates. Check compliance, and keep technical and financial content in separate envelopes where the buyer requires it.

A grade of F from `ai-slop-audit` blocks submission until the blocking findings are fixed.

### Policy and contracts

- **Router and policy.** The proposal router sets workflow order and cross-cutting routes. [`AGENTS.md`](AGENTS.md) holds the model-neutral policy. [`rules/common/core.md`](rules/common/core.md) holds the always-on baseline.
- **Multi-phase work.** The [runtime-agnostic orchestration contract](docs/operations/runtime-agnostic-orchestration-2026-09-07.md) governs scoped work packages, evidence and pricing checkpoints and context hygiene. It applies to Claude Code and Codex alike.
- **External content.** The same contract sets least agency and sanitised handling of external content.

### Sister engines

Some work belongs to a sister engine. This engine hands it over instead of improvising.

| Need | Engine |
|---|---|
| Feasibility, projections and investor readiness | [Business Plan Skills](https://github.com/peterbamuhigire/business-plan-skills) |
| Campaigns, content calendars and marketing reporting | [Social Media Skills](https://github.com/peterbamuhigire/social-media-skills) |
| Current facts | Digital Research Engine (catalogue id `digital-research-skills`) |
| Finance | [`chwezi-accounting-doctrine`](https://github.com/peterbamuhigire/chwezi-accounting-doctrine) |
| Visual formatting | [`chwezi-design-engine`](https://github.com/peterbamuhigire/chwezi-design-engine) |
| Software specification | [`chwezi-sdlc-documentation`](https://github.com/peterbamuhigire/chwezi-sdlc-documentation) |
| Engineering | [`chwezi-dev-engine`](https://github.com/peterbamuhigire/chwezi-dev-engine) |
| Website delivery | [Website Skills](https://github.com/peterbamuhigire/website-skills) |

- Website Skills keeps no copy of this engine. It resolves this engine through the catalogue, like every other sibling.
- Four checkouts may still sit under their earlier folder names: `design-system-skills`, `srs-skills`, `skills-web-dev` and `chwezi-research-engine`. The portfolio catalogue in `chwezi-engine-agents` lists each as an alias.
- The full routing list is in [`AGENTS.md`](AGENTS.md).

## What is inside

The engine holds 115 active `SKILL.md` files: the parent router and 114 skills in 11 categories. They are counted from the `skills/` tree. The [skill catalogue](docs/skill-catalogue.md) gives every skill with a one-line description and a link.

| Category | Skills | What it covers |
|---|---:|---|
| [Proposal pipeline](skills/pipeline/) | 10 | The ten section skills, from cover letter to financial proposal. |
| [Profiles and sectors](skills/profiles-sectors/) | 18 | Proposer profiles, the sector router, four procurement frameworks and twelve sectors. |
| [Domain delivery](skills/domain-delivery/) | 16 | Project management, M&E, risk, safeguards, change and other delivery domains. |
| [Strategy and positioning](skills/strategy-positioning/) | 12 | Premium positioning and pricing, key accounts, orals, AI transformation, web and service design. |
| [SaaS proposals](skills/saas-proposals/) | 14 | Discovery to trust credentials for multi-tenant SaaS bids. |
| [AI-on-SaaS proposals](skills/ai-on-saas-proposals/) | 11 | The same arc for AI features inside a SaaS product. |
| [AI-agent proposals](skills/ai-agent-proposals/) | 11 | Autonomous and multi-agent products. |
| [AI-agent commercial terms](skills/ai-agent-commercial/) | 8 | SLAs, credits, refunds, contract exhibits, renewals and outcome pricing. |
| [Writing and content](skills/writing-content/) | 3 | Premium commercial writing and two blog skills. |
| [Language](skills/language/) | 2 | East African English, and French and Kiswahili standards. |
| [Quality and operations](skills/meta/) | 9 | Anti-slop, audits, red team, submission proof, kaizen, skill safety and documentation. |
| [Router](skills/SKILL.md) | 1 | The parent skill that routes and sequences the rest. |
| **Total** | **115** | |

### Repository layout

| Folder | Holds |
|---|---|
| `skills/` | The 115 skills, with deeper `references/` beside them. |
| `rules/` | The always-on baseline in `rules/common/core.md`. |
| `scripts/` | The validators, the installer and the plugin-manifest generator. |
| `hooks/` | The plugin's destructive-command gate for Bash, and its tests. |
| `tests/` | Unit tests, fixtures and the agent-integration check. |
| `examples/` | `uganda-eoi-sanitised`, a sanitised EOI package. |
| `templates/` | The skill template. |
| `docs/` | Guidance, the source register and dated records. See the [docs index](docs/README.md). |
| `.claude-plugin/` and `.codex/` | The plugin and marketplace manifests, and the Codex model-policy helper. |
| `prompts/` | A prompt for a full kaizen operation on a bid project. |

## Installation

### Prerequisites

- Claude Code, for the plugin route.
- Node.js 18 or newer, for the clone installer.
- Python 3.11 or newer and PyYAML for the validators and tests: `python3 -m pip install PyYAML`. There is no requirements file. `pytest` is optional, because the suite runs under `unittest`.
- The installer and every check were last run together on 31 October 2026 with Python 3.14, PyYAML 6.0.3 and Node.js 22 on Linux. The Windows route (`install.ps1`) was not run there.

### Claude Code plugin (recommended)

The repository ships a marketplace (`chwezi-proposal`) and a plugin (`proposal`) in `.claude-plugin/`. The two commands are in [Start here](#three-steps), step 1.

### Clone and install

`install.sh` and `install.ps1` delegate to `scripts/install-engine.js`. It copies the skills, rules and hooks into `~/.claude` (`--scope user`, the default) or into `.claude` under the current directory (`--scope project`).

It records ownership in `.chwezi/install-state.json`. Add `--dry-run` to preview the plan.

```text
git clone https://github.com/peterbamuhigire/proposal-skills
cd proposal-skills
bash install.sh --scope project --dry-run    # Linux, macOS, Git Bash: preview
bash install.sh --scope project              # install
node scripts/install-engine.js doctor --scope project
node scripts/install-engine.js uninstall --engine proposal-skills --scope project
.\install.ps1 --scope project                # Windows PowerShell instead of install.sh
```

- Run `install.sh` through `bash`. Git stores it without the executable bit, so `./install.sh` stops with `Permission denied` on a fresh clone.
- Project scope writes to the directory you run it from. Run the install lines inside the project that should receive the skills, not inside this checkout, and give `install.sh` by its path, for example `bash ../proposal-skills/install.sh --scope project --dry-run`.
- The Linux sequence (preview, install, `doctor`, uninstall) was run on 31 October 2026 into a throwaway project directory. `doctor` reported every installed file present and unmodified, and the install held all 115 `SKILL.md` files.

### Codex

Codex reads `AGENTS.md` as the repository policy. Before substantive Codex work, run the model-policy check in `.codex/` (Python 3.11 or newer). Apply it only when drift is reported:

```text
python3 <engine-root>/.codex/ensure_model_policy.py --runtime codex --check
python3 <engine-root>/.codex/ensure_model_policy.py --runtime codex --apply
```

- `--check` prints `PASS: Codex model policy is correct` and exits 0 when the settings match. It prints a `DRIFT:` line and exits 1 when they do not; an empty Codex home gives `DRIFT: Codex config.toml is missing`. It exits 2 on an error.
- `--apply` uses `CODEX_HOME` (default `~/.codex`), keeps unrelated settings and backs up what it touches. See [`.codex/README.md`](.codex/README.md). It was not run for this update.
- With `--runtime claude` the helper reports `NOT_APPLICABLE` and changes nothing.

### Manual route (any runner)

Clone the repository and read [`AGENTS.md`](AGENTS.md) and the [proposal router](skills/SKILL.md). Then load the routed `skills/<category>/<skill-name>/SKILL.md` directly, together with `rules/common/core.md`. Claude Code picks up `CLAUDE.md`, which imports `AGENTS.md`.

### Local marketplaces

Both Codex and Claude can install the local `proposal@chwezi-proposal` marketplace plugin from the catalogue-resolved checkout:

- **Codex:** `codex plugin marketplace add .` then `codex plugin add proposal@chwezi-proposal`.
- **Claude:** `claude plugin marketplace add .` then `claude plugin install proposal@chwezi-proposal`.
- Native offline installation was tested in a disposable container on 29 October 2026. It was not repeated on 31 October. Public directory approval and model behaviour remain unassessed.
- `scripts/validate_skills.py` enforces a hard limit of 5,000 files per engine. It applies to the full checkout (including Git and caches) and to the package inventory.
- Measured on 31 October 2026 at commit `c29e8b3`, the checkout held 904 files and the package 530. Keep build dependencies and disposable artefacts outside the checkout.

### Updating

No update command has been tested, so the update route is `NOT_ASSESSED`. After you pull a newer clone, preview the install with `--dry-run` before you apply it.

## Validation

Run every command from the repository root. The checks use `python3` (use `python` where only that name exists) and need PyYAML. They leave tracked files unchanged. Python writes only ignored `__pycache__` folders.

| Command | What it checks | Expected result |
|---|---|---|
| `python3 -X utf8 scripts/validate_skills.py --baseline quality-baseline.json` | The skill contract for every `SKILL.md`, marketplace parity, the 5,000-file ceiling, the dated source register and retired World Bank form labels. | Exit 0, `findings: 0` |
| `python3 -X utf8 scripts/routing_smoke_test.py` | The routing fixtures in `tests/fixtures/routing-fixtures.json` against skill descriptions. | Exit 0 and a top-three hit rate of 100%. The precision@1 and owned-negative figures are a lexical proxy, not a model run. |
| `python3 -X utf8 scripts/encoding_link_gate.py` | UTF-8, mojibake markers, broken local Markdown links, machine-specific paths outside dated records, portable sibling routes. | Exit 0, `findings: 0` |
| `python3 -X utf8 scripts/source_ingestion_guardrail.py` | The ban on book extractions and reconstructive book content. | Exit 0, `findings: 0` |
| `python3 scripts/proposal_fixture_check.py` | The structure of the fictional bid package in `tests/fixtures/`. | `result: PASS` |
| `python3 -X utf8 -m unittest discover -s tests` | The test suite: 117 tests, also collected and passed by `pytest`. | `OK` |
| `git diff --check` | Whitespace errors in the working tree. | Exit 0, no output |

All seven were run on 31 October 2026 and exited 0. None needs `pwsh`, Pandoc, Mermaid, a browser, LibreOffice or a container. PyYAML is the only third-party Python package the checks import. `pytest` is optional: a real `pytest` run collected the same 117 tests and passed them.

### Other checks and helpers

- `python3 scripts/proposal_fixture_check.py --input <package>/validator-input.json --check-content` scans a package's technical and financial envelope files, including `.docx`, for the other envelope's markers. The sanitised example in `examples/uganda-eoi-sanitised/` passes.
- Add `--allow-unscanned-types` to that command to accept a file type the scan cannot read, such as PDF.
- `python3 -X utf8 scripts/page_budget_check.py <spec.json>` proposes or checks a weighted page allocation (`--propose` gives a proportional split). `tests/fixtures/page-budget-example.json` is a worked input.
- `python3 -X utf8 scripts/check_form_labels.py`, `scripts/check_marketplace.py` and `scripts/check_source_currency.py` are the three gates that `validate_skills.py` calls. Each also runs alone.
- `python3 -X utf8 scripts/validate_p0_commercial_fixture.py tests/fixtures/p0-commercial-fixture.json` and `python3 -X utf8 scripts/validate_healthcare_evidence_packs.py tests/fixtures/healthcare-evidence-packs.json` take a fixture path and print `PASS`. Called without one, they fail.
- `node hooks/test-destructive-bash-gate.js` (61 checks) and `node hooks/test-plugin-hook-config.js` (7 checks) test the plugin hooks. They need Node.js only and are not in CI.
- `python3 tests/agent-integration/test_proposal_agent_contract.py` checks the engine manifest against the portfolio catalogue. It needs PyYAML. It is not part of `unittest` discovery or CI.
- That agent-integration test looks for `chwezi-engine-agents` next to this checkout. Where that folder is absent it prints `NOT ASSESSED` instead of failing.
- The canonical engine audit and quick validator in `chwezi-dev-engine` are listed in [`CONTRIBUTING.md`](CONTRIBUTING.md). Both ran on Linux and passed for this engine.

### Where the checks run

The workflow `.github/workflows/skill-quality.yml` runs the first six commands above on `ubuntu-latest` with Python 3.12. It was not run here. `git diff --check` is the release gate declared in `.skills-engine/engine-manifest.yaml`, which lists no other check.

## Quality and improvement

The engine audits itself under the Portfolio Kaizen Standard. A published score is capped at 65 out of 100, and every plan targets 95 with evidence and a re-audit date. The evidence is committed in the repository:

- [`docs/kaizen/2026-10-engine-kaizen/`](docs/kaizen/2026-10-engine-kaizen/05-final-report.md), the 29 October 2026 cycle: World Bank form crosswalk, hard package ceiling, routing measures, scoped source register.
- [`docs/kaizen/2026-10-engine-kaizen-pass-2/`](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md), the 31 October 2026 cycle.
  - The open backlog is in [`06-next-cycle.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/06-next-cycle.md).
  - The documentation follow-ups are in [`07-docs-followups.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md).
- Earlier cycles and reviews are indexed in [`docs/README.md`](docs/README.md).

**Latest score.** The pass 2 report records a raw score of 61.4 and a published score of `min(61.4, 65)` = 61.4 for 31 October 2026. Its baseline, measured before its changes, was raw 54.5, so compare 61.4 with 54.5. The 29 October final was raw 58.5. The target of 95 is not met.

Scores are reviewer judgements, not bid-win probabilities. A missing mandatory live-bid requirement blocks release whatever the score.

### Open findings that matter to a user

- No real solicitation, bidder evidence pack, evaluator or submission receipt has been used. The tools prove their mechanics on fictional data only.
- PPDA: the scope of the e-GP mandate, the monetary thresholds and the bid and performance security amounts are `NOT_ASSESSED`. The PPDA reference labels its UGX figures as unverified.
- AfDB, UNDP, PRAG and Uganda data-protection claims are unverified. The skills label the AfDB figures and the 0 to 4 scoring scale as such.
- Routing is measured with a lexical proxy over skill descriptions. The 41 fixtures name 27 of the 115 skills, and no model-judged run has been made.
- The World Bank form map follows the March 2025 Standard RFP. The issued RFP controls where it differs.
- Accessibility is unchanged at 40 out of 100: no assistive-technology run has been made.

## Date-triggered gates

One gate in this engine depends on the calendar. No other check compares anything with today's date, and no unit test depends on it.

The gate is the source register [`docs/source-registers/2026-10-currentness.json`](docs/source-registers/2026-10-currentness.json). It holds 14 records (10 `SCOPED`, 4 `NOT_ASSESSED`), all volatile, all with review date 2026-11-30.

| Date | Effect |
|---|---|
| 2026-11-30 | The gate still passes on this day. |
| 2026-12-01 | `scripts/validate_skills.py` and `scripts/check_source_currency.py` exit 1 with `review expired` for all 14 records. The CI validation step fails with them. |

**How it was verified.** The scripts have no `--as-of` option, because they read `date.today()`. The gate was run with that call replaced. It gave 0 errors on 2026-11-29 and 2026-11-30, and 14 on 2026-12-01 and 2027-01-01.

`validate_skills.py` run the same way exits 0 on 2026-11-30 and 1 on 2026-12-01.

**How to renew it.**

1. Re-read each `SCOPED` source, then update its `access_date`, `verified_date` and `review_date`.
2. Set a volatile record's `review_date` no more than 45 days after its `verified_date`.
3. Leave a claim that cannot be re-read as `NOT_ASSESSED`. It carries no verified date, but its `review_date` must still move forward, because the gate checks all 14 records.

The re-audit is due on 30 November 2026, or before a live bid if that is sooner.

## What the October 2026 kaizen improved

This section lists the kept changes of three pieces of work: the 29 October cycle, the 31 October pass 2 and the 31 October documentation wave. Both cycle reports record that no experiment was reverted. Every commit named below is on `main`.

The table below summarises the results. The defects follow, then [other kept changes](#other-kept-changes-checks-routing-and-documentation).

- **29 October sources.** The [report](docs/kaizen/2026-10-engine-kaizen/05-final-report.md) and the [experiment log](docs/kaizen/2026-10-engine-kaizen/03-experiment-log.md).
- **Pass 2 sources.** The [backlog](docs/kaizen/2026-10-engine-kaizen-pass-2/02-improvement-backlog.md), [experiment log](docs/kaizen/2026-10-engine-kaizen-pass-2/03-experiment-log.md), [validation record](docs/kaizen/2026-10-engine-kaizen-pass-2/04-validation-record.md) and [final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md).
- **"Measured"** means the figure was re-run on 31 October 2026 for this section, by unpacking the earlier commit into a scratch directory. Anything else is copied from the cited record.
- **Limit of the proof.** All proof is on fictional fixtures, a lexical routing proxy, or text read from sources on 31 October. No real bid, evaluator or model-judged routing run has been used.

### Before and after

| Measure | 29 Oct before (`8eddd70`) | 29 Oct after (`9089c0a`) | Now (`b608bcb`) |
|---|---:|---:|---:|
| Raw score; published `min(raw, 65)` (reports) | 53; 53 | 58.5; 58.5 | 61.4; 61.4 |
| Unit tests (measured) | 52 | 63 | 117 |
| Routing fixtures (measured) | 26 | 31 | 41 |
| First-rank hits (measured) | 19/26 | 23/31 | 32/41 |
| Owned-negative checks passing (measured) | not checked | 2/2 | 7/7 |
| Dated source records (measured) | none | 11 | 14 |
| Stale form-label findings, current scanner over each tree (measured) | 22 | 12 | 0 |
| Commands run by CI (measured) | 2 | 2 | 6 |

Every score is below the cap of 65, so raw and published are equal. The target of 95 is not met.

### Defects fixed, most serious first

- **Critical: the stale World Bank form map survived in the skill the router loads first.**
  - The 29 October fix had corrected only the reference guide. `world-bank/SKILL.md`, its scoring guide and `afdb/SKILL.md` still taught TECH-5 as team composition, TECH-7 as the staffing schedule, TECH-8 as the work schedule and a FIN-5 form that the March 2025 RFP does not have.
  - `6efc922` corrects all three files and adds `scripts/check_form_labels.py`, which `validate_skills.py` now runs.
  - Measured: the scanner reports 12 findings on 8 lines in the pre-fix files and 0 now. The 12 form ids were also checked against the downloaded RFP text (validation record).
  - Limit: a paragraph that carries a recorded warning phrase is exempt from the scan as a whole.
- **Critical: the World Bank forms guide itself.**
  - `references/tech-fin-forms-guide.md` described the retired form order and an invented FIN-5 "Miscellaneous Expenses" form.
  - `5a4e39e` rewrote it from 306 to 89 lines against the inspected March 2025 RFP, and it says the issued RFP controls. `09c8adc` completed the form names in the fixture it is tested against.
  - Three regression tests cover the current map, a stale staffing or extra financial form and a duplicate form (experiment log). The unit suite went from 52 tests (measured) to 55 (log) with this change.
- **Major: World Bank scoring norms that no issued document states.**
  - The skill and scoring guide gave "typically 75" as the pass mark, 10 to 20 points for firm experience, 30 to 50 for methodology and a shortlist of 3 to 6.
  - `3db28f3` replaces them with the ranges in the Procurement Regulations (Seventh Edition, September 2025, Annex X) and the RFP Data Sheet. The Data Sheet sets the pass mark, with an indicative 70 to 85. Firm experience is 0 to 10, methodology 20 to 50 and the shortlist 5 to 8. The scoring guide's worked example was recomputed.
  - Measured: the retired phrases are in the old skill (lines 136 and 277) and absent now.
  - Not changed, and labelled unverified: the 0 to 4 scale and the AfDB figures, because the Bank's rated-criteria guidance and the AfDB pages could not be fetched.
- **Major: PPDA submission guidance contradicted the 2023 Regulations.**
  - The skill applied the consultancy two-envelope rule to every method. It said a bid securing declaration is always included. It said PPDA uses a performance securing declaration instead of guarantees.
  - `a8cac10` adds a decision table for method, envelopes, delivery channel and the four securities. Each row is tied to a regulation (Rules and Methods regs 63, 66 and 68; Consultancy reg 47; Contracts reg 11). Four tests refuse the retired claims.
  - The scope of the e-GP mandate, the monetary thresholds and the security amounts stay `NOT_ASSESSED`.
- **Major: no method for a capped, weighted brief.**
  - The section skills' default lengths add up to at least 9.5 pages for a six-page cap, and `06-methodology` said its section should be the longest.
  - `aa49a51` adds a weighted page-budget and compliance-matrix reference, a router rule that the solicitation's caps and weights override default lengths, and `scripts/page_budget_check.py` (13 tests).
  - Measured on the fictional six-page brief: the script proposes 2.0, 1.5, 1.5 and 1.0 pages. The old habit of 5.0, 0.25, 0.25 and 0.5 exits 1 with floor errors. It is allocation arithmetic and predicts no evaluator score.
- **Major: envelope separation was checked by file name only.**
  - `00ef43d` adds `proposal_fixture_check.py --check-content`. It scans the text and `.docx` files (body, headers, footers, footnotes) of each envelope for the other envelope's markers.
  - Measured: with a line "UGX 45,000,000" planted in the technical file of the sanitised example, the previous checker returned PASS (exit 0). The new option returns FAIL (exit 1) with file, line and marker. The clean example passes.
  - The option is opt-in and 13 tests cover it. Other file types are `NOT_ASSESSED` unless accepted. The live-package part stays open.
- **Major: Windows checkout paths in shipped content.**
  - `CONTRIBUTING.md`, `docs/skill-authoring-standard.md`, `skills/meta/skill-writing/SKILL.md` and the example submission manifest carried drive-letter paths, and the link gate matched only an older pattern.
  - `7ad4f13` replaces them with catalogue wording and adds a gate rule (URLs, install-scope text, dated records, scripts and tests are exempt; 4 tests). `4066815` had already replaced the same kind of path in the router `AGENTS.md`.
  - Measured: the gate reports 6 lines in 4 files before the fix and 0 after. The pass 2 log says five files, but the six lines it lists are in four. About 18 lines remain in dated records, which the gate exempts on purpose.

## Other kept changes: checks, routing and documentation

These changes add checks, tighten routing and make the commands portable. Each item names its commit and says how it was measured.

### New checks and tests

- **Hard file ceiling and package parity** (`4066815`, `f0e5234`).
  - `scripts/check_marketplace.py`, run by `validate_skills.py`, fails when the checkout or the package passes 5,000 entries. It also fails when marketplace identity, version or source drift from the plugin, when the plugin's skill list differs from the `SKILL.md` files on disk, or when a skill path escapes or is a symlink. A traversal error fails closed.
  - Five tests include both boundary counts.
  - Measured at `b608bcb`: 870 checkout files (the count includes `.git`, so it grows with every commit) and 530 package files, against the limit of 5,000.
- **Source currency register and its gate** (`be2c774`, `affb97f`).
  - A dated register of volatile procurement, AI and data-protection claims, with a gate that rejects expired, malformed and future-verified rows.
  - Pass 2 grew it from 11 records (7 `SCOPED`, 4 `NOT_ASSESSED`) to 14 (10 and 4) after reading the primary sources. It corrected the GIZ record to the 1 September 2025 version.
  - Pass 2 also made the gate refuse a `NOT_ASSESSED` row that carries a verified date, a non-https URL, an unknown freshness class and a volatile review window over 45 days (7 tests, was 3).
  - Measured: both counts, and `check_source_currency.py` exits 0. By design the gate fails from 2026-12-01 until the records are re-verified, as [Date-triggered gates](#date-triggered-gates) says. It checks metadata only and verifies no claim.
- **CI runs every registered check** (`7ad4f13`).
  - `.github/workflows/skill-quality.yml` ran 2 commands and now runs 6: skill validator, routing, link gate, ingestion guardrail, fixture check and the unit suite.
  - Measured: the workflow lists 2 commands at `9089c0a` and 6 now, and the same commands exit 0 locally.
  - It was not run on a GitHub runner (`NOT_ASSESSED`).

### Routing and discoverability

- **Routing metrics that show first-rank accuracy** (`feea230`).
  - The runner reported only whether the expected skill was in the top three (100%). That hid the fact that it ranked first for 19 of 26 fixtures.
  - It now reports first-rank accuracy and checks forbidden primary routes (owned negatives). The fixtures grew from 26 to 31.
  - Measured: 19/26 (new runner over the earlier tree) before, 23/31 after. One collision stays visible: the World Bank full technical proposal (FTP) prompt ranks UNDP first.
- **Bidder wording and three-plus-two fixtures** (`635e76a`).
  - The descriptions of `ppda-uganda`, `world-bank`, `afdb` and `06-methodology` gained the words bidders use, for example "open domestic bidding" and "bid data sheet".
  - Each of the four now has three positive and two owned-negative fixtures. Before, only one skill had them, per the pass 2 log.
  - Measured: the original 31 fixtures move from 23 to 24 first-rank hits. The 41-fixture set scores 32/41 first-rank, 41/41 in the top three and 7/7 owned negatives. This is a lexical proxy over descriptions, and 111 of 115 skills still lack that fixture coverage.

### Documentation and portability

- **Commands that run on Linux** (`dbc2f88`, `31c3cc9`, `49f1c5a`).
  - Contributor docs, the router and the README replaced PowerShell blocks and backslash paths with `python3` commands. The README gained the Validation section (seven checks, dependencies, expected results).
  - Install goes through `bash install.sh`, because git stores the file without the executable bit.
  - A router path to a skill that does not exist (`skills/ai-agent-pricing-and-packaging-proposal`) now points to `skills/ai-agent-proposals/ai-agent-pricing-and-packaging-proposal`.
  - Measured: the seven registered checks exit 0 on this Linux host. The preview, install, `doctor` and uninstall sequence into a scratch project installed 353 files including 115 `SKILL.md`. `doctor` reported 0 missing and 0 modified, and uninstall removed 353. `install.ps1` was not run (no `pwsh`).
- **Documentation index and gate calendar** (`c28f206`, `81caeef`, `b608bcb`).
  - `docs/README.md` grouped the 16 entries of `docs/` when it was written. [`07-docs-followups.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md) records what the wave left alone and the cross-engine mismatches. [Date-triggered gates](#date-triggered-gates) names the one gate that depends on the calendar.
  - The behaviour on 2026-11-30 and 2026-12-01 was checked by replacing `date.today` for one process, as recorded in that file. It was not re-run for this section.

## Sources and references

The citation lists moved to [References and sources](docs/references.md), so that this README stays short. They hold citations only. No book content is stored in this repository.

- [Books](docs/references.md#books), listed by author, year and title where the repository records them.
- [Repositories](docs/references.md#repositories): the sister engines, and the outside projects whose patterns this engine adapted, with licence and commit where recorded.
- [Standards and official sources](docs/references.md#standards-and-official-sources): Uganda, World Bank, AfDB, United Nations, other development partners, data protection and AI governance, and assurance and quality standards.
- [Websites and articles](docs/references.md#websites-and-articles).

## Contributing, author and licence

- **Contributing.** [`CONTRIBUTING.md`](CONTRIBUTING.md) explains how to add or change a skill and which checks to run. Start from the [authoring standard](docs/skill-authoring-standard.md) and the [skill template](templates/skill-template.md).
- **Adding a skill.** Add one only for a repeatable workflow or domain contract that has its own justification, never to improve a metric.
- **Author.** Peter Bamuhigire (techguypeter.com).
- **Licence.** MIT, copyright 2026 Peter Bamuhigire. See [`LICENSE`](LICENSE).
