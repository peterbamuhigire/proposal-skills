# AI-Agent Success-Definition Language

Library of precise outcome / resolution / step / action definitions for agentic commercials, each with one counter-example. Pairs with `../ai-agent-success-fee-and-outcome-pricing/SKILL.md` and `ai-agent-outcome-pricing-clauses.md`.

The counter-example rule: every definition must identify at least one event that looks like success but is excluded. If the definition cannot exclude that event, redraft.

---

## A — Resolution Definitions

### A.1 Customer-Support Resolution

> **Resolution** means the closure of a Buyer ticket by the Agent where the ticket is not reopened, escalated, or re-worked by a human within thirty (30) calendar days of closure.
>
> **Counter-example.** A ticket auto-closed by inactivity (no customer reply for the system's default inactivity window) is **not** a Resolution.
>
> **Counter-example.** A ticket closed and reopened within 30 days with a different reason code is **not** a Resolution.
>
> **Evidence.** Audit Log entry showing Agent close action; ticket status confirmation at day 31.

### A.2 Insurance Claims Triage Closure

> **Triage Closure** means the Agent's assignment of a claim to a workflow lane (fast-track, standard, investigate) where the human adjuster does not override the lane within seventy-two (72) hours of assignment.
>
> **Counter-example.** A claim re-triaged because of new information from the claimant is **not** an Agent failure (it counts as a Triage Closure).
>
> **Counter-example.** A claim where the human adjuster overrides the lane within 72 hours is **not** a Triage Closure.
>
> **Evidence.** Audit Log entry showing Agent triage action; claim-system lane confirmation at hour 72.

### A.3 Debt-Collection Promise-to-Pay (PTP)

> **PTP** means the Agent's logging of a customer commitment to pay an amount on a date, where the commitment is honoured within fourteen (14) calendar days of the committed date.
>
> **Counter-example.** A PTP that is renegotiated by the customer (new amount or date) within 7 days is **not** a PTP (it is logged separately as a renegotiation event).
>
> **Counter-example.** A PTP that is rescinded by the customer is **not** a PTP.
>
> **Evidence.** Audit Log; payment-system reconciliation at day 14 of the committed date.

---

## B — Outcome Definitions

### B.1 Recovered Debt

> **Recovered Debt** means a payment received by the Buyer in respect of an account in arrears that the Agent contacted during the relevant period, where the payment is not subject to Reversal within thirty (30) calendar days of receipt.
>
> **Counter-example.** A payment received and then reversed (chargeback, court-ordered repayment, originating-bank reversal) within 30 days is **not** Recovered Debt.
>
> **Counter-example.** A payment received from an account the Agent did not contact in the period is **not** Recovered Debt attributable to the Agent.
>
> **Evidence.** Audit Log of Agent contact; payments-system reconciliation at day 30; chargeback report.

### B.2 Saved ARR (Churn Save)

> **Saved ARR** means the annual recurring revenue of a Buyer customer who indicated intent to cancel (verified in the system of record) and who remained an active paying customer for ninety (90) days after the Agent's save intervention.
>
> **Counter-example.** A customer who cancelled within 90 days of the save intervention is **not** a Saved ARR.
>
> **Counter-example.** A customer who reduced spend by more than 50 % within 90 days is **not** a full Saved ARR (the saved ARR is pro-rata to the reduced spend).
>
> **Evidence.** Audit Log of Agent save action; billing-system status at day 90.

### B.3 Renewed Policy

> **Renewed Policy** means an insurance policy that was up for renewal in the relevant period and was renewed by the customer, where the Agent's intervention is logged in the renewal journey and the customer paid the first premium of the renewal term.
>
> **Counter-example.** A policy renewed and then cancelled within the cooling-off window is **not** a Renewed Policy.
>
> **Counter-example.** A policy renewed but with the first premium unpaid at day 30 is **not** a Renewed Policy.
>
> **Evidence.** Audit Log; policy-management system; payment confirmation.

### B.4 Fraud-Loss Reduction

> **Fraud-Loss Reduction** means the verified reduction in monthly Fraud Loss versus the Baseline Fraud Loss Rate (Annex [FL-1]), confirmed by the Buyer's risk function quarterly.
>
> **Counter-example.** A month in which a non-Agent change (rule-engine update, policy change, fraud-pattern shift outside the Agent's scope) is the dominant factor is **not** Agent-attributable.
>
> **Evidence.** Audit Log; risk-function confirmation; baseline reconciliation.

---

## C — Step / Action Definitions

### C.1 Step (Tool Call)

> **Step** means an invocation by the Agent of a tool, an external API, a system write, an outbound communication, or a parameter-bound function call, as logged in the Audit Log.
>
> **Counter-example.** An internal reasoning step that does not invoke a tool, write to a system, or initiate a communication is **not** a Step (it is part of the Agent's planning).
>
> **Counter-example.** A retry of a failed Step within the configured retry policy is **one** Step, not multiple.
>
> **Evidence.** Audit Log entry per Step.

### C.2 Action (System Write)

> **Action** means a Step that changes state in a system of record (creates, updates, or deletes a record) or initiates an external effect (sends a message, executes a transaction, raises a ticket on a third-party system).
>
> **Counter-example.** A read-only tool call (lookup, query) is **not** an Action (it is a Step).
>
> **Counter-example.** A draft created and held for human approval is **not** an Action until the human approves it.
>
> **Evidence.** Audit Log; system-of-record reconciliation.

---

## D — Agent / Persona Definitions

### D.1 Citizen-Service Agent

> **Citizen-Service Agent** means a single configured Agent persona dedicated to handling citizen requests of a defined Action Catalogue, with named oversight, named kill-switch authority, and a configured volume envelope, operated on a calendar-month basis.
>
> **Counter-example.** A copilot used by named officers to assist their own work is **not** a Citizen-Service Agent.
>
> **Counter-example.** A workflow automation with deterministic rules and no LLM-based planning is **not** a Citizen-Service Agent.

### D.2 Support Agent

> **Support Agent** means a single configured Agent persona dedicated to handling customer enquiries, with an included monthly Resolution allowance and an oversight queue, operated on a calendar-month basis.

---

## E — Reversal Events (Cross-Outcome)

A Reversal Event undoes an Outcome. The standard Reversal Events are:

- **Chargeback** — the customer's bank reverses the payment.
- **Refund** — the Buyer refunds the customer (full or partial).
- **Complaint upheld** — the Buyer's complaints function or an external ombudsman upholds the customer's complaint in respect of the Agent-touched interaction.
- **Ticket reopen** — the ticket is reopened by a customer or by a human agent.
- **Policy cancellation** — the policy is cancelled within the cooling-off window or within 90 days for retention-attributed renewals.
- **Court-ordered repayment** — a court orders repayment to the customer.
- **Risk reclassification** — the Buyer's risk function reclassifies an event after the fact.

Each Outcome Definition should name the Reversal Events that apply and the Reversal Window.

---

## F — Counter-Example Catalogue (Common Mistakes)

| Outcome | Looks like success but is not | Why |
|---|---|---|
| Resolution | Ticket auto-closed by inactivity | The customer didn't reply; the Agent didn't resolve |
| Resolution | Ticket closed and reopened with different reason | The underlying issue was not resolved |
| Recovered debt | Payment received and reversed within 30 days | Reversal undoes the outcome |
| Saved ARR | Customer cancelled within 90 days | The save did not hold |
| Renewed policy | First premium unpaid | The renewal is incomplete |
| Triage closure | Adjuster overrides lane within 72 hours | The Agent's triage was wrong |
| PTP | Promise rescinded by customer | The PTP did not hold |
| Fraud-loss reduction | Month dominated by non-Agent factor | Not attributable to Agent |
| Step | Internal reasoning step | Not a billable Step |
| Step | Retry within retry policy | Counts as one Step, not multiple |
| Action | Draft held for human approval | Not yet an Action |
| Action | Read-only lookup | A Step, not an Action |

---

## G — How to Build a New Definition (Procedure)

1. Name the unit (Resolution / Outcome / Step / Action / Agent).
2. State the criterion that triggers the unit.
3. State the cooling-off window (if applicable).
4. State the Reversal Events that exclude the unit.
5. Provide **at least one counter-example** that satisfies (2) but fails one of (3) or (4).
6. Name the evidence source (Audit Log + named system of record).
7. State the dispute window (typically 60 days).
8. State the attribution test (named in Annex [AT-1] of the Outcome-Pricing Clauses).

A definition that cannot survive the counter-example rule is not ready for contract.
