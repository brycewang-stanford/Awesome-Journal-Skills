---
name: jmr-writing-style
description: Use when polishing prose for a Journal of Marketing Research (JMR) manuscript — a third-person 200-word abstract, AMA author-year citations, the exact-statistics number conventions, and a front-loaded research argument that clears JMR's dual bar without drifting into managerial Journal-of-Marketing framing. Late-stage polish only.
---

# Writing Style (jmr-writing-style)

## When to trigger

- The abstract, intro, or prose buries the contribution
- Citations and numbers are not in AMA style
- The writing reads as a managerial pitch rather than a research argument
- Final language polish before submission (after the contribution is settled)

## JMR-specific style rules

- **Abstract**: **200 words maximum, written in the third person.** It should state the marketing question, the approach (experiment/model), the key result, and the contribution — not a teaser. (Title **≤ 25 words**; up to **8 keywords**.)
- **Citations**: **AMA author-year** style — "Thorelli (1960)" / "(Thorelli 1960)"; list all authors up to three, "et al." for four or more. There is **no reference cap**, so cite both relevant behavioral and modeling work. Not APA-numeric.
- **Numbers in prose**: report **exact p-values to three digits**, with **no leading zero** (`p = .032`, `.97`), and **no more than three decimals**; report effect sizes alongside significance. Mirror the table conventions in the text.
- **Formatting**: 12-point Times New Roman (or 12-point LaTeX font), double-spaced (tables/references may be single-spaced), 1-inch margins; no page/line numbers, no headers/footers. Keep the print article within **50 pages**.

## Write a front-loaded research argument

- Open with the **marketing phenomenon and the research question**, then the gap/tension, then what you do and find — the contribution should be visible on page one without the appendix.
- Use **active voice** and direct sentences; explain the mechanism or identification in plain terms before the technical detail.
- Keep it a **research** contribution. Managerial implications belong in the discussion as a consequence of the findings, not as the lead — leading with "what managers should do" reads as a *Journal of Marketing* paper.
- Match register to genre: behavioral papers narrate the process and converging studies; modeling papers state the question, the model intuition, then the identification.

## AI-content disclosure

If any AI-generated content is used, it must be **identified in the main document** (e.g., in Methods) and noted in the **Acknowledgments** — write these in now so the submission conforms.

## Anti-patterns

- A first-person or results-teaser abstract, or one over 200 words.
- APA-numeric citations; "p < .05" or asterisks in prose; leading zeros before decimals.
- Managerial-pitch framing that hides the research contribution.
- Polishing prose before the contribution and identification are settled.


## Style execution pass for Journal of Marketing Research

Run this as a concrete capability pass. First lock the marketing construct, data or study design, inference threat, and managerial or consumer implication; then test whether the manuscript addresses marketing reviewers who expect measurement, experiments, consumer behavior, or empirical strategy to answer a marketing question.

- **Primary move:** Rewrite the opening and transitions so the venue-level claim, evidence object, and contribution are visible before technical detail; keep house-style limits tied to the source map.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Marketing Science for quantitative modeling, Journal of Marketing for strategic managerial contribution, Journal of Consumer Research for consumer-theory depth; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```text
[Target] JMR
[Abstract] <=200 words, third person, states contribution: pass/fix
[Citations] AMA author-year: pass/fix
[Numbers] 3-digit p, no leading zero, <=3 decimals, effect sizes: pass/fix
[Argument] front-loaded, research-first (not managerial): pass/fix
[AI disclosure] present if used
[Next skill] jmr-submission
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md)
- [`../../resources/external_tools.md`](../../resources/external_tools.md)
