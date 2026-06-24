---
name: rfs-robustness
description: Use when results may be fragile or when multiple-testing / out-of-sample discipline is the bottleneck for a The Review of Financial Studies (RFS) manuscript. Builds the robustness battery referees will demand; does NOT design identification or write the rebuttal.
---

# Robustness & Multiple-Testing Discipline (rfs-robustness)

## When to trigger

- The main result holds in one specification but you have not stress-tested it
- A new return predictor / cross-sectional anomaly is the central claim
- You tested many candidate variables and want to report the ones that "worked"
- Reviewers will ask "does this survive [alternative spec / subsample / period]?"
- Results may be sensitive to outliers, windsorization, or a single event

## The two robustness mandates at RFS

RFS punishes **fragile results** and, in cross-sectional asset pricing, **undisciplined multiple testing**. Build the battery proactively — a result that only the authors can reproduce in one specification is treated as no result.

Two RFS-specific mechanisms raise the bar above JF/JFE:
- **Public code release is a condition of publication.** Referees and post-publication readers can and do re-run your code. A robustness claim you cannot reproduce from the released code is a liability, not a footnote — design the battery so the released scripts regenerate every check.
- **Registered Reports neutralize the multiple-testing critique by construction.** Because RFS offers **pre-results review** (the format it pioneered in finance), pre-specifying the hypothesis and the test *before* seeing outcomes is the strongest possible answer to "you data-mined this." Even outside the Registered Report track, pre-specification is the RFS-preferred defense. The q-factor spanning logic of Hou, Xue, and Zhang (2015) "Digesting Anomalies" (RFS 28(3)) is a model for confronting the anomaly zoo head-on.

### A. General-fragility battery (all empirical papers)
- **Alternative specifications**: different FE, control sets, functional forms — show the coefficient is stable.
- **Alternative measures**: re-estimate with an alternative proxy for the key variable.
- **Subsamples**: split by period, size, industry, region; the sign should not flip without explanation.
- **Outliers**: re-run with alternative winsorization/trimming; drop influential observations.
- **Placebo / falsification**: a setting where the effect should be zero.
- **Alternative clustering**: show inference is not driven by an SE choice.

### B. Multiple-testing discipline (cross-sectional asset pricing especially)
- If the claim is a *new predictor or anomaly*, confront the data-mining critique head-on.
- Report and discuss multiple-testing-adjusted significance (e.g., Bonferroni / Holm, FDR control, or the higher t-hurdles argued in the asset-pricing replication literature such as Harvey–Liu–Zhu).
- Distinguish **in-sample** fit from **out-of-sample** performance; report OOS explicitly.
- Pre-specify the hypothesis; do not present a survivor of a large specification search as if it were a single test.
- For factor claims, run spanning tests against established factor models and report the alpha after controls.

### C. Mechanism / external validity (supporting robustness)
- Show the mechanism, not just the reduced-form effect — heterogeneity consistent with the proposed channel strengthens credibility.
- Triangulate with a second data source or setting when feasible.

### Sequencing the battery
- Run the fragility checks before writing the main tables — a result that moves under reasonable perturbation is not ready.
- For asset-pricing claims, treat the out-of-sample and multiple-testing checks as primary, not optional add-ons.
- Decide early which single check per result earns a place in the main paper; the rest go to the Internet Appendix (`rfs-internet-appendix`).
- If a check weakens the result, address it in the text — do not bury it or omit it; referees will re-run the obvious ones.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RFS is finance top-3 (with JF, JFE) — corporate-causal chain for corporate papers, factor-zoo haircut for asset pricing.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Main coefficient shown stable across ≥3 alternative specifications
- [ ] Alternative measure of the key variable tested
- [ ] Subsample / period splits reported; sign stability explained
- [ ] Outlier/winsorization sensitivity checked
- [ ] Placebo or falsification test included
- [ ] For asset-pricing claims: multiple-testing adjustment + out-of-sample test reported
- [ ] Spanning tests against standard factor models (if a factor claim)
- [ ] Every robustness check regenerable from the code RFS will require you to release publicly
- [ ] Robustness tables sized for the Internet Appendix, not the main paper

## Anti-patterns

- Reporting the 3 predictors that worked out of 40 tested, with no adjustment.
- Calling a result "robust" after one alternative control set.
- In-sample-only predictability dressed as economically meaningful.
- A subsample sign flip mentioned only in a footnote with no explanation.
- Dumping 30 robustness tables into the main paper instead of the IA.

## Output format

```
【Main result】coefficient / magnitude
【Fragility checks done】[specs, measures, subsamples, outliers, placebo]
【Multiple-testing】adjustment used + OOS result (if asset pricing)
【Surviving concerns】[...]
【Where reported】main paper vs. Internet Appendix
【Next step】rfs-tables-figures
```
