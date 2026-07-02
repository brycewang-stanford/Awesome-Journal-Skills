---
name: cell-citation
description: Use to convert references to Cell Press author–date style — in-text "(Smith et al., 2021)", an alphabetical reference list by first author with full author lists, journal names spelled out. This is the OPPOSITE of Science's numbered-by-appearance style.
---

# Reference Style (cell-citation)

## When to trigger

- References are numbered by appearance (Science/Nature style) and must become author–date.
- The reference list is ordered by citation order instead of alphabetically.
- Author lists are truncated with "et al." in the bibliography.
- You are porting a manuscript from a numbered-style journal to Cell.

## Cell Press citation mechanics

- **In-text: author–date.** Parenthetical "(Smith et al., 2021)" or narrative "Smith et al. (2021) showed…". Multiple: "(Smith et al., 2021; Lee and Cho, 2020)". Two authors: "(Lee and Cho, 2020)". Same author/year: "(Smith et al., 2021a, 2021b)".
- **Reference list: alphabetical by first author's surname** — NOT numbered, NOT by order of appearance.
- **Full author lists** in the bibliography (Cell Press does not truncate to "et al." for typical author counts; confirm the cutoff).
- **Journal names** per Cell Press style (often spelled out / standard form); include year, volume, and pages/article number.
- A **single reference list** covering main text and STAR Methods.

> This is the **opposite** of *Science*, which uses **numbered references in order of appearance**. If you are transferring from Science (or Nature's numbered convention), you must **re-cite in author–date and re-sort alphabetically** — a mechanical but non-trivial conversion.

## Reference formats (shape)

- **Journal article:**
  `Author, A.B., Author, C.D., and Author, E.F. (2021). Title of the article. Journal Name Volume, pages.`
- **Book:**
  `Author, A.B. (2020). Book Title, edition (Publisher).`
- **Chapter:**
  `Author, A.B. (2020). Chapter title. In Book Title, C.D. Editor, ed. (Publisher), pp. xx–yy.`
- **Dataset/code:** cite with repository, accession/DOI, and year (consistent with `cell-data`).
- **Preprint:** include the server (e.g., bioRxiv) and DOI.

> Surname precedes initials in the list; "and" before the final author; year in parentheses after the author list. Use a Cell Press CSL/style file to enforce this.

## Common conversion fixes (numbered → Cell author–date)

| From (Science/numbered)            | To (Cell author–date)                          |
|------------------------------------|------------------------------------------------|
| "*(12)*" in text                   | "(Smith et al., 2021)"                          |
| List ordered by appearance         | list **alphabetical** by first author           |
| "A. B. Author, …" (initials first) | "Author, A.B., …" (surname first)               |
| Truncated "et al." in biblio       | full author list                                |
| Merged notes-and-references list   | references only; move notes to text/footnotes   |
| Numbers resolve to list positions  | every in-text (Author, year) resolves to an entry |

## Worked conversion (numbered → Cell author–date)

A Science-style sentence and its list entry:

> Loss of XYZ1 expands the stem pool *(7)*.
> 7. A. B. Smith, C. D. Lee, E. F. Wong, *Cell* **180**, 233–247 (2020).

Converted to Cell Press style, the in-text marker becomes the name-year token and the entry moves into the single alphabetical list with surname-first initials, full author list, spelled-out journal, and the year in parentheses after the authors:

> Loss of XYZ1 expands the stem pool (Smith et al., 2020).
> Smith, A.B., Lee, C.D., and Wong, E.F. (2020). Title of the article. Cell *180*, 233–247.

Note the mechanical traps this exposes: initials flip to follow the surname, "and" precedes the final author, the citation-order number is discarded entirely, and the entry re-sorts by "S" rather than by where it first appeared. Do all of these in one pass or the list and the in-text markers drift out of sync.

## STAR Methods and the single list

Cell uses **one** reference list for the whole paper, including citations that appear only in STAR Methods (protocols, algorithms, prior reagents). Do not build a separate methods bibliography. A common failure when porting from a journal that footnotes methods is orphaned method citations that never made it into the alphabetical list — sweep the STAR Methods text for name-year tokens and confirm each resolves. Software and datasets cited in the Key Resources Table follow `cell-data` conventions (repository, accession/DOI, version) rather than the journal-article shape.

## Tooling

- Use Zotero/EndNote with the **Cell Press** CSL/style; do a final manual pass on author-list completeness and journal-name form (managers often truncate).
- Verify every in-text "(Author, year)" has a matching alphabetical entry, and that a/b suffixes disambiguate same-author/year citations.
- Watch narrative vs. parenthetical placement: "Smith et al. (2020) showed…" keeps only the year in parentheses, while a parenthetical cite wraps both name and year — reference managers frequently mangle the narrative form on conversion.

## Output format

```
【Style detected】 numbered-by-appearance / Nature / other → Cell author–date
【In-text】 author–date "(Smith et al., 2021)"? yes/no
【List order】 alphabetical by first author? yes/no
【Author lists】 full (not et al.) in biblio? surname-first? yes/no
【Same-author/year】 a/b suffixes applied? yes/no
【Unresolved citations】 [...]
【Next】 cell-submission
```

## Anti-patterns

- **Do not** leave numbered "(12)" citations anywhere in a Cell manuscript.
- **Do not** order the reference list by appearance — Cell is **alphabetical**.
- **Do not** truncate author lists with "et al." in the bibliography.
- **Do not** copy Science's numbered convention by reflex — Cell is author–date.

> Confirm the exact author–date format, author-list cutoff, and journal-name style against current Cell Press author guidelines.
