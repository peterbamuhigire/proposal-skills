# SaaS Vendor-vs-Build Narrative

Build-vs-buy narrative for defending vendor-managed SaaS over in-house build or installed software. Use inside the Executive Summary, Understanding of the Assignment, and as the standalone response to "we can build this ourselves" or "our team will configure an open-source alternative."

## The Decision Framework

The vendor-vs-build decision rests on five questions:

1. **Differentiation**: does the capability *differentiate* the client commercially, or is it commodity infrastructure?
2. **Capacity**: does the client have the engineering capacity to build, operate, and continuously improve at the required quality?
3. **Time to value**: can the client deliver value at the required tempo by building, or only by buying?
4. **Total cost of ownership over 5 years**: which option costs less when all costs (build, operate, maintain, secure, comply, replace) are included?
5. **Risk and accountability**: which option places risk and accountability with the party best able to manage it?

A capability that is non-differentiating, where capacity is constrained, where time is critical, where TCO favours buy, and where risk is better held by the vendor — should be bought. The opposite should be built.

## The Standard Narrative (template for proposals)

### Opening (one paragraph)
"Some capabilities should be built in-house; others should be bought from specialists. The question is not whether to build everything or buy everything, but which capabilities to build and which to buy. In our experience with [vertical] clients, the capabilities that warrant in-house build are those that materially differentiate the client commercially or where the client holds unique data, expertise, or process advantage. The capabilities that warrant buy are those where industry-grade quality is the bar, where the build effort does not improve the client's competitive position, and where the total cost of ownership and risk profile favour a specialist."

### The Quadrant (table)

| | High Differentiation | Low Differentiation |
|---|---|---|
| **High Capacity to Build** | Build, with a clear product-and-platform strategy | Strong candidate to buy and free capacity for differentiation |
| **Low Capacity to Build** | Partner-build (agency builds, transitions to client team), or buy with deep customisation | Buy |

### The Five-Question Pass (for the specific capability)

Walk through the five questions for the specific capability in scope, with the client's situation explicit:

1. **Differentiation**: "Does [capability] differentiate [client] in [vertical]? In our view: [yes / no / partly]. Evidence: [comparables, market position, customer feedback]."
2. **Capacity**: "Does [client]'s engineering function have the capacity (people, skills, time) to build, operate, and continuously improve [capability] at the required quality? In our view: [yes / no / partly]. Evidence: [team size, skill mix, current backlog, hiring pipeline]."
3. **Time to value**: "Can [client] deliver value at the required tempo by building? Required tempo: [date]. Build tempo: [estimated timeline]."
4. **Total cost of ownership**: "Over five years, what is the all-in cost of build vs buy?" (Use the TCO table from the business case template.)
5. **Risk and accountability**: "Which option places risk and accountability with the party best able to manage it?"

### The TCO Comparison

Use a five-year TCO comparison adapted from the business-case template, with build-side and buy-side cost components:

| Cost Component | Build (in-house) | Buy (vendor-managed SaaS) |
|---|---|---|
| Initial engineering build | [Cost] | [Implementation fee] |
| Engineering team (years 1–5) | [Cost] | [Reduced or zero] |
| Infrastructure (servers, storage, network) | [Cost] | [Subscription fee] |
| Security and compliance (audit, pen-test, certifications) | [Cost] | [Vendor inherited] |
| BCDR and disaster-recovery testing | [Cost] | [Vendor inherited] |
| Operations and 24x7 support | [Cost] | [Vendor inherited] |
| Continuous improvement (new features, dependency updates) | [Cost] | [Vendor inherited via roadmap] |
| Talent attrition risk | [Cost] | [Not applicable] |
| Total 5-year TCO | **[Total]** | **[Total]** |

### The Time-to-Value Comparison

| Milestone | Build (in-house) | Buy (vendor-managed SaaS) |
|---|---|---|
| First usable environment | [Months] | [Weeks] |
| First user productive | [Quarter] | [Month] |
| First measurable metric movement | [Year+] | [Quarter] |
| Full rollout complete | [18–36 months] | [6–12 months] |

### The Risk Comparison

| Risk | Build | Buy |
|---|---|---|
| Key-person dependency | High (named engineers own the system) | Mitigated (vendor team + escrow) |
| Security exposure | Client carries full liability | Shared, with vendor's certifications and SLA |
| Compliance certification | Client must achieve and maintain | Inherited where available |
| Operational continuity | Client builds 24x7 capability | Vendor SLA |
| Technology obsolescence | Client manages refresh cycle | Vendor manages roadmap |
| Exit | Sunk cost; potentially unrecoverable | Defined exit clause and data return |

## When Build Wins

Acknowledge honestly when build is the better choice for the specific capability:

- The capability differentiates the client and the differentiation is sustainable.
- The client has the engineering capacity and the capability is core to the operating model.
- There is no vendor-managed SaaS that meets the requirement at acceptable risk.
- The buyer's regulator or governance posture forbids vendor-managed alternatives.

In these cases, the agency can still add value as a partner-build operator: the agency builds, hands over, and supports the client team through ramp-up.

## When Buy Wins

- The capability is industry-standard and the bar is industry-grade quality.
- Time to value matters and the build tempo cannot meet it.
- TCO favours buy over five years.
- Risk and accountability are better held by a specialist.
- The client's engineering capacity is better deployed against true differentiation.

## Hybrid: Partner-Build

For high-differentiation capabilities where the client lacks current capacity, the agency offers a partner-build model:

1. **Phase 1 — Agency builds**: agency engineering team builds the capability under shared governance with the client's product owner.
2. **Phase 2 — Joint operation**: agency and client teams operate together, with the agency leading and the client team learning.
3. **Phase 3 — Client operates**: client team operates with the agency in a retained advisory capacity.
4. **Phase 4 — Client owns**: client team owns; agency available for change requests and major releases.

The commercial model for partner-build is typically a fixed Phase 1 fee, retainer for Phase 2, smaller retainer for Phase 3, and time-and-materials for Phase 4.

## Anti-Patterns

- Defaulting to "buy" without the differentiation analysis.
- Defaulting to "build" because of NIH (not-invented-here).
- Comparing five-year TCO without including operational and continuous-improvement cost.
- Ignoring talent-attrition risk in the build case.
- Treating "buy" as a transaction rather than a long-term relationship with renewal, expansion, and exit consequences.

## See Also

- `saas-business-case-and-roi-template.md` for the TCO and time-to-value tables.
- `saas-objection-handling-playbook.md` for the "we can build it ourselves" objection.
- `saas-win-themes-and-discriminators.md` for positioning.
- `../consulting-frameworks/references/strategy-frameworks.md` for build/buy/partner strategic frameworks.
