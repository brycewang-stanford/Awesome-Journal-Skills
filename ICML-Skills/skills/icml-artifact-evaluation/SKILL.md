---
name: icml-artifact-evaluation
description: Use when packaging ICML artifacts - code, data, model weights, simulators, benchmarks, proof scripts, notebooks, anonymous repositories, and supplementary code/data ZIPs - for both the double-blind review package and the public release that accompanies accepted PMLR papers. Use when checking anonymity, decision relevance, licensing, and the OpenReview code URL field under current ICML rules.
---

# ICML Artifact Evaluation

ICML does not let artifacts sit outside the paper's scientific argument. Reproducibility and code
availability are explicitly considered in decision-making, and accepted submissions may publish the
original supplementary material on OpenReview.

## Review-stage package

- Decide whether the artifact is code, data, model weights, simulator, benchmark, proof script,
  notebook, or supplementary manuscript.
- Anonymize authors, repository ownership, filenames, commit history, logs, model cards, dataset
  cards, licenses, and personal paths.
- If using an anonymous repository, put it on a branch that will not change after the submission
  deadline.
- Put critical evaluation material in the paper body, not only in supplement. Reviewers decide
  whether to consult appendices or supplementary material.
- Provide minimal commands, environment details, expected runtime, hardware assumptions, and result
  mapping.

## Public-release package

- Because accepted original supplementary material may become public, review-stage artifacts should
  not contain private, illegal, or unreleasable content.
- For camera-ready, final supplementary material is not uploaded separately; code/data should move
  to a public repository or archive and be linked in the paper/OpenReview code URL field.
- Add clear licenses and persistent identifiers when possible.

## Anonymity leak checklist

ICML double-blind review means a single deanonymizing artifact can trigger a desk reject, so audit
the package the way an adversarial reviewer would.

| Leak vector | Where it hides | Mitigation |
| --- | --- | --- |
| Repo ownership | Anonymous-repo account name, commit author | Use a fresh anonymized host, strip git history |
| File metadata | PDF author field, notebook kernel, model card | Clear metadata, rename author paths |
| Hard-coded paths | Cluster usernames in scripts and logs | Replace with placeholders before zipping |
| External links | Personal site, non-anonymous URL, shortener | Remove or route through an anonymous mirror |

## Worked vignette: optimizer artifact package

A paper shipping an adaptive optimizer includes training scripts, a pretrained checkpoint, and a
proof-checking notebook. The review package gives minimal commands, expected runtime, and the
hardware assumption so a reviewer can map a command to a benchmark number, while the checkpoint
filename and the notebook kernel are scrubbed of the lab name. Because accepted ICML supplements can
become public, the team confirms the checkpoint is releasable and the license is stated before the
deadline, then plans the public repository and OpenReview code URL for camera-ready.

## Output format

```text
[Artifact role] code / data / model / benchmark / proof / none
[Review package] sufficient / incomplete / unsafe
[Anonymity risks] <metadata, repo, filenames, links>
[Decision relevance] <why reviewers need it>
[Public release plan] <repo/archive/license/code URL>
```

