---
name: jaar-citation-and-style
description: Use when formatting citations and references for a Journal of the American Academy of Religion (JAAR) article. JAAR's distinctive rule is IN-TEXT author-date citations (NOT footnote citations) with an alphabetized year-keyed reference list; footnotes are reserved for substantive points. Handles reference apparatus; it does not write the argument.
---

# Citation & Style (jaar-citation-and-style)

JAAR has a citation style that trips up authors coming from history or theology: **citations go
in-text (author-date), not in footnotes.** Footnotes are for substantive remarks only. Getting this
wrong signals you have not read the style sheet — fix it before submitting.

## When to trigger

- Converting a footnote-cited draft to JAAR's in-text style
- Building the reference list and checking entry forms
- Handling primary-source citations, translations, and transliteration in references
- Final style pass before submission

## JAAR's citation rules (verify current style sheet)

1. **In-text author-date citations.** Cite as `(Wolf 1996: 33)` or in prose `Clarkson notes … (1995:
   45–46)`. Do **not** put bibliographic citations in footnotes.
2. **Footnotes for substance only.** Use notes for points outside the body of the argument, not to cite
   sources. Keep them lean (they count toward the word budget).
3. **Reference list.** An **alphabetized, year-keyed** list of works cited; format each entry per the
   JAAR style sheet.
4. **House conventions.** Serial (Oxford) comma; gender-neutral language; **italicize foreign words**;
   a consistent transliteration system for non-Latin scripts.
5. **Fallback style.** For anything the JAAR style sheet does not address, the sheet directs authors to
   the **Chicago Manual of Style** (the downloadable sheet references the **15th edition**; CMOS is now
   in its 18th — **待核实** the current edition the live style guide cites). Treat JAAR's in-text
   author-date system as primary regardless.

## Primary sources, translations, transliteration

- Cite primary texts by the conventions of your subfield, but keep them consistent and keyed to the
  reference list; give edition/translation information.
- Provide originals where the argument turns on wording; note the translator; transliterate consistently.

## Anti-patterns

- Footnote-style bibliographic citations (the most common JAAR style error)
- A footnote apparatus so heavy it blows the word budget
- Inconsistent transliteration or undefined foreign terms
- Reference-list entries that don't match the in-text author-date keys
- Defaulting to a CMOS edition without checking which the current style sheet names (待核实)

## Output format

```
【In-text citations】author-date, not footnotes? [Y/N]
【Footnotes】substantive only, lean? [Y/N]
【Reference list】alphabetized, year-keyed, style-sheet form? [Y/N]
【House conventions】serial comma + gender-neutral + foreign-term italics? [Y/N]
【Transliteration】consistent + terms defined? [Y/N]
【CMOS edition】confirmed against live style sheet? [Y/N/待核实]
【Next】jaar-review-process
```

## Conversion table: history/theology habits → JAAR house style

Most authors arriving at JAAR are trained in disciplines whose flagship venues cite in notes. The
AAR/Oxford University Press journal expects a specific in-text apparatus, so the highest-yield style
pass is mechanical reformatting first.

| You wrote (footnote-trained) | JAAR wants (in-text author-date) |
|------------------------------|----------------------------------|
| `As Smith argues.¹` + note "¹ Smith, *Imagining Religion*, 22." | `As Smith argues … (1982: 22).` + keyed entry |
| `Ibid., 24.` / `op. cit.` | Repeat author-date: `(1982: 24)` — no Latin shorthand |
| `See note 14 above for sources.` | Cite in-text at the point of use; reserve notes for substance |
| `Cf. the *Bhagavad Gītā* 2.47.` in a note | Cite the primary text in-text per subfield convention |
| Bibliography of "Works Consulted" | Reference list of **works cited only**, alphabetized, year-keyed |

## Worked vignette: de-noting a textual-historical draft

An author submits a study of a Kabbalistic commentary with 78 footnotes, 60 of them bare citations
migrated from a dissertation. The JAAR pass:

- **Bibliographic notes go in-text.** Note 12 ("Scholem, *Major Trends*, 205–6") becomes
  `(Scholem 1941: 205–6)` in the sentence; the note disappears. After conversion, only 11 notes
  survive — all genuinely substantive (a manuscript-variant aside, a definitional caveat on *sefirot*).
- **Foreign terms.** *Ein Sof*, *tiqqun*, *devequt* are italicized and glossed on first use under a
  single declared transliteration system, so a non-Hebraist religion-studies reader can follow — a
  point `jaar-writing-style` also enforces.
- **Budget effect.** Cutting 49 citation-only notes returns words to the body, easing the length
  ceiling that `jaar-structure-and-exposition` tracks (notes count toward it); every surviving in-text
  key now matches an alphabetized, year-keyed entry, and "Works Consulted" but never cited are removed.

## Referee and copyedit pushback → the fix

- "Citations belong in the text, not notes" → run the conversion table above end-to-end.
- "Note apparatus is overweight" → strip citation-only notes; keep substantive asides.
- "Reference entry doesn't match the in-text key" → reconcile every `(Author year)` to its entry.

Hedged calibration: the downloadable sheet long referenced CMOS 15th while CMOS is now in its 18th
edition; treat the in-text author-date system as primary and verify the named fallback edition on the
journal's current submission guidelines rather than assuming the cached number.

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JAAR style sheet: in-text author-date citations, CMOS fallback
