# Proposal Skills

Proposal Skills is a library of 115 skills for planning, drafting, reviewing, and packaging bids, tenders, requests for proposals, expressions of interest, consulting offers, and commercial proposals. It works from the actual solicitation, buyer context, evaluation criteria, and proposer evidence; it does not infer tender requirements from prior bids or invent credentials, compliance, or delivery capacity. Its operating standards emphasise traceable claims, feasible methods and pricing, consistent sections, professional British English, and evidence-based review.

The engine produces proposal sections and full bid packages, compliance and evidence maps, workplans and team plans, commercial exhibits, SaaS and AI proposal materials, and review or red-team findings. It serves consultants, agencies, development-sector firms, proposal teams, and bid reviewers; specialist routes cover procurement and sectors, while current research, finance, design, and implementation questions hand off to the relevant domain engines.

## Installation

Install the native Claude Code plugin, or clone the repository and use its installer. The clone installer requires Node.js 18 or newer and supports user or project scope.

```text
/plugin marketplace add https://github.com/peterbamuhigire/proposal-skills
/plugin install proposal@chwezi-proposal

git clone https://github.com/peterbamuhigire/proposal-skills
cd proposal-skills
./install.sh --scope project      # macOS/Linux/Git Bash
.\install.ps1 -scope project      # Windows PowerShell
```

## Capabilities

The category table reflects 115 active skill files under `skills/`, including the parent router. Open a category to browse its current skills; the [proposal router](skills/SKILL.md) sets the workflow and cross-cutting routes.

| Category | Skills | Focus |
|---|---:|---|
| [Proposal pipeline](skills/pipeline/) | 10 | Cover letter, executive summary, assignment understanding, profile, experience, methodology, team, work plan, EOI, and financial proposal |
| [Profiles and sectors](skills/profiles-sectors/) | 18 | Proposer profiles, sector positioning, and procurement routes including PPDA Uganda, AfDB, UNDP, and World Bank |
| [Domain delivery](skills/domain-delivery/) | 16 | Project management, M&E, risk, change, safeguards, stakeholder engagement, and specialist delivery proposals |
| [Strategy and positioning](skills/strategy-positioning/) | 12 | Discovery, evaluator journey, account pursuit, value defence, service design, orals, and proposal storytelling |
| [SaaS proposals](skills/saas-proposals/) | 14 | SaaS discovery, business case, pricing, implementation, pilots, procurement, adoption, and vertical positioning |
| [AI-on-SaaS proposals](skills/ai-on-saas-proposals/) | 11 | AI fit, evaluation, risk, pricing, pilot design, procurement, adoption, and team composition |
| [AI-agent proposals](skills/ai-agent-proposals/) | 11 | Agent discovery, autonomy, methodology, safety, pilots, evaluation, procurement, and adoption |
| [AI-agent commercial terms](skills/ai-agent-commercial/) | 8 | Packaging, SLAs, credits, pricing, refunds, contract terms, renewal, and true-up |
| [Writing and content](skills/writing-content/) | 3 | Premium commercial writing and separate blog planning and drafting routes |
| [Language](skills/language/) | 2 | East African English and language standards |
| [Quality and operations](skills/meta/) | 9 | Anti-slop review, red-team, submission proof, localisation, skill safety, and improvement workflows |
| [Proposal router](skills/SKILL.md) | 1 | Orchestration and cross-engine routing for multi-section work |

## References

- [Proposal Skills repository](https://github.com/peterbamuhigire/proposal-skills) — active skill inventory and source implementation.
- [Proposal router](skills/SKILL.md), [repository policy](AGENTS.md), [common rules](rules/common/core.md), and [language standards](skills/language/language-standards/SKILL.md) — evidence, routing, and writing contracts consulted for this overview.
- [Runtime-agnostic orchestration contract](docs/operations/runtime-agnostic-orchestration-2026-09-07.md) — scoped packages, evidence and pricing checkpoints, context hygiene, least agency, and sanitised handling of external content for multi-phase proposal work.
- Sister engines for commercial inputs: [Business Plan Skills](https://github.com/peterbamuhigire/business-plan-skills) for feasibility, projections, and investor readiness; [Social Media Skills](https://github.com/peterbamuhigire/social-media-skills) for campaigns, content calendars, and marketing reporting. Other cross-engine routes are listed in [AGENTS.md](AGENTS.md).
- [Everything Claude Code (ECC)](https://github.com/affaan-m/ECC) — cited in local skill provenance and repository rules for specific workflow adaptations.
