# Responsible-AI Agent Commitment — Section Template

Drop-in template for the Responsible-AI Agent Commitment subsection of an agentic proposal. Pairs with `ai-agent-risk-and-responsible-ai`. Edit names, jurisdictions, and cadences per engagement.

---

## Responsible-AI Agent Commitment

### Scope

This commitment covers the AI agent(s) and multi-agent system(s) delivered under this engagement. It applies to every action class set out in the Action Catalogue (Annex X), to every Tenant set out in Annex Y, and to every jurisdiction listed in Annex Z. The commitment is signed by the Agent Safety Lead and reviewed quarterly by the Agent Safety Council with annual sign-off by the SteerCo.

### Principles

We commit to seven principles:

1. **Accountability** — every agent action is owned by a named human role on the buyer side. The agent does not bear accountability; it bears authority within bounds.
2. **Transparency** — the action catalogue, the autonomy levels, the oversight model, the sub-processor list, the eval methodology, and the kill-switch architecture are documented and available to the buyer.
3. **Fairness** — the agent's decisions are eval-tested for unfair outcomes across protected and sensitive categories where the data permits.
4. **Safety** — irreversible actions are L1-gated with a named human approver; the agent cannot complete an irreversible action without that approval.
5. **Privacy** — agent memory is scoped per session, per tenant, and per task; cross-tenant state is prohibited; data-residency commitments are honoured.
6. **Human oversight** — every action class has an oversight model (HITL / HOTL / audit) and an intervention SLA.
7. **Contestability** — any affected user, tenant, or regulator can contest an agent action through a named channel; a human is the decision-maker on contested actions; redress is delivered within the SLA.

### Governance Forum — Agent Safety Council

The Agent Safety Council meets monthly during the engagement, quarterly in production:
- Chair: Agent Safety Lead (agency) co-chaired by buyer-side Agent Safety Lead.
- Standing members: Engagement Lead; Buyer Sponsor; Security and Compliance Lead (agency); CISO or DPO (buyer); Customer Success Lead; Human-in-the-loop Designer; Eval Engineer; Tool Engineer.
- Standing agenda: eval report; intervention-rate trend; irreversible-action incidents (target: zero); audit-log completeness; kill-switch drill results; red-team report; sub-processor changes; contestability cases; regulator engagement.
- Decisions: autonomy-level changes per action class; action catalogue amendments; sub-processor approvals; incident classification.

### Accountable Role — Agent Safety Lead

The Agent Safety Lead is a named role accountable for this commitment, with authority to:
- Trigger the kill-switch on any agent class or tenant.
- Suspend an action class pending review.
- Convene an emergency Agent Safety Council meeting within 24 hours.
- Escalate to the SteerCo and the buyer's executive sponsor.

### Human-Final on Irreversibility

Every irreversible action — money out, public statement issued, regulatory filing submitted, ledger posted, account closed, refund or chargeback authorised, transaction settled, contractual commitment made — requires explicit approval by a named human role recorded in the Action Catalogue. The agent cannot complete such an action without that approval recorded in the Audit Log. Value-bound dual approval applies where the action exceeds the threshold set per action class.

### Full Audit Log

Every agent action is logged with:
- Decision and reasoning trace (where the model surface permits).
- Tool call name, parameters, return value.
- Result, including any post-call assertions.
- Human decision (if any), with named approver and timestamp.
- Tenant, agent identity, session, task.

Audit-log completeness SLA: **99 %** measured monthly. Retention: minimum [seven (7)] years or as required by sectoral rule. Access: buyer, internal audit, external auditor, regulator (subject to disclosure controls). Replay capability for forensic review is available.

### Contestability

Any affected user, tenant, or regulator can contest an agent action by:
- Reaching the redress channel published at [URL or contact].
- Receiving acknowledgement within [24 hours].
- Receiving a resolution within [10 business days] or, where the contestation is complex, an interim response and a committed resolution date.
- Receiving the contestation outcome from a named human, with the agent decision overridden where the human concludes overrides are appropriate.

Contested actions and outcomes are logged and reviewed by the Agent Safety Council.

### Transparency-to-Affected-Party

Where the agent communicates externally or takes an action that affects a third party:
- The third party is informed they are interacting with or being acted upon by an AI agent in line with applicable rules (EU AI Act Article 50 where applicable; sectoral disclosure rules; the buyer's own customer-communication policy).
- Outbound communications carry an agent signature with contact for a human.
- Voice agents identify as agents at the start of the call.
- High-stakes actions carry a human-review prompt.

### Kill-Switch Readiness

- Kill-switch architecture has four layers: per-action-class, per-agent, per-tenant, global.
- The authority chain is named in the runbook with after-hours coverage.
- Drill cadence: quarterly minimum. The first drill is in the pilot's Supervised stage; the second in the Agentic stage; subsequent drills quarterly.
- Time-to-stop SLA: 60 seconds for per-action and per-agent; 5 minutes for tenant-wide; 15 minutes for global.
- Post-drill review is required within five business days.

### Eval and Red-Team Discipline

- Golden datasets defined per use case, with adversarial cases.
- Eval thresholds set per action class.
- Eval CI integrated; threshold breach blocks deploy.
- Drift watch with monthly review and alerting.
- Red-team catalogue specific to agents: prompt injection via tool output, scope manipulation, memory poisoning, identity confusion, multi-agent collusion, side-channel leakage.
- Red-team refresh quarterly.

### Incident Classification and Disclosure

- Class 1: Irreversible-action incident — immediate kill-switch consideration; SteerCo within 4 hours; regulator notification within sectoral SLA.
- Class 2: Scope breach — Agent Safety Lead within 4 hours; SteerCo within 24 hours.
- Class 3: Intervention SLA breach cluster — Agent Safety Council within 5 business days.
- Class 4: Near-miss — quarterly safety-council review.

Public communications follow the buyer's communications policy with input from the agency Communications and Security & Compliance leads.

### Sub-Processor Disclosure

The sub-processor list (Annex X) names every model provider and tool-call API the agent uses. Changes to the list are notified to the buyer with [thirty (30)] days' notice or earlier where a regulator requires.

### Sign-Off

- Quarterly review by the Agent Safety Council.
- Annual sign-off by the SteerCo.
- Annual independent review by [internal audit / external assurance provider] from year two.

Signed:
- [Name], Agent Safety Lead (agency)
- [Name], Buyer-side Agent Safety Lead
- [Name], Engagement Lead
- [Name], SteerCo Chair

Date: [DD Month YYYY]
