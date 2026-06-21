---
name: conbio-data-analysis
description: Use when executing and reporting the analysis for a Conservation Biology manuscript so it survives expert, double-blind review — appropriate ecological/statistical models, honest uncertainty, robustness, and reproducibility. Covers detection, hierarchical models, spatial structure, and effect sizes that matter for conservation. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (conbio-data-analysis)

*Conservation Biology* reviewers are methodologically sophisticated, and the journal expects a
**data-availability statement** with data and code deposited at acceptance (see
`conbio-reporting-and-data-policy`). Analyze as if your code will be re-run — because it may be. This
skill covers execution and reporting norms; design decisions live in `conbio-study-design`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, alternative models, or uncertainty
- Reconciling exploratory vs. confirmatory analyses
- Making the analysis reproducible before deposit

## Analysis norms Conservation Biology expects

1. **Report uncertainty honestly.** Confidence/credible intervals, not just stars or p-values; report
   the **magnitude and conservation meaning** of the estimate, not only significance.
2. **Use the right model for the data.** Hierarchical/mixed models for nested data; occupancy and
   N-mixture for detection; capture-recapture for survival/abundance; GLMs/GAMs for nonlinearity;
   account for spatial autocorrelation and zero-inflation where present.
3. **Robustness that probes, not decorates.** Show specifications that could *break* the result
   (alternative predictors, samples, priors, estimators), and say what you learn.
4. **Right inference.** Cluster/group at the correct level; avoid pseudoreplication in the analysis;
   correct for multiple comparisons when testing many implications.
5. **Confirmatory vs. exploratory.** Separate preregistered/confirmatory tests from exploratory ones;
   do not mine for a significant interaction and theorize it post hoc.
6. **Model checking.** Report convergence, residual diagnostics, validation/out-of-sample performance
   for predictive models; show the result is not an artifact of one modeling choice.

## Conservation-specific reporting
- Translate estimates into **decision-relevant quantities** (extinction risk, population trend,
  effect of a management action, area needed) with uncertainty.
- For projections (PVA, SDM, climate), state the assumptions and the range of plausible outcomes —
  not a single point forecast.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for bootstrap, MCMC, simulation, and any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded installs).
- Keep table/figure numbers matched to script outputs.

## Anti-patterns

- Stars/p-values with no effect sizes or intervals
- Raw counts analyzed as abundance with detection ignored
- "Robustness" that only reruns near-identical specs to manufacture stability
- p-hacking / HARKing exploratory results into confirmatory claims
- A single point projection presented as certain
- A results section whose numbers the code cannot reproduce


## Evidence pass for Conservation Biology

Use this as a second-pass capability check. First lock the species/system threat, conservation decision, and uncertainty relevant to action; then test whether the manuscript addresses conservation-science reviewers who ask whether evidence changes biodiversity, management, or policy action.

- **Primary move:** Audit unit, comparison, uncertainty, missingness, sensitivity, and reproducibility before making any prose or submission recommendation.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Biological Conservation for applied conservation breadth, Global Change Biology for climate/ecosystem process, Ecology Letters for theory-forward ecology; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Submission-ready gate:** before final advice, re-open `resources/official-source-map.md` for upload-week rules and name the one live-check item that could change the recommendation.

## Output format

```
【Main estimate】magnitude + interval + conservation meaning
【Model】why this model fits the data (detection / hierarchy / spatial)
【Robustness】specs that could break it → what held
【Confirmatory vs exploratory】clearly separated?
【Uncertainty in projections】range stated, not a point?
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】conbio-figures-and-tables
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — modeling, inference, and synthesis packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data-availability and reproducibility expectations
