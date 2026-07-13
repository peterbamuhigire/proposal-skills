# July 2026 conformance upgrade record

Date: 13 July 2026

Engine: `C:\wamp64\www\proposal-skills`

Benchmark: canonical `skills-web-dev` skill-writing, composition, engine-audit, anti-slop, and slop-audit contracts.

## Scope and inventory

- Active root: `skills/`.
- Active entrypoints before and after: 107. No skill was added, removed, renamed, consolidated, or deactivated.
- Inactive template artefacts before: 20. After: 21, including the new repository authoring template at `templates/skill-template.md`.
- Inactive skill aliases identified: 0.
- Pre-existing domain knowledge, procurement frameworks, profiles, examples, references, and cross-engine finance/design routes were retained.

## Before state

The canonical scanner reported 0 of 107 skills fully compliant.

| Canonical finding | Count |
|---|---:|
| Capability contract | 81 |
| Decision rules | 106 |
| Degraded mode | 90 |
| Five anti-patterns | 58 |
| Frontmatter YAML | 1 |
| Directory/frontmatter identity | 28 |
| Input contract | 104 |
| Line limit | 3 |
| Output contract | 7 |
| Portable metadata | 107 |
| Portable sections | 17 |
| Trigger description | 85 |

The main causes were legacy descriptions that did not begin with `Use when`, missing portable metadata, prose-only inputs and outputs, absent permission and degraded-mode boundaries, no decision tables, and entrypoints that pre-dated the 500-line contract. Ninety-three direct child reference files lacked a backlink to their parent skill, and 442 resolvable Markdown-file references were code-formatted paths rather than checked links.

## Implemented cohorts

| Cohort | Active skills | Result |
|---|---:|---|
| SaaS and AI-on-SaaS | 25 | Normalised in place; domain contracts and neighbour routes retained. |
| AI-agent product and commercial | 19 | Normalised in place; autonomy, safety, SLA, pricing, and contract logic retained. |
| Domain delivery and pipeline | 26 | Normalised in place; proposal-section and delivery logic retained. |
| Profiles, procurement frameworks, and sectors | 16 | Normalised in place; identity and framework routes retained. |
| Strategy and writing | 12 | Normalised in place; finance, website, AI, premium, service, and commercial-writing routes retained. |
| Parent, language, meta, and blog writer | 9 | Normalised directly by the release owner. |

The overlength multilingual and blog-writing entrypoints were preserved as directly linked reference guides and replaced with concise execution entrypoints. Reference backlinks were added without changing substantive reference content.

## Local controls added

- `docs/skill-authoring-standard.md` and `templates/skill-template.md`.
- `scripts/validate_skills.py` with zero-debt baseline comparison.
- `quality-baseline.json` with 107 active skills and empty failure counts.
- `tests/fixtures/routing-fixtures.json` with 18 positive, negative, collision, limited-capability, and failure-path fixtures.
- `scripts/routing_smoke_test.py`, requiring the expected skill in the top three for every fixture.
- `.github/workflows/skill-quality.yml` for pushes to `main` and pull requests.
- `CONTRIBUTING.md` with authoring, validation, and release procedure.

## Final conformance evidence

| Gate | Result |
|---|---|
| Local validator against zero-debt baseline | 107 active skills; 0 findings |
| Routing smoke test | 18/18 fixtures; 100% expected-skill-in-top-three precision; threshold 100% |
| Canonical engine scanner | 107/107 fully compliant; 0 findings |
| Canonical quick validator | 107/107 skill directories passed |
| Active entrypoint line limit | 0 over 500 lines |
| Direct-child reference backlinks | 93 repaired; 0 residual findings |
| Direct reference paths | 442 converted to checked Markdown links; 0 unlinked reference bullets |
| Broken relative links | 0 |
| Git whitespace check | Passed |
| Skill safety audit | Safe; no unsafe installer, credential harvesting, hidden execution, or excessive privilege introduced |
| Anti-slop audit | Grade A; no blocking finding or evidence-free filler retained in changed human-facing content |

## Capability work outside conformance

The April/July capability score and its proposed expansion remain separate from conformance debt. Full model bids, evaluator simulation, compliance-matrix expansion, finance workbook exemplars, rendered document/deck proof, and live-source refresh automation are future capability work; none is required to clear the structural zero-debt gate.
