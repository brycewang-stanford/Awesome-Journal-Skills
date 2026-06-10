---
name: ectj-literature-positioning
description: Use when positioning an EctJ paper against econometric theory, applied econometrics, statistics, machine learning, and field-economics literatures while keeping the leading-case contribution compact.
---

# EctJ Literature Positioning

Use this to make the novelty legible to econometricians and applied users. At EctJ,
positioning is differentiation, not a survey: the journal rewards a leading-case,
path-breaking contribution under a hard limit of about 20 pages including the printed
appendix, so a sprawling related-work section is both off-fit and a budget leak. Place the
paper at a precise seam in the methodological frontier and show that seam matters in
applications.

## Positioning checks

- Identify the closest econometric object: estimator, test, identifying restriction,
  asymptotic regime, design, inference problem, or computational procedure.
- Separate the paper from exhaustive-method papers: EctJ can reward a sharp leading case,
  but the leading case must be economically useful.
- Cite adjacent statistics or ML work when the method overlaps, but explain what the
  econometric setting adds.
- Tie theory references to assumptions that the paper weakens, changes, or makes empirically
  usable.
- Explain the empirical-application literature only enough to show applied value.

## Positioning compression

Use a two-layer related-work structure:

- **Frontier layer**: the two or three econometric papers closest in object and proof strategy. State the
  exact delta: weaker assumption, different asymptotic regime, new computational route, sharper finite-sample
  diagnostic, or applied implementation.
- **Use layer**: the applied or adjacent-statistics literature that would use the method. Keep this short:
  it exists to prove applied value, not to become a field survey.

Avoid a broad "methods survey" paragraph. EctJ's page discipline means every citation should either define
the incumbent method or prove why the leading case matters.

## Output format

```text
[Nearest literatures] <econometrics/statistics/ML/application>
[Closest 3 papers] <paper -> difference>
[Leading-case contrast] <why this is not a routine extension>
[Applied-value bridge] <where users benefit>
[Missing citations] <must add before submission>
```
