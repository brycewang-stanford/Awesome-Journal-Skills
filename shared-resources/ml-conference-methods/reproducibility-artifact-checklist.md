# Reproducibility Artifact Checklist

Use this checklist for anonymous review packages and post-acceptance releases.
It complements, but never replaces, the current official venue checklist.

## Anonymous Review Package

- Remove author names, affiliations, usernames, paths, cloud buckets, commit
  history, grant IDs, private URLs, and notebook metadata.
- Include exact environment setup: package manager, language version, GPU/CPU
  assumptions, system libraries, and random seeds.
- Include a fast smoke test that runs in minutes and verifies the environment.
- Map each main paper table/figure to a command, config, notebook, proof script,
  or documented non-releasable component.
- Separate large checkpoints, data, and logs from core scripts; document access,
  licenses, and restrictions.
- State expected runtime and storage needs. Reviewers should not discover a
  multi-day job by accident.

## Public Release

- Replace anonymous links with durable public repositories or archives.
- Add explicit licenses for code, data, model weights, and generated assets.
- Preserve the exact revision used for the paper.
- Add a top-level README with commands, expected outputs, hardware, and known
  nondeterminism.
- Keep a citation or DOI path when feasible.

## Red Flags

- "Code will be released" with no review artifact and no explanation.
- Missing preprocessing scripts or undocumented private data.
- Hidden model selection, cherry-picked seeds, or unmatched compute.
- Supplement-only evidence for a claim that decides the paper.
- Artifact that deanonymizes authors during double-blind review.
