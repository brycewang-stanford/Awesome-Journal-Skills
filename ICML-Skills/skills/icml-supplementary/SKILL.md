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

## Output format

```text
[Main body] <items that must stay>
[Appendix PDF] <items>
[Supplementary manuscript] <items>
[Code/data supplement] <items>
[Camera-ready public artifact] <items>
```

