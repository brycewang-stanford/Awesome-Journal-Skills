---
name: ijoc-data-analysis
description: Use when running and reporting the computational experiments — and assembling the reproducible code/data deposit — for an INFORMS Journal on Computing (IJOC) manuscript. Turns a designed protocol (see ijoc-methods) into defensible, reproducible results; it does not redesign the experiment.
---

# Computational Experiments & Reproducibility (ijoc-data-analysis)

## When to trigger

- The protocol is designed and you are now **running experiments** and interpreting results
- A referee questions whether a performance win is **real** versus tuning, seed luck, or benchmark selection
- You need to turn raw outputs into the **statistical comparison** IJOC expects (not just a table of best times)
- You are assembling the **IJOC GitHub Software and Data Repository** deposit and want it to reproduce the paper

## Making the computational claim defensible

IJOC's distinctive risk is a result that is real on the page but an artifact underneath. Pre-empt the three ways a referee will attack it.

- **Tuning artifact.** Show the win holds with tuning done symmetrically on a disjoint set. Report performance at default *and* tuned for both your method and the baselines, so the gain is not hidden in hyperparameters.
- **Seed/variance artifact.** For any stochastic component, run **multiple seeds** (commonly ≥10) and report mean, dispersion (sd/IQR), and the distribution — a box/violin plot or a table of quartiles — not a single best run. State the seeds; they go in the deposit.
- **Benchmark-selection artifact.** Report on the **full** standard instance set, including instances where you lose or time out; aggregate with a **performance profile** (Dolan–Moré) so the whole picture is visible. Cherry-picking the favorable subset is the fastest way to lose a referee's trust.

## The statistics IJOC reviewers expect

Means and "X is fastest" are not enough. Use the comparisons that suit computational data:

- **Performance profiles** to compare solvers across a whole instance set (fraction solved within a factor of the best).
- **Pairwise nonparametric tests** (Wilcoxon signed-rank for matched instances; sign test) rather than t-tests on heavy-tailed runtimes.
- **Multiple-comparison control** (e.g., Holm/Bonferroni) when comparing several methods at once.
- **Scaling evidence:** runtime/memory vs. instance size on log axes, with the empirical growth compared to the theory from `ijoc-theory-development`.
- **Equal-effort comparisons:** quality at equal time, or time at equal quality — never "ours had more time."

Report optimality gaps with their definition, dual bounds where available, and time limits explicitly (a "solved" count is meaningless without the limit).

## Assembling the IJOC reproducibility deposit

Accepted IJOC papers deposit artifacts in the **INFORMSJoC GitHub organization**, and the deposit is part of the contribution — design it to *reproduce the paper*. Concretely (检索于 2026-06；以官网为准):

- Start from the **template repository** (`github.com/INFORMSJoC/2019.0000`) and replace placeholders with your manuscript ID `XXXX.YYYY`.
- Three root files are required: **`README.md`** (with a `## Cite` section as the first subheading, using DOI `10.1287/ijoc.XXXX.YYYY.cd`), **`LICENSE`**, and **`AUTHORS`**.
- Organize into `src/`, `data/` (with documented provenance), `scripts/` (to replicate experiments), `results/`, `docs/`.
- Pin dependencies (`requirements.txt`, `Manifest.toml`, environment files). A best-faith reproducibility effort is expected even if exact bit-reproduction is not.
- On acceptance, a **tagged snapshot** (`vXXXX.YYYY`) is archived and a **code DOI** (`…​.cd`) is minted alongside the article DOI — so the deposited state must match the published results.

The README's replication section should let a reader regenerate each table/figure from `scripts/`. If your `results/` directory maps one-to-one to the paper's exhibits, the reproducibility reviewer's job — and yours during the R&R — becomes mechanical.

## Checklist

- [ ] Win shown at default and tuned; tuning symmetric on a disjoint set
- [ ] ≥ multiple seeds for stochastic runs; dispersion and distribution reported; seeds recorded
- [ ] Full standard instance set reported, including losses/timeouts; performance profile shown
- [ ] Nonparametric pairwise test (Wilcoxon) + multiple-comparison control where needed
- [ ] Scaling plot vs. size on log axes; compared to the theoretical complexity
- [ ] Gaps defined; dual bounds and time limits stated
- [ ] Deposit built from the IJOC template: README(+`## Cite`)/LICENSE/AUTHORS; src/data/scripts/results; pinned deps; seeds
- [ ] `results/` maps to the paper's tables/figures; scripts regenerate them

## Anti-patterns

- A single best run reported for a randomized algorithm
- Means and "fastest" with no statistical test or performance profile
- Dropping the instances where the method loses or times out
- Reporting "solved 47/50" without the time limit
- A deposit that is a code dump with no README replication path, or that does not reproduce the published numbers
- Letting the deposited snapshot drift from the accepted results

## Output format

```text
【Journal】INFORMS Journal on Computing
【Skill】ijoc-data-analysis
【Headline result】the computational win, stated with its metric
【Artifact controls】default+tuned / #seeds+dispersion / full instance set
【Statistics】performance profile + Wilcoxon (+ MC control)? [Y/N]
【Scaling vs. theory】[consistent / discrepancy noted]
【Deposit】template/README+Cite/LICENSE/AUTHORS/scripts/seeds ready? [Y/N]
【Next skill】ijoc-contribution-framing
```
