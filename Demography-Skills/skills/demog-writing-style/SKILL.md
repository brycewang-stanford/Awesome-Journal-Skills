---
name: demog-writing-style
description: Use when drafting or polishing a Demography (PAA / Duke University Press) manuscript so it reads for population scientists across components, follows the journal's house style (loosely APA), and fits the limits (Research Articles <= 8,000 words main text; Notes <= 4,000; Commentaries <= 2,000; abstract <= 200 words; up to 5 keywords; 3-5 highlights). Tightens prose and format; it does not invent content.
---

# Writing Style (demog-writing-style)

A Demography paper must be readable by a demographer outside its component, formatted to the journal's
**loosely APA** house style, and disciplined to the word and front-matter limits. This skill is about
reaching population scientists and respecting the format — not about generating claims.

## When to trigger

- Drafting the introduction, framing the contribution, or final polish
- Over the word cap and needing to cut without losing the argument
- Writing the **<= 200-word abstract**, **3-5 highlights**, or selecting **<= 5 keywords**
- Aligning citations/headings/format to the journal's house style before submission

## Reach population science

1. **Front-load the contribution.** By the end of the introduction the reader knows the population
   question, the data and method, the finding, and why it matters for demography broadly. Don't make a
   migration scholar dig for the "so what" in your fertility paper.
2. **Define component-specific jargon** on first use; a mortality reader should follow a family-
   demography paper. Spell out acronyms and data-source names.
3. **Quantity-first prose.** Lead with the demographic quantity and its magnitude (a difference in e0,
   a parity-progression ratio, a net flow), then interpret it. Avoid "the model shows…" without
   saying what changed and by how much.
4. **Signpost.** Clear section structure so a reader can follow data -> method -> result -> meaning.

## Format to the house style

- **References**: **loosely APA** (author-date); keep one consistent style (manage with Zotero/BibTeX).
  Articles **recommend <= 75 references**; Notes/Commentaries **<= 15**. References excluded from the
  word count.
- **Front matter**: **abstract <= 200 words**; **up to 5 keywords/phrases**; **3-5 highlights**, each a
  complete sentence **<= 85 characters** including spaces.
- **Spelling**: Merriam-Webster conventions.
- **Anonymize**: review is **double-blind** — avoid self-identifying references ("as we showed in…")
  and strip identifying file metadata (see `demog-submission`).

## Fit the limits (main-text counts exclude abstract, keywords, footnotes, acknowledgments, references)

- Move full life tables, sensitivity grids, and extended results to the **online appendix**.
- Cut throat-clearing and literature dumps; engage the demographic conversation, not every paper (see
  `demog-literature-positioning`).
- Prefer one decisive figure (a Lexis surface, an age schedule) to three redundant tables.
- Keep within the **table/figure limit** (~8 for Articles, 4 for Notes — see `demog-tables-figures`).

## Anti-patterns

- A component-insider intro that never states general interest to demographers
- Burying the contribution in the middle of the paper
- An abstract over 200 words, or highlights that exceed 85 characters
- Mixed citation styles; self-references that break double-blind anonymity
- Padding a Research Note toward Article length

## Calibration anchor: write the population process, not the association

Demography, the open-access flagship of the Population Association of America at Duke University Press,
reads as population science when the prose names a *process* — fertility, mortality, migration, family
formation, or compositional change — and the quantity that measures it. Two illustrative rewrites
(language invented to show the move):

| Drafted as a generic association | Rewritten as a population process |
|----------------------------------|-----------------------------------|
| "Education is associated with lower mortality (HR 0.78)." | "Among women aged 50-69, the college-educated face ~22% lower age-specific death rates, widening the e0 gap by ~2.1 years (illustrative)." |
| "Migrants have higher fertility." | "Newly arrived migrants show elevated period TFR, but a tempo correction suggests catch-up timing, not higher quantum (illustrative)." |

The left column could appear in any health or labor journal; the right column states the demographic
quantity, the population, and the age/period logic a demographer expects.

## Referee-pushback patterns and the writing fix

- *"This reads like an epidemiology paper that happens to use population data."* -> Lead the abstract and
  intro with the population question and the demographic quantity, not the regression coefficient.
- *"A migration scholar could not follow the fertility argument."* -> Define component-specific terms
  (parity progression, ASFR, tempo/quantum) on first use; spell out every data-source acronym.
- *"The contribution to population science is stated only in the conclusion."* -> Move the "so what for
  demography" sentence into the first paragraph; a Demography reader should not have to dig for it.
- *"You report stars but never the magnitude."* -> Lead with the demographic quantity and its size,
  then interpret it.

## Output format

```
【Contribution stated by end of intro?】[Y/N]
【Reads past the component?】jargon defined / acronyms + data sources spelled? [Y/N]
【Abstract】word count (<= 200); 【Highlights】3-5, each <= 85 chars?
【Keywords】<= 5?
【Word count】Article <= 8,000 / Note <= 4,000 / Commentary <= 2,000 (main text)?
【House style + anonymized】loosely APA + no self-ID refs? [Y/N]
【Next】demog-data-and-reproducibility
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — word/abstract caps, highlights, keywords, house style, double-blind anonymity
