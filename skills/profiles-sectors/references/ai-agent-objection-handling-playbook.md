# AI-Agent Objection Handling Playbook

Drop-in replies and evidence for agent-specific objections. Pairs with `saas-objection-handling-and-competitive-displacement`.

## The Top Twelve Agentic Objections

### 1. "We are not comfortable with autonomy. Why should we let AI act on its own?"

- **Acknowledge** — the concern is correct; autonomy without oversight is the failure mode of every published agentic incident.
- **Reply** — autonomy is committed per action class, not per agent; irreversibles remain HITL; the agent never approves money out or a regulatory filing on its own; the kill-switch authority is named with after-hours coverage; quarterly drills are mandatory.
- **Evidence** — autonomy commitment matrix; kill-switch drill log; Responsible-AI Agent Commitment with named Agent Safety Lead.

### 2. "If the agent does the work, what happens to our staff?"

- **Acknowledge** — agents change jobs; pretending otherwise loses trust.
- **Reply** — we commit a framing per role: augment, redeploy, or retrain. The supervisor retraining curriculum is funded in the engagement. Redeployment timing is in the change plan. We do not promise "no impact" when there is impact.
- **Evidence** — Augment-Redeploy-Retrain Communications Brief; funded retraining curriculum; redeployment plan; union consultation evidence (where applicable).

### 3. "What if the agent does something irreversible and wrong?"

- **Acknowledge** — the worst-case is real; we mitigate by making it impossible by design.
- **Reply** — irreversible actions are L1-gated; a named human approves before commit. Value-bound dual approval applies above the threshold. The action catalogue is published and signed. Anomalous-action alerting catches drift. Kill-switch fires per-action or per-agent in 60 seconds. PI / E&O cover is in place.
- **Evidence** — reversibility classification in the action catalogue; kill-switch architecture; incident classification and runbook; insurance certificate.

### 4. "Who is liable if the agent harms a customer?"

- **Acknowledge** — accountability is the question every buyer's general counsel will ask.
- **Reply** — the buyer remains accountable to the regulator and the customer (this is the legal position in our markets and the agency cannot transfer it). The agency carries delivery liability per the MSA. PI / E&O covers delivery failures. The audit log supports any forensic review. The contestability channel and redress SLA address the customer side. We do not promise to transfer regulatory liability; we promise the discipline and evidence that supports the buyer's accountability.
- **Evidence** — MSA liability allocation; PI / E&O certificate; audit-log SLA; redress mechanism.

### 5. "Our regulator has not approved agents."

- **Acknowledge** — regulator stance is fluid and the right concern.
- **Reply** — the methodology is regulator-ready: action audit log, irreversibility gating, intervention SLO, kill-switch drill, Responsible-AI agent commitment, transparency-to-affected-party. Sovereign-AI option is available where the regulator prefers on-prem. We engage the regulator quarterly. Where the regulator is not yet ready for L3+ autonomy, we operate at L1 / L2 and re-stage as the regulator's guidance matures.
- **Evidence** — regulator engagement plan; sovereign-AI architecture; compliance map; quarterly regulator scan output.

### 6. "We tried an agent vendor before. It demoed well and failed in production."

- **Acknowledge** — extremely common; we have inherited several such failures.
- **Reply** — we stage Shadow → Supervised → Agentic with binary evidence at each gate. Production exit requires all of: golden-set thresholds met; shadow-traffic thresholds met; supervised intervention rate within ceiling; zero irreversibility incidents; kill-switch drill verified; red-team pass; audit-log completeness verified. Partial pass is a pilot extension, not a production exit. We carry abort fees if the pilot fails.
- **Evidence** — POC scoping template; success-threshold table; abort-conditions; previous pilot evidence packs from references.

### 7. "Will the agent be safe against prompt injection?"

- **Acknowledge** — prompt injection via tool output is the most under-addressed agent risk.
- **Reply** — the red-team catalogue specifically tests prompt injection direct and indirect (via tool output), scope manipulation, memory poisoning, identity confusion, multi-agent collusion. Output filtering at the tool boundary; system-prompt hardening with capability minimisation; content provenance; quarterly red-team. Component-level evaluation alongside end-to-end.
- **Evidence** — red-team catalogue; quarterly scorecard; remediation cadence.

### 8. "What is the supervisor's role really? Are we just renaming jobs?"

- **Acknowledge** — the most common reason agent programmes fail in adoption.
- **Reply** — supervisor is not a renamed doer. The supervisor reads agent reasoning, judges abstain, intervenes fast, uses contestability, reads the audit log. We deliver a funded six-module curriculum. The supervisor's new authority is named in the operating model. Where pay banding requires adjustment, that is in scope of change management.
- **Evidence** — supervisor curriculum specification; new operating model; HR sign-off (buyer-side).

### 9. "We do not want the agent to pretend to be a human."

- **Acknowledge** — correct stance; hidden agents lose customer trust and breach EU AI Act Article 50 and similar.
- **Reply** — every external communication discloses the agent in line with applicable rules. Voice agents identify at the start of the call. The contestability link is always present. High-stakes actions carry a route to a human. We will not deploy hidden agents.
- **Evidence** — disclosure UX specification; sample outbound communications; regulator-mapping table.

### 10. "Costs are unpredictable. The agent makes many model calls per task."

- **Acknowledge** — fair-use and model-cost pass-through must be in the contract.
- **Reply** — fair-use clause with per-tenant action ceiling; anomalous-action ceiling; step budget per task; vendor cost pass-through with index, cap, and margin floor; FX clause where applicable. Pricing pattern matched to volume profile.
- **Evidence** — pricing pattern decision; fair-use clause; vendor cost pass-through clause; worked examples at P50 / P90 / P99.

### 11. "What happens if the agent gets stuck in a loop or fights another agent?"

- **Acknowledge** — multi-agent failure cascades are a documented agentic failure mode.
- **Reply** — orchestrator-level governance; blast-radius limit per agent; loop detection and break; anti-collusion guard with independent verifier on high-stakes; replay-deterministic orchestrator log.
- **Evidence** — multi-agent governance subsection; orchestration ADR; component-level eval.

### 12. "How do we know the agent is not getting worse over time?"

- **Acknowledge** — drift is the production failure mode for agents.
- **Reply** — drift watch in production on task-success, intervention rate, abstain-correctness, irreversibility incidents, cost-per-task. Eval refresh monthly during engagement, quarterly in production. Red-team refresh quarterly. Prompts and models refreshed on a stated cadence with rollback.
- **Evidence** — Operate phase deliverables; drift watch dashboards; refresh cadence schedule.

## How to Use This Playbook

- Match the buyer's objection to a numbered entry and choose the reply pattern.
- Cite the evidence reference; do not improvise.
- Where the buyer's variant of the objection is sharper, escalate to a deeper artefact (the methodology, the risk register, the responsible-AI commitment).
- Avoid two failure modes: brushing off the objection ("trust us"); and over-promising ("we will be perfectly safe").
