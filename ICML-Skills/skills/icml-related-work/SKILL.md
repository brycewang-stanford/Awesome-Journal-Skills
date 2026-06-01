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

## Output format

```text
[Closest work] <3-5 papers or clusters>
[Concurrent ICML handling] none / cite anonymously / include PDF / split papers
[Incrementality risk] high / medium / low
[Technical delta] <one sentence>
[Related-work rewrite] <paragraph>
```

