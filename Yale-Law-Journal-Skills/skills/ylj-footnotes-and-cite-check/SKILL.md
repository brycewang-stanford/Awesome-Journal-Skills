---
name: ylj-footnotes-and-cite-check
description: Use when running the final footnote-apparatus audit of a The Yale Law Journal (YLJ) piece — verifying every cite exists, is pinpointed, is correct Bluebook form, and actually supports its sentence, in preparation for (or during) the student source-pull. It verifies; it does not construct new cites (ylj-sources-and-bluebook).
---

# Footnotes & Cite-Check (ylj-footnotes-and-cite-check)

The heavy-footnote apparatus is what distinguishes legal scholarship, and YLJ's **source-pull** verifies
every footnote by hand. This skill runs the same audit *you* should run before submission and again
during editing, so the piece survives source-pull cleanly. It verifies an existing apparatus; building
cites is `ylj-sources-and-bluebook`, and the editorial cycle that triggers source-pull is
`ylj-revision-and-editing`.

## When to trigger

- Final pass before submission — the apparatus must be source-pull-ready
- Answering source-pull author queries during the editing cycle
- A reader or editor flagged a cite that may not support its sentence
- Reconciling short forms (`id.`, `supra`) and cross-references after heavy revision

## The four-point cite test (every footnote)

1. **Existence.** The source is real and retrievable (case in the reporter, statute in the code,
   article in the journal). Dead or invented cites are the gravest source-pull failure.
2. **Support.** The cited page/section actually says what the sentence claims. The cite-doesn't-support
   failure is the most common — read the pinpoint, not just the source's headnote.
3. **Pinpoint.** The cite points to the exact page/section/paragraph relied on, not the source's first
   page.
4. **Form.** Bluebook form is correct for the source type, with the right signal and consistent short
   forms.

## Apparatus-wide consistency sweep

| Check | Failure it catches |
|-------|--------------------|
| **Short-form chain** | An `id.` pointing at the wrong antecedent after a paragraph was moved |
| **`supra` notes** | A `supra note 14` whose note 14 was renumbered or deleted |
| **First-full-cite rule** | A short form used before the source's first full citation |
| **Cross-references** | "See Part III.B" when restructuring renamed the Part |
| **Quotation fidelity** | Quoted text that no longer matches the source verbatim; missing `[ ]`/`. . .` |
| **Signal accuracy** | `See` where the source states it directly (or `E.g.` with one example) |

## Risk-ordered audit pass

Do not audit footnotes only from note 1 to the end. First isolate the citations that would damage the
piece if they fail:

1. **Load-bearing law:** holdings, statutory text, constitutional provisions, agency rules.
2. **Novelty claims:** cites used to prove what prior scholarship has or has not said.
3. **Empirical / historical claims:** any number, date, institutional practice, or archive fact.
4. **Quotations:** all block quotes and all quotations used as proof of meaning.
5. **String cites:** sources in a chain where one weak cite can make the whole proposition look padded.

For each high-risk note, write a one-line support note: "source says X at pin Y; manuscript sentence
claims Z; support is direct / inferential / weak." Anything weak becomes a revision task, not a
source-pull answer to defer.

## Quotation and integrity audit

- Re-collate every direct quotation against the source character-for-character; mark alterations per
  Bluebook (`[ ]`, `. . .`, `(emphasis added)`, `(citation omitted)`).
- Flag any paraphrase that tracks the source's wording without quotation marks — fix it before an editor
  raises it as an integrity issue.

## Pre-empt the source-pull

Build a query-resistant apparatus: for the hardest cites, drop an explanatory parenthetical that shows
*where* in the source the support lives. This converts a likely author query into a verified footnote.

## Checklist

- [ ] Every cite passes existence + support + pinpoint + form
- [ ] Hardest/most-load-bearing cites personally re-checked against the source
- [ ] Short-form chain (`id.`/`supra`) consistent after all revisions
- [ ] First-full-cite precedes every short form
- [ ] Cross-references match the final Part/section structure
- [ ] Quotations collated verbatim; alterations Bluebook-marked
- [ ] No unmarked paraphrase tracking a source's wording

## Anti-patterns

- A cite to a source whose pinpoint doesn't actually say what the sentence claims
- `id.` / `supra` chains broken by reordering, left for the source-puller to untangle
- A quotation that drifted from the source during editing (verbatim no longer matches)
- Relying on a headnote or syllabus instead of the opinion's actual holding page
- Treating the apparatus as the editors' job — they verify it; they don't build it

## Output format

```
【Cites audited】N footnotes; existence + support + pinpoint + form all pass? Y/N
【High-risk notes】load-bearing citations support-logged? Y/N
【Hard cites】load-bearing cites re-checked against source? Y/N
【Short forms】id./supra chain + cross-refs consistent? Y/N
【Quotations】collated verbatim + alterations marked? Y/N
【Source-pull-ready】Y/N
【Next】ylj-workflow to route the next piece, or ylj-revision-and-editing if mid-edit
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Bluebook, KeyCite/Shepard's, and cite-checking tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — YLJ source-pull / citation-requirement facts
