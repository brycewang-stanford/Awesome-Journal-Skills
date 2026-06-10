---
name: red-topic-selection
description: Use when testing whether a research question fits the Review of Economic Dynamics (RED) — a journal whose scope is defined by method and lens (dynamic, quantitative economics) rather than subfield. Helps decide if the paper studies a genuinely dynamic mechanism through a dynamic model, and whether it belongs at RED versus a generalist or a specialist outlet.
---

# Topic Selection for RED (red-topic-selection)

## When to trigger

- Deciding whether a paper is "a RED paper" before investing in it
- A dynamic-macro idea that could also go to a general-interest or a field journal
- Worried the question is too static, too purely empirical, or too applied-micro for RED's lens

## What RED actually wants

RED publishes meritorious original contributions to **dynamic economics**, and its scope is set by
**method/lens, not subfield**. In-scope work studies a mechanism through a **dynamic model** — and that
model may be **theoretical, computational, or empirical**:

- Dynamic general-equilibrium (DSGE) and heterogeneous-agent models
- Growth, business cycles, and economic fluctuations
- Labor dynamics, search/matching, human capital over the life cycle
- Monetary and fiscal policy in dynamic environments
- International macro and open-economy dynamics
- Any area of economics where the dynamics are the point and a dynamic model carries the argument

Crucially, **heavily computational quantitative work is squarely in scope** — RED is one of the natural
homes for simulation-intensive macro. The SED community (the people behind the SED Annual Meetings) is
the readership; pitch to them.

## Quick fit test

- [ ] Is the **dynamic mechanism** the core contribution (not incidental)?
- [ ] Does a **dynamic model** carry the argument (theory, computation, or empirical dynamics)?
- [ ] Would the **SED audience** see this as advancing dynamic economics?
- [ ] Is the contribution quantitative/structural rather than a one-off reduced-form correlation?

If the dynamics are cosmetic, or the paper is a static cross-section, RED is likely the wrong lens —
reframe around the dynamic mechanism or choose another venue.

## Wrong-venue redirects

- Mostly reduced-form policy estimate with no dynamic model -> field journal or applied-economics outlet.
- Pure econometric method with no dynamic-economics object -> methods/econometrics outlet.
- Broad macro paper whose contribution is policy relevance rather than dynamic mechanism -> generalist macro
  or policy journal.
- Calibration exercise with no new mechanism, method, or disciplined moment -> revise before targeting RED.

## Dynamic-mechanism test

Write the candidate contribution in this form:

```text
Because [state variable] evolves through [law of motion/friction], [shock/policy/choice] changes
[future object], generating [quantitative/theoretical implication].
```

If the sentence still works after deleting the law of motion, the paper may not be a RED paper. If the
result depends on dynamics but the model is not disciplined by moments, proofs, or computation, route to
`red-data-analysis` before drafting.

## Fit-scoring pass

Score each dimension 0–2 before committing the project to RED:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Dynamics | static comparison | dynamics present but incidental | transition/fluctuation is the object |
| Model | none or a sketch | calibrated model supports a side result | dynamic model carries the headline claim |
| Discipline | parameters chosen freely | partial targets | explicit calibration/estimation against moments |
| Audience | generalist or policy | field-adjacent | SED community would discuss it at the Annual Meeting |

Illustrative read: 7–8 → proceed; 5–6 → strengthen the weak dimension first (usually Discipline); ≤4 →
re-scope or pick another venue. The thresholds are working heuristics, not journal policy.

## Scoring vignette: a household-finance idea

"Mortgage refinancing frictions and consumption." Version A regresses spending on rate gaps: Dynamics 1,
Model 0, Discipline 0, Audience 1 → not a RED paper. Version B builds a life-cycle model with a fixed
refinancing cost, calibrates that cost to observed refinancing hazards, and quantifies the mortgage
channel of monetary transmission: Dynamics 2, Model 2, Discipline 2, Audience 2 → squarely in scope. Same
topic, different lens — the venue decision turns on version B's dynamic model, not on the subject matter.

## Anti-patterns

- Bolting a token dynamic equation onto an essentially static result
- Assuming RED only takes theory, or only takes empirics (it takes both, through a dynamic lens)
- Pitching to a generalist audience instead of the SED community

## Output format

```text
[RED fit] strong / possible / weak
[Dynamic mechanism] <state variable, law of motion, or equilibrium force>
[Model discipline] theory / computation / calibration / estimation / missing
[Best route] RED / generalist macro / field journal / methods outlet
[Next step] red-contribution-framing or red-data-analysis
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — RED scope sources
