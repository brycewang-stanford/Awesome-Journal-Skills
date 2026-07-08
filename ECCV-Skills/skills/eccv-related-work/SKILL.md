---
name: eccv-related-work
description: Use when positioning an ECCV submission in the literature — covering the two intervening CVPR/ICCV cycles since the last ECCV, March-deadline concurrent-work conventions, the no-self-repo citation rule, Springer-vs-CVF venue attribution hygiene, and turning a numbered LNCS bibliography into an argument.
---

# ECCV Related Work

Use this when auditing novelty positioning for ECCV. The venue's cadence
sets the task: since the previous ECCV, **two CVPRs and one ICCV** have
published — for a 2026 submission, that means CVPR 2024, ICCV 2025, and
CVPR 2025 (plus early-2026 arXiv) all landed after ECCV 2024. A related-work
section that stops at the last even year reads as two years stale.

## Coverage sweep, ordered by reviewer expectation

1. **The direct lineage**: the three to five papers your method visibly
   descends from, with the mechanism-level difference stated per paper.
2. **The intervening cycles**: CVPR/ICCV work from the odd-year gap that
   attacks the same task — the in-niche reviewer's first check.
3. **The concurrent band**: arXiv papers within a few months of the March
   deadline; conventions below.
4. **The classical root**: pre-deep or early-deep work the task descends
   from — European panels notice (and reward) correct genealogy more than
   most venues.

## Concurrent-work conventions around a March deadline

- Treat unpublished arXiv work from the months near the deadline as
  concurrent: cite it, mark it "(concurrent)", compare qualitatively if
  feasible, but reviewers cannot require you to beat it. The exact cutoff
  convention is per-cycle policy — 待核实 in the current author FAQ.
- ECCV 2026's dual-submission rule defined "publication" as peer-reviewed,
  accepted, and longer than four pages excluding references — arXiv
  preprints and tech reports did not count as publications, for your
  eligibility *and* for what you can be scooped by.
- Your own prior arXiv posting is legal (not an anonymity violation), but
  the submission must cite it in third person like a stranger's work, and
  must **not cite your own public codebase** — that link is treated as an
  identity leak.

## Venue attribution hygiene

ECCV's version of record is **Springer LNCS**, not CVF open access — and
vision bibliographies chronically misattribute across the big three. Check
each load-bearing citation against the actual proceedings:

| Error pattern | Example trap | Check against |
|---|---|---|
| ECCV paper cited as CVPR/ICCV | SSD and Perceptual Losses are ECCV 2016, not CVPR | SpringerLink `link.springer.com/conference/eccv` |
| Sibling paper credited to ECCV | Mask R-CNN is ICCV 2017; ResNet is CVPR 2016 | CVF open access for CVF venues |
| arXiv year vs proceedings year | Preprint 2025, proceedings 2026 | dblp entry |
| "ECCV" for a workshop paper | ECCV workshop ≠ main conference in LNCS subline | The specific LNCS volume front matter |

## Making numbered citations argue

LNCS numeric style hides authorship, so the prose must carry the argument:

```text
Weak:   "Many works study X [4,9,12,17,21]."
Strong: "Two families address X: geometry-based pipelines [4,9] that
         require per-scene optimization, and feed-forward models [12,17]
         that trade accuracy for speed; [21] sits between them but
         assumes calibrated cameras. We remove that assumption."
```

Every citation cluster should end with the sentence that says what *you* do
differently — otherwise the cluster is a bibliography, not related work.

## Differentiation stress test

Before the freeze, answer in one written sentence each:

- Which single existing paper would a hostile reviewer say already does this?
- What breaks if that paper's method is run on your exact setting?
- Which intervening-cycle paper is closest, and does your experiments
  section actually contain it as a baseline (`eccv-experiments`)?

If question three's answer is "cited but not compared", fix the experiment
or pre-empt in text why comparison is impossible — silence is the reject.

## Output format

```text
[Coverage status] <lineage / intervening-cycle / concurrent / classical gaps>
[Attribution audit] <citation -> verified venue, errors found>
[Anonymity conflicts] <own-work citations, repo links to remove>
[Closest rival] <paper -> baseline present? / preempted in text?>
[Cluster rewrites] <bibliography-style cluster -> argument sentence>
```
