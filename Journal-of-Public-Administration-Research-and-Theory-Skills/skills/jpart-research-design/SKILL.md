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
【Rival ruled out】the adjudication sentence (often selection / common-method)
【Preregistered?】confirmatory vs exploratory split
【Next】jpart-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — experiment/causal packages (R/Stata/Python) and survey platforms
- [`../../resources/code/`](../../resources/code/) — reproducible DiD/IV/RDD/DML skeleton to adapt
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — preregistration / blinded pre-reg report policy
