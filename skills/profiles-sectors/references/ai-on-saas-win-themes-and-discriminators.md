# AI-on-SaaS Win Themes and Discriminators

Win-theme library for AI-on-SaaS bids — themes that an evaluator can score, that competitors cannot trivially claim, and that the engagement can actually deliver. Pairs with `saas-win-themes-and-discriminators.md` and `proposal-strategy-and-persuasion.md`.

## The Six Discriminators That Survive Evaluator Scrutiny

### Discriminator 1 — Eval Before Models, Not After
**Claim**: We engineer the evaluation before we choose the model.
**Evidence**: Phase 1 deliverable is a golden-set spec and a threshold table. Phase 3 deliverable is eval results across at least two models. CI gates deploys on threshold.
**Why it wins**: Competitors lead with "we use [model X]." We lead with "we measure first." This is the single biggest discriminator for technical evaluators.

### Discriminator 2 — Three Planes, Not Two
**Claim**: AI is a discipline, with its own plane alongside the control plane and application plane.
**Evidence**: AI plane named in methodology (model gateway, model registry, eval harness, red-team harness, drift watch). AI roles named in the roster (AI Safety, Eval, MLOps, Prompt, RAG, Data-for-AI). AI workstreams gated independently of the SaaS build.
**Why it wins**: Competitors collapse AI into the application plane and ship eval as an afterthought.

### Discriminator 3 — Hallucination as an Engineered Ceiling, Not a Disclaimer
**Claim**: We commit to a numeric hallucination ceiling, with abstain logic in the system.
**Evidence**: Hallucination SLO in the SoW. Abstain-correctness ≥ 0.95 as an exit criterion. Drift watch with weekly alerting. Rollback runbook tested in Phase 4.
**Why it wins**: Most vendors mention disclaimers; few commit to a measured ceiling. CISOs and regulators reward the commitment.

### Discriminator 4 — Model-Agnostic from Day One
**Claim**: The production architecture is model-agnostic via a gateway with at least two providers and a fallback.
**Evidence**: Gateway architecture in Phase 2. Two-model eval in Phase 3. Fallback routing tested in Phase 5. Open-weight option for sovereign tenants.
**Why it wins**: Procurement teams have seen vendors trapped by model-provider price-shocks and bans. The gateway addresses the fear directly.

### Discriminator 5 — Responsible-AI as an Engineered Commitment, Not a Principles List
**Claim**: Our Responsible-AI commitment is signed by a named accountable role, with named controls, named frequencies, and a quarterly board-level report.
**Evidence**: Commitment section in the proposal. AI Governance Forum cadence. Quarterly Responsible-AI report. Annual board-level declaration. Redress mechanism with SLA.
**Why it wins**: Evaluators have read many Responsible-AI statements; few are signed commitments with named owners. This wins ethics and DPO evaluators.

### Discriminator 6 — Per-Tenant AI Cost Attribution from Day One
**Claim**: AI cost is attributed per tenant, per call, per feature — not as a generic cloud bill.
**Evidence**: Telemetry from Phase 2. Cost-per-call SLO. Per-tenant dashboards. Quarterly tenant-cost-attribution review.
**Why it wins**: CFOs reward attribution. Vendors who ship without it cannot defend their pricing under buyer scrutiny.

## Sample Win-Theme Paragraphs (Drop-In)

### Win-Theme Paragraph A — Eval Discipline
> Our approach to AI quality begins with measurement, not models. In the first three weeks of the engagement we assemble the golden dataset with your subject-matter experts, agree the numeric thresholds at the SteerCo, integrate the eval into CI so that a deploy below threshold does not ship, and stand up the drift watch in production. Only then do we select models — evaluated against the same golden set, scored, and gated. The discipline is unglamorous; it is also the difference between an AI feature that demos well and one that runs.

### Win-Theme Paragraph B — Three Planes
> A SaaS implementation has a control plane and an application plane. An AI-on-SaaS engagement has a third — the AI plane, comprising the model gateway, the model registry, the per-tenant RAG indexes, the eval harness, the red-team harness, and the drift watch. We name this plane explicitly because the failure modes of an AI feature are different from the failure modes of a workflow — they require their own discipline, their own roles, their own gates, and their own reviews. Naming the AI plane is what distinguishes a credible AI-on-SaaS methodology from "we will add AI to the SaaS."

### Win-Theme Paragraph C — Responsible-AI Commitment
> Our Responsible-AI commitment is engineered, not aspirational. A named AI Safety Lead chairs the AI Governance Forum with your nominated AI Safety Sponsor. Quarterly Responsible-AI reports are signed and retained. A redress mechanism is published with a one-business-day first-response SLA. Sub-processor changes are notified at least thirty days in advance. The commitment is auditable on request and the controls are connected to the methodology, the risk register, and the trust portal. We do not write Responsible-AI as a paragraph; we operate it as an obligation.

## Discriminator Selection Per Bid

Select two to three discriminators per bid, matched to the buyer's evaluators and the competitive set:

| Evaluator profile | Lead with |
|---|---|
| CTO / Solution Architect | Discriminators 1, 2, 4 (eval, three planes, model-agnostic) |
| CISO / DPO | Discriminators 3, 5 (hallucination ceiling, Responsible-AI commitment) |
| CFO / Procurement | Discriminators 4, 6 (model-agnostic, per-tenant cost attribution) |
| Regulator / Compliance | Discriminators 3, 5 (ceiling, commitment) |
| Sponsor / Business Owner | Discriminator 5 + outcome paragraph (commitment + outcome) |

## Anti-Patterns in Win-Theme Writing

- Win themes that any competitor could claim ("we use the best AI").
- Discriminators with no evidence anchored in the methodology.
- Lists of features dressed up as discriminators.
- Themes that evaluators cannot score.

## Cross-References

- `proposal-strategy-and-persuasion.md` — discriminator selection logic.
- `saas-win-themes-and-discriminators.md` — base SaaS themes.
- `ai-on-saas-methodology-blocks.md` — evidence anchors.
- `ai-on-saas-responsible-ai-commitment.md` — commitment that backs theme C.
