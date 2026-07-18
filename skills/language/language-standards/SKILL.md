---
name: language-standards
description: Use when proposal content must be written or reviewed in British East African English, Francophone African French, or standard East African Kiswahili; use east-african-english for English-only tone work.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Language Standards
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Select and enforce one declared language standard while preserving procurement meaning, proposer voice, and culturally appropriate professional register.

<!-- dual-compat-start -->
## Use When

- Draft, translate, or review proposal content in English, French, or Kiswahili.
- Reconcile multilingual terminology, dates, numbers, courtesy, headings, or calls to action.

## Do Not Use When

- Use `east-african-english` for English-only tone and idiom work that does not need multilingual routing.
- Do not translate legal, statutory, technical, or procurement terms without a verified source or qualified reviewer.

## Inputs

| Artefact | Source/provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Source text and target language | Proposal lead or client | Yes | Stop translation until both are explicit. |
| Approved terminology, names, and mandatory form wording | Client forms, ToR, glossary, verified source | Conditional | Preserve source wording and flag the term for review. |
| Proposer profile and country context | `profiles` and `sectors` | Yes for proposal drafting | Do not infer voice, dialect, or institutional title. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Language-conformant proposal text | Evaluator and proposal editor | Meaning, names, figures, register, spelling, and declared language convention remain consistent. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Language review record | Proposal release owner | Language, locale, unresolved terminology, and reviewer-required items are recorded. |

## Capability Contract

Read and search are required. Editing is allowed only for authorised drafting or language correction. External translation services, network verification, publishing, certification of translation, and submission require explicit authority.

## Degraded Mode

Fallback: when a qualified reviewer, approved glossary, source wording, or verification capability is unavailable, return the narrowest useful qualified translation, mark affected terminology `not assessed`, and do not certify accuracy.

## Decision Rules

| Condition or choice | Action | Failure or risk avoided |
|---|---|---|
| English for Uganda, Kenya, Tanzania, or regional procurement | Use British spelling and the East African professional register | Imported US usage or unnatural tone |
| French for Francophone African institutions | Use formal French and preserve official programme terminology | Literal English-to-French phrasing |
| Kiswahili for formal East African communication | Use standard formal Kiswahili and verify specialist terms | Colloquial or mixed-register output |
| Mandatory wording exists in the buyer's form | Reproduce it exactly and flag any apparent inconsistency | Non-compliant paraphrase |

## Workflow

1. Identify the source language, target language, audience, country context, and mandatory wording.
2. Select the matching section of the multilingual guide and establish approved terminology.
3. Draft or review for meaning before polishing grammar, courtesy, spelling, dates, and numbers.
4. Stop when a legal, statutory, technical, or procurement term cannot be verified.
5. Recover by retaining the source term, flagging it for a qualified reviewer, or narrowing the output.
6. Run a consistency pass across headings, tables, repeated terms, figures, and calls to action.

## Quality Standards

- Translation preserves obligation, qualification, uncertainty, price, date, and named-entity meaning.
- Tone is formal and natural for the declared locale, without machine-translation residue or invented cultural claims.

## Anti-Patterns

- Mixing British and American spelling in one proposal. Fix: select the declared standard and run a consistency pass.
- Translating an official programme name freely. Fix: use the buyer's published wording.
- Using conversational Kiswahili in a formal tender. Fix: apply standard professional register and verify specialist terms.
- Copying English sentence structure into French. Fix: recast the sentence naturally without changing its obligation.
- Certifying a translation without a qualified reviewer. Fix: mark reviewer-dependent accuracy not assessed.

## Worked Example

For a Ugandan technical proposal, write “programme”, “organisation”, and “mobilisation”, retain the client's exact project title, and format the date as “13 July 2026”. If the same bid requires a French annex, translate the narrative but preserve official acronyms and price figures exactly.

## References

- [Multilingual language guide](references/multilingual-language-guide.md)
- [English-only East African standard](../east-african-english/SKILL.md)
- [Proposer profile router](../../profiles-sectors/profiles/SKILL.md)
<!-- dual-compat-end -->
