# ICASSP Reproducibility Code Adapter

ICASSP does not run an artifact-evaluation track, so there is no badge to earn and no reviewer
obligation to rerun your code. The payoff of a clean package is different here: it makes the
four-page claim **credible on inspection** and lets the work outlive the conference. This
directory points to the repository-wide reproducibility kit and then lists the measurement checks
that are specific to signal-processing papers — the parts a generic structural check cannot see.
It is not a DSP toolbox and not an econometrics kit; your recipes belong in an ESPnet, SpeechBrain,
Asteroid, or PyTorch project, not here.

## Repository-wide kit (reused, not duplicated)

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

Run the structural checker on a package that, under ICASSP's single-blind policy, can already
carry your name:

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/release
```

A pass tells you the package is well-formed. It says nothing about whether the numbers are right;
that is what the checks below are for.

## Signal-processing measurement checks (do these by hand)

The structural checker looks at layout; an ICASSP result stands or falls on the **measurement**.
Cross-reference each item against
[`../../skills/icassp-reproducibility/SKILL.md`](../../skills/icassp-reproducibility/SKILL.md) and
[`../../skills/icassp-experiments/SKILL.md`](../../skills/icassp-experiments/SKILL.md):

- **The metric's ruler is in the box.** Whatever decides the paper — WER, SI-SDR, PESQ/STOI,
  EER/minDCF, PSNR/SSIM, BER, RMSE — ships with the exact scorer and its configuration, not just a
  reported figure.
- **The signal front end is pinned.** Sample rate, framing, window, FFT size, feature extraction,
  and any resampling are fixed; a silent front-end change moves every downstream number.
- **The data slice is exact.** Corpus release and the precise split or trial list are named or
  included, so the number is computed on the same signal set a reviewer would use.
- **Randomness is bounded.** Seeds for initialization, data order, and augmentation are set, and
  the report states how many runs the mean and spread summarize.
- **Cost is measured, not asserted.** Hardware and training time are logged, and any real-time
  claim carries an actual latency or real-time-factor measurement.

Venue policy always comes from the live official pages
([`../official-source-map.md`](../official-source-map.md) records the 2026-07-09 trail); this
adapter never substitutes for the current paper kit.
