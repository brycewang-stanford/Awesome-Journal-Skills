---
name: edbt-supplementary
description: Use when deciding what belongs in an EDBT paper body versus its artifact and appendices, covering the per-shape page budget with unlimited references, the rule that decision-critical evidence stays inside the reviewed pages, and how to split a database-systems paper between body and reproducible package.
---

# EDBT Supplementary

Use this when assembling EDBT supplementary material. The governing rule is simple and strict: **the
paper must be judgeable from the reviewed pages alone.** The artifact and any appendix support the
paper; they do not hold the argument. Reviewers open the artifact at their discretion, so anything
the decision depends on lives in the body.

## What goes where

| Content | Body (within page budget) | Artifact / appendix |
|---|---|---|
| The problem, contribution, and what it enables | Yes | — |
| Core mechanism / system design | Yes | Full parameter grids, extra configs |
| The headline results and the scope/overhead | Yes | Full result tables, secondary sweeps |
| The evaluation setup a claim depends on | Named in the body | The complete harness and logs |
| Workload / dataset summary + derivation | Summary + criterion | The full derivation scripts and data |
| Raw logs, build scripts, containers | — | Yes |
| Reproduction instructions | A pointer | The README and run scripts |

If a reviewer would need to open the artifact to know whether to accept, the paper is
mis-partitioned — move that evidence into the body.

## The page-budget discipline (per shape)

EDBT's budget depends on the paper shape (EDBT 2022 CFP; reverify per cycle): **Regular** and
**Experiments & Analysis** papers ≤12 pages; **Vision** papers ≤6; **references are unlimited** and
do not count. Consequences:

- **References do not eat your budget** — cite generously; the constraint is body text, figures,
  tables, and in-body appendices.
- Keep the headline result tables and the scope/overhead discussion **in the body** — they are
  decision-critical.
- Long parameter sweeps, per-configuration breakdowns, and full harness output go to the artifact
  with explicit forward references.
- Do not use the artifact to smuggle in a result that would not fit — an argument that only closes
  with material outside the reviewed pages reads as unreviewable.

## Reproducibility-forward supplementary rules

```text
[Runnable]     the artifact builds and runs from its README on a clean machine; a demo run succeeds
[Provenance]   dataset versions, workload derivation, engine build/commit, and seeds are pinned
[Consistency]  every body number traces to a script in the package
[Clean archive] no stray credentials, caches, or huge irrelevant files; (if double-blind) no
                identity strings, owner paths, or cluster names
[Opens clean]  verify the archive unpacks and the README orients a reader in one minute
```

## Appendix architecture (when the template allows in-body appendices)

- Order appendix sections to mirror the evaluation's structure; reviewers navigate by result, not
  page number.
- Keep each appendix section referenced from the body at least once — orphaned material is invisible
  under discretionary review.
- Confirm on the current call whether in-body appendices count against the page budget (they usually
  do) versus supplementary material attached separately; this changes the split.

## Vignette: splitting a distributed-systems paper

A paper contributing a query-processing operator and its evaluation: the body keeps the problem, the
mechanism, the headline latency/scalability results with variance, the overhead-on-skew-free case,
and a scope subsection; the artifact holds the container/build recipe, the workload-derivation
scripts with pinned dataset versions, the full parameter sweeps, the raw logs, and the analysis
notebooks. Nothing decision-critical lives only in the artifact, because artifact inspection is
discretionary and the reviewers judge from the pages.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Shape + budget] Regular | Experiments-&-Analysis | Vision — body within limit?
[Partition check] anything decision-critical outside the body? <none / move: what>
[Reproducibility] artifact runnable + provenance pinned + consistent with paper? yes/no
[Clean archive] (if double-blind) identity-free; no stray files? passed/issues
[Body dependency] <what a reviewer can decide without opening the artifact>
```
