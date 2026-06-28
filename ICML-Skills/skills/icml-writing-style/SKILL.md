---
name: icml-writing-style
description: Use when rewriting a machine-learning paper for ICML-style claims, 8-page clarity, soundness/originality/significance framing, impact statement, lay-summary readiness, and reviewer-updateable rebuttal posture.
---

# ICML Writing Style

ICML writing has to make a rigorous ML contribution clear inside a tight 8-page body. The style is
less about broad excitement and more about soundness, originality, significance, clarity, and
reproducibility.

## Introduction shape

1. Define the ML problem precisely.
2. State what prior methods, theory, or evaluations fail to cover.
3. Give the contribution in a form a reviewer can evaluate: method, theorem, benchmark, empirical
   finding, system, or analysis.
4. Preview the evidence: proof, ablation, baseline, dataset, or reproducibility artifact.
5. Bound the claim and point to appendices only for support, not for the main idea.

## Style rules

- Put critical evidence in the main body, not only in appendices or supplement.
- Use claims that can be mapped to soundness, originality, significance, and clarity.
- Name assumptions and constraints early.
- Keep the impact statement factual and proportionate.
- Avoid prompt-injection text, identity hints, and non-anonymous repository references.
- Write with the knowledge that original submissions and rebuttal may become public if accepted.

## Review-dimension map

Before polishing language, map each major paragraph to what an ICML reviewer is being asked to score.
This prevents a cleanly written paper from still reading as underspecified.

| Review dimension | Main-body writing obligation | Failure mode to remove |
| --- | --- | --- |
| Soundness | State assumptions, training/evaluation protocol, and uncertainty around the result | theorem or experiment appears only in appendix |
| Originality | Name the closest prior work and the exact technical difference | novelty rests on adjectives like "new" or "first" |
| Significance | Explain who gains what capability and under which regime | contribution sounds like a narrow leaderboard bump |
| Clarity | Put definitions, notation, and evidence order before dense results | reviewer must reconstruct the claim from tables |
| Reproducibility | Point to code/data/artifact or explain the missing piece | artifact promise is vague or post-deadline dependent |

If a contribution does not map cleanly to at least one dimension, cut it from the main claim or move
it to a lower-priority paragraph.

## PMLR two-column discipline

ICML proceedings appear in PMLR's two-column format, so prose must survive narrow columns: short
sentences, equations that do not overflow, and figures legible at column width. Front-load the
contribution because the heavy reviewer load means the first column of page one carries
disproportionate weight; a buried thesis reads as a weak thesis. Check the current style file rather
than assuming last year's margins.

## Eight-page evidence budget

Treat the 8-page body as an evidence budget, not just a length limit.

| Page zone | Must earn space by doing this | Move out if... |
| --- | --- | --- |
| First column | Problem, gap, contribution, and strongest evidence anchor | it is background a reviewer already knows |
| Method section | Defines the object being evaluated and the assumption regime | detail is implementation-only and not needed for soundness |
| Theory / analysis | States theorem intuition and assumptions before formal detail | proof mechanics can live in appendix without changing trust |
| Experiments | Shows baseline choice, ablation, uncertainty, and failure case | table only supports a secondary claim |
| Impact statement | Names realistic benefits, limits, and risks | it becomes promotional or generic |

Every strong claim in the introduction should point to a page-zone anchor. If the only support is in
the appendix, soften the claim or bring the support into the body.

## Claim calibration table

| Overclaim pattern | ICML reviewer reaction | Calibrated rewrite |
| --- | --- | --- |
| "Our method is state of the art" | Asks which tuned baselines, which regime | "Improves over tuned X on Y under stated budget" |
| "Provably converges" | Checks whether assumptions match experiments | "Converges at rate R under assumptions A, observed in-regime" |
| "Generalizes broadly" | Wants scaling evidence | "Holds across the model sizes and datasets we test" |

Add a public-record pass after calibration. If the paper is accepted, the original submission,
reviews, rebuttal, and discussion can be visible, so claims should remain defensible after response.
Replace "we will show" or "details forthcoming" with the exact evidence already present. Replace
private-code promises with anonymized, deadline-stable artifact language that matches the actual
submission package.

## Worked vignette: framing an optimizer contribution

For a paper pairing a non-convex convergence theorem with deep-learning benchmarks, the introduction
states the optimization problem, names the rate prior methods cannot match, gives the theorem and the
benchmark win as separable contributions, and bounds the claim to the assumption regime. This lets a
loaded reviewer extract soundness, originality, and significance from one column without hunting the
appendix.

## Output format

```text
[Claim before] <original>
[Claim after] <ICML-calibrated version>
[Evidence anchor] <proof/experiment/baseline/artifact>
[Review dimension] soundness / originality / significance / clarity / reproducibility
[Page-zone anchor] first column / method / theory / experiments / impact
[Impact statement note] <needed addition or narrowing>
[Public-record pass] original/rebuttal/discussion wording remains defensible? [Y/N]
[8-page compression] <what to cut or move>
```
