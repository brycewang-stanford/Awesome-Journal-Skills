---
name: icsme-supplementary
description: Use when deciding what belongs in an IEEE ICSME paper body versus its anonymized artifact and appendices, covering the IEEEtran two-column 10-page budget where figures and appendices count, the rule that decision-critical evidence stays inside the reviewed pages, double-anonymous supplementary material, and how to split a mining/evolution paper between body and package.
---

# ICSME Supplementary

Use this when assembling ICSME supplementary material. The governing rule is simple and strict:
**the paper must be judgeable from the reviewed pages alone.** The artifact and any appendix support
the paper; they do not hold the argument. Reviewers read the artifact at their discretion, so
anything the decision depends on lives in the 10 pages — and there is no revision round to move it
in later.

## What goes where

| Content | Body (within the 10-page budget) | Artifact / appendix |
|---|---|---|
| Research questions and their answers | Yes | — |
| Core technique or study design | Yes | Full parameter grids, extra config |
| The headline evolution results and their threats | Yes | Full result tables, secondary plots |
| Statistical tests behind a claim | The result + test named | The computation notebook |
| Subject-system list and selection criterion | Summary + criterion | The complete list with SHAs |
| Mining pipeline detail | The protocol in prose | The scripts and pipeline diagram |
| Raw corpus, logs, scripts | — | Yes |
| Reproduction instructions | A pointer | The README and run scripts |

If a reviewer would need to open the artifact to know whether to accept, the paper is
mis-partitioned — move that evidence into the body.

## The 10-page discipline (figures and appendices count)

ICSME's IEEEtran two-column budget (2026: 10 pages including figures, tables, and appendices, plus
2 reference-only pages) is tighter than FSE's single-column allowance. Consequences:

- Keep the full threats-to-validity treatment and the primary result tables **in the body** — they
  are decision-critical and cannot be delegated to the artifact.
- Long per-subject breakdowns, the full mining pipeline diagram, and additional RQ variants go to
  the artifact with explicit forward references.
- **In-paper appendices count against the 10 pages** — do not use an appendix to smuggle back space
  the two-column limit denied you.
- Do not use the artifact to smuggle in a result that would not fit; an argument that only closes
  with material outside the reviewed pages reads as unreviewable.

## Double-anonymous supplementary rules

```text
[No identity]   no authors, affiliations, acknowledgements, grants, cluster paths, repo owners, or
                your own org's project as a named subject anywhere in the archive or appendix
[Anonymized links] the data-availability link points at an anonymizing host, not a personal repo
[Clean archive]  no .git history, .DS_Store, credentials, caches, or large irrelevant corpora dumps
[Opens clean]    verify the archive unzips and the README orients a reader in one minute on a
                fresh machine
```

## Appendix architecture (within the budget)

- Order appendix sections to mirror the RQ order; reviewers navigate by RQ, not page number.
- Keep each appendix section referenced from the body at least once — orphaned material is invisible
  under discretionary review.
- Confirm on the current call whether any online appendix is permitted separately from the 10 pages;
  historically ICSME counts in-paper appendices against the limit and expects the rest in the
  artifact.

## Vignette: splitting a mining + interview paper

A paper mining commit history plus interviewing maintainers: the body keeps the RQs, the study
design, the headline quantitative evolution results with effect sizes, the key qualitative themes,
and a threats subsection; the artifact holds the mining scripts with pinned SHAs, the extracted
corpus, the full codebook with inter-rater agreement, the interview protocol, and the analysis
notebooks. Nothing decision-critical lives only in the artifact, because artifact inspection is
discretionary and the reviewers judge from the 10 pages.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical outside the body? <none / move: what>
[Page budget] body within 10 pages (figures+appendices counted)? refs within 2? yes/no
[Anonymity] archive clean of identity + metadata + own-org subjects? passed/issues
[Body dependency] <what a reviewer can decide without opening the artifact>
```
