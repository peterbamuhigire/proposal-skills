# Core Rules — Proposal Engine

> Distilled from this engine's own `AGENTS.md`.

## Kaizen quality gate: 65/100 to publish, 95/100 is the target

Every audited deliverable in this engine is capped at 65/100 for publication
readiness and every improvement plan targets 95/100, with evidence and a
re-audit date. A deliverable below 65 does not ship; one between 65 and 95 ships
with the gap and its remediation plan stated, not silently.

*Full audit workflow:* `skills/meta/kaizen-improvement-system`.

## Never infer a tender's evaluation criteria from a past, similar tender

Mandatory requirements, scoring weightings, and compliance thresholds are
specific to the issuing tender document. A past tender from the same sector or
even the same client is evidence to check against, never a substitute for
reading the current one.

*Applies the same principle as `intent-driven-development` Rule 2 (ECC audit,
report 02, §3.2): a repository — or here, a past submission — tells you how
things went last time, not what the current evaluator requires.*

## Each `SKILL.md` is the execution contract; `references/` loads only when needed

Treat the skill file as authoritative and complete for the task at hand.
Reference material exists for depth, not as a substitute for reading the
skill first.
