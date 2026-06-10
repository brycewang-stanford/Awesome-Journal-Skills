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

## What an AAAI reviewer actually opens

AAAI does not run a separate badged artifact-evaluation committee the way some systems venues do;
the same broad-AI reviewer who scores the paper also inspects whatever supplement you attach. That
reviewer may be a planning, knowledge-representation, or constraint-satisfaction specialist rather
than a deep-learning engineer, so the artifact has to be legible without insider tooling. Optimize
for a reviewer who skims, not one who will spend an afternoon configuring a cluster.

| Reviewer action | Passes | Fails |
| --- | --- | --- |
| Opens the ZIP | sane tree, top README | nested archives, 0-byte files |
| Reads appendix | maps to numbered claims | contradicts the paper |
| Tries one command | reproduces one headline number | needs private data or credentials |
| Scans for identity | nothing reveals authors | Git logs or home paths leak |

## Phase-1 artifact red flags

Because clearly-below-bar papers can be cut before author feedback, a supplement that looks thin or
unrunnable is a cheap reason to summary-reject. Avoid these:

- Checklist promises released code, but the ZIP only holds figures and no scripts.
- A "see our repository" pointer to a mutable, deanonymizing URL.
- Multimedia attached for spectacle that carries no technical claim, inflating size with no rigor.
- Datasets shipped with no license note, leaving reuse legality unverifiable.

## Worked vignette

A constraint-solving paper claims a 30% node-expansion reduction. The team ships a large ZIP of raw
solver logs but no driver script. The reproduction path is empty, so artifact status is "risky"; the
fix is a small `run_main.py` that regenerates Table 2 from seeds, a trimmed log sample, and a license
for the benchmark instances. The raw dump moves to the post-acceptance release.

## Output format

```text
[Artifact status] complete / partial / risky / unavailable
[Submitted files] technical appendix / multimedia appendix / code-data ZIP
[Reviewer reproduction path] <commands and expected output>
[Anonymity risks] <metadata, links, paths, logs>
[Missing items] <data, code, seeds, licenses, hardware>
```

