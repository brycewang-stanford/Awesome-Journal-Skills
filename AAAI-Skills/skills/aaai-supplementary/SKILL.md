---
name: aaai-supplementary
description: Use when organizing AAAI supplementary material, including the technical appendix, multimedia appendix, and code/data ZIPs, while respecting that AAAI supplements are due with the paper, treated as immutable after submission, must stay double-blind, and should never hide main-paper-critical evidence from reviewers who skim the appendix.
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

## Where each item belongs

A broad-AI reviewer will skim the appendix, not study it, so placement decides whether evidence is
actually seen. Anything a claim depends on belongs in the main paper; the appendix only deepens it.

| Material | Main paper | Technical appendix | Multimedia | Code/data ZIP |
| --- | --- | --- | --- | --- |
| Core result | yes | no | no | no |
| Full proof | sketch | full | no | no |
| Extra ablation | summary | detail | no | no |
| Demo of behavior | no | no | yes | no |
| Scripts and configs | no | no | no | yes |

## Reviewer-pushback patterns

- "The key result is only in the appendix." Fix: promote it to the main paper; AAAI reviewers are not
  obligated to find a load-bearing claim buried in supplement.
- "Supplement contradicts the checklist." Fix: reconcile every appendix number with the checklist
  before submission, since neither can be edited later.
- "Multimedia is huge but adds nothing." Fix: drop spectacle clips; include video only when it is the
  evidence, not decoration.

## Worked vignette

A vision paper hides its ablation table in the ZIP and leaves only a teaser figure in the paper. The
navigation map exposes the gap: a disputed claim points to a file a skimming reviewer will miss. The
fix moves the ablation summary into the main paper, keeps full per-class numbers in the technical
appendix, and scrubs the ZIP's metadata so nothing deanonymizes the immutable supplement.

## Output format

```text
[Supplement plan] technical appendix / multimedia appendix / code-data ZIP / none
[Main-paper dependencies] <material that must not be hidden in supplement>
[Navigation map] <claim -> supplement file/section>
[Anonymity risks] <paths, metadata, links, ownership>
[Submission risk] <missing/corrupt/too large/not allowed>
```

