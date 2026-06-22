---
name: mind-submission
description: Use when running the final pre-submission preflight for Mind via ScholarOne — preparation for triple-anonymous review, the ~8,000-word limit, the 50–200-word abstract, line numbering, the one-article-per-12-months rule, file format, and the MIND house style. Final checks; it does not draft content.
---

# Submission Preflight (mind-submission)

The last check before submitting on **ScholarOne**. Mind is **triple-anonymous**, so the single most
common avoidable failure is a manuscript that is not properly prepared for anonymous review — such a
paper **will not be read**. Verify volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files / settings ScholarOne expects
- Confirming the word limit, abstract, line numbering, and anonymization are all in order

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** Mind Association / Oxford University Press.
- **Portal:** **ScholarOne** (`mc.manuscriptcentral.com/MIND`); submit in **Word or PDF**, with
  high-resolution image files sent at the same time.
- **Review model:** **triple-anonymous** across all papers — author identity is not revealed to
  editors or referees unless and until a paper is accepted; prepare for anonymous refereeing or it
  will not be read.
- **Scope / what they accept:** **quality is the sole criterion of publication, with no area, no
  style, and no school of philosophy excluded**. Content types: **articles, discussions (discussion
  notes), book reviews, and critical notices**.
- **Critical notices:** **longer than book reviews**, letting the author develop their own ideas in
  response to the book under discussion (distinct from a short book review).
- **Volume / competitiveness:** the journal **receives over 800 submissions each year** and draws on a
  large pool of expert referees, associate editors, and the Editorial Board. (Acceptance rate and
  time-to-first-decision are **not published** as fixed figures — 需复核.)
- **Length:** articles **no longer than around 8,000 words in total**; longer only in **exceptional
  circumstances** (e.g., very extensive quotations from original texts); symbol-heavy papers should
  paginate equivalently to an 8,000-word article. (Word limits for discussions / book reviews /
  critical notices are **not pinned** here — 需复核.)
- **Abstract:** published abstract **50–200 words**; a longer submission abstract (up to ~250 words,
  待核实) may be included to aid review.
- **Submission limit:** **no more than one article may be submitted by any corresponding author
  during any twelve-month period**.
- **Line numbering:** **required** for the review copy (LaTeX `lineno`; Word line-numbering option).
- **Style:** the **MIND Stylesheet / MIND house style** applies to the **accepted** final version;
  authors sign the **standard OUP copyright licence agreement** at acceptance.
- **Fee:** **no submission fee** (verified 2026-06-22). An **open-access option is available for a
  charge**, handled by OUP after acceptance; OUP sets the exact APC, eligible licences, and any
  read-and-publish / transformative-agreement waivers on its live charges page — confirm there.

## Triple-anonymous failure audit

Mind's anonymity rule is not a cosmetic check; an identifying manuscript may not be read. Run a
failure audit with three passes:

1. **Text pass.** Search for first-person self-citations, acknowledgements, grant numbers, conference
   versions, appendix URLs, and phrases like "in my earlier paper." Replace with neutral references
   where scholarly continuity still matters.
2. **File pass.** Strip document properties, PDF metadata, tracked-change names, embedded comment
   authors, and LaTeX build paths that reveal a username or institution.
3. **Argument pass.** Make sure anonymization did not make the paper evasive. Self-citations should
   remain intellectually honest, just not identity-revealing.

Record any unavoidable prior-work clue in a private submission note only if the portal requests it.

## Preflight checklist

### Type & length
- [ ] Content type chosen (article / discussion / book review / critical notice — critical notice is the *longer* book-engagement piece)
- [ ] Article ~8,000 words (or justified exception); symbol-heavy paper paginated equivalently
- [ ] Abstract within the stated length (published 50–200 words)
- [ ] Subject is in scope — quality is the sole criterion; **no area, style, or school of philosophy is excluded**

### Anonymity (triple-anonymous)
- [ ] No author names, affiliations, or revealing acknowledgements in the manuscript
- [ ] No self-identifying references ("as I argued in…"); self-citations neutralized
- [ ] Identifying **file metadata stripped** (document properties)

### Preparation & format
- [ ] **Line numbering** on the document (LaTeX `lineno` / Word)
- [ ] Word or PDF; high-resolution image files ready to upload at the same time
- [ ] Consistent citation style (full MIND house-style conversion at acceptance — see `mind-citation-and-style`)
- [ ] Alt text for figures; funding declared where applicable

### Eligibility & compliance
- [ ] Not in breach of the **one-article-per-12-months** corresponding-author rule
- [ ] Original, unpublished work; aware of the standard OUP copyright licence signed at acceptance
- [ ] No submission fee; if open access is wanted, the OUP charge (APC/Read&Publish 需复核) is settled after acceptance

## Anti-patterns

- Uploading a manuscript that reveals the author (triple-anonymous — it will not be read)
- Omitting line numbers from the review copy
- An abstract outside the stated range, or an article well over ~8,000 words with no justification
- Submitting a second article within twelve months as the same corresponding author
- Assuming a default reference export already matches the MIND house style

## Output format

```
【Type】Article / Discussion / Book review / Critical notice (length ok? Y/N)
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Line numbering】present? [Y/N]
【Abstract】word count (50–200 published)
【12-month rule】clear? [Y/N]
【Format】Word/PDF + images + alt text ready? [Y/N]
【Next】await decision → mind-revision-and-response
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — ScholarOne, LaTeX `lineno`, anonymization, the MIND Stylesheet
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Mind URLs behind every fact in this pack
