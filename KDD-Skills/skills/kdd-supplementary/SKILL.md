---
name: kdd-supplementary
description: Use when splitting a KDD paper across its 8 content pages, the optional appendix after the references, and the cited repository, under the camera-ready rule capping references plus appendix at 3 of 12 pages. Covers appendix triage, reviewer-discretion reality, and the one-page cross-cycle resubmission change summary.
---

# KDD Supplementary

Use this when distributing material across the three containers a KDD submission
actually has: the 8 content pages, the optional appendix after the references, and the
repository cited in the PDF. KDD has no separate supplement upload deadline in the
2026 pattern — the appendix travels inside the submission PDF — which makes the split
decision a writing-time decision, not a deadline-week one.

## The container model

| Container | Size discipline | Reviewer obligation | Survives to proceedings? |
|---|---|---|---|
| 8 content pages | Hard budget | Must be reviewable standalone | Yes, grows to 9 |
| Appendix (after refs) | Unbounded at submission (verify current CFP) | Discretionary reading | Only within the 3-page refs+appendix cap |
| Cited repository | Practically unbounded | Rarely opened; never linkable again after submission | Yes, as the public artifact |

The asymmetry between submission and camera-ready is the planning trap: an appendix
that balloons to 15 pages at submission must shrink to fit **references + appendix
within 3 pages** of the 12-page proceedings version. Anything you are not prepared to
delete or migrate to the repository later should not be load-bearing in review.

## What belongs where

**Content pages** — everything a reviewer needs to score the paper: the mechanism, the
main comparison table, the mechanism-isolating ablation, complexity statements, the
deployment metrics (ADS). The KDD failure pattern is a body that reads like an
extended abstract with "see Appendix" doing the arguing; reviewers score what they can
see in eight pages.

**Appendix** — proofs of stated propositions, full hyperparameter grids, per-dataset
result breakdowns, extra case studies, prompt/feature inventories, dataset
documentation. Order it by reference-frequency from the body, restate each claim
before its proof, and reference every appendix table from the body at least once —
orphaned appendix material is invisible under reviewer discretion.

**Repository** — anything executable, anything larger than a page of tables, extended
logs, and full configs. Remember the one-way door: the repo must be cited in the PDF
at submission because rebuttals cannot introduce links (see `kdd-artifact-evaluation`).

## Resubmission special page

A paper returning after a Resubmit decision prepends a **one-page summary of changes
as the first page of the PDF**, alongside the previous OpenReview forum id in the
form. Treat that page as the highest-value real estate in the resubmission:

```text
Summary of Changes (Resubmission of forum <id>)

R1-W1 "no ablation isolating the decay mechanism"
  -> New Table 5 (Sec 5.3): decay ablation across all datasets.
R2-W1 "temporal leakage suspected in splits"
  -> Splits rebuilt time-ordered (Sec 4.2); all tables regenerated;
     headline delta changed from +4.1 to +3.3, conclusions unchanged.
R3-W2 "claims exceed tested scale"
  -> Claim scoped to <=2.1B events (Abstract, Sec 1); added 2.1B-event run.
Unaddressed: R2-W3 (user study) - out of scope, argued in Sec 6.
```

Point-by-point, mapped to sections, honest about what changed numerically and what
was declined — this is the page the new area chair reads first.

## Appendix triage pass (pre-deadline)

1. List every appendix section with the body reference(s) that point to it; delete
   sections with zero inbound references or add the reference.
2. For each, ask: if a reviewer never opens this, does any scored dimension drop? If
   yes, promote its key row/claim into the body.
3. Mark each section's camera-ready fate now: `migrate-to-body`, `compress`,
   `move-to-repo`, or `cut` — the 3-page cap arrives with acceptance.
4. Anonymity-sweep the appendix with the same rigor as the body; grant numbers and
   internal system names hide in appendix footnotes.

## Vignette: splitting a graph-systems paper

A submission proposes a partitioning scheme for distributed GNN training with a
cost-model analysis, twelve datasets, and a parameter study. The split that survives
both review and the eventual 3-page cap:

- **Body**: the partitioning mechanism with its one algorithm block, the cost-model
  proposition (statement plus intuition), the main table on the five most
  informative datasets, the mechanism ablation, and the scaling figure.
- **Appendix**: the cost-model proof, the remaining seven datasets' rows, the full
  parameter sweep, and cluster configuration details — each referenced from the body
  ("full results in Appendix A.2").
- **Repository**: the partitioner implementation, per-dataset configs, the raw sweep
  logs, and the plotting scripts.
- **Camera-ready fates decided at submission time**: proof → compress to one column;
  seven-dataset table → move to repo with a pointer; parameter sweep → cut, summary
  sentence stays.

Nothing in the appendix is load-bearing for the score; everything in it answers a
question a reviewer might ask. That is the target state.

## Appendix anti-patterns seen at this venue

- **The overflow appendix**: paragraphs that clearly belong to Section 4 but were
  pushed out at the page limit, complete with dangling "as discussed above"
  references. Reviewers read it as a 9th content page smuggled past the budget.
- **The dataset dump**: twenty per-dataset tables with no summary statistic in the
  body; the body should carry the aggregate, the appendix the breakdown.
- **The unreviewed method**: a "practical extension" appearing only in the appendix
  and then claimed in the conclusion — claims live where reviewers score them.
- **The stale appendix**: numbers regenerated in the body but not in the appendix
  after a late pipeline fix; run the consistency diff before upload.

## Cycle-volatile mechanics to reconfirm

- Whether the current cycle caps appendix length at submission or allows separate
  supplementary uploads in the OpenReview form (待核实 per cycle).
- Whether reviewers are instructed that appendix reading is optional — assume yes
  and write the body accordingly.
- The exact camera-ready arithmetic: the 9-content/3-refs+appendix/12-total split is
  the 2026 rule; later cycles may rebalance it.

## Output format

```text
[Container split] body: <sections> / appendix: <sections> / repo: <items>
[Standalone test] body scoreable without appendix: yes / no -> <promotions needed>
[Orphan check] appendix sections w/o body references: <list or none>
[Camera-ready fates] <section -> migrate/compress/move-to-repo/cut>
[Resubmission page] present + point-by-point / N-A
[Anonymity] appendix + repo sweep: clean / findings
```
