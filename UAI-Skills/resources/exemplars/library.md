# UAI Exemplars Library (topic × method)

> **Verified 2026-07-08.** Every row below was confirmed against PMLR — either the
> volume landing page (`proceedings.mlr.press/v.../...`) or the machine-readable paper
> metadata in the corresponding `github.com/mlresearch/v...` repository (titles,
> authors, and page ranges quoted from those records). Each cited volume was separately
> confirmed to be a **Conference on Uncertainty in Artificial Intelligence** edition:
> v161 = UAI 2021, v216 = UAI 2023, v244 = UAI 2024.
>
> **Sibling-volume trap:** UAI, AISTATS, ICML, and COLT all publish through PMLR, so a
> PMLR URL alone proves nothing about the venue. Check the volume's own title line
> ("Conference on Uncertainty in Artificial Intelligence") before attributing a paper
> to UAI. Pre-PMLR UAI papers (roughly pre-2020 editions) live in AUAI Press
> proceedings and must not be given invented PMLR volume numbers.
>
> **Zero-hallucination rule:** this library provides design positioning only. It states
> no result numbers, no theorem constants, and no claims beyond what the metadata
> records. Read the paper on PMLR before citing anything from it. If you add a row and
> cannot verify it live, mark it 待核实 with no attribution.

---

## How to use this library

Find the row nearest your project's topic × method cell, then study how that paper
makes **uncertainty itself the contribution** — a posterior, a guarantee, a graph, a
calibration property — which is the fit bar in
[`../../skills/uai-topic-selection/SKILL.md`](../../skills/uai-topic-selection/SKILL.md).
Pair each exemplar with the corresponding evidence discipline in
[`../../skills/uai-experiments/SKILL.md`](../../skills/uai-experiments/SKILL.md) and the
framing rules in
[`../../skills/uai-writing-style/SKILL.md`](../../skills/uai-writing-style/SKILL.md).

---

## Verified exemplars

### Monte Carlo foundations for variational models

- **Ruiz, Titsias, Cemgil & Doucet, "Unbiased gradient estimation for variational
  auto-encoders using coupled Markov chains," UAI 2021, PMLR v161:707–717**
  (`proceedings.mlr.press/v161/ruiz21a.html`; metadata verified in `mlresearch/v161`).
  - **Why an exemplar:** attacks the estimator itself — unbiasedness of ML gradient
    estimation for VAEs via coupled chains — so the contribution is an inference
    primitive, not an architecture. Classic UAI shape: a Monte Carlo idea with a
    provable property.
  - **Self-check:** is your contribution a property of the estimator (unbiasedness,
    variance, coupling) that you can state and verify, independent of any one model?

### Calibration meets causal effect estimation

- **Deshpande & Kuleshov, "Calibrated and Conformal Propensity Scores for Causal
  Effect Estimation," UAI 2024, PMLR v244:1083–1111**
  (`proceedings.mlr.press/v244/deshpande24a.html`; metadata verified in
  `mlresearch/v244`).
  - **Why an exemplar:** joins two UAI lanes — calibration and causal inference — by
    making a calibration property of the propensity model do causal work. The bridge
    between uncertainty quality and identification-adjacent estimation is a
    distinctively UAI move.
  - **Self-check:** does your uncertainty property provably feed a downstream causal or
    decision quantity, or does it merely coexist with one?

### Conformal prediction machinery

- **Colombo, "Normalizing Flows for Conformal Regression," UAI 2024, PMLR v244:881–893**
  (`proceedings.mlr.press/v244/colombo24a.html`; metadata verified in
  `mlresearch/v244`).
  - **Why an exemplar:** upgrades the calibration step of conformal regression by
    learning it, keeping the distribution-free promise while localizing intervals — an
    interval-validity contribution, evaluated as such.
  - **Self-check:** if your method modifies a conformal pipeline, do you show what
    happens to coverage — marginal and conditional — rather than only interval width?

### Causal discovery beyond a single dataset

- **Günther, Ninad & Runge, "Causal discovery for time series from multiple datasets
  with latent contexts," UAI 2023, PMLR v216:766–776**
  (`proceedings.mlr.press/v216/gunther23a.html`).
  - **Why an exemplar:** widens structure learning to pooled time-series datasets with
    latent context variables — an assumptions-and-identifiability contribution where
    the graph class and the data regime are stated up front.
  - **Self-check:** can you name the graph class, the observation regime, and the
    assumption set in one sentence each, the way discovery papers here must?

### Bayesian deep learning, judged as inference

- **Mohan & Scaife, "Evaluating Bayesian deep learning for radio galaxy
  classification," UAI 2024, PMLR v244:2587–2597**
  (`proceedings.mlr.press/v244/mohan24a.html`; metadata verified in `mlresearch/v244`,
  including a public software link and an OpenReview ID — evidence of the venue's
  code-release norm in practice).
  - **Why an exemplar:** an applications paper that survives UAI review by evaluating
    BNNs on inference criteria — predictive performance, uncertainty calibration, and
    shift detection — rather than accuracy alone.
  - **Self-check:** if your paper is an application, are calibration and shift behavior
    measured as primary endpoints, with code released?

---

## Topic × method index

| Topic | Verified UAI exemplar | Edition / PMLR | Method family |
| --- | --- | --- | --- |
| Gradient estimation for deep generative models | Ruiz et al. | 2021 / v161:707–717 | Coupled MCMC |
| Causal effects with calibrated nuisances | Deshpande & Kuleshov | 2024 / v244:1083–1111 | Calibration + conformal + propensity |
| Distribution-free intervals | Colombo | 2024 / v244:881–893 | Conformal + normalizing flows |
| Structure learning, time series | Günther, Ninad & Runge | 2023 / v216:766–776 | Constraint-based discovery, latent contexts |
| Applied Bayesian deep learning | Mohan & Scaife | 2024 / v244:2587–2597 | BNN evaluation: calibration + shift |

Five verified rows across five distinct lanes (Monte Carlo, causal estimation,
conformal, discovery, applied BDL). Note what the set demonstrates jointly: every row
attaches a checkable uncertainty property to its method — the pack's recurring theme.

---

## Adding rows without hallucinating

1. Locate the paper on `proceedings.mlr.press` and confirm the volume's title line
   names the Conference on Uncertainty in Artificial Intelligence.
2. Prefer quoting title/authors/pages from the `mlresearch/v<N>` GitHub metadata file,
   which is the typeset record.
3. Record the edition ↔ volume pair against the anchor list in
   [`../official-source-map.md`](../official-source-map.md) (v124=2020, v161=2021,
   v180=2022, v216=2023, v244=2024, v286=2025).
4. For pre-PMLR classics (the venue dates to the 1980s), cite AUAI Press / the original
   proceedings and verify via DBLP — never guess a PMLR volume.
5. When verification fails, omit the row or mark it 待核实 with no author attribution.
