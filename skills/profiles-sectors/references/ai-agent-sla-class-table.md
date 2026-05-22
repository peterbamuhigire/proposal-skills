# AI-Agent SLA Class Table

Drop-in SLA class table for agentic engagements. Pairs with `../ai-agent-sla-and-credit-schedule/SKILL.md`. Use Bronze for low-stakes pilots, Silver as the commercial default, Gold for regulated verticals, Platinum for mission-critical agents.

## Class Table

| Dimension | Bronze (Entry) | Silver (Standard) | Gold (Regulated) | Platinum (Mission-Critical) |
|---|---|---|---|---|
| Availability of control plane and inference path | 99.0 % monthly | 99.5 % monthly | 99.9 % monthly | 99.95 % monthly |
| Task-success rate (binary, per action catalogue) | ≥ 75 % | ≥ 85 % | ≥ 92 % | ≥ 95 % |
| Intervention rate ceiling | ≤ 25 % | ≤ 15 % | ≤ 10 % | ≤ 5 % |
| Time-to-resolve P95 (resolution agents) | ≤ 24 h | ≤ 4 h | ≤ 1 h | ≤ 15 min |
| Time-to-action P95 (action agents) | ≤ 1 h | ≤ 15 min | ≤ 5 min | ≤ 60 s |
| Kill-switch time-to-stop from authorised command | ≤ 30 min | ≤ 5 min | ≤ 60 s | ≤ 30 s |
| Kill-switch drill cadence | Annual | Semi-annual | Quarterly | Quarterly + on incident |
| Audit-log completeness | ≥ 98 % | ≥ 99 % | ≥ 99.5 % | ≥ 99.9 % |
| Audit-log retention | 3 years | 5 years | 7 years | 10 years or regulator-mandated |
| Replay availability | Next business day | ≤ 4 h | ≤ 1 h | ≤ 15 min |
| Intervention SLA (time-to-human escalation) | ≤ 1 h business hours | ≤ 15 min | ≤ 5 min | ≤ 60 s 24x7 |
| Reporting cadence | Monthly | Monthly | Monthly + quarterly review | Monthly + monthly review |
| Termination right for SLA breach | After 6 consecutive misses | After 4 consecutive misses | After 3 consecutive misses | After 2 consecutive misses |
| Service-credit cap (% of monthly fees) | 10 % | 25 % | 50 % | 100 % |
| Refund triggers active | Force-majeure only | Force-majeure + intervention overshoot 90 days | Full Abort-and-Refund schedule | Full Abort-and-Refund schedule + audit-log breach refund |

## Credit Schedule per Metric (Stepped)

### Availability
| Observed availability | Bronze credit | Silver credit | Gold credit | Platinum credit |
|---|---|---|---|---|
| ≥ class threshold | 0 % | 0 % | 0 % | 0 % |
| 0.5 ppt below | 5 % | 10 % | 15 % | 20 % |
| 1.0 ppt below | 10 % | 20 % | 30 % | 40 % |
| 2.0 ppt below | Cap | Cap | Cap | Cap |

### Task-Success Rate
| Observed task-success | Bronze credit | Silver credit | Gold credit | Platinum credit |
|---|---|---|---|---|
| ≥ class threshold | 0 % | 0 % | 0 % | 0 % |
| 2 ppts below | 3 % | 5 % | 10 % | 15 % |
| 5 ppts below | 8 % | 15 % | 25 % | 35 % |
| 10 ppts below | Cap | Cap | Cap | Cap |

### Intervention Rate (above ceiling)
| Observed intervention above ceiling | Bronze credit | Silver credit | Gold credit | Platinum credit |
|---|---|---|---|---|
| ≤ ceiling | 0 % | 0 % | 0 % | 0 % |
| +2 ppts | 2 % of unit fees | 4 % | 6 % | 10 % |
| +5 ppts | 5 % | 10 % | 15 % | 25 % |
| +10 ppts | 10 % | 25 % | 40 % | 60 % |
| > +10 ppts | Cap | Cap | Cap | Cap |

### Time-to-Resolve / Time-to-Action (P95 above threshold)
| Observed P95 above threshold | Bronze credit | Silver credit | Gold credit | Platinum credit |
|---|---|---|---|---|
| ≤ threshold | 0 % | 0 % | 0 % | 0 % |
| 1.5× threshold | 3 % | 5 % | 10 % | 15 % |
| 2.0× threshold | 8 % | 15 % | 25 % | 35 % |
| ≥ 3.0× threshold | Cap | Cap | Cap | Cap |

### Kill-Switch
A kill-switch breach (time-to-stop above class threshold on any authorised invocation, or a failed drill not remediated within 7 days) triggers a one-time credit of 25 % of monthly fees on Gold and 50 % on Platinum, in addition to other credits, and a joint review.

### Audit-Log Completeness
Audit-log completeness below class threshold for one month triggers a credit equal to 10 % of monthly fees on Silver, 15 % on Gold, 25 % on Platinum, and obligates a remediation plan within 14 days. Two consecutive months below threshold triggers the Audit-Log Breach Refund.

## Aggregate Credit Cap

Credits across all metrics do not exceed the class service-credit cap (% of monthly fees) in any month. Credits do not stack across metrics beyond the cap. The cap is the sole monetary remedy for SLA misses, except where the Abort-and-Refund clause triggers.

## Africa-Context Notes

- For sovereign-AI deployments (Granica, local hosted models) where the model is operated inside the buyer's country, the kill-switch and audit-log SLAs are unchanged; the model-provider force-majeure clause names the sovereign provider explicitly.
- For public-sector engagements, Gold is typically the maximum class on offer; Platinum is reserved for systemically critical agents (border, identity, payments) and requires the public-sector SLA variant.
- For financial-services engagements, Gold is the regulator-aware default; CBK, CBN, SARB, BoU, BNR conduct rules may require additional named accountability per the FS SLA variant.
- Time-to-resolve thresholds in markets with intermittent connectivity should reflect the network reality of the buyer's tenants; relax P95 by one tier where the buyer's last-mile is the binding constraint.
