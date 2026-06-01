---
name: neurips-artifact-evaluation
description: Use when packaging NeurIPS code, data, models, demos, benchmarks, or other research artifacts for anonymous review, reproducibility, public release, or MLRC-style artifact scrutiny.
---

# NeurIPS Artifact Evaluation

NeurIPS main track does not reduce artifact quality to a generic badge workflow. It expects code,
data, and execution details when they are needed to support the scientific claim, and its checklist
and code/data guidance make artifact quality visible to reviewers.

## Artifact decision

- If the contribution is a method, include training and evaluation code or justify why it cannot be
  shared.
- If the contribution is a dataset or benchmark, provide metadata, license, preservation plan,
  representative-use discussion, and access restrictions.
- If the contribution depends on a model, include weights, prompts, decoding settings, compute
  resources, or a precise explanation of unavailable components.
- If the contribution is theoretical, artifact focus may shift to proof checks, symbolic scripts,
  experiment notebooks, or counterexample generation.

## Anonymous review package

- Keep the ZIP within the current official size limit and anonymize filenames, repository URLs,
  usernames, commit history, model cards, dataset cards, comments, notebooks, and logs.
- Include a short `README` with exact commands, environment, expected runtime, hardware assumptions,
  and which experiments are reproducible from the package.
- Do not require reviewers to run unsafe code outside a secure environment.
- Avoid external links unless the current policy allows them and anonymous browsing is guaranteed.

## Public release package

- De-anonymize accepted artifacts.
- Add licenses for code, data, model weights, and generated outputs.
- Archive code in a durable service when appropriate; NeurIPS MLRC guidance recommends Software
  Heritage for reproducibility papers.
- Keep a mapping from paper claims to commands or notebooks so users can reproduce headline results.

## Output format

```text
[Artifact role] method / dataset / benchmark / model / demo / proof / none
[Review package] sufficient / insufficient
[Anonymity risks] <paths, metadata, URLs, usernames>
[Reproducibility gaps] <commands, environment, data, hardware, licenses>
[Public-release plan] <archive, DOI, license, docs>
```

