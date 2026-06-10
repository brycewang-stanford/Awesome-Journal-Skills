---
name: ijcai-artifact-evaluation
description: Use when packaging IJCAI or IJCAI-ECAI code, data, proofs, models, and appendices as reproducibility evidence or supplementary material, especially when there is no separate artifact-evaluation badge but reviewers need convincing, anonymous, deadline-safe evidence.
---

# IJCAI Artifact Evaluation

Use this for artifact packaging around IJCAI. Treat the current reproducibility guidelines
and supplementary-material rules as controlling; do not assume a separate formal artifact
evaluation track unless the current cycle announces one.

## Package design

- Decide what reviewers need to classify the results as convincing or credible: proofs,
  pseudocode, datasets, code, model cards, logs, environment details, or ablation notebooks.
- Keep essential evidence in the paper whenever space allows because reviewers are not
  required to read supplementary material.
- Put optional evidence in the Technical Appendix or ZIP, respecting the current size and
  format limit. IJCAI-ECAI 2026 allowed up to 50MB in PDF or ZIP form.
- Anonymize repository paths, user names, institutions, license headers, model checkpoints,
  data provenance, and notebook metadata.
- Include a minimal run map: environment, dependencies, hardware, commands, expected outputs,
  runtime, seeds, and known limitations.
- For proprietary or restricted data/code, explain why it cannot be shared and provide enough
  detail for in-principle reproduction.

## Evidence by claim type

IJCAI usually has no separate artifact-evaluation badge, so the artifact's job is to move the
reproducibility rating toward convincing and to pre-empt a broad PC's doubt. Match the package
to the claim.

| Claim | Artifact that convinces an IJCAI reviewer | Weak substitute to avoid |
| --- | --- | --- |
| New search/planning algorithm | Runnable solver, instance generator, seeds, time/memory limits | A results CSV with no way to regenerate it |
| Theoretical guarantee | Full proofs, assumption list, citations to formal tools | "Proof omitted for space" with no appendix |
| Multi-agent protocol | Simulator, opponent policies, randomization seeds | Screenshots of one run |
| Learning result | Code, environment file, configs, compute and runtime | Final-number table only |
| Dataset | Datasheet, license, controlled-access path | Vague "available on request" |

## Worked vignette: packaging a SAT-solver paper

A SAT/CSP paper claims a new restart heuristic wins on hard industrial instances. Strong
package: the solver binary or source, the exact instance set or a deterministic generator,
solver and compiler versions, per-instance runtimes with the timeout stated, and a run map
showing one command that reproduces the cactus plot. Anonymize the repository name, license
headers, and any cluster paths. This lets a skeptical constraint-reasoning reviewer re-run a
sample and raises the rating from credible to convincing without needing a badge track.

## Reviewer pushback and the venue-specific fix

- "Cannot regenerate the benchmark instances." Ship a generator plus seeds, not just outputs.
- "Artifact leaks author identity." Scrub paths, license headers, checkpoint names, and
  notebook metadata before the full-paper deadline; there is no late re-upload.
- "Restricted data blocks reproduction." Document the legal barrier and give enough protocol
  for in-principle reproduction rather than implying a release you cannot deliver.

## Output format

```text
[Artifact role] paper evidence / supplement / post-acceptance release
[Contents] <proofs/code/data/models/logs/docs>
[Anonymity risks] <paths/licenses/metadata/URLs>
[Reproducibility claim] convincing / credible / weak
[Fixes before upload] <ordered list>
```
