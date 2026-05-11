# AI-Agent SLA — Healthcare Variant

Regulator-aware SLA variant for agentic engagements in healthcare. Pairs with `ai-agent-sla-class-table.md` and `ai-agent-sla-exhibit-template.md`. Reflects African Medicines Agency principles, country-specific regulatory bodies, clinical-safety expectations, and patient-data protection frameworks.

## Applicable Regulators (Reference List)

- **Kenya**: Ministry of Health; Kenya Medical Practitioners and Dentists Council (KMPDC); Pharmacy and Poisons Board; ODPC for patient data.
- **Nigeria**: NAFDAC; Medical and Dental Council of Nigeria (MDCN); HMOs and NHIS; NDPB / NDPA for patient data.
- **South Africa**: SAHPRA; Health Professions Council of South Africa (HPCSA); POPIA Information Regulator.
- **Uganda**: National Drug Authority (NDA); Uganda Medical and Dental Practitioners Council; UPC for patient data.
- **Rwanda**: Rwanda Food and Drugs Authority; Rwanda Medical Council; NCAS for patient data.
- **Pan-African**: African Medicines Agency (AMA) principles; WHO Africa guidance on digital health and AI.

## Mandatory SLA Class

Gold is the minimum for any healthcare-administrative agent. Platinum is required for agents that touch:
- Triage or scheduling that affects clinical timing.
- Medication-related workflows.
- Patient-facing communications where misinformation has clinical risk.
- Insurance claims that affect access to care.

## Hard Limit — No Autonomous Clinical Decision

**The Agent does not make autonomous clinical decisions.** Specifically:
- The Agent does not diagnose.
- The Agent does not prescribe.
- The Agent does not adjust medication dosage.
- The Agent does not change a treatment plan.
- The Agent does not give clinical advice to a patient.

The Agent's role in clinical workflows is **admin-only**:
- Scheduling, rescheduling, reminders.
- Document drafting (clinical summaries, referral letters, after-visit summaries) for clinician review and sign-off.
- Insurance pre-authorisation administration.
- Triage routing where the Agent recommends a workflow lane and a clinician (not the Agent) confirms.
- Translation and accessibility support, with clinician sign-off where the output is patient-facing.
- Medication reminders (delivery, not adjustment) where the prescribing clinician authorised the reminder.
- Eligibility, billing, and claims administration.

The Action Catalogue explicitly excludes any action that constitutes a clinical decision. This is non-negotiable.

## Healthcare-Specific SLA Adjustments

### 1. Patient-Detriment SLA
Where the Agent's actions can affect patient access to care:

| Metric | Threshold |
|---|---|
| Patient-detriment incidents per 10,000 Tasks | ≤ 0.1 (Gold); ≤ 0.05 (Platinum) |
| Median time to identify patient detriment | ≤ 12 hours |
| Patient-safety event escalation to Buyer's clinical lead | Immediate (within 1 hour) |
| Regulator-notification trigger | Any patient-safety event meeting the regulator's reportable-event definition, within 24 hours |

A patient-detriment incident is the Agent causing or contributing to patient harm — missed appointment due to wrong reschedule, denied or delayed pre-authorisation, wrong patient routing, identity confusion, communication error.

### 2. Clinician Sign-Off SLA
Where the Agent produces clinical-adjacent output (referral letter, after-visit summary, discharge instructions, clinical translation) the output is **held for clinician sign-off** before delivery to the patient or the next provider. The sign-off SLA:

| Step | Threshold |
|---|---|
| Output ready for clinician review | Logged with timestamp |
| Clinician sign-off elapsed time (P95) | Buyer's clinical workflow KPI |
| Output held in queue without sign-off | Maximum 72 hours; then auto-pause and notify clinical lead |

### 3. Audit-Log Retention
Audit-log retention is the **longer of ten (10) years and the clinical-records retention requirement** for the relevant jurisdiction. For paediatric and oncology workflows, retention may be longer.

### 4. Patient Data Protection
- Patient identifiable data is end-to-end encrypted in transit and at rest.
- Data-residency follows the country's data-protection law for health data, which often requires in-country storage.
- Sub-Processor list excludes any provider that retains health data for training without explicit and granular consent.
- The Sovereign-AI Provider Schedule is mandatory where the regulator requires it.

### 5. Identity and Authentication
Patient identification and matching uses the country's national identity standard or the Buyer's MRN system. The Agent's actions are bound to the verified patient identity at every step. Identity confusion is a Platinum-level SLA breach.

### 6. Accessibility
The Agent supports patient-facing communications in the relevant national languages (Swahili, Pidgin, isiZulu, Luganda, Kinyarwanda, etc.) and accessible formats. Failure to operate in a required language is a service-quality breach.

### 7. Emergency-Diversion SLA
Where a patient interaction triggers an emergency-diversion rule (red-flag symptoms in a chat; safeguarding concern; suicide-risk language), the Agent must:
- Stop the routine workflow immediately.
- Surface the emergency-diversion protocol to the patient (named emergency number for the country).
- Notify the Buyer's clinical lead within the SLA window (15 minutes for Platinum).
- Log the diversion event in the Audit Log.

The emergency-diversion catalogue is in Annex [ED-1] of the Action Catalogue and is reviewed quarterly with the Buyer's clinical safety officer.

## Healthcare-Specific Exclusions and Out-Clauses

In addition to the standard Out-Clauses:

- **Public health emergency** — during declared public health emergencies, the time-to-resolve thresholds are reviewed jointly; kill-switch and audit-log SLAs remain.
- **Clinical-safety event under investigation** — where a patient-safety event is under investigation by the Buyer's clinical-safety committee, the relevant Agent action class is paused; SLA is suspended for that action class for the investigation window.
- **Regulator pause for a model-class** — where the regulator pauses a model class (e.g. a foundation-model recall for safety) the Agency invokes the fall-back; SLA is suspended for the affected window with kill-switch and audit-log unaffected.

## Healthcare-Specific Refund Triggers

In addition to the standard Refund Triggers:

- **Clinical-safety event attributable to Agency fault** — any clinical-safety event determined by the Buyer's clinical-safety committee to be at the Agency's fault triggers the Buyer's abort right with full pro-rata refund and 60-day wind-down.
- **Regulator order against the Agent in clinical workflows** — a final order from the country's health regulator to terminate or substantially restrict the Agent triggers abort.
- **Sustained clinician-sign-off-queue overflow** — where outputs awaiting clinician sign-off exceed the queue maximum (72 hours) for more than 30 days, the workflow design is insufficient and the engagement is re-scoped or aborted.

## Healthcare-Specific Pricing Caveats

- **Outcome-based pricing tied to clinical outcomes is not used.** The agent does not make clinical decisions; pricing the agent on clinical outcomes is inappropriate.
- **Outcome-based pricing tied to administrative outcomes** (claims throughput, scheduling adherence, no-show rate) is permissible.
- **Per-agent (Pattern D) with explicit FTE-equivalent comparison** is the default for clinical-admin agents (clinical translation, after-visit summary drafting).
- **Hybrid (Pattern E)** is appropriate for high-volume admin agents (eligibility, pre-authorisation, claims administration).
- **Sovereign-AI premium** is documented; some jurisdictions require it.

## Healthcare-Specific Audit Rights

- Clinical-safety committee access to Audit Log at any time for safety-relevant events.
- Regulator-direct audit on prior notice through the Buyer.
- Independent auditor's report (SOC 2 Type II + ISO 27001 + ISO 42001 + HIPAA-aligned controls where the Buyer operates internationally) is the routine substitute.

## Healthcare-Specific Insurance

Professional Indemnity Insurance minimum: USD 10 million per claim, USD 20 million aggregate, with explicit cover for AI-system actions in healthcare admin workflows. Cyber Liability: USD 10 million per claim with explicit cover for breach of patient data. Where the engagement is multi-country, cover is endorsed for each operating country.

## Communication and Patient Trust

- Patient-facing materials disclose that the patient is interacting with an AI Agent, the Buyer's identity, the Agent's admin-only scope, and the patient's right to a clinician.
- The Buyer's complaint and feedback mechanisms are surfaced in the Agent's interaction.
- The Agency does not communicate publicly about a healthcare engagement without the Buyer's written consent.
