---
name: aaai-writing-style
description: Use when revising an AAAI manuscript for broad AI audience fit, concise contribution claims, two-column readability, reproducibility-checklist alignment, and policy-aware AI-system claims.
---

# AAAI Writing Style

Use this to make a technically sound draft readable to a broad AI program committee. AAAI rewards
clear AI contribution, not only subfield-specific benchmark wins.

## AAAI framing

- State the AI problem, the new capability or insight, and the evidence in the first page.
- Make clear whether the contribution is method, theory, system, benchmark, dataset, evaluation,
  human-AI interaction, social impact, or alignment.
- Explain why the result matters outside a single dataset or implementation.
- Keep claims aligned with the reproducibility checklist and supplementary evidence.
- Discuss limitations and ethical considerations when the method affects people, safety, privacy,
  fairness, security, or social impact.

## Two-column readability

- Use figures and tables as decision aids, not decoration.
- Keep notation lightweight and define it near first use.
- Use compact related-work contrasts instead of long literature catalogues.
- Make the Phase 1 summary easy: problem, method, evidence, limitation, checklist compliance.
- Avoid unsupported "general intelligence", "human-level", or "safe" claims.

## Output format

```text
[AAAI fit sentence] <one sentence>
[Contribution type] method / theory / system / benchmark / dataset / evaluation / social impact
[First-page fixes] <problem, method, evidence, limitation>
[Checklist alignment] pass / needs revision
[Overclaim risks] <claims to narrow or evidence to add>
```

