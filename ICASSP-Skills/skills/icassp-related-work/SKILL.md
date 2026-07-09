---
name: icassp-related-work
description: Use when positioning an ICASSP submission across the signal-processing literature — IEEE SPS journals (TSP, TASLP, SPL, TIP and siblings), sibling conferences (Interspeech, ICIP, EUSIPCO, WASPAA), and ML venues, citing normally under single-blind review, and sharpening the technical delta against the nearest current-cycle work in four pages.
---

# ICASSP Related Work

Use this to audit novelty and positioning. ICASSP is single-blind, so you **cite normally** — no
anonymized references, no hiding your own prior work. Reopen the current call only for
dual-submission and prior-publication rules. The four-page limit makes related work a
precision instrument, not a survey.

## Positioning checks

- Separate the **signal-processing novelty** (a new estimator, transform, representation,
  objective, architecture, or resource) from an engineering improvement.
- Compare against both the **IEEE SPS journal** literature and the **conference** literature; a
  reviewer from the relevant technical committee knows both.
- Position against the **nearest current-cycle work**, not a five-year-old baseline; ICASSP
  reviewers work in the subfield and notice a stale comparison immediately.
- Because review is single-blind, cite your own prior work in normal first person and make the
  incremental delta explicit rather than obscuring it.

## Literature lanes table

| Lane | Typical venues | What ICASSP reviewers check |
|---|---|---|
| SPS journals | IEEE TSP, TASLP, SPL, TIP, TIFS, TMM, TCI, TSIPN, JSTSP, OJSP | Whether the closest journal result is acknowledged and the delta stated |
| ICASSP + IEEE conferences | prior ICASSP, ICIP, ICME, SLT, ASRU | Whether the nearest conference method is compared or distinguished |
| Speech/audio siblings | Interspeech, WASPAA, EUSIPCO, DCASE | Whether a paper mis-attributed to ICASSP actually lives here |
| ML venues | NeurIPS, ICML, ICLR, AAAI | Whether generic-ML priors are credited without claiming their generality |

A bibliography that cites only ML venues and no SPS journals tells a committee reviewer the paper
may be rediscovering a known signal-processing result — a recognizable weakness that benchmark
strength does not repair.

## The sibling-venue attribution trap

Signal-processing landmarks are scattered across venues, and misattributing one is a credibility
hit. Common confusions to check before citing:

- Papers you *think* are ICASSP that are actually **Interspeech** (much of the speech-synthesis
  and self-supervised-speech canon) or **journal** papers (TASLP separation work).
- **ICIP** for image results and **EUSIPCO/WASPAA** for European and audio-workshop results.
- Verify each cited venue against dblp (`conf/icassp/`, `journals/`) rather than trusting memory;
  see [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) for the
  guard list.

## Positioning vignette

Suppose the paper proposes a low-complexity beamformer for a hearing device. Its nearest neighbors:
a TASLP paper with higher complexity, a prior ICASSP paper with a similar structure but no latency
budget, and an ML paper with a black-box network. The novelty sentence should name all three
contrasts — lower complexity than the journal method, an explicit latency budget the prior ICASSP
work lacked, and interpretability the black-box model lacked — in one or two sentences, because
four pages cannot afford a paragraph per contrast.

## Concurrent-work judgment

- Independently concurrent arXiv work: cite neutrally, state the technical difference, and avoid
  priority claims a reviewer cannot verify.
- Your own workshop or prior-conference version: cite it in first person and state exactly what
  this paper adds, since single-blind review does not require hiding it.
- If a venue's archival status is unclear for dual-submission purposes, declare the overlap rather
  than gambling on an organizer's interpretation.

## Output format

```text
[Novelty type] estimator / transform / representation / objective / architecture / resource
[Nearest 3 works] <work -> venue (verified) -> technical delta>
[Lane coverage] SPS journals / ICASSP+conf / siblings / ML — gaps?
[Attribution risk] <any venue to re-verify on dblp>
[Novelty sentence] <one ICASSP-ready contribution contrast>
```
