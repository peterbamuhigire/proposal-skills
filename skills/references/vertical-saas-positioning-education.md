# Vertical SaaS Positioning — Education

Positioning brief for SaaS implementation and SaaS product-development proposals in education. Covers universities, school groups, technical and vocational education and training (TVET) providers, examinations bodies, education ministries, and EdTech companies.

## Sub-Vertical Map

| Sub-vertical | Typical Buyer | Typical Pain Pattern |
|---|---|---|
| University | Vice-Chancellor + Director ICT + Registrar | Student information, learning management, research, fees, accreditation |
| School group | CEO + Head of Schools + Director ICT | Multi-campus operations, parent communication, fees, learning outcomes |
| TVET provider | Principal + Director Programmes | Apprenticeship tracking, industry-employer linkage, qualifications |
| Examinations body | Executive Secretary + ICT Director | Candidate management, exam logistics, results, integrity |
| Education ministry | Permanent Secretary + Director Planning | EMIS, teacher management, school-feeding, scholarships |
| EdTech | Founder + CTO + Head of Product | Speed to market, learner acquisition, content production, retention |

## Regulators and Compliance Realities

- **Education ministries / commissions** — accreditation, curriculum, fee regulation.
- **Higher education regulators** — National Council for Higher Education (Uganda), Commission for University Education (Kenya), NUC (Nigeria).
- **Examinations regulators** — UNEB (Uganda), KNEC (Kenya), WAEC, NECO (Nigeria).
- **Data protection** — child-data protection often has heightened rules; school-age data residency expectations exist.
- **Qualifications frameworks** — UVQF, KNQF, NQF — for TVET and certification interoperability.

## Common Integration Reality

- Student information systems (SIS) — multiple regional and global vendors.
- Learning management systems (LMS) — Moodle (dominant in higher education in the region), Canvas, Blackboard, Google Classroom in primary/secondary.
- Library information systems.
- Research information systems for universities.
- Finance / fees systems with payment-gateway and mobile-money integrations.
- Examinations management systems.
- EMIS for ministry-level data.
- Identity systems — student ID, national ID linkage for older students.

## Proof Points the Agency Should Cite

- SIS rollouts with reduced student-services cycle time.
- LMS rollouts with measured course-completion and engagement.
- Fees-collection modernisations with collection-rate uplift.
- Examinations modernisations with reduced cycle time and improved integrity.
- TVET-employer-linkage platforms with measured employment outcomes.

## Price Ceiling Notes

- Universities have constrained budgets but multi-year planning horizons.
- School groups vary widely; high-end private school groups tolerate enterprise pricing, public schools and donor-funded programmes have rate ceilings.
- Examinations bodies have sector-specific procurement and integrity requirements.
- EdTech is venture-backed where it exists; fixed-price, milestone-based works well.

## Win Themes for This Vertical

- **Learner-centric design** — workflows respect the learner's time and constraints (cost of data, device variability, schedule conflicts).
- **Connectivity and device variability** — works on low-bandwidth and on older Android devices.
- **Local-language support** — multi-language UI for primary and secondary education.
- **Examinations integrity** — for examinations bodies, integrity is the entire value proposition.
- **TVET-employer linkage realism** — the agency understands the employer side of the equation.
- **Capacity transfer** — for ministry and donor work, the operating capability transfers.

## Anti-Patterns Specific to This Vertical

- Designing for high-bandwidth, high-end-device users only.
- Treating LMS rollout as a software project rather than a pedagogical change.
- Ignoring the multi-stakeholder political reality (ministry, union, parents, employers).
- Underestimating the academic-calendar lock-in (cannot cut over mid-term).
- For examinations, underestimating the integrity threat surface.

## Discovery Questions Specific to Education

In addition to the standard SaaS discovery question bank:

- Which SIS, LMS, finance, and library systems are in scope?
- What is the academic calendar and which cutover windows are realistic?
- What is the bandwidth and device-mix reality for learners and educators?
- Which languages must the UI support?
- How is fees collection done today (bank, mobile-money, agent)?
- For higher education, what is the research-information dimension?
- For examinations, what is the integrity threat model?
- For TVET, what is the employer-linkage value proposition?
- For ministry work, which EMIS reports does the SaaS feed?

## See Also

- `saas-discovery-question-bank.md`.
- `saas-procurement-and-security-questionnaire-playbook.md`.
- `saas-implementation-methodology-blocks.md`.
- `saas-business-case-and-roi-template.md`.
- `vertical-saas-positioning-public-sector.md` for the ministry overlap.
- `../capacity-building/SKILL.md` for capacity-transfer.
