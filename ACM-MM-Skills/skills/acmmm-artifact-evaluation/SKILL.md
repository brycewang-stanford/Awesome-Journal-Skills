---
name: acmmm-artifact-evaluation
description: Use when packaging code, models, datasets, or media as ACM MM (ACM Multimedia) artifacts — building the anonymous review package versus the public release, and choosing between the Open Source Software Competition, the Dataset track, the Reproducibility track, and main-track supplementary evidence, each with its own blinding and expectations.
---

# ACM MM Artifact Evaluation

Use this to turn an ACM Multimedia project's code, models, media, and data into the *right*
artifact for the *right* track. ACM MM has a track economy around artifacts, and the choice
determines blinding, format, and what reviewers judge.

## Which track is the artifact?

| Artifact is primarily... | Route to | Blinding | Judged on |
|---|---|---|---|
| A reusable software system/framework | Open Source Software Competition | Single-blind | Adoption, quality, license, docs |
| A new dataset/benchmark | Dataset track | Single-blind | Scale, quality, ethics, usefulness |
| A reproduction of published results | Reproducibility track | Single-blind | Whether results rebuild; ACM badges |
| Supporting evidence for a method paper | Main-track supplement | Double-blind | Whether it backs the paper's claims |

The named single-blind tracks exist *because* the artifact's identity cannot be hidden; a
main-track method paper's artifact, by contrast, must be **anonymous** through review.

## Two artifacts, two audiences

Plan both from the start:

- **Anonymous review artifact** — what reviewers see during double-blind review: an
  anonymized repository, an anonymous data mirror, stripped media metadata, and a README that
  reveals no author identity.
- **Public release artifact** — what ships at/after camera-ready: the de-anonymized
  repository, a permanent archive (DOI), the license, and the final dataset/model.

```text
review/    -> anonymous repo, anon data mirror, no names in code/media, run instructions
release/   -> public repo + DOI, LICENSE, model weights, dataset card, citation
```

## Open Source Software Competition

- The bar is a system others will *use*: clear install, documentation, examples, an
  OSI-approved license, and evidence of quality or adoption.
- Reference models and reproducible examples matter more than a single benchmark number —
  this is the lane exemplified by community frameworks and portable libraries.

## Dataset track

- Ship a **dataset card**: collection method, size, splits, license, consent, and known
  biases or limitations.
- Address ethics and rights explicitly, especially for user-generated or scraped media; a
  dataset a reviewer cannot legally use is not a contribution.

## Licensing and rights decisions

- Choose a code license (permissive vs. copyleft) and a **data** license separately; they are
  not the same choice.
- For media, confirm you have the right to redistribute; where you cannot, provide a
  retrieval script or agreement path instead of the raw files.
- Record third-party asset licenses so the release is clean.

## Ethics and consent for media artifacts

Multimedia artifacts carry people's faces, voices, and content, so the ethics review is not a
formality:

- **Consent and rights** — confirm you may redistribute the media; user-generated content often
  cannot be re-hosted, so ship a retrieval script or agreement path instead.
- **Privacy** — remove or justify identifiable individuals who did not consent; a dataset of
  scraped faces is a rejection risk regardless of its scale.
- **Documentation** — a dataset card that states collection method, consent, license, and known
  biases is part of the contribution, not paperwork.

## Timeline: review artifact, then release

```text
before paper deadline:  anonymous review artifact ready (repo + data mirror, no identity)
during review:          reviewers/AC access the anonymous artifact
on acceptance:          build the public release (de-anonymized repo + DOI + license)
by camera-ready:        release replaces the anonymous mirror; dataset/model final
```

Plan the public release early even though it ships late — a scramble at camera-ready is how
projects end up with a broken anonymous link and no working public archive.

## Output format

```text
[Track] Open Source / Dataset / Reproducibility / main-track supplement
[Blinding] correct for track / mismatch
[Review artifact] anonymous + runnable / gaps: <list>
[Release artifact] archived + licensed / gaps: <list>
[Rights] code+data+media licenses set / open questions: <list>
[Top fixes] <ordered>
```
