---
name: acl-artifact-evaluation
description: Use when packaging code, datasets, prompts, model outputs, or annotation materials for an ACL submission under ACL Rolling Review, covering anonymized supplement archives, scientific-artifact items of the Responsible NLP checklist, licensing and intended-use documentation, data statements, and post-acceptance public release.
---

# ACL Artifact Evaluation

Use this to plan the evidence package around an ACL paper. ACL has no separate
artifact-badge track; instead, artifact scrutiny is folded into review through
the supplement archive and Section B ("scientific artifacts") of the
Responsible NLP checklist, which reviewers cross-check against the PDF.

## What counts as an artifact here

- Code: training/inference scripts, evaluation harnesses, prompt templates.
- Data: new corpora, annotations, filtered subsets of existing corpora, test
  suites, adversarial sets.
- Model outputs: generations, ranked lists, logits used in analysis — often the
  cheapest way to make an LLM paper checkable without GPUs.
- Human-subject materials: annotation guidelines, interface screenshots,
  consent text, compensation description.

## Submission-time packaging rules

- Supplements upload as .tgz/.zip through the OpenReview form; links to
  tracked cloud storage are not acceptable, and any linked page must be
  anonymous.
- Scrub identity everywhere reviewers can look: file paths, git metadata,
  notebook author fields, license headers, dataset hosting pages, README
  contact lines.
- Reviewers are not required to open supplements. The paper plus checklist
  must stand alone; the archive is for verification, not for essential content.

## Checklist items your artifact must satisfy

| Responsible NLP item (Section B) | Artifact implication |
|---|---|
| Cited creators + versions of used artifacts | Pin dataset/model versions in the README and bibliography |
| License / terms of use stated | Include the license you release under *and* those you consumed under |
| Use consistent with intended use | Justify research use of scraped or user-generated data |
| PII and offensive content handled | Describe scanning/anonymization steps actually performed |
| Documentation of domains, languages, demographics | Ship a data statement or datasheet, not just row counts |
| Statistics on splits reported | Train/dev/test sizes in both paper and README |

Checklist answers contradicted by the archive read as misleading information —
grounds for desk rejection under ARR policy, and a credibility wound even when
not enforced.

## What an ACL reviewer opens first

1. The README — it has roughly one minute to orient them.
2. Prompt files and evaluation scripts, for any LLM claim: exact prompts,
   decoding parameters, and scoring code are the reproduction spine.
3. Annotation guidelines, for any dataset or human-eval claim: reviewers judge
   whether the labels could possibly mean what the paper says.
4. A sample of the data itself — quality problems visible in twenty random
   examples have sunk otherwise strong resource papers.

## Vignette: packaging a multilingual benchmark submission

A hypothetical paper releases a 7-language reading-comprehension test suite
built from news text plus a baseline evaluation of five LLMs.

- Ship per-language provenance: source, license, collection window, and the
  filtering pipeline as runnable code, since "web text" alone fails checklist
  item B on documentation.
- Include annotator guidelines, pay, recruitment channel, and agreement
  statistics; multilingual annotation quality is the first attack surface.
- Provide the exact prompts and outputs for all five models so reviewers can
  re-score without API keys.
- Keep a versioned, hash-stamped test file so post-publication contamination
  can be audited later.

## Release ladder after acceptance

```text
anonymous supplement  ->  public repo + dataset page  ->  archived, versioned release
   (review-time)          (camera-ready links)            (DOI/hub artifact, cited version)
```

Post-acceptance, register the artifact where your community actually looks
(model/dataset hubs, a maintained repo), state the license explicitly, and put
the citation-of-record (the Anthology entry) in the README.

## Anonymization sweep, concretely

Run these before zipping, on a copy:

```bash
# authorship trails in code and docs
grep -ri "yourname\|yourlab\|university" . --include="*.py" --include="*.md"
# git history and remotes leak owners
rm -rf .git; # or re-init a fresh repo for the archive copy
# notebook metadata carries usernames and kernel paths
jupyter nbconvert --clear-output --inplace *.ipynb
# absolute paths in configs and logs
grep -r "/home/\|/Users/" . | head
```

Then check the parts tools miss: license headers naming the lab, dataset
hosting pages with institutional branding, model cards listing maintainers,
and README badges pointing at owner-named CI.

## Sizing and format sanity

- Keep the archive lean: strip checkpoints reviewers cannot load anyway,
  cached datasets, and virtualenvs; describe big assets and provide them at
  camera-ready instead.
- One top-level README, one environment file, one entry point per claimed
  result — reviewers grant roughly a minute before giving up.
- Verify the .zip/.tgz opens on a machine that has never seen the project;
  OpenReview upload limits and accepted fields vary by cycle, so check the
  live form rather than last cycle's.

## Output format

```text
[Artifact role] anonymous supplement / camera-ready release / public benchmark
[Contents] <code/data/prompts/outputs/guidelines>
[Checklist alignment] <Section B items satisfied vs missing>
[Anonymity findings] <paths/metadata/hosting leaks>
[Release plan] <post-acceptance registry, license, versioning>
```
