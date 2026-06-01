---
name: iclr-artifact-evaluation
description: Use when packaging ICLR code, data, checkpoints, demos, logs, and reproduction instructions for reviewers or post-acceptance release, including anonymized links and private discussion-period sharing.
---

# ICLR Artifact Evaluation

Use this to prepare artifacts that make an ICLR paper reproducible and reviewable. ICLR may not run
a separate artifact-badge process for every paper, so the practical bar is whether reviewers and ACs
can verify the claims without identity leakage or excessive setup.

## Artifact package

- Provide a minimal reproduction path for every central table or figure: command, config, seed,
  expected runtime, hardware, and expected output file.
- Include data provenance, preprocessing scripts, licenses, and any access restrictions.
- Separate heavy checkpoints or datasets from the core anonymized supplement when file-size limits
  require it; document private reviewer links clearly.
- Remove usernames, organization names, cloud buckets, Git history, API keys, and metadata that can
  deanonymize authors.
- Add a smoke-test script that runs in minutes and confirms environment integrity.
- Mark any unreleasable component and give a defensible reason, not a vague "proprietary" note.

## ICLR-specific handling

- Submit supplementary material by the paper deadline when the current Author Guide requires it.
- During discussion, use private links or revised supplements only within current OpenReview rules.
- If a demo is useful, make it anonymous and robust to reviewer traffic, and avoid analytics that
  identify visitors.
- After acceptance, replace anonymous links with durable public archives or project pages.

## Output format

```text
[Artifact status] complete / partial / risky / unavailable
[Reviewer path] <fastest route to reproduce main claim>
[Anonymity risks] <metadata, links, logs, demos>
[Release plan] anonymous review / post-acceptance public / cannot release
[Missing evidence] <commands, seeds, data, checkpoints, licenses>
```

