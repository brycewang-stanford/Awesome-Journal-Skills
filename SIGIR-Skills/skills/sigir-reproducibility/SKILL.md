---
name: sigir-reproducibility
description: Use when strengthening the reproducibility of a SIGIR paper or preparing a SIGIR Reproducibility track submission — pinning the retrieval pipeline, seeds and variance for neural rankers, documenting collection versions and index settings, and structuring a reproduction study of published IR results with honest divergence analysis.
---

# SIGIR Reproducibility

Reproducibility is unusually load-bearing at SIGIR for two reasons. First, the venue
runs a dedicated **Reproducibility track** (its own track in 2026, split out of the
former combined Resource & Reproducibility track — budget and dates 待核实 on the
current page), so reproduction studies are publishable first-class work. Second, the
field's own literature documents how often reported IR gains fail to replicate under
matched tuning — reviewers of *regular* papers therefore read reproducibility signals
as a proxy for whether the gains are real.

## Why IR results drift: the usual suspects

| Drift source | Typical symptom | Pin it by |
|---|---|---|
| Collection version | "MS MARCO" numbers off by points | Exact version/split ids, `ir_datasets` identifiers, checksums |
| Index-time analysis | BM25 baseline differs across papers | Scripted index build; record stemmer, stopwords, k1/b |
| Doc processing for neural models | Recall@k shifts | Max length, stride, title concatenation recorded as config |
| Truncated vs judged pools | Inflated dense-retrieval scores | State pooling; report judged@k alongside nDCG |
| Seeds and nondeterminism | ±0.005 nDCG run-to-run | Multiple seeds; report mean ± sd, not the best run |
| Eval tool discrepancies | MAP differs at 4th decimal | One canonical scorer (`trec_eval`/`ir_measures`) with flags recorded |
| Hyperparameter asymmetry | Baselines lose by under-tuning | Equal tuning budget, documented per system |

A reproducibility-strong SIGIR paper closes each row with an artifact, not a promise:
the config file *is* the documentation.

## Minimum reporting block for any empirical SIGIR paper

Put this in the paper (it fits in ~0.3 page and pre-empts three review objections):

- Collections with versions; train/dev/test usage; any filtering.
- Index/build settings for every system, baselines included.
- Tuning protocol: search space, budget, selection metric, dev split — symmetric
  across systems.
- Seeds: how many, and whether tables show mean, sd, and the significance test.
- Compute: hardware, wall-clock for index+train+retrieve, and query latency setup.
- Pointer to the repository with run files (see `sigir-artifact-evaluation`).

```yaml
# config-as-artifact: one file per reported system, committed to the repo
system: ours-dense-v2
collection: msmarco-passage/dev/small        # ir_datasets id
index: {tokenizer: bert-base-uncased, max_len: 256, stride: 128}
train: {seeds: [13, 42, 71], batch: 64, lr: 2e-5, epochs: 3}
eval: {tool: ir_measures, metrics: [nDCG@10, RR@10, R@1000], qrels: official}
significance: {test: paired-t, correction: bonferroni, alpha: 0.05}
```

## Writing a Reproducibility track paper

A reproduction study is not a re-run; it is an *investigation*. The track rewards:

1. **Target selection with stakes** — results the community builds on (a widely
   cited ranker, a standard baseline configuration, a claimed efficiency win).
2. **Faithful reimplementation first**: reproduce with the original artifacts where
   they exist; document every forced deviation and why.
3. **Divergence analysis as the contribution**: when numbers differ, isolate the
   cause (collection version? tuning? eval tool?) with controlled toggles — the
   drift table above is your experimental design.
4. **Generalization probes**: does the original conclusion survive new collections,
   matched tuning, or current baselines? "Holds, but the margin halves under equal
   tuning" is a publishable, community-serving finding.
5. **Respectful register**: the genre convention is scientific, not gotcha — criticize
   configurations, not authors, and give original authors' artifacts credit where due.

Anti-patterns the track's reviewers flag: reproducing only the headline number while
skipping ablations; declaring "failure to reproduce" without exhausting configuration
space; and shipping a reproduction whose *own* pipeline is unpinned (the irony reject).

## Decay planning: the three-year audience

A SIGIR paper's reproducibility has two audiences with different failure modes: the
reviewer this spring (needs the 10-minute runnable path) and the researcher in three
years (meets link rot, dataset takedowns, deprecated toolkit APIs, and vanished model
checkpoints). Plan for the second audience explicitly:

- Cite collections by **stable identifiers** (`ir_datasets` ids, TREC track names,
  dataset DOIs), never by lab-server URLs.
- Freeze an **archival copy** of your own artifacts (Zenodo/institutional DOI) at
  camera-ready; GitHub is a working mirror, not an archive.
- Record toolkit **versions in the paper text**, not only in the lockfile — the paper
  outlives the repository more often than authors expect.
- If a resource you depend on has restrictive terms (query logs, commercial APIs),
  state what a future reproducer *can* do without it: which tables survive, which die.
- Leave the qrels/run checksums in the repo README; three years later they are the
  only way to prove a re-download matches the evaluated state.

## Reproducibility as review defense for regular papers

- Close comparisons without variance are the most common SIGIR experimental
  criticism; three seeds with mean ± sd is cheap insurance for neural systems.
- An honest "we could not reproduce baseline X's published number; we report our
  best faithful configuration (details in repo)" reads as strength, not weakness —
  the community knows the drift problem intimately.
- Never copy baseline numbers across collections or eval setups from other papers'
  tables without saying so; mixed-provenance tables are a known reject trigger.

## Quick self-audit before submission

- [ ] Every number in every table regenerates from a shipped run file plus one
      documented command.
- [ ] Every system row has a config file; diffs between systems are visible as
      config diffs, not prose.
- [ ] The seeds behind each neural row are enumerable, and the shipped run is
      identified (which seed, or the per-topic mean).
- [ ] A colleague outside the project reproduced Table 1 from the repo README
      without asking questions (the strongest cheap test available).
- [ ] The paper's reporting block and the repo's configs agree — reviewers diff
      them when suspicious.

## Output format

```text
[Mode] hardening a regular paper / Reproducibility track study
[Drift audit] rows closed with artifacts: <k>/7 (collection/index/processing/pool/seed/tool/tuning)
[Reporting block] present in paper y/n; missing items <list>
[For repro studies] target + stakes / faithfulness log / divergence causes isolated
[Variance] seeds <n>, mean±sd shown y/n, test named y/n
[Biggest residual risk] <the one unpinned thing a reviewer will find>
```
