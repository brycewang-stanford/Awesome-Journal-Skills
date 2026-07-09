---
name: acmmm-topic-selection
description: Use when deciding whether a project is a genuine ACM MM (ACM Multimedia) contribution rather than single-modality work, choosing a thematic area, and routing between ACM MM, CVPR/ICCV, ACL/EMNLP, ICMR, MMSys, NeurIPS/ICLR, and the ACM TOMM journal by finding the cross-modal or media-systems core of the contribution.
---

# ACM MM Topic Selection

Use this before writing. ACM MM is strongest for work that **treats more than one medium at
once** — vision, audio/speech, language, sensor, interaction — or that advances the systems
that transport, index, and render media. The core test is whether the contribution *lives
at a seam between media*.

## Fit test

- Prefer ACM MM when the contribution is **cross-modal integration** (fusion, alignment,
  cross-modal retrieval/generation), a **media-systems** advance (streaming, QoE,
  transport), or a **human-centric media** result (emotion, aesthetics, engagement, art).
- Route to **CVPR/ICCV/ECCV** if the contribution is a pure computer-vision claim — a better
  detector, segmenter, or backbone with no essential second modality.
- Route to **ACL/EMNLP** if it is a pure language claim, and to **NeurIPS/ICLR** if it is a
  general ML method whose multimedia setting is incidental.
- Route to **ICMR** for retrieval-centric work that is more IR than multimedia systems, to
  **MMSys** for systems/networking-heavy media delivery, and to the **ACM TOMM** journal
  when the work needs journal-length treatment.
- Confirm the argument can be made convincing in a **6–8 page** sigconf body.

## Fit signal table

| Signal in the project | ACM MM reading |
|---|---|
| Two or more modalities that must interact for the result to hold | Core fit — the house genre |
| A reusable media system, framework, or dataset the community adopts | Core fit (Open Source / Dataset tracks) |
| Subjective quality / emotion / engagement measured with a user study | Core fit (human-centric areas) |
| A single-modality benchmark win (vision-only, text-only) | Better at CVPR/ICCV or ACL |
| Retrieval accuracy with no systems or cross-modal novelty | ICMR or SIGIR |
| Media delivery / networking with little content modeling | MMSys |

## Picking the thematic area

The main track is split into thematic areas (Multimodal Fusion; Generative and Foundation
Models; Search and Recommendation; Emotional and Social Signals; Art and Culture; Systems;
Transport and Delivery; Responsible Multimedia; and more). The area is not cosmetic — it
selects your reviewers. Name the **primary** area honestly; if the paper genuinely spans
two, pick the one whose reviewers can best judge the *contribution*, not the application.

## Vignette: where an audio-visual model goes

A project fuses lip motion and speech to improve transcription in noise. ACM MM reading:
strong fit — the gain exists *only* because two modalities correct each other, which is the
Multimodal-Fusion heartland. Strip the audio and keep a visual speech-recognition benchmark,
and the same project reads as a CVPR paper; strip the video and tune a language model on the
transcripts, and it becomes an ACL/speech paper. The multimedia contribution is the
correction *between* streams.

## Routing within ACM MM

Deciding it is an ACM MM paper is only half the choice; the track shapes everything after.

| The project's center of gravity | Track within ACM MM |
|---|---|
| A method paper with cross-modal results | Main track (pick a thematic area) |
| A bold vision / new direction, evidence lighter | Brave New Ideas |
| A shared task entry with a competitive result | Multimedia Grand Challenge |
| A reusable, documented software system | Open Source Software Competition |
| A new dataset or benchmark | Dataset track |
| A rebuild of prior published results | Reproducibility track |

The tracks differ in blinding and in what reviewers reward, so a strong-but-early idea does
better in Brave New Ideas than as a thin main-track method paper, and a great system does better
in the Open Source competition than buried as a main-track artifact.

## The single-modality trap

The most common misroute is a **single-modality paper wearing a multimedia costume**: audio or
text is bolted on but never shown to matter. If a leave-one-modality-out ablation would leave
the result essentially unchanged, the paper is not cross-modal, and an ACM MM reviewer will say
so. Either make the second modality load-bearing or route the paper to its true home venue
before writing — retrofitting multimedia framing onto a vision or NLP result rarely survives
review.

## Sharpening moves before committing

- Name the cross-modal or systems primitive: the fusion mechanism, the alignment objective,
  the delivery scheme, or the perceptual measure. If none exists, the ACM MM framing does
  not either.
- Decide the track early — main vs. Brave New Ideas (vision paper), Open Source Software,
  Dataset, or Reproducibility — because each has a different format and blinding rule.
- If the payoff is subjective, plan a **user study** now; ACM MM reviewers expect perceptual
  claims to be measured, not asserted.
- Thematic-area lists drift between cycles; scan the current Topics of Interest before final
  routing.

## Output format

```text
[Fit] strong ACM MM / possible ACM MM / better elsewhere
[Best venue] ACM MM / CVPR / ICCV / ACL / ICMR / MMSys / NeurIPS / TOMM / other
[Thematic area] <primary area, if ACM MM>
[Cross-modal or systems core] <one sentence>
[Top rejection risk] <single-modality framing / weak fusion / no user study / scope>
[Next action] <method, user study, framing, or venue switch>
```
