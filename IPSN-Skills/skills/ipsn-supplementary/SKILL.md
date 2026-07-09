---
name: ipsn-supplementary
description: Use when deciding what belongs in an IPSN-lineage paper body versus its artifact, appendix, and demo/poster track, covering the ≤12-page ACM two-column budget, the rule that decision-critical evidence stays inside the reviewed pages, double-blind supplementary material, dataset release, and how to split a sensor-systems paper between body and package.
---

# IPSN Supplementary

Use this when assembling IPSN supplementary material. The governing rule is simple and strict: **the
paper must be judgeable from the reviewed pages alone.** The artifact, appendix, and any dataset
support the paper; they do not hold the argument. Reviewers open the artifact at their discretion, so
anything the decision depends on lives in the ≤12-page body.

## What goes where

| Content | Body (within page budget) | Artifact / appendix |
|---|---|---|
| The sensing claim and its answer | Yes | — |
| Core method (IP) or platform design (SPOTS) | Yes | Full parameter grids, extra config, board files |
| Headline energy/latency/accuracy numbers + how measured | Yes | Full measurement logs, per-run traces |
| Deployment yield / sync / loss headline | Yes | Full per-node, per-day breakdowns |
| Ground-truth methodology | Named + summarized | The reference data and calibration logs |
| Raw traces, firmware, scripts | — | Yes |
| Secondary plots, extra sites, sensitivity sweeps | A pointer | Yes |

If a reviewer would need to open the artifact or a demo to know whether to accept, the paper is
mis-partitioned — move that evidence into the body.

## The ≤12-page discipline

IPSN's ACM two-column budget (IPSN 2024: **≤12 pages inclusive** of figures, tables, and references;
successor SenSys: 12/6) is compact and counts everything. Consequences:

- The energy/latency budget, the primary results with ground truth, and the limits section are
  decision-critical — keep them **in the body**.
- Long protocol tables, per-node deployment breakdowns, full sensitivity sweeps, and extra sites go
  to the artifact/appendix with explicit forward references.
- Do not use the artifact to smuggle in a result that would not fit — an argument that only closes
  with material outside the reviewed pages reads as unreviewable.
- There is no separate reference allowance in the inclusive budget; a bloated bibliography costs body
  space directly.

## Double-blind supplementary rules

```text
[No identity]   no authors, affiliations, acknowledgements, grants, lab-named testbeds, or repo owners
                anywhere in the archive, appendix, board files, or imagery
[Anonymized links] dataset/firmware links point at an anonymizing host, not a personal repo or a DOI
                that resolves to an author
[Clean imagery]  board photos and scope screenshots stripped of lab logos/watermarks; site names generalized
[Clean archive]  no .git history, credentials, caches, or large irrelevant binaries
[Opens clean]    the archive unzips and a README orients a reviewer in one minute on a fresh machine
```

## Demo/poster and dataset paths

- IPSN ran a separate **demos/posters** track (its own HotCRP historically). A live-hardware demo or
  a poster is a different deliverable from the paper — do not rely on it to carry the paper's
  argument. In the merged successor, demos/posters publish in the **IEEE** proceedings (verify).
- A **dataset release** can be a first-class contribution, but at submission it must be anonymized;
  reserve the DOI-issuing archive (Zenodo / IEEE DataPort) for camera-ready.

## Appendix architecture (when the template allows in-paper appendices)

- Order appendix sections to mirror the evaluation order; reviewers navigate by claim, not page
  number.
- Keep each appendix section referenced from the body at least once — orphaned material is invisible
  under discretionary review.
- Confirm on the current call whether appendices count against the ≤12-page budget or attach
  separately; this varies and changes the split.

## Vignette: splitting a deployment paper

A paper deploying nodes with an on-device estimator: the body keeps the sensing claim, the method,
the headline energy/yield/accuracy numbers with ground truth, and a limits subsection; the artifact
holds firmware and board files, the raw traces, the surveyed ground truth and calibration, the
per-node/per-day breakdowns, and the analysis scripts. Nothing decision-critical lives only in the
artifact, because artifact inspection is discretionary and reviewers judge from the pages.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical outside the body? <none / move: what>
[Page budget] body within ≤12 pp inclusive? appendices counted correctly? yes/no
[Anonymity] archive + board files + imagery clean of identity? passed/issues
[Body dependency] <what a reviewer can decide without opening the artifact/demo>
```
