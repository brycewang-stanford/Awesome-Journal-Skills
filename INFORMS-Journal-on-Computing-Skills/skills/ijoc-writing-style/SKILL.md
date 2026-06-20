---
name: ijoc-writing-style
description: Use when the prose, abstract, or introduction of an INFORMS Journal on Computing (IJOC) manuscript buries the computational advance or misreads the house voice. Makes the method land for an OR-meets-CS readership; it does not change the underlying results.
---

# Writing Style (ijoc-writing-style)

## When to trigger

- The abstract reads like an application summary and never states the computational advance
- The introduction takes pages to reach "what is new computationally"
- The method section is unreadable prose where pseudocode and structured statements belong
- The paper is over the **25-page limit** and needs tightening, not just trimming
- A coauthor wants the draft to read like an IJOC paper, not a CS conference paper or an OR theory paper

## The IJOC voice

IJOC readers are OR/MS researchers comfortable with computation and CS researchers comfortable with OR — write for both. The voice is **precise, methods-forward, and quantitative**: state the problem, state the method, state what it provably and empirically achieves, in that order. Avoid two failure modes the readership notices instantly — the *application-essay* voice that delays the method, and the *CS-conference* voice that drops OR rigor (no problem formulation, no fair baseline discussion). The house format reinforces brevity: single-column, 1.5-spaced, 12-point, 1-inch margins, with a **≤300-word abstract carrying no formulas or mathematical notation** (检索于 2026-06；以官网为准).

## The abstract: three moves in ≤300 words

IJOC's guidance is to cover, without notation: (1) **research questions and challenges** — the OR problem and why it is computationally hard; (2) **methodology and results** — what you designed and what it achieves; (3) **importance and implications** — why the computational advance matters. Lead the second move with the magnitude ("solves instances an order of magnitude larger"), not the technique name alone. Because formulas are barred, describe the method in words a non-specialist in your sub-area can follow.

## The introduction: reach the contribution fast

By the end of page one the reader should know the OR problem, why existing methods fall short computationally, what you do, and by how much. Use the **contribution sentence** from `ijoc-contribution-framing` near the top, then a short bulleted list of contributions. Defer the literature deep-dive; do not open with a multi-page survey.

## Method prose, equations, and pseudocode

Write algorithms as **numbered pseudocode**, not paragraphs; reserve prose for the *idea* and the *invariants*. Number and reference every equation you rely on. State theorem assumptions in the theorem, not three pages earlier. Define notation once, in a table if it is heavy. The reader should be able to re-implement from the paper plus the deposit — that is the IJOC standard.

## Fitting the page limit

The **main paper is capped at 25 pages including references, tables, and figures**, with up to **10 further pages of appendices**; longer appendices move to online supplements, and code/data live in the GitHub deposit (not the page count). Tighten by moving long proofs and exhaustive result tables to the supplement/deposit while keeping the **main paper self-contained on its central claims** — a reader must be able to follow the contribution without the supplement.

## Word choices that signal computational rigor

Small lexical habits mark an experienced IJOC author. Say "on standard benchmark instances" rather than "on our test problems"; "within the same time limit / at equal wall-clock" rather than "faster"; "the performance profile shows" rather than "results indicate"; "we prove" only when you do, otherwise "we observe empirically." Report numbers with their units and conditions inline (e.g., "31% root-gap reduction on the full set, single-threaded, 1-hour limit"), so a skimming reviewer absorbs the conditions with the claim. Avoid hedge-words ("somewhat," "quite") around quantitative results — give the magnitude instead. This register is what tells the Area Editor the paper was written by someone who runs experiments seriously.

## Checklist

- [ ] Abstract ≤300 words, no formulas, covering questions/challenges → methodology/results → importance
- [ ] Page one delivers problem, gap, method, and magnitude
- [ ] Contribution sentence appears early and matches the abstract and conclusion
- [ ] Algorithms in numbered pseudocode; equations numbered and referenced
- [ ] Notation defined once; theorem assumptions stated locally
- [ ] Within 25 main pages (+≤10 appendix); main paper self-contained on central claims
- [ ] Voice is methods-forward — neither application essay nor formulation-free CS paper

## Anti-patterns

- An abstract that summarizes the application and never states the computational advance
- A formula or heavy notation in the abstract (against IJOC guidance)
- A multi-page survey before the contribution
- Algorithms described in dense prose instead of pseudocode
- Over the page limit because raw result tables and full proofs sit in the main text
- A main paper that cannot be understood without the online supplement

## Output format

```text
【Journal】INFORMS Journal on Computing
【Skill】ijoc-writing-style
【Abstract】≤300 words, no formulas, 3 moves present? [Y/N]
【Page-one contribution】problem+gap+method+magnitude? [Y/N]
【Pseudocode/equations】algorithms numbered; equations referenced? [Y/N]
【Length】≤25pp main (+≤10 appendix); self-contained? [Y/N]
【Voice】methods-forward, not app-essay / not formulation-free CS? [Y/N]
【Next skill】ijoc-submission
```
