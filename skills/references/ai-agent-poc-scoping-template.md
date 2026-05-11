# AI-Agent POC Scoping Template

Full template for scoping an AI-agent pilot with the three pilot stages (Shadow → Supervised → Agentic), binary thresholds, abort conditions, and exit-to-production gates. Pairs with `ai-agent-poc-and-pilot-scoping`.

## Agent POC Charter (one page)

- **Workflow** — one sentence.
- **Outcome owned by agent** — one sentence.
- **Volume** — per day, per tenant.
- **Autonomy commitment** — per action class.
- **Action catalogue v0** — bullet list, with reversibility class.
- **Time-box** — 8 to 16 weeks.
- **Production decision** — one binary go / no-go question this pilot answers.
- **Abort triggers** — three named conditions.
- **Fee** — pilot fee with abort-fee structure.
- **Signed by** — agency Engagement Lead and buyer SteerCo Chair.

## Three-Stage Pilot Plan

### Stage 1 — Shadow Mode (Weeks 1–4)

- **What** — Agent runs against real or carefully selected shadow traffic; the agent does **not** take actions; every proposed action is logged.
- **Why** — Discover failure modes; calibrate abstain; verify scope-confinement under realistic load before exposing systems.
- **Success thresholds** —
  - Agreement rate with human reviewer ≥ 85 % on the action-class level.
  - Agreement rate ≥ 75 % on the outcome level (a higher bar on full task is acceptable later).
  - Abstain-correctness ≥ 0.90 on the should-abstain subset of the golden set.
  - Zero scope breaches in shadow logs.
- **Evidence pack** — agreement-rate report by action class; disagreement-class analysis; abstain-correctness report; scope-confinement audit.
- **Gate** — buyer signs Stage-2 transition.
- **Abort triggers** — agreement below 60 %; one scope breach not detected internally; one prompt-injection success.

### Stage 2 — Supervised Mode (Weeks 5–12)

- **What** — Agent acts on **reversible** actions; named humans confirm every irreversible action; oversight queue is live; intervention SLA measured.
- **Why** — Test the human-in-the-loop design under live load; verify intervention SLA; verify kill-switch readiness; harden audit log.
- **Success thresholds** —
  - Task-success ≥ 80 % on reversible actions (defined per action class).
  - Intervention rate ≤ 20 % at week 8; trending down.
  - Zero unauthorised irreversible actions (cumulative).
  - Audit-log completeness ≥ 99 %.
  - Kill-switch drill executed at least once with sub-60-second time-to-stop.
- **Evidence pack** — task-success rate, intervention curve, scope-confinement audit, oversight-queue metrics, kill-switch drill log.
- **Gate** — buyer signs Stage-3 transition.
- **Abort triggers** — any unauthorised irreversible action; sustained intervention rate above 35 %; failed kill-switch drill.

### Stage 3 — Agentic Mode (Weeks 12–16)

- **What** — Agent acts on reversible actions without confirmation; irreversibles remain HITL per the autonomy commitment; humans on the loop monitor metrics, audit sample, intervene on flag.
- **Why** — Verify production-ready operation; confirm autonomy at the agreed level; produce the production-exit evidence pack.
- **Success thresholds** —
  - Task-success ≥ 85 % sustained.
  - Intervention rate ≤ 12 % for two consecutive weeks.
  - Zero scope breaches.
  - Audit-log completeness ≥ 99 %.
  - Red-team pass at agent-specific catalogue.
  - Kill-switch drill executed a second time at sub-60-second time-to-stop.
- **Evidence pack** — production-readiness pack with all the above plus a regulator-grade replay sample.
- **Gate** — production exit decision based on full evidence pack.
- **Abort triggers** — any irreversible-action incident at agency fault; sustained intervention above ceiling; red-team failure on critical attack class.

## Golden Dataset Specification

| Item | Specification |
|---|---|
| Size | 200–500 cases (sector-dependent; financial services may require more for sanctions / AML) |
| Source | Anonymised production cases + curated adversarial cases |
| Adversarial cases | Prompt injection via tool output; scope-edge cases; irreversibility-edge cases; multilingual cases; regulator-sensitive cases |
| Labelling owner | Named domain SME on buyer side |
| Sign-off owner | Named buyer-side decision-maker |
| Refresh cadence | Monthly during pilot; quarterly in production |

## Shadow Traffic Specification

- Live or near-live production traffic mirrored to the agent in a read-only mode (the agent decides; the agent does not act).
- Sampling rate sufficient for statistical confidence on action-class level.
- Privacy-preserving where required (token redaction; tenant-scoped traffic only).
- Comparison harness logs human action vs proposed agent action; reviewer adjudicates.

## Success Threshold Table (per use case)

| Metric | Stage 1 (Shadow) | Stage 2 (Supervised) | Stage 3 (Agentic) | Production exit |
|---|---|---|---|---|
| Agreement rate (action) | ≥ 85 % | n/a | n/a | n/a |
| Agreement rate (outcome) | ≥ 75 % | n/a | n/a | n/a |
| Task-success rate | n/a | ≥ 80 % | ≥ 85 % | ≥ 85 % sustained |
| Intervention rate | n/a | ≤ 20 % | ≤ 12 % | ≤ target |
| Irreversible incidents | n/a | 0 | 0 | 0 |
| Audit-log completeness | ≥ 95 % | ≥ 99 % | ≥ 99 % | ≥ 99 % |
| Kill-switch drill | n/a | 1 pass | 2 pass | Quarterly |
| Red-team pass | partial | full at component | full | full |
| Scope breaches | 0 | 0 | 0 | 0 |

## Tenant Confinement in POC

- Per-tenant memory; no cross-tenant state.
- Per-tenant audit log.
- Per-tenant action catalogue where the tenants have different scopes.

## Abort Conditions and Fees

| Trigger | Stage | Effect |
|---|---|---|
| Irreversible-action incident at agency fault | Any | Immediate abort; pro-rata refund of unused pilot fee; evidence pack returned |
| Scope breach undetected by agency | Any | Immediate abort; pro-rata refund; root-cause owed to buyer |
| Intervention rate > 35 % for 2 weeks | Stage 2 | Abort or fall back to Stage 1 with re-scope; agency at risk for re-scope effort |
| Red-team critical attack class failure | Stage 3 | Pause; remediate; re-test before continuing |
| Regulator inquiry | Any | Joint pause; abort option available to either party |

## Exit-to-Production Gate

All of the following must be met:
1. Stage-3 thresholds met for at least two consecutive weeks.
2. Zero irreversibility incidents cumulative.
3. Two successful kill-switch drills.
4. Red-team pass on the full agent attack catalogue.
5. Audit-log completeness ≥ 99 % sustained.
6. Buyer SteerCo and Agent Safety Lead sign-off.
7. Where applicable, regulator notification complete and any required sign-off received.
8. Operations runbook signed; on-call coverage in place; supervisor retraining curriculum delivered.

Partial pass is a **pilot extension**, not a production exit.

## Time-Box and Cadence

- Weekly stand-up; weekly evidence-pack increment.
- Mid-pilot gate at week 8: continue or pivot.
- Two stage-transition gates: Shadow → Supervised; Supervised → Agentic.
- Total time-box: 8 to 16 weeks; extensions in 4-week increments only with stage-gate justification.

## Agent POC Proposal Section Template

> **Pilot Scope.** The pilot covers one workflow — [name] — with one production decision — [name]. The pilot will be staged Shadow → Supervised → Agentic, with binary success thresholds at each stage and named abort conditions.
>
> **Pilot Stages.** Shadow Mode (weeks 1–4): agent proposes, human acts, agreement rate measured. Supervised Mode (weeks 5–12): agent acts on reversible actions, humans confirm irreversible, intervention SLA measured. Agentic Mode (weeks 12–16): agent acts on reversible without confirmation; irreversibles remain HITL.
>
> **Success Thresholds.** [insert from threshold table above].
>
> **Abort Conditions.** Any unauthorised irreversible action; sustained intervention above ceiling; scope breach; failed kill-switch drill; critical red-team failure; regulator inquiry.
>
> **Exit Gate.** All thresholds met for two consecutive weeks; two kill-switch drills passed; red-team pass; audit-log completeness verified; SteerCo sign-off; regulator notification complete where applicable.
>
> **Deliverables.** Charter; golden dataset; action catalogue v1; agent build; oversight queue; kill-switch operations; eval and red-team harness; evidence pack at each stage; production-readiness pack at exit; operations runbook; supervisor retraining curriculum.
>
> **Fee and Abort-Fee.** [insert].
