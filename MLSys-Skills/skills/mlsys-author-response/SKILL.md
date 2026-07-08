---
name: mlsys-author-response
description: Use when drafting MLSys author responses on OpenReview under the venue's compressed rebuttal window, prioritizing systems-reviewer objections about workload representativeness, baseline tuning, and missing measurements, deciding whether to run new experiments in days, and keeping replies anonymous and decision-focused.
---

# MLSys Author Response

Use this when MLSys reviews land. The controlling fact about this venue's rebuttal is
**time**: in the 2026 cycle, reviews were released January 12 and author responses were due
January 16 — four days, including whatever new measurements you attempt. Verify the current
window on the mlsys.org dates page the day reviews are scheduled, then plan hours, not weeks.

## Hour-zero triage (the four-day clock)

| Window | Action |
|---|---|
| Hours 0-4 | All authors read all reviews once without replying; classify each point as factual error / missing measurement / scope objection / preference |
| Hours 4-12 | Decide the at-most-two new experiments that are actually runnable; launch them immediately — machines, not prose, are the bottleneck |
| Day 2 | Draft skeleton replies per reviewer around the launched runs; resolve internal disagreements about concessions |
| Day 3 | Insert numbers as runs finish; cut everything that does not move a score |
| Final hours | Anonymity and tone pass; submit well before the cutoff — OpenReview traffic spikes at deadline |

A run that cannot finish by day 3 does not exist for rebuttal purposes. Promise it for the
camera-ready or artifact instead of gambling the reply on it.

## What systems reviewers actually object to

- **"The workload is not representative."** The most common MLSys objection. Answer with
  evidence the workload matches a public trace, a named benchmark family (reviewers know the
  MLPerf lineage), or a measured production characteristic — or concede the scope and say so
  in one sentence.
- **"The baseline is not tuned."** Never answer defensively; state the tuning protocol
  (search space, budget, best configuration found) from the submission, or run the stronger
  configuration now and report it even if it narrows your win. A narrowed-but-honest gap
  gains more points than a defended-but-doubted one.
- **"Where is memory / p99 / cost / energy?"** If it is in the appendix, quote the exact
  number and its location — remember reviewers were not obliged to read the appendix. If it
  was never measured, this is your best candidate for the two rebuttal runs.
- **"The gain will vanish on hardware X / at scale Y."** Do not extrapolate. Give the
  mechanism-level argument for where the gain comes from, state the boundary honestly, and
  offer the analytical model or roofline reasoning if the paper has one.

## Reply skeleton per point

```text
> R2: "Throughput gains may come from batching, not the proposed scheduler."
We separated these in the submission: Table 4 (main paper, p.8) fixes batch size and
still shows 1.4x; the ablation with batching disabled entirely is Fig. 7.
New for this response: at R2's suggested batch=1 setting, the gain is 1.25x
(3 runs, std 0.02), consistent with the scheduler mechanism.
We will state the batch=1 result in Sec. 6.2.
```

Pattern: restate the objection in one line, anchor to a page/table in the submitted PDF,
add at most one new number with its run count and variance, commit to a specific edit.

## Rules and boundaries

- Stay anonymous — research-track responses must not reveal company, cluster names, or
  internal system identities even when doing so would answer the question crisply.
- Do not paste external links or point to updated arXiv versions unless the current cycle's
  instructions explicitly allow it; assume the submitted record is the whole record.
- Do not restructure the paper in prose ("we will rewrite Sections 3-5") — meta-reviewers
  read that as an admission the submission was not ready.
- Concede real limitations plainly. Systems reviewers reward "this does not help under
  uniform load, and we now say so" far more than a paragraph of deflection.
- One reply block per reviewer, ordered by their objections' impact on the decision, not by
  the order they were written.

## Prioritization when everything is on fire

1. A factual misreading by the most negative reviewer (cheapest score to recover).
2. A missing measurement that two or more reviewers independently requested.
3. The workload-representativeness objection, if raised.
4. Everything else, in one compact "minor points" list.

Leave stylistic complaints unanswered rather than crowding out the decision-critical
material; MLSys response formats are short, and the meta-reviewer skims for whether the
central systems objection was met.

## Worked triage: a typical MLSys review set

Fictional but representative packet for a serving-system paper, and the calls made:

- R1 (systems, negative): "evaluation uses synthetic Poisson arrivals; real traffic is
  bursty." → Decision-critical, and a run is feasible: replay a public trace on the
  smallest model overnight. This becomes rebuttal experiment #1.
- R2 (ML, lukewarm): "quality impact of request dropping never measured." → Second
  experiment: quality metric under the dropping policy, one model, three seeds.
- R3 (systems, positive but doubting generality): "single GPU generation tested." →
  No hardware available in-window. Answer with the mechanism argument: which hardware
  property the gain depends on, plus a scoped-claim edit offer. No run promised.
- All three: "writing dense in Section 4." → Two lines at the end: acknowledged, will
  split 4.2 and move the config table to the appendix.

The discipline: two launched runs, one mechanism argument, one batched concession —
and nothing else. Six half-answered points lose to three closed ones.

## Tone calibration

- Systems reviewers respect being corrected with data and resent being lectured about
  their own field; delete any sentence explaining basics ("as is well known in
  serving systems...").
- Thank reviewers once, globally, not per point — the response budget is too small for
  ritual.
- Where two reviewers contradict each other (one wants more breadth, one more depth),
  say so explicitly and state your choice; meta-reviewers reward authors who notice.

## Cycle-volatility warnings

- The four-day window, the response format, and whether a discussion phase follows the
  response are all cycle-specific; the 2026 numbers here are anchors, not promises.
- Whether reviewers may see updated PDFs during response varies — check the current
  OpenReview instructions rather than assuming.

## Output format

```text
[Deadline] <response due date + hours remaining>
[Runnable-by-deadline experiments] <at most two, with launch status>
[Reviewer map] <reviewer -> decision-critical objection -> anchor in submitted PDF>
[Concessions] <limitations to admit plainly>
[Draft reply] <per-reviewer text, anonymous, no links>
```
