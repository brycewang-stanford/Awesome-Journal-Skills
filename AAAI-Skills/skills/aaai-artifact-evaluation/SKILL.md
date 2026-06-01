---
name: aaai-artifact-evaluation
description: Use when packaging AAAI code, data, multimedia appendices, technical appendices, reproducibility evidence, and post-acceptance artifact releases without violating double-blind or immutable-supplement rules.
---

# AAAI Artifact Evaluation

Use this to prepare artifacts that reviewers can use to assess reproducibility. AAAI supplementary
material is part of the submission record; after review starts, do not assume it can be updated.

## Artifact package

- Provide a technical appendix for proofs, algorithms, assumptions, hyperparameters, and extended
  experiments.
- Provide code/data ZIPs that reproduce main tables or figures, with a short README, environment,
  commands, seeds, expected outputs, and runtime.
- Provide multimedia appendices only when they support the technical claim.
- Remove author names, usernames, paths, repository history, cloud buckets, API keys, and metadata.
- Avoid web pointers in the reviewed submission unless current rules explicitly allow them.
- Include licensing and access notes for datasets, models, and third-party code.

## AAAI-specific discipline

- Treat the supplementary deadline as final.
- Verify ZIP integrity before submission; missing or corrupted files may not be fixable during
  rebuttal.
- Make the reproducibility checklist consistent with the artifact package.
- Prepare a post-acceptance public release path but keep review artifacts anonymous.

## Output format

```text
[Artifact status] complete / partial / risky / unavailable
[Submitted files] technical appendix / multimedia appendix / code-data ZIP
[Reviewer reproduction path] <commands and expected output>
[Anonymity risks] <metadata, links, paths, logs>
[Missing items] <data, code, seeds, licenses, hardware>
```

