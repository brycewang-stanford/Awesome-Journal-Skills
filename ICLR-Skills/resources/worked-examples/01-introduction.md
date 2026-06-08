> **Illustrative teaching example.** The paper, method, and every number below are **fictional** and
> exist only to demonstrate ICLR house style for an abstract + introduction. No real-paper facts or
> ICLR policy are stated here — for policy see [`../official-source-map.md`](../official-source-map.md).
> Corresponding skills: [`iclr-writing-style`](../../skills/iclr-writing-style/SKILL.md),
> [`iclr-topic-selection`](../../skills/iclr-topic-selection/SKILL.md), and
> [`iclr-experiments`](../../skills/iclr-experiments/SKILL.md).

# Worked Example: An ICLR-Style Abstract + Introduction (before → after)

This demonstrates the **ICLR framing arc** from `iclr-writing-style`:
**ICLR fit (what learning insight) → first-page problem (what is hard or missing) → contribution type
(method / theory / benchmark / analysis / data / systems / application) → empirical evidence the
community can verify → reviewer-navigation path → honest limitation** — written so the paper still
reads well through OpenReview snippets and public discussion, with the **contribution stated on the
first page** and **each claim matched to an experiment** (`iclr-experiments`).

**Illustrative paper (fictional):** *"Slot-Routed Representations: Disentangling Object Identity from
Pose Without Labels."* Fictional setting: a self-supervised representation-learning method evaluated
on synthetic and natural-image probing benchmarks.

---

## Before (buries the idea — typical first-draft abstract + intro)

> Representation learning has received significant attention in recent years. Many architectures have
> been proposed for learning features from images, including autoencoders, contrastive methods, and
> generative models. In this paper, we propose a new architecture that uses a slot-attention module
> followed by a routing transformer with a contrastive objective and an auxiliary reconstruction loss,
> trained with Adam for 800 epochs on four datasets. We run extensive experiments and show that our
> method achieves strong results. We also provide ablations. Section 2 reviews related work, Section 3
> describes our method, Section 4 presents experiments, and Section 5 concludes.

**What's wrong (against `iclr-writing-style` / `iclr-topic-selection` / `iclr-experiments`):**

- **Leads with architecture plumbing** ("slot-attention module followed by a routing transformer...")
  instead of the representation-learning insight — the skill warns against hiding the core idea behind
  implementation detail.
- **No first-page statement of what is learned or why it changes practice.** A reviewer spanning
  another subfield cannot tell what the representation buys them.
- **No contribution type declared** (method? analysis? benchmark?) — `iclr-writing-style` asks for this
  explicitly.
- **"Strong results" with no claim and no verifiable evidence** — `iclr-experiments` requires each
  experiment to map to a stated claim.
- **No reviewer-navigation path** ("what to verify": key ablation, main figure, artifact).
- **No limitation / honest scope**, which `iclr-topic-selection` flags for high-impact model claims.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (ICLR arc — insight + contribution type + verifiable evidence on the first page)

> **Abstract.** Self-supervised image encoders learn features that entangle *what* an object is with
> *how* it is posed, so a small viewpoint change moves the representation as much as a change of object.
> **We show that a single routing constraint — forcing each object slot to be reconstructed from a
> pose-invariant code plus a separate low-dimensional pose code — disentangles identity from pose
> without any labels**, and that this changes a downstream property the community cares about: identity
> retrieval stays stable under viewpoint shift. *(ICLR fit + first-page insight, one sentence.)* On a
> controlled synthetic benchmark our representation cuts identity-retrieval error under held-out
> viewpoints by **31%** relative to the strongest contrastive baseline, and the gain persists on
> natural images. *(headline empirical evidence, with a number and a baseline.)* The contribution is a
> **method plus the analysis that explains why it works**: we isolate the routing constraint in an
> ablation and show identity/pose separation is what drives the downstream gain. *(contribution type
> declared.)*
>
> **Introduction.** Good visual representations should let downstream models recognize an object
> regardless of viewpoint, yet widely used self-supervised encoders fail this: we find that a 30-degree
> rotation displaces the embedding as far as swapping the object entirely. *(first-page problem — what
> is missing, stated as a measured failure, not a slogan.)*
>
> Why is this hard? Without labels, nothing tells the encoder which factors of variation are "identity"
> and which are "nuisance," so contrastive and reconstructive objectives are free to spend capacity on
> pose. *(why it is hard — the learning problem, before any architecture.)*
>
> Our contribution is a **method**: a routing constraint that reconstructs each object slot from a
> pose-invariant identity code and a separate 3-dimensional pose code, trained only with reconstruction
> and a standard contrastive loss — no pose labels, no augmentation tuned to the benchmark. *(contribution
> type stated on the first page, as `iclr-writing-style` asks.)* The constraint is one term; the rest of
> the model is standard, which is deliberate — we want the *mechanism*, not a new architecture, to carry
> the result.
>
> We support one claim with one experiment each. *(the `iclr-experiments` discipline.)* **Claim 1**
> (disentanglement): on synthetic data with ground-truth pose, identity and pose codes are linearly
> decodable from each other at chance level — Figure 2. **Claim 2** (downstream value): identity-retrieval
> error under held-out viewpoints drops 31% versus the strongest contrastive baseline, across five seeds
> with non-overlapping confidence intervals — Table 1. **Claim 3** (mechanism): removing only the routing
> constraint erases 27 of the 31 points, isolating it as the cause — Table 2 ablation.
>
> A reviewer can verify the paper in three steps: read **Figure 2** (disentanglement holds), **Table 1**
> (the gain is real and not single-seed), and the **Table 2 ablation** (the routing term, not capacity,
> causes it); the anonymized artifact reproduces all three with one command. *(reviewer-navigation path —
> "what to verify," per `iclr-writing-style`.)*
>
> We are explicit about scope: the disentanglement guarantee is demonstrated where pose is
> low-dimensional and approximately factorizable; we show degradation as pose dimensionality grows and do
> not claim the method handles articulated or multi-object pose. *(honest limitation tied to a real
> constraint, per `iclr-topic-selection` and `iclr-reproducibility`.)* Section 2 gives the method;
> Section 3 reports the three experiments above; the appendix holds compute, seeds, and failure cases.
> *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the ICLR bar

Mapped to the skill checklists:

- **States the representation insight on the first page** — identity/pose disentanglement without labels,
  legible to a vision, generative-modeling, *or* representation-theory reviewer (`iclr-writing-style`:
  "state the representation, learning problem, or model-behavior insight in the first page").
- **Contribution type declared** — "a method plus the analysis that explains why it works" — instead of
  leaving reviewers to guess (`iclr-writing-style` contribution-type line).
- **Each claim is matched to one experiment** with a number, a named baseline, and multi-seed variance,
  pre-empting "is the baseline tuned fairly?" and "single-seed win?" (`iclr-experiments`,
  `iclr-reproducibility`).
- **Mechanism is isolated by a one-term ablation** ("removing only the routing constraint erases 27 of
  31 points"), answering the predictable "does it win because of more capacity/compute?"
  (`iclr-experiments`).
- **Reviewer-navigation path is explicit** ("read Figure 2, Table 1, the Table 2 ablation; the artifact
  reproduces all three"), which `iclr-writing-style` asks for under public review.
- **Architecture plumbing is demoted to a tool**, mentioned only where the method is described, never as
  the lead (avoids the "hiding the idea behind implementation detail" anti-pattern).
- **Honest, specific limitation** (low-dimensional/factorizable pose; degrades as pose grows), not a
  throwaway, consistent with `iclr-topic-selection`'s "honest limitations for high-impact claims."
- **OpenReview-robust**: the abstract and first paragraph stand alone as a snippet — the insight, the
  number, and the contribution type all survive being read out of context.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified ICLR papers**
> whose abstracts execute this arc, and [`../official-source-map.md`](../official-source-map.md) for the
> ICLR-specific submission and OpenReview policy this example deliberately does **not** invent.
