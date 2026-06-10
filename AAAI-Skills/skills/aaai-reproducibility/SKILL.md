---
name: aaai-reproducibility
description: Use when strengthening an AAAI paper's reproducibility checklist (placed after references), experimental traceability, seed and hyperparameter reporting, compute and cost disclosure, dataset access and licensing, code/data ZIP readiness, and the claim-to-evidence map that Phase-1 reviewers use to judge rigor across AAAI's broad AI scope.
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

## Checklist-to-evidence consistency grid

AAAI places the reproducibility checklist after the references, and reviewers cross-check each "yes"
against the paper and supplement. A "yes" with no backing artifact reads worse than an honest "no",
because it signals the checklist was filled in carelessly.

| Checklist answer | Must be backed by | Phase-1 risk if unbacked |
| --- | --- | --- |
| code available | runnable scripts in the ZIP | "claimed but absent" |
| seeds reported | seed list and variance | "single-run cherry-pick" |
| compute disclosed | train vs. inference vs. search cost | "hidden tuning budget" |
| data accessible | license and access path | "irreproducible by anyone" |

## Reviewer-pushback patterns

- "Checklist says code available but I see only figures." Fix: ship scripts and a one-line driver
  before the deadline; do not promise the repository in rebuttal.
- "Results may be seed-dependent." Fix: report multiple seeds with spread, and set the checklist seed
  answer to match the supplement exactly.
- "Closed API, not reproducible." Fix: add an open substitute model or release prompts and outputs so
  the claim is checkable.

## Worked vignette

A vision-language paper checks "code and data available" but the ZIP holds only PDFs of plots. Audit
verdict: reproducibility grade "fragile", with a checklist conflict between the "yes" and the missing
scripts. The smallest fix is a `reproduce.sh` that regenerates one headline table from seeds plus a
dataset license note, after which the checklist answer becomes truthful and Phase-1 defensible.

## Output format

```text
[Reproducibility grade] strong / adequate / fragile / not reviewable
[Checklist conflicts] <answers that contradict paper/supplement>
[Evidence gaps] <claims without submitted verification>
[Compute/data disclosure] complete / incomplete
[Priority fixes] <smallest changes before submission>
```

