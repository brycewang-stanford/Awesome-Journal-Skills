---
name: interspeech-experiments
description: Use when designing or auditing the experimental evidence for an INTERSPEECH paper — task-correct metrics (WER/CER, MOS/CMOS, EER/minDCF, PESQ/STOI), baselines reviewers accept, significance testing over utterances and seeds, condition coverage across speakers/noise/languages, and data hygiene for speech corpora.
---

# INTERSPEECH Experiments

"Not convincing" is the standard Interspeech rejection, and it almost always means
the experimental design — not the idea — failed. Speech evaluation has decades of
conventions per task; an experiment section that ignores them is illegible to the
reviewer pool regardless of how good the numbers are.

## Metric-task law

| Task family | Primary metrics | Convention notes |
|---|---|---|
| ASR | WER / CER | normalization + scorer disclosed; CER for unsegmented scripts |
| TTS / VC | MOS, CMOS (+ objective proxies) | panel protocol reported; CMOS for close systems |
| Speaker verification | EER, minDCF | official trial lists; DCF prior/costs stated |
| Diarization | DER / JER | collar and overlap handling stated |
| Enhancement / separation | PESQ, STOI/ESTOI, SI-SDR (+ DNSMOS-style proxies) | wideband vs narrowband named |
| SLU / speech translation | intent acc / F1, BLEU/COMET on ASR output | cascaded vs end-to-end made explicit |
| Paralinguistics / health | UAR, F1 | speaker-disjoint splits are mandatory |

Using a proxy where the community expects the primary (e.g., only neural MOS
predictors for a TTS claim) needs an explicit defense sentence.

## Baselines that count

- The **stock recipe** of a public toolkit on the same corpus (an ESPnet/
  SpeechBrain recipe number is a shared, checkable baseline).
- The **latest challenge baseline** if your task has a running challenge —
  reviewers know those numbers by heart.
- Your method's **ablated self** — at Interspeech, one clean ablation of the
  single proposed component often persuades more than two extra datasets.
- Reimplemented prior work must be validated: show your reimplementation matches
  its published number before showing you beat it.

## Significance: over what randomness?

State which variation your statistics cover — the two are routinely conflated:

- **Test-set variation**: bootstrap over utterances (or speakers, if claims are
  speaker-level) → CI on the metric difference between systems.
- **Training variation**: multiple seeds → mean ± sd; a 0.2 WER gain with sd 0.3
  across seeds is not a result.
- Matched-pairs tests (paired bootstrap; the classic MAPSSWE-style segment test
  for ASR) for A-vs-B claims on the same test set.
- Subjective scores: CIs over raters *and* stimuli; ±0.1 MOS is panel noise
  under most protocols (see `interspeech-reproducibility`).

## Condition coverage — the speech-specific axis

A speech claim is implicitly quantified over speakers, acoustic conditions, and
often languages. Reviewers probe the quantifier:

- **Speaker-disjointness**: train/test speaker overlap invalidates verification,
  paralinguistic, and health claims outright.
- **Condition breakdown**: report clean vs noisy, near- vs far-field, read vs
  spontaneous where the corpus offers them — an average hides the regression your
  method causes in one condition.
- **Language scope**: "multilingual" needs a per-language table; English-only
  results support English-only claims.
- **Domain leakage**: SSL pretraining data overlapping the test corpus (the
  LibriSpeech-descendant problem) must be checked and stated for foundation-model
  work.

## Data hygiene

- Official partitions only, or published manifests for custom splits.
- No tuning on test: LM weights, thresholds, and checkpoint selection all happen
  on dev — say so in one line.
- License and consent status of every corpus stated (see
  `interspeech-artifact-evaluation`); leaked or scraped audio can sink an
  otherwise strong paper on ethics review.

## Designing inside 4 pages

Budget roughly one column for the decisive comparison, half for ablation, half for
analysis. The analysis half is what separates accepted Interspeech papers: one
error-pattern finding (where the gains live — short utterances, overlapping
speech, a phone class) converts a benchmark delta into a scientific statement.

## Worked micro-example: is 4.9 vs 5.6 WER real?

```text
Claim: proposed 4.9% vs baseline 5.6% WER on test-other (2939 utts).
1. Paired per-utterance errors → paired bootstrap, 1000 resamples.
2. Δ WER 95% CI: [-0.9, -0.5] — excludes 0 → test-set variation covered.
3. Across 3 seeds: 4.9, 5.0, 4.8 (sd 0.1) vs 5.6, 5.7, 5.6 (sd 0.06)
   → training variation does not swallow the gap.
4. Report: "−0.7 abs. WER (95% CI [−0.9, −0.5], paired bootstrap;
   consistent across 3 seeds)."
```

Two randomness sources, two checks, one sentence in the paper. If step 2's CI
had straddled zero, the honest paper reports the trend and softens the verb —
and usually survives review better than the inflated version.

## Negative results and regressions

Interspeech's mixed jury respects a disclosed regression far more than a
suspicious clean sweep. If the method loses on clean speech while winning on
noisy, print both numbers and make the trade-off the story — condition-dependent
behavior is a *finding* in a field about acoustic variability, and hiding it is
the reviewer-trust equivalent of a failed significance test.

## Pre-submission experiment audit

```text
[ ] Primary metric matches task convention; ruler disclosed
[ ] Baseline set includes a public-recipe or challenge anchor
[ ] Each A>B claim carries a CI or matched-pairs test
[ ] Seeds: n stated; variance reported or single-run admitted
[ ] Speaker-disjoint splits verified where required
[ ] Condition/language breakdown present; regressions named
[ ] Dev-only tuning stated; test touched once
[ ] One analysis finding, not just deltas
```

## Output format

```text
[Claim inventory] each claim → metric → evidence status
[Metric-law check] conventions met / violations
[Baseline verdict] anchored / self-referential / stale
[Statistics] randomness covered (test-set / seeds / raters) per claim
[Coverage gaps] speaker / condition / language / leakage
[Cheapest decisive fix] <one experiment that most raises conviction>
```

Metric conventions are community law rather than CFP text and move slowly, but
challenge editions and recipe baselines roll every year — re-anchor at design
time (sources logged in `resources/official-source-map.md`, 2026-07-08).
