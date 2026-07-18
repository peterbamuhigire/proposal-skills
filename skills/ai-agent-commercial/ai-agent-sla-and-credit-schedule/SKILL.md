---
name: ai-agent-sla-and-credit-schedule
description: Use when defining an agent SLA and service-credit schedule for availability, task success, intervention rate, resolution time, kill-switch response, or audit-log access.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# AI-Agent SLA and Credit Schedule
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- The proposal must commit to an SLA that is enforceable against the agent's operational reality (not just platform uptime).
- The buyer's procurement, legal, or operations team requires service credits tied to the agent's performance.
- The bid is in a regulated vertical (financial services, public sector, healthcare, insurance) where SLO commitments are mandatory.
- The competitive set includes vendors who promise "99.9 % uptime" as if the agent were a database.
- The MSA must distinguish platform availability from agent task-success, intervention-rate, and time-to-resolve.

## Do Not Use When

- The engagement is non-agent SaaS (use the SaaS SLA section of `saas-msa-dpa-sla-template-language`).
- The engagement is a fixed-fee consulting study with no operational agent.

## Domain Inputs

- The four operational metrics the agent will be measured against (availability, task-success, intervention rate, time-to-resolve) with baseline observed in pilot.
- The autonomy ramp curve from `ai-agent-pricing-and-packaging-proposal` and `ai-agent-methodology`.
- The kill-switch architecture and tested time-to-stop from `ai-agent-compliance-credentials`.
- The audit-log completeness and retention numbers.
- The buyer's tier expectation (Bronze / Silver / Gold / Platinum).
- The agency's margin floor and the maximum credit it can absorb in a single month.
- Model-provider concentration (which providers, what their own SLAs are, what their force-majeure terms are).
- Regulator-specific SLA constraints (e.g. CBK / CBN / SARB conduct rules, public-sector citizen-redress timelines, clinical-safety rules in healthcare).

## Domain Method

1. Decide the **SLA class** the buyer is buying — Bronze (entry), Silver (standard), Gold (regulated), Platinum (mission-critical). The class drives the metric thresholds, the credit percentages, the report cadence, and the termination right.
2. Commit each of the **four agent SLA metrics** to a number per class:
   - **Availability** of the agent control plane and inference path.
   - **Task-success rate** (binary success per the action catalogue's definition, measured monthly).
   - **Intervention rate** (percentage of attempted tasks requiring human correction, override, or completion — directly tied to the intervention-credit clause in the pricing exhibit).
   - **Time-to-resolve** at P50 / P95 (for resolution agents; or time-to-action at P95 for action agents).
3. Add the **operational guardrail SLAs** the agent class needs that no SaaS SLA needs:
   - **Kill-switch SLA** — time-to-stop from authorised command, drill cadence, drill log.
   - **Audit-log completeness SLA** — percentage of agent actions logged with reasoning trace, retention period, replay availability SLA.
   - **Intervention SLA** — time-to-human when the agent escalates.
4. Write the **credit formula** per metric — linear (1 % credit per 0.1 % miss), stepped (10 % at one threshold, 25 % at the next, 50 % at the floor), or capped (no more than X % of monthly fees in any month).
5. Define the **service-credit cap** — typical pattern is 25 % of monthly fees for Silver, 50 % for Gold, 100 % for Platinum, with a hard cap (no compounding across credits).
6. Write the **out-clauses** — force-majeure on upstream model provider (named providers, named outage definition, evidence requirement); customer-fault exclusions (buyer-supplied bad data, buyer-changed action catalogue without change order, buyer-bypassed irreversibility gate); regulator-pause (joint-review trigger).
7. Define the **report cadence** — monthly statement showing observed metric per metric, credits applied, exclusions invoked, evidence link.
8. Tie the **termination right** to consecutive misses — typical pattern is termination right at three consecutive material misses on Gold, two on Platinum.
9. Output the **SLA Exhibit** as an annex to the financial proposal and the MSA.

## The Four Agent SLA Metrics

| Metric | Definition | Why agentic, not SaaS |
|---|---|---|
| Availability | The agent control plane and inference path respond within the agreed latency; the agent is accepting tasks. | A database can be "up" and still wrong; an agent's "up" means it is taking tasks and acting within scope. |
| Task-success rate | Percentage of attempted tasks the agent completed to the action-catalogue's binary success definition for that task class. | A copilot's accuracy is a recommendation; an agent's task-success is its product. |
| Intervention rate | Percentage of attempted tasks requiring human correction, override, or completion. | This is the metric that defines whether the buyer is actually saving FTE; tied directly to intervention-credit pricing. |
| Time-to-resolve (or time-to-action) | P50 and P95 wall-clock time from task receipt to closure (or to action for action agents). | A copilot can be slow and useful; an agent must act on a timer. |

Plus three operational guardrails:

| Guardrail | SLA shape |
|---|---|
| Kill-switch | Time-to-stop ≤ 60 s for Platinum, ≤ 5 min for Gold, ≤ 30 min for Silver. Quarterly drill with log. |
| Audit-log completeness | ≥ 99.9 % for Platinum, ≥ 99.5 % for Gold, ≥ 99 % for Silver. Replay available within 15 min for Platinum, 1 hr for Gold. |
| Intervention SLA | Time-to-human ≤ 60 s for Platinum, ≤ 5 min for Gold, ≤ 15 min for Silver. |

See [ai-agent-sla-class-table](../../profiles-sectors/references/ai-agent-sla-class-table.md) for the full thresholds and credit schedule.

## The Three Out-Clauses

### Upstream Model-Provider Force-Majeure
Named model providers (OpenAI, Anthropic, Google, AWS Bedrock, Azure OpenAI, Mistral, Cohere, sovereign hosted) with named outage definition. When the provider's own status page declares a regional or service-wide outage of the relevant model family for more than X minutes, the corresponding agent SLA is suspended for the affected window, with evidence-link to the provider status page in the monthly statement. The agency commits to multi-provider fall-back where the buyer has accepted the model-routing-policy variation; otherwise the buyer accepts the single-provider exposure.

### Customer-Fault Exclusions
Buyer-supplied bad data feeding the agent (clearly outside the data-quality contract); buyer-changed action catalogue without change order; buyer-bypassed irreversibility gate (e.g. removed a dual-approval step); buyer-paused supervisor queue causing intervention SLA to breach; buyer-side identity outage preventing the agent from authenticating.

### Regulator-Pause
A regulator instruction to pause the agent triggers a joint review. SLA is suspended for the affected window. The agency does not pay credits during a regulator-mandated pause. The buyer retains the right to terminate without penalty if the regulator action is final.

## Credit Formula Patterns

- **Linear** — 1 % credit on monthly fees per 0.1 percentage-point miss. Predictable; easy to model.
- **Stepped** — 10 % at the first threshold; 25 % at the second; 50 % at the floor. Bigger signal at the bad outcomes.
- **Capped** — no more than the class cap (25 / 50 / 100 % of monthly fees) in any month; credits do not stack across metrics beyond the cap.

The default is stepped with a class cap. Linear looks fair but lets large misses get away too cheaply. Capped without stepping rewards just-missing.

## Quality Standards

- Every metric has a definition the buyer would accept and the agency can prove from the audit log.
- Every credit is a formula, not a discretionary number.
- The service-credit cap is named and visible.
- Out-clauses are explicit and evidence-backed.
- The kill-switch SLA, the audit-log completeness SLA, and the intervention SLA are present and numbered.
- The termination right at consecutive misses is named.
- The monthly statement shape is described — the buyer can see what would be reported every month before signature.
- The SLA does not promise an availability number the agent's infrastructure cannot prove; the methodology, the audit-log, the kill-switch, and the model-routing posture support every commitment.

## Domain Risks

- "99.9 % uptime" as the only SLA on an agent — uptime is the floor, not the product.
- Task-success rate without a binary definition per task class.
- Intervention rate stated but not tied to credits — buyer carries the intervention overhead.
- No kill-switch SLA — when something goes wrong, the buyer has no contractual basis to demand a stop time.
- No audit-log completeness SLA — disputes cannot be evidenced.
- Model-provider force-majeure undefined — the first model outage destroys the SLA.
- Credit cap absent or unbounded — margin floor blown.
- Discretionary credits ("we will work with you in good faith") — procurement reads this as no credit.

## Domain Outputs

- **Agent SLA Exhibit** for the MSA / SoW (drop-in from [ai-agent-sla-exhibit-template](../../profiles-sectors/references/ai-agent-sla-exhibit-template.md)).
- **SLA Class Table** populated for this engagement (from [ai-agent-sla-class-table](../../profiles-sectors/references/ai-agent-sla-class-table.md)).
- **Credit Schedule** drafted per metric.
- **Out-Clauses** drafted (force-majeure, customer-fault, regulator-pause).
- **Monthly SLA Statement** template the buyer will receive.
- **Termination-Right** clause.

## Anti-Patterns

- Quoting an unverified commercial term. Fix: trace it to the approved brief or contract record and label any unresolved variable.
- Billing an attempted task as a completed outcome. Fix: define the eligible event, exclusions, reversal window, and evidence source.
- Leaving credits, refunds, or liability uncapped. Fix: state the eligible fee base, cap, trigger, exclusions, and approval owner.
- Updating one exhibit while dependent terms still conflict. Fix: reconcile pricing, SLA, credit, refund, renewal, and liability provisions together.
- Removing a legal placeholder without authority. Fix: retain the marker, name the decision owner, and require qualified review before issue.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| service scope, telemetry definitions, dependencies, and risk appetite | Buyer, proposal owner, approved contract record, or measured operating evidence | Yes | Stop before making a commitment; list the missing evidence and provide only a qualified option set. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| SLA schedule and credit model | Operations, legal, and procurement | Scope, assumptions, exclusions, owners, decision logic, and observable acceptance tests are explicit and traceable to supplied evidence. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| SLA schedule and credit model | Operations, legal, and procurement | Assumptions, measures, authority, exclusions, and acceptance tests are explicit and traceable to the supplied evidence. |

## Capability Contract

Minimum capability is read access to the approved commercial record and calculation support for any stated formula. Drafting authority permits edits only inside the requested proposal or contract working copy. Do not sign, publish, spend, change production configuration, concede liability, or represent legal approval without explicit authority. Legal and tax conclusions require qualified review.

## Degraded Mode

Fallback when tools are unavailable: use the qualified path below.

If source terms, telemetry, calculation tools, or legal review are unavailable, return the narrowest useful marked draft: identify unverified variables, preserve placeholders, show the calculation method where possible, and mark each unavailable check as not assessed. Never convert missing evidence into approval.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Set SLA class and remedy | Choose measurable commitments supported by telemetry, staffing, exclusions, and credit affordability. | Unmeasurable promise or uncapped exposure. |
| Evidence is incomplete or positions conflict | Stop commitment drafting, record the conflict, and request the named owner’s decision. | Invented terms, double recovery, or an unauthorised concession. |
| Evidence and authority are complete | Draft, cross-check dependent exhibits, and retain the calculation or clause trace. | An internally inconsistent commercial package. |

## Workflow

1. Confirm the consumer, authority, controlling commercial record, and required inputs; stop when a baseline or accountable owner is missing.
2. Reproduce relevant calculations and identify conflicts across pricing, SLA, credit, refund, renewal, liability, and scope; stop when a formula cannot be reproduced.
3. Apply the domain method and decision rules within delegated authority, recording assumptions and exclusions.
4. Draft the contracted output and cross-check every dependent exhibit; recover by reconciling the controlling term with its owner and rerunning the calculation.
5. Verify acceptance conditions, evidence trace, legal-review markers, and anti-slop controls; block release until failed checks are corrected.

## Worked Example

The buyer needs 99.5% availability and a 15-minute kill-switch response. Select the supported class, define measurement windows and exclusions, then model the worst credit month.

<!-- dual-compat-end -->

## References

- [ai-agent-sla-class-table](../../profiles-sectors/references/ai-agent-sla-class-table.md) — full Bronze / Silver / Gold / Platinum thresholds and credit schedule.
- [ai-agent-sla-exhibit-template](../../profiles-sectors/references/ai-agent-sla-exhibit-template.md) — drop-in SLA exhibit.
- [ai-agent-credit-and-refund-clauses](../../profiles-sectors/references/ai-agent-credit-and-refund-clauses.md) — credit and refund clauses.
- [ai-agent-dispute-resolution-and-audit-rights](../../profiles-sectors/references/ai-agent-dispute-resolution-and-audit-rights.md) — SLA dispute mechanics and audit rights.
- [ai-agent-sla-financial-services](../../profiles-sectors/references/ai-agent-sla-financial-services.md) — FS variant.
- [ai-agent-sla-public-sector](../../profiles-sectors/references/ai-agent-sla-public-sector.md) — public-sector variant.
- [ai-agent-sla-healthcare](../../profiles-sectors/references/ai-agent-sla-healthcare.md) — healthcare variant.
- [saas-msa-dpa-sla-template-language](../../profiles-sectors/references/saas-msa-dpa-sla-template-language.md) — base SaaS MSA / DPA / SLA.
- [ai-agent-pricing-and-packaging-proposal](../../ai-agent-proposals/ai-agent-pricing-and-packaging-proposal/SKILL.md) — pricing patterns the credits attach to.
- [ai-agent-intervention-credit-and-abort-refund](../ai-agent-intervention-credit-and-abort-refund/SKILL.md) — intervention-credit mechanics.
- [ai-agent-msa-and-sla-addendum-templates](../ai-agent-msa-and-sla-addendum-templates/SKILL.md) — MSA addendum.
- [customer-service-and-maintenance-proposals](../../strategy-positioning/customer-service-and-maintenance-proposals/SKILL.md) — generic SLA frame.
