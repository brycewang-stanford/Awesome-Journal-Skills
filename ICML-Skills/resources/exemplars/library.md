# ICML Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared at **ICML — the International Conference on Machine Learning** — in the cited year,
> by locating its page in *Proceedings of Machine Learning Research* (PMLR, `proceedings.mlr.press`),
> where each ICML proceedings volume is published. PMLR volume → ICML year mapping used here:
> **v37 = ICML 2015**, **v70 = ICML 2017**, **v80 = ICML 2018**, **v119 = ICML 2020**. Papers that
> could not be confirmed as **ICML** specifically were **omitted** — this is deliberately a short,
> clean, verified list rather than a long, uncertain one.
>
> **Sibling-venue guard (do NOT confuse ICML with):** NeurIPS, ICLR, CVPR, AAAI, JMLR, UAI, AISTATS,
> COLT. Many landmark ML papers people *assume* are "ICML" are not — e.g. most Transformer and
> diffusion-model variants premiered at **NeurIPS or ICLR**, not ICML. Every entry below was checked
> against its PMLR/ICML proceedings page, not against memory.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent reported metrics — read the original PMLR PDF before citing any number. For
> ICML-specific policy, scope, and submission facts, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × problem** is closest to yours, then study how that paper makes a
*rigorous, evaluable* ML contribution legible inside ICML's tight format — the ICML bar of
**soundness, originality, significance, clarity, reproducibility** (see
[`../../skills/icml-topic-selection/SKILL.md`](../../skills/icml-topic-selection/SKILL.md),
[`../../skills/icml-writing-style/SKILL.md`](../../skills/icml-writing-style/SKILL.md), and
[`../../skills/icml-experiments/SKILL.md`](../../skills/icml-experiments/SKILL.md)). For each, ask the
self-check question before claiming your paper is "ICML-shaped."

---

## By method

### Normalization / optimization for deep nets (training method)

- **Ioffe & Szegedy, "Batch Normalization: Accelerating Deep Network Training by Reducing Internal
  Covariate Shift," ICML 2015, PMLR 37:448–456.**
  Verified: `proceedings.mlr.press/v37/ioffe15.html` (PMLR v37 = ICML 2015).
  - **Why it is an exemplar:** isolates one precise training pathology (shifting layer-input
    distributions), proposes a single drop-in mechanism, and backs it with controlled training-curve
    evidence — the canonical "small architectural change, large, well-measured effect" ICML method
    paper.
  - **Self-check:** does your method target one named mechanism, and can a reviewer see the gain under
    a fair, matched-compute comparison rather than a leaderboard win?

### Generative modeling with a theory-grounded objective (generative models)

- **Arjovsky, Chintala & Bottou, "Wasserstein Generative Adversarial Networks," ICML 2017,
  PMLR 70:214–223.**
  Verified: `proceedings.mlr.press/v70/arjovsky17a.html` (PMLR v70 = ICML 2017).
  - **Why it is an exemplar:** motivates a new GAN objective from the geometry of the Wasserstein
    distance, ties an analytic argument to a concrete training-stability claim, and shows the loss
    tracks sample quality — theory and method advancing together, an ICML strength.
  - **Self-check:** does your objective follow from a stated mathematical property, and do you show
    the property translates into a measurable training or sample-quality benefit?

### Meta-learning / fast adaptation (learning-to-learn method)

- **Finn, Abbeel & Levine, "Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks,"
  ICML 2017, PMLR 70:1126–1135.**
  Verified: `proceedings.mlr.press/v70/finn17a.html` (PMLR v70 = ICML 2017).
  - **Why it is an exemplar:** one model-agnostic idea (optimize for parameters that adapt in a few
    gradient steps) stated generally, then demonstrated across classification, regression, and RL —
    breadth of applicability shown, not just asserted.
  - **Self-check:** is your contribution stated at the right level of generality, and do you show it
    holds across more than one task family rather than a single benchmark?

### Interpretability / model understanding (analysis method)

- **Koh & Liang, "Understanding Black-box Predictions via Influence Functions," ICML 2017,
  PMLR 70:1885–1894.** (ICML 2017 Best Paper.)
  Verified: `proceedings.mlr.press/v70/koh17a.html` (PMLR v70 = ICML 2017).
  - **Why it is an exemplar:** brings a classical statistical tool (influence functions) to modern
    deep models, with an efficient implementation and honest treatment of where the theory's
    assumptions break — rigor plus candor about limits, the ICML soundness posture.
  - **Self-check:** does your analysis method come with a clear assumption set, and do you report what
    happens when those assumptions are violated rather than hide it?

### Deep reinforcement learning algorithm (RL method)

- **Haarnoja, Zhou, Abbeel & Levine, "Soft Actor-Critic: Off-Policy Maximum Entropy Deep
  Reinforcement Learning with a Stochastic Actor," ICML 2018, PMLR 80:1856–1865.**
  Verified: `proceedings.mlr.press/v80/haarnoja18b.html` (PMLR v80 = ICML 2018).
  - **Why it is an exemplar:** derives an algorithm from the maximum-entropy RL framework, then
    targets the two failure modes practitioners actually hit (sample complexity and brittle
    convergence), with multi-seed continuous-control evidence — principled motivation meeting an
    honest experimental audit.
  - **Self-check:** does your algorithm follow from a stated objective, and do your RL results report
    seed variance rather than a single lucky run?

### Self-supervised representation learning (empirical study / method)

- **Chen, Kornblith, Norouzi & Hinton, "A Simple Framework for Contrastive Learning of Visual
  Representations," ICML 2020, PMLR 119:1597–1607.**
  Verified: `proceedings.mlr.press/v119/chen20j.html` (PMLR v119 = ICML 2020).
  - **Why it is an exemplar:** strips a crowded area down to a simple framework and uses systematic
    ablations (augmentation composition, projection head, batch size) to attribute the gains —
    showing *why* it works, the kind of careful empirical study ICML rewards.
  - **Self-check:** if your contribution is empirical, do ablations isolate which design choices drive
    the result, so the finding is mechanistic rather than a tuned leaderboard number?

---

## By topic (each cell is a verified ICML paper above)

| Topic | Verified ICML exemplar | ICML year / PMLR vol:pp | Method |
| --- | --- | --- | --- |
| Deep-net training / optimization | Ioffe & Szegedy, "Batch Normalization" | 2015, v37:448–456 | Normalization layer |
| Generative models | Arjovsky, Chintala & Bottou, "Wasserstein GAN" | 2017, v70:214–223 | Theory-grounded GAN objective |
| Meta-learning | Finn, Abbeel & Levine, "MAML" | 2017, v70:1126–1135 | Gradient-based meta-learning |
| Interpretability | Koh & Liang, "Influence Functions" | 2017, v70:1885–1894 | Influence-function analysis |
| Reinforcement learning | Haarnoja et al., "Soft Actor-Critic" | 2018, v80:1856–1865 | Max-entropy off-policy RL |
| Self-supervised learning | Chen et al., "SimCLR" | 2020, v119:1597–1607 | Contrastive representation learning |

---

## Omitted for lack of ICML-specific verification (do not attribute to ICML without re-checking)

To keep the list zero-hallucination, candidates were **excluded** unless their ICML/PMLR proceedings
page was located. Common sibling-venue confusions to guard against:

- **"Attention Is All You Need" (Transformers), Vaswani et al. 2017** — appeared at **NeurIPS 2017**,
  **not ICML**. Listed here only as a guardrail.
- **"Denoising Diffusion Probabilistic Models" (DDPM), Ho et al. 2020** — appeared at **NeurIPS
  2020**, **not ICML**. Many diffusion variants are NeurIPS/ICLR, not ICML.
- **"Adam: A Method for Stochastic Optimization," Kingma & Ba 2015** — appeared at **ICLR 2015**,
  **not ICML**.
- **"On Calibration of Modern Neural Networks," Guo, Pleiss, Sun & Weinberger** — *was* verified at
  **ICML 2017, PMLR 70:1321–1330** (`proceedings.mlr.press/v70/guo17a.html`); omitted from the six
  core rows only to avoid over-clustering the library on ICML 2017. It is a legitimate ICML exemplar
  for **uncertainty / calibration** and may be promoted into the table when broadening coverage.

Before adding any new paper to this library, confirm it on `proceedings.mlr.press` (the ICML
proceedings volume for that year, with page range) — **not** NeurIPS/ICLR/CVPR/AAAI/JMLR/UAI — and
update the access-date header. When in doubt, omit.
