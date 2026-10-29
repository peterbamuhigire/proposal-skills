# Proposal engine October Kaizen report

The critical current-form mismatch is fixed: deliverable planning, expert
inputs, conduct and SEA/SH declarations now map to the inspected World Bank
RFP, and the invented FIN-5 is excluded. The engine also enforces hard package
and checkout capacity, reports routing metrics accurately and checks dated
source review records. These improvements do not make a synthetic bid ready
for submission. **The target of 95 is not achieved.**

The baseline was frozen at `8eddd70` before implementation. Scores below are
reviewer judgements (inference), not measured bid-win probabilities. Each row
uses the same ten Standard dimensions; the baseline's /10 ratings are shown
here on a /100 scale.

| Dimension | Before | After | Evidence and remaining deficiency |
|---|---:|---:|---|
| Doctrine | 70 | 70 | Tender-specific requirements retained; legal/project authority absent |
| Taxonomy and routing | 50 | 55 | First-rank and owned negatives measured; one exposed FTP collision remains |
| Skill depth | 60 | 65 | Correct current form guide; wider framework depth not exercised |
| Applied proof | 40 | 50 | Three form regressions and rendered synthetic pack; no real-bid evaluator |
| Standards currency | 40 | 50 | Scoped register and expiry gate; legal amendments/other editions incomplete |
| Output readiness | 50 | 60 | Correct form/envelope mechanics; credentials and signatures absent |
| Accessibility and inclusion | 40 | 40 | Font correction only; no accessibility certification or user study |
| Production and handoff | 50 | 55 | Native install and release guards; actual submission receipt absent |
| Hygiene | 70 | 75 | Hard cap and portable router; complete external semantics unassessed |
| Safety and integrity | 60 | 65 | Stale forms refused and unsupported scoring assumptions removed; live legal proof absent |

Raw **53 → 58.5**. Standard capped: `min(53,65)=53` → `min(58.5,65)=58.5`.
Separate user initial cap: `min(53,45)=45`. The raw evidence is preserved;
no score is artificially promoted to 95 or reduced to hide the baseline.

Kept commits: P1 `5a4e39e` (form crosswalk); P2 `4066815` (hard packaging gate);
P3 `feea230` (routing measures); P4 `be2c774` (scoped currentness). Each was
followed by the registered checks; no experiment was reverted. Subsequent
documentation records final native/render review. See
[validation](04-validation-record.md) and [experiment log](03-experiment-log.md).
All dimensions are equal or better. Original routing outcomes are preserved;
first-rank proportion improves from 19/26 to 23/31. Any missing mandatory live
bid requirement remains a release blocker regardless of score.
