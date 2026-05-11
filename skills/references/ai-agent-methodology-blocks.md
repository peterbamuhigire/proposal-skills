# AI-Agent Methodology Blocks

Reusable methodology content for the `06-methodology` section of an agentic proposal. Pairs with `ai-agent-methodology`. Use as drop-in blocks; edit to the engagement.

## Block 1 — Agentic Mental Model (paragraph)

> An agent is a system that **plans, calls tools, decides, and acts** within an explicit action catalogue, under an explicit autonomy level, with explicit oversight, with named kill-switch authority, and with full audit. Our methodology engineers the four parts as named disciplines: the planner that reasons about the task; the tool layer that exposes a confined set of actions; the decision layer that judges sufficiency of evidence and decides to act, escalate, or abstain; and the audit layer that records every decision so that the buyer, the buyer's auditor, and the buyer's regulator can reconstruct what the agent did and why.

## Block 2 — Conceptual Approach (paragraph)

> The Action Catalogue is designed before the agent is built; autonomy levels are committed per action class, not per agent; the oversight model and intervention SLA are designed not improvised; kill-switch authority is named with after-hours coverage; audit completeness is a measured discipline with a 99 % SLA; the Responsible-AI Agent Commitment is signed by a named Agent Safety Lead and reviewed quarterly. The agent never approves an irreversible action on its own.

## Block 3 — The Eight Standard Phases (table)

| # | Phase | Purpose | Key deliverables | Gate |
|---|---|---|---|---|
| 1 | Discover and Strategy Gate | Confirm the engagement is genuinely agentic; commit autonomy targets and action catalogue v0 | Discovery Findings; Autonomy Commitment; Action Catalogue v0 | Signed by buyer SteerCo |
| 2 | Action-Catalogue Design | Enumerate, classify reversibility, set rate limits, design identity policy | Action Catalogue v1; Identity-and-Impersonation Policy | Signed |
| 3 | Architecture for Autonomy | Agent loop; oversight queue; kill-switch; audit log; eval and red-team plans; multi-agent orchestration where applicable | Architecture ADR; Eval Plan; Red-Team Plan | ADR signed; plans approved |
| 4 | Build | Build the agent, tool layer, oversight queue, audit log, kill-switch, eval and red-team harness | Working agent at component level; CI green; red-team component-level pass | Kill-switch test pass |
| 5 | Shadow Stage | Agent runs against real traffic; does not act; agreement measured | Agreement-rate report; disagreement-class analysis; abstain report | Buyer signs Stage 2 transition |
| 6 | Supervised Stage | Agent acts on reversible; humans confirm irreversible; intervention SLA measured | Task-success report; intervention curve; oversight queue metrics; kill-switch drill (first) | Buyer signs Stage 3 transition |
| 7 | Agentic Stage | Agent acts on reversible without confirmation; irreversibles HITL | Production-readiness pack; second kill-switch drill; red-team full pass | Production exit decision |
| 8 | Operate | Drift watch, intervention trend, drill cadence, refresh cadence, regulator engagement | Quarterly Safety Council report; quarterly drill log; annual commitment sign-off | Annual SteerCo sign-off |

## Block 4 — Action-Catalogue and Reversibility (subsection)

> Every action the agent can take is enumerated in the Action Catalogue with: the system it acts on, the authority required, the parameter and value bounds, the rate limit per day per tenant, and a reversibility class (Reversible-no-harm / Reversible-with-effort / Irreversible). Irreversible actions are L1-gated — a named human approves before commit. Value-bound dual approval applies above the threshold per action class. The Action Catalogue is signed; amendments require a change order.

## Block 5 — Autonomy and Oversight Model (subsection)

> Autonomy is committed per action class, not per agent. The same agent can be L1 (confirm each action) on irreversible transactions and L3 (supervise) on triage. For each action class the proposal commits: the autonomy level at go-live, the trajectory by month 6, the oversight model (HITL / HOTL / audit), the intervention SLA, the supervisor queue staffing floor, and the escalation tree. The intervention SLA is measured monthly; sustained breach for two weeks triggers Agent Safety Council review.

## Block 6 — Kill-Switch and Drill (subsection)

> The kill-switch has four layers: per-action-class, per-agent, per-tenant, and global. The authority chain is named in the runbook with after-hours coverage. Time-to-stop SLA is 60 seconds for per-action and per-agent, 5 minutes for per-tenant, 15 minutes for global. The first drill is in pilot Stage 2; the second in Stage 3; subsequent drills quarterly. The drill log is available to the buyer's auditor and, where invited, to the buyer's regulator.

## Block 7 — Eval and Red-Team Strategy (subsection)

> Eval is engineered before the agent is built. Golden datasets are sized per use case with adversarial cases (prompt injection direct and via tool output; scope-edge cases; multilingual cases; irreversibility-edge cases). Eval metrics are committed numerically per action class. Eval CI gates deploy on threshold breach. Component-level evaluation runs alongside end-to-end evaluation so a failure in one component does not hide in an end-to-end pass. The agent-specific red-team catalogue runs at component build, at Stage 2, at Stage 3, and quarterly in production.

## Block 8 — Multi-Agent Orchestration (subsection — where applicable)

> The orchestration pattern is named — manager-worker, planner-actor-critic, or swarm — with an architecture ADR. Inter-agent contracts specify input and output schemas, error handling, retry policy, and escalation. A blast-radius limit caps the actions any single agent can take in the chain. An anti-collusion guard runs an independent verifier on high-stakes decisions. Loop detection breaks runaway interactions. The orchestrator log is replay-deterministic for forensic review.

## Block 9 — Operate (subsection)

> After production exit the agency operates the agent fleet on a defined operating model — agency-led, buyer-led, or joint. Operations carries five disciplines: drift watch (eval, performance, cost-per-task); intervention-rate trend; irreversibility-incident counter (target zero); model and prompt refresh cadence; regulator-notification readiness. The Agent Safety Council meets quarterly. The kill-switch drill runs quarterly. The red-team refreshes quarterly. The Responsible-AI Agent Commitment is reviewed annually with SteerCo sign-off.

## Block 10 — Deliverables Summary (table)

| Phase | Deliverable | Binary acceptance criterion |
|---|---|---|
| 1 | Discovery Findings | Buyer SteerCo signs |
| 1 | Action Catalogue v0 | Buyer Action-Catalogue Owner signs |
| 2 | Action Catalogue v1 + Identity Policy | Buyer signs |
| 3 | Architecture ADR + Eval Plan + Red-Team Plan | Buyer CTO + Agent Safety Lead sign |
| 4 | Working agent at component level | Component eval thresholds met; kill-switch test passes |
| 5 | Shadow Stage evidence pack | Agreement rate ≥ X; abstain ≥ Y; zero scope breach |
| 6 | Supervised Stage evidence pack | Task-success ≥ X; intervention ≤ Y; zero unauthorised irreversible; kill-switch drill pass |
| 7 | Production-readiness pack | All Stage 3 thresholds; second drill; red-team full pass; audit-log completeness ≥ 99 % |
| 8 | Quarterly Safety Council report | Council sign-off |
| 8 | Annual Responsible-AI commitment sign-off | SteerCo signs |

## Block 11 — Sample Proposal Paragraph (drop-in)

> The methodology proceeds through eight phases — Discover, Action-Catalogue Design, Architecture for Autonomy, Build, Shadow, Supervised, Agentic, Operate — with gates between each phase that require the buyer's sign-off on a binary evidence pack. Autonomy is committed per action class: the agent operates at L3 on triage and assembly, at L1 (named human approval) on irreversible actions. The kill-switch authority is named with after-hours coverage; drills run quarterly with the log available to the buyer's auditor. The Responsible-AI Agent Commitment is owned by a named Agent Safety Lead and reviewed quarterly by the Agent Safety Council. The agent never approves an irreversible action on its own. The buyer remains accountable to the regulator and the customer.
