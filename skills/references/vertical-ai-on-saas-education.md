# Vertical AI-on-SaaS — Education

Vertical positioning, named AI use cases, regulator stance, discriminators, and risk language for AI-on-SaaS bids in universities, secondary schools, EdTech platforms, examinations bodies, and ministries of education. Pairs with `ai-on-saas-vertical-positioning` and extends `vertical-saas-positioning-education.md`.

## Named AI Use Cases

| Use case | Hallucination tolerance | HITL stance | Risk class |
|---|---|---|---|
| Tutoring copilot for students | ≤ 2 % on factual; ≥ 95 % citation for academic | Student-facing; teacher-monitored | Medium |
| Assessment-marking assistance (with HITL) | ≤ 1 % on objective; rubric-graded otherwise | HITL strict; teacher signs every mark | High |
| Advisor copilot for academic advising | ≤ 2 % with citations | Adviser confirms before action | Medium |
| Content-generation assistance for instructors | Drafting only | Instructor edits and owns | Medium |
| Accessibility (TTS, translation, summarisation for learners with needs) | Reading-grade verified | Accessibility staff sign-off on launch | Medium |
| Plagiarism / integrity signal explanation (not deciding) | Explanatory | Faculty decides | High |

## Regulator Stance

- **Kenya**: Ministry of Education; NCHE; KNEC; TSC; ODPC.
- **Uganda**: NCHE Uganda; UNEB; Ministry of Education; PDPO.
- **Tanzania**: TCU; NECTA.
- **Rwanda**: HEC; NESA; NCDP.
- **Nigeria**: NUC; WAEC / NECO / JAMB; NDPC.
- **South Africa**: CHE; DHET; Umalusi; Information Regulator (POPIA + minor data).
- **Cross-border**: FERPA where US-linked; GDPR for EU learners; UN Convention on the Rights of the Child for minors.

Vertical-specific AI exposure:
- **Minor-data handling** — special category protections for under-18 learners.
- **Exam integrity** — AI-assisted cheating concerns; AI-assisted invigilation concerns; both must be addressed honestly.
- **Pedagogical role** — AI augments instruction; it does not replace certified instruction.
- **Equity** — fairness across language, socioeconomic, and disability cohorts is foundational.

## Discriminators for Education Bids

1. **Minor-data baseline** — explicit consent posture, PII-minimisation, retention discipline, parental-rights interface.
2. **Instructor-in-the-loop pedagogy** — AI augments the instructor; the instructor remains the credentialed author of assessments, syllabi, and feedback.
3. **Exam-integrity stance — honest and stated** — explicit AI-use-in-assessment policy; AI features designed to support integrity (e.g. process-not-product evaluation), not to invigilate punitively.
4. **Accessibility-first** — AI features include TTS, translation, summarisation, and reading-grade adjustment as core, not optional.
5. **Equity measurement** — per-cohort metrics for language, region, disability, socioeconomic; cohort-drift alerted.

## Risk Framing — Education-Specific Language

- "Minor-data baseline" (not "data protection").
- "Instructor-in-the-loop pedagogy."
- "Exam-integrity policy."
- "Accessibility entitlement."
- "Pedagogical authority" (not "user authority").
- "Parental-rights interface" where applicable.

## Sample Vertical Paragraph

> In education, our AI-on-SaaS practice is built on a minor-data baseline, instructor-in-the-loop pedagogy, an honest exam-integrity stance, and accessibility-first feature design. Where learners are under eighteen, the consent posture, PII minimisation, retention controls, and parental-rights interface are set as Phase 1 deliverables, not afterthoughts. AI augments the certified instructor; the instructor remains the author of assessments, syllabi, and feedback, and signs every mark on assessments where AI assists in grading. The exam-integrity stance is published and includes a clear policy on AI-use in assessment, drafted with the awarding body's input. Accessibility features — text-to-speech, translation, summarisation, reading-grade adjustment — are core to every learner-facing AI feature. Per-cohort fairness is measured by language, region, disability, and socioeconomic cohort and reviewed quarterly at the academic governance committee.

## Cross-References

- `vertical-saas-positioning-education.md`.
- `ai-on-saas-risk-register-for-proposals.md` — R-AI-EDU-01 minor-data and integrity.
- `ai-on-saas-responsible-ai-commitment.md`.
- `ai-on-saas-trust-and-compliance-section-template.md`.
