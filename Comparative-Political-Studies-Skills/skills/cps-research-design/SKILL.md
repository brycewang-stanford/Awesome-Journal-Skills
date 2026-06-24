---
name: cps-research-design
description: Use when defending the research design of a Comparative Political Studies (CPS) manuscript — cross-national/panel identification, case-based comparison and process tracing, experiments, or multi-method designs. CPS prizes comparative leverage. Strengthens the design; it does not write code.
---

# Research Design (cps-research-design)

CPS is methodologically pluralist but demanding about each tradition. The design must credibly connect
the comparative argument (`cps-theory-building`) to evidence and rule out the leading rival
(`cps-literature-positioning`). This skill is mode-aware: pick the section that matches your work and
defend the *comparative leverage* — the variation across cases or time that identifies the claim.

## When to trigger

- Specifying the identification strategy, case selection, or experimental design
- A reviewer questioned causal claims, case choice, external validity, comparability, or a confound
- Designing a cross-national panel, a subnational comparison, or a natural experiment across borders
- Justifying why the design adjudicates the rival account, not just shows an association

## Comparative-causal toolkit (cross-national / panel)

- **Identification first.** State the estimand and the assumptions that license a causal reading
  (parallel trends, exclusion, continuity, ignorability). Defend them; don't assert them.
- **Designs**: cross-national panels with unit and period fixed effects; DiD/event study around reforms
  (use modern staggered-adoption estimators, not naive TWFE); RD around institutional thresholds; IV
  (first-stage strength, exclusion, weak-IV-robust inference); survey experiments fielded comparatively.
- **Comparability.** Defend that the units are measured the same way across countries (V-Dem vs. Polity
  coding, harmonized surveys); address country-level confounding and cross-national measurement error.
- **Inference**: cluster at the level of treatment assignment (often country or country-year); few-cluster
  corrections (wild bootstrap) when the number of countries is small; multiple-comparison adjustment.
- **Sensitivity**: how strong must an unobserved country-level confounder be to overturn the result?

## Case-based / qualitative comparison

- **Comparison logic**: most-similar (control on shared traits, vary the cause) or most-different
  (shared outcome despite different contexts) — justified by design, not convenience.
- **Case selection**: typical, deviant, most/least-likely, paired comparison. Say what each case is a
  case *of* and avoid selecting on the outcome.
- **Process tracing** with explicit tests (hoop, smoking-gun, straw-in-the-wind); state what evidence
  would have **disconfirmed** the mechanism.
- **Source transparency**: archives, interviews, fieldnotes — plan documentation (see `cps-transparency-and-data`).

## Experiments (survey / field, fielded comparatively)

- Preregister design and primary analyses; report power/MDE; pre-specify subgroups and the comparison.
- For cross-country survey/conjoint experiments: equivalence of instruments and treatment realism across
  contexts; sampling frames; what the comparative contrast licenses about generalization.

## Multi-method linkage

- Use the quantitative estimate for the average comparative effect and the case evidence for the
  *mechanism*; state how each method covers the other's blind spot, not as decoration.

## The adjudication test (CPS-specific)

For the **single strongest rival**, write one sentence: *"If the rival were true rather than my
argument, the cross-case/over-time pattern would look like ___; instead it looks like ___."* If you
cannot, the design does not yet identify the comparative contribution.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). CPS is comparative politics — cross-national and sub-national designs; emphasize identification and clustered / multiway inference.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference, `romano_wolf` for many-outcome
  family-wise control, and `mediate` for mediation (not naive controlling-away).
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the effect size in interpretable units; route the full battery to the
appendix/supplement. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Naive TWFE on staggered reforms; clustering at the wrong level; ignoring the small-number-of-countries problem
- "Causal" language on a design that only supports cross-national correlation
- Convenience or selecting-on-the-outcome case selection dressed up as most-similar design
- Cross-national survey experiment with non-equivalent instruments across countries
- A design with no comparative leverage — one snapshot that cannot distinguish your argument from the rival

## Output format

```
【Mode】comparative-causal / case-based / experiment / multi-method
【Comparative leverage】the across-case / over-time variation that identifies the claim
【Estimand or claim】what is being identified/shown
【Key assumption(s)】and how each is defended (incl. comparability)
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity】planned checks
【Next】cps-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — comparative datasets, identification packages, and CAQDAS for qualitative work
- [`../../resources/code/`](../../resources/code/) — staggered-DiD / IV / RDD / DML command chain to adapt
