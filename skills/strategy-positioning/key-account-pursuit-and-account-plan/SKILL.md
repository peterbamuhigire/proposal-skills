---
name: key-account-pursuit-and-account-plan
description: Use when selecting, pursuing, or growing a strategic key account through an account plan, GRASP stakeholder map, relationship map, Account Cube expansion, value co-creation, executive sponsor, or strategic-account negotiation; use sales-discovery-and-objection-handling for a single bid's discovery.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Key-Account Pursuit and Account Plan
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Plan and run the pursuit or growth of a strategically important client over several proposals, not one bid: decide whether the account deserves key-account investment, map the people who decide, set a relationship target, design value the client can measure, and govern the account with a named sponsor and a one-page plan.

<!-- dual-compat-start -->

## Use When

- Use when deciding which prospects or existing clients deserve key-account status, pursuit investment or a managed exit.
- Use when writing or refreshing an account plan for a bank, telco, ministry, development partner, conglomerate or other strategic client.
- Use when mapping a buying group with GRASP, planning multi-threaded relationships, or appointing and briefing an executive sponsor.
- Use when planning expansion inside an existing client (Account Cube), value co-creation, quarterly value reviews or a strategic-account renegotiation.
- Use when pursuing a small, knowable target universe (licensed banks, insurers, SACCOs above a threshold, private hospitals) as a named-account programme.

## Do Not Use When

- Use `sales-discovery-and-objection-handling` for discovery, qualification and objections on one opportunity or bid.
- Use `premium-pricing-and-value-defense` for the fee structure and price defence of a single proposal; this skill links to its strategic-account negotiation reference.
- Use `saas-mutual-action-planning-and-close-plans` for a close plan from selection to go-live on one SaaS deal.
- Use `stakeholder-engagement` when the deliverable is a stakeholder-engagement plan for the client's own programme, not our relationship with the client.
- Stop when public-procurement rules restrict pre-tender contact with the buyer; relationship activity must then follow the procurement's communication rules.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Account history: revenue, margin, projects, proposals won and lost | Firm's CRM, finance records, proposal archive | Yes for existing clients | Mark financial fields `not assessed`; do not estimate revenue from memory. |
| Client strategy sources: annual report, strategic plan, regulator filings, public statements | Client, public record, Digital Research Engine | Yes | Record the gap and limit the plan to the "grand strategy" hypothesis. |
| Stakeholder evidence: names, roles, meetings, relationship notes | Account team, meeting records | Yes | Mark GRASP cells unknown; never invent a stakeholder's view. |
| Procurement and conflict-of-interest constraints | Procurement framework (`sectors`), client policy | Conditional | Treat all contact as restricted until the rule is confirmed. |
| Proposer profile | `profiles` skill | Yes for client-facing text | Stop client-facing drafting until one profile is loaded. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Account selection decision (strategic / star / status / streamline) with rationale | Firm leadership | Each account is scored on potential and strength with evidence and a review date. |
| One-page account plan | Account lead, sponsor, delivery team | All twelve plan sections are filled or marked `not assessed`; every objective is specific, measurable and dated. |
| GRASP stakeholder map and multi-threading check | Account team | Every buying-group member has goal, role, appeal, state and power; single-threaded levels are flagged. |
| Value hypotheses and value-tracking agenda | Client executive and account lead | Each hypothesis names a baseline, a measurement method and the client's own metric. |
| Sponsor brief and negotiation plan (where relevant) | Executive sponsor | Roles, hours, talking points, concessions and walk-away positions are written before the meeting. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Account evidence register (sources, dates, owners) | Reviewer | Every figure and stakeholder note is traceable to a record or marked as an assumption. |
| Decision log (selection, relationship target, sponsor, concessions) | Firm leadership | Decisions carry date, owner, rationale and review date. |

## Capability Contract

Read and search access to the account record and client sources is required. Drafting the plan and briefs is permitted when the task authorises it. Contacting the client, sending messages, committing discounts, signing agreements or sharing client data outside the firm requires explicit human authority. Personal data about client staff is held only for the account relationship and handled under the applicable data-protection law (Uganda DPPA 2019 and Regulations 2021, claim PL-01; Kenya DPA 2019, claim PL-02); verify other jurisdictions before storing it.

## Degraded Mode

When client strategy sources, stakeholder evidence or financial history are unavailable, use the fallback of a hypothesis-grade plan: label each section `hypothesis` or `not assessed`, list the evidence needed, and set a discovery action with an owner and date. Never present an unverified stakeholder view, revenue figure or client strategy as fact.

## Decision Rules

| Condition or choice | Action | Failure or risk avoided |
|---|---|---|
| Account has high profit-growth potential and our position is strong | Classify **strategic**: senior lead, joint annual plan, sponsor, co-created value | Under-investing in the accounts that matter most |
| High potential, weak position | Classify **star**: time-boxed pursuit budget and entry proposition | Spending strategic effort without a route in |
| Strong position, limited growth | Classify **status**: delivery excellence and margin protection | Over-serving a mature account |
| Low potential, weak position | Classify **streamline**: productised, low-touch service or managed exit | Cost-to-serve eroding margin |
| One stakeholder or one level holds the whole relationship | Build a multi-threading plan across levels and functions | Losing the account when one person moves |
| Client stakeholders disagree on priorities | Facilitate their convergence (priority-allocation exercise) before proposing | Designing for one faction and losing the others |
| A value claim has no baseline | Agree the baseline with the client's finance or operations team first | Unprovable value and weak renewal case |
| A key account exceeds a concentration threshold the firm has set | Record dependency risk and a diversification action | Vulnerable-supplier position |
| Public procurement rules restrict contact | Follow the tender communication channel only | Disqualification or conflict-of-interest finding |

## Workflow

1. **Route and confirm authority.** Confirm this is multi-proposal account work, the proposer profile, and any procurement contact restrictions. Stop if restrictions are unknown.
2. **Select.** Score the account on profit-growth potential and our strength; add strategic importance (reference value, market access), willingness to innovate and relationship strength. Classify strategic, star, status or streamline. See [account selection and relationships](references/account-selection-and-relationship-typology.md).
3. **Decode the client's pragmatic strategy.** Combine formal sources with what operators need this quarter using the account-intelligence procedure (read, listen, trace the pain, force trade-offs, converge, translate) and its question bank (targets, pressures, decisions, problems, horizon). See [pragmatic strategy and GRASP](references/pragmatic-strategy-and-grasp-mapping.md).
4. **Map the buying group.** Record each member's DMU role and GRASP (goal, role, appeal, state, power). Run the multi-threading check. Decision point: if a decider or controller is unknown, make naming them the first action.
5. **Place the relationship.** Locate the account on the relationship typology now and set a target position with dated actions.
6. **Design value.** Write value hypotheses in the client's metrics (cash, margin, cycle time, risk) with baselines; choose co-creation depth; plan the Account Cube expansion path. See [expansion, value co-creation and sponsorship](references/account-expansion-value-and-sponsorship.md).
7. **Govern.** Appoint and brief the executive sponsor; set the review cadence and the quarterly value-tracking agenda; define the account-team roles (RASIC).
8. **Negotiate when terms are due.** Prepare with the [strategic-account negotiation reference](../premium-pricing-and-value-defense/references/strategic-account-negotiation.md): compatible interests first, equivalent-value options, conditional concessions, post-settlement review.
9. **Write the one-page plan.** Use the [template](references/one-page-account-plan-template.md). Every objective names a metric, baseline, target, date and owner.
10. **Check and recover.** Run critical-analysis and anti-slop gates on client-facing parts. If evidence is missing, recover by returning a qualified plan with discovery actions rather than filling gaps.

## Quality Standards

- Every account objective is specific, measurable, owned and dated; nothing is labelled "partnership" without a joint plan or investment behind it.
- Value statements use the client's own metrics and name a baseline and a measurement method.
- The stakeholder map covers at least the decider, controller (budget), user and gatekeeper, or records them as unknown.
- The plan separates observed facts, client statements and our hypotheses.
- Sponsor activity is social and strategic; tactical price negotiation stays with the account lead.

## Anti-Patterns

- Calling a large client "key" without dedicated resources. Fix: classify it and either fund the key-account plan or treat it as a large account.
- Planning from the annual report alone. Fix: decode the pragmatic strategy through operator-level conversations.
- Single-threaded relationships, strong technical ties and no senior tie. Fix: set named contacts per level and function and review the coverage quarterly.
- Promising value without a baseline. Fix: agree the baseline and measurement method with the client before claiming improvement.
- Discounting to please at renewal. Fix: open with delivered value, offer equivalent-value options and trade every concession for something.
- Sponsors who bypass the account lead. Fix: brief the sponsor, keep them strategic, and route commitments through the lead.
- Using unsourced statistics about key-account performance. Fix: cite a primary source or omit the figure.

<!-- dual-compat-end -->

## References

- [Account selection and relationship typology](references/account-selection-and-relationship-typology.md) - four account types, captive universes, client grading, relationship typology and quality, trust development and recovery.
- [Pragmatic strategy and GRASP mapping](references/pragmatic-strategy-and-grasp-mapping.md) - account-intelligence procedure and question bank, token priority-convergence exercise, DMU roles, GRASP, nine-box customer SWOT, competitive profile matrix.
- [Account expansion, value co-creation and sponsorship](references/account-expansion-value-and-sponsorship.md) - Account Cube, value-based selling, co-creation, value tracking, sponsor roles, escalation, account team.
- [One-page account plan template](references/one-page-account-plan-template.md) - template and worked example.
- [Strategic-account negotiation](../premium-pricing-and-value-defense/references/strategic-account-negotiation.md) - negotiation guidelines for strategic clients.
- [Sales discovery and objection handling](../sales-discovery-and-objection-handling/SKILL.md) - single-opportunity discovery.
- [Premium client proposal strategy](../premium-client-proposal-strategy/SKILL.md) - premium buyer positioning for the proposals the plan generates.
