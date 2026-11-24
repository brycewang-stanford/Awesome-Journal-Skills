---
name: pnas-writing
description: Use to structure a PNAS main text and hold its length — Title, Significance Statement, Abstract, Introduction, Results, Discussion, in-text Materials and Methods, references — and to choose the required Classification (Biological/Physical/Social Sciences + minor subject) and keywords at submission.
---

# Main-Text Writing & Structure (pnas-writing)

## When to trigger

- The manuscript structure is unclear or out of PNAS order.
- Materials and Methods are missing, or someone wants to push them out of the main text.
- The paper is over the length budget.
- You have not chosen a **Classification** (major + minor) or keywords.
- The Results read like a lab notebook instead of an argument.

## PNAS main-text order

A PNAS research article runs, in order:

1. **Title** — declarative, specific, parseable by a non-specialist.
2. **Author list & affiliations.**
3. **Significance Statement** — ≤120 words (`pnas-significance`); submitted separately but part of the article.
4. **Abstract** — ~250-word single paragraph (`pnas-abstract`).
5. **Introduction** — the gap and why it matters broadly; end on what you found.
6. **Results** — argument-ordered (below).
7. **Discussion** — interpretation and broader significance; PNAS also permits a **combined "Results and Discussion."**
8. **Materials and Methods** — **kept in the main text** (see below).
9. **Acknowledgments, data availability, references.**

## Materials and Methods stays in-text (a key PNAS difference)

PNAS keeps a **Materials and Methods** section in the main text — unlike *Cell* or *Science* Reports, which push methods to supplements/endmatter. Provide enough method in the body to evaluate and reproduce the work; longer protocols and extended data go to **SI Appendix**. Do not strip the main-text Methods to chase a word count — move detail to SI instead.

## Length budget

- Research Reports have a **preferred length of 6 pages and a maximum of 12 pages**; a standard 6-page article is roughly **4,000 words, 50 references, and 4 medium-size figures/tables** (PNAS author center, re-verified 2026-11-23). Budget the **whole package** — abstract, Significance Statement, main text, figures/tables, and references — against the page allowance.
- **Confirm the current word/character/page caps and the figure-table allowance in PNAS author guidelines** before finalizing; treat any number here as a working target, not a rule.
- Over-length material (extended methods, supporting figures/tables, supplementary text) → **SI Appendix**.

## Classification + keywords (required at submission)

PNAS requires a **Classification** for every research article:

- **Major category — exactly one division:** **Biological Sciences**, **Physical Sciences**, or **Social Sciences**.
- **Minor subject area:** one (sometimes a permitted second) subject within that division (e.g., Biological Sciences → Genetics; Physical Sciences → Applied Physical Sciences; Social Sciences → Economic Sciences). Pick from the PNAS list.
- **Keywords:** at least three and no more than five (PNAS main-manuscript template).

Choose the classification that matches the **handling and review community** you want, consistent with the venue call in `pnas-fit` and the editor choice in `pnas-track`/`pnas-submission`.

## Structure as argument, not chronology

Order the Results by the **logic of the claim**, not the order experiments were run:

1. Establish the phenomenon (the headline result).
2. Rule out the obvious alternative explanations.
3. Show the mechanism / generality.
4. Demonstrate the broad implication.

Each Results paragraph: **claim sentence first**, then evidence (figure callout + numbers), then inference.

## Cross-references

- Main figures/tables: "Fig. 1", "Table 1".
- Supporting Information: "*SI Appendix*, Fig. S1 / Table S1"; datasets as "Dataset S1".

## Output format

```
【Order check】 Title / authors / Significance / Abstract / Intro / Results / Discussion / Materials and Methods / refs — gaps?
【Methods location】 in main text? yes (FIX if missing) — extended detail in SI Appendix?
【Length】 package within budget? N vs cap (confirm guidelines)
【Classification】 major (Bio/Phys/Social) + minor subject chosen? + keywords (3–5)?
【Results order】 argument-ordered, claim-first? yes/no
【Items in main vs SI】 main: [...] / SI Appendix: [...]
【Next】 pnas-figures
```

## Anti-patterns

- **Do not** delete the main-text Materials and Methods to fit a word count — move detail to SI Appendix.
- **Do not** omit the Classification or keywords; they are required at submission.
- **Do not** structure Results chronologically when a logical order is clearer.
- **Do not** import a Science Report's "Methods-in-supplement" structure — PNAS keeps Methods in-text.
- **Do not** treat the Significance Statement or abstract as optional sections.
