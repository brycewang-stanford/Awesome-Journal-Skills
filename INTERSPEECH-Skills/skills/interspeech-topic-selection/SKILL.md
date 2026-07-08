---
name: interspeech-topic-selection
description: Use when deciding whether a project belongs at INTERSPEECH, the ISCA flagship speech conference, or should be routed to ICASSP, ASRU/SLT, Odyssey, SSW, ACL/EMNLP, or a speech journal — testing whether spoken language is the contribution, matching subfields to the reviewer pool, and choosing between the 4-page and Long Paper tracks.
---

# INTERSPEECH Topic Selection

Interspeech is the annual conference of ISCA — the **International Speech
Communication Association**, not to be confused with the computer-architecture
symposium that shares the acronym. It is the broadest speech venue in existence:
phoneticians, hearing scientists, ASR engineers, and voice-cloning teams review in
adjacent areas of the same program. Fit means convincing *speech* reviewers, and the
2026 theme in Sydney was "Speaking Together" — inclusion across languages, cultures,
and modalities. Reconfirm scope at https://interspeech2026.org before routing.

## The modality test

Ask: **if the audio were replaced by its transcript, would the contribution survive?**

- If yes, the paper is NLP wearing a headset — route it to an ACL-family venue where
  text-based reviewers will value it.
- If no — the claim depends on acoustics, prosody, speakers, articulation, hearing,
  or the speech signal itself — Interspeech is a candidate.
- Borderline: spoken-language understanding and speech-LLM work fits when the spoken
  channel (disfluency, ASR errors, prosody, audio tokens) is analyzed, not assumed away.

## Where Interspeech sits among its neighbors

| If the core contribution is... | Prefer | Why not Interspeech |
|---|---|---|
| Speech science *or* technology, any subfield | **Interspeech** | — (this is home turf) |
| General signal processing, radar, imaging | ICASSP (IEEE) | Interspeech reviewers expect speech, not DSP breadth |
| ASR-only deep dive, workshop-scale | ASRU / SLT (IEEE, biennial) | Smaller, narrower; fine for follow-ups |
| Speaker/language recognition depth | Odyssey (ISCA workshop) | Specialist audience; Interspeech still fine |
| TTS system depth | SSW (ISCA Speech Synthesis Workshop) | Same trade-off as Odyssey |
| Text NLP, LLM reasoning, no audio analysis | ACL / EMNLP / NAACL | Fails the modality test |
| Mature work needing >4 pages of record | IEEE/ACM TASLP, Computer Speech & Language, Speech Communication | Journal timelines, no conference clock |

## Subfield-to-area matching

Interspeech submissions are reviewed inside scientific areas chosen at submission
time. Misfiled papers draw reviewers with the wrong evaluation instincts:

- **Recognition-side**: ASR architectures, robustness, adaptation, decoding.
- **Generation-side**: TTS, voice conversion, singing synthesis.
- **Talker-side**: speaker verification, diarization, anti-spoofing, voice privacy.
- **Human-side**: phonetics, prosody, production/perception, pathological speech,
  child speech, second-language learning.
- **Interaction-side**: spoken dialogue, SLU, speech translation, audio LLMs.
- **Resource-side**: corpora, benchmarks, evaluation methodology, challenges.

A phonetics claim reviewed by ASR engineers (or vice versa) is the most common
self-inflicted rejection at this venue; pick the area for the *claim*, not the tools.

## Track choice inside Interspeech (new in 2026)

Interspeech 2026 introduced a **Long Paper track** (reported: up to 8 pages plus 2
reference pages, targeted acceptance below 30%) alongside the classic 4-page regular
paper. Choose long only when the contribution genuinely cannot be stated in four
pages — a benchmark with extensive analysis, a theory-plus-system arc. A padded
4-page idea in the long track competes against a stricter bar. Verify the current
track rules; this split is one cycle old.

## Signals the project is Interspeech-shaped

- The evaluation uses speech-native metrics (WER, MOS, EER, PESQ) on named corpora.
- Error analysis engages speakers, accents, noise conditions, or phonetic categories.
- The related work traces through the ISCA Archive, not only arXiv and ACL.
- A speech scientist and a speech engineer would both find something to argue with.

## Signals to reroute

- Results reported only on text benchmarks with audio as an afterthought.
- The novelty is a general ML trick demonstrated on speech among other domains —
  NeurIPS/ICML reviewers reward generality; Interspeech reviewers ask what it
  teaches about speech.
- The paper is a product description without a falsifiable claim.

## Three triage vignettes

- **"We fine-tuned an LLM to summarize meeting transcripts."** Transcript-only
  input, text output, no acoustic analysis — fails the modality test. Route to an
  ACL-family venue; return here only if ASR-error propagation or prosodic cues
  enter the analysis.
- **"Our vocoder halves inference cost at equal MOS."** Speech-native claim,
  speech-native metric, engineering contribution — strong Interspeech fit in a
  generation-side area; SSW is the specialist fallback if the delta is
  vocoder-internals deep.
- **"A cross-linguistic study of vowel reduction in child speech."** No system at
  all, and still a strong fit — human-side areas review speech *science* on its
  own terms. This breadth is exactly what ICASSP does not offer.

## Questions to settle before committing

- Which two or three scientific areas could plausibly host the claim, and which
  reviewer pool do you actually want? (Decide now; it is frozen at submission.)
- Is there a running challenge whose test set and baseline make your evaluation
  legible for free?
- Does the evidence you can gather by the deadline fill 4 pages convincingly, or
  does honesty require the Long Paper track or a journal?
- If the answer is "reroute," is the finding still worth an ISCA workshop
  (Odyssey, SSW, task workshops) where the specialist audience is denser?

## Output format

```text
[Modality test] survives transcript-only? yes / no / partial — <one line>
[Interspeech fit] strong / plausible / reroute
[Area match] <scientific area the claim belongs to>
[Track] 4-page regular / Long Paper (verify current rules) / workshop or challenge
[Reroute target] <ICASSP / ASRU / SLT / Odyssey / SSW / ACL-family / journal + reason>
[Cycle reality] next deadline and source URL, or 待核实
```

## Cycle anchor (checked 2026-07-08)

Interspeech 2026: Sydney, Australia, 27 September – 1 October 2026, hosted with
ASSTA; submissions closed 25 February 2026. Interspeech 2027 is announced for São
Paulo, Brazil (29 August – 2 September 2027) — the first South American edition —
so a project failing today's fit test has a concrete next target. Treat every date
here as a snapshot; reopen the official site before planning.
