---
name: jeg-writing-style
description: Use when polishing Journal of Economic Growth (JEG) prose — abstract, introduction, model exposition, empirical-result and magnitude-translation paragraphs, APA author-year references, keywords, JEL codes, and Springer Nature declarations for growth and comparative-development manuscripts.
---

# Writing Style (jeg-writing-style)

## When to trigger

- The paper is technically complete but the growth contribution is not legible
- Abstract, introduction, or model section needs JEG-specific tightening
- Springer metadata, APA references, declarations, or keywords need final polish

## Style principles

- Lead with the growth question and mechanism.
- State whether the paper is theoretical, empirical, or mixed.
- Translate estimates or model results into growth economics: convergence, long-run
  income, productivity, fertility, human capital, technology, institutions.
- Keep claims bounded to the sample, model, and identifying assumptions.
- Use author-year citations with an APA 7 style reference list.

## Abstract repair pattern

Use this order:

```text
Question -> growth mechanism -> method/data/model -> headline result -> scope/implication.
```

Avoid abstracts that lead with "we develop a model" or "we use a panel" without naming the growth
mechanism. For JEG, method is persuasive only after the growth question is clear.

## Mechanism-first introduction

The first two pages should answer:

- What growth fact or dynamic pattern is hard to explain?
- Which mechanism is proposed: human capital, fertility, technology, institutions, finance, migration,
  inequality, political economy, structural transformation, or another channel?
- Why does the model, data, or calibration isolate that mechanism rather than merely document an
  association?
- What changes in our understanding of long-run growth or development?

Move institutional background, data details, and calibration minutiae after this chain is visible. JEG
readers need the growth mechanism before they need the technical inventory.

## Magnitude translation rules

JEG prose converts coefficients into growth language; a raw beta is a draft, not a result:

- Long-run level effects: give log points and the implied ratio ("0.14 log points, roughly a 15% income gap").
- Growth-rate effects: annualize and compound ("0.3 percentage points of annual growth compounds to about 35% higher income over a century" — illustrative arithmetic).
- Convergence results: translate the coefficient into the half-life of the income gap.
- Calibration output: state the share of an observed gap or transition the mechanism accounts for, with the untargeted-moment fit reported alongside.
- Fertility and demographic results: express effects in children per woman and transition-timing years, then connect them to income per capita through the model's quantity-quality margin.

## Worked vignette — rewriting a persistence-results paragraph

Before (illustrative): "The coefficient on historical literacy is 0.21 and significant at the 1% level across all specifications."

After: "Districts one standard deviation above the mean in 1880 literacy have roughly 21% higher GDP per capita today (Conley SE, 250 km). Through the lens of the model, about half of this gap reflects intergenerational human-capital transmission; the remainder loads on the institutional channel examined in Section 6. Taken at face value, historical literacy differences account for an illustrative one-fifth of present-day interdistrict income dispersion."

The rewrite names the unit, the spatial inference, the mechanism split, and the aggregate stake — the four things a growth specialist scans a results paragraph for.

## Section architecture in accepted articles (hedged)

- Comparative-development empirics commonly run: introduction → historical background → data → empirical strategy → results → mechanisms → often a model rationalizing the findings → conclusion.
- Theory papers commonly run: introduction → model → equilibrium and dynamics → comparative statics or calibration → empirical or historical corroboration → conclusion.
- In both modes a long online appendix is the norm while the main text stays mechanism-first; treat these orderings as priors from recent issues and verify formatting specifics against the journal's current author guidelines.

## Submission-sensitive details

- Abstract should be 150-250 words.
- Provide 4-6 keywords and JEL classification codes.
- Include Statements/Declarations where required by Springer.
- LLMs cannot be authors; disclose LLM use if applicable.
- Use editable LaTeX source or Word files.

## Output format

```text
[Section] abstract / intro / model / empirics / conclusion
[Growth mechanism] ...
[Main edit] ...
[Metadata/declarations] ...
[Next step] jeg-submission
```
