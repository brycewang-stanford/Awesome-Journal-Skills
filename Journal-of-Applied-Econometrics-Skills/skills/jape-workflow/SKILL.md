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

## Final-week gate

In the last week before submission, run the route in this order:

1. Reconfirm scope with `jape-topic-selection`: real-data application and replication path are still central.
2. Run `jape-data-analysis`: master script regenerates every article and appendix exhibit.
3. Run `jape-tables-figures`: article exhibits fit the 35-page limit and appendix material is staged.
4. Run `jape-replication-and-data-policy`: archive files, README, versions, and plain-text outputs match.
5. Run `jape-writing-style` and `jape-submission`: summary, keywords, declarations, and Editorial Express
   materials are consistent.

Do not submit if the manuscript PDF and archive package disagree about a sample, variable, seed, or table
label. That mismatch is a substantive credibility problem, not a clerical issue.

## Stage gates with archive checkpoints

The archive deposit is the thread that runs through every stage; verify it at each gate rather than once at the end:

| Gate | Pass condition | Archive checkpoint |
| --- | --- | --- |
| Project start | Real-data application with an econometric lesson | Data confirmed exportable to plain CSV/TXT, or documentable for access |
| First full draft | Estimand, design, inference all stated and tested | Master script regenerates every draft exhibit |
| Pre-submission | ≤35 pp text; summary ≤100 words, citation-free | Package cold-runs on a clean machine |
| Under review | — (wait; respect the 3-paper cap elsewhere) | Freeze the submitted package as a tagged version |
| Revision | Every referee point answered with evidence | Revised numbers and revised code committed together |
| Acceptance | Final exhibits match regenerated output digit-for-digit | Deposit to the ZBW-hosted archive with readme |

## Failure modes by lifecycle stage

- **Stage 1–2:** committing to data that later proves undepositable and undescribable — the project dies at acceptance, the worst possible time.
- **Stage 3–4:** inference chosen by software default rather than data structure; a JAE referee pool of inference specialists will catch it.
- **Stage 5–6:** robustness crammed into the article instead of the unlimited appendix, blowing the 35-page limit.
- **Stage 8–10:** manuscript revised but package not — the mismatch surfaces when the archive deposit is checked against the published paper.

## Worked routing decision (illustrative)

An author arrives with a finished panel-IV draft asking "what now?" Route: the draft is 39 pages → `jape-tables-figures` first (move two robustness grids to the appendix); the IV tables show no first-stage F → `jape-data-analysis` and `jape-identification-strategy` (effective F + Anderson–Rubin columns); data are a licensed commercial panel → `jape-replication-and-data-policy` (confidential-data readme + extraction code now, not after acceptance); only then `jape-writing-style` for the 100-word summary and `jape-submission` for Editorial Express. Three of the five stops exist only because the destination is JAE.

## Output format

```
【Fit】applied on real data, replicable? [Y/N]
【Stage】lifecycle step (1–10)
【Gate】current stage's archive checkpoint passed? [Y/N]
【Next skill】which JAE skill now
【Archive】data/code on track for the Data Archive? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JAE URLs behind every fact
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling
