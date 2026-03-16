# Data Protection and Privacy

Reference material for the data-management skill. Provides detailed guidance on data protection principles, African and East African data protection legislation, Data Protection Impact Assessments, cross-border data transfers, special data categories, practical compliance for development projects, and proposal strategy notes. Use when proposals involve personal data collection, data governance, MIS design, digital platforms, health information systems, or any processing of personally identifiable information.

Sources: African Union Data Policy Framework (February 2022); AU Convention on Cyber Security and Personal Data Protection (Malabo Convention, 2014; entered into force June 2023); Uganda Data Protection and Privacy Act 2019; Kenya Data Protection Act 2019; Rwanda Law Relating to the Protection of Personal Data and Privacy 2021; Uganda Data Governance Study (2023); GDPR comparative analysis literature (2024-2025).

---

## 1. Data Protection Principles

### Eight Core Principles

These principles appear across the AU Data Policy Framework, GDPR, and all four East African jurisdictions. Any proposal involving personal data must demonstrate compliance with each.

| # | Principle | Description | Proposal Implication |
|---|-----------|-------------|----------------------|
| 1 | **Lawfulness, fairness, and transparency** | Processing must have a lawful basis; data subjects must be informed of how their data will be used | State the legal basis in methodology; include participant information sheets |
| 2 | **Consent** | Data subjects must give free, specific, informed, and unambiguous consent; consent must be withdrawable | Design consent forms; describe opt-out mechanisms |
| 3 | **Purpose limitation** | Data collected for specified, explicit, and legitimate purposes only; no secondary use without fresh consent | Define data purposes in project inception; restrict scope in data sharing agreements |
| 4 | **Data minimisation** | Collect only data that is adequate, relevant, and limited to what is necessary | Justify every data field in survey instruments; avoid "nice-to-have" variables |
| 5 | **Accuracy** | Data must be accurate and kept up to date; inaccurate data must be erased or rectified without delay | Build validation rules into data collection tools; schedule periodic data cleaning |
| 6 | **Storage limitation** | Data retained only as long as necessary for the stated purpose | Define retention periods in data management plan; schedule destruction |
| 7 | **Integrity and confidentiality** | Appropriate technical and organisational security measures against unauthorised access, loss, or destruction | Specify encryption, access controls, and audit trails in technical proposals |
| 8 | **Accountability** | The data controller must demonstrate compliance with all principles | Designate a data protection officer or focal point; maintain processing records |

### Data Subject Rights

Data subjects hold the following rights under East African and AU frameworks. Projects must design systems that can fulfil these rights upon request.

| Right | Description | Implementation Requirement |
|-------|-------------|----------------------------|
| **Access** | Right to obtain confirmation of processing and a copy of personal data held | Build data export functionality into MIS/databases |
| **Rectification** | Right to correct inaccurate or incomplete data | Provide correction request mechanisms in data collection systems |
| **Erasure** | Right to request deletion when data is no longer necessary or consent is withdrawn | Design deletion procedures; maintain audit trail of deletions |
| **Restriction** | Right to limit processing in certain circumstances | Implement data flags to restrict processing without deletion |
| **Portability** | Right to receive data in a structured, machine-readable format | Support CSV/JSON export from project databases |
| **Objection** | Right to object to processing based on legitimate interests or for direct marketing | Document objection process in data management plan |

### Lawful Bases for Processing

Six lawful bases (aligned across AU framework and East African laws):

1. **Consent** — most common in development projects; must be documented and withdrawable.
2. **Contractual necessity** — processing needed to perform a contract with the data subject.
3. **Legal obligation** — processing required by law (e.g., tax records, statutory reporting).
4. **Vital interests** — processing necessary to protect someone's life (e.g., emergency health data).
5. **Public interest** — processing necessary for a task carried out in the public interest or official authority (common basis for government projects).
6. **Legitimate interests** — processing necessary for legitimate interests of the controller, balanced against data subject rights (weakest basis; rarely appropriate for development projects).

**Proposal guidance:** For most consulting assignments, consent and public interest are the primary bases. State the chosen basis explicitly in the methodology section and data management plan.

---

## 2. African Data Protection Landscape

### AU Malabo Convention (2014/2023)

The African Union Convention on Cyber Security and Personal Data Protection was adopted on 27 June 2014 in Malabo, Equatorial Guinea. It entered into force on 8 June 2023 after reaching the required 15 ratifications.

**Scope:** Establishes continental standards for electronic transactions, personal data protection, cybersecurity, and cybercrime.

**Key provisions on data protection (Chapter II):**
- Requires each State Party to establish a national data protection authority
- Mandates prior authorisation or declaration for processing personal data
- Prohibits processing of sensitive data (racial/ethnic origin, political opinions, religious beliefs, health, sexual life, genetic data, criminal records) except with explicit consent or legal exception
- Requires data controllers to ensure confidentiality and security of processing
- Establishes data subject rights to information, access, objection, and rectification
- Addresses cross-border data transfers: transfers to non-Party states only where the receiving state ensures adequate protection

**Ratification status (as of early 2026):** 17 ratifications. Signatories include most East African states. Uganda, Kenya, and Rwanda have domesticated the principles through national legislation; Tanzania's bill is pending.

### AU Data Policy Framework (February 2022)

The AU Data Policy Framework provides continental guidance on data governance, complementing the Malabo Convention with practical data management standards.

**Data categorisation:**

| Category | Examples | Protection Level |
|----------|----------|------------------|
| **Personal data** | Names, ID numbers, phone numbers, location data | Full data protection law applies |
| **Community data** | Indigenous knowledge, cultural heritage data, community health patterns | Community consent required; benefit-sharing obligations |
| **Business/proprietary data** | Trade secrets, algorithms, business intelligence | Commercial confidentiality; IP protection |
| **Sensitive data** | Health records, biometrics, financial data, children's data, criminal records | Heightened protections; explicit consent; additional safeguards |
| **Public sector data** | Government statistics, budget data, procurement records | Open-by-default principle; anonymisation where personal data overlaps |

**Cross-border data flow principles:**
- Data sovereignty: African states retain jurisdiction over data generated within their borders
- Free flow within Africa: Framework encourages intra-African data flows to support AfCFTA
- Adequacy-based transfers: Transfers outside Africa require adequacy assessment of the receiving jurisdiction
- Data localisation: Framework acknowledges national localisation requirements while seeking continental harmonisation

**Data sovereignty position:** The Framework asserts that Africa's data is a strategic asset. It promotes local data storage and processing infrastructure, African-owned cloud services, and continental data exchange mechanisms.

### Continental Trends

- **44 of 55** AU member states now have data protection or privacy legislation (up from 36 in 2022)
- **38 operational** Data Protection Authorities across the continent (some recently established, with limited capacity)
- **GDPR influence:** Most post-2018 African laws are modelled substantially on GDPR principles, with adaptations for local context
- **Key divergences from GDPR:** lower enforcement capacity, fewer adequacy decisions, higher reliance on consent (vs. legitimate interests), emerging community data concepts not present in GDPR, and digital infrastructure gaps affecting implementation

---

## 3. East African Data Protection Laws

### Comparative Table

| Feature | **Uganda** | **Kenya** | **Rwanda** | **Tanzania** |
|---------|-----------|----------|-----------|-------------|
| **Legislation** | Data Protection and Privacy Act, 2019 | Data Protection Act, 2019 | Law No. 058/2021 Relating to the Protection of Personal Data and Privacy | Personal Data Protection Act (under development; apply Uganda/Kenya standards as minimum) |
| **Lead agency** | Personal Data Protection Office (PDPO), under NITA-U | Office of the Data Protection Commissioner (ODPC) | National Cyber Security Authority (NCSA) | Pending designation |
| **Registration** | Data controllers and processors must register with PDPO | Data controllers and processors must register with ODPC | Notification to NCSA required before processing | Expected to require registration |
| **Consent rules** | Free, specific, informed, unambiguous; written or electronic; withdrawable | Free, specific, informed, unambiguous; opt-in required; children under 18 require parental consent | Explicit consent for sensitive data; implied consent permitted for non-sensitive where reasonable | Expected to align with Kenya/Uganda |
| **Data subject rights** | Access, rectification, erasure, restriction, objection | Access, rectification, erasure, portability, objection, right not to be subject to automated decisions | Access, rectification, erasure, objection, restriction | Expected to include core rights |
| **Breach notification** | Required; no specified timeframe in the Act (regulations pending) | Within 72 hours to ODPC; without undue delay to affected data subjects | Required; timeframe specified in implementing regulations | Expected to require notification |
| **Cross-border transfers** | Permitted only to countries with adequate protection or with data subject consent | Permitted with adequate protection, binding corporate rules, or standard contractual clauses; ODPC may approve specific transfers | Permitted with NCSA authorisation and adequate protection in receiving country | Expected to restrict transfers |
| **Penalties** | Up to UGX 4.8 million (approx. USD 1,300) and/or imprisonment up to 10 years for serious offences | Up to KES 5 million (approx. USD 38,000) or 1% of annual turnover; imprisonment up to 2 years | Fines and imprisonment as specified in implementing regulations | Pending |
| **Special categories** | Health data, biometric data, genetic data, children's data, financial data | Health, genetic, biometric, children's, racial/ethnic, political opinions, sexual orientation | Health, biometric, genetic, criminal records, political opinions, religious beliefs | Expected to align with regional standards |

### Key Implementation Notes

**Uganda — PDPA 2019 compliance gaps (from DG Study 2023):**
- Low registration rates with PDPO; many data controllers unaware of obligations
- Data sharing between government agencies lacks standardised agreements
- Citizen awareness of data protection rights is minimal, particularly in rural areas
- Sector-specific guidelines (health, education, agriculture) not yet issued
- Enforcement actions remain limited due to PDPO resource constraints

**Kenya — strongest enforcement posture in East Africa:**
- ODPC actively issuing guidance notes and conducting audits
- DPIA requirements are well-defined and enforced for high-risk processing
- Registration portal operational; compliance certificates issued
- Breach notification within 72 hours is a hard requirement

**Rwanda — digital-first approach:**
- NCSA integrates data protection with broader cybersecurity mandate
- Strong alignment with national digital transformation strategy (Smart Rwanda)
- Data protection embedded in e-government standards

---

## 4. Data Protection Impact Assessment (DPIA)

### When a DPIA Is Required

A DPIA is mandatory (under Kenya DPA 2019, Section 31, and recommended practice across East Africa) when processing is likely to result in high risk to data subjects. Triggers include:

- **Large-scale processing** of personal data (e.g., national surveys, census support, beneficiary databases)
- **Systematic monitoring** of public areas or populations (e.g., CCTV, GPS tracking, remote sensing linked to individuals)
- **Sensitive data processing** at scale (health records, biometric enrolment, children's data)
- **Automated decision-making** with significant effects (e.g., beneficiary targeting algorithms, credit scoring)
- **New technologies** applied to personal data (AI/ML, blockchain identity, IoT devices)
- **Cross-border transfers** of personal data outside the jurisdiction
- **Matching or combining** datasets from different sources

### DPIA Process

| Step | Activity | Output |
|------|----------|--------|
| 1. **Description** | Document the nature, scope, context, and purposes of processing; describe data flows and storage | Data flow diagram; processing inventory |
| 2. **Necessity and proportionality** | Assess whether processing is necessary for the stated purpose; confirm data minimisation | Justification statement for each data element |
| 3. **Risk assessment** | Identify risks to data subjects (unauthorised access, data loss, re-identification, discrimination, distress) | Risk register with likelihood and impact ratings |
| 4. **Mitigation measures** | Define technical and organisational measures to reduce identified risks to acceptable levels | Controls matrix (encryption, access controls, pseudonymisation, training, audit) |
| 5. **Consultation** | Consult the relevant DPA if residual risks remain high; consult affected communities where appropriate | DPA correspondence; stakeholder consultation records |
| 6. **Sign-off and review** | Senior management approval; schedule periodic review (at minimum, annually or when processing changes) | Signed DPIA document; review schedule |

### DPIA Template Structure for Proposals

When a proposal includes a DPIA as a deliverable or annex, use this structure:

1. Project overview and data processing description
2. Legal basis and regulatory framework
3. Data flow diagram (collection → storage → processing → sharing → retention → destruction)
4. Data elements inventory (each field, purpose, sensitivity level)
5. Risk assessment matrix (risk description, likelihood, impact, risk level, mitigation)
6. Technical security measures (encryption standards, access control, backup, audit logging)
7. Organisational measures (policies, training, incident response, DPO appointment)
8. Data subject rights fulfilment procedures
9. Cross-border transfer safeguards (if applicable)
10. Residual risk assessment and DPA consultation needs
11. Review schedule and version control

---

## 5. Cross-Border Data Transfers

### AU Framework Requirements

The AU Data Policy Framework and Malabo Convention establish that cross-border transfers require:
- Adequate level of data protection in the receiving country
- Appropriate safeguards where adequacy is not established
- Data subject consent as a supplementary (not sole) basis
- Government oversight capacity for monitoring compliance

### Country-Specific Transfer Mechanisms

| Mechanism | Uganda | Kenya | Rwanda |
|-----------|--------|-------|--------|
| **Adequacy determination** | PDPO to assess; criteria not yet published | ODPC may issue adequacy lists; none published yet | NCSA authorisation required |
| **Standard contractual clauses** | Not yet formalised; use international templates | Recognised; ODPC model clauses under development | Permitted with NCSA approval |
| **Binding corporate rules** | Not addressed in PDPA 2019 | Recognised under DPA 2019 | Not explicitly addressed |
| **Data subject consent** | Permitted as transfer basis | Permitted as supplementary basis | Permitted with explicit consent |
| **Government/public interest** | Permitted for international cooperation | Permitted for public interest | Permitted for international obligations |

### Data Localisation Requirements

Several African countries impose data localisation requirements. Key provisions relevant to East African projects:

- **Nigeria:** Nigeria Data Protection Regulation 2019 requires personal data of Nigerian citizens to be stored and processed in Nigeria, with limited exceptions
- **Rwanda:** Government data must be hosted on local or government-approved cloud infrastructure
- **Kenya:** Critical national data infrastructure provisions under development; financial sector data subject to CBK localisation requirements
- **Uganda:** No blanket localisation requirement, but government data hosting increasingly directed to National Data Centre

**Proposal guidance:** When designing systems that process data across borders (e.g., regional M&E platforms, cloud-hosted databases), specify the data hosting location, justify any cross-border flows, and include transfer safeguards in the data management plan. For multi-country projects, conduct a transfer assessment for each jurisdiction.

---

## 6. Special Categories of Data

### Health Data

Health data receives heightened protection across all East African jurisdictions. In the context of development projects:

- **DHIS2 and health MIS:** Systems collecting patient-level or facility-level health data must implement role-based access controls, audit trails, and anonymisation/pseudonymisation for reporting. Uganda's DHIS2 instance processes data for 7,000+ health facilities.
- **Consent:** Explicit consent required for health data processing; exceptions for vital interests (emergencies) and public health surveillance (with appropriate safeguards)
- **Research exemption:** Health research data may be processed without individual consent where approved by a research ethics committee and subject to anonymisation requirements
- **Retention:** Health records retention periods vary by type (patient records typically 5-10 years post-last-contact; research data per ethics approval)

### Children's Data

- **Age threshold:** Under 18 in Kenya and Uganda; processing requires verifiable parental/guardian consent
- **Purpose restriction:** Children's data may only be processed for purposes directly in the child's best interest
- **Educational data:** School management information systems (e.g., EMIS) must treat student data as children's data with full protections
- **Profiling prohibition:** Automated profiling of children is prohibited or severely restricted

### Biometric Data

- **Definition:** Fingerprints, facial recognition data, iris scans, voice patterns, DNA profiles
- **National ID programmes:** Uganda's National Identification and Registration Authority (NIRA) collects biometric data; projects interfacing with national ID systems must comply with NIRA data sharing protocols
- **Project use:** Biometric data collection in development projects (e.g., beneficiary verification, deduplication) requires explicit consent, strong encryption, and purpose limitation

### Financial Data

- **Mobile money data:** Given East Africa's mobile money penetration (Uganda: 50.5 million accounts), projects involving financial inclusion data must comply with both data protection law and financial sector regulations (Bank of Uganda, CBK requirements)
- **Credit information:** Regulated under separate credit reference bureau legislation; additional consent and accuracy obligations
- **Payment data:** PCI-DSS compliance expected for projects processing card payment data

### Employee Data

- **HR systems:** Projects implementing HR or payroll systems must address employee data protection, including purpose limitation, access restrictions, and retention schedules
- **Monitoring:** Employee monitoring (email, internet, GPS) requires notice and proportionality assessment

---

## 7. Practical Compliance for Projects

### Data Protection Checklist for Development Projects

Use this checklist during project inception and include relevant items in the data management plan:

**Governance:**
- [ ] Identify applicable data protection law(s) for each project country
- [ ] Appoint a data protection focal point or officer
- [ ] Register with relevant Data Protection Authority (PDPO, ODPC, NCSA) if required
- [ ] Conduct DPIA for high-risk processing activities
- [ ] Establish data governance committee or include data protection in project steering committee terms of reference

**Data Collection:**
- [ ] Define and document lawful basis for each data processing activity
- [ ] Design consent forms (plain language, specific purposes, withdrawal mechanism)
- [ ] Minimise data collection to fields strictly necessary for project objectives
- [ ] Build validation rules into data collection instruments (ODK, KoboToolbox, SurveyCTO)
- [ ] Train enumerators and data collectors on data protection principles and protocols

**Storage and Security:**
- [ ] Encrypt data at rest (AES-256 minimum) and in transit (TLS 1.2+)
- [ ] Implement role-based access controls with principle of least privilege
- [ ] Maintain audit logs of data access and modifications
- [ ] Establish backup procedures with encrypted off-site storage
- [ ] Separate personally identifiable information (PII) from analytical datasets using unique identifiers

**Sharing:**
- [ ] Execute data sharing agreements before transferring data to partners or government
- [ ] Anonymise or pseudonymise data before sharing for analysis or reporting
- [ ] Assess cross-border transfer requirements if data leaves the jurisdiction

**Retention and Destruction:**
- [ ] Define retention periods for each data category
- [ ] Schedule and document data destruction at end of retention period
- [ ] Use secure deletion methods (overwriting, physical destruction of media)
- [ ] Maintain destruction certificates or records

### Consent Form Template Elements

A compliant consent form for project data collection should include:

1. **Project identity:** Name, implementing organisation, contact details
2. **Purpose:** Clear statement of why data is being collected and how it will be used
3. **Data elements:** List of specific data to be collected
4. **Legal basis:** Reference to applicable law and chosen lawful basis
5. **Recipients:** Who will receive or access the data (project team, government, donors)
6. **Retention period:** How long data will be kept
7. **Cross-border transfers:** Whether data will leave the country and safeguards applied
8. **Rights:** Data subject rights (access, rectification, erasure, complaint to DPA)
9. **Voluntariness:** Explicit statement that participation is voluntary and refusal has no negative consequences
10. **Withdrawal:** How to withdraw consent and what happens to data already collected
11. **Signature/mark:** Space for informed consent (signature, thumbprint, or witnessed verbal consent for non-literate participants)

### Data Sharing Agreement Essentials

Data sharing agreements (DSAs) between project partners, government agencies, or donors should cover:

- Parties and their roles (controller, processor, joint controller)
- Purpose and scope of data sharing
- Data elements to be shared
- Legal basis for sharing
- Security measures required of the receiving party
- Restrictions on onward sharing
- Retention and destruction obligations
- Breach notification procedures between parties
- Liability allocation
- Governing law and dispute resolution
- Term and termination provisions

### Breach Response Protocol

| Phase | Timeframe | Actions |
|-------|-----------|---------|
| **Detection** | Immediate | Identify the breach; contain it (isolate affected systems, revoke compromised access) |
| **Assessment** | Within 24 hours | Determine scope, affected data subjects, data categories, likely impact |
| **Notification — DPA** | Within 72 hours (Kenya hard requirement; best practice for all jurisdictions) | Notify relevant DPA with breach details, affected numbers, likely consequences, measures taken |
| **Notification — data subjects** | Without undue delay | Notify affected individuals if breach poses high risk to rights and freedoms |
| **Remediation** | Within 1-4 weeks | Implement corrective measures; update security controls; document lessons learnt |
| **Review** | Within 3 months | Conduct post-incident review; update DPIA if necessary; report to steering committee |

### Data Retention and Destruction Procedures

| Data Category | Recommended Retention | Destruction Method |
|---------------|----------------------|-------------------|
| Project beneficiary records | Duration of project + 2 years (or as specified by donor) | Secure digital deletion; shredding of physical records |
| Survey/research data | Duration of project + 5 years (for verification and evaluation) | Anonymise for long-term retention; delete PII |
| Financial and procurement data | 7 years (audit requirements) | Secure archival then destruction |
| HR and personnel data | Duration of engagement + 3 years | Secure deletion; return personal documents to individuals |
| Health data | Per ethics approval; typically 5-10 years | Secure deletion with destruction certificate |
| Consent forms | Duration of data retention + 1 year | Shredding; secure digital deletion |

### Training Requirements for Project Staff

All project staff handling personal data should receive training covering:

- Applicable data protection law and project-specific obligations
- Data collection protocols and consent procedures
- Data security practices (password management, device security, encryption)
- Recognising and reporting data breaches
- Data subject rights and how to respond to requests
- Confidentiality obligations and consequences of violations

**Frequency:** At inception (mandatory), refresher annually, and when processing activities change significantly.

---

## 8. Proposal Strategy Notes

### When to Address Data Protection in Proposals

Data protection should be addressed explicitly when:

- The ToR involves collecting, storing, or processing personal data
- The assignment includes MIS development, database design, or digital platform creation
- Health data, beneficiary data, or household survey data is involved
- The project operates across multiple jurisdictions
- The client is a government agency subject to data protection obligations
- The donor framework requires data protection compliance (World Bank, AfDB, UNDP, EU-funded)

Even when the ToR does not mention data protection, including a brief data protection commitment in the methodology demonstrates awareness and professionalism — a differentiator in East African consulting markets where many competitors overlook this.

### Standard Proposal Commitments

Include these commitments in methodology or data management sections:

1. **Data minimisation:** "We shall collect only the data elements strictly necessary to achieve the assignment objectives."
2. **Encryption:** "All personal data will be encrypted at rest (AES-256) and in transit (TLS 1.2+)."
3. **Consent:** "Informed consent will be obtained from all data subjects prior to data collection, using plain-language consent forms in relevant local languages."
4. **Access controls:** "Role-based access controls will restrict data access to authorised project personnel on a need-to-know basis."
5. **Retention and destruction:** "Personal data will be retained for [specified period] after project completion, after which it will be securely destroyed with documented certification."
6. **DPIA:** "A Data Protection Impact Assessment will be conducted during inception for all high-risk processing activities."
7. **Compliance:** "All data processing will comply with the [Uganda Data Protection and Privacy Act 2019 / Kenya Data Protection Act 2019 / applicable law]."

### Linking to Donor Requirements

| Donor | Data Protection Expectations | Proposal Reference |
|-------|------------------------------|-------------------|
| **World Bank** | Environmental and Social Framework (ESF) ESS1 requires assessment of data-related risks; Bank Policy on Access to Information; WB Group data privacy principles | Reference ESF and propose DPIA as part of ESMP |
| **AfDB** | Integrated Safeguards System (ISS 2023) OS1 includes data considerations; AfDB data governance standards | Reference ISS and propose data governance framework |
| **UNDP** | UNDP Data Protection and Privacy Policy (2020); mandatory DPIA for high-risk processing; data minimisation and purpose limitation requirements | Reference UNDP policy; align project data management plan with UNDP standards |
| **EU** | EU external action instruments require GDPR-equivalent protections; mandatory DPIA for funded projects involving personal data | Reference GDPR alignment; propose EU-standard data protection measures |
| **USAID** | ADS 508 (Privacy Programme); mandatory Privacy Impact Assessment (PIA) for systems processing PII | Reference ADS 508; propose PIA as deliverable |
| **GIZ** | GIZ data protection officer oversight; German Federal Data Protection Act (BDSG) applies to GIZ-funded data processing | Reference BDSG alignment; propose data protection officer role |

**Differentiator strategy:** Most East African proposals treat data protection as an afterthought or omit it entirely. A well-articulated data protection approach signals technical maturity and reduces perceived risk for the evaluator. Position data protection not as a compliance burden but as a quality assurance measure that protects the client's reputation and the project's beneficiaries.
