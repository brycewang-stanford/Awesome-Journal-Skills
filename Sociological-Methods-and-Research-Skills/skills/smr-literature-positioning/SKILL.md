---
name: smr-literature-positioning
description: Use when positioning a Sociological Methods & Research (SMR) manuscript against the methods literature across sociology, statistics, econometrics, psychometrics, and computational social science, and avoiding sibling-journal misattribution. Maps the contribution onto prior methods; does not derive or simulate.
---

# SMR Literature Positioning

Use this to place the contribution in the *methods* literature, not the substantive one. SMR
reviewers are methodologists who often know the closest prior estimator, the original derivation, and
the competing approach in a neighboring discipline. A missed precedent is the fastest path to a
reject.

## Position against methods, not findings

The literature review of an SMR paper answers "what is the closest *method*, and how is yours
different?" — not "what is known about the substantive topic." Structure the review as a small map:

- **Direct ancestors**: the method(s) your contribution extends, corrects, or replaces. Cite the
  primary source, not a textbook summary.
- **Cross-discipline siblings**: the same problem solved in statistics, econometrics, psychometrics,
  machine learning, or network science. SMR readers expect you to know that a "new" sociology method
  may already exist under another name elsewhere.
- **Competing methods**: the alternatives a reviewer will demand you beat in simulation. Name them
  here so the comparison set in `smr-simulation-studies` is not a surprise.

## The precedent audit

Run this before drafting the review:

- Search the **original** statistical literature, not just sociology — many SEM, latent-variable,
  multilevel, missing-data, and causal-inference tools originate in statistics/psychometrics.
- For each near-neighbor, write one line: *what they do, what you do differently, why the difference
  matters*. If you cannot state the difference, you have not yet differentiated the contribution.
- Distinguish **re-derivation** from **novelty**: presenting a known result as new is a credibility
  killer at a methods venue. If you rediscovered something, say so and add what is genuinely new.

## Cross-field translation table

| Sociology framing | Likely prior literature to check | Risk if missed |
|---|---|---|
| Causal effect with controls | statistics (potential outcomes, DAGs), econometrics | "good/bad controls" already settled elsewhere |
| Latent classes / trajectories | psychometrics, biostatistics (finite mixtures, GBTM) | reinventing a named model |
| Measurement invariance | psychometrics (MGCFA, alignment) | overstating a known non-invariance result |
| Missing data | statistics (MI, IPW, FIML), biostatistics | ignoring the standard estimator |
| Network effects | network science, spatial econometrics | a known identification problem |
| Text-as-data | NLP, computational linguistics, comp. social science | a method already standard in CSS |

## Sibling-journal misattribution guard

When citing "where methods like this are published," be precise:

- *Sociological Methodology* (ASA annual) ≠ **Sociological Methods & Research** (SAGE). Do not
  conflate them in the cover letter or positioning.
- *Psychological Methods* (APA), *Political Analysis*, *Structural Equation Modeling*, and the
  *Journal of Educational and Behavioral Statistics* are neighbors, not SMR. Attribute exemplar
  papers to the correct venue (see `resources/exemplars/library.md`).

## Checklist

- [ ] Direct method ancestors are cited from primary sources, not textbooks.
- [ ] Cross-discipline siblings (statistics/psychometrics/econometrics/CSS) were searched and cited.
- [ ] Each near-neighbor has a one-line "what they do / what you do / why it matters."
- [ ] The simulation comparison set is foreshadowed in the review.
- [ ] No known result is presented as novel; re-derivations are flagged.
- [ ] Sibling journals are attributed correctly; no SMR/Sociological Methodology conflation.

## Anti-patterns

- **Substantive review in a methods paper**: paragraphs on the topic instead of on the method.
- **Sociology-only search**: missing the statistics/psychometrics origin of the method.
- **Textbook citation for a primary result**: citing a handbook instead of the derivation.
- **Strawman map**: omitting the strongest competitor so the simulation looks favorable.
- **Venue confusion**: attributing a *Sociological Methodology* or *Psychological Methods* paper to SMR.

## Output format

```text
[Direct ancestors] <method -> your difference>
[Cross-discipline siblings] <field : closest prior + difference>
[Competing methods to beat] <named alternatives for the simulation>
[Precedent risks] <any near-rediscovery to disclose>
[Next SMR skill] smr-derivation-and-properties
```
