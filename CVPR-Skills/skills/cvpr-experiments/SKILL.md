---
name: cvpr-experiments
description: Use when designing or auditing the experimental program of a CVPR paper, covering benchmark and baseline selection under matched-compute fairness, the ablation study reviewers treat as mandatory, qualitative and failure-case evidence, efficiency metrics tied to the Compute Reporting Form, and generalization tests beyond a single dataset.
---

# CVPR Experiments

CVPR runs on benchmark evidence: reviewers at the 2026 edition sorted 16,092 submissions
largely by asking "do the tables prove the sentence?" This skill designs an experimental
program that answers the four questions every vision review implicitly asks — does it
work, why does it work, when does it fail, and what does it cost.

## Does it work: main comparisons

- **Benchmarks**: use the datasets your subfield's last two cycles used, current
  versions, standard splits. A new task may justify a new benchmark, but then the
  benchmark itself becomes a contribution needing validation (and, if claimed as one,
  public release by camera-ready — verified 2026 policy).
- **Baselines**: the leaderboard's current top methods plus the strongest *simple*
  baseline. The comparison that kills papers in review is the one you omitted because
  it was too strong.
- **Fairness**: match backbones, pretraining corpora, input resolution, and training
  schedule wherever possible — or tabulate the mismatch explicitly. Beating a
  ResNet-era method with a ViT-L and calling it method innovation is the single most
  common CVPR review objection.
- **Provenance**: mark which numbers are re-runs under your protocol vs. quoted from
  papers; asterisk and footnote the re-runs.

## Why it works: the ablation is not optional

Vision reviewers treat ablations as the paper's proof of understanding. Structure the
grid so each row removes or replaces exactly one design decision:

```text
# ablation-matrix.txt — one experiment per line, one variable per experiment
A0  full method                                  (reference row)
A1  - temporal attention  → per-frame baseline    tests the core claim
A2  - our loss   → standard L1                    is the loss or the architecture doing it?
A3  - pretrain   → from scratch                   how much rides on initialization?
A4  swap: our module in baseline X                does the gain transfer?
A5  sensitivity: key hyperparameter sweep         is A0 a lucky point?
```

Rows A4 (transplant) and A5 (sensitivity) separate memorable ablation sections from
perfunctory ones. Every ablation row cited in prose belongs in the 8-page body; the
long grid goes to the supplement.

## When it fails: qualitative evidence with integrity

Cherry-picked grids convince nobody at a venue that invented the genre. The credible
pattern:

| Qualitative element | Purpose |
|---|---|
| Random (or id-listed) sample grid | Shows typical, not best-case, behavior |
| Side-by-side vs. two strongest baselines | Same inputs, aligned crops, labeled columns |
| Failure cases with a taxonomy | "Fails under occlusion and low light" beats silence |
| Video for anything temporal | In the supplement — external links are banned |

State the selection rule in the caption ("first 8 validation images", "random seed 0").
A stated rule converts pretty pictures into evidence.

## What it costs: efficiency as a first-class axis

The 2026 cycle made compute visible venue-wide via the mandatory Compute Reporting Form
(hardware + verification sections required; deeper compute sections optional but tied
to recognition badges). Align the paper with the form: report params, FLOPs, latency
(named hardware, batch size, resolution), and training GPU-hours for your method *and*
re-run baselines where you can. "Real-time" with no hardware named contradicts your own
CRF and reviewers can now check.

## Generalization: the second-dataset rule

A method shown on one dataset is a result about that dataset. Cheap robustness
evidence reviewers reward: evaluate the trained model on a second domain without
retuning; report cross-dataset transfer; if your field has corruption/shift suites, run
them. One honest sentence about where transfer degrades is worth more than a defensive
omission — it becomes your limitations paragraph (see `cvpr-writing-style`).

## Budgeting the program before running it

At CVPR-scale training costs, experiment selection is a resource-allocation problem.
Plan the program backward from the paper's skeleton:

1. List the tables and figures the argument needs (main comparison, decisive ablation,
   efficiency table, qualitative grid, one transfer result).
2. Price each in GPU-hours using a pilot run; the totals routinely show the "nice to
   have" grid costing more than the flagship.
3. Spend on order-of-information value: the ablation that could falsify the core
   claim runs *first*, not last — discovering in October that A1 ≈ A0 should redirect
   the project, not decorate it.
4. Reserve 15–20% of budget for rebuttal week; the most common January request is a
   small matched-setting re-run, and having compute standing by converts a weakness
   into a mini-table.
5. Log everything into the recipe ledger (`cvpr-reproducibility`) as it runs; the CRF
   optional sections then fill themselves.

## Statistical care, vision edition

Multi-seed everything is unaffordable at modern budgets; the defensible pattern is
multi-seeded cheap experiments with mean ± std, a single flagged flagship run, and no
headline claims resting on differences smaller than observed seed noise (full protocol
in `cvpr-reproducibility`). For generative work, repeat *evaluation* sampling; for
detection, fix and disclose the exact mAP implementation.

## Reverify each cycle

- Standard splits and evaluation-server rules for your benchmarks (some test sets are
  withheld; see `cvpr-reproducibility` for submission-server discipline).
- CRF structure and any new compute/efficiency reporting requirements.
- Benchmark leaderboard state the month before the deadline.
- Any dataset-ethics or human-data review requirements added to the form (待核实 each
  cycle).

## Output format

```text
[Evidence audit] works / why / fails / costs — covered?
[Comparison risks] unmatched: <backbone/pretrain/resolution/schedule>
[Ablation] rows isolating single factors: <n>; transplant + sensitivity present?
[Qualitative] selection rule stated? failures taxonomized?
[Efficiency] params/FLOPs/latency/GPU-hours vs CRF: consistent?
[Priority additions] <ordered by review impact>
```
