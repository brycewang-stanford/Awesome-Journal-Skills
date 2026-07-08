> **Illustrative teaching example.** The paper, method, benchmarks-as-described,
> and every number below are **fictional**, invented only to demonstrate ECCV
> first-page craft. No real-paper results are quoted and no venue policy is
> invented. Corresponding skills:
> [`eccv-writing-style`](../../skills/eccv-writing-style/SKILL.md),
> [`eccv-experiments`](../../skills/eccv-experiments/SKILL.md), and
> [`eccv-related-work`](../../skills/eccv-related-work/SKILL.md).

# Worked Example: An ECCV First Page (before → after)

The target is the first-page test from `eccv-writing-style`: by the end of
page 1 of a single-column LNCS paper, an **adjacent-niche reviewer** — the
majority of an ECCV panel — must know what input becomes what output, why the
current method families fail, and what one idea fixes it, with every claim
scoped to benchmark + protocol + substrate so it can be defended in a one-page
rebuttal later.

**Fictional paper:** *"Scaffold Splats: Feed-Forward Indoor Reconstruction from
Six Unposed Images."* Fictional setting: a feed-forward model that outputs a
Gaussian-splat scene from a handful of unposed wide-baseline photos.

---

## Before (a typical first draft)

> **Abstract.** 3D reconstruction is a fundamental problem in computer vision
> with many applications in AR/VR and robotics. Recently, 3D Gaussian
> Splatting has attracted significant attention. However, existing methods
> have limitations. In this paper, we propose Scaffold Splats, a novel
> framework for high-quality reconstruction from sparse views. Extensive
> experiments demonstrate that our method significantly outperforms
> state-of-the-art methods on multiple benchmarks.
>
> **Introduction.** With the rapid development of neural rendering, novel view
> synthesis has made remarkable progress... [half a page of history]. Despite
> this progress, sparse-view reconstruction remains challenging. Motivated by
> the above observations, we design a novel architecture that effectively
> leverages geometric priors. Our contributions are: (1) a novel framework;
> (2) a novel module; (3) extensive experiments showing superior performance.

**Why this fails the ECCV bar** (per `eccv-writing-style` / `eccv-experiments`):

- The **setting is never pinned**: how many views? posed or unposed? per-scene
  optimization or feed-forward? The adjacent-niche reviewer cannot even choose
  the right baseline universe — the exact misfiling risk mixed panels create.
- "Significantly outperforms state-of-the-art" is a **fragile claim**: no
  benchmark, no protocol, no substrate — indefensible in a one-page rebuttal.
- The contribution list is **unfalsifiable** ("novel framework", "novel
  module", "extensive experiments" — the bullet the venue's reviewers mock).
- Half a page of field history spends the scarcest asset (page 1 of 14,
  figures included) on what every reader already knows.
- No named mechanism: "effectively leverages geometric priors" gives the
  reviewer nothing to evaluate, and the ablation section nothing to toggle.

---

## After (ECCV first-page arc)

> **Abstract.** Given six unposed, wide-baseline photos of an indoor scene, we
> reconstruct a renderable 3D Gaussian scene in a single forward pass — no
> per-scene optimization and no camera poses. Existing routes fail on this
> input for distinct reasons: per-scene splat optimization needs dense posed
> coverage, and current feed-forward reconstructors assume near-neighboring
> views, degrading sharply past 30° baselines. Our key idea is a **layout
> scaffold**: the model first predicts a coarse room-structure lattice from
> all views jointly, then anchors per-view Gaussian predictions to the
> scaffold, which resolves the cross-view ambiguity that wide baselines
> create. On the [fictional] SparseRooms-6 protocol, Scaffold Splats improves
> PSNR by +1.8 dB over the strongest feed-forward baseline under a matched
> ViT-B backbone and identical training data, and degrades 3× more slowly as
> baseline angle grows; per-scene optimizers remain ahead when 50+ posed views
> are available, and we say so. Code, weights, and the evaluation protocol
> will be released.
>
> **Introduction, ¶1 (setting, pinned).** Six photos of a room, taken casually
> and without pose metadata, are what a real user produces; dense posed
> capture is what current splat pipelines require. We address exactly this
> gap: feed-forward reconstruction from six unposed views, evaluated at
> wide baselines.
>
> **¶2 (why each family fails — nameable reasons).** Per-scene optimization
> [refs] produces the highest fidelity but needs poses and dense coverage;
> at six views it collapses to floaters. Feed-forward reconstructors [refs]
> handle two or three near-neighboring views but fuse features pairwise, so
> wide baselines break correspondence — errors we quantify in Sec. 5.3.
> Pose-free methods [refs] recover cameras but still optimize per scene,
> inheriting the coverage requirement. *(Each family gets a specific,
> checkable failure — the `eccv-related-work` cluster-into-argument rule.)*
>
> **¶3 (the one idea).** Our observation: what six wide-baseline views share
> is not local texture but **room layout**. Scaffold Splats therefore predicts
> a coarse structural lattice first, jointly from all views, and conditions
> every per-view Gaussian head on it — turning an unconstrained multi-view
> fusion problem into anchored local prediction. *(One named mechanism the
> ablations can toggle: scaffold on/off, Sec. 5.2.)*
>
> **¶4 (claims, sized).** Under a matched backbone and training corpus,
> Scaffold Splats improves PSNR/SSIM on SparseRooms-6 and on re-splits of two
> public indoor sets [refs]; the win **persists at equal inference budget**;
> and a failure panel (Sec. 5.5) shows where the scaffold misleads —
> non-Manhattan interiors and glass. *(Matched-substrate row, efficiency
> frontier, and an honest failure case — the `eccv-experiments` triad,
> promised on page 1 and delivered in the body.)*

---

## What transferred (checklist for your own first page)

| Move | Where it shows up in the "after" |
| --- | --- |
| Pin the setting before selling it | Abstract sentence 1: input count, unposed, feed-forward |
| One failure reason per method family | ¶2 — optimization / feed-forward / pose-free each break differently |
| Name a single toggleable mechanism | ¶3 — the layout scaffold, with its ablation pre-announced |
| Size every claim to benchmark + protocol + substrate | +1.8 dB, matched ViT-B, identical data, named protocol |
| Concede the regime you lose | "per-scene optimizers remain ahead when 50+ posed views..." |
| Promise only checkable artifacts | Code, weights, protocol release — no vague "extensive experiments" |

> Next: check the positioning against real, venue-verified papers in
> [`../exemplars/library.md`](../exemplars/library.md), and the current-cycle
> format rules in [`../official-source-map.md`](../official-source-map.md) —
> the 14-page LNCS budget counts the teaser figure this page requires.
