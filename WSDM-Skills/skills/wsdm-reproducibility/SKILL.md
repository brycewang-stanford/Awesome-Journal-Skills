---
name: wsdm-reproducibility
description: Use when hardening the reproducibility of a WSDM paper built on logs, graphs, or user-interaction data - provenance of behavioral datasets, temporal split discipline, click-bias assumptions, seed and variance reporting, privacy-preserving release, and honesty tiers for results no outsider can rerun.
---

# WSDM Reproducibility

Make a web-search/data-mining paper re-derivable. WSDM has no reproducibility
checklist to fill (none surfaced for current editions; 待核实 each cycle) - which
raises the bar rather than lowering it, because reviewers apply the norm
without giving you a form to hide behind. The venue-specific twist: WSDM
evidence usually comes from *behavioral* data (queries, clicks, follows,
purchases), and behavioral data has failure modes that generic ML
reproducibility advice never mentions.

## Provenance: behavioral data decays

A log dataset is a measurement of a platform at a moment - the platform's
ranker, UI, and user base are all baked into it. Reproducibility therefore
starts with recording what generated the data:

- Collection window, platform surface (web vs app, market/locale), and any
  known ranker or UI changes inside the window.
- The logging policy: what produced the exposures users could click on. A
  click log is a *logged-policy* artifact; results on it are conditional on
  that policy (this is the entire lesson of the position-bias and unbiased
  learning-to-rank literature born at this venue).
- Filtering steps with counts at every stage: bots removed, sessions
  segmented, minimum-activity thresholds. Two labs "using the same dataset"
  routinely diverge purely on preprocessing counts.

## Temporal discipline

Random splits on interaction data leak the future into training. Default to
time-based splits and document them to the day:

```yaml
# split-manifest.yaml - ship with the artifact, cite in the paper
dataset: platform-logs-v3
train:  {start: 2025-01-06, end: 2025-05-31}
valid:  {start: 2025-06-01, end: 2025-06-14}
test:   {start: 2025-06-15, end: 2025-06-28}
user_handling: users may span splits (temporal, not user-disjoint)
item_handling: cold items in test retained; reported separately
leakage_checks:
  - no feature computed over any window overlapping valid/test
  - global statistics (IDF, popularity) frozen at train end
notes: one ranker deployment change on 2025-04-12 inside train window
```

State whether users are shared across splits (temporal split) or disjoint
(generalization-to-new-users split) - the two answer different questions and
mixing them is a classic silent irreproducibility source in recommendation
papers.

## Bias assumptions are part of the method

If the paper estimates relevance or preference from clicks, its results depend
on an exposure/position-bias model. Reproducibility means naming it:

| What you assume | What must be reported |
|---|---|
| Position bias (examination model) | The propensity model, how it was estimated, on what data |
| No exposure bias (rare, say so) | Why the setting justifies it |
| Popularity/selection bias corrected | The correction estimator and its hyperparameters |
| Offline metrics proxy online value | The known gap, plus any online evidence |

An unstated bias model makes the numbers unreproducible even with the code,
because a re-implementer will pick a different default.

## Runs, seeds, and variance

- Report the number of runs and the seed policy for every learned component;
  ranking metrics on sparse test sets are noisy, and single-run nDCG deltas of
  under a point are routinely within seed variance.
- Give variance (std or CI) for headline comparisons; where a system-scale
  experiment genuinely cannot be repeated, say "single run" in the table note
  rather than letting the reader assume otherwise.
- Statistical tests over query/user-level paired differences beat aggregate
  deltas; state the unit of analysis (query, session, user) - it changes the
  test.

## The honesty ladder for unrerunnable results

Industrial WSDM papers often include numbers nobody outside can regenerate
(online A/B tests, full-traffic logs). Use graded language that matches the
evidence tier, and put the tier in the paper:

1. **Rerunnable**: public data + released code; anyone can regenerate tables.
2. **Rebuildable**: released code + documented proprietary pipeline; an insider
   could regenerate, an outsider can audit the logic.
3. **Attested**: online/production results reported with measurement protocol
   (traffic share, duration, metric definitions, guardrails) but not
   regenerable. Attested numbers support deployment claims, not method-ranking
   claims - do not let an A/B win stand in for a missing offline comparison.

## Privacy is a reproducibility constraint, not an excuse

WSDM requires an ethical-considerations section; user-data handling belongs in
it. De-identification, aggregation thresholds, and consent/ToS basis for the
data should be stated - and any released sample must survive a re-identification
sniff test (rare queries and long-tail items are quasi-identifiers). "We cannot
release anything" is acceptable only alongside rung 2-3 evidence above and a
public-benchmark mirror where feasible (see `wsdm-artifact-evaluation`).

## Pre-submission reproducibility sweep

Run once when experiments freeze, once on the final PDF:

```text
[ ] Data provenance paragraph: window, surface, logging policy, filters+counts
[ ] Split manifest shipped and cited; user-sharing across splits stated
[ ] Bias/exposure model named, with estimation procedure and data
[ ] Seeds and run counts per learned component; variance on headline deltas
[ ] Unit of analysis named for every statistical test
[ ] Each result family labeled: rerunnable / rebuildable / attested
[ ] Attested results carry protocol: traffic %, duration, metric definitions
[ ] Released sample re-identification check done (rare queries, tail items)
[ ] Ethics section covers user-data basis and mitigations, specifically
[ ] Repo numbers regenerate paper tables (spot-check two tables end-to-end)
```

Items that fail with no time to fix become limitation sentences, not
silence - at a no-rebuttal venue, a disclosed gap is survivable and a
discovered one usually is not.

## Output format

```text
[Provenance] window / surface / logging policy / filter counts: recorded? 
[Splits] temporal manifest present; user-sharing stated: yes / no
[Bias model] named + estimation reported: yes / no / not applicable
[Variance] runs, seeds, CI/test + unit of analysis per headline table
[Tier] rerunnable / rebuildable / attested per result family
[Privacy] ethics-section coverage of user data: adequate / gaps listed
```
