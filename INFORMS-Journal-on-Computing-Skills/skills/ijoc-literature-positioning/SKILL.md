---
name: ijoc-literature-positioning
description: Use when staking the computational/methodological contribution of an INFORMS Journal on Computing (IJOC) manuscript against OR/MS and CS prior art. Positions the advance relative to the right baselines and the right frontier; it does not invent citations.
---

# Literature Positioning (ijoc-literature-positioning)

## When to trigger

- Reviewers say "the contribution over existing methods is unclear" or "this is incremental"
- Your related-work section cites application papers but not the **algorithmic/computational** prior art you actually compete with
- You straddle OR and CS literatures and are unsure which frontier you are advancing
- A referee names a recent method you did not compare against, and you must decide whether it is the relevant baseline

## Positioning IJOC papers — two frontiers, one claim

An IJOC paper usually advances against **two literatures at once**: the OR/MS literature that owns the *problem* and the computing literature that owns the *method*. Your positioning must make clear which frontier you push and by how much, in computational terms. The decisive move is to identify the **state-of-the-art method you must beat or match**, cite it precisely, and commit to it as an experimental baseline. Vague positioning ("little work exists") reads as not having read the field and is a fast path to desk rejection by an Area Editor who knows it well.

| Your claim type | The prior art you must engage | The baseline this implies |
|-----------------|-------------------------------|---------------------------|
| New exact method, larger instances | best published exact method for this problem | re-run or cite its reported results on shared instances |
| New formulation, tighter bounds | strongest existing formulation / relaxation | root-gap and node-count comparison |
| New heuristic, better quality/time | the leading heuristic and the best exact bound | gap-to-optimal and time-to-target |
| ML-for-OR, learns to solve faster | both the OR baseline and prior learning approaches | beat the OR method *and* prior learning |
| New simulation/estimation method | prior estimators for the same estimand | variance/cost at equal accuracy |
| Software/tooling | prior tools and the methods they implement | feature/performance comparison, not just existence |

## Engaging recent work fairly

IJOC reviewers are active researchers in the chosen area; they will know the last two years of work. Cite the **most recent** competing methods, not only the classics, and state honestly where a competitor is still better (e.g., "Method X remains faster on dense instances; we win on sparse and large"). Honest scoping is more credible than a blanket "we outperform all." When a competitor's code is in the IJOC GitHub repository or a public repo, plan to actually run it rather than quoting stale numbers from different hardware.

## Sibling-journal framing in the related work

Position so the reader sees why this is IJOC and not a sibling: emphasize the **computational/methodological delta**. If the related work reads like an *Operations Research* model survey, the computing contribution is buried; if it reads like a CS algorithms paper with no OR task, the OR relevance is missing. The synthesis — "here is the OR problem, here is the computing frontier, here is the gap we close" — is the IJOC signature.

## Using the IJOC corpus and deposit as evidence

Two underused positioning moves are specific to IJOC. First, the **IJOC Software and Data Repository** means many recent competing methods ship with runnable code; cite those and, where feasible, re-run them on your instances rather than quoting heterogeneous published numbers — a re-run comparison is far more persuasive to a referee who knows the field. Second, IJOC's **"Test of Time" award** and its published archive signal which methods the area considers canonical; engaging those anchors your claim in the literature the Area Editor and reviewers actually hold as the bar. Position against the strongest *reproducible* competitor, not merely the most cited.

## Checklist

- [ ] The single state-of-the-art method you compete with is named and cited precisely
- [ ] Both the problem (OR/MS) literature and the method (computing) literature are engaged
- [ ] Recent (last ~2 years) competing methods are cited, not only canonical ones
- [ ] Each claimed advantage is tied to a baseline you will actually run or fairly quote
- [ ] Where a competitor is still better, the paper says so and scopes the claim
- [ ] The positioning makes the IJOC (not OR/MS/MPC/IJOO/CS) fit obvious
- [ ] No invented or padded citations; every cited result is checkable

## Anti-patterns

- "Little/no prior work exists" on a topic the Area Editor has published in
- Comparing only to old baselines while a current method dominates the field
- Citing application papers as if they were your methodological competitors
- Quoting a competitor's runtimes from a different machine as if comparable
- A related-work section that could belong to *Operations Research* or a CS venue with the journal name swapped
- Overclaiming "we outperform all existing methods" without per-regime honesty

## Output format

```text
【Journal】INFORMS Journal on Computing
【Skill】ijoc-literature-positioning
【SOTA to beat/match】named method + citation
【Frontier(s) advanced】OR/MS problem / computing method / both
【Claimed delta】the computational gap closed, in measurable terms
【Honest scoping】where a competitor still wins
【Sibling boundary】why IJOC and not OR / MS / MPC / IJOO / CS
【Next skill】ijoc-methods
```
