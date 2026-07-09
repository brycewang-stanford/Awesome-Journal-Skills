---
name: infocom-supplementary
description: Use when deciding what fits inside an IEEE INFOCOM paper's tight IEEEtran budget, covering the rule that appendices count toward the nine pages of text, the absence of a separate supplementary channel at review time, double-blind handling of any released material, and how to split an analytical or systems networking paper between the body and an optional external release.
---

# INFOCOM Supplementary

Use this when assembling INFOCOM material. The governing fact is blunt: **there is no separate
supplementary or appendix upload at review time, and in-paper appendices count toward the nine
pages of text.** The paper must be **complete and judgeable from the ten-page PDF alone.** Anything
you want a reviewer to weigh must fit inside the budget; anything you release externally is optional
context they may not open.

## What goes where

| Content | Body (within the 9-page text budget) | Optional external release |
|---|---|---|
| Problem, system model, assumptions | Yes | — |
| Main theorems and their proof (sketch in body, full proof in in-budget appendix) | Yes | The long-form technical report, if any |
| Protocol/algorithm description | Yes | Reference implementation |
| Headline results and honest baselines | Yes | Full result tables, extra plots |
| Simulator configuration behind a claim | Named in the body | The scripts and configs |
| Trace/dataset | Source + selection criteria | The dataset itself (if releasable) |
| Reproduction instructions | A pointer (if you release) | The README and run scripts |

If a reviewer would need to open an external file to judge whether to accept, the paper is
mis-partitioned — the deciding evidence must be inside the ten pages, because reviewers are not
guaranteed to look further.

## The page-budget discipline (appendices included)

INFOCOM's IEEEtran budget is **10 pages maximum, with ≤9 pages for all text, figures, tables, and
appendices** — only references may use the 10th page. Consequences:

- **An in-paper appendix is not free space.** A full proof or a big parameter table in an appendix
  consumes the same nine-page budget as the introduction. Sketch proofs in the body and include the
  full proof only if it fits; otherwise cite a technical report.
- **There is no "move it to the supplement" escape.** Unlike venues with an unlimited appendix or a
  separate supplementary PDF, INFOCOM gives you one budget for everything a reviewer reads.
- **Do not smuggle a result into an external file.** An argument that only closes with material
  outside the ten pages reads as unreviewable at a venue with no rebuttal to explain it.

## Double-blind rules for any released material

```text
[No identity]   no authors, affiliations, acknowledgements, grants, cluster paths, or repo owners
                in any material linked from the submission
[Anonymized links] if you link a simulator/dataset for review, use an anonymizing host, not a
                personal repo or homepage
[Clean archive]  no .git history, credentials, or identifying trace names in released files
[Optional]      the reviewer may not open it — so nothing decision-critical lives only there
```

## In-budget appendix architecture

- Order appendix material to mirror the results it supports; a reviewer navigates by claim, not by
  page number.
- Keep every appendix section referenced from the body — orphaned derivations waste the budget.
- Measure the nine-page text boundary with references excluded; a proof that pushes text past nine
  pages makes the paper non-compliant, not merely long.

## Vignette: splitting an analytical + simulation paper

A paper with a competitive-ratio proof and a trace-driven evaluation: the body keeps the model, the
theorem with a proof sketch, the headline simulation results with confidence intervals, and a
limits paragraph; a tight in-budget appendix holds the full proof *only if it fits within nine
pages* (otherwise a cited technical report carries it); an optional public archive holds the
simulator scripts, the trace access, and the plotting code. Nothing that decides acceptance lives
only in the archive, because external material is discretionary and the reviewers judge from the
PDF.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical outside the 10-page PDF? <none / move: what>
[Page budget] text incl. appendices within 9 pages? refs within the 10th? yes/no
[Proof placement] sketch in body + full proof in-budget or in a cited report? yes/no
[Anonymity] any linked material clean of identity + metadata? passed/issues
```
