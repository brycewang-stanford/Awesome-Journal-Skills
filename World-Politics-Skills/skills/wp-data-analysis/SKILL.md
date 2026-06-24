---
name: wp-data-analysis
description: Use when executing and reporting the analysis for a World Politics manuscript so it survives expert triple-blind review and the Dataverse replication requirement — honest uncertainty, robustness, and triangulation appropriate to comparative cross-national, qualitative, or formal-empirical work. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (wp-data-analysis)

World Politics reviewers are methodologically demanding, and authors who **rely on quantitative data
must deposit replication materials in the World Politics Dataverse** that let others reproduce the
**exact numerical results** (see `wp-transparency-and-data-policy`). Analyze as if both are true —
because they are. This skill covers execution and reporting norms; design decisions live in
`wp-research-design`.

## When to trigger

- Running main and supporting analyses; building the results/findings section
- A reviewer asked for robustness, heterogeneity, or alternative specifications
- Reconciling the cross-case pattern with within-case evidence (mixed methods)
- Making the analysis reproducible before deposit

## Analysis norms World Politics expects

1. **Report uncertainty honestly.** Confidence/credible intervals, not just stars; the magnitude and
   substantive meaning of the estimate across cases, not just its significance.
2. **Robustness that probes, not decorates.** Show specifications that could *break* the result
   (alternative measures of regime/institution/conflict, alternative samples of cases, estimators,
   fixed effects), and say what you learn.
3. **Cross-national inference.** Cluster at the appropriate level (often country); address serial
   correlation and cross-sectional dependence in TSCS; small-N panels need honest few-cluster
   corrections (e.g., wild-cluster bootstrap).
4. **Measurement that travels.** Validate constructs across cases; report reliability; show results are
   not an artifact of one coding/scaling choice or one source (V-Dem vs. Polity, COW vs. UCDP).
5. **Heterogeneity with discipline.** Pre-specify subgroups/regions where possible; correct for
   multiple comparisons; do not mine for a significant interaction and theorize it post hoc.
6. **Triangulation.** Where the design is mixed-method, show the within-case process evidence and the
   cross-case statistics point the same way, and reconcile where they don't.

## Qualitative / comparative-historical specifics
- Make the **evidentiary basis explicit** — which sources support which inferential step; link claims
  to documents/interviews via evidence tables (see `wp-tables-figures`).
- For process tracing, report the tests passed/failed and what would have disconfirmed the argument.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for bootstrap, randomization, and any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- Keep table/figure numbers matched to script outputs — the Dataverse package must reproduce them.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). World Politics is comparative/IR with a strong qualitative tradition; apply the chain below to its quantitative-causal lane and say so when work is case-based.

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

- Stars-only tables with no effect sizes or intervals
- "Robustness" that only reruns near-identical specs to manufacture stability
- Results that hinge on one data source or one coding choice without showing alternatives
- Clustering at the wrong level; ignoring TSCS serial correlation / cross-sectional dependence
- A findings section whose numbers the deposited code cannot reproduce

## Referee-pushback patterns and the World Politics fix

World Politics referees span a methodologically plural community, so each tradition is judged on its
own terms. The recurring objections, and the answering move, are stable.

| Referee objection | The fix this skill drives |
|-------------------|----------------------------|
| "Robustness only reruns near-identical specs" | Show specs that could *break* it: rival measures (V-Dem vs. Polity, COW vs. UCDP), alternative case samples; report what each did |
| "Stars but no magnitudes" | Lead with effect size + interval + substantive meaning across cases |
| "Quant and case evidence diverge" | State it, adjudicate with within-case evidence, narrow the scope condition |

A frequent risk is the **fishing concern**: an interaction found post hoc and theorized as if
predicted. Pre-specify subgroups, correct for multiple comparisons, report the unconditional result
too. (Confirm expectations against the journal's reviewer guidelines.)

## Worked micro-example (illustrative numbers)

A hypothetical mixed-method study asks whether **fiscal decentralization dampens ethnic conflict
onset** across ~120 countries, paired with two within-case process-tracing narratives.

```text
Main estimate (illustrative): 1-SD rise in decentralization → onset HR 0.72, CI [0.58, 0.90]
  reading: ~28% lower onset risk at the mean, not just "p < 0.05"
Robustness:  swap V-Dem for OECD measure → HR 0.79 [0.61, 1.02] (weaker, crosses 1)
Few clusters (41) → wild-cluster bootstrap p = 0.04 (vs naive 0.01)
Triangulation: HR and both case narratives agree on a budgetary-bargain mechanism; the lone case
  where decentralization did NOT dampen conflict had centrally appointed governors → scope condition.
```

The honest reading: the effect is real but **scope-conditioned on genuine fiscal autonomy**, with
the weaker interval reported, not suppressed. Figures illustrative only.

## Output format

```
【Main estimate】magnitude + interval + substantive meaning across cases
【Identification check】(per research-design) result
【Robustness】specs / alternative sources that could break it → what held
【Measurement】construct validated across cases? source sensitivity shown?
【Triangulation】within-case + cross-case agree? reconciled?
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】wp-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, TSCS/panel, survival, and text-as-data packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Dataverse replication requirement
