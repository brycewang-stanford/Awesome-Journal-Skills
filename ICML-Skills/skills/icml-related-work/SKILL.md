---
name: icml-related-work
description: Use when positioning an ICML submission against close ML literature, concurrent ICML submissions, recent public papers, workshop papers, ICLR/AISTATS/NeurIPS neighbors, and prior work under double-blind constraints.
---

# ICML Related Work

Use this when novelty, incremental contribution, or concurrent-submission handling is the risk.
ICML 2026 treats related concurrent ICML submissions with overlapping authors as prior work.

## Required coverage

- Closest ML methods, theory, datasets, benchmarks, and evaluation papers.
- Neighboring venue papers from NeurIPS, ICLR, AISTATS, UAI, COLT, MLSys, KDD, ACL, CVPR, and other
  relevant areas.
- Related concurrent ICML submissions by overlapping authors; cite anonymously and include PDFs in
  supplementary material when a reasonable reviewer would expect them.
- Workshop papers without published proceedings generally do not trigger dual-submission violation,
  but their relationship still needs honest positioning.
- Very recent public work close to the full-paper deadline can be treated as concurrent, but good
  judgment and subfield norms matter.

## Delta paragraph

```text
<Prior work> addresses <problem> using <mechanism>. It leaves <specific gap>.
Our submission differs by <technical delta>, and this matters because <evidence>.
```

## Novelty-pushback table (ICML reviewer reflexes)

ICML reviewers triage novelty fast because the load is heavy and the first PMLR page must already
signal the delta. Map the likely objection to a venue-specific repair.

| Reviewer objection | What it means at ICML | Repair before submission |
| --- | --- | --- |
| "This is a known trick rebranded" | Mechanism overlaps a COLT/NeurIPS result | Cite it, state the assumption or rate that differs, move the delta to page 1 |
| "Concurrent work already does this" | Overlapping-author ICML paper or recent arXiv | Cite anonymously, attach the PDF, give a one-line technical separation |
| "Optimization angle is incremental" | A new step-size or proximal variant | Show the regime where prior rates fail and yours holds, plus a tuned-baseline plot |
| "Benchmark-only contribution" | No mechanism, just leaderboard | Add an ablation tying the gain to the proposed component |

## Worked vignette: a new optimizer with convergence theory

Suppose the paper proposes an adaptive-step method with a non-convex convergence guarantee plus
deep-learning benchmarks. The related-work risk is that reviewers know Adam, AdaGrad, Lion, and the
escaping-saddle and variance-reduction literature. Position it by separating the assumption set
(smoothness, bounded variance, PL condition) your rate needs from what neighbors assume, naming the
closest COLT/NeurIPS optimization theory, and conceding which benchmarks are shared rather than
claiming a blanket win. The delta paragraph then reads as a precise rate-and-regime statement, not a
list of beaten methods.

## Output format

```text
[Closest work] <3-5 papers or clusters>
[Concurrent ICML handling] none / cite anonymously / include PDF / split papers
[Incrementality risk] high / medium / low
[Technical delta] <one sentence>
[Related-work rewrite] <paragraph>
```

