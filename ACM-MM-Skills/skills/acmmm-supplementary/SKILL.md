---
name: acmmm-supplementary
description: Use when organizing the ACM MM (ACM Multimedia) supplementary material due after the paper deadline — deciding what belongs in the 6-8 page body versus the supplement, packaging video/audio/interactive demos that render on a reviewer's machine, keeping all assets anonymous for double-blind tracks, and pointing to code and data.
---

# ACM MM Supplementary Material

Use this to plan the ACM Multimedia supplement, which has its **own deadline after the paper**
(in 2026, April 8 versus the April 1 paper deadline). For a multimedia paper the supplement is
not an afterthought — it is where the video, audio, and interactive evidence lives.

## Body vs. supplement split

The 6–8 page sigconf body carries the argument; the supplement carries what the argument rests
on but cannot fit.

| Content | Body | Supplement |
|---|---|---|
| Core claim, main results table, teaser | Yes | — |
| The two or three decisive media examples | Yes (stills/short) | Full clips |
| Extra qualitative media across conditions | — | Yes |
| Full user-study protocol and per-rater data | Summary only | Yes |
| Hyperparameters, extra ablations, proofs | Pointer only | Yes |
| Code / data pointers | Named | Yes |

A reviewer must be able to follow the body **without** the supplement; the supplement then
*confirms* rather than *completes* the argument.

## Packaging media that actually plays

The single most common ACM MM supplement failure is media a reviewer cannot open.

```text
video:  H.264/MP4, standard resolution, plays in a browser/VLC; no exotic codec
audio:  WAV or MP3; label each clip with the claim it supports
demo:   if interactive, provide a recorded fallback video — do not assume the reviewer runs it
size:   keep within the cycle's stated limit; compress rather than omit evidence
index:  a short README mapping each file to the paper claim/figure it supports
```

## Anonymity for double-blind tracks

- Strip author names from filenames, EXIF/media metadata, and any on-screen watermark or slate.
- Remove identifying voices/faces of the authors from demo videos where they would reveal
  identity, or note that they are incidental.
- Route dataset and code links through an **anonymous mirror**; a personal or lab URL is a leak.
- The Reproducibility, Open Source Software, and Dataset tracks are single-blind and do not need
  this — but the main track and Brave New Ideas do.

## Make the supplement legible

- Open with a one-paragraph README: what is here, and which paper claim each file supports.
- Order files to follow the paper's sections, not upload order.
- Caption every clip; an unlabeled video is not evidence a reviewer can use.

## What reviewers actually open

Reviewers are time-pressed and will not download a 2 GB archive or install a codec. Design for a
skim:

- Lead the index with the **two or three clips that decide the paper**, labeled by claim.
- Keep individual files small enough to stream; compress rather than omit.
- Never make the argument depend on a file the reviewer has to run or build — provide a recorded
  fallback for any interactive demo.

## Format and codec table

| Asset | Safe choice | Avoid |
|---|---|---|
| Video | H.264/MP4, standard resolution | Exotic/proprietary codecs, 4K walls of clips |
| Audio | WAV or MP3, labeled | Unlabeled waveforms, lossless dumps for size's sake |
| Interactive demo | Recorded MP4 fallback + optional code | Assuming the reviewer runs your app |
| Appendix | PDF, same template family | A zip of loose screenshots |

## Timing against the paper deadline

The supplement has its own, later deadline (April 8 vs. April 1 in 2026), which is a chance and a
trap: do not defer *all* media to that week, because rendering, compressing, and anonymizing a
video library takes longer than expected. Freeze the decisive clips with the paper, and use the
extra days for the confirmatory extras, not the core evidence.

## Pre-submission checklist

- Every media file opens with common open-source players.
- The index maps each file to a specific figure, table, or claim.
- No author identity in any filename, metadata, watermark, or link (double-blind tracks).
- The body still stands alone if the supplement were removed.
- Total size is within the current cycle's stated cap (待核实 each year).

## Output format

```text
[Split] body self-contained / body depends on supplement
[Media playability] all files open / risky: <list>
[Anonymity] clean / leaks: <list>
[Index] each file mapped to a claim / unlabeled: <list>
[Size] within cap / over
[Top fixes] <ordered before the supplement deadline>
```
