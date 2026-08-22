# Control-plane adoption

This engine adopts the shared ten-engine contract from
`C:\wamp64\www\skills-web-dev\docs\engine-control-plane.md`. Proposal
doctrine remains authoritative for bids, tenders, compliance, pricing,
delivery plans, and submission-ready document bundles.

## Local roles and commands

| Role | Responsibility | Required evidence |
|---|---|---|
| Proposal writer | Shape the evaluator journey, solution, method, and proof. | Draft mapped to the brief. |
| Compliance mapper | Reconcile every instruction, form, criterion, and mandatory attachment. | Requirement matrix. |
| Evaluator red-team | Score likely evaluator objections, contradictions, and unsupported promises. | Red-team findings. |
| Evidence auditor | Verify source, pricing, partner, personnel, and past-performance support. | Evidence register and exceptions. |

Route thin commands `bid-review`, `compliance`, `price-check`, and
`submission` to canonical proposal skills. No command may silently change a
commercial promise or submit an external package.

## Hook and release contract

- `preflight` captures solicitation version, deadline/time zone, submission
  channel, decision owner, and cross-engine obligations.
- `context` loads source register, compliance matrix, pricing basis, templates,
  clarifications, and approved differentiators.
- `before_write` checks scope, version, permissions, claims, pricing support,
  and impact on signed-off sections or attachments.
- `after_write` reruns scanners, anti-slop, compliance, source, document,
  spreadsheet, and render checks and records results.
- `release` requires requirement-matrix coverage, source and pricing support,
  red-team review, submission checklist, and final approval.
- `stop` preserves package version, missing inputs, deadline risk, open
  compliance findings, and the next owner.

Missing mandatory evidence or approval is `NOT ASSESSED` and blocks submission.

## Human approval adapter

Commercial and submission controls are detailed in
[`approval-enforcement.md`](approval-enforcement.md) and catalogued in
[`approval-adapter.json`](approval-adapter.json). The final package, recipient,
pricing, terms, and submission method must pass the shared gate.
