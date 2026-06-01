---
name: aistats-supplementary
description: Use when preparing AISTATS supplementary material, appendices, proof details, code/data archives, simulation scripts, additional tables, and anonymized artifacts under deadline, size, anonymity, and reviewer-discretion constraints.
---

# AISTATS Supplementary

Use this when assembling AISTATS supplementary material. The supplement can support the
paper, but the main submission must remain understandable without it.

## Supplement structure

- Put theorem proofs, derivations, extra ablations, simulation details, dataset
  documentation, and robustness tables in a clean appendix or supplementary manuscript.
- Put executable assets in a separate archive when current OpenReview forms allow it.
- Respect the current supplementary deadline. AISTATS 2026 placed supplementary-material
  submission after the paper deadline but before review.
- Keep all supplementary files double-blind: no authors, institutions, acknowledgements,
  private paths, repository owners, grants, or identifying metadata.
- Do not use the supplement to hide essential motivation, core method description, main
  theorem statements, or primary empirical results.
- Verify archives open on a clean machine and contain no credentials, cache directories,
  large irrelevant files, or hidden OS metadata.

## Output format

```text
[Supplement status] Ready / Needs fixes / Not ready
[Files] <appendix/proofs/code/data/logs>
[Deadline] <current supplement deadline and source>
[Anonymity checks] <passed/issues>
[Main-paper dependency] <what breaks if supplement is ignored>
```
