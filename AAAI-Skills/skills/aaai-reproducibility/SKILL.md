---
name: aaai-reproducibility
description: Use when strengthening an AAAI paper's reproducibility checklist, experimental traceability, seed reporting, compute disclosure, dataset access, code/data readiness, and evidence map.
---

# AAAI Reproducibility

Use this when a draft needs to survive AAAI review on rigor, not just novelty. AAAI-26 required a
reproducibility checklist after references, so the checklist must agree with the paper and
supplement rather than read as an afterthought.

## Reproducibility audit

- Map each central claim to submitted evidence: theorem, table, figure, ablation, appendix item,
  checklist answer, or code/data artifact.
- Record seeds, splits, preprocessing, hyperparameters, model selection, early stopping, prompt
  selection, and hardware.
- Report variance or uncertainty when stochasticity affects conclusions.
- Document dataset licenses, access constraints, sensitive data, human-subjects issues, and
  annotation procedures.
- Separate training compute, inference compute, and experiment search cost.
- Check the reproducibility checklist for contradictions with the main text and supplement.

## Common AAAI weaknesses

- Checklist says code/data are available but supplement lacks runnable commands.
- Main results rely on one seed, one benchmark, or one prompt family.
- Baselines are weaker than current open-source or widely cited systems.
- Evaluation uses closed data or APIs with no reproducibility substitute.
- Human evaluation omits annotator instructions or quality control.

## Output format

```text
[Reproducibility grade] strong / adequate / fragile / not reviewable
[Checklist conflicts] <answers that contradict paper/supplement>
[Evidence gaps] <claims without submitted verification>
[Compute/data disclosure] complete / incomplete
[Priority fixes] <smallest changes before submission>
```

