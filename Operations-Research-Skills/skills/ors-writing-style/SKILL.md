---
name: ors-writing-style
description: Use when polishing the prose and notation of an Operations Research (OR) manuscript — enforcing the equation-free introduction, the text-only abstract under 200 words, clean theorem-proof exposition, and INFORMS author-year house style. Polishes language and house style; it does not formulate the model (ors-theory-development) or run the submission preflight (ors-submission).
---

# Writing Style & House Style (ors-writing-style)

## When to trigger

- Drafts are complete and you want them to read like an *Operations Research* paper.
- The introduction contains equations, or the abstract is over 200 words or full of symbols.
- You need consistent notation, theorem exposition, and author-year citations.

## OR's distinctive style rules

- **Equation-free introduction (hard rule):** the introduction must clearly state the
  **problem, the results, and their significance to the OR community** and must
  **contain no equations or mathematical notation**. Write each result as "we show
  that ..." in plain language. This is a distinctive OR accessibility requirement.
- **Abstract:** must **not exceed 200 words** and should be **text-only** — minimize
  math symbols and avoid accented variables. State the problem, approach, and headline
  result in prose.
- **Keywords:** up to **three**.
- **Citations:** **author-year** style, e.g., "(Norman 1977)" or "Norman (1977)".
  Keep the reference list in the INFORMS author-year convention.

## Theorem-proof exposition

- Lead each formal result with a one-sentence plain-language statement of what it means
  before the symbols.
- Keep the **main text** focused on ideas and proof sketches; route long proofs to the
  **e-companion** (which must not be longer than the manuscript).
- Define notation once, near first use; provide a notation table if the model is heavy.
- Use consistent symbols across model, theorems, exhibits, and appendix.

## Format and clarity

- **Manuscript format:** 1.5-spaced, **11-point** font, **1-inch** margins; submit as a
  **PDF** (source LaTeX/Word on acceptance); use the provided **LaTeX style files**.
- Prefer precise, active prose; avoid vague "novel/important" without the specific
  delta (that lives in `ors-contribution-framing`).
- Make every claim either proved (cite the theorem) or empirically supported (cite the
  exhibit) — no unsupported assertions.

## Anti-patterns

- Equations or notation in the introduction (violates the equation-free rule).
- A 250-word, symbol-laden abstract.
- Mixing citation styles or drifting from author-year.
- Dumping a three-page proof into the main text instead of the e-companion.
- Notation that changes between the model section and the proofs.

## Output format

```
【Intro】equation-free? problem/results/significance in words? 
【Abstract】≤200 words, text-only? word count: ...
【Citations】author-year consistent? 
【Theorem exposition】plain-language lead + e-companion routing?
【Format】1.5-spaced / 11-pt / LaTeX style files
【Next step】ors-submission
```
