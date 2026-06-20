---
name: jais-theory-development
description: Use when building the theoretical engine of a Journal of the Association for Information Systems (JAIS) manuscript — original theory for the Theory category, a behavioral mechanism, an economic mechanism, a design theory, or a pre-theoretical framing for a novel digital phenomenon. Adapts the form of "theory" to the category and tradition; it does not run the analysis (jais-data-analysis) or frame the contribution (jais-contribution-framing).
---

# Theory Development (jais-theory-development)

## When to trigger

- Your claims are descriptive ("A is associated with B") with no IS mechanism
- You are targeting the **Theory** category and need a genuinely *new* construct or framework, not a relabeled import
- You built an IT artifact but cannot say what generalizable **design knowledge** it embodies
- A Senior Editor or reviewer says "the theoretical contribution is unclear" or "this is a borrowed-theory application"
- You have a novel digital phenomenon and need a disciplined pre-theoretical framing

## Why theory carries more weight at JAIS

JAIS is the AIS flagship and the Basket journal that treats **theory as a contribution in its own right** — it runs a standalone Theory category for "original theory" that proposes new concepts or integrates existing theories into novel frameworks. Even in empirical Research Articles, JAIS **discourages primary construct development** as the headline move — meaning a paper whose contribution *is* a new construct usually belongs in Theory, not as a bolt-on to a Research Article. This is the JAIS-specific discipline: name your theoretical genre, then build to that genre's bar.

## Theory takes a different shape by genre — pick your row

| Genre | What "theory" means here | What you must produce |
|-------|--------------------------|------------------------|
| **Theory category (conceptual)** | a new construct, a novel framework, or a novel theory integration | the construct's definition + nomological net, OR the integrative framework and its boundary conditions, with generative propositions |
| **Behavioral** | a causal mechanism linking IT to cognition, behavior, or outcomes | a priori hypotheses with an explicit mechanism, mediation/moderation logic, and boundary conditions |
| **Economics of IS** | an economic mechanism (incentives, information, matching, network effects) | a model or argument yielding signed, falsifiable predictions and an identification logic |
| **Design science** | a *design theory* — the principles that make the artifact work | kernel/justificatory theory, generalizable design principles, and testable utility propositions |
| **Foundational / novel phenomenon** | a pre-theoretical conceptualization of something not yet studied | a careful conceptual vocabulary and the insight it surfaces — over-theorizing too early is itself a flaw here |

## Build a *new* construct properly (the Theory-category trap)

A relabeled existing construct is the most common Theory desk-reject. To clear the bar: define the construct precisely; distinguish it from its nearest neighbors (discriminant logic, not just a new name); specify its dimensions and how it would be measured; and embed it in a nomological net of antecedents and consequences. JAIS reviewers reward a construct that *does work* the field's existing vocabulary cannot.

## Cross- and inter-disciplinary borrowing is a feature, used correctly

JAIS explicitly "encourages theory based multi- or inter-disciplinary research," so importing from economics, psychology, sociology, organization theory, or computer science is welcome — but the import must be transformed by the IS context. The strongest theory papers run a *round trip*: they borrow a theory, show how a digital phenomenon breaks or extends one of its assumptions, and return a revised theory that the source discipline would also find new. A one-way import ("we apply self-determination theory to app use") is the weak version; a round trip ("autonomous AI agents violate self-determination theory's assumption that competence is self-earned, requiring a revised account of motivation under delegated competence") is the JAIS version.

## Integrate theories without flattening them

A "novel integration" must change what each source theory predicts, not staple them side by side. State the tension or gap between the theories, then show how the integration resolves it and yields predictions neither theory makes alone. Multi- or inter-disciplinary borrowing is encouraged — but the IS phenomenon must reshape the borrowed theory, not merely host it.

## Derive claims before you look at results

Whatever the genre, JAIS expects the theoretical logic to *precede* the evidence. State the mechanism in words — what is the IT-enabled force, on whom, through what channel, and when does it reverse — then write the hypotheses (behavioral), comparative-statics predictions (economics), or design propositions (design science) that follow from it. Theorize mediation as a channel and moderation as a reason the IT effect strengthens or weakens, rather than as terms you happen to test. Predictions that merely restate correlations the data already revealed are HARKing, and a developmental Senior Editor will read the seams.

## Make boundary conditions and the IT artifact load-bearing

IS effects are contingent on the artifact, the user, the task, and the context. Name where the theory holds and where it breaks, and ensure the technology is *in* the mechanism (not an interchangeable treatment). A theorized scope condition beats an over-claimed universal law.

## Checklist

- [ ] The genre's correct *form* of theory is used (new construct / framework / mechanism / design theory / pre-theoretical framing)
- [ ] If a new construct: defined, discriminated from neighbors, dimensionalized, embedded in a nomological net
- [ ] If an integration: the tension is named and the synthesis yields predictions neither parent makes
- [ ] The IT artifact / digital phenomenon is load-bearing in the mechanism, not decorative
- [ ] Hypotheses / propositions / design propositions are derived *before* results (no HARKing)
- [ ] Boundary conditions and scope are stated
- [ ] The genre matches the chosen JAIS category (construct-first → Theory, not Research Article)
- [ ] Any borrowed reference-discipline theory is revised by the IS context (a round trip, not a one-way import)

## Referee pushback mapped to the theory fix

- *"This is a relabeled existing construct."* → Add discriminant logic: define your construct against its nearest neighbors, give its dimensions, and show the work it does that the existing vocabulary cannot.
- *"The integration just staples two theories together."* → Name the tension between them and derive a prediction neither parent makes alone; if there is none, you have a literature summary, not a theory.
- *"The technology is interchangeable here."* → Put the artifact's specific affordances *inside* the mechanism so swapping the technology would change the prediction.
- *"This belongs in a Research Article, not Theory."* (or vice versa) → Re-match the genre to the category; a construct-first paper is Theory, a theory-test is a Research Article.

## Worked vignette: building a construct for the Theory category (illustrative)

A team wants to theorize how always-on AI copilots change knowledge work. A weak Theory submission relabels "technostress" as "AI-stress" and stops. A JAIS-grade move defines a genuinely new construct — say, *delegation ambivalence*, the simultaneous pull to offload cognition to the copilot and the felt loss of authorship over the output. It is discriminated from technostress (which is about overload, not authorship), dimensionalized (offloading intensity × authorship threat), and embedded in a net: antecedents in the copilot's proactivity and the task's identity-relevance, consequences in trust calibration and skill atrophy. Generative propositions follow that neither the technostress literature nor the automation literature predicts. *That* is a Theory-category contribution; the same idea bolted onto a survey would be discouraged as primary construct development in a Research Article.

## Anti-patterns

- "We applied [theory X] to [setting Y]" with no new IS mechanism — a borrowed-theory application.
- A "new construct" that is an existing one with a fresh label and no discriminant logic.
- A Theory-category submission that summarizes literature instead of producing generative theory.
- A design-science paper with an artifact but no generalizable design principles.
- Over-theorizing a Foundational/novel-phenomenon paper before it has been carefully described.

## Output format

```text
【Genre & theory form】new construct / framework / behavioral mechanism / economic model / design theory / pre-theoretical
【JAIS category fit】Theory / Research Article / Foundational / Literature Review
【Core mechanism or construct】IT-enabled force → on whom → through what channel (or construct definition + net)
【Claims】H1..Hn / propositions P1..Pn / signed predictions
【Boundary conditions】where it holds / reverses
【Source status】verified URL / 待核实
【Next skill】jais-literature-positioning
```
