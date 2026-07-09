> **Illustrative teaching example.** The paper, method, array geometry, and every number below
> are **fictional** and exist only to demonstrate ICASSP house style. No real-paper facts,
> datasets, or results are stated, and no policy is invented. A non-speech example is used on
> purpose, to show that the ICASSP first-page arc is a *signal-processing* pattern, not a speech
> pattern. Corresponding skills:
> [`icassp-writing-style`](../../skills/icassp-writing-style/SKILL.md),
> [`icassp-topic-selection`](../../skills/icassp-topic-selection/SKILL.md), and
> [`icassp-experiments`](../../skills/icassp-experiments/SKILL.md).

# Worked Example: An ICASSP-Style Abstract + Introduction (before → after)

This shows the **ICASSP first-page arc**: **signal problem → why current methods break → the
mechanism you change → the task-matched number that proves it → why an SPS reviewer should
care** — all inside the space a 4-page IEEE paper can afford. ICASSP is single-blind, so the
author block is present; the discipline is compression and measurement, not anonymity.

**Illustrative paper (fictional):** *"A Model-Based Neural Beamformer for Direction-of-Arrival
Estimation Under Array Gain-Phase Errors."* Fictional method: a small network that refines a
classical subspace DOA estimate using a differentiable array-manifold model.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Deep learning has transformed many fields. Direction-of-arrival estimation is an
> important problem in array signal processing. We propose a new neural network that estimates
> directions of arrival and achieves excellent results on simulated data, outperforming classical
> methods in most of our experiments.
>
> **Introduction.** Array processing has been studied for decades, and many methods exist,
> including MUSIC and ESPRIT. Recently deep learning has become popular. In this paper we train a
> neural network to estimate directions of arrival. We test it on simulations and show it works
> well. Section 2 reviews related work, Section 3 presents the method, Section 4 gives
> experiments, and Section 5 concludes.

**What's wrong (against the ICASSP skills):**

- **No signal-processing contribution on the first page** — leads with "deep learning has
  transformed many fields," not the array problem or what breaks.
- **No mechanism** — "a neural network" is not a contribution; the reader cannot tell what part
  of the estimation chain changed.
- **Metric is vague and possibly wrong** — "excellent results," "outperforming in most
  experiments," with no RMSE, no SNR sweep, no Cramér-Rao reference.
- **Generic-ML smell** — a paper that could be about anything routes to a generic ML venue, not
  to ICASSP's array-processing reviewers (`icassp-topic-selection`).
- **Over-signposted roadmap** substituting for an argument.

---

## After (ICASSP arc — problem → gap → mechanism → measurement → why it matters)

> **Abstract.** Subspace direction-of-arrival (DOA) estimators such as MUSIC attain near-optimal
> accuracy under a *known* array manifold, but degrade sharply when real arrays carry unknown
> **gain and phase errors** across elements. Purely data-driven networks fix this only by
> memorizing one array's imperfections and fail to transfer. We introduce a **model-based neural
> beamformer** that keeps the classical steering-vector model differentiable and learns a small
> correction to the array manifold, so the subspace estimate is refined rather than replaced. On
> simulated uniform linear arrays with gain-phase errors drawn from a controlled distribution, the
> method reduces angular RMSE relative to MUSIC and to a black-box network across a 0-20 dB SNR
> sweep, and stays within a bounded gap of the Cramér-Rao bound at high SNR. Code, array
> configurations, and seeds are released. *(problem → gap → mechanism → task-matched metric →
> reproducibility, all on page one.)*
>
> **Introduction.** *(¶1 — the signal problem and the contribution, first breath.)* Estimating the
> directions of arrival of narrowband sources from a sensor array is a foundational array-processing
> task, and subspace methods are the standard tool. Their guarantees, however, assume the array
> **manifold is known exactly**; on hardware with per-element gain and phase errors, the assumed
> steering vectors are wrong and resolution collapses. We present a method that **corrects the
> manifold model** with a small learned term instead of discarding the model, recovering subspace
> accuracy on imperfect arrays.
>
> *(¶2 — gap: why existing methods are insufficient, each with a named reason.)* Calibration
> methods estimate the errors offline but assume access to known-direction pilots the deployment
> may not provide. Robust-MUSIC variants widen assumptions but pay a resolution cost that grows with
> error magnitude. Black-box DOA networks learn the mapping end-to-end but **entangle the errors of
> the specific training array** with the estimation rule, so a network trained on one array
> transfers poorly to another. *(each prior line gets a specific failure, not a vague "prior work
> is limited.")*
>
> *(¶3 — the mechanism and its assumption.)* Our estimator keeps the physics: the steering vector
> remains a differentiable function of angle and a **learned per-element gain-phase correction**,
> and the DOA is read from the corrected subspace. The only modeling assumption is that the
> correction is **frequency-flat across the narrowband** of interest; we state where that holds and
> where it would not. *(mechanism stated so a reader could reimplement it.)*
>
> *(¶4 — measurement, each claim paired.)* We evaluate on simulated uniform linear arrays with
> gain-phase errors from a controlled distribution, reporting **angular RMSE versus SNR** from
> 0 to 20 dB over many trials (Fig. 2), a **resolution test** on two closely spaced sources
> (Table 1), and the gap to the **Cramér-Rao bound** at high SNR (Fig. 3). Every curve is a mean
> over seeded Monte-Carlo runs with its spread shown, and the array configurations and seeds are in
> the released package. *(every claim → a figure, table, or theoretical reference.)*
>
> *(¶5 — why it matters to SPS reviewers + roadmap.)* The contribution is to make a data-driven
> refinement **inherit the interpretability and near-optimality of the subspace model** while
> tolerating real hardware errors — a model-based-deep-learning result aimed squarely at array
> processing. Section 2 states the signal and error model; Section 3 derives the corrected
> estimator; Section 4 reports the RMSE, resolution, and Cramér-Rao comparisons. *(brief roadmap,
> no over-signposting.)*

---

## Why the "after" meets the ICASSP bar

- **Contribution on page one** — the abstract and ¶1 give the array problem, the gap, the
  mechanism, and the metric before any training detail (`icassp-writing-style`).
- **Mechanism, not "a neural network"** — the paper names exactly what it changes (a learned
  correction inside a differentiable manifold model), so a reviewer can judge novelty in four
  pages (`icassp-writing-style`, `icassp-topic-selection`).
- **Task-matched measurement** — angular RMSE, a resolution test, and the Cramér-Rao bound are
  the *right* rulers for DOA; "outperforms in most experiments" is replaced by an SNR sweep with
  spread (`icassp-experiments`).
- **Right venue** — the result is an array-signal-processing contribution with a physical model,
  a strong ICASSP fit rather than a generic-ML re-route (`icassp-topic-selection`).
- **4-page discipline** — the derivation spine stays in the body; extended error-distribution
  studies and additional geometries go to released material, since ICASSP has no reviewed appendix
  (`icassp-writing-style`, `icassp-supplementary`).
- **Reproducibility on page one** — code, array configurations, and seeds are promised up front,
  and single-blind review means they can be public immediately (`icassp-reproducibility`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, dblp-verified ICASSP
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for ICASSP submission policy.
