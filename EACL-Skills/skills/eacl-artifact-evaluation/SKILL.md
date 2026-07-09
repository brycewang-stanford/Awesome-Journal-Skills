---
name: eacl-artifact-evaluation
description: Use when packaging code, data, prompts, model outputs, and annotation materials for an EACL submission, first as an anonymized ACL Rolling Review supplement aligned with the Responsible NLP checklist, then as a public post-acceptance ACL Anthology release, with attention to licensing, dataset documentation, and reproduction instructions.
---

# EACL Artifact Evaluation

Use this to turn a paper's evidence into artifacts that survive review and become a public
release. EACL runs through ACL Rolling Review, so the artifact lives two lives: an **anonymized
supplement** attached at ARR submission, and a **public release** after commitment acceptance.
Both are audited against the Responsible NLP checklist. Reopen the current checklist before
packaging.

## The two lives of an EACL artifact

| Stage | Form | Must be | Owner |
|---|---|---|---|
| ARR submission | Anonymized `.zip`/`.tgz` supplement | Fully de-identified, self-contained | Authors |
| Commitment acceptance | Public repo + Anthology link | Licensed, versioned, reproducible | Authors |

Do not conflate them: the review supplement must contain **no author-identifying strings**,
while the public release must contain **exactly the identifying and licensing information the
supplement omitted**.

## What belongs in an EACL artifact

- **Code** to reproduce the headline tables, with a top-level entry point.
- **Data**: the dataset or a loader plus a documented path to it; if redistribution is
  restricted, document access precisely rather than implying release.
- **Prompts and decoding settings** verbatim for any LLM-based result — these are part of the
  method, not an afterthought.
- **Model outputs** retained so scores can be re-computed without re-running expensive models.
- **Annotation materials**: guidelines, interface, pay information, and inter-annotator
  agreement.

## Anonymized-supplement checklist

```text
[ ] No author names in paths, file headers, LICENSE, or notebook metadata
[ ] Git history stripped or repo re-initialized
[ ] No personal hosting URLs (Drive/Dropbox) that identify authors
[ ] Prompts + decoding params included verbatim
[ ] Model outputs included for re-scoring
[ ] A README that reproduces at least one reported table
[ ] Smoke-checked (see resources/code/README.md)
```

Run the shared smoke checker before upload:

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-supplement
```

## Licensing and documentation for the public release

- Choose a **license** appropriate to code (e.g. permissive) and data (respecting upstream
  dataset terms); the paper text should state it.
- Document **intended use** and known limitations of any released dataset — required by the
  checklist and expected by the European community's data-governance norms.
- Version the release with a tag that matches the camera-ready, so the Anthology PDF and the
  repo cannot drift.

## Multilingual and lower-resource specifics

- If the artifact covers lower-resourced languages, document **provenance and speaker/annotator
  context** carefully; thin documentation of a low-resource dataset is a common EACL reviewer
  concern.
- Keep language codes and scripts explicit (ISO codes, script variants) so the artifact is
  usable by others working on those languages.

## Output format

```text
[Artifact stage] Anonymized supplement / Public release
[Contents] <code/data/prompts/outputs/annotation coverage>
[Anonymization] <pass/fail with specific leaks>
[Reproduces] <which reported table the README regenerates>
[Licensing + docs] <license, dataset terms, intended-use note>
[Gaps] <what a reviewer could still not reproduce>
```
