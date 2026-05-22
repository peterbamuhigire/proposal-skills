# Vertical AI-Agent — Operations (IT Ops, SRE, Engineering, Coding)

Vertical positioning, named agent use cases, autonomy stance, regulator framing, discriminators, and risk language for AI-agent bids in IT operations, SRE / DevOps, engineering productivity, and coding-agent rollouts. Pairs with `ai-agent-vertical-positioning`.

## Named Agent Use Cases (with autonomy and reversibility)

| Use case | Autonomy at go-live | Reversibility | Notes |
|---|---|---|---|
| Alert triage and incident routing | L3 | Reversible | Routes; never closes the incident |
| Runbook execution on bounded actions | L2 / L3 | Mixed | Restart a service in pre-prod is L3; in prod is L1 |
| Log summary and root-cause assembly | L3 | Reversible | Synthesises; engineer decides |
| Infrastructure-change triage | L2 | Reversible | Proposes; SRE applies via change-control |
| Coding agent — refactor, test generation, dependency update | L2 / L3 | Reversible (in sandbox) | Sandbox by default; pull-request authorship under human review |
| Coding agent — merge to main | **L1** | Irreversible (in repo) | Lead engineer reviews and merges |
| Coding agent — production deployment | **L1** | Irreversible (in prod) | Named approver per change |
| Cost-anomaly triage | L3 | Reversible | Identifies; finance / ops reviews |
| Security alert triage | L2 / L3 | Reversible | Routes and contextualises; security engineer decides |

## Regulator Stance

- Data-protection regulators (general).
- Sectoral where the operations are inside a regulated service (financial services, healthcare, public sector).
- Internal governance — change-control board, SOX where applicable, ISO 27001 controls, SOC 2 controls.

Vertical-specific exposure:
- **Production-change risk** — autonomous changes to production cause incidents.
- **Secret leakage** — coding agents can leak secrets via tool output or generated code.
- **Dependency safety** — coding agents can introduce supply-chain risk.
- **Regression risk** — code changes can introduce regressions a fast pipeline misses.

## Discriminators for Operations Bids

1. **Sandbox by default** — agents act in pre-prod / sandbox; production touches require human approval.
2. **Deterministic replay** — the agent's actions are replay-deterministic for incident review.
3. **Merge-gate human review** — coding agents author pull requests; engineers merge.
4. **Rollback by default** — every agent change has a rollback path; automatic where possible.
5. **Observability of the agent itself** — dashboards on agent decisions, tool calls, cost, error rate.
6. **Coding-agent specific eval** — test pass, regression, dependency safety, secret leak, code-quality score.
7. **Sub-processor allowlist for tool calls** — every tool the agent can call is approved.

## Risk Framing — Operations-Specific Language

- "Production blast radius" (not "AI quality").
- "Rollback by default" (not "we will be careful").
- "Sandbox-first" (not "we will test in production").
- "Dependency safety" — supply-chain controls.
- "Secret leakage" — explicit risk class.
- "Regression" — guarded by test pass.

## Sample Vertical Paragraph for Executive Summary

> Our operations agent practice keeps production safe by design. Agents propose, draft, triage, assemble; engineers review, merge, and deploy. Coding agents author pull requests in a sandbox; the merge gate is human. Production changes require a named approver; the rollback path is automatic where the system supports it. Agent decisions, tool calls, costs, and error rates are observable in a dashboard alongside the agent's actions. Coding-agent specific evaluation covers test pass, regression, dependency safety, and secret leakage so the agent's contribution to the codebase is auditable and safe.

## Pricing Pattern Notes

- Pattern C (per-step) suits operations agents.
- Pattern D (per-agent) suits coding-agent fleets where engineers "rent" agent time.
- Pattern E (hybrid) for enterprise rollouts.

## Coding-Agent Specific Eval Categories

- Test pass on changed code.
- Regression on broader test suite.
- Dependency-safety check (SCA, licence, vulnerability).
- Secret-scan on diffs.
- Code-quality score (linter, complexity, duplication).
- Review-acceptance rate (engineers accepting agent PRs without major rework).

## Cross-References

- `ai-agent-risk-register-for-proposals.md` — R-AG-OPS-01 (production blast radius); R-AG-OPS-02 (secret leakage; dependency safety).
- `ai-agent-responsible-ai-commitment.md`
- `ai-agent-trust-and-compliance-template.md`
