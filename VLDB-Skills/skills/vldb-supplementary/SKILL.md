---
name: vldb-supplementary
description: Use when deciding what lives outside a PVLDB paper's page budget, covering the rule that appendices count against the limit, the extended technical report on arXiv under single-blind review, proof and algorithm placement, artifact repositories as the extra-results home, and keeping the paper self-contained for VLDB reviewers.
---

# VLDB Supplementary

Use this when the paper is overflowing its category budget. PVLDB's constraint
is unusual: **references are free, but appendices are not** — every page of
appendix, acknowledgement, or extra table counts inside the 12 (or 8, or 6)
page limit. There is no separate supplementary upload lane to hide length in,
so "supplementary material" at this venue means things that live *outside the
PDF entirely*.

## The three external homes

| Home | Best for | Constraint |
|---|---|---|
| Extended technical report (arXiv or institutional) | Full proofs, extra experiments, parameter sweeps, tuning details | Cite it from the paper by version; single-blind review makes this uncomplicated |
| Artifact repository | Configs, raw results, additional plots, per-workload breakdowns | Must be tagged so cited numbers stay stable |
| The paper itself | Anything a reviewer needs to *judge* the claims | The only place reviewers are obliged to look |

Because PVLDB review is single-blind, posting the extended report under your
own names is normal practice, not an anonymity hazard — the inverse of the
double-anonymous venues in this collection. (Reconfirm the current identity
policy on the live volume guidelines; see the source map.)

## The self-containment test

Reviewers commit to the PDF, not to your links. Before exporting content:

- Every claim in the abstract must be substantiated *inside* the paper — a
  headline result whose only evidence is "see the TR" is unreviewable.
- Keep one representative experiment per claim in the body; export the
  sensitivity grid, not the flagship curve.
- Keep algorithm pseudocode for the core mechanism; export correctness proofs
  if long, but keep the theorem statement and a two-line argument sketch.
- Never export the competitor-fairness details (versions, tuning); reviewers
  check those during, not after, review.

## Cut order when 14 pages must become 12

```text
1. Redundant transitions and roadmap prose        (~0.5 pp, free)
2. Sensitivity sweeps -> TR, keep one sentence each (~1 pp)
3. Secondary workload's full plots -> TR, keep summary table (~0.5-1 pp)
4. Long proofs -> TR, keep statements + sketches   (~0.5 pp)
5. NEVER: experimental setup, baseline tuning disclosure,
   limitations, or the one experiment behind each claim
```

## Version discipline for external material

- Freeze the TR version you cite (arXiv vN, not the bare identifier) at
  submission time; updating the TR mid-review silently changes what reviewers
  read.
- If a revision verdict arrives, the new experiments belong in the *paper*
  first — the required-changes list is judged on the PDF, and exporting a
  demanded result to the TR reads as evasion.
- Sync the repository tag whenever the TR gains results, so the three
  artifacts (paper, TR, repo) never disagree on a number.

## Failure patterns

- The two-body problem: paper and TR drift until a reviewer finds a
  contradicting number — instant credibility loss.
- Link-dependence: a body that reads like an index into external material.
- Budget denial: planning "we'll appendix it" at a venue where the appendix
  eats the same 12 pages.

## Output format

```text
[Budget state] <pages used / category limit>
[Export plan] <item -> TR / repo, estimated savings>
[Self-containment] passes / claims relying on external evidence listed
[Version pins] TR version, repo tag, consistency check
[Kept in body] <setup, fairness ledger, per-claim evidence — confirmed>
```
