# AI-Agent Change Management Playbook

Full playbook for engineering trust, adoption, and acceptance of AI agents. Pairs with `ai-agent-change-management-and-adoption`.

## Step 1 — Stakeholder Mapping for Agentic Change

Map five constituencies per agent:

1. **Affected internal users** — the people whose work the agent changes. Augment, redeploy, or retrain — name the framing per role.
2. **Supervisors** — the people who oversee the agent. New role: doer → supervisor / quality / exception handler. Funded retraining required.
3. **Customers / citizens / counterparties** — the affected external parties. Disclosure UX, contestability, redress.
4. **Unions / works-councils / staff associations** — consultation cadence and evidence pack.
5. **Regulator** — transparency-to-affected-party; quarterly engagement where appropriate.

## Step 2 — Augment / Redeploy / Retrain Framing

For each affected role, commit a framing publicly and internally:

- **Augment** — role remains; the agent removes routine load. Productivity expectation named.
- **Redeploy** — role changes; doer becomes supervisor / quality / exception. Funded retraining; new authority defined.
- **Retrain** — role is displaced; the human moves to a different role. Funded retraining; transition timing committed.

Vague "AI will augment our workforce" loses union trust and adoption.

## Step 3 — Trust Staging with Named Evidence

| Stage | Agent role | Human role | Communication | Evidence shown |
|---|---|---|---|---|
| Shadow | Agent proposes; does not act | Human acts; reviewer compares | "The agent is learning; you remain the decision-maker." | Agreement rate; disagreement classes; abstain report |
| Confirm | Agent acts on the human's confirmation | Human approves every action | "The agent does the keystrokes; you decide." | Confirmation latency; override rate |
| Supervised | Agent acts on reversible; humans confirm irreversible | Human runs the oversight queue | "The agent handles the routine; you handle the exception." | Intervention rate; irreversibility incidents (zero); supervisor CSAT |
| Agentic | Agent acts on reversible without confirmation; irreversibles HITL | Human supervises queue and audits sample | "The agent handles the work end-to-end; you supervise the queue." | Task-success; intervention at ceiling; contestability cases; queue headroom |

Move stage only when binary evidence is met. Communications follow the evidence, not the other way around.

## Step 4 — Supervisor Retraining Curriculum

Funded in the financial proposal. Six modules over four to eight weeks:

1. **Reading agent reasoning** — what the agent thought it was doing; how to spot drift.
2. **Judging abstain** — when to trust the agent's abstain; when to override.
3. **Intervening fast** — the intervention SLA; the queue tools; the escalation tree.
4. **Using contestability** — how to triage a contested action; when to override; how to record.
5. **Reading the audit log** — how to reconstruct an agent decision; how to support an internal audit.
6. **Communicating with affected parties** — when to step in; when to disclose; how to redress.

Certification: each supervisor passes a practical exercise before independent oversight.

## Step 5 — Union / Works-Council / Staff-Association Communications

Where consultation is required:

- Establish cadence in advance (monthly during build; quarterly in production).
- Evidence pack: action catalogue; autonomy commitment; oversight model; supervisor retraining curriculum; redeployment plan; redress mechanism.
- Named consultation owner on the buyer side; the agency supports.
- Document outcomes; revise where the council raises substantive issues.

## Step 6 — External Communications and the Agent-on-Your-Behalf Disclosure UX

External communications follow a designed pattern:

- Every outbound message identifies the agent (e.g. "This response was prepared by [Agent Name], an AI agent operating on behalf of [Buyer]. A human is available — reply with HUMAN or use [link].").
- Voice agents identify at the start of the call.
- Jurisdictional disclosure rules applied (EU AI Act Article 50 where applicable; sectoral rules; the buyer's customer-communication policy).
- High-stakes actions carry a one-click route to a human.
- Contestability link always present.

The buyer's Communications and Compliance leads review the disclosure UX before launch. Adoption is harmed by hidden agents; trust is built by transparent ones.

## Step 7 — Adoption Metrics Dashboard

Standard metrics:

| Metric | Type | Floor / ceiling |
|---|---|---|
| Intervention rate | Internal | At or below ceiling from pricing model |
| Override rate | Internal | Trend metric; spikes investigated |
| Abstain-correctness | Internal | ≥ 0.95 on should-abstain subset |
| Supervisor CSAT | Internal | ≥ 4.0 / 5 to sustain adoption |
| Supervisor queue headroom | Internal | ≥ 20 % to absorb spikes |
| Contestability case load | Internal + external | Trend metric |
| External satisfaction | External | Sectoral benchmark |
| Complaint rate attributable to agent | External | Below incumbent baseline |
| Redress SLA performance | External | Sectoral benchmark |
| Transparency-disclosure presence | External | 100 % of external communications carry disclosure |

## Step 8 — Quarterly Adoption Review

- Agent Safety Council and Customer Success review:
  - Trust staging position per agent and per use case.
  - Adoption metrics trend.
  - Supervisor capacity and morale.
  - External satisfaction and complaint trend.
  - Action catalogue stability.
- Outcomes:
  - Autonomy-level changes (per action class).
  - Supervisor curriculum updates.
  - External-disclosure UX updates.
  - Action catalogue change orders.

## Common Failure Modes and the Fixes

| Failure | Cause | Fix |
|---|---|---|
| Agentic-stage abandoned; system falls back to supervised | Intervention rate stays high; supervisors burn out | Diagnose eval drift or prompt regression; pause and refresh; staffing floor for queue |
| Supervisor team rebels | Renamed to "supervisor" without retraining or new authority | Re-launch with funded curriculum; define authority; pay banding adjusted where applicable |
| Customer / citizen complaints surge | Hidden agent disclosure; no contestability | Disclose; publish contestability channel; train customer-service team on redress |
| Union escalation | No consultation evidence pack | Pause and consult; provide pack; revise framing |
| Regulator inquiry | Transparency or accountability gap | Pause; deliver audit-log access; produce Responsible-AI commitment; commit drill cadence |
| Adoption stalls | Trust staging skipped — agentic from day one | Reset to supervised; re-stage; communicate honestly |

## Communication Templates (illustrative)

### To affected staff at announcement (augment framing)
> Over the next six months we are deploying an AI agent that will handle the most routine 60 % of customer-support tickets. Your role remains. The agent does the routine; you do the work that requires judgement. We are funding a supervisor curriculum and adjusting your queue to focus on the cases that benefit most from your attention.

### To affected staff at announcement (redeploy framing)
> Over the next six months we are deploying an AI agent for first-line claims triage. Your role changes. You move from triaging claims to supervising the agent and handling the cases the agent escalates. We are funding a supervisor curriculum; your authority is named in the new operating model; we will sit with you through the transition.

### To unions / works-council
> We are proposing to deploy an AI agent in [workflow]. The action catalogue, autonomy commitment, oversight model, supervisor retraining curriculum, and redeployment plan are attached. We commit to monthly consultation through the build, quarterly thereafter. We invite the council to review and to raise substantive issues that we will address before launch.

### To customers (disclosure)
> This response was prepared by [Agent Name], an AI agent operating on behalf of [Buyer]. A human is available; reply with HUMAN or use [link]. You can contest any action taken on your account through [contestability link]; we acknowledge within 24 hours and respond within 10 business days.
