---
name: icassp-reproducibility
description: Use when strengthening ICASSP reproducibility across signal-processing modalities — pinning the scoring ruler for the paper's metric, dataset versions and splits, front-end/DSP settings, seeds, and compute, and mapping each claim to a checkable location, since ICASSP has no reviewed appendix and the four pages plus a public release must carry it.
---

# ICASSP Reproducibility

Use this before submission and again before camera-ready. ICASSP has **no reviewed supplement**,
so reproducibility rests on what the four pages state plus whatever you release publicly (which,
under single-blind review, may be public immediately). The recurring ICASSP failure is not a
missing repository — it is a **number whose measurement cannot be reconstructed**.

## The evidence spine

Map each claim — an algorithm result, a theoretical bound, or an empirical metric — to a
checkable location in the paper or the released package:

- For an empirical result: dataset and version, split or trial list, front-end/DSP settings,
  model, the **exact scorer and its configuration**, seeds, number of runs, and reported spread.
- For an estimation/detection result: the signal and noise model, the estimator, and the
  reference bound (e.g., Cramér-Rao) the result is compared against.
- For a real-time or embedded claim: hardware, latency or real-time factor, and memory.
- Explain any data you cannot release honestly, and describe how a reader could reproduce from
  the licensed source.

## The scoring ruler is the thing that decays

Across ICASSP's modalities, the same trap recurs: the metric name is stated but the **ruler**
behind it is not, so the number is unreproducible.

| Modality | Metric | The ruler that must be pinned |
|---|---|---|
| Speech recognition | WER / CER | Text normalization, scoring tool, reference edition |
| Enhancement / separation | SI-SDR, PESQ, STOI | Reference alignment, permutation policy, mode/wideband setting |
| Speaker / biometrics | EER, minDCF | Trial list, score normalization, DCF operating point |
| Image / video restoration | PSNR, SSIM | Border handling, bit depth, color space, crop |
| Communications | BER / BLER | SNR definition, channel model, decoder settings |
| Estimation | RMSE / MSE | SNR range, trial count, and the bound compared to |

Ship the ruler, not just the model: a released checkpoint with no scorer configuration cannot
reproduce the headline metric.

## Front-end determinism

Signal papers decay silently through the front end. Pin the sample rate, framing, window
function, FFT size, feature type, and any resampling. A change from a 25 ms to a 20 ms window, or
a resampler swap, moves every downstream number without touching the model — and reviewers who
reproduce will notice.

## Degrees of reproducibility

- **Turnkey** — one command regenerates each reported metric from released outputs and seeds.
- **Scripted** — scripts exist but need documented manual steps or licensed-data access.
- **Descriptive** — prose detailed enough that a competent engineer could rebuild the pipeline.

For ICASSP, make the **scoring path** turnkey even when full training stays scripted; reviewers
rerun scorers, not trainings. Stating the achieved level honestly beats promising turnkey
behavior that fails on a clean machine.

## Reproducibility stub

```bash
# Pin the environment and the ruler; regenerate the headline number.
pip install -r requirements.txt          # exact versions, including the DSP/feature lib
python3 run_eval.py --config configs/main.yaml --seed 1
python3 run_eval.py --config configs/main.yaml --seed 2
python3 run_eval.py --config configs/main.yaml --seed 3
python3 aggregate.py --runs runs/ --report mean_std   # matches Table 1 mean ± spread
```

## Vignette: a keyword-spotting paper

A submission reports detection accuracy for a small-footprint keyword spotter. Its reproducibility
spine: the corpus version and split, the feature front-end (sample rate, mel bins, window), the
decision threshold and how it was set, seeds and run count, the on-device latency, and the exact
scorer for the false-alarm/false-reject operating point — plus one honest sentence on the
condition it was not evaluated under (e.g., far-field noise).

## Output format

```text
[Claim inventory] <claim -> checkable location>
[Scoring ruler] pinned / partial / missing
[Front-end] sample rate / framing / features pinned?
[Randomness] seeds + run count + reported spread
[Reproducibility level] turnkey / scripted / descriptive
[Fixes] <what must appear in the 4 pages vs the released package>
```
