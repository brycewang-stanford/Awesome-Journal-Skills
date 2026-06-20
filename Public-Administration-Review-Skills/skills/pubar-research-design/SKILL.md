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
【Key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity】planned checks (clustering, few-cluster, Oster/E-value)
【Next】pubar-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design/identification packages (R/Stata/Python) and CAQDAS for qualitative work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — pre-registration badges and TOP notes
