---
name: webconf-reproducibility
description: Use when hardening the reproducibility of a Web Conference (WWW) paper whose evidence rests on crawls, platform APIs, live systems, or user logs — covering dataset decay, temporal snapshots, seed and environment reporting, the reproducibility appendix inside the 12-page PDF, and honest claims when the Web itself cannot be replayed.
---

# Web Conference Reproducibility

Reproducibility at this venue has a problem no offline-ML venue has: **the object
of study mutates**. Pages die, APIs close, ranking systems retrain, platform
policies change what may be collected at all. A Web Conference paper is
reproducible to the degree that it *pins what can be pinned and measures what
cannot*. The 2026 CFP's sanctioned home for this material is the optional appendix
— "details on reproducibility, proofs, pseudo-code" — inside the same 12-page PDF,
which reviewers are not obliged to read; so the reproducibility *claims* go in the
main 8 pages and the reproducibility *mechanics* go in the appendix.

## Three reproducibility regimes

| Regime | Example evidence | What "reproducible" means | Your obligation |
|---|---|---|---|
| Frozen | Public benchmark, released crawl | Re-run → same numbers | Seeds, versions, exact splits |
| Decaying | Your own crawl, API pulls | Re-collect → quantifiably similar corpus | Snapshot, checksums, collection code, date stamps |
| Unreplayable | Live A/B test, production traffic, human subjects | Independent teams can audit the protocol | Full protocol, power analysis, aggregate release |

Most reviews go wrong when a paper claims regime-1 language ("fully reproducible")
for regime-2 or regime-3 evidence. Classify every experiment in the paper into a
regime and phrase its claim accordingly; the honest sentence "results on the live
platform are audit-reproducible but not replay-reproducible" has never sunk a
strong paper.

## Pinning the decaying regime

- **Date-stamp everything**: crawl window, API version, model checkpoints of any
  third-party service used (an LLM API call in 2025 is not the same function in
  2026 — record model name *and* version string).
- **Checksum the corpus** at collection time; publish per-file SHA-256 in a
  manifest so drift is detectable, not just suspected.
- **Prefer citable snapshots**: Common Crawl snapshot IDs, Internet Archive
  captures, Wikipedia dumps with dates — these convert a decaying corpus into a
  frozen one for everyone downstream.
- **Separate collection from analysis** in the codebase, so a future team can
  re-run analysis on your frozen snapshot even when re-collection is impossible.

## Determinism audit for the modeling stack

```python
# Repro header every experiment script in the artifact should share
import os, random, numpy as np, torch

SEED = int(os.environ.get("RUN_SEED", 17))
random.seed(SEED); np.random.seed(SEED); torch.manual_seed(SEED)
torch.use_deterministic_algorithms(True)          # surfaces nondeterministic ops
os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8" # required by some CUDA GEMMs

# Log the things people forget to log:
#   graph/dataloader shuffling seeds, negative-sampling seeds,
#   train/val/test split hash, library versions, GPU model, wall-clock.
```

Web-specific nondeterminism deserves explicit lines in the appendix: crawl
ordering, deduplication thresholds, timezone normalization of timestamps, and —
for graph papers — node ID remapping, which silently reorders neighbor sampling.

## Temporal honesty

Web data is time-indexed, and the venue's reviewers increasingly check for
**temporal leakage**: random splits over user-item interactions or evolving graphs
let the model train on the future. The reproducibility appendix should state the
split *rule* (e.g., "train < 2025-06-01 ≤ test"), not just percentages, and the
artifact should ship the split-generation code rather than opaque index files
alone. If the paper uses a random split on temporal data for comparability with
prior work, say so and add one temporal split as a robustness check — this
one-sentence-plus-one-table addition preempts the most common modern objection.

## Vignette: the benchmark that dissolved

A 2024-vintage misinformation dataset distributes tweet IDs for rehydration. By
the time a team builds on it for a WWW submission, 38% of the tweets are deleted,
suspended, or geo-blocked — and deletion is *not random*: the most-reported
content vanishes first. Naively rehydrating and comparing against the original
paper's numbers silently changes both the task and the class balance. The
regime-honest handling, which fits in four appendix sentences plus one table
column: report the rehydration date and survival rate, compare label distributions
between the original and surviving corpus, rerun the strongest baseline on the
surviving subset so all comparisons share one corpus, and phrase cross-paper
comparisons as indicative rather than head-to-head. Reviewers do not penalize
decay — it is the field's shared condition — but they increasingly penalize
pretending it did not happen.

## What goes where

1. **Main 8 pages**: one reproducibility paragraph — regime classification,
   snapshot/DOI pointers, seed policy, split rule. Claims a reviewer must weigh
   cannot hide past page 8.
2. **Appendix (within the 12)**: hyperparameter tables, environment details,
   collection protocol, per-dataset manifests, negative results of tuning.
3. **Artifact** (see `webconf-artifact-evaluation`): everything executable, the
   manifest with checksums, and the recrawl/dead-link accounting script.

A placement corollary for review strategy: because the appendix is optional
reading, a reviewer who doubts reproducibility may score the doubt without
opening Appendix B. The main-text paragraph therefore needs one *forward pointer
with content* — "seeds, environment, and the full collection protocol are in
App. B; the artifact reproduces Table 2 with one script" — so the doubt has an
address before it becomes a score.

## Pre-submission reproducibility gate

- [ ] Every experiment classified frozen / decaying / unreplayable, phrased to match.
- [ ] Collection dates, API versions, and third-party model versions stated.
- [ ] Split rules explicit; temporal data has a temporal split somewhere.
- [ ] Seeds and repetition counts reported; variance shown where runs repeat.
- [ ] A stranger with the appendix plus artifact could rebuild the headline table
      or, failing that, audit the protocol end to end.

## Output format

```text
[Regimes] frozen=<experiments> decaying=<...> unreplayable=<...>
[Pinning] dates/checksums/snapshots: complete / gaps <where>
[Temporal] split rule stated? leakage risk? robustness split present?
[Determinism] seed policy + environment logged: yes/no
[Placement] claims in main text, mechanics in appendix: verified
[Honesty edits] <sentences whose reproducibility claim overshoots the regime>
```
