---
name: socc-supplementary
description: Use when deciding what belongs in an ACM SoCC paper body versus its released artifact and appendices, covering the acmart 12-page (full) or 6-page (short) budget with unlimited references, the rule that decision-critical evidence stays inside the reviewed pages, dual-anonymous supplementary material, and how to split a cloud-systems measurement paper between body and package.
---

# SoCC Supplementary

Use this when assembling SoCC supplementary material. The governing rule is simple and strict: **the
paper must be judgeable from the reviewed pages alone.** The released artifact and any appendix
support the paper; they do not hold the argument. Reviewers read the artifact at their discretion,
so anything the decision depends on — the headline throughput, tail, and cost results — lives in the
body.

## What goes where

| Content | Body (within page budget) | Artifact / appendix |
|---|---|---|
| The cloud problem and the contribution | Yes | — |
| Core mechanism or measurement design | Yes | Full config grids, extra parameters |
| Headline throughput / **tail** / **cost** results | Yes | Full result tables, secondary regimes |
| The key baseline comparison | The result + baseline named and tuned | The full sweep and raw logs |
| Testbed / trace description | Summary + key parameters | The complete node list, full trace spec |
| Raw logs, workload generators, replay scripts | — | Yes |
| Reproduction instructions | A pointer | The README and run scripts |

If a reviewer would need to open the artifact to know whether to accept — for instance to find the
p99 or the cost breakdown — the paper is mis-partitioned; move that evidence into the body.

## The page-budget discipline

SoCC's `acmart` budget (full: **12 pages** of text and figures; short: **6 pages**), with
**unlimited references**, counts figures, tables, and any in-paper appendix. Consequences:

- Keep the **tail and cost** results and the primary baseline comparison **in the body** — they are
  decision-critical at a cloud venue.
- Long configuration sweeps, per-node breakdowns, and additional workload regimes go to the artifact
  with explicit forward references.
- The unlimited-reference allowance is for the bibliography only; it does not let body text or
  decision-critical figures escape the 12/6-page limit.
- Do not use the artifact to smuggle in a result that would not fit — an argument that only closes
  with material outside the reviewed pages reads as unreviewable.

## Dual-anonymous supplementary rules

```text
[No identity]   no authors, affiliations, acknowledgements, grants, cluster names, provider hints,
                or repository owners anywhere in the archive or appendix
[Anonymized links] the availability link points at an anonymizing host, not a personal/corporate repo
[Scrubbed traces]  released traces carry no identifying provenance (org name, internal IDs)
[Clean archive]  no .git history, .DS_Store, credentials, caches, or large irrelevant files
[Opens clean]    verify the archive unpacks and the README orients a reader in one minute on a
                fresh machine
```

## Appendix architecture (when the template allows in-paper appendices)

- Order appendix sections to mirror the result order; reviewers navigate by claim, not page number.
- Keep each appendix section referenced from the body at least once — orphaned material is invisible
  under discretionary review.
- Confirm on the current call whether in-paper appendices count against the 12/6-page budget; this
  varies and changes the split.

## Vignette: splitting a cloud-systems measurement paper

A paper measuring a scheduler on a replayed trace: the body keeps the problem, the mechanism, the
headline throughput/p99/cost results with tuned baselines, the key trade-off figure, and a
limitations paragraph; the artifact holds the replay harness, the (anonymized) trace, the full
config sweep, the per-node logs, and the analysis scripts. Nothing decision-critical lives only in
the artifact, because artifact inspection is discretionary and the reviewers judge from the pages.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical (tail/cost/baseline) outside the body? <none / move: what>
[Page budget] body within 12/6 pages? references-only unlimited allowance respected? yes/no
[Anonymity] archive + traces clean of identity + metadata? passed/issues
[Body dependency] <what a reviewer can decide without opening the artifact>
```
