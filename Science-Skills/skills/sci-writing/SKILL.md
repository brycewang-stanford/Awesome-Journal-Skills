---
name: sci-writing
description: Use when choosing the Science (AAAS) Research Article format (standard vs extended online) and holding its length and structure budgets — main-text word caps, figure caps, argument-ordered Results, and deciding what belongs in the main text versus Supplementary Materials.
---

# Main-Text Writing & Format (sci-writing)

## When to trigger

- Unsure whether the work fits the **standard Research Article** budget or needs the **extended online format** (Science no longer lists a separate Report category).
- The main text is over length, or Methods are bloating the body.
- The structure wanders (lab-notebook order instead of argument order).
- Co-authors keep adding paragraphs and the paper is creeping past budget.

## Pick the format first

| Format               | Use when                                                | Main-text cap | Display items | Main-text refs |
|----------------------|---------------------------------------------------------|---------------|---------------|----------------|
| **Research Article (standard)** | The default for all peer-reviewed research papers | ≤ 3,000 words | 3–5 (figs+tables) | ~50 |
| **Research Article (extended online format)** | Rare cases whose results cannot be presented within the standard constraints; the cover letter must justify the extra length | ≤ 6,000 words | ≤ 6 (may include videos) | ≤ 100 |

> Caps from the *Science* Information for Authors page (re-verified 2026-11-23; see `resources/official-source-map.md`). *Science* no longer lists Reports as a separate category — older ~2,500-word Report / ~4,500-word Research Article budgets are obsolete. The principle is fixed: **Science main texts are short**, and most detail lives in Supplementary Materials.

## What goes where

- **Main text (Research Article)**: divided into sections with brief subheadings; lean, results-and-interpretation narrative. **Materials and Methods are NOT in the main text** — they go to Supplementary Materials with enough detail to allow replication.
- **Supplementary Materials**: full Materials and Methods, supplementary figures/tables, supplementary text, captions, and additional data. This is where rigor lives without bloating the body.

## Structure as argument, not chronology

Order the Results by the **logic of the claim**, not the order experiments were run:

1. Establish the phenomenon (the headline result).
2. Rule out the obvious alternative explanations.
3. Show the mechanism / generality.
4. Demonstrate the broad implication.

Each Results paragraph: **claim sentence first**, then the evidence (figure callout + numbers), then the inference.

## Length discipline tactics

- One idea per paragraph; lead sentence is the claim.
- Move any sentence that a general reader can skip → Supplementary.
- Methods detail, validation, controls → Supplementary (cited as "fig. S3", "table S1").
- Cut "In order to" → "To"; cut "It is worth noting that"; cut throat-clearing.

## Before/after: compressing to the Science register

Science prose earns its word budget sentence by sentence. Typical compressions:

| Draft (lab-report register) | Science register |
|-----------------------------|------------------|
| "In order to investigate whether X affects Y, we performed a series of experiments in which…" | "To test whether X affects Y, we…" |
| "It is worth noting that the observed effect was statistically significant (p < 0.05)." | "The effect was robust (Δ = 12 ± 2%, P = 0.003, n = 14)." |
| "As can be seen in Fig. 2, there appears to be a trend toward increased activity." | "Activity increased threefold (Fig. 2)." |
| "These results may suggest a possible role for Z in this process." | "Z is required for this process (fig. S4)." |

The pattern: verbs over nominalizations, numbers over adjectives, one hedge maximum per claim, and every figure callout attached to a quantitative statement rather than "as shown in".

## What Science referees expect from the body text

- Each Results paragraph is checkable: a referee can match the claim sentence to a specific panel and a specific statistic without hunting.
- Alternative explanations are ruled out **in the main text**, even if the ruling-out data live in the SM ("this was not due to A or B; figs. S5 and S6").
- The final paragraph states scope and limits in one or two sentences — referees at a general-science weekly flag manuscripts whose conclusions quietly exceed the shown systems or conditions.
- No forward references to unpublished work as load-bearing evidence.

## Reference and supplement cross-refs

- Main figures: "Fig. 1"; supplementary: "fig. S1" (lowercase f); tables: "Table 1" / "table S1".
- Supplementary Materials are cited in the main text and listed at the end.

## Output format

```
【Format】 Research Article standard (≤3,000w / 3–5 items / ~50 refs) or extended online (≤6,000w / ≤6 items / ≤100 refs)
【Current main-text word count】 N → over/under budget by M
【Methods location】 main text (FIX → move to SM) / Supplementary (ok)
【Results order】 argument-ordered? yes/no
【Items in main vs SM】 main: [...] / SM: [...]
【Next】 sci-figures
```

## Anti-patterns

- **Do not** keep a full Methods section in the main text — it belongs in Supplementary Materials.
- **Do not** structure Results chronologically when a logical order is clearer.
- **Do not** treat the word cap as negotiable by shrinking font in figures — move content to SM instead.
- **Do not** add a standalone Discussion that repeats Results; integrate the interpretation.
