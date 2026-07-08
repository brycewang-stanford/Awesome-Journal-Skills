---
name: cikm-experiments
description: Use when designing or auditing the empirical program of a CIKM paper — matching evidence to the claim's lanes across retrieval, mining, and knowledge-management evaluation cultures, choosing datasets and baselines that survive a blended panel, isolating the boundary mechanism, and meeting applied-track deployment-evidence bars.
---

# CIKM Experiments

The empirical program of a CIKM paper answers to three evaluation cultures. IR
culture wants ranked-metric discipline on recognized collections with significance
testing; mining culture wants mechanism isolation, scaling behavior, and honest
baselines; KM/database culture wants evidence that the method survives real data —
heterogeneous, noisy, incomplete. Design the experiment section as the union of what
the claimed lanes require, not the maximum of one.

## Claim-lane-evidence contract

For every claim sentence in the introduction, write down which lane it invokes and
what that lane's standard evidence is:

| Claim invokes... | Required evidence pattern | Frequent hole |
|---|---|---|
| Better retrieval/ranking | Standard collections, tuned baselines, metric@k with paired significance tests | Untuned baselines; "significant" without a test |
| A better mechanism | Ablation removing exactly that mechanism; sensitivity to its key parameter | Ablations that vary three things at once |
| Scalability | Time/memory vs. input-size curves on stated hardware | A single wall-clock number, no curve |
| Robust to real data | Noise/incompleteness injection or a genuinely messy dataset | Only clean benchmark data |
| KG/side-information helps | The identical model minus the KG, plus a KG-quality sweep | Confounding KG addition with capacity increase |
| Deployed impact (Applied track) | Launch evidence: online metrics, A/B or pre/post windows, traffic scale | Offline proxy metrics presented as deployment proof |

The Applied Research row is a track requirement, not a style preference: CIKM 2026's
call demands substantiation by a system launch, data release, or equivalent
practical evidence.

## Dataset strategy for a blended panel

- Include at least one dataset each lane recognizes as legitimate for the task —
  a public IR/recommendation benchmark, a graph/KG corpus, and (when claiming
  practice) an industrial or organizational dataset, released or described honestly.
- Report per-dataset licenses, sizes, and collection windows; the resource-minded
  part of the pool reads dataset tables the way IR readers read metric tables.
- For LLM-era work, state the contamination position: whether test queries,
  documents, or KG facts could sit in a pretrained model's training data, and what
  was done about it. The blended pool increasingly asks this across all lanes.

## Mechanism isolation at the boundary

CIKM contributions typically fuse components (a ranker + a KG; a miner + an index).
The decisive experiment is the one that holds the fusion fixed and removes only the
claimed novelty — otherwise the panel cannot tell the contribution from the
engineering. Budget for it first; it is the experiment reviewers ask for when it is
missing, and with no confirmed rebuttal channel at CIKM (待核实), a missing ablation
cannot be repaired mid-review.

## Reporting floor

```text
For every results table/figure:
  - datasets named with split protocol and seed policy
  - baseline tuning budget stated (same search space as the proposed method?)
  - variance across runs, and the test behind any "significant"
  - hardware + software versions for anything timed
  - pointer to the artifact path that regenerates it
```

The floor exists because the appendix cannot absorb it: 2026 budgets count
appendices inside the page limit, so this information lives in captions, in the
protocol paragraph, or in the cited artifact — never nowhere.

## Variance and significance protocol

The IR lane brings the family's strictest statistics culture, and it grades the
whole paper by these habits:

- Multiple runs with distinct seeds for anything stochastic; report the spread
  (std or CI), not just the best run — "best of five" is a red flag, "mean ± std
  of five" is the norm.
- Paired tests for system comparisons on shared queries/instances; say which test
  and at what level, and correct for multiple comparisons when sweeping many
  configurations.
- Effect sizes over asterisks alone: a 0.2-point gain can be "significant" on a
  large query set and still not matter; state both the margin and the test.
- Per-slice reporting when the claim is slice-shaped (the gains "concentrate on
  relation-dependent queries" claim needs the slice table that shows it).

## LLM-era pitfalls the panel now checks

- **Contamination**: pretrained components may have seen the test collections;
  state the exposure analysis or choose post-cutoff data.
- **LLM-as-judge**: if an LLM scores outputs, validate it against human labels on
  a sample and report agreement; unvalidated judge scores are decoration.
- **Prompt variance**: prompted baselines need the same tuning-budget parity as
  trained ones — report the prompt-search effort on both sides.
- **API drift**: hosted-model results must pin model version and date, or the
  experiment is unrepeatable by construction (`cikm-reproducibility`).

## Design vignette

A paper claims: entity linking over enterprise wikis improves internal search. The
minimum honest program: (1) linking quality vs. TAGME-line baselines on a public
corpus, with significance; (2) end-to-end search quality with linking on/off — same
index, same ranker; (3) an ablation degrading link precision synthetically to show
the dependence; (4) one messy-data run (stale pages, duplicate entities) with the
failure modes described. Four experiments, each answering a different lane.

## Budgeting the program against the May gate

Experiment programs at this venue fail by sequencing more than by design. Order of
execution when time is short: (1) the decisive ablation — it defines whether there
is a paper; (2) the headline comparison with proper baselines and variance — it
defines how strong; (3) one lane-coverage run for whichever community the claim
still leaves unserved; (4) robustness/messy-data sweeps; (5) everything else. Cut
from the bottom, never from the top. And freeze the protocol (splits, metrics,
tuning budgets) *in writing* before results exist — protocol decisions made after
seeing numbers are the reproducibility crisis's origin story, and the blended
panel includes people who ask when the protocol was fixed.

## Output format

```text
[Contract table] <claim → lane → evidence → status>
[Decisive ablation] <what is removed, what stays fixed>
[Panel coverage] <which lane still has no dataset/evidence speaking to it>
[Reporting floor] <captions/protocol/artifact items missing>
[Next run] <the single experiment to schedule first>
```
