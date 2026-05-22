# AI-Agent SLA and Commercial Proposal Layer — Audit 2026

Internal audit produced for the proposal-skills engine to close the **AI-agent SLA and commercial contracting** gap left open after the 2026 AI-agent product-skill hardening session. The agent-product stack (discovery, business case, pricing patterns, POC, methodology, risk, compliance, procurement, change management, team, vertical positioning) now covers the *what we will build and operate* and the *price we will charge*. It does not yet cover the *contract clauses, SLA classes, credit schedules, refund clauses, MSA/SLA addendums, outcome-pricing language, intervention-credit mechanics, and procurement-objection commercial responses* that the buyer's legal, procurement, finance, and supervision functions will demand before signature.

Agents are the most commercially exposed AI class proposed. A copilot that hallucinates produces a bad draft a human discards. An agent that hallucinates pays the wrong supplier, ships the wrong stock, sends the wrong letter, files the wrong claim, refunds the wrong customer. The commercial layer therefore has to do three things SaaS commercials never had to do at this intensity:

1. Define the unit of value (resolution / outcome / step / agent) tightly enough to survive procurement scrutiny.
2. Tie operational SLOs (task-success, intervention rate, time-to-resolve, kill-switch, audit-log completeness) to **money** through a credit schedule.
3. Provide an **honest exit** for the buyer (abort and refund) when the agent's autonomy curve fails.

This audit defines the dedicated commercial / contractual arsenal — SLA classes with credit schedules, contract-language pack, success-fee and outcome-pricing structures, intervention-credit and abort-refund mechanics, MSA/SLA addendums specific to agentic engagements, packaging patterns, procurement-objection commercial handling, renewal and true-up mechanics, and vertical SLA variants — so the agent proposal can be read end-to-end by procurement, legal, finance, and CISO with the same conviction the technical proposal currently gives to the head of operations.

## Scope of This Audit

The audit covers engagements with at least three of these characteristics:

1. The deliverable is one or more **autonomous AI agents** acting on the buyer's behalf, priced under one of the six agent pricing patterns (per-resolution / per-outcome / per-step / per-agent / hybrid / success-based).
2. The buyer's procurement, legal, or finance team will negotiate a **service-credit schedule** tied to operational SLOs (uptime, task-success, intervention rate, time-to-resolve, kill-switch).
3. The buyer expects a **refund or pro-rata exit** if the agent fails to reach autonomy, if an irreversible-action incident occurs at the agency's fault, if the regulator intervenes, or if the model-cost pass-through breaches its cap.
4. The engagement requires an **MSA and SLA** that explicitly recognises the agent's action accountability, audit-log retention, kill-switch SLA, replay availability, and contractual evidence pack.
5. The buyer is in a regulated vertical (financial services, public sector, healthcare, insurance) where the SLA must be **regulator-aware** (consumer-protection rules, public-sector procurement rules, clinical-safety rules).

## What the Engine Has Today

| Existing asset | What it covers | Gap for the commercial / contractual layer |
|---|---|---|
| `skills/ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md` | Six pricing patterns; intervention credit, vendor pass-through, fair-use, abort and refund, autonomy ramp, FX (all named) | The clauses are named, not drafted as ready-to-paste contract language. No SLA class table. No packaging-pattern decision matrix. No outcome-definition rigour. No success-fee structures. |
| `skills/profiles-sectors/references/ai-agent-pricing-models-reference.md` | Worked examples per pattern; one-paragraph sample clause per pattern; cross-pattern clauses (pass-through, fair-use, abort and refund, autonomy ramp, FX) | Sample clauses are illustrative, not exhibit-grade. No pricing exhibit template. No outcome-pricing exhibit. No success-definition rigour. No FX corridor / sovereign-AI pass-through depth. |
| `skills/profiles-sectors/references/saas-msa-dpa-sla-template-language.md` | MSA / DPA / SLA clause themes; SLA tier table (Starter / Pro / Enterprise) on availability only; severity table; credit mechanism; carve-outs | Agent-specific dimensions absent: task-success, intervention rate, time-to-resolve, kill-switch SLA, audit-log completeness, replay availability, fee-for-evidence-pack on dispute, action accountability, model-provider force-majeure. No agent SLA class table. No agent MSA addendum template. |
| `skills/ai-agent-proposals/ai-agent-business-case-and-roi/SKILL.md` | Cost stack and downside scenarios | Credit cost is not modelled into the downside as a P&L line. Service credits are not stress-tested against margin floor. |
| `skills/ai-agent-proposals/ai-agent-procurement-and-questionnaire/SKILL.md` | Ten agent procurement domains | Commercial/contractual answers (SLA, credits, refund, abort, indemnity sub-cap for agentic action, audit-log fee on dispute) are not surfaced as a domain. |
| `skills/strategy-positioning/sales-discovery-and-objection-handling/SKILL.md` | Generic objection handling | No commercial objection map for agents ("we don't pay for failed tasks", "we want a price floor", "we want a price corridor", "we want to audit the audit log", "we want a refund if the agent flops"). |
| `skills/strategy-positioning/premium-pricing-and-value-defense/SKILL.md` | Premium fee defence | No agent-specific outcome-pricing defence, no success-fee defence, no "credit is real value" defence. |
| `skills/pipeline/10-financial-proposal/SKILL.md` | Financial proposal narrative + AI commercial structure block + AI-agent commercial structure block | The agent block names clauses; the exhibit-grade language to drop into the financial proposal does not exist. |
| `skills/strategy-positioning/customer-service-and-maintenance-proposals/SKILL.md` | Support, maintenance, SLA, escalation, severity, credit mechanism | Generic SaaS SLA, not agent SLA. No task-success or intervention-rate commitment. No kill-switch SLA. |

The pricing skill names every clause. The reference file gives one paragraph per pattern. The MSA/DPA/SLA reference handles non-agent SaaS. None of these gives the proposal writer or the agency's legal team a **drop-in pricing exhibit, drop-in SLA exhibit, drop-in MSA addendum, or drop-in refund-policy template** specific to agentic engagements. The financial proposal carries an "AI-Agent Commercial Structure Block" pointer; what it points to is one-paragraph illustrative language. Procurement will reject one-paragraph language.

## What the Engine Lacks (Synthesised)

The engine cannot today produce, end-to-end, a Bain/EY/McKinsey-grade *commercial and contractual layer* for an agentic engagement because eight artefact families are missing:

1. **Agent SLA class table with credit schedule** — Bronze / Silver / Gold / Platinum tiers on a four-metric matrix (availability + task-success + intervention-rate + time-to-resolve), with credit formulas, service-credit cap, out-clauses for force-majeure on the upstream model provider, and exclusions for customer-caused failures. The existing SaaS table is single-metric (availability) and not regulator-aware.
2. **Agent commercial-packaging decision matrix** — "Agent Included in Pro" vs "Agent Add-on" vs "Agent Standalone"; bundling logic; how the agent affects the core SaaS pricing and the SLA the buyer can be promised at each packaging shape. The engine treats agent pricing as a pattern selection, not a packaging selection.
3. **Agent contract-language pack** — drop-in pricing exhibit, SLA exhibit, refund/credit exhibit, abandonment-and-refund language, vendor-cost-pass-through language, FX corridor, dispute resolution, audit rights for SLA metrics. Today the engine has paragraphs, not exhibits.
4. **Agent success-fee and outcome-pricing structures** — gain-share, success fee, hybrid base-plus-success, performance-corridor pricing; how to define an "outcome" precisely (counter-example rule, cooling-off, attribution test, reversal clause); downside protection for the vendor (base covers cost; cap on success fee; floor on units billed).
5. **Intervention-credit and abort-refund mechanics** — formula-grade intervention credit (per-resolution price reduced when human intervention required; sample tables); abort-and-refund language drafted to exhibit standard; customer-facing visibility of credits on the monthly statement so the buyer sees the credit operationally, not just contractually.
6. **MSA / SLA addendum templates for agentic engagements** — drop-in MSA addendum extending `saas-msa-dpa-sla-template-language` with agent-specific clauses: action accountability, audit-log retention, kill-switch SLA, replay availability, fee-for-evidence-pack on dispute, model-provider force-majeure, sub-cap for irreversible-action liability, agent-identity warranty.
7. **Agent procurement-objections on commercials** — "we don't pay for failed tasks", "we want a price floor", "we want a price corridor", "we want to audit the audit log", "we want a refund if the agent fails", "we want unlimited liability for agentic action", "we want indemnity for regulator action" — with ethical, trade-not-give response patterns.
8. **Agent renewal and true-up** — renewal mechanics; true-up clauses when actual volume diverges from plan; ramp-down protection; autonomy-progression price-step language (price re-sets at each autonomy level achieved); index-linked renewal anchored to model-provider price index and FX.

Plus vertical SLA variants for financial services (consumer-protection rules, CBK/CBN/SARB conduct rules), public sector (no outcome pricing, citizen-redress timelines), and healthcare (clinical-safety rules, no autonomous clinical decision).

## NEW SKILLS

Create the following under `skills/<skill-name>/` with `SKILL.md` and `references/` where useful.

| New skill | Why it is its own skill |
|---|---|
| `ai-agent-sla-and-credit-schedule` | An SLA class table with credit schedule is a separate artefact from a pricing pattern. The four-metric matrix (availability + task-success + intervention-rate + time-to-resolve) does not exist in the SaaS SLA reference. Force-majeure on the upstream model provider needs explicit treatment. |
| `ai-agent-commercial-packaging` | Packaging (Included / Add-on / Standalone) is a separate decision from pricing pattern. It changes the SLA the buyer can be promised, the eval and red-team cost recovery shape, and the renewal posture. |
| `ai-agent-contract-language-pack` | The proposal writer needs drop-in exhibit language, not paragraph-grade samples. The pack is a curation skill that points at the right exhibit for the right pattern and shape. |
| `ai-agent-success-fee-and-outcome-pricing` | Outcome pricing has its own discipline: outcome definition, cooling-off, attribution, reversal, counter-example rule, base-plus-success structure, downside protection. Cannot be folded into the six-pattern pricing skill without losing the structure. |
| `ai-agent-intervention-credit-and-abort-refund` | Intervention credit is the agent's signature commercial mechanism. Abort-and-refund is the buyer's emergency exit. Both deserve a dedicated skill so the agency does not give them away by accident or refuse them under pressure. |
| `ai-agent-msa-and-sla-addendum-templates` | The MSA / SLA addendum is a different artefact from the SaaS MSA / SLA. Action accountability, kill-switch SLA, replay availability, fee-for-evidence-pack, model-provider force-majeure are agent-specific. |
| `ai-agent-procurement-objections-on-commercials` | Commercial objections are different from technical and pricing objections. They are negotiated against the SLA, the credit schedule, the refund clause. A separate skill keeps the trade-not-give discipline visible. |
| `ai-agent-renewal-and-true-up` | Renewal in agentic engagements is not the SaaS renewal: autonomy ramps shift the price; model-provider price moves; volume diverges from plan; ramp-down requires protection. A separate skill keeps the levers clean. |

## ENHANCED SKILLS

| Skill | What changes |
|---|---|
| `ai-agent-pricing-and-packaging-proposal` | Add packaging-pattern decision matrix; add SLA-tier alignment with pricing tier; cross-link new SLA and credit skills; pointer to the new contract-language pack. |
| `ai-agent-business-case-and-roi` | Add a credit-cost line into the downside scenarios; stress-test margin floor against the credit schedule at P50 / P90 / P99 intervention; size the worst-credit-month. |
| `ai-agent-procurement-and-questionnaire` | Add an eleventh domain (commercial / contractual answers): SLA, credits, refund, abort, indemnity, audit rights on the audit log, evidence-pack fee on dispute. |
| `references/saas-msa-dpa-sla-template-language.md` | Cross-link to the new agent MSA addendum and SLA addendum. |
| `premium-pricing-and-value-defense` | Add agent-specific value defence (outcome pricing, success fee, "credit is real value"). |
| `10-financial-proposal` | Enhance the agent commercial structure block: drop-in exhibits referenced by name (pricing exhibit, SLA exhibit, refund clauses). |
| `sales-discovery-and-objection-handling` | Add agent commercial objections (the ten common procurement asks) with trade-not-give response patterns. |
| `customer-service-and-maintenance-proposals` | Add agent SLA, credit, refund commitments lens. |

## NEW REFERENCES

Drop into `skills/profiles-sectors/references/` as ready-to-paste contract language.

| Reference | Purpose |
|---|---|
| `ai-agent-sla-class-table.md` | Full Bronze / Silver / Gold / Platinum with metric thresholds and credit schedule. |
| `ai-agent-sla-exhibit-template.md` | Drop-in SLA exhibit for an MSA. |
| `ai-agent-pricing-exhibit-template.md` | Drop-in pricing exhibit covering the five patterns + intervention credit + abort refund + vendor pass-through + FX. |
| `ai-agent-credit-and-refund-clauses.md` | Exact contract language for credits and refunds. |
| `ai-agent-outcome-pricing-clauses.md` | Gain-share, success-fee, hybrid base-plus-success language. |
| `ai-agent-msa-addendum-template.md` | MSA addendum for agentic engagements. |
| `ai-agent-abandonment-and-refund-policy-template.md` | Customer-facing policy language. |
| `ai-agent-packaging-pattern-decision-matrix.md` | Bundled vs add-on vs standalone with worked examples. |
| `ai-agent-dispute-resolution-and-audit-rights.md` | SLA dispute mechanics, evidence-pack fee, audit-log access. |
| `ai-agent-commercial-objection-handling.md` | Ten common procurement objections with response patterns. |
| `ai-agent-renewal-and-true-up-clauses.md` | Renewal mechanics, true-up, ramp-down protection. |
| `ai-agent-success-definition-language.md` | How to define "success" precisely in contract. |
| `ai-agent-vendor-cost-pass-through.md` | Pass-through, indexed pricing, foundation-model-provider price change. |
| `ai-agent-sla-financial-services.md` | Vertical SLA variant for FS (CBK / CBN / SARB conduct rules). |
| `ai-agent-sla-public-sector.md` | Vertical SLA variant for public sector (no outcome pricing; citizen-redress timelines). |
| `ai-agent-sla-healthcare.md` | Vertical SLA variant for healthcare (no autonomous clinical decision; admin-only). |

## Africa Context Notes

- FX clauses must cover KES / NGN / UGX / RWF / ZAR with explicit reference rate and 15 % corridor.
- Sovereign-AI provider pass-through (Granica / Inception / local hosted models) needs its own pass-through clause distinct from the global model providers.
- Collection-cycle realities (45–90 days in some markets, longer in public sector) make per-resolution pricing dangerous without a floor and a base; this is reflected in the packaging decision matrix.
- Public-sector buyers will not accept outcome pricing on citizen services on political grounds; SLA variants reflect this.
- Several FS regulators (CBK, CBN, SARB, BoU, BNR) now require named accountability for automated decisioning; the MSA addendum reflects this with an explicit accountability clause.

## Cross-Engine Handoff

- **Software-dev session** owns: kill-switch architecture, audit-log retention and completeness mechanics, replay determinism, intervention-detection telemetry, the engineering enforcement of every metric this layer commits to. The SLA cannot be more aggressive than the engineering can prove.
- **Business-plan session** owns: credit-cost into the P&L, margin floor against the credit schedule, revenue-recognition for outcome and success-fee structures, FX hedge cost, model-provider concentration risk, contingency reserve for irreversible-action incidents.
- **This session** owns: the language that makes commitments contractual, the credit schedule that makes them enforceable, the refund clause that makes the buyer's exit honest, the addendum that makes the MSA agent-aware, and the procurement-objection responses that protect margin without breaking the relationship.
