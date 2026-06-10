---
name: psychbull-writing-style
description: Use when drafting and polishing a Psychological Bulletin manuscript so it reads as an integrative synthesis and meets APA 7th-edition style plus MARS/PRISMA/JARS reporting structure, including the ≤ 250-word abstract. Guides prose and structure; it does not run the analysis.
---

# Writing Style (psychbull-writing-style)

Psychological Bulletin prose must do something a primary paper's does not: **integrate and evaluate an
entire literature** while meeting **APA 7th-edition** style and the matching reporting standard —
**MARS** for meta-analyses, **PRISMA** for systematic reviews, **JARS** for quantitative/mixed work.
This skill guides structure and prose; the numbers come from the analysis skills.

## When to trigger

- Drafting or restructuring the manuscript
- Writing the **≤ 250-word abstract**
- Making sure the methods section satisfies MARS/PRISMA item-by-item
- Tightening an over-long or descriptive review into an evaluative argument

## Structure for a synthesis

1. **Introduction** — the open question, why the field disagrees, what a synthesis can resolve; the
   contribution, not a study-by-study recap.
2. **Method (MARS/PRISMA)** — eligibility criteria, **search** (databases, strings, dates, counts),
   screening, **coding and reliability**, effect-size metric, **model**, heterogeneity, moderators, and
   **bias** plans. Written so an item-by-item MARS/PRISMA check passes.
3. **Results** — pooled effect with CI and prediction interval, heterogeneity, moderators, bias
   diagnostics, sensitivity; lean on the exhibits (forest/funnel/PRISMA).
4. **Discussion** — the theoretical contribution, scope conditions, limitations of the *evidence base*,
   and a research agenda (see `psychbull-theory-integration`).

## The abstract (≤ 250 words)

- State the question, the **synthesis type**, the size of the literature (**k**), the **pooled effect**,
  key **moderators**, and the **bottom line** on robustness. APA structured-abstract conventions help.

## Evaluative, not descriptive

- **Synthesize, don't annotate.** Group studies by argument and finding, not one paragraph per paper.
- Write for the **whole field**: define constructs and methods so non-specialists follow.
- Keep terminology and effect-size language **consistent** with the exhibits and tables.
- **Masked**: no author clues in the text; neutralize self-citations (see `psychbull-submission`).

## Anti-patterns

- An "annotated bibliography" that lists studies instead of integrating them
- A method section that omits search strings/dates/counts (fails PRISMA/MARS)
- An abstract over 250 words, or one with no k / pooled effect / bottom line
- Burying the contribution under descriptive summary
- Inconsistent effect-size terms between text, tables, and figures

## The prose bar that separates a Bulletin synthesis from a methods report

As the APA's flagship integrative-review outlet, Psychological Bulletin rewards prose that *argues*
about a literature, not prose that merely catalogs it. Referees read for an evaluative voice:

| Writing dimension | Reads as a Bulletin synthesis | Reads as a methods-only report (reject risk) |
|-------------------|-------------------------------|----------------------------------------------|
| Introduction | Frames the field's unresolved tension | Recaps each study in turn |
| Organization | Grouped by argument and mechanism | One paragraph per paper, chronologically |
| Results prose | Ties the pooled estimate to the open question | Dumps coefficients with no interpretation |
| Discussion | Advances or refines a theoretical account | Restates the forest plot in words |
| Audience | Written for the whole discipline | Assumes the reader is a meta-analysis specialist |

## Worked vignette — writing up the intervention synthesis

*Illustrative numbers only.* For the self-affirmation synthesis (k = 42, g = 0.34 [0.24, 0.44],
I² = 68%, bias-adjusted toward ≈ 0.25), the write-up under this skill's rules:

- **Abstract (≤ 250 words)** names the synthesis type, k = 42, the pooled g and CI, the delivery-format
  moderator, and the bottom line that the effect is positive but likely inflated by selective reporting.
- **Method** is written so a MARS reviewer can tick each item: databases and dated strings, screening
  and reliability (κ = 0.81), Hedges' g with small-sample correction, a random-effects/RVE model, and
  the pre-registered moderator and bias plan.
- **Results** lead with the prediction interval, not just the CI, so the 68% heterogeneity is honest in
  the prose, then walk through the converging bias diagnostics.
- **Discussion** explains *why* earlier studies disagreed (delivery format) rather than re-listing them.

## Referee pushback → venue-specific fix

- *"This reads as an annotated bibliography."* → Re-outline around arguments and mechanisms; merge the
  per-paper paragraphs into thematic syntheses.
- *"The abstract omits the headline numbers."* → Insert k, the pooled effect with CI, and the robustness
  bottom line within the 250-word cap.
- *"The method won't pass a MARS item check."* → Add the missing search strings, dates, counts, and the
  reliability statistic, item by item.

## Output format

```
【Structure】intro / method(MARS-PRISMA) / results / discussion present? [Y/N]
【Method completeness】search + coding + model + bias all described? [Y/N]
【Abstract】≤ 250 words; states k + pooled effect + bottom line? [Y/N]
【Evaluative】synthesizes vs annotates? [Y/N]
【APA 7th + masked】consistent style, no author clues? [Y/N]
【Next】psychbull-open-science-and-transparency
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — APA-style reference managers; MARS/PRISMA/JARS standards
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — APA 7th, 250-word abstract, MARS/PRISMA/JARS requirements
