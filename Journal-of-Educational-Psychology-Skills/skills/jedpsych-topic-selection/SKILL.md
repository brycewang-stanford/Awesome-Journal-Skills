---
name: jedpsych-topic-selection
description: Use when deciding whether an educational-psychology project fits the Journal of Educational Psychology and which manuscript type to target. JEP wants original, primary psychological research on learning and instruction that matters for real educational settings; it does not typically publish single-instrument reliability/validity studies. Frames the question; it does not collect data.
---

# Topic Selection & Fit (jedpsych-topic-selection)

The Journal of Educational Psychology publishes **original, primary psychological research pertaining to
education across all ages and educational levels** (检索于 2026-06；以官网为准). The bar is a finding
that is **theoretically grounded**, **methodologically rigorous**, and **educationally consequential** —
it should change how psychologists understand learning, motivation, achievement, or instruction *and*
matter for learners in schools, classrooms, or online settings. Use this skill to pressure-test fit
before investing.

## When to trigger

- Choosing among possible projects or framings for JEP
- A reader said the work feels "atheoretical," "not educational," or "just a lab effect"
- Deciding between a single study, a multi-study package, or a meta-analysis
- Unsure whether a measurement/validation paper belongs here (it usually does not)

## The fit test

A strong JEP paper usually clears all four:

1. **Educational relevance.** The phenomenon is about learning, motivation, engagement, achievement,
   reading/math/science learning, assessment, self-regulation, or instruction — and the result has a
   defensible implication for educational practice or policy. State who in education inherits the claim.
2. **Psychological theory.** A learning/motivation/cognitive mechanism predicts the effect; this is a
   *psychological* research journal, not a program-evaluation outlet (see `jedpsych-theory-and-hypotheses`).
3. **Rigor for the setting.** Adequately powered for its design — and if students are nested in classes
   or schools, the design and analysis must respect that nesting (see `jedpsych-study-design`,
   `jedpsych-data-analysis`).
4. **Ecological validity.** It speaks to real educational contexts, not only a stripped lab analog —
   field trials, authentic tasks, and real learners strengthen fit.

## Manuscript type

- **Primary empirical article** — a completed experiment, randomized field trial, quasi-experiment, or
  longitudinal study with a learning-relevant outcome.
- **Multi-study article** — several studies that build one cumulative claim (lab → classroom, mechanism
  → boundary, replication → extension); each study must add inference.
- **Meta-analysis** — published **occasionally**, only for **exceptionally important** syntheses
  pertinent to educational psychology; follow APA meta-analysis reporting standards.
- **Out of scope (usually):** reliability/validity studies of a specific test or instrument.

## Fit scoring — worked example (illustrative)

Score a candidate against the four gates before investing. A reading-intervention project, two framings:

```
Candidate A (off-fit): a lab study showing a memory-encoding effect on word
            lists, N = 60 undergraduates, no link to instruction.
  Educational relevance ✗   Theory ✓   Rigor ~ (small)   Ecological ✗
  Verdict: off-fit for JEP → general cognition outlet, or rebuild as a
           classroom learning study with an instructional implication.

Candidate B (strong): cluster-randomized comprehension-strategy intervention,
            48 classrooms (~1,100 students), pretest covariate, transfer outcome.
  Educational relevance ✓ (classroom reading) Theory ✓ (strategy-instruction
  mechanism)  Rigor ✓ (cluster-powered)  Ecological ✓ (real classrooms)
  Verdict: strong fit → primary empirical article.
```

## Manuscript-type decision rules

| If the work is... | Target type | Why |
|-------------------|-------------|-----|
| One completed learning study, results in hand | Primary empirical article | the standard JEP slot |
| A cumulative claim built across studies | Multi-study article | each study must add inference, not repeat |
| A prospective classroom/school trial, not yet run | Primary article (preregister) | settle nesting + power before recruiting |
| A field-defining quantitative synthesis | Meta-analysis | only if "exceptionally important"; follow MARS |
| Validation of one instrument | Specialty measurement journal | JEP does not typically publish these |

## Reviewer / editor pushback at the fit stage

- "Interesting psychology, but where is the education?" → name the instructional or policy implication and
  the real-setting evidence; if there is none, the venue is wrong.
- "This is program evaluation, not psychological research" → foreground the learning/motivation mechanism
  the study tests, not just whether the program worked.
- "Underpowered for a classroom effect" → power at the level of randomization; a student-level N hides a
  small number of clusters (route to `jedpsych-study-design`).

## Anti-patterns

- A lab effect with no plausible bridge to learning or instruction
- A pure program evaluation with no psychological mechanism or theory
- A single-instrument reliability/validity paper (out of scope)
- A classroom study powered and pitched as if students were independent
- A meta-analysis pitched as routine rather than field-defining

## Output format

```
【Question / effect】one sentence
【Educational relevance】who in education inherits the claim
【Theory】the learning/motivation mechanism
【Rigor + setting】powered for its design? ecologically valid?
【Type】Primary empirical / Multi-study / Meta-analysis
【Fit verdict】strong / needs reframing / off-fit (why)
【Next】jedpsych-theory-and-hypotheses
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — power for nested designs, preregistration tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JEP aims, scope, and accepted manuscript types
