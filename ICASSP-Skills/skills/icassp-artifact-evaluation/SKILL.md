---
name: icassp-artifact-evaluation
description: Use when packaging ICASSP code, data, audio or image samples, model checkpoints, scoring scripts, seeds, and logs, even though ICASSP has no formal artifact badge. Covers what signal-processing reviewers actually open, how single-blind review lets artifacts be public from the start, and how to make a task's measurement reproducible turnkey.
---

# ICASSP Artifact Evaluation

Use this for evidence packaging around ICASSP. There is **no formal artifact-evaluation
committee or badge** at ICASSP as of the 2026 cycle; artifacts are voluntary and their value is
in review credibility and post-publication impact. Because review is **single-blind**, a
repository can carry your name from day one — no anonymous mirror is required.

## Artifact plan

- Decide what evidence supports the four-page claim: training and evaluation code, the exact
  dataset splits or trial lists, the **scoring script**, model checkpoints, seeds, logs, and a
  handful of qualitative samples (audio, spectrogram, image, or signal plot).
- Keep the decision-critical numbers reproducible from the released package; a reviewer who
  cannot regenerate the headline metric discounts it.
- Ship a **minimal reproduction map**: environment, dependencies, hardware, commands, expected
  outputs, runtime, seeds, and any known nondeterminism (GPU kernels, thread counts).
- For restricted corpora you cannot redistribute, provide enough provenance and preprocessing to
  reproduce from the licensed source without violating the data-use terms.
- Because links can be public, put the repository URL in the paper and test it from a logged-out
  browser before submission.

## What ICASSP evidence reviewers open first

| Claim type | First artifact inspected | Common failure caught |
|---|---|---|
| Recognition/detection accuracy | Scoring script + dataset split | WER/error computed with an undocumented text-normalization or split |
| Enhancement / separation gain | Reference-aligned SI-SDR/PESQ/STOI scorer | Metric computed with mismatched reference or windowing |
| Speaker / biometric verification | Trial list + EER/minDCF scorer | Non-standard trials that inflate the score |
| Image/signal restoration | PSNR/SSIM script + test set | Metric on a different crop, bit depth, or borders |
| Real-time claim | Latency/RTF measurement harness | Feasibility asserted, never measured |

Signal-processing reviewers will **rerun a scorer on a provided output far more readily than they
will retrain a model**, so make the measurement path turnkey before polishing training code.

## Worked vignette: packaging a separation result

A hypothetical submission reports source-separation gain on a two-speaker mixture set.

- Ship the **mixture generation** as one parameterized script (seed, SNR range, corpus source),
  not as constants buried in a notebook, so a reviewer can regenerate the exact test mixtures.
- Include the **reference-aligned SI-SDR scorer** with its settings; separation numbers are
  meaningless if the alignment and permutation handling differ.
- Emit result tables directly from logged outputs so the paper's numbers and the artifact's
  numbers cannot drift apart.
- Provide five listenable example mixtures with their separated outputs; a reviewer often judges
  perceptual quality from these before reading the metric table.

## Turnkey scoring stub

```bash
# One command should reproduce the headline metric from released outputs.
python3 score.py \
  --hyp outputs/dev.hyp \
  --ref data/dev.ref \
  --metric si-sdr \
  --config configs/scoring.yaml   # window, alignment, permutation policy pinned here
# Expected: dev SI-SDR = <value in Table 1> (mean over 3 seeds)
```

## Calibration anchors

- Assume only the README and one entry script get opened; design the package so the top-level
  README reproduces the main number in one command.
- Do not confuse a released toolkit with an artifact: ICASSP reviewers want the exact recipe that
  produced *this paper's* numbers, not a general library dump.
- Formats and sizes for any uploaded supplementary media are cycle-specific; verify against the
  current paper kit rather than past years.

## Output format

```text
[Artifact role] public release / demo samples / scoring package
[Contents] code / data-split / scorer / checkpoints / seeds / samples
[Reproduction level] turnkey / scripted / descriptive / weak
[Measurement risks] metric ruler / split / alignment / normalization
[Fixes before release] <ordered list>
```
