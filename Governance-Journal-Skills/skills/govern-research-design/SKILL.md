---
name: govern-research-design
description: Use when defending the research design of a Governance: An International Journal of Policy, Administration, and Institutions manuscript — comparative/causal designs for governance & institutions, qualitative & comparative-historical case logic, mixed methods, and the measurement of governance/institutions. Governance judges each tradition on its own terms. Strengthens the design; it does not write code.
---

# Research Design (govern-research-design)

*Governance* welcomes any rigorous approach but is demanding about each. The design must credibly
connect the argument (`govern-theory-building`) to comparative/institutional evidence and **rule out the
strongest rival institutional explanation**. This skill is mode-aware: pick the section that matches your
work. (For the conceptual contribution, this is the empirical-design variant.)

## When to trigger

- Specifying identification, case selection, or comparative design
- A reviewer questioned causal claims, case choice, country selection, or an institutional confound
- Choosing governance/institutions measures (V-Dem, QoG, WGI, etc.) and defending them
- Justifying why the design adjudicates the rival account from `govern-literature-positioning`

## (a) Comparative / causal designs (governance & institutions)

- **Identification first.** State the estimand and the assumptions that license a causal reading
  (parallel trends, exclusion, continuity, ignorability). Defend them; don't assert them.
- **Reform DiD / event study.** When a reform rolls out across units/countries over time, use **modern
  staggered-adoption estimators** (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille,
  Borusyak et al.) — **not naive TWFE**, which is biased under heterogeneous/dynamic effects. Show
  pre-trends and event-study leads/lags.
- **Cross-national panels.** Justify fixed effects (country, year), the level of clustering, and what is
  identified off within-country vs. between-country variation.
- **IV / RDD where applicable.** IV: first-stage strength, exclusion, weak-IV-robust inference. RDD
  (e.g., electoral or threshold-based reform rules): density/manipulation tests, bandwidth robustness.

## (b) Qualitative / comparative-historical

- **Case selection by design logic** (most/least likely, typical, deviant, paired comparison) — not
  convenience. Say what each case is a case *of*, and how the selection adjudicates the argument.
- **Process tracing with explicit tests** (hoop, smoking-gun, straw-in-the-wind, doubly-decisive); state
  what evidence would have **disconfirmed** the argument in each case.
- **QCA where used.** Justify calibration of set membership, the truth table, and consistency/coverage
  thresholds; report and interpret limited diversity, not just the solution formula.
- **Source transparency.** Archives, interviews, fieldnotes — plan how they will be documented and cited
  (see `govern-transparency-and-data`).

## (c) Mixed methods

- State the **integration logic** up front: does the qualitative work generate, test, or explain the
  quantitative result (or vice versa)? Sequencing and the role of each strand must be deliberate.
- Show **where the strands converge** and own where they diverge — divergence is informative, not a flaw
  to bury.

## (d) Measuring governance & institutions (caveats)

- **V-Dem, QoG, WGI, Bertelsmann, ICRG, etc.** are estimates, not facts. Report the version, the
  construct each index actually captures, and the measurement model's uncertainty (e.g., V-Dem posterior
  credible intervals). Do not treat composite indices as ground truth.
- **WGI** in particular aggregates perceptions and is endogenous to outcomes — flag this when it sits
  near the dependent or treatment variable.
- Show results are not an artifact of one index: triangulate across measures where the concept allows.

## The rival-institutional adjudication move (Governance-specific)

For the **strongest rival institutional explanation**, write one sentence: *"If the rival were true
rather than my argument, the cases/data would look like ___; instead they look like ___."* A design that
cannot distinguish your account of governing from the leading institutional alternative has not yet
identified the contribution.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Governance is public administration and institutions research — comparative and causal designs on governance reforms; the chain serves its quantitative-causal lane, while comparative-historical / qualitative work uses its own standards.

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

- Naive TWFE on a staggered reform; clustering below the level of treatment assignment
- "Causal" language on a cross-national correlation the design only supports as association
- Convenience country selection dressed up as theory-driven case logic
- Treating V-Dem/WGI/QoG scores as exact, ignoring index uncertainty and construct mismatch
- A design that cannot rule out the leading rival institutional account

## Output format

```
【Mode】comparative-causal / qualitative / comparative-historical / mixed
【Estimand or claim】what is being identified/shown
【Key assumption(s)】and how each is defended
【Governance measures】index + version + uncertainty/construct caveat
【Rival ruled out】the rival-institutional adjudication sentence
【Robustness/sensitivity】planned checks
【Next】govern-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — staggered-DiD/IV/RDD packages, QCA/process-tracing tools, governance indices
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — pre-analysis plan as supplementary material; transparency notes
