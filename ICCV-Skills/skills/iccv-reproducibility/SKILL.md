---
name: iccv-reproducibility
description: Use when hardening the reproducibility story of an ICCV paper, covering full recipe disclosure without a mandated compute form, protocol pinning for foundation-model and zero-shot evaluations, seed and variance honesty at vision training scale, and writing results that stay checkable across the two-year gap to the next ICCV.
---

# ICCV Reproducibility

ICCV 2025 imposed no compute-reporting form and no reproducibility checklist that
could be verified at check time (2026-07-08) — which means the venue's
reproducibility bar is enforced socially: by reviewers who re-implement things
for a living, and by a two-year horizon in which your paper is the standing
reference until the next ICCV. Absent a form, the paper itself must carry the
full disclosure. This skill is the audit.

## The two-year checkability test

A CVPR paper gets superseded in twelve months; an ICCV paper's numbers get
re-quoted, re-run, and re-attacked for at least twenty-four. Write every result
so that a stranger in the *next* odd year can adjudicate a discrepancy:

- Dataset **version and split files** named (not "standard split" — the standard
  moves), with checksums where licenses allow.
- Metric **implementation** cited by repo and version; identically named metrics
  differ across codebases by more than typical paper deltas.
- Pretraining **corpus and checkpoint** identified for every initialization; a
  gain that rides an undisclosed web-scale pretrain is a different claim than
  the paper makes.
- Evaluation resolution, crop policy, and test-time augmentation stated per
  table, since these silently absorb whole points.

## Foundation-model era: pin the protocol, not just the seed

Much post-2023 ICCV work evaluates *around* large pretrained models, which adds
reproducibility failure modes that classical training-recipe disclosure never
covered:

| Moving part | What to pin in the paper |
|---|---|
| Backbone / VLM checkpoint | Exact identifier and revision hash, not the family name |
| Prompts and templates | Verbatim, in the supplement, including the ensemble if any |
| API-served models (if unavoidable) | Access dates + version string; state that decommissioning breaks exact reproduction |
| Zero-shot class lists / vocabularies | The literal list, since "the standard 80 classes" has variants |
| Retrieval corpora / support sets | Snapshot date and filtering rules |

A "zero-shot" table whose prompt engineering is unstated is not zero-anything;
reviewers at ICCV increasingly ask.

## Recipe as a build artifact

Maintain one machine-readable record per reported row, from the first
experiment, and *generate* the implementation section from it rather than
reconstructing memories in deadline week:

```toml
# ledger/tab2_row5.toml — the row is reproducible iff this file is complete
model      = "ours-large"
init       = "vitl14-<hash>, corpus: <name+version>"
data       = { train = "co3d-v2@sha256:...", eval = "co3d-v2-test-list.txt" }
schedule   = { optim = "adamw", lr = 3e-4, epochs = 60, batch = 512, warmup = 5 }
aug        = ["rrc-336", "hflip"]
seeds      = [0, 1, 2]            # or [0] with flagged=true
hardware   = "16xA100-40G, bf16"
eval       = { resolution = 336, tta = false, metric_impl = "<repo>@<tag>" }
command    = "python train.py -c configs/tab2_row5.toml"
```

The ledger also answers rebuttal-week questions in minutes ("which schedule made
Fig. 5?") — at ICCV those questions arrive in a seven-day window in May.

## Variance honesty at vision budgets

Nobody multi-seeds a 16-GPU week ten times, and pretending otherwise persuades
no one. The defensible pattern, stated in the paper's own words: cheap decisive
experiments (the headline ablation, the small-backbone variant) run with ≥3
seeds and reported as mean ± std; the flagship run flagged explicitly as single;
and no claim in the abstract resting on a margin smaller than the seed noise
visible in your own tables. For stochastic *evaluation* (generation, sampling-
based detection), repeat the evaluation pass and report its spread separately
from training variance — the two get conflated constantly.

## Compute disclosure without a form

No mandated form means you choose the disclosure, and the cheap honest version
is one paragraph: total GPU-hours for the flagship, per-experiment cost for the
grid, hardware and precision, and wall-clock per training run. Two reasons to
volunteer it. Reviewers calibrate "simple and effective" claims against what the
method costs to obtain; and any efficiency or "real-time" adjective in your
abstract is unfalsifiable without named hardware — an easy weakness for a
reviewer to poke in a cycle where you get one page of rebuttal to answer.

## Withheld test sets and server etiquette

Benchmarks with evaluation servers turn your test number into a receipt rather
than a rerunnable command. Record submission IDs and dates in the ledger, stay
inside per-week submission budgets (tuning on the server is the field's
canonical sin and organizers publish shame lists), and always give readers the
validation-set protocol whose numbers predict the server's — that is what they
will actually reproduce.

## Determinism paragraph, written once

State the posture instead of implying perfection: which RNGs were seeded, whether
deterministic kernels were enabled (and the throughput cost if not), known
nondeterminism sources (scatter atomics, multi-GPU reduction order, dataloader
scheduling), and the reproduction tolerance you measured across identical-seed
reruns. One measured tolerance sentence ("±0.15 mIoU across nodes") converts
future "failed to reproduce" issues into calibration checks.

## Reverify each cycle

- Whether 2027 introduces any reproducibility checklist, compute form, or
  code-submission expectation (none verified for 2025).
- Benchmark version churn since the last cycle — two years is long in dataset
  time (`iccv-experiments` covers the drift audit).
- Current supplement constraints that bound how much recipe detail ships.

## Output format

```text
[Checkability grade] two-year test: pass / gaps
[Ledger coverage] rows with complete recipes: n/m
[Foundation-model pins] checkpoints · prompts · vocabularies · API versions: pinned?
[Variance] multi-seeded: <list>; flagged single runs: <list>; claims vs noise: OK?
[Compute paragraph] present with hardware + GPU-hours: yes/no
[Fix list] <ordered by what a re-implementer hits first>
```
