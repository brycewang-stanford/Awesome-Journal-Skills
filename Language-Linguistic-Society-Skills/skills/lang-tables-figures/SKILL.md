---
name: lang-tables-figures
description: Use when preparing the exhibits of a Language (LSA) manuscript — numbered examples, Leipzig-convention interlinear glosses, IPA transcription, tableaux/trees, and quantitative tables and figures. Language has specific conventions for linguistic examples that reviewers and typesetters enforce. Prepares exhibits; it does not generate data.
---

# Examples, Tables & Figures (lang-tables-figures)

In a linguistics paper the **numbered example** is the primary exhibit, and *Language* has firm
conventions for how examples, glosses, transcriptions, and quantitative displays are formatted. Getting
these right lets the paper read cleanly under double-anonymous review and pass into production without a
copyediting fight. Verify current specifics against the **Language Style Sheet** and the CUP/Overleaf
template before submission.

## When to trigger

- Formatting numbered examples, interlinear glosses, trees, tableaux, or IPA
- Building quantitative tables and figures from a model
- A reader said an example was mis-glossed, unreadable, or unnumbered
- Preparing figure captions and accessibility text

## Numbered examples (the core exhibit)

- **Number every example consecutively** — `(1)`, `(2)`, `(3)` — with sub-parts lettered `(1a)`,
  `(1b)`; reference them in the text by number, never "the example above."
- Give **object-language data in italics** (or the journal's current convention), followed by the gloss
  and a free translation in single quotes.
- Cite a **source** for each non-elicited token; mark elicited judgments (`*`, `?`, `#`) consistently.

## Interlinear glossing (Leipzig Glossing Rules)

- Use the standard **three-line format**: object language / morpheme-by-morpheme gloss / free
  translation, with the object and gloss lines **word-aligned** and morpheme boundaries matched
  (`-` for affixes, `=` for clitics, `.` for a single-word gloss of a portmanteau).
- Use **small-caps grammatical labels** (`PST`, `3SG`, `ERG`, `NMLZ`) from the Leipzig list; define any
  non-standard abbreviation in a list of glossing abbreviations.
- Keep the number of morphemes on the gloss line equal to the object line; misalignment is the most
  common example error reviewers flag.

## Transcription (IPA)

- Use **IPA** for phonetic/phonological data; state the transcription conventions and any language-
  specific symbols. Use a Unicode IPA font; do not fake symbols with look-alikes.
- Distinguish phonemic `/ /` from phonetic `[ ]` transcription consistently.

## Trees, tableaux, and formal displays

- Syntactic trees, OT tableaux, autosegmental diagrams, and derivations are **numbered examples** too;
  keep them legible in grayscale and vector where possible.
- For an OT tableau, mark the winner (`☞`), violations (`*`), and fatal violations (`*!`) per convention.

## Quantitative tables and figures

- Lead with the exhibit that carries the **main generalization**; do not bury it among model dumps.
- Report **effect sizes and intervals** in tables; name the model and clustering in the note. Prefer a
  plot (partial effects, by-speaker variation) over a wall of coefficients where it communicates better.
- Colorblind-safe, legible in grayscale; provide **alt text / a descriptive caption** for every figure.

## Referee/production conformance check

| Slip reviewers and typesetters catch | Language-appropriate fix |
|--------------------------------------|--------------------------|
| Gloss line misaligned with object line | match morpheme counts; align word-by-word |
| Non-standard glossing labels undefined | use Leipzig labels; list abbreviations |
| Examples referenced as "above/below" | number and cite by number |
| IPA faked with look-alike characters | use a Unicode IPA font |
| Coefficient dump where a plot would show the pattern | promote a partial-effects figure |

## Calibration (exhibits as argument, hedged)

Craft heuristics fitting *Language*'s conventions, not graded rules; confirm against the Style Sheet.
Because the numbered example *is* the evidence, a clean, correctly aligned gloss does more persuasive
work than any prose summary — a reader who can parse your example accepts the generalization. Illustrative:
a paper presents a key portmanteau affix with a mismatched gloss line and undefined labels; the fix
re-aligns the morphemes, glosses the portmanteau with `.` (e.g., `3SG.PST`), adds the abbreviation list,
and promotes the by-speaker variation from a coefficient table to a figure with alt text.

## Anti-patterns

- Gloss lines whose morpheme count does not match the object line
- Non-Leipzig or undefined grammatical abbreviations
- Examples that are unnumbered or cross-referenced by position, not number
- Faked IPA, or mixed phonemic/phonetic brackets used inconsistently
- A wall of coefficients where one figure would carry the generalization; missing figure alt text

## Output format

```
【Main exhibit】the example/figure carrying the central generalization
【Numbering】examples numbered consecutively, sub-parts lettered? [Y/N]
【Glossing】Leipzig three-line, aligned, labels defined? [Y/N]
【Transcription】IPA correct, brackets consistent? [Y/N/NA]
【Quant displays】effect sizes + model note + alt text? [Y/N/NA]
【Next】lang-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — glossing, IPA, tree/tableau, and plotting tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Language Style Sheet and example conventions
