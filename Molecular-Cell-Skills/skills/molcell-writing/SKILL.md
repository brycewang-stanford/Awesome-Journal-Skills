---
name: molcell-writing
description: Use to structure a Molecular Cell Article and hold its length — Summary, Introduction, Results, Discussion, STAR Methods, figure legends, references — with the ~7,000-word main-text and ~7-display-item budgets, and Results subheadings that carry the single-mechanism argument.
---

# Main-Text Writing & Structure (molcell-writing)

## When to trigger

- Unsure how a Molecular Cell Article is structured.
- The main text is over length, or the Discussion repeats the Results.
- The Methods are written as a free-text section (Molecular Cell uses STAR Methods).
- Results wander through techniques instead of advancing the single-mechanism argument.

## Molecular Cell Article structure (in order)

1. **Summary** — single paragraph (`molcell-summary`).
2. **Introduction** — ~3 short paragraphs posing the molecular question (`molcell-framing`).
3. **Results** — the bulk; organized by the proof of mechanism, **with descriptive subheadings**.
4. **Discussion** — concise interpretation, model, limitations; does **not** re-list results.
5. **STAR Methods** — Structured, Transparent, Accessible Reporting (`molcell-star-methods`).
6. **Figure legends** — each stands alone (title + per-panel + statistics).
7. **References** — Cell Press numbered style (`molcell-citation`).
8. **Supplemental information** — supporting figures/tables/videos.

> Molecular Cell does **not** use a free-text Methods section — methods live in **STAR Methods** with a Key Resources Table. This is non-negotiable for Cell Press.

## Length and display-item budget (verify on the official site)

- **Article main text** ≈ **7,000 words**, counting Introduction, Results, Discussion, **and main figure legends**, but **excluding** STAR Methods, supplemental item legends, and references. A working target — confirm the current cap.
- **Display items**: up to **~7** figures/tables for a standard Article; additional supporting items go to Supplemental Information.
- **Short Article**: ~**4,000 words** for a single, fully validated conceptual point — consider it when the mechanism is decisive but compact.
- STAR Methods and references sit outside the main-text word budget but have their own expectations.

> Numbers are working targets. The principle is fixed: Molecular Cell Articles are deep but tightly written; validation and orthogonal controls go to Supplemental Information and STAR Methods.

## Results: subheadings that carry the mechanism

- Use **descriptive subheadings** that read as molecular claims ("The clamp loader gates ATP hydrolysis", not "Biochemical assays").
- Each Results block: **claim sentence first**, then the evidence (figure callout + numbers + statistics), then the inference and the alternative you exclude.
- Order by the **logic of the proof** (phenomenon → mechanism → separation-of-function → physiological relevance), not by the chronology of experiments.
- Each subheading should map to one or two figures.

## Discussion discipline (concise)

- Interpret — don't recap. State the molecular **model** the data support and draw it in words.
- Address the **main alternative mechanism** and how your data exclude it.
- State **limitations** honestly (what the reconstitution omits, what the resolution cannot resolve).
- End on the mechanistic significance / open molecular question — not "more work is needed."

## Length discipline tactics

- One idea per paragraph; lead with the claim.
- Move orthogonal confirmations, titrations, and controls to Supplemental (cited "Figure S3", "Table S1").
- Cut "In order to" → "To"; cut "It is worth noting that" and throat-clearing.
- Demote any result that doesn't serve the single mechanism; comprehensiveness is not a virtue here.

## Cross-references

- Main figures: "Figure 1" (Cell Press spells out "Figure"); panels "Figure 1A".
- Supplemental: "Figure S1", "Table S1", "Video S1".
- STAR Methods sections are referenced by name (e.g., "see STAR Methods").

## Output format

```
【Sections present】 Summary / Intro / Results / Discussion / STAR Methods / legends / refs
【Methods format】 free-text (FIX → STAR Methods) / STAR Methods (ok)
【Main-text length】 ~N words incl. main legends → over/under ~7,000 (or ~4,000 Short Article)
【Display items】 N → within ~7? main vs Supplemental split
【Results subheadings】 molecular-claim style + proof-ordered? yes/no
【Discussion】 interpretive (model + excluded alternative)? limitations stated? yes/no
【Next】 molcell-figures
```

## Anti-patterns

- **Do not** write a free-text Methods section — Molecular Cell requires STAR Methods.
- **Do not** let the Discussion re-list the Results.
- **Do not** order Results by technique chronology when the proof order is clearer.
- **Do not** pad the main text with arc-irrelevant experiments to look comprehensive.

> Confirm exact word and item caps against the current Molecular Cell information-for-authors page.
