---
name: pnasnexus-writing
description: Use to choose the PNAS Nexus article type, structure the main text, and hold the page-based length budget — Research Report / Brief Report / Perspective / Review / Registered Report — keep Materials and Methods in the main text, and select the required research-area classification at submission.
---

# Article Type, Structure & Length (pnasnexus-writing)

## When to trigger

- You have not chosen an **article type**, or the type doesn't match the content's length/ambition.
- The manuscript structure is unclear or the Methods are being pushed out of the main text.
- The paper is over the **page budget**.
- You have not chosen a **classification** (research area + subcategory).
- The Results read like a lab notebook instead of an argument.

## Step 1: choose the article type (this sets the budget)

| Article type | Length (confirm current guidelines) | Use it for |
|--------------|--------------------------------------|------------|
| **Research Report** | preferred **6 pages**, **max 12** (a standard 6-pp article ≈ **4,000 words, 50 references, 4 figures/tables**) | the default for full original research |
| **Brief Report** | **≤3 pages** (≈1,600 words, 15 refs) | a short, complete, single-point study |
| **Registered Report — Stage 1** | **≤3 pages** (≈1,600 words; intro + methods + analysis plan, pre-results) | hypothesis-driven study reviewed *before* data collection |
| **Registered Report — Stage 2** | preferred **6 pages / 4,000 words**, **max 12** | the completed study after Stage-1 in-principle acceptance |
| **Perspective** | **≤10 pages** | a forward-looking, evidence-grounded opinion (may be unsolicited) |
| **Review** | **≤10 pages** | a synthesis of a field (may be unsolicited) |

> The **page limit counts the whole package** — abstract, Significance Statement, main text, figure captions, and table legends all count toward it. There is no separately stated absolute word cap for the 12-page maximum; the "≈4,000 words" figure describes a *6-page* article, not the 12-page ceiling. A "6,000-word cap" seen in third-party guides is **待核实** — the official limit is page-based.

## Step 2: PNAS Nexus main-text order

A Research Report runs, in order:

1. **Title** — declarative, specific, parseable by a non-specialist.
2. **Author list & affiliations.**
3. **Significance Statement** — 50–120 words (`pnasnexus-significance`), for Research Reports / Stage 2 Registered Reports.
4. **Abstract** — ≤250-word single paragraph, no headings (`pnasnexus-abstract`).
5. **Introduction** — the gap and why it matters broadly; end on what you found.
6. **Results** — argument-ordered (below).
7. **Discussion** — interpretation and broader, cross-field significance. (A combined "Results and Discussion" is acceptable where it reads better.)
8. **Materials and Methods** — **in the main text** (see below).
9. **Acknowledgments, funding, data availability, references.**

> PNAS Nexus does **not** mandate a rigid IMRaD order beyond the in-text-Methods requirement — but the order above is the conventional, reviewer-friendly shape. Confirm any type-specific structure in current guidelines.

## Materials and Methods stays in-text (a key requirement)

PNAS Nexus requires a **Materials and Methods** section **in the main text** — verbatim: *"The main text must contain a materials and methods section which provides enough information for readers to follow the experiments in the paper. This information cannot be provided solely as supporting information."* Provide enough method in the body to evaluate and reproduce the work; longer protocols and extended data go to **Supporting Information (SI)**. Do not strip the main-text Methods to chase the page count — move detail to SI instead.

## Step 3: classification (required at submission)

PNAS Nexus asks authors to file the paper under one of **three major research-area categories**, each with subcategories:

- **Biological, Health, and Medical Sciences**
- **Physical Sciences and Engineering**
- **Social and Political Sciences**

Pick the category (and subcategory) that matches the **handling and review community** you want, consistent with the venue/division call in `pnasnexus-fit`. Exact subcategory lists are **待核实** — choose from the live list in the submission system.

## Length discipline

- If you are over budget, **move detail to SI** (extended methods, supporting figures/tables, supplementary text) rather than deleting the main-text Methods.
- Remember captions and legends count toward the page budget — tighten them.
- Consider whether the work is really a **Brief Report** (≤3 pp) rather than an over-padded Research Report.

## Structure as argument, not chronology

Order the Results by the **logic of the claim**, not the order experiments were run:

1. Establish the phenomenon (the headline result).
2. Rule out the obvious alternative explanations.
3. Show the mechanism / generality.
4. Demonstrate the broad, cross-field implication.

Each Results paragraph: **claim sentence first**, then evidence (figure callout + numbers), then inference.

## Cross-references

- Main figures/tables: "Fig. 1", "Table 1".
- Supporting Information: "SI Appendix, Fig. S1 / Table S1" (confirm the exact SI labeling the journal uses); datasets as "Dataset S1".

## Output format

```
【Article type】 Research Report / Brief Report / Registered Report (S1/S2) / Perspective / Review
【Budget】 within page limit for that type? (6 pp pref / 12 max for Research Report) — captions+legends counted?
【Order check】 Title / authors / Significance / Abstract / Intro / Results / Discussion / Materials and Methods / refs — gaps?
【Methods location】 in main text? yes (FIX if only in SI) — extended detail in SI?
【Classification】 research area (Bio-Health-Medical / Physical-Engineering / Social-Political) + subcategory chosen?
【Results order】 argument-ordered, claim-first? yes/no
【Items in main vs SI】 main: [...] / SI: [...]
【Next】 pnasnexus-figures
```

## Anti-patterns

- **Do not** pick the wrong article type — a single-point study padded into a Research Report wastes the budget; a sprawling study squeezed into a Brief Report loses rigor.
- **Do not** delete the main-text Materials and Methods to fit the page count — move detail to SI.
- **Do not** put Methods *only* in Supporting Information — the journal forbids it.
- **Do not** omit the classification; it is required at submission.
- **Do not** forget that captions, legends, abstract, and Significance Statement all count toward the page budget.
