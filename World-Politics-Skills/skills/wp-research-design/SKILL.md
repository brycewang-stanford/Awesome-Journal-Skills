---
name: wp-research-design
description: Use when defending the research design of a World Politics manuscript — comparative-historical and case selection, quantitative cross-national identification, qualitative process tracing, experiments, or formal-empirical linkage for cross-case questions. World Politics expects explicit research design and appropriate methods, judged on each tradition's own terms. Strengthens the design; it does not write code.
---

# Research Design (wp-research-design)

World Politics asks every article to "be explicit about its research design and use appropriate
methods," and applies separate expectations to quantitative and qualitative work. Because the journal
values **arguments that travel across cases**, the design must connect a portable argument
(`wp-theory-building`) to evidence in a way that **rules out the strongest cross-case rival**. This
skill is mode-aware: pick the section that matches your work.

## When to trigger

- Specifying case selection, identification, or experimental design for a cross-case question
- A reviewer questioned causal claims, case choice, external validity, or a confound
- Justifying why your design adjudicates the rival account from `wp-literature-positioning`

## Comparative-historical & case-based (a World Politics staple)
- **Case selection by design logic** — typical, deviant, most/least-likely, paired/structured-focused
  comparison, or set-theoretic (QCA). Say what each case is a case *of* and why the comparison
  identifies the argument. Convenience is not a design.
- **Process tracing** with explicit tests (hoop, smoking-gun, straw-in-the-wind); state what evidence
  would have **disconfirmed** the argument in each case.
- **Travel.** Show the comparison licenses a claim beyond the cases studied (scope conditions), not
  just a within-case story.

## Quantitative / cross-national
- **Identification first.** State the estimand and the assumptions that license a causal reading
  (parallel trends, exclusion, continuity, ignorability). Defend them; don't assert them.
- **TSCS realities.** With time-series-cross-section data, address serial correlation, unit effects,
  and cross-sectional dependence (panel-corrected SEs, Driscoll–Kraay); avoid naive TWFE on staggered
  treatment — use modern estimators.
- **Designs**: DID/event study, IV (first-stage strength, exclusion, weak-IV-robust inference), RDD,
  matching/weighting with balance + sensitivity; survival models for onset/duration.
- **Inference**: cluster at the right level (often country); sensitivity to unobserved confounding.

## Experiments & formal-empirical
- Experiments: preregister design and primary analyses; report power/MDE; address attrition and ethics
  (APSA Principles — see `wp-review-process`/`wp-submission`). State the generalization claim across
  contexts honestly.
- Formal-empirical: make the **empirical test follow from the model's comparative statics**, and
  distinguish predictions unique to your model from those shared with rivals.

## The adjudication test (World Politics–specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather than
my argument, the cases/data would look like ___; instead they look like ___."* If you cannot, the
design does not yet identify a contribution that travels.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). World Politics is comparative/IR with a strong qualitative tradition; apply the chain below to its quantitative-causal lane and say so when work is case-based.

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

- Convenience case selection dressed up as theory-driven; selecting on the dependent variable
- Naive TWFE on staggered treatment; ignoring serial correlation / cross-sectional dependence in TSCS
- "Causal" language on a design that only supports cross-case association
- A within-case story over-generalized with no scope conditions
- A design that cannot distinguish your argument from the leading alternative

## Design-objection patterns and the venue-specific fix

World Politics judges each tradition on its own terms and prizes designs built to adjudicate, so
design objections cluster predictably across the comparative and IR styles it publishes.

| Referee objection | The fix this skill drives |
|-------------------|----------------------------|
| "Case selection unjustified" | State what each case is a case *of* and the design logic (typical / deviant / most–least-likely / paired); convenience is not a design |
| "Selecting on the dependent variable" | Add variation on the outcome, or reframe as a scope-condition study with disconfirming cases |
| "Causal language on associational design" | Match the verb to the warrant; reserve causal claims for designs that identify them |

## Worked micro-example (illustrative)

A hypothetical comparative study asks whether **electoral autocracies are more war-prone than closed
ones**. A weak version selects three war-fighting electoral autocracies and infers a tendency — a
selection-on-the-outcome flaw a referee will name immediately.

```text
Mode:      comparative-historical, structured-focused comparison
Estimand:  conflict propensity, electoral vs closed autocracy, holding capacity fixed
Selection: 2 electoral + 2 closed autocracies matched on GDP/region; varies on the OUTCOME
Adjudication: if the rival "capacity, not regime type" held, the matched closed cases would
  fight as often; instead the electoral cases initiate ~2x more disputes (illustrative).
Travel:    scope condition — holds where elections raise audience costs, not where they are sham
```

The redesign varies on the outcome and writes the adjudication sentence, so the comparison can
identify a contribution that travels. (Counts and ratios illustrative; confirm design expectations
against current guidelines.)

## Output format

```
【Mode】comparative-historical / quant cross-national / qualitative / experiment / formal-empirical
【Estimand or claim】what is being identified/shown, and across which cases
【Case selection / key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity】planned checks
【Next】wp-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — identification/TSCS packages, QCA, and CAQDAS for qualitative work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — reviewer-guideline expectations for design and methods
