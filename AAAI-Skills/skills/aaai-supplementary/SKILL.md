---
name: aaai-supplementary
description: Use when organizing AAAI technical appendices, multimedia appendices, code/data ZIPs, immutable supplementary material, and double-blind supplementary files.
---

# AAAI Supplementary

Use this when deciding what belongs in the main paper, technical appendix, multimedia appendix, or
code/data ZIP. AAAI supplementary material is due with the paper and should be treated as immutable
once submitted unless current instructions say otherwise.

## Supplement structure

- Keep the central contribution, method, core results, and checklist-relevant evidence in the main
  paper.
- Put proofs, extra ablations, extended qualitative examples, implementation details, and additional
  error analysis in the technical appendix.
- Put videos, audio, interactive demos, or visualizations in a multimedia appendix only when they are
  technically necessary.
- Put scripts, datasets, logs, model configs, and checkpoints in code/data ZIPs.
- Add a compact appendix map so reviewers can find support for each disputed claim.

## Anonymity and immutability

- Remove identity from file names, metadata, paths, Git history, author comments, and license
  headers.
- Do not use web pointers for extra material if current AAAI rules disallow them.
- Submit final, uncorrupted files. Do not rely on rebuttal to repair missing content.
- Keep the supplement consistent with the reproducibility checklist.

## Output format

```text
[Supplement plan] technical appendix / multimedia appendix / code-data ZIP / none
[Main-paper dependencies] <material that must not be hidden in supplement>
[Navigation map] <claim -> supplement file/section>
[Anonymity risks] <paths, metadata, links, ownership>
[Submission risk] <missing/corrupt/too large/not allowed>
```

