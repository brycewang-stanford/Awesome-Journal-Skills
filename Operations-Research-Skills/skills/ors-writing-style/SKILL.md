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

## Prose pushback patterns OR referees raise (with the fix)

| Referee remark | What it really flags | Venue-specific fix |
|----------------|----------------------|--------------------|
| "Introduction is hard to follow" | equations/notation leaked into the intro | rewrite every result as a plain-language "we show that ..." line; banish all symbols |
| "Abstract is impenetrable" | symbol-laden, over 200 words | text-only rewrite stating problem, approach, headline result in prose |
| "Theorem statements are dense" | symbols precede meaning | lead each formal result with a one-sentence plain-language reading, then the math |
| "Notation is inconsistent" | symbol drift across model/proof/exhibit | one notation table; define once near first use; reconcile end-to-end |
| "Main text is bloated by proofs" | three-page derivation inline | move it to the e-companion (which must not exceed the manuscript); keep a sketch |
| "Claims feel unsupported" | assertion with no theorem/exhibit anchor | tie every claim to a proved result or a numbered exhibit; delete the rest |

These are *Operations Research* style flags, not generic copy-editing. As the INFORMS
flagship, OR enforces the equation-free intro precisely so a non-specialist optimizer,
queueing theorist, or simulation methodologist can read the contribution across
methodological silos — a bar empirical-OM venues do not set.

## Equation-free rewrite micro-example (illustrative)

Before (forbidden in the intro): "We prove that the policy minimizing
E[∑ₜ γᵗ c(xₜ,aₜ)] is a threshold rule with threshold s* solving g(s*)=0."

After (intro-legal): "We show that the cost-minimizing replenishment policy is a simple
threshold rule — order up to a single critical level — and we characterize that level."

The symbols, the discount factor, and the optimality equation move to the model section;
the introduction keeps only the decision-relevant reading. This is the single most
common style repair on first-round OR revisions.

## Self-audit before handing to ors-submission

- [ ] Introduction: zero equations, zero notation; problem + results + OR significance in words
- [ ] Abstract: text-only, ≤ 200 words, no accented variables; up to 3 keywords
- [ ] Every theorem opens with a plain-language sentence before symbols
- [ ] Single consistent notation system across model, proofs, exhibits, e-companion
- [ ] Author-year citations throughout; reference list in INFORMS convention
- [ ] Long proofs in the e-companion (≤ manuscript length), sketch retained in main text

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
