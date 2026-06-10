---
name: sci-citation
description: Use when converting a reference list to Science (AAAS) numbered style — italic numbers cited in order of appearance, a single continuous list that the Supplementary Materials share, full author lists rather than "et al." in the bibliography, and abbreviated journal titles. Late-stage style pass for the flagship AAAS weekly.
---

# Reference Style (sci-citation)

## When to trigger

- References are in author–date (APA/Harvard) or Nature style and must become Science style.
- The reference list is not ordered by citation appearance.
- Author lists are truncated with "et al." in the bibliography.
- Notes and references are split when Science combines them.

## Science citation mechanics

- **Numbered, in order of appearance** in the text, as italic numbers in parentheses: *(1)*, *(2, 3)*, *(4–6)*.
- A **single reference list** numbered consecutively; in Science, **main text and Supplementary Materials share one continuous numbering** (the SM continues the count). Confirm against current guidelines, but design for one list.
- **Notes and references are combined** — explanatory notes get a number in the same list.
- The reference list gives **full author lists** (Science does not truncate to "et al." in the bibliography for typical author counts).
- **Journal titles abbreviated** (per standard abbreviations); include volume, page (or article number), year.

## Reference formats (shape)

- **Journal article:**
  `A. B. Author, C. D. Author, E. F. Author, Title of the article. *Journal Abbrev.* **Volume**, page (year).`
- **Book:**
  `A. B. Author, *Book Title* (Publisher, ed., year), pp. xx–yy.`
- **Chapter:**
  `A. B. Author, in *Book Title*, C. Editor, Ed. (Publisher, year), pp. xx–yy.`
- **Dataset/code:** cite with repository, accession/DOI, and year (consistent with `sci-data`).
- **Preprint:** include the repository and DOI/identifier.

> Initials precede surnames; titles are in sentence case; journal in italics; volume in bold. Use a reference manager style file for Science to enforce this mechanically.

## Common conversion fixes

| From                              | To (Science)                                  |
|-----------------------------------|-----------------------------------------------|
| "(Smith et al., 2021)"            | "*(12)*"                                       |
| "Smith, J. (2021)."               | "J. Smith, …"                                 |
| Truncated "et al." in biblio      | full author list                              |
| Alphabetical reference list       | ordered by first appearance                   |
| Separate "Notes" section          | merged into the numbered list                 |

## Tooling

- Use Zotero/EndNote with the **Science** CSL/style; do a final manual pass on abbreviations and author-list completeness (managers often truncate).
- Verify every in-text number resolves and the list has no gaps/duplicates after the SM merge.

## Why the continuous-numbering rule bites at Science specifically

Most general journals keep main-text and supplement references separate. Science's heavy reliance on Supplementary Materials means the SM often carries the bulk of the citations, and the house convention threads them into **one** consecutively numbered list (the SM continues the count from the main text). A reference first cited in fig. S7's legend gets the next free number, not a parallel "S" series. This is the single most common style defect when a manuscript is ported from a Nature-style or author–date template, because those tools renumber the SM independently. Confirm the exact current convention against the author guidelines, but build the list as one stream.

## Worked micro-example (illustrative)

A Report cites three sources in its first paragraph, then introduces a fourth source only in the Supplementary Methods:

- Main text: "...prior surveys disagreed *(1, 2)*, and the standard model predicts otherwise *(3)*."
- SM Methods: "We adapted the assay of *(4)*."
- Combined reference list (one stream, by appearance):
  1. `A. B. Chen, D. Okafor, Title of the first survey. *Science* **370**, 112 (2020).`
  2. `R. Mehta, S. Lindqvist, L. Park, Title of the second survey. *Nat. Commun.* **11**, 4471 (2020).`
  3. `J. Ito, Title of the model paper. *Phys. Rev. Lett.* **124**, 030601 (2020).`
  4. `K. Adeyemi, T. Roy, Title of the assay paper. *Cell* **180**, 55 (2020).`

Note: initials precede surnames, titles are sentence case, journal abbreviated and italic, volume bold — and reference 4, though first invoked in the SM, takes the next integer, not "S1".

## Conversion-failure patterns to catch

| Failure mode (what a copyeditor flags) | Science-specific fix |
|----------------------------------------|----------------------|
| SM references restart at 1 or use an "S" prefix | Merge into the single stream; renumber by first appearance across main + SM. |
| Manager truncated authors to "et al." in the list | Restore the full author list; Science prints all authors for typical counts. |
| Explanatory footnotes sit in a separate "Notes" block | Fold each note into the numbered list as its own entry. |
| In-text markers rendered upright "(12)" not italic | Apply the italic-number-in-parentheses form *(12)*. |
| List alphabetized by a default CSL | Re-sort strictly by order of first citation. |

## Calibration anchors (confirm against current author guidelines)

- Numbering is by appearance, not alphabetical; markers are italic numbers in parentheses, e.g., *(1)*, *(2, 3)*, *(4–6)*.
- One continuous list spanning main text and Supplementary Materials; notes and references are combined.
- Full author lists in the bibliography; journal titles abbreviated; volume bold; year in parentheses.
- After the SM merge, verify every in-text number resolves and the list has no gaps or duplicates.

## Output format

```
【Style detected】 author-date / Nature / other → Science
【Numbering】 by appearance? single continuous list incl SM? yes/no
【Author lists】 full (not et al.) in biblio? yes/no
【Journal abbreviations】 applied? yes/no
【Unresolved/duplicate refs】 [...]
【Next】 sci-cover-letter
```

## Anti-patterns

- **Do not** leave author–date citations anywhere in a Science manuscript.
- **Do not** alphabetize the reference list — order is by appearance.
- **Do not** truncate author lists with "et al." in the bibliography.
- **Do not** keep separate main-text and SM reference numbering if guidelines call for one continuous list.
