> **Illustrative teaching example.** The paper, method, setting, and every number below are
> **fictional** and exist only to demonstrate AISTATS house style. No real-paper facts, datasets, or
> results are stated, and no policy is invented. Corresponding skills:
> [`aistats-writing-style`](../../skills/aistats-writing-style/SKILL.md),
> [`aistats-topic-selection`](../../skills/aistats-topic-selection/SKILL.md), and
> [`aistats-experiments`](../../skills/aistats-experiments/SKILL.md).

# Worked Example: An AISTATS-Style Abstract + Introduction (before → after)

This demonstrates the **AISTATS first-page arc** from `aistats-writing-style`:
**problem → gap (why existing methods are insufficient) → method or theorem → evidence →
why it matters at the AI/statistics intersection** — with the AISTATS rules that the contribution sits
**on the first page**, **assumptions are explicit**, and **every major claim is paired with proof
structure, simulation design, an empirical table, or a reproducibility detail** (no overclaiming when
variance is unreported).

The framing also reflects `aistats-topic-selection`: AISTATS is strongest when **statistical reasoning is
not merely an evaluation detail** — here, calibrated uncertainty with a finite-sample guarantee is the
contribution, not a deep-learning system win (which would route to ICML/NeurIPS/ICLR).

**Illustrative paper (fictional):** *"Finite-Sample Calibrated Posteriors for Heteroscedastic Regression
via Conformal Variational Inference."* Fictional method: a variational scheme whose predictive intervals
carry a distribution-free coverage guarantee.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Deep learning has achieved remarkable success across many domains. In this work we study
> uncertainty quantification, which is an important problem. We propose a new neural network method that
> combines variational inference with a calibration step and achieves strong performance on several
> benchmarks, outperforming prior methods in most settings.
>
> **Introduction.** Uncertainty quantification has been studied extensively. Many approaches exist,
> including Bayesian neural networks, ensembles, and dropout. In this paper, we use a variational
> autoencoder-style architecture with an additional calibration module, trained end-to-end, to produce
> predictive intervals. We evaluate on standard datasets and show our method works well. Section 2
> reviews related work, Section 3 describes our method, Section 4 presents experiments, and Section 5
> concludes.

**What's wrong (against `aistats-writing-style` / `aistats-topic-selection` / `aistats-experiments`):**

- **No statistical contribution on the first page** — leads with "deep learning success," not the
  problem/gap/guarantee. AISTATS wants the AI-statistics contribution in the first page.
- **Assumptions are hidden** — no data-generating, distributional, or exchangeability assumption is
  stated, the exact failure AISTATS reviewers flag.
- **Overclaims** ("outperforming prior methods in most settings," "works well") with **no uncertainty
  reported** — variance, repeated runs, or paired tests absent (`aistats-experiments`).
- **No claim → evidence pairing**: "strong performance" is not tied to a guarantee, a simulation design,
  or a table.
- **Venue-misfit framing**: pitched as a deep-learning systems win (an ICML/NeurIPS/ICLR contribution),
  not as statistical novelty — the `aistats-topic-selection` re-route signal.
- **Over-signposted roadmap** standing in for an argument.

---

## After (AISTATS arc — problem → gap → guarantee → evidence → why it matters)

> **Abstract.** Variational predictive intervals for heteroscedastic regression are fast but
> **miscalibrated**: their nominal credible level rarely matches realized coverage, and existing
> calibration fixes either assume a correct likelihood or lose coverage under distribution shift. We
> introduce **conformal variational inference (CVI)**, which post-processes any variational posterior so
> that its predictive intervals attain **distribution-free, finite-sample marginal coverage at level
> 1 − α**, under only the assumption that calibration and test points are **exchangeable**. We prove the
> coverage bound and a matching upper bound showing intervals are not conservative by more than
> O(1/n_cal). On synthetic heteroscedastic designs where ground-truth coverage is known, CVI attains
> nominal coverage while the uncalibrated variational baseline under-covers; on real regression tasks it
> matches baseline interval width at the target coverage. We report coverage and width with standard
> errors over 20 seeds. *(problem → gap → method → guarantee → evidence → uncertainty reported — all on
> the first page.)*
>
> **Introduction.** *(¶1 — problem + contribution, first breath.)* Predictive uncertainty is only useful
> if it is **calibrated**: a 90% interval should contain the truth 90% of the time. Variational inference
> gives cheap predictive intervals for heteroscedastic regression, but their coverage is governed by an
> approximate posterior and is typically **wrong by an unknown amount**. We give a method, **conformal
> variational inference**, that wraps any such posterior and returns intervals with a **finite-sample,
> distribution-free coverage guarantee**.
>
> *(¶2 — gap: why existing methods are insufficient.)* Existing remedies are insufficient for distinct,
> nameable reasons. Bayesian calibration sharpens the posterior but inherits **likelihood
> misspecification**, so its coverage claim is asymptotic and model-dependent. Temperature/recalibration
> scaling targets **average** calibration and can still mis-cover in the tails that matter for decisions.
> Standard conformal prediction is distribution-free but, applied to a point predictor, **discards the
> input-dependent variance** that a variational model already estimates — wasting the heteroscedastic
> signal. *(each prior line gets a specific failure, not a vague "prior work is limited.")*
>
> *(¶3 — method + the explicit assumption.)* CVI uses the variational posterior's predictive standard
> deviation as a **conformity score normalizer**, then calibrates the interval radius on a held-out
> calibration set. The **only** assumption is **exchangeability** of calibration and test points; we make
> no claim that the variational likelihood is correct. *(assumption stated plainly, per the AISTATS rule
> that hidden distributional assumptions are review risk.)*
>
> *(¶4 — guarantee + evidence, each claim paired.)* We prove CVI intervals satisfy
> P(Y ∈ Ĉ(X)) ≥ 1 − α for any α (Theorem 1, proof in App. A), with an upper bound 1 − α + O(1/n_cal)
> ruling out trivial over-coverage (Theorem 2). Empirically, on synthetic heteroscedastic designs where
> true coverage is computable, CVI hits nominal coverage while the uncalibrated baseline under-covers by
> a visible margin (Fig. 1; Table 1); on real tasks it holds coverage at no width cost versus the
> baseline at matched coverage. **All numbers are reported with standard errors over 20 seeds**, and the
> calibration/test split, score, and α grid are in App. B. *(every claim → theorem, figure, table, or
> reproducibility location.)*
>
> *(¶5 — why it matters at the AI/statistics intersection + roadmap.)* The contribution is to make a
> **fast approximate-Bayesian method carry an exact frequentist guarantee** without assuming the model
> is correct — bridging variational scalability and conformal validity. Section 2 states the assumptions
> and method; Section 3 proves the coverage bounds; Section 4 reports the synthetic and real experiments.
> *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the AISTATS bar

Mapped to the skill checklists:

- **Contribution on the first page** — the abstract and ¶1 state the problem, the gap, the method, and
  the guarantee before any architecture detail (`aistats-writing-style`: "Put the AI/statistics
  contribution in the first page").
- **Assumptions explicit** — exchangeability is named as the *only* assumption, and the paper
  *disclaims* likelihood correctness (`aistats-writing-style`: reviewers are sensitive to hidden
  distributional/asymptotic assumptions).
- **Every claim paired with evidence** — coverage → Theorem 1/App. A; non-conservativeness → Theorem 2;
  empirical coverage → Fig. 1/Table 1; reproducibility → App. B (`aistats-writing-style` and
  `aistats-experiments` claim→evidence map).
- **No overclaiming** — "matches baseline width at target coverage" with **standard errors over 20
  seeds**, not "outperforms in most settings"; uncertainty is reported (`aistats-experiments`:
  "Avoid overclaiming when differences are small or variance is unreported").
- **Synthetic vs. real separated** — synthetic designs *validate the coverage assumption* where truth is
  known; real tasks *show practical relevance* (`aistats-experiments`: separate simulations that validate
  assumptions from real-data experiments).
- **Right venue** — the contribution is a **statistical guarantee** (finite-sample, distribution-free
  coverage), not a systems/scaling result, so it is a strong AISTATS fit rather than an ICML/NeurIPS
  re-route (`aistats-topic-selection` fit test).
- **8-page discipline** — proofs and the full experimental protocol are pushed to the appendix while the
  body stays intelligible (`aistats-writing-style`: use the 8-page body for core logic).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified AISTATS papers**
> (PMLR proceedings) whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for AISTATS-specific submission policy.
