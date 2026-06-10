---
name: joe-replication-and-data-policy
description: Use to prepare code and data materials for a Journal of Econometrics (JoE) submission under Elsevier's data-citation and availability norms, including reproducible Monte Carlo and the [dataset] reference tag. Reflects that JoE has no mandatory central replication archive — replication is encouraged, not universally mandated.
---

# Replication & Data Policy (joe-replication-and-data-policy)

## When to trigger

- You are assembling the code/data materials for a JoE submission or revision
- You need to know whether a mandatory replication package is required (it is not, as far as verified)
- You are citing a dataset and need the correct Elsevier format
- Your Monte Carlo or empirical illustration must be made reproducible for referees

## What JoE actually requires (and does not)

The *Journal of Econometrics* applies **Elsevier's research-data policy**: authors are **encouraged** to cite underlying datasets and to support a **data availability statement**. Crucially, JoE has **not** historically operated a **mandatory, centrally-enforced public code/data archive** for all empirical papers — unlike the *Journal of Applied Econometrics* (JAE Data Archive) or Econometric Society journals (replication packages vetted by a Data Editor). For JoE, replication materials for applied **illustrations** are **encouraged rather than universally mandated**. (待核实: this characterization is inferred from the absence of a stated mandate plus secondary summaries; confirm against an explicit official replication-policy statement before relying on it.)

Because JoE is a **methodology** journal, the reproducibility center of gravity is the **Monte Carlo and the estimator code**, not a large administrative-data archive. Make the *method* runnable.

## Data citation (Elsevier `[dataset]`)

- Cite relevant/underlying datasets in the text **and** in the reference list, tagged **`[dataset]`**.
- Elements: **author(s), dataset title, repository, version, year, persistent identifier (DOI)**.
- Include a **data availability statement** describing access conditions for any real data used in the illustration. (待核实: confirm the exact current requirements on the live Guide for Authors.)

## Reproducible methodology package (best practice)

- **Estimator as a usable artifact:** ship the new estimator/test as a documented function or command (R/Stata/Python/MATLAB/Julia) with a minimal worked example so referees can run it.
- **`run_all` master script** that regenerates **every Monte Carlo table, every theory figure, and the empirical illustration** from raw inputs.
- **Pin versions and seeds:** `renv.lock` / `requirements.txt` / recorded `ssc` versions / `Project.toml`; fix and report random seeds and replication counts so simulations reproduce exactly.
- **Archive on a stable repository** (e.g., Zenodo, openICPSR) even though JoE does not mandate a central archive — it pre-empts referee replication requests and supports the optional **Data in Brief / MethodsX** co-submission route. (待核实: co-submission is via Editorial Manager per the Elsevier guide.)

## Anti-patterns

- Assuming a mandatory, Data-Editor-vetted package like the Econometric Society journals — JoE does not enforce one (待核实)
- Citing a dataset only in prose, without the `[dataset]` reference-list entry
- Unreproducible Monte Carlo (unreported seeds, package versions, or replication counts)
- Shipping results but not the estimator, so referees cannot actually run the method


## Reproducibility pass for Journal of Econometrics

Use this as a second-pass capability check. First lock the estimand or theorem, assumptions, asymptotic/simulation evidence, and applied relevance; then test whether the manuscript addresses econometrics reviewers who expect methodological novelty, assumptions, simulation or empirical illustration, and reproducibility.

- **Primary move:** Name data, code, environment, disclosure limits, and archive/deposit route; unresolved proprietary or ethics barriers must be explicit.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Econometric Theory for proof-first work, JBES for applied statistical methods, Quantitative Economics for economics-theory methods; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Data citation】[dataset] entries with DOI/version? [Y/N]
【Availability statement】access conditions stated? [Y/N]
【Estimator artifact】documented, runnable, worked example? [Y/N]
【run_all】regenerates all MC tables + figures + illustration? [Y/N]
【Reproducibility】seeds + versions + reps pinned? [Y/N]
【Archive】staged on stable repo (optional but recommended)? [Y/N]
【Next step】joe-review-process
```
