---
name: iclr-artifact-evaluation
description: Use when packaging ICLR code, data, checkpoints, demos, logs, and reproduction instructions for reviewers or post-acceptance release, including anonymized links and private OpenReview discussion-period sharing. Use when a reviewer asks for a missing repro path, when a public comment questions whether claims can be verified, or when converting an anonymous supplement into a durable post-acceptance release for the permanent ICLR record.
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

## What reviewers actually open

ICLR reviewers sample the supplement under time pressure during an open discussion everyone can
read later. Optimize for the first ten minutes.

| Reviewer signal | Strong artifact | Weak artifact |
| --- | --- | --- |
| "Rerun the headline table?" | `run_main.sh` with seed, config, log | "See repo", no entry point |
| "Is this anonymous?" | Stripped remotes, no analytics | Demo that logs reviewer IPs |
| "Checkpoint matches paper?" | Hash-pinned weights + eval command | Unlabeled `.pt` files |
| "What is not covered?" | "Cannot release X, license Y" | Silent gaps read as hiding |

## Worked vignette

A submission proposes a self-supervised contrastive objective for graph encoders and ships a 9 GB
checkpoint but no eval command. A public review asks how to reproduce Table 2 without retraining.
The fix: add `eval_table2.sh` that loads the checkpoint, runs the frozen-encoder probe, prints the
exact numbers, pin the checkpoint hash, and note in the thread that it runs in minutes on one GPU.
The clean path stays public forever and reassures every later reader of the accepted paper.

## Reviewer-pushback patterns

- "Anonymous link is dead." Host static files in the OpenReview supplement ZIP, not an external
  service that can expire mid-discussion.
- "Smoke test passes but the real run does not." Ship a longer reference log so reviewers can diff
  intermediate values, not only final scores.
- "Proprietary, cannot share." Replace the vague label with a synthetic-data substitute.

## Output format

```text
[Artifact status] complete / partial / risky / unavailable
[Reviewer path] <fastest route to reproduce main claim>
[Anonymity risks] <metadata, links, logs, demos>
[Release plan] anonymous review / post-acceptance public / cannot release
[Missing evidence] <commands, seeds, data, checkpoints, licenses>
```

