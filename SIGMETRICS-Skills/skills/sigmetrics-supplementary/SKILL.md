---
name: sigmetrics-supplementary
description: Use when deciding what belongs in an ACM SIGMETRICS paper body versus its appendices and anonymized artifact, covering the 20-page single-column acmsmall budget, the rule that decision-critical claims (theorem statements, assumptions, headline validation) stay inside the reviewed pages, full proofs in appendices, double-anonymous supplementary material, and how to split a proof-plus-measurement paper.
---

# SIGMETRICS Supplementary

Use this when assembling SIGMETRICS supplementary material. The governing rule is simple and strict:
**the paper must be judgeable from the reviewed pages alone.** Appendices and the artifact support
the paper; they do not hold the argument. Reviewers read the artifact at their discretion, so
anything the decision depends on — the theorem statements, their assumptions, and the headline
validation — lives in the body.

## What goes where

| Content | Body (within the 20-page budget) | Appendix / artifact |
|---|---|---|
| Theorem/bound statements and their assumptions | Yes | — |
| Full proofs | The statement + key idea | Full derivations (appendix) |
| The model and why its assumptions are plausible | Yes | Extended sensitivity analysis |
| The headline analysis-vs-measurement validation | Yes | Full simulation sweeps, extra distributions |
| Baselines and the main comparison | Yes | Full parameter grids, per-workload tables |
| Simulator, trace-processing scripts, seeds | — | Yes (anonymized) |
| Trace/dataset itself | Summary + provenance | The processed dataset (or documented access) |

If a reviewer would need to open the artifact (or dig into an appendix) to know whether the central
claim holds, the paper is mis-partitioned — move that evidence into the body.

## The page-budget discipline

SIGMETRICS's acmsmall budget (2026: 20 pages of technical content including tables and figures; plus
**unlimited references**) is single-column and finite for everything except references. Consequences:

- Keep every **theorem statement, its assumptions, and the one figure showing
  analysis-vs-simulation agreement in the body** — they are decision-critical.
- **Full proofs** typically go to an appendix; confirm on the current call whether appendices count
  against the 20 pages or attach separately, because that changes the split.
- Do not use the appendix or artifact to smuggle in a result that would not fit — a bound whose
  proof only closes in supplementary material the reviewer may not read reads as unreviewable.

## Double-anonymous supplementary rules

```text
[No identity]   no authors, affiliations, acknowledgements, grants, cluster paths, group/system
                names, or trace provenance revealing the institution -- except in the Operational
                Systems Track, which may name the system/org
[Anonymized links] any code/data link points at an anonymizing host, not a personal repo
[Clean archive]  no .git history, .DS_Store, credentials, caches, or large irrelevant files
[Opens clean]    verify the archive unzips and a README orients a reader in one minute on a fresh
                machine (what the model is, how to regenerate a figure, how to check a proof)
```

## Appendix architecture

- Order appendix sections to mirror the paper: proofs in theorem order, then extended validation.
- Keep each appendix section referenced from the body at least once — orphaned proofs and sweeps are
  invisible under discretionary review.
- A proof appendix should restate the theorem and its assumptions at the top, so it is checkable
  without flipping back to the body.

## Vignette: splitting a proof-plus-measurement paper

A paper with a scheduling theorem and a trace-driven evaluation: the body keeps the model, the
theorem statements with assumptions, the proof ideas, the headline analysis-vs-simulation figure,
and the main trace-driven comparison with effect sizes; the appendix holds the full proofs and an
assumption-sensitivity sweep; the artifact holds the seeded simulator, the trace-processing scripts
with pinned provenance, and the analysis notebooks. Nothing decision-critical lives only in the
artifact, because artifact inspection is discretionary and the reviewers judge from the pages.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical (theorem/assumption/headline validation) outside the body? <none / move: what>
[Page budget] body within 20 pages? appendices counted correctly per the call? yes/no
[Anonymity] archive + appendix clean of identity + metadata? passed/issues (note Operational-track exception)
[Body dependency] <what a reviewer can decide without opening the artifact>
```
