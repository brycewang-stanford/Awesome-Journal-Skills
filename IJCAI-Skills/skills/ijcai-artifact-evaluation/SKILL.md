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

## Output format

```text
[Artifact role] paper evidence / supplement / post-acceptance release
[Contents] <proofs/code/data/models/logs/docs>
[Anonymity risks] <paths/licenses/metadata/URLs>
[Reproducibility claim] convincing / credible / weak
[Fixes before upload] <ordered list>
```
