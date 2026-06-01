---
name: asr-data-analysis
description: Use when executing and reporting the analysis for an American Sociological Review (ASR) manuscript so it survives expert masked review — honest uncertainty, robustness, and evidence handling appropriate to quantitative, demographic, comparative-historical, or computational sociology. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (asr-data-analysis)

ASR reviewers are methodologically demanding across very different traditions. Whether your evidence
is regression coefficients, life tables, archival sequences, or coded fieldnotes, the analysis must be
transparent, well-documented, and reproducible to the extent your data allow. Design decisions live in
`asr-research-design`.

## When to trigger

- Running main and supporting analyses; building the results/findings section
- A reviewer asked for robustness, heterogeneity, alternative specifications, or more evidence
- Documenting how qualitative claims are grounded in the data
- Making the analysis reproducible before sharing materials

## Analysis norms ASR expects

### Quantitative / demographic
1. **Report uncertainty and magnitude**, not just significance — intervals and substantive effect
   sizes; respect survey design (weights, clustering).
2. **Robustness that probes, not decorates** — alternative measures, samples, estimators, and
   specifications that could *break* the result; say what you learn.
3. **Heterogeneity with discipline** — pre-specify or justify subgroups; adjust for multiple
   comparisons; don't mine an interaction and theorize it post hoc.
4. **Measurement** — validate constructs, report reliability, show results aren't an artifact of a
   coding/scaling choice (especially for inequality and well-being measures).

### Comparative-historical / ethnographic
- Make the **chain of evidence explicit**: link each claim to specific sources, observations, or
  cases; present negative/disconfirming evidence.
- Use evidence tables, timelines, or coded excerpts so reviewers can trace claims to data.

### Computational / text-as-data
- Document model/version, hyperparameters, seeds, preprocessing; **validate against human-labeled
  samples**; report stability. Don't treat model outputs as ground truth.

## Reproducibility while you work
- One **master script** regenerates every table/figure from raw/constructed data (quantitative).
- **Set and report seeds** for any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- For qualitative work, keep a documented codebook and analytic memos.

## Anti-patterns

- Stars-only tables with no effect sizes or intervals; ignoring survey weights
- "Robustness" that only reruns near-identical specs to manufacture stability
- p-hacking / HARKing exploratory results into hypotheses
- Qualitative claims with no traceable evidence or negative cases
- Computational outputs reported without validation

## Output format

```
【Main result】magnitude + interval (quant) OR evidence chain (qual)
【Identification/grounding check】(per research-design) result
【Robustness / negative cases】what held
【Heterogeneity】pre-specified? MHT-adjusted? (quant)
【Reproducible】master script + seeds + pinned versions OR documented codebook? [Y/N]
【Next】asr-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, demography, networks, and text-as-data packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — ASA data-sharing norms
