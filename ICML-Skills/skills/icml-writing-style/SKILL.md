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

## Output format

```text
[Claim before] <original>
[Claim after] <ICML-calibrated version>
[Evidence anchor] <proof/experiment/baseline/artifact>
[Impact statement note] <needed addition or narrowing>
[8-page compression] <what to cut or move>
```

