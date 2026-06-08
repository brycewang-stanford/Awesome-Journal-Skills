> **Illustrative teaching example.** The paper, model, setting, and every number below are **fictional**
> and exist only to demonstrate RED house style. No real-paper facts are stated, and no policy is invented.
> Corresponding skills: [`red-writing-style`](../../skills/red-writing-style/SKILL.md),
> [`red-contribution-framing`](../../skills/red-contribution-framing/SKILL.md), and
> [`red-topic-selection`](../../skills/red-topic-selection/SKILL.md).

# Worked Example: A RED-Style Introduction (before → after)

This demonstrates the **RED introduction discipline** distilled from this pack's own skills:
**make the dynamic mechanism legible before the math** (`red-writing-style`), lead with **one dominant
contribution stated as a quantitative/mechanistic delta against the closest existing model**
(`red-contribution-framing`), and pitch to the **SED / dynamic-economics readership** with a genuinely
*dynamic* mechanism carried by a *dynamic model* (`red-topic-selection`). The arc:
**question → dynamic mechanism in words → model & what turns the mechanism on → headline magnitude and the
moment it matches → contribution as a delta → brief roadmap.**

**Illustrative paper (fictional):** *"Slow-Moving Skill and the Persistence of Earnings Losses: A
Heterogeneous-Agent Model of Displacement over the Life Cycle."* Fictional setting: a calibrated
incomplete-markets life-cycle economy in which displaced workers depreciate firm-specific human capital
that rebuilds only gradually.

---

## Before (buries the mechanism — typical first-draft intro)

> The consequences of job displacement have been studied extensively in macroeconomics and labor
> economics. In this paper, we build a heterogeneous-agent incomplete-markets model with idiosyncratic
> productivity risk, solved with the Krusell–Smith algorithm and value-function iteration on a
> discretized grid. We calibrate the model to standard moments and run a number of experiments. We find
> that displacement matters for welfare. The model has many state variables and is computationally
> intensive to solve. Section 2 reviews the literature, Section 3 lays out the environment, Section 4
> describes the calibration, Section 5 presents results, and Section 6 concludes.

**What's wrong (against this pack's skills):**

- **Leads with the solution method** ("solved with the Krusell–Smith algorithm... value-function
  iteration") instead of the dynamic mechanism — the exact inversion `red-writing-style` warns against
  ("make the mechanism legible before the math").
- **No dynamic mechanism in words.** A reader cannot tell *what dynamic force* the paper is about, or why
  a static model would miss it — fails the `red-topic-selection` fit test ("is the dynamic mechanism the
  core contribution, not incidental?").
- **No headline magnitude and no moment matched.** "Displacement matters for welfare" hides the number;
  `red-contribution-framing` requires the advance "as a quantitative/mechanistic delta with a magnitude."
- **Contribution is a description of the paper** ("we run a number of experiments"), not a delta against
  the closest existing model — a named anti-pattern.
- **Throat-clearing** ("has been studied extensively") and an **over-signposted roadmap** doing the work
  the argument should do.

---

## After (RED arc — mechanism legible before the math, contribution as a delta)

> **Why do the earnings losses from job displacement fade so slowly — and how much of the welfare cost is
> hidden in the speed of recovery rather than its depth?** We show that when displaced workers lose
> firm-specific skill that rebuilds only gradually, the welfare cost of displacement is **42% larger**
> than a model with a one-time wage drop implies, because the slow-moving state keeps consumption
> depressed long after re-employment. *(question + headline magnitude + why it matters, in the first
> breath — the mechanism, not the method, leads.)*
>
> The dynamic force is a **slow-moving skill state**: displacement destroys a stock of firm-specific
> human capital, and because that stock rebuilds only as fast as on-the-job learning allows, a worker's
> wage — and, under incomplete markets, their consumption — recovers along a protracted path rather than
> jumping back. A static or one-shot-loss model collapses this path to a point and misses where the
> welfare cost actually sits. *(mechanism in plain words, before any equation — `red-writing-style`.)*
>
> We embed this in a **life-cycle incomplete-markets economy** with idiosyncratic displacement risk,
> where the skill state evolves on its own clock. The mechanism *turns on* exactly when two model
> elements coincide: slow skill rebuilding and limited self-insurance; shut either off and the protracted
> consumption response disappears. *(model & what switches the mechanism on — the
> `red-contribution-framing` "show what turns it on" discipline.)*
>
> Calibrated to match the **observed half-life of post-displacement earnings recovery**, the model
> delivers a welfare cost of displacement **42% above** the one-time-loss benchmark, and attributes
> **two-thirds** of that gap to the *speed* of skill recovery rather than its *depth*. *(headline
> magnitude restated with the moment it matches — the calibration target stated precisely and early.)*
>
> Our contribution is to identify the **rate of skill recovery, not just the size of the wage loss**, as
> the margin that governs the welfare cost of displacement — a delta against the closest existing model,
> which treats displacement as a permanent wage cut and therefore cannot speak to recovery dynamics at
> all. *(contribution as a quantitative/mechanistic delta against the closest model, not a tour of
> results.)*
>
> The paper proceeds as follows. Section 2 lays out the environment and the skill-accumulation block;
> Section 3 presents the calibration and the main quantitative results; Section 4 isolates the mechanism
> by switching off slow recovery. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the RED bar

Mapped to the skill checklists:

- **Mechanism legible before the math** — the slow-moving skill state is described in words in the second
  paragraph, before any model object is defined (`red-writing-style`: "make the mechanism legible before
  the math"; "state magnitudes... early and precisely").
- **One dominant contribution, stated as a delta** — "rate of recovery, not just size of the loss,"
  framed against the closest existing model rather than as a description of the paper
  (`red-contribution-framing`: "state the contribution as a delta against the closest existing model").
- **Headline magnitude with the moment it matches** — the 42% welfare gap appears immediately, and the
  calibration target (the earnings-recovery half-life) is named, satisfying the "lead with the number and
  the moment it matches" rule.
- **Genuinely dynamic mechanism carried by a dynamic model** — the contribution *is* the dynamics (a
  slow-moving state); shutting off the dynamics kills the result, passing the `red-topic-selection` fit
  test rather than bolting a token dynamic equation onto a static result.
- **Pitched to the SED audience** — a heterogeneous-agent, incomplete-markets, life-cycle quantitative
  model is squarely the readership's lens; the method (solution algorithm) is demoted to where it belongs,
  in the model section, never as the lead.
- **No diffuse result list** — a single advance carries the abstract and intro, as
  `red-contribution-framing` requires ("no diffuse 'we also do X, Y, Z'").

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **verified real RED papers** whose
> introductions execute this dynamic-mechanism-first arc, and [`../code/`](../code/) for the empirical
> command chains referenced when a RED paper disciplines its model with reduced-form dynamics. For
> cross-cutting reporting and identification stakes, the shared hub is at
> [`../../../shared-resources/empirical-methods/reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md).
