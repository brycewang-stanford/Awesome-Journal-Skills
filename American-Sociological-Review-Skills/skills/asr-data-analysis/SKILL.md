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

## What an ASR analyst-reviewer is checking

As the ASA's flagship, ASR draws referees who police analysis on each tradition's terms while asking
one disciplinary question — does the evidence warrant a claim that speaks to general sociological
theory? Use this table to pre-empt the masked reviewer.

| Reviewer probe | Clears the ASR bar | Triggers a revision flag |
|----------------|--------------------|---------------------------|
| "Just a significant coefficient?" | magnitude + interval tied to a mechanism | stars-only, no interpretation |
| "Survives a reasonable confounder?" | sensitivity bound reported | one preferred spec, no probing |
| "Weighted and clustered right?" | design-respecting SEs | default SEs on a complex sample |
| "Where is disconfirming evidence?" | negative cases / null subgroups | only confirming evidence |
| "Heterogeneity real or mined?" | pre-specified or MHT-adjusted | one fished interaction theorized post hoc |

## Worked micro-example (illustrative numbers)

A hypothetical ASR study links employer credit-checking to a Black-white callback gap using
administrative hiring records across 1,200 firms.

```
Main effect: callback gap 8.0 pp (95% CI 5.1–10.9) under firm + occupation FE
Mechanism: gap concentrated in customer-facing roles (11.2 pp) vs back-office (2.3 pp)
Sensitivity: a confounder must be ~1.7× the strongest covariate to nullify
Negative case: no gap where state law bans the practice (0.4 pp, CI −2.0–2.8) → boundary evidence
Reproducible: one master script, seed=2026, renv.lock pinned
```

The intervals carry the claim, the role contrast names a portable mechanism (statistical
discrimination via screening signals), and the law-ban null is reported as evidence, not buried.

## Referee pushback → ASR-specific fix

- *"Significant but does it matter?"* → Give a scenario magnitude and name what changes for inequality
  theory.
- *"Robustness agrees by construction."* → Add a spec that could break it (placebo period,
  falsification subgroup) and report what you learned.
- *"This reads as a within-subfield exercise."* → State which general sociological debate the estimate
  adjudicates before the table, not after.

## Calibration anchors

- **Theory-forward, not table-forward.** ASR rewards an analysis that reads as a test of a mechanism;
  a results dump that defers the "why" under-performs.
- **The "so what for sociology" bar.** Each headline number should map to a sentence a generalist could
  repeat about how social processes work.
- **Breadth of admissible evidence.** Coefficients, life tables, coded fieldnotes, and validated model
  outputs all qualify — the standard is the claim-to-evidence link.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ASR is general sociology where observational designs dominate; foreground identification (DiD/IV/RDD), decomposition, and clustered inference.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the supplement. See
the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
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
