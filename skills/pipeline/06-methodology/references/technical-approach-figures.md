# Technical-Approach Figures Reference

[Owning skill](../SKILL.md)

Use when an ICT, systems-integration or consultancy proposal answers evaluation criteria that score the technical approach and methodology. Two formal figures let an evaluator see the proposed solution and the delivery sequence at a glance. Skip figures for pure advisory bids where a figure adds nothing the text does not already say.

Figure approach follows the diagram IR and render-evidence pattern adapted from Archify (MIT, https://github.com/tt-a1i/archify, commit 0e4949f910a8e390bd3b4933883a4dcabad571be) as implemented in srs-skills (M10-07). Paraphrased.

## The two figures

| Figure | Content | Authoring form |
|---|---|---|
| Figure 1: Proposed solution context | The client organisation, the proposed system, external systems (for example URA EFRIS, a mobile-money gateway, NIRA) and user groups; every interface labelled with its mechanism (REST API, signed webhook, file exchange, agreed interface) | Diagram IR, kind `context`; roles `system`, `person`, `external_system`; the client organisation as a boundary |
| Figure 2: Delivery workflow | Phases, approval gates and hand-overs exactly as the methodology text states them. For an ERP bid: discovery, posting-rule design, configured prototype, migrated-data rehearsal, UAT, cutover and first close, each with its finance-owner gate | Fenced Mermaid `flowchart LR` with `%% alt:` and `%% caption:` lines, or diagram IR kind `dataflow` when data stores and external parties matter |

Rules for the IR:

- Leave `trace` empty on every element: a proposal has no requirement registry, and `trace` accepts registry identifiers only.
- When the proposal answers a numbered terms-of-reference list, cite the ToR clause numbers in the caption as plain text (for example "Proposed solution context (ToR 3.1–3.4)"), never in `trace`.
- Put the proposal's own numeric section (for example `4.1`) in `meta.srs_section` and `evidence.srs_section`; the field requires a number.
- Keep labels in sentence case and the figure consistent with the prose: a phase, gate or interface that appears in only one of them is a compliance defect.
- A workflow of more than about seven steps drawn left to right shrinks below legible size at the body measure; split it into two figures or two rows so labels stay at 8 pt or more at the placed width.

## Presentation

- Caption below the figure, numbered by the build; alt text of at least one full sentence saying what the figure shows.
- Width to the body measure; PNG at 300 ppi or more plus SVG.
- Labels in Public Sans, the formal-document label face set by the design engine's `diagram-visual-standards.md` (`design-system-skills/skills/13-presentations-and-documents/docx-report-and-document-formatting/references/`). No monospace for whole labels, no Archify HTML or fonts, no Mermaid default styling.
- The figure manifest (`<OutputName>.figures.json`) stays with the proposal working files as evidence; it is not submitted to the client.

## Figure rendering hand-off

**Figure rendering hand-off.** Figures are rendered by the SRS engine, which owns the renderer, the diagram IR and the figure manifest; this engine holds no rendering code and must not copy any. Resolve the owning engine from `chwezi-engine-agents/catalog/engines.yaml` (entry `id: srs-skills`, `path: srs-skills`; on the reference host `C:\wamp64\www\srs-skills`) and run every command from that folder. *Inputs:* a working folder containing an `_context/` directory (a one-line brief is enough) and a document directory of Markdown section files. Each figure is either a diagram-IR file at `<doc-dir>/diagrams/<name>.ir.json`, embedded with `<!-- diagram-ir: FIG-nnn -->` (IR fields `meta.srs_section` and `evidence.srs_section` take the numeric section of this document), or a fenced Mermaid block carrying `%% alt:` and `%% caption:` lines. *Commands:* for IR figures, `python -X utf8 -m engine diagrams validate <folder> --doc <doc-dir>` then `python -X utf8 -m engine diagrams generate <folder> --doc <doc-dir>`; then `bash scripts/build-doc.sh <doc-dir> <OutputName>`, which renders every figure through `scripts/render_diagrams.py`, builds the `.docx` with Pandoc and the SRS reference template, fails if Mermaid source survives (`scripts/check_docx_diagrams.py`) and writes the figure manifest; finally `python -X utf8 -m engine diagrams verify-manifest <doc-dir>`. Give paths relative to the SRS engine folder or as Windows paths: MSYS-style `/c/...` paths stop Pandoc finding the figures. *Outputs:* PNG at 300 ppi or more at the 6.25 in body measure plus SVG under `<doc-dir>/_figures/`; numbered captions ("Figure N — caption") with alt text in the Word image description; `_figures/render-manifest.json`; and `<OutputName>.figures.json` beside the `.docx`. *Font check:* every figure's `font_substitution_check` in the figure manifest must read `PASS` (labels in Public Sans under the design engine's `diagram-visual-standards.md`); `FAIL` or `NOT_ASSESSED` means the figure is not delivered. *Other document workflows:* when the document is assembled another way (for example with the docx skill), run `python -X utf8 scripts/render_diagrams.py --doc-dir <doc-dir> --name <OutputName> --out <stitched.md> <files>` for the figures only, insert the PNGs with their captions and alt text, then run `python -X utf8 scripts/check_docx_diagrams.py <file.docx>` and `python -X utf8 -m engine diagrams manifest --doc-dir <doc-dir> --name <OutputName> --docx <file.docx>`. *Degraded mode:* if the SRS engine, its Node renderer, Chrome or Edge, or Pandoc is unavailable, no figure is promised: describe the content in prose and a table, state that figures were not produced, record the render and font checks as `NOT_ASSESSED`, and never paste diagram source into the deliverable.

## Checks before release

- [ ] Two figures present, numbered and captioned, each with alt text.
- [ ] `word/document.xml` of the built `.docx` contains no diagram source (`flowchart`, `graph TD`, `C4Context`); the build guard reports 0.
- [ ] Every figure's `font_substitution_check` is `PASS`; `verify-manifest` passes.
- [ ] Figure content matches the methodology text phase for phase and interface for interface.
