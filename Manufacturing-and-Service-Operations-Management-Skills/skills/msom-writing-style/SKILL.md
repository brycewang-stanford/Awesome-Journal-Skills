---
name: msom-writing-style
description: Use when polishing the prose of a Manufacturing & Service Operations Management (M&SOM) manuscript — front-loading the operational insight, controlling mathematical notation, writing the structured abstract, and applying INFORMS author-year house style within the 32-page typeset cap. Late-stage polish; do not invoke before the model/identification is settled.
---

# Writing Style (msom-writing-style)

## When to trigger

- The introduction buries the operational insight under notation or literature
- The structured abstract is missing a required part or is jargon-heavy
- Notation is dense, inconsistent, or front-loaded before motivation
- You are reconciling the manuscript to INFORMS author-year style and the page cap

## Lead with the operations insight, not the math

M&SOM readers are operations researchers, but the journal prizes **clarity** and **managerial relevance** alongside technical validity. Open by stating the **operational problem, the decision, and the insight** in words before equations. Introduce notation only when it is needed; a reader should grasp the contribution from the introduction without parsing a model. For analytical papers, narrate the *structure* of the result ("the optimal policy is a threshold that…") rather than dumping the theorem first.

## Write the mandatory structured abstract

The abstract is **structured, ≤ 300 words, and free of technical jargon**, with three required subsections: **Problem definition**, **Methodology-results**, and **Managerial implications**. Draft each as one or two plain sentences. The Managerial-implications subsection is required — never drop it or fill it with notation.

## Control notation and structure

- Define every symbol on first use; keep a consistent, minimal notation set; consider a notation table in the supplement.
- Keep proofs out of the main flow (online supplement, ≤ 16 pages); in the body, give intuition for why each result holds.
- Section structure typically runs problem/motivation → model or design → results/structure → numerical or empirical study → managerial insights → conclusion.

## House style and the page cap

Use **INFORMS author-year (author-date)** in-text citations with cited pages where appropriate; order the reference list by first author, number of authors, then year (INFORMS style file v1.6). Write inside the official template — the **32-page cap includes references, tables, figures, and appendices**, so tighten prose and push overflow to the supplement rather than shrinking margins or fonts (the template fixes 11-pt, one column, 1-inch margins).

## Checklist

- [ ] Introduction states problem/decision/insight in words before notation
- [ ] Structured abstract: all three required sections, ≤300 words, jargon-free
- [ ] Notation defined on first use; minimal and consistent
- [ ] Proofs moved to the supplement; intuition kept in the body
- [ ] INFORMS author-year citations; reference order per style file v1.6
- [ ] Manuscript fits the 32-page typeset cap (overflow to ≤16-page supplement)

## Anti-patterns

- A theorem-first introduction with no plain-language operational insight.
- A structured abstract missing Managerial implications or full of symbols.
- Re-deriving results in the body that belong in the supplement.
- Reference list in a non-INFORMS style straight from the reference manager.
- Shrinking fonts/margins to beat the page cap instead of cutting prose.

## Prose moves that pass M&SOM's clarity bar

M&SOM weights clarity and managerial relevance alongside validity, so the prose is graded. Narrate the policy *form* before the theorem; defer notation rather than dumping symbols up front; turn a closing "implications for managers" nod into a specific decision rule; write the abstract in the required structured subsections; and beat the page cap by cutting prose, never by shrinking the template. The test: a competent operations practitioner should grasp the decision, the insight, and the managerial takeaway *without parsing a single equation*.

## Worked micro-example (illustrative)

Vignette: an analytical paper on dynamic capacity allocation for a cloud-computing provider. A theorem-first opening reads "Proposition 1 establishes the value function is concave and the optimal admission policy monotone." The M&SOM rewrite leads with the insight in words: "When demand is volatile, reserve capacity for high-value jobs up to a threshold that *tightens as volatility rises*." The managerial-implications subsection then carries one plain sentence with an illustrative magnitude — thresholding lifts revenue per server-hour by roughly 8% over first-come-first-served. Same result; the operations insight now leads.

## Referee-pushback patterns and the venue fix

- *"The introduction is impenetrable until I read the model."* → Move the operational insight to the first paragraph; defer notation.
- *"The structured abstract is jargon-heavy or missing a section."* → Rewrite the required subsections in practitioner language; never drop managerial implications. Keep proofs in the supplement and intuition in the body, respecting the page cap by cutting prose, not formatting.

## Output format

```
【Intro】operational insight stated before notation? ...
【Structured abstract】three required sections present; ≤300 words; jargon-free ...
【Notation】defined / minimal / consistent ...
【Proofs】in ≤16-page supplement; intuition in body ...
【Style & cap】INFORMS author-year; within 32 typeset pages ...
【Next step】msom-submission
```
