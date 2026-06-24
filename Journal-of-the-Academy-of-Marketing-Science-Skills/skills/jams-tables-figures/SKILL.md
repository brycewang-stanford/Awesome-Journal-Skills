---
name: jams-tables-figures
description: Use when building exhibits for a Journal of the Academy of Marketing Science (JAMS) manuscript — the conceptual model figure, measurement and structural tables, interaction/simple-slopes plots, and managerial summary exhibits in APA style. Makes each exhibit self-contained and decision-relevant; it does not write the surrounding prose (jams-writing-style).
---

# Tables & Figures (jams-tables-figures)

## When to trigger

- The conceptual model figure is missing, cluttered, or inconsistent with the hypotheses
- Measurement and structural results are crammed into one unreadable table
- Interaction or mediation results need a clear plot
- Exhibits report significance but not the managerial magnitude

## The exhibits a JAMS paper is expected to carry

JAMS papers have a recognizable exhibit grammar. Build these deliberately:

1. **Conceptual model figure.** Almost every framework paper opens its empirics with a drawn nomological net — boxes for constructs, arrows labeled H1…Hk, mediators and moderators positioned correctly. The figure must match the hypotheses *exactly*; a mismatch between the model figure and the hypothesis list is a classic reviewer catch.
2. **Measurement table.** Items, loadings, reliability (CR / α), AVE — and a discriminant-validity table (Fornell–Larcker diagonal of √AVE, and/or an **HTMT** matrix).
3. **Structural results table.** Standardized path coefficients with SEs/CIs, *R²* for endogenous constructs, model fit (CFI, TLI, RMSEA, SRMR) or PLS metrics (*Q²*, *f²*).
4. **Mediation/moderation exhibit.** Indirect effects with bias-corrected CIs; an **interaction plot with simple slopes** (and error bands) where a moderator is central.
5. **Managerial exhibit (the JAMS differentiator).** A table or figure that translates the estimates into decision terms — effect on sales/share/CLV/margin by segment or scenario. This is where JAMS exhibits do work that the modeling siblings' tables do not.

## House-style and reporting essentials

- **Self-contained.** Each exhibit has a descriptive title, defined variables and units, sample size, and a note stating the estimator and SE type. A reader should grasp it without the body text.
- **APA style** in notes and captions; numbering consistent across text, tables, and figures; every exhibit referenced in the text in order.
- **Effect sizes visible.** Standardized coefficients, *R²*, *d*/η², or odds ratios — not significance alone. If you use significance markers, still report the magnitude.
- **Mediation done right in the exhibit:** show the indirect effect and its bias-corrected CI, not a row of Baron–Kenny steps.
- **Don't bury the contribution.** The main text carries the exhibits that prove the core argument; supplementary descriptives, full item lists, and extra robustness belong in an online appendix / supplementary file, not padded into the paper.

## Exhibit-by-genre quick guide

The right exhibit set depends on the empirical genre — build to the genre, not to a generic template:

- **Survey + SEM/PLS:** conceptual model figure → measurement table (loadings, CR/AVE) → discriminant-validity table (Fornell–Larcker with √AVE on the diagonal, and an HTMT matrix) → structural-paths table with standardized coefficients, *R²*, and fit → simple-slopes plot for any moderator → a managerial scenario table.
- **Secondary-data econometrics:** descriptives/correlations → identification diagnostic (first stage, pre-trends plot, balance) → main regression table with cluster-robust SEs → robustness columns → an elasticity/magnitude exhibit in managerial units.
- **Experiment:** a study-flow/design figure → cell-means table (M, SD, n per condition) → interaction plot with error bars → a mediation figure with bootstrapped indirect effects.
- **Meta-analysis:** a sample/coding-flow (PRISMA-style) figure → forest-style effect-size table → moderator meta-regression table → a funnel plot or other publication-bias diagnostic.

## Make the moderator and the magnitude visible

Two exhibits decide whether a JAMS reviewer believes the contingency story and the managerial payoff. The **interaction plot** must show the moderator on separate lines with the simple slopes labeled and significance of each slope stated in the note — a bare interaction coefficient in a table is not enough. The **managerial magnitude exhibit** should convert the focal effect into the unit a decision maker uses (e.g., "a one-SD increase in the focal construct raises predicted retention by X points for high-equity brands but only Y for low-equity brands"), so the boundary condition reads as a segmentation rule, not a statistical artifact.

## Common exhibit defects JAMS reviewers flag

- **Hypothesis–figure–table mismatch.** The conceptual model shows a moderator the structural table never tests, or the hypothesis numbers do not line up across the three. Cross-check them as a set before submitting.
- **Stars without sizes.** A table of asterisks tells the reader nothing about magnitude; add standardized coefficients, CIs, and *R²*.
- **Mediation as a flowchart of p-values.** Show the indirect effect and its bias-corrected CI as a number, not a diagram of significant arrows.
- **Notes that omit the estimator.** A reader cannot judge a coefficient without knowing the model, the SE type, and the sample base — put them in the note.
- **No managerial exhibit at all.** Many otherwise-clean JAMS submissions stop at the structural table; the missing decision-units exhibit is exactly what a reviewer asks for in round one.

## Title, label, and number discipline

Give every exhibit a **descriptive title** that states what it shows ("Table 3. Structural Model Estimates for the Brand-Equity → Firm-Value Path"), define every variable and abbreviation in the note, state the sample size, and number exhibits in the order they are first cited in the text. Keep one numbering sequence across the main paper, and a separate clearly-prefixed sequence for any online appendix, so a reviewer can always tell which file an exhibit lives in.

## Main text vs. supplementary split

Decide deliberately what each exhibit is for. The **main text** carries only the exhibits a reader needs to follow the core argument: the conceptual model, the key measurement evidence, the structural results, the central interaction/mediation, and the managerial-magnitude exhibit. Everything else — full item wording, complete correlation matrices, additional samples, alternative specifications, and most robustness — belongs in the **online/supplementary appendix**, clearly labeled and self-contained. Pushing supporting detail to the appendix keeps the printed paper legible and signals to the reviewer that you know which exhibits actually prove the claim.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAMS is empirical marketing with much survey-based SEM; the chain below serves causal / quasi-experimental designs and many-outcome corrections.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Conceptual model figure present and matches the hypothesis list exactly
- [ ] Measurement table: loadings, CR/α, AVE; discriminant validity (FL / HTMT)
- [ ] Structural table: standardized paths + SE/CI, *R²*, fit indices (or PLS metrics)
- [ ] Interaction/simple-slopes plot for any central moderator
- [ ] Mediation exhibit shows indirect effect + bias-corrected CI
- [ ] At least one exhibit translates estimates into managerial magnitudes
- [ ] Every exhibit self-contained; APA notes; consistent numbering; referenced in order

## Anti-patterns

- A conceptual model figure that contradicts the hypotheses or the structural table
- Measurement and structural results fused into one indecipherable table
- Tables with significance stars but no effect sizes or magnitudes
- A moderator hypothesis with no interaction plot
- Mediation shown as causal-steps rows instead of bootstrapped indirect effects
- Padding the main text with descriptives that belong in supplementary material

## Output format

```text
【Conceptual model figure】present + matches hypotheses? yes/fix
【Measurement table】loadings/CR/AVE + discriminant (FL/HTMT): pass/fix
【Structural table】std paths + SE/CI + R² + fit: pass/fix
【Mediation/moderation exhibit】indirect+CI / simple slopes: pass/fix
【Managerial exhibit】estimates → decision units? present/add
【House style】APA notes, self-contained, numbered, referenced: pass/fix
【Next skill】jams-writing-style
```
