# AI-Agent MSA Addendum Template

Drop-in MSA addendum for agentic engagements. Attach to the base SaaS MSA or the buyer's MSA. Pairs with `../ai-agent-msa-and-sla-addendum-templates/SKILL.md`.

---

# AI-Agent Addendum to the Master Services Agreement

This Addendum is entered into on [DATE] between **[BUYER]** ("Buyer") and **[AGENCY]** ("Agency"). It forms part of the Master Services Agreement between the parties dated [MSA DATE] (the "MSA"). Where any provision of this Addendum conflicts with the MSA in respect of the Agent, this Addendum shall prevail. Capitalised terms not defined here have the meaning given in the MSA, the Pricing Exhibit, the SLA Exhibit, or the Trust and Compliance Annex.

## 1. Scope of this Addendum

1.1 This Addendum applies to any Statement of Work under the MSA in which the Agency delivers, operates, or supports one or more autonomous AI Agents acting on the Buyer's behalf.

1.2 An **Agent** is software that perceives input, plans, calls tools, decides, and acts to complete a Task assigned by the Buyer, with or without explicit step-by-step confirmation, in accordance with the Action Catalogue.

## 2. Action Accountability

2.1 The Agent is operated by the Agency on behalf of the Buyer within the Action Catalogue (Annex [Z] of the Pricing Exhibit).

2.2 The Buyer retains accountability for actions the Buyer authorises through the Action Catalogue and approves through the Buyer's named Approvers for actions classified as Irreversible.

2.3 The Agency retains accountability for: (i) the Agent operating within the Action Catalogue; (ii) the autonomy commitment per action class; (iii) the Kill-Switch SLA; (iv) the Audit-Log Completeness SLA; (v) the Agent-Identity Warranty in clause 7.

2.4 Actions outside the Action Catalogue are not authorised. If attempted by the Agent, the Agency is accountable for the breach and the consequences, subject to the Sub-Cap in clause 5.

2.5 The Buyer shall designate Named Approvers for Irreversible Actions. The Named Approvers list shall be maintained in Annex [NA-1] and may be updated by written notice.

## 3. Audit Log Retention and Replay

3.1 The Agency shall maintain an **Action Audit Log** capturing, for every Agent action: decision, tool call, parameters, result, reasoning trace where feasible, human approval where applicable, timestamp, identity, tenant, and outcome.

3.2 The Audit Log completeness shall be at or above the SLA-Class threshold (SLA Exhibit, clause 3).

3.3 The Audit Log retention period shall be no less than the longer of seven (7) years or the period required by the Buyer's regulator.

3.4 **Replay** of any Agent action shall be available within the SLA-Class Replay window on the Buyer's request, the Buyer's regulator's request, or the Agency's own dispute review.

3.5 The Buyer shall have read access to the Audit Log for its tenants at all times during the term and for the retention period thereafter.

## 4. Kill-Switch SLA

4.1 The Agency operates a **Kill-Switch** capable of suspending the Agent within the SLA-Class time-to-stop on authorised command.

4.2 The named authority chain (with after-hours coverage), the drill cadence (quarterly minimum), and the drill log are set out in the Trust and Compliance Annex.

4.3 The Kill-Switch may be invoked by: (i) the Buyer's named officers; (ii) the Agency's Agent Safety Lead; (iii) a regulator with jurisdiction.

4.4 The Kill-Switch SLA remains in force during Upstream Model-Provider Force-Majeure.

## 5. Sub-Cap for Irreversible-Action Liability

5.1 Notwithstanding the general liability cap in clause [X] of the MSA, the Agency's liability for an **Irreversible-Action Incident** at the Agency's fault shall be capped at the lower of:

(a) the value of the action; and
(b) twelve (12) months of fees paid by the Buyer under the engagement giving rise to the Incident,

(the "Sub-Cap"),

except where the cause is the Agency's gross negligence, wilful misconduct, or breach of the named obligations in clauses 2 (Action Accountability), 4 (Kill-Switch SLA), or 7 (Agent-Identity Warranty), in which case the general cap in clause [X] of the MSA applies.

5.2 The Sub-Cap does not affect indemnity for third-party claims arising from an Agency-fault Irreversible-Action Incident, which operates above the Sub-Cap up to the general cap.

## 6. Fee-for-Evidence-Pack on Dispute

6.1 On the Buyer's request for a forensic Evidence Pack outside the routine Monthly Statement (typically because of a dispute, an incident, or a regulator inquiry), the Agency shall produce the Evidence Pack within the agreed SLA window.

6.2 The Agency shall produce up to **two (2) Evidence Packs per calendar year** at no additional cost.

6.3 Beyond the included allowance, the Agency may charge a documented Evidence-Pack Fee at standard professional rates. The rate card is set out in the Pricing Exhibit.

6.4 Evidence Packs required because of an Agency-fault Irreversible-Action Incident shall be produced at the Agency's cost.

## 7. Agent-Identity Warranty

7.1 The Agency warrants that every external communication initiated by the Agent (including but not limited to email, chat, voice call, ticket, posted message, and regulatory filing) discloses the Agent's identity in line with applicable rules, including:

(a) Article 50 of Regulation (EU) 2024/1689 (the AI Act) where applicable;
(b) the Buyer's regulator's transparency-to-affected-party rules;
(c) the Agency's Responsible-AI Agent Commitment.

7.2 The Agency warrants that the Agent will not impersonate a named human, will not claim authority it does not have, and will route to a Named Human for actions outside the Action Catalogue.

7.3 Breach of this warranty by the Agent constitutes a material breach of this Addendum.

## 8. Intervention SLA and Supervisor Cost Allocation

8.1 The Agency commits to the Intervention SLA — time-to-human escalation — at the SLA-Class threshold (SLA Exhibit, clause 3).

8.2 The supervisor cost the Buyer retains (people on the oversight queue, on-call, escalation engineer) is the Buyer's cost.

8.3 The Intervention Credit Clause in the Pricing Exhibit (clause 4) reduces the Unit Fees when the Intervention Rate exceeds the Ceiling, compensating the Buyer for retained supervisor cost.

## 9. Sub-Processors (Model Providers and Tool-Call APIs)

9.1 The Sub-Processor list for the Agent is set out in Annex [SP-1] and shall identify, for each Sub-Processor: name, role (model inference, tool-call API, vector store, compute), region of processing, retention default, training-data posture, contractual notice, and fallback Sub-Processor.

9.2 Changes to the Sub-Processor list shall be notified to the Buyer not less than thirty (30) days in advance. The Buyer may object within twenty (20) days; the parties shall in good faith identify an alternative.

9.3 The Buyer accepts that the Agency cannot remove a Sub-Processor without engineering and eval lead-time. The change-window shall reflect this.

## 10. Model-Provider Force-Majeure

10.1 Where a named upstream model-provider Sub-Processor declares an outage of the relevant model family for more than thirty (30) consecutive minutes, the corresponding SLA metrics in clauses 2 and 4 of the SLA Exhibit are suspended for the affected window.

10.2 The Agency commits to multi-provider fall-back where the Buyer has accepted the Model-Routing Policy variation (Annex [MR-1]). Otherwise, the Buyer accepts the single-provider exposure.

10.3 Force-Majeure does not relieve either party of the obligation to pay undisputed fees up to the date of the event.

10.4 The Kill-Switch SLA and the Audit-Log Completeness SLA remain in force at all times, including during Model-Provider Force-Majeure.

## 11. Insurance

11.1 In addition to the insurances required under the MSA, the Agency shall maintain Professional Indemnity Insurance covering claims arising from the Agent's actions for a minimum of [$ ] per claim and [$ ] aggregate per year.

11.2 The Agency shall maintain Cyber Liability Insurance covering data, regulatory, and recovery costs for a minimum of [$ ] per claim and [$ ] aggregate per year.

11.3 Certificates of insurance shall be made available to the Buyer on request.

## 12. Regulator Cooperation

12.1 Where a regulator with jurisdiction over the Buyer makes an inquiry or issues an order relating to the Agent, the Agency shall: (i) cooperate in good faith; (ii) provide the requested Audit Log access and Evidence Packs without delay; (iii) participate in joint review where the Buyer requests.

12.2 Where the regulator's order requires the Agent to pause, the Kill-Switch shall be invoked.

12.3 Where the regulator's order requires modification of the Action Catalogue, the parties shall in good faith implement the modification within the regulator's timeframe.

## 13. Termination Specific to the Agent

13.1 In addition to the termination rights in the MSA and the SLA Exhibit, the Buyer may terminate the Agent's Statement of Work on any of the Refund Triggers in the Pricing Exhibit (clause 7).

13.2 On termination of the Agent's Statement of Work, the Agency shall:
(a) invoke the Kill-Switch on the Agent's actions in the Buyer's tenancy;
(b) remove the Agent's identity and scope from the Buyer's systems;
(c) hand over the Audit Log per clause 3;
(d) return Buyer data per the DPA;
(e) cooperate in the wind-down per the Pricing Exhibit clause 7.5.

## 14. Survival

14.1 Clauses 3 (Audit Log Retention), 5 (Sub-Cap for Irreversible-Action Liability), 7 (Agent-Identity Warranty), 12 (Regulator Cooperation), and 13.2 (Termination wind-down) survive termination of this Addendum.

## 15. Order of Precedence

15.1 In the event of conflict regarding the Agent: (i) this Addendum; (ii) the SLA Exhibit; (iii) the Pricing Exhibit; (iv) the Trust and Compliance Annex; (v) the MSA.

---

**SIGNED** for and on behalf of **[BUYER]**:

Name: ____________________
Title: ____________________
Date: ____________________

**SIGNED** for and on behalf of **[AGENCY]**:

Name: ____________________
Title: ____________________
Date: ____________________

---

## Annexes Referenced

- Annex [Z] — Action Catalogue (Pricing Exhibit)
- Annex [NA-1] — Named Approvers
- Annex [SP-1] — Sub-Processor List
- Annex [MR-1] — Model-Routing Policy
- Trust and Compliance Annex
- SLA Exhibit
- Pricing Exhibit
- DPA
