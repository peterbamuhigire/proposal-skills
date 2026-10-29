# Official procurement form observations for the disposable tasks

Access date: 2026-10-29. These are limited source observations, not tender-specific legal advice.

## PPDA open/restricted non-consultancy services SBD

The official PPDA SBD index lists a “Standard Bidding Document for the Procurement of Non-Consultancy Services Under Open or Restricted Bidding”. [PPDA SBD index](https://www.ppda.go.ug/standard-bidding-documents/)

I fetched the official .docx linked from that page to a temporary prep directory and inspected it locally. The document's own contents list Part 1 Bidding Procedures (Sections 1–5), Part 2 Statement of Requirements (Section 6), and Part 3 Contract (Sections 7–9). The template describes non-consultancy services and provides the Bid Data Sheet, evaluation methodology, bidding forms, Terms of Reference, and contract forms. The standard example uses Technical Compliance Selection (TCS) and describes four sequential evaluation stages. Its submission instructions discuss separate original/copy packages inside one outer package; that is different from a QCBS technical/financial two-envelope procedure.

This fixture is deliberately scoped to an ICT implementation/configuration/support service under an open domestic non-consultancy SBD. It does not presume that a buyer purchasing off-the-shelf hardware or software should classify the package this way. Actual classification and buyer-specific BDS must control.

## World Bank consulting services RFP

The World Bank official procurement framework lists the consulting RFP non-supervision SPD as February 2025 and links the current document. [World Bank Project Procurement Framework](https://www.worldbank.org/ext/en/what-we-do/project-procurement/framework) The specific official RFP document was downloaded to the temporary prep directory and inspected locally: [official February/March 2025 RFP document](https://thedocs.worldbank.org/en/doc/648e88c7531aa9eb09daaceeaa6ffbfc-0290012025/original/SPD-RFP-Consulting-services-non-supervision-Feb-2025.docx). The file identifies a March 2025 revision, supports QCBS among listed methods, and its checklist includes a “Page Limit” column to be completed for the solicitation. The current procurement framework lists the IPF Borrowers Regulations Seventh Edition dated September 2025. [World Bank Regulations/framework page](https://www.worldbank.org/ext/en/what-we-do/project-procurement/framework)

The inspected RFP's form checklist identifies TECH-1 through TECH-8, including TECH-5 work schedule/deliverable planning, TECH-6 team composition/key expert inputs/CVs, TECH-7 Code of Conduct, and TECH-8 SEA/SH performance declaration. The financial checklist identifies FIN-1 through FIN-4: submission form, summary of costs, remuneration, and reimbursable expenses. Its data sheet separates “Financial Proposal to be submitted together with Technical Proposal” from the specific envelope contents and asks the client to supply the technical proposal type and page limits. These field descriptions make it unsafe to hard-code one technical form list/page cap for every solicitation.

The downloadable standard is copyright-limited to non-commercial use and bars modifying the SPD itself (its own front matter). This task only reads it and creates separate synthetic response notes; the source document is not redistributed here.

## Local guide discrepancy found

`skills/profiles-sectors/sectors/world-bank/references/tech-fin-forms-guide.md` lines 132–144 label TECH-5 as team composition; lines 148–164 label TECH-6 as CVs; lines 184–197 label TECH-7 as staffing schedule; lines 201 onward label TECH-8 as work schedule; lines 281–290 include FIN-5 miscellaneous expenses. The inspected March 2025 SPD instead labels TECH-5 work schedule/planning for deliverables, TECH-6 team composition/key expert inputs/CVs, TECH-7 Code of Conduct, TECH-8 SEA/SH performance declaration, and lists FIN-1 to FIN-4 only. This is a concrete current template mismatch. Recheck the actual solicitation and applicable amendment before using any local guide; the suggested small repair is to correct the form map and add a currentness note, then run tests and validators. The source file was inspected; no repo edits were made.

## Official source gaps

- No official PPDA open-domestic ICT system solicitation was supplied; the PPDA BDS below is a synthetic test fixture, not a real tender.
- The current World Bank SPD does not set a universal per-section page cap in the downloaded standard template; the Page Limit table is a solicitation field. This exercise sets its own clearly synthetic caps for the test only.
- No real bidder profile, signed declarations, CVs, project references, audited accounts, bid price, signatory evidence, portal instructions, or submission authority were provided. These remain blank/unverified and block any real bid release.
