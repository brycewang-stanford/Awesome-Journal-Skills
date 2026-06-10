---
name: ectj-literature-positioning
description: Use when positioning a The Econometrics Journal (EctJ) paper against econometric theory, applied econometrics, statistics, and machine-learning literatures while keeping the leading-case contribution compact under the roughly 20-page RES format, including the frontier-versus-use citation split.
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

## Citation placement rule

Place each citation where it changes the reader's belief:

- In the introduction, cite only the incumbent method, the nearest unresolved limitation, and the applied
  use case that makes the method worth publishing.
- In the theory section, cite papers that justify assumptions, asymptotic regimes, or proof strategies.
- In the simulation section, cite designs that explain the benchmark data-generating processes or
  competitor procedures.
- In the application section, cite field papers only to explain why the empirical setting is a useful
  diagnostic for the econometric contribution.

If a citation cannot be assigned to one of those jobs, move it to a short related-work paragraph or cut it.
This keeps EctJ positioning sharp enough to survive the page constraint while still showing command of the
econometric frontier.

## Reading the EctJ frontier before claiming a seam

The journal sits in the close intellectual orbit of the UK econometrics community, including
cemmap and its working-paper series, so the relevant frontier often lives in recent working papers
rather than published volumes. Before fixing the delta:

- Sweep recent EctJ issues and the cemmap working-paper series for the same econometric object;
  a published-only sweep at this venue routinely misses the actual nearest neighbor.
- Check whether the nearest neighbor is an identification result, an estimator, or an inference
  procedure; the delta sentence must compare like with like.
- If the closest work is in statistics or ML, add the econometric translation: which economic
  parameter, sampling frame, or policy question changes the problem.

## Worked delta statement

Vignette with illustrative content: a paper proposing inference for synthetic-control estimates
with several treated units might write the frontier layer as: "Paper A gives conformal inference
for one treated unit; Paper B gives asymptotics as both panel dimensions grow; we give a
permutation-based test valid with three to ten treated units and short panels, the range covering
most published applications." One sentence, three named deltas, an applied range — that is the
positioning density the compact EctJ format rewards. If the delta needs a paragraph of caveats,
the seam is wrong, not the writing.

## Output format

```text
[Nearest literatures] <econometrics/statistics/ML/application>
[Closest 3 papers] <paper -> difference>
[Leading-case contrast] <why this is not a routine extension>
[Applied-value bridge] <where users benefit>
[Missing citations] <must add before submission>
```
