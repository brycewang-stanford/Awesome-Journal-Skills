---
name: pubar-research-design
description: Use when defending the research design of a Public Administration Review (PAR) manuscript — public-management causal designs (DiD around reforms, survey & field experiments on bureaucrats/citizens, RD, IV), case comparison and process tracing, and mixed methods. PAR judges each tradition on its own terms. Strengthens the design; it does not write code.
---

# Research Design (pubar-research-design)

PAR accepts many methodologies but is demanding about each. The design must credibly connect the
argument (`pubar-theory-building`) to evidence drawn from public organizations, bureaucrats, citizens,
or jurisdictions. This skill is mode-aware: pick the section that matches your work and defend it
against the strongest alternative explanation.

## When to trigger

- Specifying identification, case selection, or experimental design
- A reviewer questioned causal claims, case choice, external validity, or a confound
- Preparing a **pre-analysis plan** or a pre-registration (PAR offers pre-registration badges)
- Justifying why your design adjudicates the rival account from `pubar-literature-positioning`

## PAR design-fit gate

PAR is a generalist flagship, so the design must support both an academic claim and a usable public-
management implication. Start with this gate before polishing methods language.

| Claim type | Design burden | Practice-relevance check |
|---|---|---|
| Reform or mandate effect | Assignment/timing logic, counterfactual trend, spillover check, and clustering at assignment level | The finding changes how agencies time, target, or evaluate reforms |
| Managerial behavior | Sample frame tied to real public managers or frontline staff, realistic decision task, and measured behavioral outcome | The recommendation is feasible inside public organizations |
| Citizen response / public trust | Treatment realism, representativeness limits, manipulation checks, and ethical framing | The takeaway does not overgeneralize from survey preference to administrative behavior |
| Case/process account | Case-selection logic, process-tracing tests, chronology, and rival-account evidence | The lesson transfers to a defined class of agencies, programs, or jurisdictions |
| Mixed-method mechanism | Quantitative association/effect plus qualitative implementation or mechanism evidence | The qualitative strand explains what managers can act on, not just why results are interesting |

## Quantitative / causal inference (public-management settings)
- **Identification first.** State the estimand and the assumptions that license a causal reading
  (ignorability, parallel trends, exclusion, continuity). Defend them, don't assert them.
- **Designs common in PA**: DiD/event study **around a reform or mandate** (use modern
  staggered-adoption estimators — Callaway–Sant'Anna, Sun–Abraham, BJS — not naive TWFE); IV
  (first-stage strength, exclusion, weak-IV-robust inference); RD around eligibility/funding
  thresholds; matching/weighting with balance + sensitivity.
- **Inference**: cluster at the level of treatment assignment (often agency, district, or
  jurisdiction); wild-cluster bootstrap when clusters are few (a recurring PA problem with state- or
  agency-level treatments).
- **Sensitivity**: how strong must an unobserved confounder be to overturn the result (Oster / E-value)?

## Experiments on bureaucrats and citizens
- Preregister the design and primary analyses; report power/MDE; pre-specify subgroups.
- **Bureaucrat/managerial experiments**: realism of the decision task, sample frame (which public
  managers), and generalization to real administrative behavior.
- **Citizen survey/conjoint experiments**: treatment realism, attention/manipulation checks,
  attrition, and ethics/IRB and consent.

## Qualitative / case-based & mixed methods
- **Case selection** justified by design logic (typical, deviant, most/least-likely, paired
  comparison) — not convenience. Say what the case is a case *of* (a reform, a governance form).
- **Process tracing** with explicit tests (hoop, smoking-gun, straw-in-the-wind); state what evidence
  would have **disconfirmed** the argument.
- **Mixed methods**: say what the qualitative strand adds that the quantitative cannot (mechanism,
  context, implementation), and where the two corroborate or diverge.

## The adjudication test (PAR-specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather
than my argument, the agencies/managers/citizens would look like ___; instead they look like ___."* If
you cannot, the design does not yet identify the contribution — and the practitioner takeaway is unsafe.

## Practice-safe inference rules

- **Separate evidence from recommendation.** A credible association may justify a diagnostic warning;
  a causal design may justify a stronger managerial recommendation; neither automatically justifies a
  universal policy prescription.
- **Name the implementation margin.** If the intervention is staffing, training, targeting, rule
  design, citizen communication, or interagency coordination, say which margin the design actually tests.
- **Check administrative feasibility.** A design can be internally valid but still imply an action no
  manager can implement. Flag cost, authority, data availability, and equity constraints.
- **Bound external validity.** Identify the agency type, policy domain, country/state/local context,
  and population to which the evidence should and should not travel.
- **Route transparency early.** If the result relies on confidential administrative data, plan the
  restricted-data path with `pubar-transparency-and-data` before claims harden.

## Reviewer stress tests

- Would the result survive if the strongest agency-level selection story were true?
- Is the treatment/exposure measured before the outcome and at the right organizational level?
- Are standard errors clustered at the assignment or sampling level, not merely the observation level?
- For qualitative work, what observation would have disconfirmed the mechanism?
- For mixed methods, do both strands answer the same claim, or are they two parallel papers?
- Can the Evidence for Practice box be written without making a claim the design cannot support?

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). PAR is public administration — survey/observational and some experimental work; identification + clustered/multilevel inference, magnitude for practice.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Naive TWFE on a staggered reform rollout; clustering below the assignment level
- "Causal" language (and a managerial recommendation) on a design that only supports association
- Convenience case selection dressed up as theory-driven
- Bureaucrat/citizen experiments over-generalized to real administrative behavior with no caveat
- A design that cannot distinguish your argument from the leading alternative

## Output format

```
【Mode】quant-causal / experiment / qualitative / mixed
【Estimand or claim】what is being identified/shown
【Design-fit gate】academic claim + practice relevance supported? [Y/N]
【Key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity】planned checks (clustering, few-cluster, Oster/E-value)
【Practice-safe inference】recommendation strength + implementation margin + external-validity boundary
【Transparency handoff】public / restricted / qualitative-controlled-access path
【Next】pubar-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design/identification packages (R/Stata/Python) and CAQDAS for qualitative work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — pre-registration badges and TOP notes
