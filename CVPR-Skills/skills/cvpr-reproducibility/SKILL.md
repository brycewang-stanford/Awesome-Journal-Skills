---
name: cvpr-reproducibility
description: Use when hardening a CVPR paper's reproducibility story, covering the Compute Reporting Form's hardware and compute sections, training-recipe disclosure, benchmark protocol and split hygiene, seed and variance reporting for vision experiments, and closing the gaps reviewers probe at a benchmark-driven venue.
---

# CVPR Reproducibility

At CVPR, reproducibility failures rarely look like fraud; they look like a table nobody
can match because one augmentation flag, one crop size, or one pretraining corpus went
unstated. This skill hardens the paper against that fate, anchored in the 2026-cycle
machinery (checked 2026-07-08): the Compute Reporting Form, the anonymous supplement,
and reviewers trained on a decade of un-reproducible state-of-the-art claims.

## The CRF as a reproducibility floor

The 2026 cycle attached a Compute Reporting Form to every submission — Section 1
(hardware specification) and Section 5 (verification) mandatory, deeper sections
optional, with an explicit opt-out route for proprietary constraints. Treat the
mandatory floor as the start, not the ceiling:

| CRF layer | What it pins down | Why reviewers care |
|---|---|---|
| Hardware (mandatory) | GPU model, count, primary configuration | Grounds every "real-time" and "efficient" claim |
| Verification (mandatory) | Author attestation | Somebody owns the numbers |
| Task/compute (optional) | GPU-hours or FLOPs per result | Separates a 4-GPU method from a 512-GPU method |
| Full logs (optional) | Run-level records | The strongest possible "we actually ran this" |

If your contribution *is* efficiency, filling only the mandatory sections undercuts your
own claim — report the compute and let the numbers argue.

## The recipe ledger

Vision results are recipe-sensitive. Maintain one machine-readable ledger from the first
experiment, and generate the paper's implementation-details paragraph *from it* instead
of reconstructing details in deadline week:

```yaml
# recipe-ledger.yaml — one block per reported table row
table3_row2:
  backbone: vit-b16, pretrain: <corpus + checkpoint hash>
  data: <dataset version + split file sha256>
  aug: [rrc-224, hflip, randaug-m9]
  optim: adamw, lr: 1.0e-4, sched: cosine, epochs: 90, batch: 1024
  seed: 3407          # and whether cudnn deterministic was set
  hardware: 8xA100-80G   # must agree with CRF Section 1
  command: scripts/train.sh configs/table3_row2.yaml
```

The ledger's second job is internal: when a reviewer asks in January which schedule
produced Figure 5, you answer from the file in minutes.

## Benchmark hygiene that survives scrutiny

- **Split discipline.** Name the exact split files; never tune on anything downstream of
  the test set — including "just checking" runs that leak into architecture choices.
- **Test-set frequency.** State how many times the test set was evaluated. Val-set
  ablations + one final test run is the defensible pattern.
- **Metric provenance.** Cite the metric implementation (which mAP variant? whose FID
  code, which feature extractor?). Same-name metrics differ across repos by whole
  points.
- **Pretraining disclosure.** "Initialized from X" changes the comparison class; a
  method beating from-scratch baselines while riding a web-scale pretrain is a
  different claim.
- **Baseline re-runs.** Say which baseline numbers are quoted from papers versus re-run
  under your protocol, and match backbones and schedules when you re-run.

## Variance at vision scale

Full multi-seed grids are often unaffordable at modern training budgets, and reviewers
know it. The credible middle ground: multi-seed the cheap decisive experiments (small
backbone, headline ablation) and report mean ± std; run the flagship once but state so
explicitly; never present a 0.2-point gain as a finding when the same table shows
seed-level noise of 0.4. If evaluation itself is stochastic (generation, sampling-based
detection), repeat evaluation, not just training.

## Determinism knobs, documented once

Bit-exact reproduction is often impossible on GPU stacks, but *stating your
determinism posture* is always possible and costs three lines in the supplement:

- Which seeds were fixed (Python/NumPy/framework/dataloader workers) and whether
  deterministic kernels were enabled — note the speed cost if they were not.
- Sources of accepted nondeterminism: atomics in scatter ops, multi-GPU reduction
  order, augmentation pipelines keyed to worker scheduling.
- The reproduction tolerance you actually observed: "re-running row 2 varies by
  ±0.15 mAP across identical-seed runs on different node counts" tells a reproducer
  whether their 0.1-point discrepancy is a bug or physics.

Teams that measure this once, early, stop having the "is 78.4 vs 78.6 a failure to
reproduce?" argument — with reviewers and with themselves.

## Statement-level honesty

Reproducibility text is a claims surface. "Code will be released" is a promise the
community tracks; "results reproducible from the supplement" is checkable in January.
Write the availability paragraph to match what is genuinely packaged: what ships in the
supplement now, what is released at camera-ready (datasets claimed as contributions
**must** be public by then — verified 2026 policy), and what cannot be released and why.

## Held-out evaluation servers

Several vision benchmarks score on withheld test sets via submission servers with
rate limits. This changes reproducibility mechanics: your reported test number is a
server receipt, not a rerunnable command. Record the submission ID and date in the
recipe ledger, respect per-week submission caps as an ethics matter (burning entries
to tune on test is the community's canonical sin), and give reproducers the exact
validation-set protocol that predicts the server number.

## Reverify each cycle

- CRF structure, which sections are mandatory, and award tie-ins.
- Any reproducibility checklist added to the OpenReview form.
- Supplement caps that constrain how much recipe/code detail ships at review time
  (2026 caps 待核实).

## Output format

```text
[Repro grade] recipe-complete / gaps found
[CRF] hardware row consistent with paper claims: yes/no; optional sections: <filled?>
[Ledger] rows covering all reported tables: <n/m>
[Benchmark hygiene] splits · test-set count · metric provenance · pretrain disclosure
[Variance] multi-seeded: <experiments>; single-run flagged: <experiments>
[Fix list] <ordered, highest reviewer-visibility first>
```
