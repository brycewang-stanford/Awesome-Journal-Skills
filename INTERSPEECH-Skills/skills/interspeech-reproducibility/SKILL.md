---
name: interspeech-reproducibility
description: Use when hardening the reproducibility of an INTERSPEECH paper — pinning corpus versions and official splits, publishing text-normalization and scoring rules that WER/EER silently depend on, documenting MOS listening-test protocols, reporting seeds and variance within 4 pages, and making toolkit recipes rerunnable.
---

# INTERSPEECH Reproducibility

Speech results decay through the *measurement*, not just the model. Two labs with
identical checkpoints can report WERs a point apart because their text
normalization differs, and two identical TTS systems can score half a MOS point
apart under different listening panels. Interspeech reviewers know this, and the
4-page format means reproducibility is asserted through precise, compressed
disclosure — there is no appendix to hide vagueness in.

## The five decay channels

| Channel | How results drift | Pin it by |
|---|---|---|
| Corpus version & splits | "test" ≠ official test; filtered utterances | Name corpus version + official partition; list any filtering rule |
| Text normalization | casing, punctuation, numerals change WER | Publish the norm script; name the scorer (e.g., sclite/jiwer + config) |
| Trial lists / protocols | EER/minDCF move with the trial set | Cite the exact trial list file and calibration set |
| Subjective testing | MOS panels differ in raters, scale, stimuli | Report rater count, platform, instructions, #stimuli, CI |
| Training stochasticity | seed, data order, nondeterministic kernels | Seeds logged; ≥3 runs where feasible; mean ± sd |

## Corpus discipline

- Name the release, not the family: "LibriSpeech test-other", "VoxCeleb1-O cleaned
  trial list", "CHiME-6 eval per the challenge rules" — each token is checkable.
- If you re-partition, justify it and publish the split manifests; private splits
  are the single most common irreproducibility at this venue.
- State licenses (see `interspeech-artifact-evaluation`); a reader must know whether
  they *can* obtain your training data.
- For multilingual claims, list the languages and hours per language — "50+
  languages" without a table row per language is not reproducible.

## Objective metrics: publish the ruler

WER is a Levenshtein distance over a normalization you chose. Reviewers who have
been burned will ask:

- Which scoring tool and version, with which options?
- What text normalization (case, punctuation, number expansion, compound rules)?
- Insertion-penalty / LM-weight tuning: on which dev set?
- For EER/minDCF: which trial list, which prior/costs in the DCF?
- For enhancement: PESQ-WB or NB? STOI or ESTOI? Which reference alignment?

One sentence in the paper plus scripts in the repo answers all of it.

## Subjective metrics: the protocol is the result

A MOS number without its protocol is decoration. The reportable minimum, fitted to
about three lines of a 4-page paper:

```text
Naturalness MOS: 5-point ACR; N=30 crowd raters (platform X), native speakers,
screened by anchor trials; 20 utterances/system, 8 systems, randomized;
95% CI via rater bootstrap. CMOS vs. baseline on the same panel.
```

If a claim rests on ±0.1 MOS, it rests on nothing — pair MOS with CMOS or an
objective proxy (e.g., a learned MOS predictor, clearly labeled as a proxy) and say
whether the panel can resolve the difference.

## Variance and seeds inside 4 pages

- Prefer one honest line — "mean ± sd over 3 seeds; CI excludes the baseline" —
  over three extra ablations without variance.
- Bootstrap CIs at the utterance level for WER; matched-pairs significance (e.g.,
  MAPSSWE-style or paired bootstrap) when claiming a system beats another.
- If compute allows only one run, say so and temper the claim's verbs accordingly.

## Recipe rerunnability

Most Interspeech systems live in community toolkits (ESPnet, SpeechBrain, Kaldi,
NeMo, k2, fairseq lineage). Reproducibility there means:

- Pin the toolkit commit and the recipe directory, not just the toolkit name.
- Diff-against-default: state which hyperparameters differ from the stock recipe —
  that diff *is* your method's footprint.
- Log the full config used for each table row; map rows to config files in the repo.
- Record hardware and wall-clock: "8×A100, 36h" tells readers whether they can
  replicate at all.

## Review-time vs camera-ready disclosure

During double-blind review the repo must be anonymized or described-but-withheld;
at camera-ready the links flip public. Write the reproducibility sentences so that
only the URL changes, not the promises.

## The disclosure block, worth three lines of the paper

A compact pattern that closes most reviewer doubts at once — adapt per task:

```text
Setup: ESPnet2 (commit abc123), LibriSpeech 960h official splits;
Whisper-normalizer text rules; WER via jiwer 3.x, config in repo.
Training: 3 seeds (mean±sd reported), 8×A100, 30h/run; decoding:
beam 10, no external LM; dev-clean used for all tuning.
```

Every clause preempts a specific review question; nothing in it costs a figure.

## Reviewer questions to preempt

- "Is the gain inside seed noise?" → variance line present.
- "Which normalization produced these WERs?" → ruler named and shipped.
- "Did any tuning touch the test set?" → dev-only sentence present.
- "Can I obtain the training data?" → corpus + license named.
- "Would the MOS panel resolve this difference?" → CI + panel size reported.

If the paper answers all five before they are asked, the reproducibility
paragraph has done its rhetorical job as well as its scientific one.

## Output format

```text
[Decay-channel audit] corpus / normalization / trials / subjective / seeds — pinned?
[Ruler published?] scoring tools + norm rules in repo: yes / partial / no
[Subjective protocol] complete per the reportable minimum? gaps
[Variance] runs, CI method, significance test used
[Recipe] toolkit+commit, config-per-row mapping, hardware line
[Weakest link] <the one channel most likely to break replication>
```

Cross-check any cycle-specific checklist or disclosure field on the live CFP —
Interspeech has been adding evaluation-rigor language cycle by cycle (sources:
`resources/official-source-map.md`, checked 2026-07-08).
