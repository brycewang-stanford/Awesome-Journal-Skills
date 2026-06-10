---
name: jhr-literature-positioning
description: Use when positioning a Journal of Human Resources manuscript against applied microeconomics, labor, education, health, development, discrimination, retirement, and policy literatures, with explicit reconciliation to prior estimates.
---

# Literature Positioning (jhr-literature-positioning)

## When to trigger

- The paper has a policy question but the contribution over prior work is fuzzy
- Prior estimates conflict with yours and need reconciliation
- The introduction reads like a general literature survey

## JHR positioning bar

JHR explicitly values whether a manuscript reconciles its results with prior
published work. Positioning must therefore do more than cite related papers: it
should explain why estimates differ across samples, designs, populations, periods,
or mechanisms.

## Checklist

- Name the closest prior estimates and their design.
- State whether your contribution is new variation, new data, new population,
  new mechanism, stronger reconciliation, or policy interpretation.
- Compare magnitude, not only sign and significance.
- Identify which prior result your analysis confirms, revises, or contradicts.
- Preview any comparative estimation you run to bridge prior results.

## Prior-estimate bridge

For each closest paper, write:

```text
[Prior paper] estimates [magnitude] for [population/design]. Our estimate differs because [sample,
policy environment, outcome, or design]. We bridge the difference by [comparative specification].
```

This makes the JHR reconciliation expectation visible in the literature section rather than deferring it
to the appendix.

## Reconciliation map

Build a compact map for the introduction team:

```text
Prior result | Population | Design | Estimate | Why comparable | Your bridge
```

Use the map to decide which papers deserve main-text comparison. A paper belongs in the first-page or
second-page narrative only if it supplies a benchmark estimate, a competing mechanism, or a policy context
that changes interpretation. Broader background can move later or disappear.

When estimates conflict, avoid the weak phrase "differences may reflect context." Say which context,
which sample, or which design component produces the difference, and point to the table that tests it.

## Vignette: bridging conflicting minimum-wage estimates

Illustrative positioning problem (all magnitudes invented): your state-panel
design finds a teen-employment elasticity of -0.12; the closest published
county-pair design reports -0.03.

1. Decompose the gap before writing: restricting your sample to border counties
   moves -0.12 to -0.06; matching the prior paper's 2005-2014 window moves it
   to -0.04. So roughly two-thirds of the gap is comparison-group choice, the
   rest is period.
2. Write the introduction sentence from the decomposition: "Our larger
   elasticity reflects statewide rather than border-county comparisons; under
   the border-pair design our estimate is statistically indistinguishable from
   the prior one."
3. Park the full bridge table in the Online Appendix and cite it at that
   sentence.

4. Close the loop in the conclusion: say which prior estimate now looks like a
   special case of yours, and what evidence would discriminate between the
   remaining explanations.

This is the JHR pattern: the literature section quantifies disagreement instead
of narrating it.

## Field benchmarks referees carry in their heads

Position against the benchmark literatures a JHR referee in each field will
expect you to know, hedging where canon is contested:

- **Labor**: minimum-wage employment debate, returns to experience and tenure,
  monopsony evidence.
- **Education**: returns to schooling, teacher and school value-added, class
  size, school-choice lotteries.
- **Health**: Medicaid and insurance expansions, early-life health shocks.
- **Discrimination**: audit and correspondence studies, decomposition methods
  and their critiques.
- **Retirement**: Social Security claiming, default and auto-enrollment
  effects.
- **Development**: schooling-and-earnings microdata work, cash transfers.

Missing the canonical comparison invites a referee to do the reconciliation for
you — on less favorable terms.

## Positioning sentences to avoid at JHR

- "To our knowledge, no paper has..." without saying why the gap matters.
- "Differences may reflect context" with no named sample or design component.
- A paragraph of citations with no magnitudes attached to any of them.
- Claiming to "extend" a literature whose estimates you never compare to yours.

## Output format

```text
[Closest prior estimate] citation + magnitude/design
[Your delta] data / design / population / mechanism / reconciliation
[Why estimates differ] ...
[Policy implication] ...
[Next step] jhr-identification-strategy
```
