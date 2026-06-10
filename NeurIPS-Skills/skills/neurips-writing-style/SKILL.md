---
name: neurips-writing-style
description: Use when rewriting a machine-learning paper for NeurIPS-style contribution framing, calibrated claims, contribution-type alignment, limitations, broader-impact prose, and language that pre-fills the mandatory NeurIPS Paper Checklist, for either the main track or the Datasets & Benchmarks track.
---

# NeurIPS Writing Style

NeurIPS writing must make a technical contribution legible to reviewers outside the authors' exact
subfield. Good style is precise, evidence-calibrated, and checklist-aware.

## Introduction pattern

1. Name the problem and why current ML practice cannot solve it.
2. Identify the specific gap in method, theory, data, evaluation, system, or understanding.
3. State the contribution type and why it fits NeurIPS.
4. Preview the evidence that supports the claim.
5. Bound the claim with limitations, assumptions, or failure modes.

## Style rules

- Prefer falsifiable claims over broad adjectives.
- Tie every headline result to a baseline, dataset, theorem, ablation, or user/deployment context.
- Use "we show" only when the paper actually proves or demonstrates the claim.
- Do not bury limitations; NeurIPS reviewers are instructed to reward honest limitation reporting.
- Avoid "state of the art" unless the comparison set, metric, and time boundary are explicit.
- Document non-standard agent or LLM use in the method when it is part of the research procedure.

## Write so the prose pre-answers the checklist

The mandatory NeurIPS Paper Checklist asks each "yes" answer to point at where the paper supports
it. Treat checklist items as a prose target, not a postscript: every "yes" should already have a
sentence reviewers can find. Drafting against these anchors removes most "claim broader than
evidence" comments before review.

| Checklist theme | Sentence the body should already contain |
| --- | --- |
| Claims match results | "We show X under assumptions A; we do not claim X holds when B." |
| Limitations | a labeled limitations paragraph naming failure modes and unscaled regimes |
| Theory assumptions | each theorem states its assumptions and forward-references the proof |
| Reproducibility | one sentence pointing at code, configs, seeds, and compute |
| Broader impact | concrete, non-boilerplate discussion of misuse or societal effect, not "no impact" |
| Datasets & Benchmarks | provenance, license, consent, and intended-use sentences for any released data |

The broader-impact statement is a NeurIPS norm, not a generic ethics paragraph: hedge to the current
year's checklist for exact wording and required placement.

## Reviewer-pushback rewrites

| Reviewer comment | Root cause in prose | NeurIPS-specific fix |
| --- | --- | --- |
| "Claims exceed evidence" | adjectives where a baseline should be | scope the claim to the tested regime; cite the table |
| "Where is the limitation?" | limitations hidden or absent | a visible labeled paragraph reviewers can reward |
| "Impact statement is boilerplate" | generic "no societal impact" | a specific misuse/benefit tied to this method or dataset |
| "Contribution type unclear" | intro reads as generic ML | name the declared type and what evidence it demands |
| "Novelty over a topic, not a mechanism" | abstract sells a label | state the technical delta against the closest method |

## Worked vignette: a new optimizer paper

A paper proposes a curvature-aware optimizer and writes "our method achieves state-of-the-art on
language modeling." A NeurIPS reviewer reads this as an unbounded claim. Rewrite as: "On three
autoregressive benchmarks at the 1B-parameter scale, our optimizer reaches the validation loss of
tuned AdamW in 30% fewer steps; we do not test beyond 1B or on vision, and the gain narrows under
aggressive learning-rate schedules (Appendix C)." The rewrite names the comparison set, the scale
boundary, the failure regime, and forward-references evidence, pre-answering the claims-match-results
and limitations checklist items in one move.

## Rewrite output

```text
[Claim before] <original claim>
[Claim after] <NeurIPS-calibrated claim>
[Evidence anchor] <experiment/proof/ablation/dataset/checklist>
[Limitation sentence] <plain limitation text>
[Reviewer concern reduced] <novelty/clarity/significance/reproducibility/ethics>
```

