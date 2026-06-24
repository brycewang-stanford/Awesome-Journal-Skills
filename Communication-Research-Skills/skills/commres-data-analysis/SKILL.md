---
name: commres-data-analysis
description: Use when executing and reporting the analysis for a Communication Research (CR) manuscript so it survives expert, double-anonymized review — ANOVA/regression/SEM, mediation/moderation with honest uncertainty, reliability, and APA statistical reporting. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (commres-data-analysis)

CR reviewers are quantitatively sophisticated, and the journal expects **APA-style statistical
reporting** (effect sizes and standard deviations, not stars alone). Analyze as if your numbers will
be scrutinized — because they will. This skill covers execution and reporting norms; design decisions
live in `commres-research-design`, and deposit live in `commres-transparency-and-data`.

## When to trigger

- Running main and supporting analyses; building the Results section
- A reviewer asked for robustness, an alternative specification, or a mediation re-analysis
- Reconciling preregistered vs. exploratory analyses
- Making the analysis reproducible before deposit

## Analysis norms CR expects

1. **APA statistical reporting.** Report **effect sizes** (d, η²ₚ, R², standardized β) and dispersion
   (SDs, CIs), test statistics with df, and exact p where feasible — not significance stars alone.
2. **Right model for the design.** ANOVA/ANCOVA for factorial experiments; OLS/logistic regression
   with proper controls; **SEM/CFA** for latent constructs; **multilevel models** for nested data
   (e.g., messages within participants, students within classrooms).
3. **Mediation/moderation done right.** For PROCESS/SEM models, justify the causal ordering; report
   **indirect effects with bootstrap CIs**; for moderated mediation report the index and conditional
   indirect effects; acknowledge cross-sectional limits on process claims.
4. **Report uncertainty honestly.** Confidence intervals and effect magnitudes; interpret the
   substantive meaning of the estimate, not just whether it crossed .05.
5. **Robustness that probes, not decorates.** Show specifications that could *break* the result
   (alternative measures, covariate sets, estimators, exclusions), and say what you learn.
6. **Measurement and reliability.** Report scale reliability (alpha/omega) and, for content analysis,
   **intercoder reliability**; show results are not an artifact of a coding/scaling choice.
7. **Preregistration discipline.** Clearly separate **confirmatory** (registered) from **exploratory**
   analyses; reconcile and justify deviations; correct for multiple comparisons where you test many.

## Computational / text-as-data specifics
- Document model/version, hyperparameters, seeds, and **validation against human-labeled samples**.
- For topic models/embeddings/LLM pipelines, report stability and a validation step; don't treat
  outputs as ground truth.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for bootstrap, simulation, and any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`; note SPSS/Mplus/PROCESS versions).
- Keep table/figure numbers in the manuscript matched to script outputs.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Communication Research is experiment- and survey-heavy; emphasize randomization inference, mediation done right, and family-wise corrections.

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

- Stars-only tables with no effect sizes, SDs, or intervals (an APA-reporting failure at CR)
- Reporting a mediation without bootstrap CIs, or a moderated mediation without the index
- "Robustness" that only reruns near-identical specs to manufacture stability
- p-hacking / fishing for a significant interaction; HARKing exploratory results into hypotheses
- Reporting a content analysis without intercoder reliability
- A Results section whose numbers the code cannot reproduce

## Evidence pass for Communication Research

Treat this skill as an executable review pass, not a prose hint. First lock the communication process,
the measured constructs, the study design, and the inferential claim; then judge whether the
manuscript answers CR's real reader: a quantitatively trained communication scientist who weighs
theory, measurement validity, identification, and effect interpretation.

- **Do the pass:** Audit before polishing prose — model choice, effect sizes, uncertainty, mediation
  CIs, reliability, multiple-testing, missingness, and reproducibility must be visible.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows so the next agent
  edits rather than rediscovers the issue.
- **Sibling guard:** *Journal of Communication* (all-paradigm), *Human Communication Research*
  (interpersonal), *New Media & Society* (digital). If a sibling owns the contribution, re-route
  before polishing format.
- **Stop condition:** do not give submission-ready advice until `resources/official-source-map.md`
  has been checked and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Main estimate】magnitude + effect size + interval + substantive meaning
【Model】ANOVA / regression / SEM / multilevel — matches the design?
【Mediation/moderation】indirect effect + bootstrap CI / index of moderated mediation?
【Robustness】specs that could break it → what held
【Reliability】scale (alpha/omega) / intercoder reliability reported?
【Confirmatory vs exploratory】clearly separated? MHT-adjusted where needed?
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】commres-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, reliability, mediation/SEM, and text-as-data packages
- [`../../resources/code/`](../../resources/code/) — reproducible analysis skeleton (clean → descriptive → models → robustness → tables)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — APA statistical-reporting expectation
