---
name: wsdm-supplementary
description: Use when deciding what goes where in a WSDM submission whose appendices count inside the page cap - triage between the 9-page body, the uncounted references and ethics section, and the cited external repository; compression tactics for proofs, prompts, and hyperparameter tables under WSDM's historically tight budget.
---

# WSDM Supplementary Material

Allocate content across WSDM's three containers. The defining constraint,
verified for the 2026 edition: **appendices are inside the 9-page cap**, and
only references plus the required ethical-considerations section sit outside
it (2025: 8 pages + at most 2 for references-plus-ethics). WSDM has kept a
famously lean budget since its early editions, and no separate
supplementary-upload channel was verified for current cycles (待核实 - if the
current CFP adds one, re-plan around it). So "put it in the supplement" is not
an available sentence here; the real containers are:

| Container | Counted? | Reviewer obligation | Right contents |
|---|---|---|---|
| Body (≤9 pp incl. appendices, 2026) | Yes | Read | Claims, method, all decisive evidence |
| References | No | Consulted | Complete citations - never compressed |
| Ethics section | No | Read as ethics | Societal impact, privacy, misuse, mitigations |
| Cited anonymous repository | No | Voluntary | Code, configs, raw results, full prompts, extra ablations |

## Triage rule: decisive vs supporting vs archival

- **Decisive** evidence - anything a reviewer needs to believe a headline claim
  (main comparisons, the ablation that isolates the mechanism, the bias-control
  analysis) - must be in the body. A decisive table living only in the repo is
  invisible: consulting it is voluntary and many reviewers will not.
- **Supporting** material - per-dataset breakdowns, sensitivity sweeps,
  secondary metrics - goes to a compact in-budget appendix *if* space remains,
  else to the repository with a one-line pointer stating what is there.
- **Archival** material - raw logs of runs, full hyperparameter grids, prompt
  transcripts - always repository.

The failure mode to catch in review-of-the-draft: a 9th page spent on a
supporting sensitivity sweep while the decisive ablation is squeezed into a
footnote. Rank content by claim-criticality, not by writing order.

## Compression tactics that keep meaning

1. **Merge, don't shrink, tables.** Two 6-column tables over the same systems
   become one 8-column table; dropping font size below the class minimum is a
   format violation, merging is craft.
2. **Plot the sweep, table the winner.** A hyperparameter study is one small
   figure; the chosen values go in one row of a settings table; the full grid
   goes to the repo.
3. **State theorems, sketch proofs.** WSDM papers with formal results give the
   statement plus a 3-5 line proof sketch in the body and the full proof in an
   in-budget appendix only when it is short; otherwise the repo carries a PDF
   note - and the claim sentence must not overreach what the sketch shows.
4. **Prompts by exemplar.** For foundation-model components, show one
   representative prompt inline (verbatim, boxed) and point to the repo for the
   full set; paraphrased prompts are unreproducible.
5. **Ethics section carries ethics.** Resist parking experimental overflow
   there; the SPC reads it and the move is transparent.

## The pointer pattern

Every externalized item gets an explicit, specific in-body pointer so reviewers
know evidence exists and was not hidden:

```latex
% Good: specific, verifiable, sets expectations
Full per-locale results (12 markets), the complete prompt set, and the
seed-level metric dumps behind Tables~2--4 are in the anonymous
repository \cite{anonrepo}, directory \texttt{results/}.

% Bad: vague hand-wave reviewers rightly distrust
Additional experiments are available in our repository.
```

And the repository must deliver: a pointer to a directory that does not exist,
or to results that mismatch the paper's numbers, is worse than no pointer.

## Budget worksheet

Run this a week before the deadline, not the night of:

```text
page budget (2026 anchor)        9.00
- title/abstract/intro           1.25
- related work                   0.75
- method                         2.50
- experimental setup             1.25
- results + ablations            2.50
- discussion/limitations/concl.  0.50
- in-budget appendix             0.25
                                 ----
head-room                        0.00   <- if negative, cut supporting
references                       uncounted
ethics section                   uncounted (but write it properly)
```

If head-room is negative, cut in this order: supporting appendix -> secondary
metric columns -> related-work prose (compress to positioning, see
`wsdm-related-work`) -> introduction repetition. Never cut: setup details that
gate reproducibility, limitations, or the decisive ablation.

## Edge cases

- **Short-track papers** (track introduced in 2026) compress the same triage
  into a smaller budget: there is no room for any in-budget appendix at all,
  so the split is binary - body or repository. Verify the short-paper cap in
  the current call; the pack could not pin the 2026 number (待核实).
- **Demonstrations** were capped at 4 pages *inclusive of references* in 2026
  - a different counting rule than the long track in the same year. Never
  assume counting rules transfer across tracks of the same edition.
- **Theory-heavy papers**: when full proofs genuinely cannot fit in budget,
  the honest structures are (a) a shortened conference claim whose proof does
  fit, or (b) a companion technical-report/preprint cited openly - checking
  first that the current anonymity rules permit citing it without breaking
  blinding (an anonymized preprint pointer in the repo is the safe default).
- **Cross-edition drift**: the 2025→2026 change moved references and ethics
  from a shared 2-page allowance to unrestricted space while pulling
  appendices inside the cap. Assume the containers change again; re-derive
  this skill's table from the current CFP before applying it.

## Output format

```text
[Container map] body / references / ethics / repo allocation per artifact
[Decisive-in-body check] all headline-claim evidence in the 9 pages: yes / no
[Budget] worksheet head-room: +/- N pages; cut list if negative
[Pointers] each external item has a specific in-body pointer: yes / gaps
[Repo delivery] pointers resolve and numbers match: verified / pending
```
