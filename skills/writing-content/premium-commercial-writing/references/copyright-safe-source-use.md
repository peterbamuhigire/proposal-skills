# Copyright-Safe Source Use

Parent skill: [Premium Commercial Writing](../SKILL.md).

**When to read:** whenever books, EPUBs, PDFs, articles or other copyrighted sources inform a skill, reference or client deliverable. This file sets how such sources may be used in this repository and in proposals.

## Hard repository rule (owner decision, 2026-09-23)

Book extractions, book summaries, chapter reconstructions, OCR output and raw books must **never** be stored in this repository. There is no `book-extractions/` folder. Knowledge from a book lands only as task-oriented guidance inside `SKILL.md` files and `references/` files (procedures, checklists, templates, phrase banks, decision rules) written for the task and not organised as a summary of the book. The source is cited briefly (author, year, title, publisher) where a method comes from it. `scripts/source_ingestion_guardrail.py` enforces the folder rule.

## Permitted use

- Identify durable concepts, procedures and practical principles.
- Convert them into original, operational guidance in this engine's own style and structure.
- Write original slot-templates and examples, localised to the engine's markets.
- Quote verbatim only rarely, at 25 words or fewer, with attribution, and only where the exact phrase is the value.
- Treat every statistic, price, platform fact, law or benchmark from a book as unverified: admit it only through the currentness register or a verified primary source, otherwise phrase it as a check.

## Prohibited use

- Single-book digests: a reference organised around one book, or reproducing a book's lists in its sequence with its item titles, its case studies or near-verbatim text.

- Copying protected text into repository files or client deliverables.
- Long paraphrases that preserve a source's sequence, examples or distinctive language.
- Reproducing tables, figures or named proprietary frameworks as substitutes for the original work; trademarked method names are cited, not repackaged as templates.
- Implying that the repository holds source-authorised excerpts.
- Storing working notes from a book inside the repository; keep them outside and discard them after the skill work.

## Premium-writing synthesis themes (general, source-independent)

- Reader-first structure: start with the decision, problem or answer.
- Argument discipline: claim, mechanism, evidence, control and implication.
- Commercial clarity: connect value, risk, quality and price.
- Narrative logic: current state, complication, proposed answer, proof and next step.
- Proof-based persuasion: outcomes, examples, constraints and trade-offs.
- Editorial polish: concise sentences, concrete nouns, strong headings, no unnecessary words.
- Discoverability: public content matches reader intent, entity clarity and answer-first structure.

## Acceptance checklist before adding source-informed material

- [ ] No copied or closely paraphrased source text is present.
- [ ] The guidance is organised by task, not by the book's chapters.
- [ ] The repository text is useful without access to the source.
- [ ] Volatile claims are registered, verified or phrased as checks.
- [ ] The source is cited briefly where a method comes from it.
- [ ] The material strengthens an existing workflow rather than duplicating another skill.
- [ ] `python -X utf8 scripts/source_ingestion_guardrail.py` passes.
