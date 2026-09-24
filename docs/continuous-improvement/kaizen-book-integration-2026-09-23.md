# Kaizen: Book Integration and Extraction Removal (2026-09-23)

## Scope

- Engine: `proposal-skills`. Owner: Peter Bamuhigire.
- Inputs: staged book extractions held outside the repository (not stored here), the Digital Research currentness register of 2026-09-23 (claims cited by ID in the new references), and the engine's routers and authoring standard.
- Model-currentness review: `NOT_ASSESSED` in this cycle (owned by the orchestrator).

## Changes

1. **Proposal language standard.** Added `proposal-power-paragraph-method.md` and `proposal-phrase-bank.md` under `premium-commercial-writing/references/`; wired into pipeline 01–10, `premium-commercial-writing`, `language-standards`, `east-african-english`, `anti-ai-slop` and `ai-slop-audit`.
2. **New skills.** `strategy-positioning/key-account-pursuit-and-account-plan` (four references) and `strategy-positioning/tender-orals-and-proposal-presentation` (two references), with five routing fixtures.
3. **New references.** Strategic-account negotiation; offer presentation and price order; marketing and digital services proposals (with handoffs to business-plan and social-media engines); website ownership, care plans and direction boards; objection root causes and closing language; strategic options evaluation; strategy workshops and hypothesis testing; product reasoning and estimation; weighted strategic-factor analysis; case-study and past-performance structure; SaaS commercial motion and close discipline; technical proposal evidence bridge; human-English editorial standard; copyright-safe source use (rewrite of the former book-extraction audit note).
4. **Extraction removal.** `book-extractions/` (15 files) removed with `git rm -r`; links repointed; guardrail now rejects any `book-extractions/` path; rule added to `AGENTS.md`, `rules/common/core.md`, the authoring standard and the source-distillation reference.
5. **Pre-existing compliance debt fixed.** Three engine-compliance findings (two degraded-mode wording gaps, one empty-section pattern) resolved.

## Capability preservation map (removed files)

Every capability taught by each removed file and where it now lives. Dropped items are listed with the reason.

| Removed file | Capability | Now lives in |
|---|---|---|
| `human-english-craft-synthesis-2026.md` | Proposal standard (write for the evaluator's decision) | `skills/language/language-standards/references/human-english-editorial-standard.md` |
| same | Five passes (frame, journey, evidence, revise, proof) | same, "Five passes" |
| same | Craft rules (register, grammar checklist, claim-evidence-warrant-countercase-implication) | same, "Craft rules" |
| same | Glossary and classification discipline; confusable-word checks | same, "Craft rules" |
| same | Anti-slop questions | same, "Anti-slop questions" |
| same | Evidence record | same, "Evidence record" |
| same | Collocation overlay link | same, final section |
| same | Source-limits note (title-only stubs) | Dropped: bibliographic detail about unusable files; no capability |
| `2026-09-14-technical-proposal-synthesis.md` | Outcome → scenario bridge (five elements) | `skills/profiles-sectors/references/technical-proposal-evidence-bridge.md` §1 |
| same | Engineering credibility checks | same §2 |
| same | Deliberate exclusions | same §4 |
| same | Source list | same, concept-input line |
| `2026-09-11-commercial-persuasion-and-growth-synthesis.md` | Evaluator journey stages | `premium-commercial-writing/references/buyer-psychology-and-evaluator-persuasion.md` |
| same | Innovation as bounded pilots | same, "Test before scale" |
| same | Transparent choice, proof, authority, commitment cues | same, operating rules |
| same | Context and memory cues | same |
| same | Copy craft after compliance | same, "Copy sequence" |
| same | Provenance block | Dropped: bibliographic detail, already in the 2026-09-11 Kaizen record |
| `premium-commercial-writing-audit-synthesis-2026.md` | Premium writing sells confidence; claim → mechanism → proof → control → benefit | `premium-writing-quality-gate.md` proof discipline |
| same | Executive summary leads with decision problem; cover letter relevance/trust/next step | `document-section-patterns.md`; `proposal-phrase-bank.md` §2–3 |
| same | Case study context/role/intervention/result/relevance | `document-section-patterns.md`; `05-relevant-experience/references/case-study-and-past-performance-structure.md` |
| same | Premium pricing requires value logic and trade-offs | `premium-writing-quality-gate.md`; `offer-presentation-and-price-order.md` |
| same | SEO/AI-search applies to public assets | `seo-ai-search-writing.md` |
| same | Copyright boundary | `copyright-safe-source-use.md` |
| `saas-sales-method-ae-proposal-extraction.md` | ICP and critical event | `saas-discovery-and-qualification`; `saas-discovery-question-bank.md` |
| same | Pain chain, impact per role, consensus vs hierarchy decisions | same; `meddic-and-command-of-message-for-saas.md` |
| same | Prescribe: customer story, demo/POC, objection map | `saas-demo-script-template.md`; `saas-objection-handling-playbook.md` |
| same | Provocation: surfacing an evidence-based risk the buyer is not measuring | `saas-demo-script-template.md` "Provocation" section (added in verification fix); `saas-objection-handling-playbook.md` "Pre-empting Objections with a Provocation" |
| same | Select: decision criteria, competitive categories | `saas-objection-handling-and-competitive-displacement` |
| same | Quote / impact proposal / business case layers | `saas-commercial-motion-and-close-discipline.md` §1 |
| same | Going dark discipline | same §3; `objection-root-cause-and-closing-language.md` §7 |
| same | Trade discipline; accelerated close | same §5; `strategic-account-negotiation.md` |
| same | Role-mirroring (3×3) orchestration | same §4 |
| same | Mutual action plan | `saas-mutual-action-planning-and-close-plans`; `saas-mutual-action-plan-template.md` |
| same | Not-a-fit discipline | same §2 |
| same | Named proprietary patterns ("Crazy Ivan" label, exercises) | Dropped: proprietary names; the underlying stalled-negotiation reset is covered as trade discipline and equivalent-value options |
| `saas-sales-method-fundamentals-proposal-extraction.md` | Discovery conversation template; relevance/respect/recency | `saas-commercial-motion-and-close-discipline.md` §11 |
| same | Objection vs rejection | same §11; `objection-root-cause-and-closing-language.md` §1 |
| same | Follow-up as a system; value in every touch | same §3, §11 |
| same | Purposeful meetings (purpose, artefact, decision) | same §9; `08-work-plan` governance section |
| same | Lifecycle email as deliverable | `saas-lifecycle-communications-as-deliverable` |
| same | Proprietary technique names | Dropped: trademarked labels |
| `saas-email-marketing-playbook-proposal-extraction.md` | Six lifecycle programmes | `saas-lifecycle-communications-as-deliverable`; `saas-lifecycle-email-program-proposal-template.md` |
| same | Data implementation plan workstream | same; `data-management` |
| same | Operating rules | same; `saas-commercial-motion-and-close-discipline.md` §9 |
| same | Internal-control measurement over benchmarks | same §9; `monitoring-and-evaluation` |
| same | First-90-days communication plan | `saas-customer-success-and-adoption-proposal` |
| `hacking-saas-proposal-extraction.md` | GTM motion as costable workstream | `saas-gtm-motion-design-reference.md` |
| same | Channel decay monitoring | same; `saas-commercial-motion-and-close-discipline.md` §9 |
| same | Two-of-everything redundancy | `07-team-composition`; AI team skills |
| same | Sales enablement workstream | `saas-commercial-motion-and-close-discipline.md` §9 |
| same | Experiment register; pricing experimentation | same §9; `saas-gtm-motion-design-reference.md` |
| same | Build-vs-buy narrative | `saas-vendor-vs-build-narrative.md` |
| `how-to-run-a-saas-business-proposal-extraction.md` | SaaS financial vocabulary | `saas-metrics-glossary-for-proposals.md` |
| same | Segment shapes (enterprise, mid-market, consumer) | `saas-commercial-motion-and-close-discipline.md` §6 |
| same | Horizontal vs vertical SaaS | `saas-vertical-positioning` |
| same | Sales capacity plan, quota, OTE | `saas-commercial-motion-and-close-discipline.md` §9 |
| same | Services attach rate; Rule of 40 and magic number for investor-grade buyers | `saas-metrics-glossary-for-proposals.md`; `02-executive-summary` references |
| `the-saas-playbook-walling-proposal-extraction.md` | Vertical positioning briefs | `saas-vertical-positioning`; vertical references |
| same | Tiering, expansion, freemium, card-first trial, price increases | `saas-pricing-models-reference.md`; `saas-commercial-motion-and-close-discipline.md` §7 |
| same | Dual funnels | same §7 |
| same | Demo structure (problem-first, prospect-specific, proof) | `saas-demo-script-template.md` |
| same | Recorded, role-specific demo library as a hand-over deliverable | `saas-demo-script-template.md` "Demo Library as a Hand-Over Deliverable" (added in verification fix) |
| same | Growth and drag measures | same §8 |
| same | Churn protection and net negative churn | same §7; `saas-customer-success-and-adoption-proposal` |
| same | Phased first-paying-customer funding | same §7 |
| `building-multi-tenant-saas-architectures-proposal-extraction.md` | Control and application planes | `saas-multi-tenant-architecture-credibility-block`; `saas-multi-tenant-architecture-block.md` |
| same | Tenant isolation as trust lever; tenant context | same |
| same | Cost attribution, noisy neighbour, tiering | same; `saas-implementation-methodology` |
| same | Automated onboarding | same |
| same | Install-base migration | same; `saas-commercial-motion-and-close-discipline.md` §10 |
| same | SaaS mindset change | `saas-pilot-to-rollout-change-management` |
| `saas-proposal-skills-audit-2026.md` | New-skill and enhancement plan (14 skills, 25 references) | All present under `skills/saas-proposals/` and `skills/profiles-sectors/references/` (verified by file check); `saas-discovery-conversation-script.md` was never created and its content is now §11 of the SaaS commercial-motion reference |
| same | Open gaps and follow-up sessions | This document, "Open backlog" |
| `ai-on-saas-proposal-audit-2026.md` | Eleven AI-on-SaaS skills and 20 references | All present under `skills/ai-on-saas-proposals/` and `skills/profiles-sectors/references/` (verified) |
| same | Open gaps and follow-up sessions | This document, "Open backlog" |
| `agent-products-proposal-audit-2026.md` | Eleven agent skills and 21 references | All present under `skills/ai-agent-proposals/` and references (verified) |
| same | Composition rules: stand-alone agent; agentic layer inside SaaS (both stacks); copilot with actions at lighter weight (autonomy L1–L2, small action catalogue, human approval on every action) | `ai-agent-methodology` "Composition With Other AI Families" table and a decision row in `skills/SKILL.md` (added in verification fix) |
| same | Open questions | This document, "Open backlog" |
| `agent-sla-commercial-proposal-audit-2026.md` | Eight commercial skills and 16 references | All present under `skills/ai-agent-commercial/` and references (verified) |
| same | Africa context notes (collection cycles, public-sector outcome pricing, named accountability) and ownership split | `ai-agent-sla-and-credit-schedule` "Africa Context and Ownership Boundary"; FX corridor in commercial skills |
| `premium-commercial-writing/references/book-extractions-audit-synthesis.md` (renamed) | Permitted and prohibited use; synthesis themes; acceptance checklist | `premium-commercial-writing/references/copyright-safe-source-use.md` |

Unmapped rows: none.

## Open backlog carried from the removed audit notes

1. Country-specific AI and data regulator reference pack (Kenya ODPC and AI strategy, Nigeria, South Africa, Uganda NITA-U and PDPO, Rwanda NCSA).
2. Worked competitive-displacement examples once win-loss evidence exists.
3. AI evaluation harness code templates (hand-off to the engineering and SRS engines).
4. Sovereign-AI commercial benchmarks for African deployments.
5. EU AI Act conformity-assessment worked example for export bids.
6. Multi-agent governance depth; buyer-facing agent benchmark posture; agent-on-agent commercial models; autonomous coding-agent vertical.
7. Local SaaS price-point evidence by vertical; procurement-framework overlay (World Bank, AfDB, UNDP) on SaaS pricing.
9. Vertical SaaS positioning briefs for agribusiness and supply chain, NGO programme operations, and SMB ERP (named in the 2026 SaaS audit but not yet authored).
8. Win-loss debrief: now covered by `objection-root-cause-and-closing-language.md` §8; close this item after first use on a real bid.

## Verification

Run on 2026-09-23 (see the engine ledger for exact output): skill validator (zero findings, 115 skills), routing smoke test (25 fixtures, 100%), encoding and link gate, source-ingestion guardrail (zero findings), engine compliance (115 of 115), unit tests. Product quality remains capped at 65 until a real proposal exercises the new references with reviewer evidence. Re-audit by 2026-10-23.

## Verification-fix addendum (2026-09-24)

Independent verification returned PASS-WITH-GAPS. Fixes: restored the provocation step, the copilot-with-actions composition rule, the role-specific demo library and the vertical-SaaS backlog item (rows above); restructured the negotiation procedure, pre-meeting presentation checklist, claim-to-proof register, weighted-factor procedure, strategic-audit workstreams, GRASP filling procedure and Account Cube grid into this engine's own order and wording (named frameworks retained and attributed); moved the README capabilities table directly after the purpose paragraphs; replaced realistic business names in phrase-bank examples with bracketed placeholders.

## Copyright remediation addendum (2026-09-24)

An independent reviewer found no violations but flagged 11 references as borderline single-book digests. All 11 were rewritten in place into the engine's own task order and wording, with named frameworks kept and briefly attributed: `proposal-power-paragraph-method.md`, `capacity-development-frameworks.md`, `storytelling.md`, `product-reasoning-and-estimation.md`, `institutional-strengthening-and-sustainability.md`, `data-governance-frameworks.md` §1–4, `strategy-workshops-and-hypothesis-testing.md`, `weighted-strategic-factor-analysis.md`, `pragmatic-strategy-and-grasp-mapping.md`, `orals-preparation-and-room-readiness.md` and `proposal-strategy-and-persuasion.md` §1–6 and §12. A per-file capability checklist confirmed no capability was lost (0 missing items). A new rule, "references are never single-book digests", was added to `AGENTS.md`, `rules/common/core.md`, the authoring standard and `copyright-safe-source-use.md`.
