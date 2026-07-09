# ICASSP Resources

Action-oriented resources for the ICASSP skill pack. The `skills/` give advice; this directory
lets an agent model an ICASSP-style signal-processing paper, benchmark against verified
exemplars, and assemble reproducibility artifacts without importing an unrelated code kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a signal-processing paper compressed into the ICASSP 4-page shape. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, dblp/IEEE-Xplore-verified ICASSP papers spanning ASR, speaker recognition, source separation, and audio classification, and avoid sibling-venue misattribution. |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle ICASSP format, review, portal, and policy sources before giving submission-ready advice; includes the gateway access-method note. |
| [`external_tools.md`](external_tools.md) | Open the CMS portal, IEEE Xplore, the SPS society site, and run the author-side verification passes. |
| [`code/README.md`](code/README.md) | Reuse the shared ML-conference reproducibility kit and the ICASSP-specific measurement checks (metric rulers, corpus versions, seeds) the generic tooling cannot make. |

## Scope note

This is an **IEEE signal-processing conference** pack spanning the whole ICASSP program —
speech and audio, but also image and video, communications and radar signals, sensor arrays,
estimation and detection theory, and machine learning for signals. It is **not** a
speech-only pack and **not** an econometrics pack. Speech is one track among many; the routing
skill teaches when a speech paper belongs at ICASSP versus at ISCA's Interspeech.

## Suggested workflow

1. Route and frame with
   [`../skills/icassp-topic-selection`](../skills/icassp-topic-selection/SKILL.md) and
   [`../skills/icassp-writing-style`](../skills/icassp-writing-style/SKILL.md).
2. Stress-test evidence with [`../skills/icassp-experiments`](../skills/icassp-experiments/SKILL.md),
   [`../skills/icassp-reproducibility`](../skills/icassp-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm current
   official rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the September gate.
