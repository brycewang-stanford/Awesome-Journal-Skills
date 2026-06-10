---
name: icml-supplementary
description: Use when deciding what ICML material belongs in the main 8-page body, same-PDF appendices, supplementary manuscript, code/data supplement, anonymous concurrent-submission PDF, or public camera-ready artifact.
---

# ICML Supplementary

Use this to place material correctly. ICML 2026 allows references and unlimited appendices in the
same PDF, plus supplementary manuscripts and code/data, but critical evaluation material should be
in the main paper because reviewers may choose whether to inspect supplements.

## Placement map

- Main 8-page body: contribution, method, essential assumptions, central theory, headline
  experiments, limitations, impact statement placement, and evidence needed for judgment.
- Same-PDF appendices: proofs, extended algorithms, expanded ablations, extra qualitative examples,
  dataset details, and analysis that supports but does not define the claim.
- Supplementary manuscript: anonymized concurrent submissions or unusually long supporting text that
  cannot fit cleanly in the paper PDF.
- Code/data supplement: anonymized code, data, scripts, environment, and README.
- Camera-ready public artifact: final code/data repository or archive. ICML 2026 does not provide a
  final camera-ready supplementary-material upload.

## Concurrent submission handling

If an ICML submission cites another concurrent ICML submission by overlapping authors, include the
anonymized PDF in supplementary material and explain the relationship in the main paper.

## Placement decision table

ICML reviewers may skip supplements, so misplacement is a real acceptance risk, not a formatting
nit. Decide placement by whether a reviewer can judge the claim without the material.

| Material | Needed to judge the claim? | Correct ICML home |
| --- | --- | --- |
| Headline benchmark and main ablation | Yes | Main 8-page body |
| Full proof of a stated theorem | Reviewer may verify on request | Same-PDF appendix |
| Extended hyperparameter grid, extra seeds | Supports but does not define | Same-PDF appendix |
| Runnable code, environment, README | For reproducibility audit | Anonymized code/data supplement |
| Overlapping-author concurrent paper | For dual-submission judgment | Supplementary manuscript |

## Worked vignette: optimizer paper placement

For an adaptive-step optimizer with a non-convex convergence theorem plus deep-learning benchmarks,
the convergence theorem statement, one decisive benchmark, and the component ablation stay in the
8-page body. The full proof, the step-size sensitivity sweep, and per-seed tables go to the same-PDF
appendix. The training scripts and environment file go to the code/data supplement. Because accepted
ICML papers can publish original supplementary material, scrub the code supplement of identity leaks
and unreleasable data before upload. A common reject pattern is burying the only fair tuned baseline
in the appendix where a heavily loaded reviewer never looks. When the appendix is unlimited, the
temptation is to defer hard results; resist it, because at ICML the decisive evidence has to sit in
the main body where the soundness judgment is actually formed.

## Output format

```text
[Main body] <items that must stay>
[Appendix PDF] <items>
[Supplementary manuscript] <items>
[Code/data supplement] <items>
[Camera-ready public artifact] <items>
```

