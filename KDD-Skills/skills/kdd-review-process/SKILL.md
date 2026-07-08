---
name: kdd-review-process
description: Use when reasoning about how KDD papers get judged in its dual-cycle OpenReview process: per-review rebuttal, area-chair recommendations weighed on merit through reproducibility and ethics, PC-chair decisions, the Resubmit outcome feeding the next cycle, the mixed academic-industry reviewer pool, and generative-AI review rules.
---

# KDD Review Process

Use this to model decisions rather than guess at them. KDD review runs on OpenReview,
per track and per cycle (the venue groups are literally named by track x cycle, e.g.
`Research_Track_Cycle_2`). Reconfirm the current cycle's mechanics before relying on
any stage detail — KDD tunes its process between cycles, not just between years.

## Decision machinery

- **Reviewers** score against the CFP's stated factors: technical merit, originality,
  potential impact, quality of execution, quality of presentation, related work,
  reproducibility of results, and ethics.
- **Authors** respond to each review in the rebuttal window — text only, no
  hyperlinks.
- **Area chairs** synthesize reviews, rebuttals, and reviewer discussion into a
  recommendation.
- **PC chairs** make final decisions. This last step is real, not ceremonial:
  calibration across areas happens above the AC.

## The three-outcome game

Unlike single-shot venues, KDD's decision space includes **Resubmit**, and the CFP
frames resubmissions that properly address noted concerns as having better odds than
fresh submissions. Strategic consequences:

| Outcome | What it means | Author's next move |
|---|---|---|
| Accept | Proceedings slot (uniform 12-page budget) | Camera-ready via e-rights + TAPS (`kdd-camera-ready`) |
| Resubmit | Fixable weaknesses named; invitation to the next cycle | Address concerns, declare prior forum id, prepend one-page change summary (`kdd-supplementary`) |
| Reject | Fit or soundness failure | Re-route (`kdd-topic-selection`) or rebuild before any KDD return |

Treat reviews of a Resubmit paper as a contract: the next cycle's AC sees the old
forum, so selectively ignoring named concerns is visible and costly.

## Who reviews at KDD

The pool mixes academic data-mining researchers with industry practitioners — a
KDD-specific blend with predictable reading patterns:

- The academic reader audits novelty against the mining literature and checks whether
  ablations isolate the claimed mechanism.
- The practitioner reader audits data realism: temporal splits, leakage, baseline
  tuning symmetry, and whether "deployable" claims survive contact with production
  constraints.
- A paper that satisfies one reader and insults the other (elegant method on toy
  splits; solid system with no delta over known methods) lands in the borderline pile
  where the rebuttal decides.

## Review-integrity rules worth knowing as an author

- KDD 2026 forbade reviewers from pasting any passage of a paper under review into
  generative-AI tools verbatim, and required authors to disclose their own
  generative-AI use in the submission form. Symmetrically, your rebuttal should not
  read as unedited model output — ACs increasingly discount it.
- Confidentiality runs both directions; do not cite or publicize reviewer text during
  the process.

## Reading a KDD review packet

```text
Triage order for a 3-4 review packet:
1. Extract every sentence naming a missing experiment, baseline, or
   leakage risk -> these are Resubmit-contract items.
2. Classify each reviewer: academic-lens / practitioner-lens / unclear
   (their objections need different evidence types in rebuttal).
3. Find the AC-visible consensus: an objection raised independently
   twice outweighs any single reviewer's pet issue.
4. Score your realistic ceiling: all-borderline packets are rebuttal-
   winnable; a unanimous soundness objection is a next-cycle project.
```

## Cycle dynamics

- Two cycles a year change the rejection calculus: the distance from a Cycle 1
  decision to the Cycle 2 deadline is short, so "fix and resubmit" is a same-year
  path — plan experiment capacity for it before the decision arrives.
- Per-cycle notification and discussion dates for the current cycle were not
  publicly verifiable at pack-build time (待核实); pull them from the OpenReview
  group or CFP timeline before promising a calendar to co-authors.

## Leverage per decision factor

The CFP's factor list is long; leverage over it is not uniform. Where author effort
converts into recommendation movement:

| Decision factor | Raises it | Sinks it |
|---|---|---|
| Technical merit | Mechanism isolated by ablation; complexity stated and measured | Gains attributable to tuning asymmetry or leakage |
| Originality | Mechanism-level delta over the KDD lineage | "First to apply X to Y" with no structural argument |
| Potential impact | Evidence someone else can use it (artifact, generality across regimes) | Impact claimed via market-size rhetoric |
| Execution quality | Temporal-safe splits, strong boring baselines | One-seed results at the flagship scale claim |
| Presentation | Regime-first page one; findable evidence | Appendix doing the arguing |
| Related work | Nearest ancestors contrasted, venues correct | Misattributed classics; surveyed families without deltas |
| Reproducibility | Tier-honest availability statements | Paper-artifact contradictions |
| Ethics | Data provenance and consent story stated | Scraped-data hand-waving on human data |

## Stage-by-stage realism

- **Bidding/assignment**: the registered abstract determines who bids; a misleading
  abstract buys mismatched experts (`kdd-submission`).
- **Reviews land**: score the packet against the ceiling model above before drafting
  anything; rebuttal energy is finite.
- **Discussion**: reviewers converge more than they diverge; the rebuttal's job is to
  arm the sympathetic reviewer with checkable coordinates.
- **AC recommendation**: written for the PC chairs, so the rebuttal summary line the
  AC can quote verbatim is the highest-value sentence you write all cycle.
- **PC decision**: calibration can move borderline cases both directions; nothing an
  author does at this stage helps, which is why the earlier stages get the effort.

## Output format

```text
[Stage] submitted / reviews-in / rebuttal / decision / resubmit-window
[Packet read] R-lenses: <academic/practitioner mix>, consensus objection: <...>
[Realistic ceiling] accept / borderline-rebuttal-decides / resubmit-target
[Resubmit contract] <named concerns that must be addressed if returning>
[Integrity checks] genAI disclosure filed / confidentiality clean
[Next move] <one action with owner>
```
