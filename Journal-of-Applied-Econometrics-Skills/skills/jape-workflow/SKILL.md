---
name: jape-workflow
description: Use when planning the full Journal of Applied Econometrics (JAE) manuscript lifecycle end to end — confirming an applied (not pure-theory) fit, running reproducible analysis under the 35-page limit, and staging the mandatory JAE Data Archive deposit. Orchestrator skill; routes to the other eleven.
---

# JAE Manuscript Workflow (jape-workflow)

## When to trigger

- Starting a paper aimed at the Journal of Applied Econometrics and wanting the whole path mapped
- Deciding which JAE-specific skill to invoke next
- Sanity-checking that a project fits JAE's empirical, replicable scope

## Orient first

JAE (Wiley, since 1986, Editor-in-Chief Barbara Rossi, 7 issues/year) publishes **applied** econometrics — techniques applied to **real data**, not pure theory. Its signature is **reproducibility**: accepted papers must deposit a complete set of non-confidential data (and typically code) in the **JAE Data Archive** (running since 1994, now hosted at ZBW). Plan that deposit from day one; it is not an afterthought.

## Lifecycle → owning skill

1. **Fit & framing** — application on real data, not a theorem → `jape-topic-selection`, `jape-contribution-framing`
2. **Positioning** — applied-econometrics precedent + JAE corpus → `jape-literature-positioning`
3. **Design** — credible identification defended on real data → `jape-identification-strategy`
4. **Analysis** — reproducible estimation, robust inference → `jape-data-analysis`
5. **Exhibits** — within the **35-page** limit; detail to the unlimited online appendix → `jape-tables-figures`
6. **Writing** — 100-word citation-free summary, six keywords, COI statement → `jape-writing-style`
7. **Replication** — plain ASCII/CSV + readme + programs → `jape-replication-and-data-policy`
8. **Submit** — Free Format via Editorial Express; ≤ 3 papers per author under review → `jape-submission`
9. **Review** — single-blind; Editor-in-Chief decides → `jape-review-process`
10. **Revise** — rebuttal to single-blind referees → `jape-rebuttal`

## Anti-patterns

- Treating data deposit as a post-acceptance chore
- Sending a pure-theory paper to an *applied* journal
- Overflowing 35 pages instead of using the online appendix

## Output format

```
【Fit】applied on real data, replicable? [Y/N]
【Stage】lifecycle step (1–10)
【Next skill】which JAE skill now
【Archive】data/code on track for the Data Archive? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JAE URLs behind every fact
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling
