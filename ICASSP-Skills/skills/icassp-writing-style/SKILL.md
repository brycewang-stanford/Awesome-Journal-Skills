---
name: icassp-writing-style
description: Use when revising an ICASSP paper into the IEEE two-column four-page house style — leading with the signal-processing contribution and mechanism, naming the task-matched metric on the first page, compressing method and results into 4+1 pages without a reviewed appendix, and writing math-forward claims that survive a subfield-expert reviewer.
---

# ICASSP Writing Style

Use this when revising the main paper. An ICASSP paper is a **four-page IEEE two-column object**
that must state a precise signal-processing contribution, show its mechanism, and prove it with a
task-matched number — all where a busy subfield reviewer will see it. There is no reviewed
appendix to rescue a buried argument.

## Revision rules

- Put the **signal-processing contribution and its mechanism** on the first page: the problem, why
  current methods break, what block of the signal chain you change, and the metric that proves it.
- Name the **task-matched metric** early (WER, SI-SDR, EER, PSNR, BER, RMSE — whatever the task
  uses), not a generic "accuracy" or "performance."
- Make the method **redrawable**: a reader should be able to reconstruct the block diagram or the
  estimator from the text alone.
- Use the four content pages for the core argument; push extended derivations and extra conditions
  to a cited technical report, since ICASSP has no reviewed supplement.
- Do not overclaim beyond the conditions tested; state the operating point (SNR, corpus, scene).

## First-page arc

1. **Problem** — the signal task, in its own vocabulary.
2. **Gap** — why the standard method fails, with a specific named reason per prior line.
3. **Mechanism** — the one thing you change, stated concretely.
4. **Measurement** — the task-matched metric and where it improves.
5. **Why SPS cares** — the community relevance, in one sentence.

## Compression discipline for four pages

- One claim per paper; a four-page paper that hedges between two contributions lands neither.
- Every figure must earn its column-inches; a plot that does not change a decision is a paragraph
  you could have kept.
- Define notation once; two-column measure punishes redundant redefinition.
- Keep a one-line derivation sketch in the body for any result whose full proof lives off-paper.

## Sentence-level rewrites

| Draft pattern | ICASSP-safe rewrite |
|---|---|
| "Our method significantly outperforms prior work." | "reduces WER from A to B on <corpus>/<split>, mean over N runs" |
| "We use a deep neural network to..." | "We replace the <specific block> with <specific mechanism>, keeping <the rest>" |
| "Excellent results across settings." | Claim scoped to the SNR range and corpus actually tested |
| "State-of-the-art performance." | "matches/beats <named strong baseline> under <stated condition>" |
| "It is well known that..." | Cite the specific prior result you rely on |

## Math-forward, but honest

- State the signal and noise model before the estimator; a signal reviewer reads the model first.
- Keep problem-dependent constants and operating points visible rather than absorbed into vague
  "under mild conditions" language.
- Separate proved statements from empirically observed ones; mixing them in one paragraph reads as
  a credibility leak to an expert reviewer.

## Vignette: compressing into four pages

A draft with two methods, seven figures, and a long related-work section: keep the single stronger
contribution, its mechanism, and the two decision-critical figures (the metric-vs-condition curve
and the ablation); compress related work into explicit contrasts; move the second method and the
extra conditions to a cited report. The test of a good cut: a subfield reviewer can reconstruct the
whole argument without leaving the four pages.

## Revision stub

```text
[Writing diagnosis] clear / mechanism-hidden / overclaimed / overloaded
[First-page fix] <problem -> gap -> mechanism -> metric on page one>
[Metric fit] task-matched metric named early? yes/no
[Claim discipline] <claim -> figure/table/derivation, operating point stated>
[Compression cuts] <what moves off-paper to the cited report>
```

## Output format

```text
[Diagnosis] <one-line house-style verdict>
[Contribution sentence] <one signal-processing claim with its metric>
[Cuts] <move/merge/delete to fit 4+1>
[Overclaim risks] <phrases scoped to tested conditions>
```
