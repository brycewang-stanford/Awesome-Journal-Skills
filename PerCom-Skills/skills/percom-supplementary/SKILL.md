---
name: percom-supplementary
description: Use when deciding what belongs in an IEEE PerCom paper body versus its dataset/artifact and any appendix, covering the tight IEEEtran 9+1 page budget, the rule that decision-critical evidence stays inside the reviewed pages, double-blind supplementary material, and how to split a human-subjects sensing paper between body and dataset.
---

# PerCom Supplementary

Use this when assembling PerCom supplementary material. The governing rule is simple and strict:
**the paper must be judgeable from the reviewed pages alone.** The dataset and any appendix support
the paper; they do not hold the argument. Reviewers read supplementary material at their discretion,
so anything the decision depends on lives in the 9 pages — and PerCom's budget is **tight**, which
makes the split unforgiving.

## What goes where

| Content | Body (within 9-page budget) | Dataset / appendix |
|---|---|---|
| The pervasive-computing claim and headline result | Yes | — |
| Core technique or study design | Yes | Full hyperparameter grids, extra config |
| The **cross-subject (LOSO)** headline evaluation | Yes | Full per-subject / per-session tables |
| Metrics behind a claim (F1, event-level) | The result + metric named | The computation notebook |
| Subject and sensor description | Summary + selection criterion | The complete datasheet |
| Raw signals, logs, labels, scripts | — | Yes |
| Reproduction instructions | A pointer | The README and run scripts |

If a reviewer would need to open the dataset to know whether to accept, the paper is
mis-partitioned — move that evidence into the body.

## The 9-page-budget discipline

PerCom's IEEEtran budget (**9 pages** technical content + **1 page** references) is a fraction of a
single-column ACM budget and counts figures, tables, and any in-paper appendix. Consequences:

- The **cross-subject result and its key limitation must be in the body** — they are
  decision-critical, and reviewers will not go hunting for them.
- Long per-subject breakdowns, full hyperparameter grids, additional sensor modalities, and extra
  ablations go to the dataset/appendix with explicit forward references.
- Do **not** use the dataset to smuggle in a result that would not fit — an argument that only
  closes with material outside the reviewed pages reads as unreviewable.
- Compress with editing (tighter figures, merged tables), never by shrinking the font or margins —
  that is a desk-reject ground at IEEE venues (`percom-submission`).

## Double-blind supplementary rules

```text
[No identity]   no authors, affiliations, acknowledgements, grants, testbed/lab names, deployment
                sites, or dataset-owner strings anywhere in the archive or appendix
[Anonymized links] the dataset/code link points at an anonymizing host, not a personal repo
[Clean archive]  no .git history, .DS_Store, credentials, caches, or large irrelevant files
[No re-ID media] no photos/video revealing a face, building, or badge that de-anonymizes authors
[Opens clean]    verify the archive unzips and the README orients a reader in one minute on a
                fresh machine
```

## Appendix architecture (when the template allows in-paper appendices)

- Remember appendices **count against the 9 pages** — an in-paper appendix trades against the body.
  Prefer the external dataset/artifact for bulk material.
- Order any appendix to mirror the RQ / evaluation order; reviewers navigate by claim, not page.
- Keep each appendix section referenced from the body at least once — orphaned material is invisible
  under discretionary review.

## Vignette: splitting a mixed-modality sensing paper

A paper combining wrist-IMU recognition with an ambient-sensor deployment: the body keeps the claim,
the study design, the **leave-one-subject-out** headline result with F1 and confidence intervals,
the key deployment finding, and a limitations subsection; the dataset/artifact holds the full
per-subject tables, the ambient-sensor logs, the labeling protocol with annotator agreement, the
device/sampling datasheet, and the analysis notebooks. Nothing decision-critical lives only in the
artifact, because artifact inspection is discretionary and the reviewers judge from the 9 pages.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical (esp. cross-subject result) outside the body? <none / move: what>
[Page budget] body within 9 pages? appendices counted? refs within 1 page? yes/no
[Anonymity] archive clean of identity + re-identifying media? passed/issues
[Body dependency] <what a reviewer can decide without opening the dataset>
```
