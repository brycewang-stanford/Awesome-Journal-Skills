> **Illustrative teaching example.** The paper, method, scenes, and every number below are
> **fictional** and exist only to demonstrate SIGGRAPH house style. No real-paper facts, systems,
> or results are stated, and no policy is invented. Corresponding skills:
> [`siggraph-writing-style`](../../skills/siggraph-writing-style/SKILL.md),
> [`siggraph-topic-selection`](../../skills/siggraph-topic-selection/SKILL.md), and
> [`siggraph-experiments`](../../skills/siggraph-experiments/SKILL.md).

# Worked Example: A SIGGRAPH-Style Teaser + Abstract + Introduction (before → after)

This demonstrates the **SIGGRAPH first-page arc** from `siggraph-writing-style`:
**graphics problem an expert recognizes → why prior methods fall short (quality / speed /
generality / robustness) → our technique in one sentence → the result shown (teaser + video) →
what it enables** — with the SIGGRAPH expectations that the contribution is a *graphics capability*
on a measurable axis, that evidence is **shown** through comparisons and a results video, and that
**limitations are shown, not hidden**.

The framing also reflects `siggraph-topic-selection`: SIGGRAPH is strongest when the advance is a
reusable technique for how images, geometry, or motion are **created, simulated, or rendered** —
here, real-time volumetric cloud rendering — and when the lesson survives swapping the underlying
network (otherwise it re-routes to a vision venue).

**Illustrative paper (fictional):** *"Real-Time Cloudscapes: A Compact Anisotropic Encoding for
Interactive Volumetric Clouds."* Fictional method: a compact directional encoding that renders
animated volumetric clouds at interactive rates with multiple-scattering appearance, evaluated
against an offline path-traced reference and a prior real-time approximation.

---

## Before (buries the graphics contribution — typical first-draft abstract + intro)

> **Abstract.** Volumetric rendering is important in computer graphics. We propose a neural network
> that represents clouds and renders them using a novel architecture. Our method achieves good
> results on several scenes and outperforms baselines, demonstrating the power of deep learning for
> rendering.
>
> **Introduction.** Clouds are common in games and films. Many methods render volumes. In this
> paper we train a network to represent cloud density and appearance, and we show it produces nice
> images on a dataset of scenes. Section 2 covers related work, Section 3 our method, Section 4
> experiments, Section 5 limitations, and Section 6 concludes.

**What's wrong (against `siggraph-writing-style` / `siggraph-topic-selection` / `siggraph-experiments`):**

- **No graphics problem and no capability axis on the first page** — it leads with "deep learning
  is powerful," not with a problem a rendering engineer recognizes (real-time multiple scattering)
  or the axis it moves (quality at interactive frame rates).
- **No teaser.** The single most-read object at SIGGRAPH is missing; nothing is *shown*.
- **Wrong evidence shape.** "Good results" and "outperforms baselines" name no metric, no
  reference, no timing, and no comparison a reviewer can check — and clouds are temporal, so a
  static claim ignores the video the reviewer will watch.
- **Model-as-contribution.** If the network were swapped, no rendering lesson remains — the
  `siggraph-topic-selection` signal that this is a learning paper wearing a graphics title.
- **Limitations quarantined** in a late section instead of shown.
- **Over-signposted roadmap** substituting for an argument.

---

## After (SIGGRAPH arc — problem → inadequacy → technique → shown result → what it enables)

> **Teaser (Fig. 1).** A dynamic, sunlit cumulus field rendered by our method at **interactive
> rates**, placed beside an **offline path-traced reference** and a prior real-time approximation on
> the same view, sun angle, and time budget — our result recovers the reference's silver-lining
> multiple scattering the prior real-time method flattens. *(See supplemental video for the animated
> sequence.)*
>
> **Abstract.** Real-time volumetric clouds must capture **multiple scattering** — the silver
> lining and translucency that read as "sky" — yet interactive methods approximate it away, and
> offline path tracing that gets it right costs seconds per frame. We present a **compact
> anisotropic encoding** that stores directional in-scattering in a small per-voxel basis, letting a
> lightweight shader reconstruct multiple-scattering appearance at **interactive frame rates**. On
> an animated cloudscape suite we match an offline reference within a stated perceptual tolerance
> while rendering **two orders of magnitude faster** than the reference, and we compare quality,
> temporal stability, and timing (on stated GPUs) against a prior real-time approximation. We show
> failure cases on thin, wispy cirrus and report an ablation isolating the anisotropic term.
> *(problem → inadequacy → technique → shown result vs reference + baseline → limitation posture —
> all on the first page.)*
>
> **Introduction.** *(¶1 — the graphics problem, first breath.)* The look of a sky is governed by
> light bouncing many times inside a cloud. Artists and engineers can render this correctly offline,
> but at seconds per frame; in real time they fall back on single-scattering approximations that
> make clouds read as flat cotton. The rendering question is therefore not "can a network fit a
> cloud?" but **"can we reconstruct multiple-scattering cloud appearance at interactive rates,
> matching an offline reference?"**
>
> *(¶2 — why the current state is inadequate.)* Real-time volumetric methods approximate
> higher-order scattering with ambient terms that are cheap but lose the directional silver lining;
> offline path tracing captures it but is far too slow for interaction, and precomputed transport
> assumes static media that cannot animate. No prior method delivers **animated** multiple-scattering
> clouds at interactive rates with a checkable match to a reference.
>
> *(¶3 — contribution, stated as a graphics capability.)* We contribute a **compact anisotropic
> in-scattering encoding** and a reconstruction shader that together render animated volumetric
> clouds with multiple-scattering appearance at interactive frame rates. The encoding is small
> enough to update per frame, so the clouds move.
>
> *(¶4 — evidence shown, each claim paired.)* We tie every claim to shown evidence: quality against
> an offline path-traced reference with a perceptual metric and side-by-side stills (Fig. 5) and the
> animated video; temporal stability across a moving camera in the supplemental video (flicker is
> what a still hides); timing on two stated GPUs at fixed resolution (Table 1); and an ablation
> removing the anisotropic term to isolate its contribution (Fig. 7). Code, scenes, and the
> reference renders are in the supplemental package.
>
> *(¶5 — limitations shown and what it enables.)* We show where it breaks: thin cirrus with
> sub-voxel structure loses detail, and we display the failure beside the reference rather than
> omitting it. The payoff is concrete: interactive applications gain film-like cloud lighting within
> a real-time budget. Section 3 details the encoding; Section 4 the reconstruction; results and
> comparisons follow, with limitations shown alongside them. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the SIGGRAPH bar

Mapped to the skill checklists:

- **Graphics contribution on the first page** — the teaser, abstract, and ¶1 pose a rendering
  problem and a capability axis (multiple scattering at interactive rates) before any network detail
  (`siggraph-writing-style`: "lead with the graphics contribution; the teaser carries the paper").
- **Evidence shown and proportional** — the claim is about *appearance and speed*, so the evidence
  is a comparison to an offline reference with a metric, a results video for motion and temporal
  stability, and timings on stated hardware, not "good results" (`siggraph-experiments`: match the
  shown evidence to the claim; timings are checkable claims).
- **Right venue, model-swap test passes** — the lesson (a compact anisotropic encoding recovers
  multiple scattering in real time) survives swapping the reconstruction backend, so it is a
  graphics contribution, not a learning re-route (`siggraph-topic-selection`).
- **Limitations shown, not hidden** — the cirrus failure is displayed beside the reference, which
  *builds* credibility at this venue rather than costing it (`siggraph-writing-style`).
- **Fair comparison** — same view, sun angle, and time budget against both a reference and the
  strongest prior real-time method pre-empt the reviewer's first objection (`siggraph-experiments`,
  `siggraph-related-work`).
- **Runnable results** — code, scenes, and reference renders shipped in the supplemental set up a
  deterministic reproduction and a possible replicability stamp (`siggraph-reproducibility`,
  `siggraph-artifact-evaluation`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified SIGGRAPH
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for SIGGRAPH-specific submission policy,
> the dual-track model, and the ACM TOG journal-integrated cycle.
