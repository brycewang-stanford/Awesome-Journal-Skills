---
name: jpart-data-analysis
description: Use when executing and reporting the analysis for a Journal of Public Administration Research and Theory (JPART) manuscript so it survives expert, double-blind review and the journal's mandatory data-and-code release. Covers honest uncertainty, robustness, and the PA-specific traps (common-method bias, selection). Guides analysis norms; it does not fabricate results.
---

# Data Analysis (jpart-data-analysis)

JPART reviewers are methodologically sophisticated public-management scholars, and the journal **requires
authors to release the data and software code** underlying the paper as a condition of publication (see
`jpart-transparency-and-data`). Analyze as if a referee will re-run the code — because the materials are
public. This skill covers execution and reporting; design lives in `jpart-research-design`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, or alternative specifications
- Reconciling preregistered vs. exploratory analyses
- Making the analysis reproducible before the mandatory data/code deposit

## Analysis norms JPART expects

1. **Report uncertainty and magnitude.** Confidence/credible intervals and the *substantive* size of the
   effect (e.g., a fraction of an SD of PSM), not stars alone.
2. **Robustness that probes, not decorates.** Show specifications that could *break* the result
   (alternative measures of red tape/PSM, samples, estimators, fixed effects), and say what you learned.
3. **Confront the PA-specific threats.** Common-method/common-source bias, social desirability, and
   self-selection into public service are the objections raised first — address them, don't ignore them.
4. **Heterogeneity with discipline.** Pre-specify subgroups where possible; correct for multiple
   comparisons; do not mine for a significant interaction and theorize it post hoc.
5. **Right inference.** Cluster at the assignment/agency level; randomization inference for experiments;
   small-cluster corrections (wild-cluster bootstrap) when agencies are few.
6. **Preregistration discipline.** Separate **confirmatory** from **exploratory** analyses; reconcile any
   deviation from the plan and justify it.

## Measurement (a perennial JPART referee focus)
- Validate constructs (PSM, red tape, goal ambiguity); report reliability; show the result is not an
  artifact of a single scale or coding choice. Concept defined in `jpart-theory-building` must match the
  measure used here.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from raw/constructed data.
- **Set and report seeds** for bootstrap, randomization inference, simulation, any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- Keep table/figure numbers matched to script outputs — the materials are public and will be checked.

## What JPART reviewers probe, by design

| Design | The check a JPART referee runs first | The fix that earns benefit of the doubt |
|--------|--------------------------------------|------------------------------------------|
| Survey of public employees | Are X and Y from the same self-report (common-method)? | separate sources / objective Y / marker variable + Harman caution |
| Survey/field experiment | Is it pre-registered, powered, on the right population? | preregistered estimand, MDE reported, public-employee sample |
| Observational causal | Is "effect" really selection into public service? | state estimand + assumption; sensitivity to an unobserved confounder |
| Multilevel | Is the agency-level nesting modeled? | random effects / clustered SEs, ICC reported |
| Mixed methods | Do quant and qual actually corroborate? | show agreement and own divergence |

## Worked micro-example (illustrative numbers)

A hypothetical JPART field experiment tests whether a goal-clarity intervention raises frontline
performance among **real caseworkers**. The pre-registered ITT is **+0.18 SD (95% CI 0.06 to 0.30)**,
randomization-inference *p* = 0.006. An exploratory split by tenure shows **+0.41 SD** for new hires,
but it was *not* pre-registered and the interaction *p* = 0.03 before correction; after a Bonferroni
adjustment across five exploratory subgroups it crosses 0.20. The disciplined write-up reports the
confirmatory +0.18 SD effect with its interval and substantive meaning, flags the +0.41 figure as
**exploratory and not multiplicity-robust**, and frames it as a hypothesis for future work. (All
numbers illustrative.)

## Referee-pushback patterns and the JPART repair

- *"This is common-method bias, not an effect."* → Use a separate/objective outcome or a marker
  variable; report the sensitivity, don't wave it away with a single Harman test.
- *"The robustness table only reruns near-identical specs."* → Replace decorative checks with specs that
  could break the result (alternative PSM/red-tape measures, samples), and say what held.
- *"This is selection into public service."* → State the estimand and assumption; report how strong an
  unobserved confounder must be to overturn it.
- *"I cannot tell confirmatory from exploratory."* → Segregate them explicitly; the deposited code is
  public, so the split must survive a re-run.

## Calibration anchors (hedged)

- The bar is a **public-management theory** payoff carried by credible numbers — an estimate with no
  mechanism rarely clears JPART review.
- JPART increasingly rewards **experimental and causal** designs, but a rigorous multilevel or mixed
  study is judged on its own terms.
- The **data-and-code release is mandatory** (where ethically possible) — write the analysis so the
  public package reproduces every printed number. Confirm exact wording on the live policy page.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPART is public management — observational and experimental designs on public organizations; identification + clustered/multilevel inference.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```
【Main estimate】magnitude + interval + substantive meaning
【PA threat handled】common-method / selection — how?
【Robustness】specs that could break it → what held
【Heterogeneity】pre-specified? MHT-adjusted?
【Confirmatory vs exploratory】clearly separated?
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】jpart-tables-figures
```

## Supplementary resources

- [`../../resources/code/`](../../resources/code/) — Stata + Python estimation/inference skeleton
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, inference, and experiment packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data-and-code release policy
