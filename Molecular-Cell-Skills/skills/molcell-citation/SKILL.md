---
name: molcell-citation
description: Use to convert references to the current Cell Press numbered style used by Molecular Cell — superscript numbers in order of first appearance, a reference list numbered in that order, full author lists (no et al.), abbreviated journal names. This is NOT author-date; older Cell Press author-date manuscripts must be renumbered.
---

# Reference Style (molcell-citation)

## When to trigger

- References are author–date "(Smith et al., 2021)" and must become Cell Press numbered.
- The reference list is alphabetical instead of ordered by first appearance.
- Author lists are truncated with "et al." in the bibliography.
- You are porting a manuscript from a name–year journal (or an older Cell Press template) to Molecular Cell.

## Cell Press numbered citation mechanics (current)

Cell Press moved its journals — including Molecular Cell — to a **numbered** referencing style. Confirm the live format, but the working model is:

- **In-text: superscript numbers**, assigned in **order of first appearance** (e.g., "…unwinds DNA.^1,2" and later "…as shown previously.^1").
- **Reference list: numbered in citation order** — NOT alphabetical, NOT author–date.
- **Full author lists** in each entry (Cell Press does not truncate to "et al." for typical author counts; confirm the cutoff).
- **Abbreviated journal names**, with year in parentheses, volume, and pages/article number.
- A **single reference list** covering the main text and STAR Methods.
- Reuse the same number on every later citation of a source; never assign a source two numbers.

> This is the **opposite** of the old Cell Press author–date convention and of journals like Genetics that stay name–year. Porting in from an author–date manuscript is a mechanical but error-prone renumbering — do it in one pass so the in-text superscripts and the list stay in sync.

## Reference formats (shape — confirm against the live Cell Press style)

- **Journal article:**
  `Author, A.B., Author, C.D., and Author, E.F. (2021). Title of the article. Abbrev. Journal Name 152, 1173–1183.`
- **Book:**
  `Author, A.B. (2020). Book Title, edition (Publisher).`
- **Chapter:**
  `Author, A.B. (2020). Chapter title. In Book Title, C.D. Editor, ed. (Publisher), pp. xx–yy.`
- **Dataset/structure/code:** cite with repository, accession/DOI, and year (consistent with `molcell-data`).
- **Preprint:** include the server (e.g., bioRxiv) and DOI.

> Surname precedes initials; "and" before the final author; year in parentheses after the author list. The entry is preceded by its number in the list.

## Common conversion fixes (author–date → Cell Press numbered)

| From (author–date)                     | To (Cell Press numbered)                          |
|----------------------------------------|---------------------------------------------------|
| "(Smith et al., 2021)" in text         | superscript "^12" in order of appearance          |
| List alphabetical by first author      | list **numbered by order of first appearance**    |
| Same source cited twice with two tags  | one number, reused at every citation              |
| Truncated "et al." in the biblio       | full author list                                  |
| Separate STAR Methods bibliography      | one merged, continuously numbered list            |
| Narrative "Smith et al. (2021) showed" | "Smith et al.^12 showed" (name in text, number superscript) |

## Worked conversion (author–date → Cell Press numbered)

An author–date sentence and its list entry:

> Loss of XYZ slows fork progression (Smith et al., 2021).
> Smith, A.B., Lee, C.D., and Wong, E.F. (2021). Title. Mol. Cell 81, 233–247.

Converted to the current Cell Press numbered style, the in-text token becomes a superscript number set by where the source first appears, and the entry keeps full authors but is placed at that number in the citation-ordered list:

> Loss of XYZ slows fork progression.^7
> 7. Smith, A.B., Lee, C.D., and Wong, E.F. (2021). Title. Mol. Cell *81*, 233–247.

Mechanical traps: the number is fixed the first time the source appears and reused thereafter (do not renumber on later mentions); a source deleted from the text must be removed and everything after it renumbered; and a narrative citation keeps the author name in the sentence but still carries the superscript number.

## STAR Methods and the single list

Molecular Cell uses **one** continuously numbered reference list for the whole paper, including citations that appear only in STAR Methods (protocols, algorithms, prior reagents). Do not build a separate methods bibliography. When porting from a journal that footnotes methods, sweep the STAR Methods text for citations and confirm each has a number in the single list. Software and datasets cited in the Key Resources Table follow `molcell-data` conventions (repository, accession/DOI, version) rather than the journal-article shape.

## Tooling

- Use Zotero/EndNote with the **current Molecular Cell / Cell Press** CSL/style (numbered, citation-order); do a final manual pass on author-list completeness and journal-abbreviation form.
- After any text edit that adds or removes a citation, **re-run the citation manager** so numbers re-sequence — hand-numbering drifts fast.
- Verify every superscript resolves to exactly one list entry and that no list entry is uncited.

## Output format

```
【Style detected】 author–date / alphabetical / other → Cell Press numbered
【In-text】 superscript numbers in order of appearance? yes/no
【List order】 numbered by first appearance (not alphabetical)? yes/no
【Author lists】 full (not et al.)? surname-first? journal abbreviated? yes/no
【Reuse】 each source one number, reused on later cites? yes/no
【Unresolved / uncited】 [...]
【Next】 molcell-submission
```

## Anti-patterns

- **Do not** leave author–date "(Smith et al., 2021)" tokens in a Molecular Cell manuscript.
- **Do not** order the reference list alphabetically — Cell Press numbered is by **appearance**.
- **Do not** give one source two different numbers.
- **Do not** truncate author lists with "et al." in the bibliography.

> Cell Press reference formatting evolves — confirm the exact numbered format, author-list cutoff, and journal-abbreviation style against the current Molecular Cell information-for-authors page.
