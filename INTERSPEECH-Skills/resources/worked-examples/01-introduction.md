> **Illustrative teaching example.** The system, corpus results, and every number
> below are **fictional**, invented only to demonstrate Interspeech house style.
> No real-paper content is reproduced and no venue policy is invented.
> Companion skills:
> [`interspeech-writing-style`](../../skills/interspeech-writing-style/SKILL.md),
> [`interspeech-experiments`](../../skills/interspeech-experiments/SKILL.md),
> [`interspeech-topic-selection`](../../skills/interspeech-topic-selection/SKILL.md).

# Worked Example: An Interspeech Abstract + Introduction (before → after)

The target is the **one-pass property** from `interspeech-writing-style`: a mixed
reader — phonetician, ASR engineer, or skimming area chair — must extract *task,
move, corpus, metric, delta* from the first page without effort, inside a 4-page
budget that forbids warm-up prose.

**Fictional paper:** *"Prosody-Gated Streaming ASR for Spontaneous Speech"* — a
streaming recognizer that uses a lightweight prosodic-boundary detector to gate
chunk boundaries, aimed at disfluent conversational audio.

---

## Before (the draft that reads like a text-NLP paper)

> **Abstract.** In recent years, end-to-end models have revolutionized automatic
> speech recognition. However, streaming recognition of spontaneous speech remains
> challenging. In this paper, we propose a novel prosody-aware framework that
> significantly improves recognition performance. Extensive experiments demonstrate
> the effectiveness and superiority of our proposed approach compared to strong
> baselines.
>
> **1. Introduction.** Automatic speech recognition (ASR) is a fundamental task
> with numerous applications such as voice assistants, meeting transcription, and
> accessibility. With the rise of deep learning, performance has improved
> dramatically. Nevertheless, spontaneous speech presents unique challenges.
> Motivated by this, we design a novel framework incorporating prosodic
> information. Our contributions are threefold: (1) we propose a novel
> architecture; (2) we conduct extensive experiments; (3) we achieve
> state-of-the-art results.

**Why this fails at Interspeech** (mapped to the skills):

- **No numbers, no corpus, no metric in the abstract** — "significantly improves"
  with nothing checkable; Interspeech abstracts carry the headline WER.
- **The speech is missing.** Prosody is name-dropped, never engaged: which
  boundaries, detected how, gated where? The modality test of
  `interspeech-topic-selection` would flag this framing as transcript-survivable.
- **Wasted centimeters**: "revolutionized", "fundamental task with numerous
  applications" — dead weight in a 4-page form.
- **Contribution list without content**: "novel architecture / extensive
  experiments / state-of-the-art" describes every paper and therefore no paper.
- **No latency story** — a *streaming* claim without an operating point is
  unfalsifiable (`interspeech-experiments`: metric must match the claim).

---

## After (the Interspeech shape)

> **Abstract.** Streaming ASR degrades sharply on spontaneous speech because
> fixed-length chunking cuts across disfluencies and repairs. We gate chunk
> boundaries with a 0.3M-parameter prosodic-boundary detector trained on pause and
> F0 cues, so the encoder emits at prosodically licensed points. On the (fictional)
> CONV-2k conversational corpus, prosody gating reduces WER from 14.2% to 12.9%
> (paired bootstrap, p < 0.01) at equal median latency (480 ms), with the largest
> gains on utterances containing repairs (−2.4 abs.). Gains persist at 320 ms and
> 640 ms operating points. Code and the boundary-detector recipe are released.
>
> **Index Terms**: streaming ASR, prosody, disfluency, spontaneous speech
>
> **1. Introduction.** Fixed-interval chunking is the standard compromise in
> streaming ASR: it bounds latency but ignores speech structure, so chunk edges
> fall inside disfluent regions where acoustic and lexical cues conflict. On read
> speech this costs little; on conversational audio it is the dominant streaming
> error source, concentrated at repairs and restarts [1,2] *(positioning by
> property, per `interspeech-related-work`)*.
>
> We test a specific hypothesis: **if chunk boundaries are licensed by prosody,
> streaming error on spontaneous speech drops at no latency cost.** A small
> boundary detector consumes pause duration and F0 reset features and gates the
> emit decision of a streaming Conformer [3]; the recognizer is otherwise stock,
> so the effect of gating is isolated *(one named move + clean ablation, per
> `interspeech-experiments`)*.
>
> On CONV-2k we compare against fixed 480 ms chunking and an oracle-boundary upper
> bound: gating recovers 61% of the oracle gap; per-condition analysis places the
> gains on repair-bearing utterances *(the analysis finding that turns a delta
> into a statement)*. Section 2 relates the gate to prior segmentation policies;
> Sections 3–4 give the detector, protocol, and results.

---

## What changed, itemized

| Dimension | Before | After |
|---|---|---|
| Checkability | "significant improvements" | 14.2 → 12.9 WER, p-value, latency held fixed |
| Speech engagement | prosody name-dropped | pause + F0 cues, licensed boundaries, repair-bearing analysis |
| Claim scope | "state-of-the-art" | one hypothesis, tested at three operating points |
| Method identity | "novel framework" | one gate on a cited stock recognizer (diff-based description) |
| Space | two paragraphs of motivation | first sentence *is* the problem |
| Reviewer species served | ML generalist only | engineer (WER/latency), scientist (prosodic licensing), both |

## The self-test

Read only the after-abstract and answer: task? (streaming ASR on spontaneous
speech) — move? (prosodic gating of chunk boundaries) — corpus? (CONV-2k) —
metric? (WER at fixed latency) — delta? (−1.3 abs., significant, repair-focused).
Five answers in one pass: the page is doing Interspeech's job. Then benchmark
against the real, verified papers in [`../exemplars/library.md`](../exemplars/library.md)
and check current format law in [`../official-source-map.md`](../official-source-map.md).
