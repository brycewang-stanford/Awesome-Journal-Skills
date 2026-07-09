---
name: fse-supplementary
description: Use when deciding what belongs in an ESEC/FSE paper body versus its anonymized artifact and appendices, covering the ACM-template page budget, the rule that decision-critical evidence stays inside the reviewed pages, double-anonymous supplementary material, and how to split an empirical-SE paper between body and package.
---

# FSE Supplementary

Use this when assembling FSE supplementary material. The governing rule is simple and strict:
**the paper must be judgeable from the reviewed pages alone.** The artifact and any appendix
support the paper; they do not hold the argument. Reviewers read the artifact at their discretion,
so anything the decision depends on lives in the body.

## What goes where

| Content | Body (within page budget) | Artifact / appendix |
|---|---|---|
| Research questions and their answers | Yes | — |
| Core technique or study design | Yes | Full parameter grids, extra config |
| The headline results and their threats | Yes | Full result tables, secondary plots |
| Statistical tests behind a claim | The result + test named | The computation notebook |
| Subject-system list | Summary + selection criterion | The complete list |
| Raw data, logs, scripts | — | Yes |
| Reproduction instructions | A pointer | The README and run scripts |

If a reviewer would need to open the artifact to know whether to accept, the paper is
mis-partitioned — move that evidence into the body.

## The page-budget discipline

FSE's ACM-template budget (FSE 2027: ≤18 pages of text and figures, plus reference pages) is
generous compared with a two-column conference limit, but it is finite and counts figures, tables,
and any in-paper appendix. Consequences:

- You can usually keep a full threats-to-validity treatment and the primary result tables **in the
  body** — do so; they are decision-critical.
- Long protocol tables, per-subject breakdowns, and additional RQ variants go to the artifact with
  explicit forward references.
- Do not use the artifact to smuggle in a result that would not fit — an argument that only closes
  with material outside the reviewed pages reads as unreviewable.

## Double-anonymous supplementary rules

```text
[No identity]   no authors, affiliations, acknowledgements, grants, cluster paths, or repo owners
                anywhere in the archive or appendix
[Anonymized links] the Data Availability link points at an anonymizing host, not a personal repo
[Clean archive]  no .git history, .DS_Store, credentials, caches, or large irrelevant files
[Opens clean]    verify the archive unzips and the README orients a reader in one minute on a
                fresh machine
```

## Appendix architecture (when the template allows in-paper appendices)

- Order appendix sections to mirror the RQ order; reviewers navigate by RQ, not page number.
- Keep each appendix section referenced from the body at least once — orphaned material is invisible
  under discretionary review.
- Confirm on the current call whether appendices count against the page budget or attach
  separately; this varies and changes the split.

## Vignette: splitting a mixed-methods paper

A paper mining pull requests plus interviewing developers: the body keeps the RQs, the study
design, the headline quantitative results with effect sizes, the key qualitative themes, and a
threats subsection; the artifact holds the mining scripts with pinned SHAs, the extracted dataset,
the full codebook with inter-rater agreement, the interview protocol, and the analysis notebooks.
Nothing decision-critical lives only in the artifact, because artifact inspection is discretionary
and the reviewers judge from the pages.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical outside the body? <none / move: what>
[Page budget] body within limit? appendices counted correctly? yes/no
[Anonymity] archive clean of identity + metadata? passed/issues
[Body dependency] <what a reviewer can decide without opening the artifact>
```
