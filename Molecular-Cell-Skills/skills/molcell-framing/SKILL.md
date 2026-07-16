---
name: molcell-framing
description: Use to lock the single-mechanism arc before drafting — converts a set of correct experiments into one Molecular Cell story that runs molecular question → the mechanism → physiological consequence, not a catalog of techniques.
---

# Single-Mechanism Framing (molcell-framing)

## When to trigger

- The experiments are solid but the manuscript reads as "we did ChIP-seq, then crystallography, then a knockout."
- The introduction opens with pages of background before the molecular question.
- Colleagues ask "what is the one molecular event this paper proves?"
- You can list the assays but not the single mechanism they establish.

## Molecular Cell tells ONE mechanistic story

A Molecular Cell Article is a single argument that resolves one molecular question:

> **Molecular question → the mechanism we proved → why it matters physiologically.**

Every figure is a step in proving that one mechanism. Data that don't serve the mechanism belong in Supplemental Information or a different paper. Force the whole paper into one sentence:

> "We show that **[molecular actor]** **[does what, at what level of detail]**, which explains **[process]** and is required for **[physiological outcome]**."

If you cannot fill all three brackets with a *molecular* mechanism (a residue, a base, an interface, a step), the framing is not ready — and possibly the mechanism is not complete (`molcell-fit`).

## Map figures to the proof of mechanism

Molecular Cell readers expect the argument to feel airtight: each mechanistic claim is set up, tested by orthogonal methods, and alternatives are excluded before you move on.

1. **Fig. 1** — establish the phenomenon and pose the molecular question.
2. **Figs. 2–3** — define the mechanism (structure / biochemistry / reconstitution: the molecular event).
3. **Fig. 4** — separation-of-function: point mutants that break *only* the mechanism, tying it to the phenotype.
4. **Figs. 5–6** — physiological relevance (in cells / in vivo) and generality.

If the separation-of-function figure is missing, reviewers will demand it — better to see the gap now.

## Molecular Cell introduction shape (~3 short paragraphs)

1. **The molecular problem** — the process and the specific step that is not understood.
2. **The gap / hypothesis** — what molecular event is unknown, and the question you pose.
3. **What we found** — the mechanism in molecular terms, ending on the physiological consequence. The reader knows the mechanism before Results.

Molecular Cell introductions are shorter and more focused than *Cell*'s — you are addressing molecular biologists, not a general readership, so open at the level of the mechanism, not the disease.

## The "why now" hooks

Name which applies:

- [ ] A method makes the molecular step visible (cryo-EM at near-atomic resolution, single-molecule, ribosome profiling, nanopore, cross-linking MS).
- [ ] A reconstituted system finally isolates the activity from cellular confounds.
- [ ] A separation-of-function allele lets you test the mechanism without pleiotropy.
- [ ] A longstanding molecular controversy is now decidable.

## Title discipline

- **Declarative and mechanistic**: "PROTEIN X unwinds Y by mechanism Z" beats "Insights into Y."
- The noun phrase names the molecular actor and the molecular action, not just the system.
- Avoid "Towards", "A study of", "Characterization of", "Role of", "Novel".
- Molecular Cell titles often name the complex and the molecular verb (binds, unwinds, methylates, degrades, licenses).

## Narrative anti-frames (rewrite these)

| Anti-frame                                       | Reframe                                                     |
|--------------------------------------------------|------------------------------------------------------------|
| "We characterized complex X."                    | "Complex X licenses step Y by clamping substrate Z."       |
| "Here we report several findings on…"            | "We define the molecular mechanism by which…"              |
| A technique catalog (ChIP-seq, then structure…)  | One mechanism; each method is a converging line of proof   |
| "Our data are consistent with model M."          | "Point mutants that break only step S decide for model M." |
| "Structure reveals a novel fold."                | "The structure explains how X selects substrate Y."        |

## Output format

```
【One-sentence mechanism】 "We show that [actor] [molecular action], which explains ... and is required for ..."
【Figure-to-proof map】 phenomenon / mechanism / separation-of-function / physiological relevance
【Why-now hook】 which applies
【Intro skeleton】 molecular problem / gap / mechanism+consequence
【Working title】 declarative, names the molecular actor + action
【Risk】 any step of the proof missing? (→ molcell-fit)
【Next】 molcell-writing
```

## Anti-patterns

- **Do not** present parallel technique mini-stories — Molecular Cell wants one mechanism.
- **Do not** bury the mechanism below background; molecular biologists want it in the first paragraphs.
- **Do not** inflate with "novel/unprecedented" — prove the molecular step, don't label it.
- **Do not** frame a structure paper around the fold; frame it around the mechanism it decides.

> Confirm structural expectations against the current Molecular Cell information-for-authors page.
