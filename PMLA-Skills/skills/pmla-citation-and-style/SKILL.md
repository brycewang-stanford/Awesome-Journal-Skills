---
name: pmla-citation-and-style
description: Use when formatting a PMLA (Publications of the Modern Language Association) essay in MLA style — in-text parenthetical citations keyed to a Works Cited list built from the MLA Handbook's template of core elements, plus quotation, translation, and discursive-note conventions. PMLA requires the most recent MLA Handbook. Handles citation mechanics; it does not write the argument.
---

# Citation & MLA Style (pmla-citation-and-style)

PMLA requires **MLA style as set out in the most recent edition of the MLA Handbook** — the field's own
standard, not a generic Chicago or APA format. This skill handles the mechanics: in-text parenthetical
citations, a **Works Cited** list built from the **template of core elements**, and the conventions for
quotation, translation, and discursive notes. Get this right; reviewers and editors notice.

## When to trigger

- Building or auditing in-text citations and the Works Cited list
- Deciding how to cite a primary text, edition, translation, or archival source
- Formatting quotations (run-in vs. block) and discursive notes
- Final style pass before `pmla-submission`

## MLA style essentials

1. **In-text parenthetical citation.** Cite author and page (or author and an appropriate locator) in
   parentheses, keyed to the Works Cited entry. Keep the author's name and the locator unambiguous
   where multiple works are cited.
2. **Works Cited via core elements.** Build each entry from the MLA **template of core elements**
   (Author. Title of source. Title of container, Contributors, Version, Number, Publisher, Publication
   date, Location), with "containers" for works inside larger works. One consistent style throughout.
3. **Editions and primary texts.** Cite the **reliable edition** you actually quote; if the edition
   matters to the reading, make it explicit. Be consistent across the essay.
4. **Quotation.** Short quotations run into the text with quotation marks; longer passages set off as
   block quotations per the Handbook. Reproduce wording, spelling, and punctuation exactly; mark
   omissions and interpolations clearly.
5. **Translations and non-English sources.** State your translation policy and apply it consistently;
   cite both original and translation as appropriate. **Translations are excluded** from the PMLA word
   count — but they must still be cited.
6. **Discursive notes.** PMLA permits substantive notes, but they **count toward** the 6,000–9,000-word
   range. Use them for genuine elaboration, not citation dumping.
7. **What the word count excludes.** The 6,000–9,000-word count is taken **including discursive notes**
   but **excluding the list of works cited and translations**. So your Works Cited list does not eat
   into the budget — a full, properly formatted list never costs you words. (Verify the live cap.)

## A pre-submission style check

- [ ] Every in-text citation has a matching Works Cited entry, and vice versa
- [ ] Works Cited entries follow the current MLA template of core elements
- [ ] One consistent style throughout (manage with Zotero / BibTeX-MLA, then verify by hand)
- [ ] Quotations exact; block-quote threshold and formatting per the Handbook
- [ ] Translation policy stated and applied; originals/translations cited
- [ ] Discursive notes are substantive (and the word count accounts for them; works cited and translations do not)

## Anti-patterns

- Using APA/Chicago/numeric styles instead of MLA
- In-text citations with no Works Cited entry (or orphaned entries)
- Inexact quotation; silent emendation; unspecified edition
- A reference manager's output pasted in without checking it against the Handbook
- Stuffing citations or a second argument into discursive notes that then blow the word count

## Output format

```
【Style】MLA (most recent MLA Handbook) confirmed? [Y/N]
【In-text ↔ Works Cited】one-to-one match? [Y/N]
【Core-elements entries】consistent throughout? [Y/N]
【Quotations】exact; block formatting correct? [Y/N]
【Translation policy】stated and applied? [Y/N/NA]
【Notes】substantive; counted in word total? [Y/N]
【Next】pmla-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — MLA Handbook, MLA Style Center, and reference managers
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — MLA-style requirement and word-count rule
