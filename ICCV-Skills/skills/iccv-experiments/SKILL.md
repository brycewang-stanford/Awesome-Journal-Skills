---
name: iccv-experiments
description: Use when designing the experimental program for an ICCV paper against the early-March deadline, covering benchmark-drift audits across the two-year gap, baseline fairness in the foundation-model era, ablations that isolate mechanisms, qualitative and failure evidence, and sequencing runs so the decisive result lands before the deadline, not after.
---

# ICCV Experiments

An ICCV experimental program is built under a fixed, unrepeatable date: the
early-March deadline of an odd year (March 7 in 2025, with supplement due the
same day). The program design problem is therefore *sequencing under a
deadline*, on top of the usual question of what evidence convinces a vision
reviewer. Both are handled here.

## Start with the benchmark-drift audit

Because the venue is biennial, a project conceived after one ICCV and submitted
to the next spans two years of field motion. Before designing experiments, audit
what moved:

```text
drift audit (fill once, in the autumn before the deadline)
  benchmarks:   which datasets did the last two years of CVPR/ECCV/ICCV papers
                in this area actually evaluate on? any new canonical benchmark?
  baselines:    leaderboard top-3 today vs when the project started
                → any baseline in your draft older than ~18 months is a red flag
  backbones:    what does current SOTA initialize from? (matching this defines
                "fair" for your comparisons)
  metrics:      any metric revision or new evaluation server since last cycle?
  protocols:    resolution/prompt/eval-harness conventions that changed
```

Papers rejected for "outdated comparisons" are usually not lazy — they froze
their experiment matrix at project start and never re-based. Re-run the audit in
January; two months before an ICCV deadline is exactly when the previous
November's CVPR-cycle preprints flood arXiv.

## The fairness ledger

Vision reviewers' most reliable objection is compute-and-pretraining confounds
dressed as method wins. Make fairness auditable with a ledger column per
comparison:

| Axis | Your method | Each baseline | Mismatch handling |
|---|---|---|---|
| Backbone + init checkpoint | | | Match, or add a matched row |
| Pretraining data exposure | | | Disclose; beware test-adjacent leakage in web-scale corpora |
| Input resolution / tokens | | | Match or tabulate both |
| Training schedule + budget | | | Report epochs and GPU-hours side by side |
| Number quoted vs re-run | | | Mark re-runs; footnote protocol deltas |

The foundation-model twist: when everything builds on the same giant checkpoint,
*data exposure* replaces architecture as the confound reviewers hunt. If your
improvement could plausibly come from the pretrain having seen the test domain,
run the decontamination or cross-domain check before a reviewer asks for it in a
window when you have one rebuttal page to respond.

## Ablations that isolate, not decorate

Structure the ablation grid so every row flips one switch, and include the two
rows that distinguish a mechanism from a lucky configuration: the *transplant*
(your module inserted into a baseline — does the gain travel?) and the
*sensitivity sweep* (is the headline number a plateau or a spike?). Rows argued
from in the text belong in the body; the full grid goes to the same-day
supplement. If the core ablation shows the mechanism is not doing the work, that
is an October discovery you want in November — which is why it runs first (see
sequencing below).

## Qualitative evidence with stated rules

At a venue that reviews with its eyes, image and video evidence carries real
weight and attracts real skepticism. Three requirements: a declared selection
rule on every grid ("first N val images", "random seed 0" — curation without a
rule is what reviewers assume by default); side-by-sides against the two
strongest baselines on identical inputs; and a failure-mode section with a
taxonomy, previewed in the body and cataloged in the supplement. For temporal or
3D claims, the supplement video is the primary exhibit — packaging in
`iccv-supplementary`.

## Sequencing runs toward March

The scarce resource is calendar, not GPUs. Order the program by *decision value
per week*:

1. **Falsifiers first** (autumn): the core ablation and the strongest baseline
   comparison. If the idea dies, it dies while retargeting to CVPR-November is
   still possible (`iccv-workflow`'s autumn fork).
2. **Headline table** (winter): full benchmark suite, matched settings, seeds on
   the cheap rows.
3. **Breadth pass** (January): second domain, transfer, robustness suite —
   whatever supports the claim's outer scope.
4. **Freeze margin** (mid-February): the main table freezes ~2–3 weeks out; the
   deadline is same-day for the supplement, so late results have no legal
   landing zone except the rebuttal — and reviewers may not request major new
   experiments anyway.
5. **Rebuttal reserve**: hold 10–20% of compute for May; the most common
   winnable rebuttal item is a small matched re-run reported as a mini-table
   (`iccv-author-response`).

```python
# deadline_math.py — sanity-check the plan against the calendar
runs = {"core_ablation": 6, "main_table": 21, "breadth": 10}   # GPU-days each
gpu = 8; days_left = (deadline - today).days - 18              # freeze margin
assert sum(runs.values()) / gpu <= days_left, "cut scope now, not in February"
```

## The four questions any ICCV review silently asks

Does it work (main table, matched)? Why does it work (isolating ablations +
transplant)? Where does it break (failure taxonomy, honest transfer results)?
What does it cost (params, latency on named hardware, training GPU-hours —
volunteered, since no form mandates it; see `iccv-reproducibility`)? Draft the
experiments section as answers to these four, in this order, and the reviewer's
checklist fills itself.

## Reverify each cycle

- The 2027 deadline chain — sequencing above is calendar-shaped and the calendar
  is 待核实 until posted.
- Whether supplements stay same-day (changes step 4).
- Evaluation-server rules and submission budgets on your benchmarks.
- Any new ethics/human-data documentation the 2027 forms may require.

## Output format

```text
[Drift audit] run on <date>; stale baselines found: <list>
[Fairness ledger] axes matched or disclosed per comparison: n/m
[Ablation] one-switch rows: <n>; transplant + sensitivity present: yes/no
[Qualitative] selection rules stated · failure taxonomy drafted
[Sequencing] falsifiers scheduled before <date>; rebuttal reserve: <GPU-days>
[Cut candidates] <lowest decision-value runs if the calendar slips>
```
