# AI-Agent SLA — Public Sector Variant

Regulator-aware and politically-sensitive SLA variant for agentic engagements in the public sector. Pairs with `ai-agent-sla-class-table.md` and `ai-agent-sla-exhibit-template.md`. Reflects EAC, SADC, ECOWAS public-procurement practice, AI Policy KE / NG / RW / UG / ZA, and citizen-redress expectations.

## Applicable Procurement and Policy Frameworks

- PPDA Uganda; PPRA Kenya; KPPRA; PPRA Tanzania; PPA Rwanda; BPP Nigeria; National Treasury (South Africa).
- AI Policy: Kenya National AI Strategy (KNAIS); Nigeria National AI Strategy (NAIS); Rwanda National AI Policy; Uganda National AI Strategy; South Africa AI Plan.
- Data Protection: KE Data Protection Act 2019; NG NDPR 2019 / NDPA 2023; ZA POPIA; UG DPPA 2019; RW Data Protection Law 2021.
- Public-finance: country-specific Public Finance Management Acts and procurement regulations.
- Sectoral: Identity (KE NIIMS, NG NIN, RW NIDA, UG NIRA); Border (regional EAC and SADC); Revenue (URA, KRA, FIRS, ZRA, BURS, SARS).
- Donor-aligned: World Bank, AfDB, UNDP procurement and safeguards.

## Mandatory SLA Class

Gold is the default. Platinum is reserved for systemically critical agents (border control, identity, payments, revenue, security). Bronze and Silver are not appropriate for production public-sector agents acting on or affecting citizens.

## Public-Sector-Specific SLA Adjustments

### 1. No Outcome-Based Pricing on Citizen Services
Outcome-based pricing (Patterns B, F, performance-corridor) on citizen-facing services is **politically inappropriate** in most jurisdictions:

- Citizens are not customers; outcome incentives misalign the public-service mission.
- Outcome pricing on benefit-determination, status-grant, sanction, or enforcement decisions risks accusations of profiteering.
- Outcome pricing on revenue collection may be permissible but requires explicit authority-of-government approval.

**Default pattern is D (Per-Agent / Per-Persona)** with explicit FTE-equivalent comparison.

### 2. No Autonomous Decision on Citizen Status / Benefit / Entitlement
The Agent does not make Decisions on citizen status, benefit, entitlement, sanction, or enforcement. Decisions are made by the Named Officer at the Buyer. The Agent's role is:
- Triage, route, assemble evidence.
- Draft, summarise, translate.
- Identify cases for the Named Officer's attention.

The Action Catalogue must explicitly exclude autonomous decisioning on citizen-affecting matters.

### 3. Citizen-Redress SLA
A citizen-affecting incident triggers a citizen-redress process:

| Metric | Threshold |
|---|---|
| Time to acknowledge citizen complaint | ≤ 24 hours |
| Time to investigate | ≤ 14 days |
| Time to resolution | ≤ 30 days |
| Communication to affected citizen | At each stage |
| Escalation to ombudsman | Available at every stage |

The redress process is operated by the Buyer; the Agency cooperates with evidence packs, audit-log access, and remedial action.

### 4. Transparency-to-Affected-Party
Every Agent external interaction with a citizen discloses that the citizen is interacting with an AI Agent, the Buyer's name, the citizen's right to request human review, and contact for redress. This is more stringent than EU AI Act Article 50 in some jurisdictions.

### 5. Sovereign-AI Default
For public-sector agents handling citizen data, **sovereign-AI deployment is the default** unless an explicit policy authority permits cross-border inference. The Sovereign-AI Provider Schedule names the in-country host, the data-residency commitment, and the fallback (which is typically another sovereign provider or a kill-switch-and-wait pattern, not a global provider).

### 6. Audit-Log Retention
Audit-log retention is the **longer of ten (10) years and the public-records retention requirement** for the relevant decision class. Some jurisdictions require permanent retention for certain decision classes.

### 7. Public-Records Access
Audit-Log entries that relate to public-records-eligible matters are subject to access-to-information obligations under the relevant country's law. The Agency cooperates with the Buyer's access-to-information function.

### 8. Procurement-Framework SLA Adjustments
| Framework | Adjustment |
|---|---|
| World Bank | Audit and inspection rights of the Bank are reserved; the agency cooperates. |
| AfDB | Sanctions screening and integrity due diligence apply at procurement and on Sub-Processor changes. |
| UNDP | Implementation of the UN Common Approach to AI applies where adopted. |
| PPDA / PPRA | Local content / local supplier obligations apply; the Agency's Sub-Processors include local-content evidence where possible. |

## Public-Sector-Specific Exclusions and Out-Clauses

In addition to the standard Out-Clauses:

- **Government holiday and emergency** — SLA time-to-resolve and time-to-action are suspended during gazetted government holidays and declared emergencies, with kill-switch and audit-log SLAs remaining in force.
- **Political-transition pauses** — where a transition of government or ministry triggers a formal pause of the engagement, the SLA is suspended for the pause window with all routine obligations preserved.
- **Public-protest-related citizen-impact** — where the Agent's operational pause is requested by the Buyer because of citizen impact during civil unrest, the SLA is suspended without penalty.

## Public-Sector-Specific Refund Triggers

In addition to the standard Refund Triggers:

- **Parliamentary, audit-general, or ombudsman finding** — a final finding by the relevant oversight body that the Agent has materially failed in its public-sector function triggers the Buyer's abort right with pro-rata refund.
- **Citizen-rights breach** — a finding by the country's data-protection authority, human-rights commission, or ombudsman that the Agent breached citizen rights triggers the Buyer's abort right.
- **Procurement-disqualification** — where the Buyer's procurement authority requires the engagement to be terminated due to an integrity finding against the Agency, refund applies subject to the standard formula.

## Public-Sector-Specific Pricing Caveats

- **Per-agent (Pattern D) is default**, with explicit FTE-equivalent comparison.
- **Hybrid (Pattern E) is acceptable** where the volume is variable and the buyer wants a predictable base.
- **Per-resolution (Pattern A) is acceptable** for back-office and administrative agents that do not directly affect citizens.
- **Sovereign-AI premium** is documented and not negotiated away — the regulator and the citizen expectations require it.
- **FX corridor** is mandatory; sustained FX shocks must trigger a Commercial Review, not an absorption.

## Public-Sector-Specific Audit Rights

- Auditor-General access to the Audit Log on demand, where applicable.
- Parliamentary committee access on formal request.
- The agency cooperates without invoking confidentiality against constitutional oversight bodies.

## Public-Sector-Specific Insurance

Professional Indemnity Insurance minimum: USD 5 million per claim, USD 10 million aggregate. Cyber Liability minimum: USD 5 million. For systemically critical agents (border, identity, revenue), USD 10 million per claim and USD 20 million aggregate.

## Communication and Public Confidence

- The Agent's identity, role, and the Buyer's accountability are stated on public-facing materials.
- A public-facing trust statement is maintained (the Responsible-AI Agent Commitment, adapted for public sector).
- The Agency cooperates with media inquiries through the Buyer's communications function.
- The Agency does not make public statements about a public-sector engagement without the Buyer's written consent.
