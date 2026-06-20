---
name: mathfin-replication-and-data-policy
description: Use when preparing Wiley data availability statements and reproducibility notes for a Mathematical Finance manuscript — covers the no-data case typical of this theory venue, archives for illustrative numerical code, per-exhibit provenance, and what a proofs journal does and does not require of authors.
---

# Replication & Data Policy (mathfin-replication-and-data-policy)

## When to trigger

- The manuscript needs a Data Availability Statement
- Numerical experiments, simulations, or code accompany the theory
- The paper uses no data and you need the correct statement

## Policy stance

Wiley policy expects all research- and synthesis-based articles to include a
Data Availability Statement. For this journal, that often means using Wiley's
theory/no-new-data template. There is no journal-specific mandatory replication
archive comparable to empirical economics/finance data archives, but code for
numerical illustrations should be reproducible when included.

## Statement templates

### No data

```text
Data availability statement: Data sharing is not applicable to this article as
no datasets were generated or analysed during the current study.
```

### Numerical code only

```text
Data availability statement: The numerical code used to generate the illustrative
figures/tables is available at [repository/DOI]. No proprietary empirical data
were used.
```

### Public data, if unusually used

```text
Data availability statement: The data are publicly available from [source] at
[URL]. The code used for the numerical analysis is available at [repository/DOI].
```

## Reproducibility checklist

- Set and report random seeds.
- Record software, package, compiler, and LaTeX versions when relevant.
- Include scripts that regenerate each numerical exhibit.
- Make parameter values and discretization choices visible.
- Cite archived code with a DOI when feasible.

## Numerical-experiment package

For a theory paper with figures or numerical tables, package the computation like a proof appendix:

- one entry script that recreates every numerical exhibit;
- a parameter file listing model primitives, grids, tolerances, time steps, and truncation rules;
- output files whose names match manuscript labels;
- a short note explaining expected runtime and any stochastic variation;
- a minimal smoke test with smaller grids so a referee can verify the pipeline quickly.

If no data or code exist, say that explicitly and keep the Data Availability Statement minimal. If code
exists but is not archived, explain why; otherwise the numerical illustration looks less rigorous than the
theorem it supports.

## Exhibit provenance ledger

Keep one ledger row per numerical exhibit and include it in the code archive README:

```text
exhibit: Figure 2 (error decay)
supports: Theorem 4.1 (strong rate 1/2)
script: scripts/fig2_euler_rate.py
seed: 20240117      paths: 10^6      steps: 2^4 ... 2^12
runtime: ~6 min (single core)
expected output: fig2.pdf, slope estimate within ±0.03 of 0.5
```

A referee who can re-run one script and watch the proven rate emerge trusts the rest of the
paper more; a figure with no provenance invites a "please document the experiments" major
comment.

## Boundaries of this venue's policy

- This is a proofs journal: there is no counterpart to the mandatory data-and-code archives of
  empirical finance journals, and nothing here should be padded into one.
- The mathematical core replicates itself — a complete, self-contained proof is the
  "replication package" for the theorems; other skills in this pack own that obligation.
- Wiley-level details (data-availability wording, licensing of supplementary code, any badge
  schemes) change over time; confirm against the journal's current author guidelines before
  final upload rather than relying on cached text.
- If illustrative code touches third-party market data only to choose realistic parameter
  values (volatilities, mean-reversion speeds), cite the source and state that no result
  depends on the data — keeping the paper's status as theory unambiguous.

## Minimal-footprint rule

Archive exactly what regenerates the exhibits and nothing speculative. A sprawling repository
with half-finished calibration notebooks signals an empirical ambition the journal screens
out, and hands referees objections unrelated to the theorems. One entry script, one parameter
file, deterministic seeds, matching output names — then stop.

## Output format

```text
[Data status] no data / numerical code / public data / other
[Statement] ...
[Code archive] ...
[Missing reproducibility details] ...
[Next step] mathfin-submission
```
