---
name: neurips-writing-style
description: Use when rewriting a machine-learning paper for NeurIPS-style contribution framing, concise claims, contribution-type alignment, limitations, societal impact, and checklist-compatible prose.
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

## Rewrite output

```text
[Claim before] <original claim>
[Claim after] <NeurIPS-calibrated claim>
[Evidence anchor] <experiment/proof/ablation/dataset/checklist>
[Limitation sentence] <plain limitation text>
[Reviewer concern reduced] <novelty/clarity/significance/reproducibility/ethics>
```

