---
name: submission-proof-and-receipt-discipline
description: Use when a tender, EOI, or proposal submission has a deadline and a formal receipt requirement, to fix the exact submitted state, prove what was sent, when, to whom, and hold the confirmation; use the relevant submission checklist (e.g. giz-eu-local-procurement-response) for the mechanical pack checks this skill assumes are already done.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Submission Proof and Receipt Discipline
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178. Discipline distilled from the ECC skill engine's `skills/operator-approval-loop/SKILL.md` — the receipt-and-proof principle only, not its hashing/epoch/claim-token database mechanism, which is scoped for an always-on agent dispatching live messages and is not warranted for this engine's document-authoring workflow. See Degraded Mode and the note at the end of this file for the scoping reasoning.

<!-- dual-compat-start -->
## Use When

- A tender, EOI, or proposal has a hard deadline and a portal, email, or physical submission channel that issues (or should issue) a formal receipt, timestamp, or acknowledgement.
- More than one person or file version could plausibly be "the one that was submitted," and a dispute, clarification request, or evaluator query later needs an unambiguous answer to what was sent.
- A buyer's procurement rules (GIZ AVB, PPDA, EU/BMZ, AfDB, World Bank, or similar) make late or mismatched submissions grounds for disqualification, so the proof of timely, correct submission is itself part of compliance.

## Do Not Use When

- The deliverable has no deadline or formal receipt requirement (an internal draft, a discovery call follow-up).
- The mechanical pack checks (page limits, price tokens, template integrity) have not yet passed — run the relevant checklist first, e.g. `skills/domain-delivery/giz-eu-local-procurement-response/references/submission-pack-checklist.md`; this skill assumes the pack is already correct and is about proving what left the building, not about what should be in it.

## Required Inputs

| Artefact | Source/provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Final, gate-passed submission pack (technical + financial as applicable) | Bid team, after the relevant submission checklist and `bid-red-team-dual-review` where applicable | Yes | The exact artefact this skill proves was sent | Stop; do not fix a state that has not passed its own gates |
| Submission channel and its receipt mechanism (portal confirmation, email read/delivery receipt, courier waybill, hand-delivery stamped acknowledgement) | ToR/RFP submission instructions | Yes | Determines what "proof" looks like for this tender | Stop and confirm the channel before the deadline, not after |
| Deadline (date, time, timezone) as stated in the ToR/RFP or the latest approved clarification/addendum | Buyer documents | Yes | Anchors the timeliness claim | Do not infer from a similar past tender — see `rules/common/core.md` |

## Workflow

1. **Fix the submitted state before sending.** Record a content fingerprint of the exact final files: file names, sizes, and a checksum (e.g. `sha256sum` or the OS-native equivalent) for each file in the submission pack. This is the artefact-level equivalent of hashing a draft — cheap, and it settles "which version did we actually send" disputes without needing a database.
2. **Record the who and how.** Note who performed the submission action, the exact channel used (portal account, email address and subject line, courier and tracking number, or the person who hand-delivered), and the destination address/portal exactly as specified in the ToR/RFP.
3. **Submit inside the deadline with margin.** Treat the buyer's stated deadline as fixed and jurisdiction/timezone-specific; do not assume your local clock matches the buyer's stated timezone. Submitting close to the deadline increases the cost of any receipt failure (Step 5) because there is no time left to retry.
4. **Capture the receipt at the moment of submission, not after.** Portal confirmation screen/number, email delivery or read receipt, courier waybill, or a signed and stamped hand-delivery acknowledgement. If the channel does not auto-issue one, request one explicitly and do not treat silence as delivery.
5. **Reconcile fingerprint, receipt, and deadline into one record.** One line per submission: file fingerprints, submitter, channel, destination, timestamp, deadline, and receipt reference. This is the durable answer to "what did we submit, when, to whom, in what state" if it is ever questioned.
6. **Hold the receipt outside the file that can be silently replaced.** Keep the receipt (screenshot, confirmation email, waybill scan) as its own artefact, not only as a note inside the proposal file, so a later edit to the proposal folder cannot alter the evidence of what was actually sent.
7. **If no receipt arrives**, escalate before the deadline passes, not after: retry the channel, use a documented fallback (alternate email, phone confirmation), and if the deadline is missed by a channel failure, retain every artefact (timestamps, error messages, correspondence) that could support a clarification or protest.

## Decision Rules

| Condition | Action |
|---|---|
| Submission channel does not auto-issue a receipt | Request one explicitly before treating the submission as complete |
| No receipt received and deadline is approaching | Escalate immediately through a documented fallback channel; do not wait silently |
| More than one file version exists for the same submission | Reconcile to one fingerprinted set before submitting; do not submit an unreconciled pack |
| Deadline timezone is ambiguous in the ToR/RFP | Treat the more conservative (earlier) reading as binding and confirm via the clarification protocol if time allows |
| A dispute or clarification later questions what was submitted | Produce the fingerprint + receipt record; never reconstruct "what we probably sent" from memory or the current state of the working folder |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Submission proof record (fingerprint, submitter, channel, destination, timestamp, deadline, receipt reference) | Bid lead, signatory, and any later dispute/clarification process | One record per submission, complete before the deadline closes |
| Retained receipt artefact, stored separately from the editable proposal folder | Bid lead | Cannot be altered by later edits to the proposal working files |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| File checksums for the exact submitted pack | Bid lead, any later reviewer | Matches the files as sent; regenerable and independently verifiable |
| Receipt (portal confirmation, delivery/read receipt, waybill, signed acknowledgement) | Bid lead, buyer-facing correspondence | Timestamped and attributable to the specific submission, not a general "we sent something" claim |

## Capability Contract

Read, search, and running a checksum command are required. Sending the submission itself, and any related buyer correspondence, requires the same explicit authority already required by the pipeline and domain-delivery skills — this skill does not grant submission authority, it disciplines the proof once authority has been exercised.

## Degraded Mode

If the channel offers no receipt mechanism at all (e.g. a bare email with no read receipt available), the fingerprint plus a timestamped copy of the sent email (headers included) is the minimum acceptable record — state explicitly that no third-party receipt exists, rather than silently treating the send as proven delivery.

## Domain Anti-Patterns

- Treating "I clicked submit" as proof, with no fingerprint or receipt retained.
- Storing the only copy of the receipt inside the same folder that keeps getting edited after submission.
- Submitting minutes before a deadline with no time buffer to recover from a channel failure.
- Assuming the buyer's stated deadline is in the proposer's local timezone without checking.
- Reconstructing "what we submitted" from the current working files instead of the fingerprinted record, after the fact.

## Scoping note: why this is not a port of operator-approval-loop's mechanism

ECC's `operator-approval-loop` solves a different problem: an always-on agent that drafts outbound messages to counterparties and must not send without a human-approved, tamper-evident, exactly-once-attempted dispatch, with concurrent workers, claim tokens, and epoch-keyed decisions to prevent stale or duplicate sends. A proposal engine does not dispatch messages autonomously and has no concurrent-worker race condition to guard against — a human submits a tender through a portal, email, or courier, once, at a known deadline. What transfers is the underlying discipline ECC's mechanism exists to serve: fix the exact state before it goes out, prove who sent it and when, and hold a receipt that cannot be quietly rewritten. That discipline is what this skill captures. The hashing, epoch rotation, claim-token database, and dispatch-worker reconciliation are infrastructure for a problem (concurrent automated dispatch) this engine does not have, so porting them here would add mechanism without adding assurance.
