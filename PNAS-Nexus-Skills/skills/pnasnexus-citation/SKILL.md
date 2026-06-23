---
name: pnasnexus-citation
description: Use to get PNAS Nexus references right — note that PNAS Nexus accepts references in any readable style at submission (unlike flagship PNAS's strict numbered-by-appearance), so the job is internal consistency, completeness, resolvable in-text citations, and the [dataset] tag for data/software. Prepare a single consistent (preferably numbered) style for production; confirm the final style on acceptance.
---

# Reference Style (pnasnexus-citation)

## When to trigger

- References are inconsistent, incomplete, or mix several styles.
- In-text citations don't all resolve to the list (or vice versa).
- Datasets/software are cited as bare URLs rather than formal references.
- You are about to submit and want the reference list clean.

## The PNAS Nexus rule that surprises people: format-neutral at submission

PNAS Nexus states, verbatim, *"You may format references in any readable style at submission."* This is a **deliberate contrast with flagship PNAS**, which enforces a numbered, in-order-of-appearance style up front. So at PNAS Nexus, **do not burn effort forcing a specific house style for initial submission** — instead make the references **clean, complete, consistent, and resolvable**.

> The **final published** reference style is **待核实** — OUP/PNAS-portfolio journals typically render a **numbered, in-order-of-appearance** list at production, but the official page only guarantees submission-stage neutrality. Prepare a single consistent numbered style (it converts cleanly to most production styles) and confirm the exact format on acceptance.

## What actually matters at submission (the real checklist)

- [ ] **One consistent style** throughout — pick a reference-manager style (a numbered/Vancouver or PNAS-style works well) and apply it uniformly; do not leave a mix.
- [ ] **Every in-text citation resolves** to an entry in the list, and every list entry is cited — no orphans, gaps, or duplicates.
- [ ] **Complete metadata** — authors, title, journal/venue, year, volume, pages or article number, and a **DOI** where one exists.
- [ ] **Author lists** complete and accurate (avoid silent "et al." truncation in the list unless the chosen style requires it; reference managers often over-truncate — check).
- [ ] **Data and software cited as references** with the **`[dataset]`** tag where the journal asks for it (see `pnasnexus-data`), not buried as URLs in the text.
- [ ] **Preprints** clearly labeled as preprints with their repository/DOI.

## A safe, convertible default (numbered, in order of appearance)

If you want one style that is clean now and converts easily at production, use **numbered, in order of appearance**:

- In text: numbers in parentheses or brackets — **(1)**, **(2, 3)**, **(4–6)** — in the order references first appear.
- A **single numbered reference list** in appearance order.
- Each entry: authors, article title, abbreviated journal/venue, volume, pages/article number, year, DOI.

Reference formats (shape — confirm production requirements on acceptance):

- **Journal article:** `1. A. B. Author, C. D. Author, Article title. J. Abbrev. Volume, page–page (Year). DOI.`
- **Book:** `2. A. B. Author, Book Title (Publisher, ed. X, Year).`
- **Book chapter:** `3. A. B. Author, Chapter title in Book Title, C. D. Editor, Ed. (Publisher, Year), pp. xx–yy.`
- **Dataset:** `[dataset] 4. A. B. Author, Dataset title. Repository. Accession/DOI. Deposited DD Month Year.`
- **Preprint:** `5. A. B. Author, Title. Repository [Preprint] (Year). DOI (accessed DD Month Year).`

## Tooling

- Use Zotero/EndNote with a numbered or PNAS-style CSL; do a final manual pass on completeness and author-list truncation (managers often truncate).
- Verify every in-text citation resolves and the list has no gaps/duplicates; renumber after any reordering of the text.
- Run a DOI-completeness pass — add DOIs wherever they exist.

## Output format

```
【Submission rule】 references format-neutral at submission (PNAS Nexus) — make them clean, not house-styled
【Consistency】 one style applied uniformly? yes/no
【Resolvable】 all in-text ↔ list, no orphans/gaps/duplicates? yes/no
【Completeness】 authors / title / venue / year / vol / pages / DOI present? yes/no
【Data/software refs】 cited with [dataset] tag where required? yes/no
【Production style】 numbered-by-appearance prepared (convertible)? confirm final style on acceptance (待核实)
【Next】 pnasnexus-submission
```

## Anti-patterns

- **Do not** waste pre-submission effort hand-forcing a strict house style — PNAS Nexus accepts any readable style at submission.
- **Do not** ship a list that mixes several styles inconsistently.
- **Do not** leave in-text citations that don't resolve, or list entries never cited.
- **Do not** cite datasets/software as bare URLs — use formal references with the `[dataset]` tag.
- **Do not** assume the submission style is the final published style — confirm production requirements on acceptance.
