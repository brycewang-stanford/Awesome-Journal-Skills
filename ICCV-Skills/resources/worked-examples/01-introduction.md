> **Illustrative teaching example.** The paper, method, datasets-as-described, and every
> number below are **fictional**, invented solely to demonstrate ICCV first-page craft.
> No real results are quoted and no venue policy is invented. Companion skills:
> [`iccv-writing-style`](../../skills/iccv-writing-style/SKILL.md),
> [`iccv-related-work`](../../skills/iccv-related-work/SKILL.md), and
> [`iccv-experiments`](../../skills/iccv-experiments/SKILL.md).

# Worked Example: Rewriting an ICCV First Page (before → after)

**Fictional paper:** *"Occlusion-Aware Gaussian Surfels for Open-World Multi-View
Reconstruction"* — a 3D reconstruction method whose claimed capability is completing
surfaces behind occluders using learned category-agnostic priors.

The rewrite demonstrates the targets from `iccv-writing-style`: a generalist vision
reviewer can state the idea from page 1; the mechanism comes before the adjectives;
every claim is scoped to dataset + protocol; and the intro's contribution bullets are
falsifiable statements, not activities.

---

## Before (the draft that gets a "limited novelty" review)

> **Abstract.** 3D reconstruction is a fundamental problem in computer vision with
> numerous applications in robotics, AR/VR, and autonomous driving. Recently, Gaussian
> splatting has attracted increasing attention due to its efficiency and quality.
> However, existing methods still struggle in complex real-world scenarios. In this
> paper, we propose a novel occlusion-aware framework that significantly improves
> reconstruction quality. Extensive experiments on several challenging benchmarks
> demonstrate that our approach achieves state-of-the-art performance.
>
> **Introduction (opening).** In recent years, neural rendering has revolutionized 3D
> reconstruction. From NeRF to Gaussian splatting, tremendous progress has been made.
> Despite this progress, challenges remain. Motivated by these observations, we design
> a novel framework... Our contributions are: (1) we propose a novel occlusion-aware
> framework; (2) we conduct extensive experiments; (3) we achieve state-of-the-art
> results.

**Diagnosis against the skills:**

- *No stated capability.* "Struggle in complex scenarios" names no failure mechanism;
  the reader cannot tell what the paper makes possible (`iccv-writing-style`:
  mechanism-first).
- *Unscoped superlatives.* "Significantly improves," "state-of-the-art" with no
  dataset, protocol, or budget — each one is a rebuttal liability in the one-page May
  window.
- *Contribution bullets are activities.* "We conduct extensive experiments" is work
  performed, not a claim a reviewer can falsify.
- *History-tour opening.* Two sentences of "in recent years" spend the page's most
  valuable inches teaching the reviewer nothing they don't know.
- *Invisible positioning.* Nothing distinguishes this from the two nearest neighbors a
  skeptic will name (`iccv-related-work`: the delta must be mechanical and early).

---

## After (the first page rebuilt)

> **Abstract.** Multi-view reconstruction methods recover only what at least two
> cameras see: surfaces behind occluders come back as holes or hallucinated blobs,
> because per-primitive optimization has no evidence there and no prior to fall back
> on. We introduce occlusion-aware Gaussian surfels: each surfel carries a visibility
> state inferred per view, and invisible regions are completed by a category-agnostic
> shape prior trained on synthetic occlusion pairs — reconstruction and completion
> share one representation and are optimized jointly. On [Benchmark-A] and
> [Benchmark-B] under the standard 12-view protocol, our method reduces chamfer error
> in occluded regions by [X]% relative to the strongest splatting baseline at matched
> optimization time, while leaving visible-region accuracy unchanged. Code, the
> synthetic occlusion-pair generator, and evaluation masks will be made publicly
> available.
>
> **Introduction (opening).** A delivery robot mapping a cluttered shelf needs the
> geometry of the cereal box *behind* the jar it can see. Current splatting pipelines
> cannot provide it: primitives are optimized only where photometric evidence exists,
> so occluded surfaces receive no gradient and default to holes. The failure is not
> rendering quality but *evidence allocation* — and it is invisible in standard
> benchmarks, whose evaluation masks exclude occluded regions entirely.
>
> We make occlusion a first-class state rather than an absence...
>
> **Contributions.** (1) A per-view visibility state for Gaussian surfels that
> routes optimization between photometric evidence and a learned prior — removable in
> ablation, with the paper reporting both settings. (2) An occluded-region evaluation
> protocol with released masks for [Benchmark-A/B], under which prior methods'
> occluded-surface error is [Y]× their visible-surface error. (3) Evidence that joint
> optimization beats reconstruct-then-complete pipelines at matched compute, on both
> benchmarks and on [Robotics-Set] without retuning.

**Why this passes the same checks:**

- The capability and its failure mechanism ("no gradient where there is no evidence")
  are stated before any method words — an adjacent-area reviewer can now evaluate the
  story.
- Every number is scoped: benchmark, view protocol, matched optimization time. The
  May rebuttal can defend each sentence by pointing at a table.
- Bullets are falsifiable: a removable mechanism (ablatable), a released protocol
  (checkable), a compute-matched comparison (auditable). "Extensive experiments" has
  disappeared.
- The availability sentence uses the anonymity-era phrasing ICCV 2025 prescribed
  ("will be made publicly available") instead of a lab-identifying repo link
  (`iccv-submission`).
- The concrete opening image (the shelf) replaces the history tour; lineage citations
  move to related work, positioned by mechanism per `iccv-related-work`.

---

## Transfer checklist

When applying this rewrite pattern to a real draft, do these in order:

1. Write the failure-mechanism sentence first; if you cannot, the problem statement —
   not the prose — is what needs work.
2. Attach a scope tuple (dataset, protocol, budget) to every comparative claim.
3. Convert each contribution bullet until it could be proven false by an experiment.
4. Replace the opening history paragraph with one concrete instance of the failure.
5. Re-run the generalist test: someone outside the subfield reads page 1 and states
   the idea back. Their sentence is your calibration.
