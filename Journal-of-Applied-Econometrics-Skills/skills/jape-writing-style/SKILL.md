---
name: jape-writing-style
description: Use when drafting or polishing prose for a Journal of Applied Econometrics (JAE) manuscript to its house conventions — a 100-word citation-free summary, up to six keywords, sectioned structure, a conflict-of-interest statement, acknowledgments that do not thank reviewers, and citation-style-agnostic Free Format references.
---

# Writing Style for JAE (jape-writing-style)

## When to trigger

- Writing the summary (abstract), keywords, and front matter for a JAE paper
- Checking the manuscript against JAE's specific formatting conventions
- Resolving how to handle references when no house style is mandated

## JAE's specific style rules

- **Summary (abstract): no more than 100 words.** It must be understandable without reference to the rest of the paper and **contain no citations** — state the finding plainly and cut every reference.
- **Up to six keywords.** **Title without abbreviations.**
- **Numbered sections/subsections.**
- **Conflict-of-interest statement required.**
- **Acknowledgments must not thank the anonymous reviewers** (review is single-blind).
- **References: any consistent style.** JAE accepts references "in any style or format, as long as it is consistent throughout the manuscript," reinforced by **Free Format** first submission — pick one style, apply it uniformly, and do not stall on a template.

## Prose register for applied econometrics

Write so results are **transparent and replicable**: state the estimand, estimator, inference, and data plainly; report numbers with their standard errors; explain a method only as far as applied readers need to trust and use it; avoid over-claiming beyond what the design supports. Do not turn the introduction into a theory survey. Push extended derivations and robustness into the unlimited online appendix, keeping the 35-page main text tight. Mark any fact drawn from bot-blocked Wiley pages as needing live verification.

## Engineering the 100-word summary

Compress in a fixed order, cutting in this priority: citations first (mandatory — the summary carries none), then methods detail beyond the estimator's name, then motivation clauses, then hedges that the text will state anyway. What survives, in order: question, data (source + span), method in one clause, headline number with its uncertainty, and the takeaway. Worked compression (illustrative):

```text
Before (128 words, 2 citations): "A large literature following [A 2004]
and [B 2015] has examined exchange-rate pass-through... Our paper uses
state-of-the-art local projection methods with HAC corrections..."

After (78 words, 0 citations): "We estimate exchange-rate pass-through
to import prices using monthly micro data on 1,900 product lines,
2002–2023. Twelve-month pass-through is 0.31 (s.e. 0.06), about half
the aggregate consensus; the gap closes once invoicing-currency
composition is held fixed. Aggregation, not pricing behavior, explains
the discrepancy. Data and programs are available in the Journal of
Applied Econometrics Data Archive."
```

The closing archive sentence is idiomatic for this venue and costs nine words.

## Reporting estimates in JAE prose

- Every headline number travels with its uncertainty: "0.31 (s.e. 0.06)" or a bootstrap interval — never a bare point estimate in the introduction.
- Name the inference once, precisely, then stop re-explaining it: "standard errors are HAC (Bartlett, 12 lags) throughout unless noted."
- Significance language follows the test actually run: with few clusters write "wild-bootstrap p = 0.08", not "significant at 10%" as if the asymptotics were clean.
- Software and key packages are cited like literature — the deposited code names versions, and the text should not contradict it.

## Style objections and quick fixes

- "The summary assumes the reader knows the literature" → it must stand alone; delete every "in contrast to prior work" clause.
- "Notation is introduced and never reused" → cut it; applied readers need the estimator's behavior, not a second derivation (that lives in the appendix).
- "The introduction is a methods survey" → restructure: question → data → finding → lesson, with method papers cited in passing.

## Output format

```
【Summary】≤100 words, no citations, self-contained? [Y/N]
【Numbers】headline estimates carry s.e./CI in prose? [Y/N]
【Keywords】≤6? title free of abbreviations? [Y/N]
【Structure】numbered sections/subsections? [Y/N]
【Declarations】COI present; reviewers not thanked? [Y/N]
【Refs】one consistent style? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — summary cap, keywords, COI, reference-style sources
