# AI-Agent Risk Register for Proposals

Twelve-entry agent risk register, drop-in ready for the Risk Analysis section of an agentic proposal. Pairs with `ai-agent-risk-and-responsible-ai`. Likelihood / impact bands are illustrative and should be re-scored per engagement.

## Risk Register Table

| ID | Risk | Description | Likelihood | Impact | Trigger | Mitigation | Owner | Escalation | Residual |
|---|---|---|---|---|---|---|---|---|---|
| R-AG-01 | Autonomy-action incident | Agent acts wrongly inside its autonomy level | Medium | High | Eval drop > threshold; user complaint cluster; sampled audit finding | Eval thresholds in CI; intervention SLO; drift watch; prompt regression; rollback; refresh cadence | Agent Safety Lead | SteerCo within 24 h on cluster | Low |
| R-AG-02 | Irreversibility incident | Agent takes an action that cannot be undone | Low–Med | Very High | Reversibility class misjudged; bypass of human approval; race condition | Reversibility classification on every action; L1 gating on irreversibles; named approver; value-bound dual approval; transaction confirmation token; dry-run pattern | Agent Safety Lead | SteerCo immediately; regulator per runbook | Very Low |
| R-AG-03 | Accountability dispute | Regulator, court, or counterparty pursues accountability | Medium | High | Customer complaint; regulator inquiry; counterparty claim | Action audit log to regulator-grade; contractual liability allocation; professional indemnity / E&O; redress mechanism with SLA | Security and Compliance Lead | General Counsel; SteerCo | Low |
| R-AG-04 | Scope creep | Agent's effective scope expands beyond catalogue | Medium–High | Medium | New tool added without change order; emergent action through chained prompts; buyer adds use case | Action Catalogue gate with sign-off; change-control clause in MSA; monthly catalogue review; anomalous-action alerting | Tool Engineer / Agent Architect | SteerCo monthly | Low |
| R-AG-05 | Multi-agent collusion / failure cascade | Agents in a system reinforce each other's errors or get stuck in loops | Low (single-agent) / Medium (multi) | High | Loop detection alarm; orchestrator timeout; disagreement-cluster between agents | Orchestrator-level governance; blast-radius limit; loop detection; replay determinism; anti-collusion guard; component-level eval | Multi-Agent Orchestrator Engineer | Agent Safety Lead | Low |
| R-AG-06 | Prompt injection via tool output | External system returns content that injects instructions | Medium | High | Anomalous tool-output content; sudden behaviour change after tool call | Output filtering at tool boundary; system-prompt hardening with capability minimisation; content provenance; red-team against tool-output injection quarterly | Agent Safety Lead | Security and Compliance Lead | Low |
| R-AG-07 | Memory poisoning | Persistent memory corrupted, biasing future decisions | Low–Med | Medium–High | Memory-write anomaly; reasoning drift over time; user-targeted injection | Memory scoping per session / tenant / task; memory-write review; periodic memory audit; memory reset cadence; bounded memory size | Agent Safety Lead | Agent Architect | Low |
| R-AG-08 | Regulator action on agentic system | Regulator suspends, requires conformity assessment, imposes ban | Low–Med | Very High | Inquiry; sectoral notice; market guidance change | Kill-switch architecture; conformity readiness; sovereign-AI option; jurisdictional fallback; regulator-notification runbook; quarterly regulator scan | Security and Compliance Lead | SteerCo; CEO | Low–Med |
| R-AG-09 | Kill-switch failure | Kill-switch fails in drill or in incident | Low | Very High | Drill failure; partial stop; authority chain unreachable | Multi-layer kill-switch (per-action, per-agent, per-tenant, global); independent authority chain with after-hours coverage; quarterly drill; post-drill incident review | Agent Ops Lead | Agent Safety Lead immediately | Very Low |
| R-AG-10 | Identity / impersonation breach | Agent communicates externally without proper disclosure | Low–Med | Medium | Anomalous outbound; complaint from affected party | Identity-and-impersonation policy; signature injection on every external communication; automated disclosure; regulator-aligned transparency check in CI | Agent Architect | Security and Compliance Lead | Low |
| R-AG-11 | Escalation overload | Intervention rate exceeds supervisor queue capacity | Medium | Medium–High | Queue depth alarm; SLA breach trend; supervisor CSAT drop | Intervention SLO; queue capacity floor; overflow plan; autonomy gating that backs off when queue saturated; supervisor retraining curriculum | Human-in-the-loop Designer | Customer Success Lead; SteerCo | Low |
| R-AG-12 | Legacy-system damage | Agent calls a tool that mutates a system in an unintended way | Low | High | Post-call assertion failure; downstream system alarm; rollback triggered | Tool-call allowlist with parameter bounds; value bounds; transaction wrapper; dry-run; post-call assertion; automatic rollback; sandbox by default | Tool Engineer | Agent Architect | Very Low |

## How to Use This Register

1. Drop the table (or a tailored subset) into the Risk Analysis section of the proposal.
2. Re-score likelihood and impact per engagement.
3. Anchor every mitigation in a methodology phase or deliverable.
4. Cross-reference with the Responsible-AI Agent Commitment so the auditor sees a coherent story.
5. Add engagement-specific entries (sectoral, jurisdictional, tenant-specific) below the standard twelve.

## Engagement-Specific Add-On Entries (examples)

- **R-AG-FS-01** — Sanctions / watchlist false negative — recall failure on agent triage. Mitigation: recall-prioritised eval; HITL strict on disposition; daily watchlist freshness SLA; quarterly false-negative drill.
- **R-AG-HEALTH-01** — Clinical-scope drift — agent providing advice beyond the admin scope. Mitigation: action catalogue with explicit non-clinical scope; system-prompt enforcement; quarterly scope audit; immediate kill-switch on detected drift.
- **R-AG-LEGAL-01** — Citation hallucination — agent cites a case that does not exist. Mitigation: citation-grounded outputs with verifier; lawyer-final on every filing and advice; quarterly hallucination audit on citations.
- **R-AG-PUB-01** — Administrative-law fairness — agent recommendation embeds bias affecting citizen rights. Mitigation: fairness eval; HITL strict; published action catalogue; contestability channel; regulator-observable drill.

## Residual-Risk Sign-Off

The Responsible-AI Agent Commitment lists residual risks and the Agent Safety Lead signs off annually. The SteerCo is informed of any residual risk re-classified upward in a quarter.
