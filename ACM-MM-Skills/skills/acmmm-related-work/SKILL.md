---
name: acmmm-related-work
description: Use when building or auditing the related-work section of an ACM MM (ACM Multimedia) paper — covering the multimedia literature spread across vision, audio/speech, language, HCI/QoE, and systems, handling arXiv-speed concurrency, keeping citations double-blind, and verifying that cited "ACM MM papers" are ACM MM and not ICMR, MMSys, CVPR, or TOMM.
---

# ACM MM Related Work

Use this to position an ACM Multimedia paper against a literature that is unusually *spread
out*: a cross-modal contribution touches several single-modality communities plus the
multimedia venues that combine them.

## The five multimedia shelves

A strong ACM MM related-work section shows command of all shelves the contribution touches,
not just the author's home community:

- **Vision** — the visual side (CVPR/ICCV/ECCV) your method builds on or competes with.
- **Audio/speech and music** — the acoustic side (ICASSP, INTERSPEECH, ISMIR) if a stream is
  audio.
- **Language** — the text side (ACL/EMNLP) if captions, transcripts, or descriptions matter.
- **HCI / QoE / human-centric** — perception, engagement, and interaction (CHI, QoMEX) when
  the claim is subjective.
- **Multimedia proper** — ACM MM, ICMR, MMSys, and TOMM, where these threads are combined.

## Coverage vs. venue-hygiene table

| Task | What to do | Failure it prevents |
|---|---|---|
| Cover each modality you use | Cite the current best single-modality work per stream | "You ignored the vision literature" |
| Cite the fusion lineage | Trace the cross-modal line your method extends | "No delta over existing fusion" |
| Verify the venue string | Confirm each "ACM MM" cite on dblp `conf/mm` | Misattributing an ICMR/CVPR paper to ACM MM |
| Handle concurrency | Note contemporaneous arXiv work honestly | "You missed / overclaimed novelty vs. X" |
| Keep it blind | Cite your own prior work in third person | Double-blind violation |

## Positioning, not listing

Do not enumerate. For each closest neighbor, state in one clause **what it did** and in one
clause **what your paper adds** — and make sure the delta is *cross-modal*, since "we swap a
better encoder" is a single-modality delta a reviewer will discount.

```text
[Neighbor] Late-fusion audio-visual highlight scoring (VenueYear).
[Their move] Average per-modality scores.
[Our delta] Score the timing DISAGREEMENT between streams — a signal averaging cannot represent.
```

## Concurrency under arXiv speed

Multimedia sub-areas move fast and preprint heavily. Acknowledge genuinely concurrent work
(roughly same-window preprints) as concurrent rather than prior, do not claim to beat a
method you did not run, and do not silently drop a close preprint — a reviewer who knows it
reads the omission as evasion.

## Double-blind citation hygiene

- Cite your own earlier papers in the third person ("Prior work [X] showed..."), never "our
  previous paper."
- Avoid anonymity leaks through a dataset, system name, or repository that only your group
  uses.
- The single-blind tracks (Reproducibility, Open Source Software, Dataset) relax this — but
  the main track and Brave New Ideas do not.

## Building the section in passes

```text
Pass 1: list the modalities and sub-fields your contribution touches (the shelves).
Pass 2: for each shelf, cite the current strongest 2-3 works you build on or beat.
Pass 3: trace the FUSION lineage — the cross-modal line your method extends — as its own thread.
Pass 4: add same-window arXiv work as concurrent, not prior.
Pass 5: verify every "ACM MM" cite on dblp; convert your self-cites to third person.
```

A reader should finish the section able to name *which* prior fusion approach you improve on and
*why* the single-modality shelves are covered but not the whole story.

## The multimedia-specific omission risk

Because a cross-modal paper sits between communities, the dangerous omission is usually the
*other* community's closest work — a vision-trained author who misses the audio or IR paper that
already did half the job. Before submitting, ask a question from each shelf's perspective: "what
would an audio reviewer, an IR reviewer, and a systems reviewer each say I missed?" That triage
catches the omissions that sink cross-area papers.

## Venue-verification pass

Before submission, spot-check every citation that claims an ACM MM placement against dblp's
`conf/mm` edition record. The common traps: ICMR papers cited as ACM MM, TOMM journal
articles cited as the conference, and CVPR/ICCV vision papers cited as multimedia. Fix the
venue string or the claim that rests on it.

## Output format

```text
[Shelf coverage] vision/audio/language/HCI-QoE/multimedia — <covered / gaps>
[Fusion lineage] traced / missing
[Deltas] cross-modal and specific / single-modality or vague: <list>
[Concurrency] handled / risky omissions: <list>
[Blindness] clean / leaks: <list>
[Venue hygiene] verified / suspect cites: <list>
```
