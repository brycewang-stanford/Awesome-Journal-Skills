---
name: icassp-topic-selection
description: Use when deciding whether a project fits ICASSP, the IEEE Signal Processing Society flagship spanning all signal processing, and specifically for the ICASSP-versus-Interspeech routing decision for speech work, plus routing to ICIP, EUSIPCO, WASPAA, SPS journals, or ML venues by identifying the signal-processing primitive of the contribution.
---

# ICASSP Topic Selection

Use this before writing. ICASSP is the **IEEE Signal Processing Society flagship**, and its
defining feature is **breadth**: speech and audio, image and video, communications and radar,
sensor arrays, estimation and detection theory, and machine learning for signals all review under
one roof. Speech is **one track among many**, not the identity of the venue. A project fits when
its contribution changes a **signal-processing primitive** and can be proved in four pages.

## Find the signal-processing primitive

Name what the contribution actually is:

- A new **estimator, transform, filter, or detector**; a new **representation or embedding**; a
  new **objective or inference procedure**; a **resource** (corpus/benchmark); or a
  **model-based-deep-learning** result that changes a block of the signal chain.
- If no signal-processing primitive exists — the paper is generic ML with no signal model — ICASSP
  is likely the wrong venue (see the re-route table).

## The ICASSP-vs-Interspeech routing decision (read this for any speech paper)

Speech papers can go to either venue, and picking wrong costs a cycle. They differ on mechanics as
much as on scope:

| Dimension | ICASSP (IEEE SPS) | Interspeech (ISCA) |
|---|---|---|
| Scope | **All** signal processing; speech is one track | **Speech and spoken language only** |
| Culture | Signal-processing methods, math-forward | Speech-science + engineering, spoken-language focus |
| Format | **4+1** (4 content pages + reference page) | **4+1** (4 content + reference page), different template |
| Anonymity | **Single-blind** — author list included | **Double-anonymous** with a pre-deadline anonymity period |
| Deadline | **September** (autumn) | **Late February** (winter) |
| Portal | **CMS** (`cmsworkshops.com`) | **Microsoft CMT** |
| Proceedings | **IEEE Xplore** | **ISCA Archive**, open access |

Decision rule: route to **ICASSP** when the contribution is a **signal-processing method** whose
speech application is one instance (a new front-end, estimator, separation objective, or array
technique), or when the September calendar and single-blind culture fit. Route to **Interspeech**
when the contribution is fundamentally about **spoken language** — phonetics, prosody, dialogue,
speech science, or a speech-specific model where the linguistic content is the point — or when the
February calendar and double-blind norms fit. When both fit, let deadline and reviewer community
decide.

## Fit signal table (full ICASSP breadth)

| Signal in the project | ICASSP reading |
|---|---|
| New estimator/filter/detector with a signal model + evaluation | Core fit — the house genre |
| Speech/audio method framed as a signal-processing mechanism | Core fit (vs Interspeech if it is spoken-language-centric) |
| Image/video restoration, coding, or analysis | Core fit (compare ICIP for image-specific work) |
| Communications, radar, array, or sensor signal processing | Core fit |
| Generic deep net with strong benchmarks but no signal insight | Better at NeurIPS/ICML/ICLR/AAAI |
| A finished, journal-length result with extensive theory | An SPS journal (TSP/TASLP/SPL) |

## Re-route table

- **Generic ML, no signal model** → NeurIPS, ICML, ICLR, AAAI.
- **Spoken-language-centric speech** → Interspeech (or SLT/ASRU for those subfields).
- **Image-specific** → ICIP; **European/audio-workshop** → EUSIPCO, WASPAA, DCASE.
- **Journal-length, finished** → IEEE TSP, TASLP, SPL, TIP, or a sibling SPS journal; consider the
  **OJSP-ICASSP** track to present at ICASSP while publishing open-access in a journal.

## Sharpening moves before committing

- State the primitive in one sentence; if you cannot, the ICASSP framing does not yet exist.
- Confirm the result fits four pages with a task-matched metric and a standard baseline; a claim
  that needs journal-length exposition should go to an SPS journal or the OJSP track.
- For speech work, run the ICASSP-vs-Interspeech table explicitly rather than defaulting to
  whichever deadline is closer.
- Subject-area emphasis drifts by cycle; scan the current EDICS list before final routing.

## Output format

```text
[Fit] strong ICASSP / possible ICASSP / better elsewhere
[Primitive] estimator / transform / representation / objective / resource / model-based-DL / none
[If speech] ICASSP vs Interspeech -> <decision + reason (scope/calendar/blinding)>
[Best venue] ICASSP / Interspeech / ICIP / EUSIPCO / WASPAA / SPS journal / ML venue
[Contribution sentence] <one signal-processing claim>
[Next action] <framing, experiment, or venue switch>
```
