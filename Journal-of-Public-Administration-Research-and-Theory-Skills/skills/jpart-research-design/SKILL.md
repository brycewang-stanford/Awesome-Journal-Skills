---
name: jpart-research-design
description: Use when defending the research design of a Journal of Public Administration Research and Theory (JPART) manuscript — survey/lab/field experiments on public employees and citizens, causal observational designs, multilevel structures, or mixed methods. JPART has moved strongly toward experimental and causal identification. Strengthens the design; it does not write code.
---

# Research Design (jpart-research-design)

JPART has moved toward **experimental and causal** identification, and reviewers expect the design to
connect the theory (`jpart-theory-building`) to evidence credibly. This skill is mode-aware: pick the
section that matches your work and defend it against the strongest alternative explanation a
public-management reviewer will raise.

## When to trigger

- Specifying identification, an experiment, sampling, or measurement
- A reviewer questioned causal claims, common-method bias, endogeneity, or external validity
- Preparing a **pre-analysis plan** / preregistration (JPART accepts blinded pre-reg reports)
- Justifying why the design adjudicates the rival account from `jpart-literature-positioning`

## Design-choice gate

Start by matching the theoretical claim to the minimum credible design. Do not
choose the design by data availability alone.

| Claim type | Minimum design burden | Common downgrade |
|------------|-----------------------|------------------|
| "X causes Y in public organizations" | Identification strategy with an estimand, assignment/variation story, and falsification or sensitivity evidence | Reframe as association or theory-building descriptive evidence |
| "Mechanism M explains the effect" | Mediating evidence that is temporally and conceptually downstream of treatment/exposure, plus rival-mechanism checks | Reframe as a plausible mechanism to be tested, not demonstrated |
| "Public employees/citizens respond differently by condition C" | Pre-specified heterogeneity, adequate power, and measurement invariance across groups | Treat as exploratory moderation |
| "Policy/intervention improves performance" | Implementation fidelity, baseline comparability, outcome validity, and spillover/contamination checks | Reframe as pilot evidence |
| "Case evidence revises theory" | Case selection logic, process-tracing observations, rival explanations, and explicit scope conditions | Reframe as illustrative theory elaboration |

## Experiments (the modern JPART workhorse)
- **Population matters.** Public-management theory often requires *public employees* or *citizens* as
  subjects — defend the sample (e.g., real managers, frontline staff) over a generic MTurk pool.
- **Design.** Preregister the design and primary analyses; report power/MDE; pre-specify subgroups;
  use vignette/conjoint/factorial designs where the theory is about trade-offs.
- **Validity.** Attention/manipulation checks, attrition, realism of treatment, and consent/IRB.
- **Replication awareness.** PA has an active experimental-replication norm — design so the experiment
  could be re-run and pre-register to make exploratory vs. confirmatory analyses explicit.

## Observational / causal
- **Identification first.** State the estimand and the assumptions that license a causal reading
  (ignorability, parallel trends, exclusion, continuity). Defend them, don't assert them.
- **Designs:** DID/event study (modern staggered-adoption estimators, not naive TWFE), IV (first-stage
  strength, exclusion, weak-IV-robust inference), RDD (density/manipulation tests, bandwidth), matching
  /weighting with balance + sensitivity.
- **PA-specific confounds:** self-selection into public service, common-source/common-method bias when
  X and Y come from the same survey, endogenous sorting of managers to organizations.

## Multilevel / organizational
- Employees nested in agencies nested in jurisdictions — use multilevel models; cluster SEs at the level
  of treatment/assignment; report ICCs; do not ignore the nesting that PA data almost always has.

## Mixed methods
- Make the qualitative and quantitative components *answer the same theoretical question*; say what each
  buys and where they corroborate or diverge.

## The adjudication test (JPART-specific)

For the **single strongest rival explanation** (often selection or common-method bias), write one
sentence: *"If the rival were true rather than my mechanism, the data would look like ___; instead they
look like ___."* If you cannot, the design does not yet identify the contribution.

## Reviewer stress tests

Run these before the manuscript claims JPART-level causal or theoretical leverage:

- **Theory-design alignment:** the unit of theory, treatment/exposure, outcome, and
  inference level match. A theory about managers is not proven by citizen vignettes
  unless the bridge is explicit.
- **Measurement separation:** key independent/dependent variables are not merely
  two self-reports from the same respondent at the same time; if they are, build a
  common-method defense or narrow the claim.
- **Assignment credibility:** the reader can say why some units received more/less
  treatment and why that variation is not just latent performance, resources, or
  managerial quality.
- **Organizational nesting:** the standard errors, random effects, or design account
  for agencies, offices, jurisdictions, schools, or teams where treatment and outcomes cluster.
- **Generalization boundary:** state whether the result generalizes to public
  employees, citizens, organizations, jurisdictions, or one institutional setting.
- **Transparency path:** preregistration, data/code release, and any restricted-data
  exception can be anonymized and reconciled with `jpart-transparency-and-data`.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPART is public management — observational and experimental designs on public organizations; identification + clustered/multilevel inference.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A "behavioral PA" experiment on a generic online panel when the theory is about *public managers*
- Common-source bias: X and Y from the same self-report survey, called a causal effect
- Naive TWFE on staggered adoption; clustering at the wrong level; ignoring agency-level nesting
- Treating self-selection into public service as ignorable
- A design that cannot distinguish your mechanism from selection or the leading alternative

## Output format

```
【Mode】experiment / observational-causal / multilevel / mixed
【Population】public employees / citizens / orgs — defended? [Y/N]
【Estimand or claim】what is being identified/shown
【Key assumption(s)】and how each is defended
【Design-choice gate】causal / mechanism / heterogeneity / policy / case-theory burden met?
【Rival ruled out】the adjudication sentence (often selection / common-method)
【Stress-test gaps】theory-design / measurement / assignment / nesting / generalization / transparency
【Preregistered?】confirmatory vs exploratory split
【Next】jpart-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — experiment/causal packages (R/Stata/Python) and survey platforms
- [`../../resources/code/`](../../resources/code/) — reproducible DiD/IV/RDD/DML skeleton to adapt
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — preregistration / blinded pre-reg report policy
