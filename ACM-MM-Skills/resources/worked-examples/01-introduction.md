> **Illustrative teaching example.** The paper, method, setting, and every number below are
> **fictional** and exist only to demonstrate ACM MM house style. No real-paper facts, datasets,
> or results are stated, and no policy is invented. Corresponding skills:
> [`acmmm-writing-style`](../../skills/acmmm-writing-style/SKILL.md),
> [`acmmm-topic-selection`](../../skills/acmmm-topic-selection/SKILL.md), and
> [`acmmm-experiments`](../../skills/acmmm-experiments/SKILL.md).

# Worked Example: An ACM MM-Style Abstract + Introduction (before → after)

This demonstrates the **ACM MM first-page arc** from `acmmm-writing-style`:
**problem → why one modality is not enough → the cross-modal method → media-grounded evidence →
why it matters for multimedia** — under the ACM MM rules that the *multimedia* contribution sits
on the first page, that the **fusion is the contribution** (not a single-modality encoder), and
that subjective/perceptual claims are backed by an actual user study, not asserted.

The framing also reflects `acmmm-topic-selection`: ACM MM is strongest when the contribution
**lives at the seam between media** — here, aligning short-form video with its soundtrack and
on-screen captions. Strip two of the three modalities and the paper routes to CVPR (pure vision),
ACL (pure language), or ICMR (retrieval-only), not ACM MM.

**Illustrative paper (fictional):** *"Hearing the Cut: Audio-Visual-Text Alignment for
Highlight Detection in User-Generated Video."* Fictional method: a fusion model that predicts
highlight moments from the *disagreement* between what is seen, heard, and captioned.

---

## Before (buries the multimedia contribution — typical first-draft abstract + intro)

> **Abstract.** Video understanding has advanced rapidly with deep learning. In this work we study
> highlight detection, an important problem for content platforms. We propose a new neural network
> that processes video frames and achieves strong performance on a benchmark, outperforming prior
> methods. We also use audio and captions as extra inputs.
>
> **Introduction.** Highlight detection has been studied extensively. Many approaches use CNNs or
> transformers on video frames. In this paper, we add audio and text features to a video backbone
> and train end-to-end to score each moment. We evaluate on a standard dataset and show our method
> works well. Section 2 reviews related work, Section 3 describes our model, Section 4 presents
> experiments, and Section 5 concludes.

**What's wrong (against `acmmm-writing-style` / `acmmm-topic-selection` / `acmmm-experiments`):**

- **No multimedia contribution on the first page** — it leads with "video understanding," and
  audio/text arrive as an afterthought ("extra inputs"). ACM MM wants the *cross-modal* idea up
  front.
- **Fusion is not the contribution** — "add audio and text features to a video backbone" is a
  concatenation, not a mechanism. Reviewers ask what the modalities *do for each other*.
- **Single-modality framing** — pitched as a video benchmark win, which is a CVPR/ICCV contribution
  (`acmmm-topic-selection` re-route signal), not a multimedia one.
- **Overclaims** ("works well," "outperforming prior methods") with **no ablation** isolating the
  cross-modal gain and **no user study** for a perceptual "highlight" target (`acmmm-experiments`).
- **No claim → evidence pairing**: "strong performance" is tied to nothing specific.
- **Over-signposted roadmap** standing in for an argument.

---

## After (ACM MM arc — problem → why one modality fails → fusion → media evidence → why it matters)

> **Abstract.** Highlights in user-generated video are often **inaudible to a vision-only model**:
> the moment a crowd gasps or a caption lands the punchline is signalled by *cross-modal surprise*,
> not by any single stream. Existing detectors either score frames alone or late-fuse per-modality
> scores, discarding the *timing disagreement* between what is seen, heard, and read. We introduce
> **Cross-Modal Surprise (CMS)**, which localizes highlights from the moment-level divergence among
> synchronized video, audio, and caption streams, learned with a contrastive alignment objective.
> On a public short-video benchmark CMS improves mean average precision over the strongest
> late-fusion baseline, and an **ablation removing each modality shows the audio–text divergence
> term carries most of the gain**. A **user study (N reported, with inter-rater agreement)** confirms
> CMS-selected moments are preferred as highlights. *(problem → gap → fusion mechanism → ablated and
> perceptual evidence — all on the first page.)*
>
> **Introduction.** *(¶1 — problem + contribution, first breath.)* A highlight is a moment a viewer
> would *replay*, and on user-generated video that judgment is rarely carried by the picture alone —
> the laugh track, the gasp, the caption's timing all move it. We present **Cross-Modal Surprise**,
> a model that detects highlights from the **disagreement across synchronized video, audio, and
> caption streams** rather than from any one of them.
>
> *(¶2 — why one modality is not enough.)* Vision-only detectors miss moments with flat visuals but
> loud reactions; audio-only detectors fire on ambient noise; caption-only models miss non-verbal
> beats. Late fusion — averaging per-modality scores — cannot represent the case that matters here,
> where the *timing mismatch* between streams is the signal. *(each prior approach gets a specific
> failure, not a vague "prior work is limited.")*
>
> *(¶3 — the fusion mechanism + what it assumes.)* CMS aligns the three streams to a shared
> moment-level clock with a contrastive objective, then scores each moment by a learned **divergence**
> among the aligned embeddings. The **only structural assumption** is that the streams are
> approximately synchronized at capture; we handle drift with a soft alignment window. *(the fusion,
> not a backbone swap, is named as the contribution.)*
>
> *(¶4 — evidence, each claim paired.)* On the benchmark, CMS improves mAP over the strongest
> late-fusion baseline (Table 1). A leave-one-modality-out **ablation** attributes most of the gain
> to the audio–text divergence term (Table 2), directly testing the cross-modal claim. Because
> "highlight" is a **perceptual** target, we run a **user study**: raters prefer CMS moments over the
> baseline's, and we report agreement and the protocol in the supplement. *(every claim → a table, an
> ablation, or a study, per `acmmm-experiments`.)*
>
> *(¶5 — why it matters for multimedia + roadmap.)* The contribution is to make **cross-modal
> disagreement a first-class signal** for content understanding, reusable wherever streams are
> synchronized. Section 2 covers related fusion and highlight work; Section 3 details alignment and
> scoring; Section 4 reports the benchmark, ablations, and user study. *(brief roadmap, no
> over-signposting.)*

---

## Why the "after" meets the ACM MM bar

Mapped to the skill checklists:

- **Multimedia contribution on the first page** — the abstract and ¶1 name the cross-modal idea
  before any backbone detail (`acmmm-writing-style`: "put the multimedia contribution up front").
- **Fusion is the contribution** — the divergence mechanism, not a modality concatenation, is stated
  and then *ablated* (`acmmm-experiments`: isolate the cross-modal gain).
- **Right venue** — the claim only exists across three media, so it is an ACM MM fit rather than a
  CVPR/ICCV (vision-only) or ACL (text-only) re-route (`acmmm-topic-selection`).
- **Perceptual claim, perceptual evidence** — "highlight" is subjective, so a **user study with
  reported agreement** backs it, not an accuracy number alone (`acmmm-experiments`: use user studies
  / QoE where the target is subjective).
- **No overclaiming** — improvements are tied to specific tables and an ablation, not "works well."
- **sigconf discipline** — the alignment details and the full user-study protocol move to the
  supplement while the 6–8-page body carries the argument (`acmmm-writing-style`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, metadata-verified
> ACM MM papers** whose first pages lead with a multimedia contribution, and
> [`../official-source-map.md`](../official-source-map.md) for ACM MM-specific submission policy.
