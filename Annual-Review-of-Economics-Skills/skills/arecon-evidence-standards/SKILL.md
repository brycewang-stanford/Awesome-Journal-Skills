---
name: arecon-evidence-standards
description: Use when appraising the credibility of the primary studies an Annual Review of Economics (ARE) review synthesizes, and when calibrating comprehensiveness, balance, and fair treatment of competing views. Weighs evidence and audits even-handedness; it does not design the spine (arecon-organizing-framework) or run your own identification.
---

# Evidence Appraisal & Balance (arecon-evidence-standards)

## When to trigger

- The framework is set and you are filling cells with conflicting empirical results
- You must decide whether "the literature finds X" is actually supported, or only loosely
- The field has rival schools, a live controversy, or estimates that disagree
- You are a contributor to this literature and worry the review tilts toward your own work

## Appraising evidence you did not produce

An ARE review **runs no identification of its own** — there is no design to defend, no replication package of your data. Instead you act as the field's **referee-of-record for adjacent readers**: you judge how much weight each primary study can bear so the review weighs the evidence correctly. Make the appraisal explicit, not implicit:

- **DID / event study:** does the cited paper use TWFE on staggered timing without addressing heterogeneity bias? A study that predates Callaway–Sant'Anna / Sun–Abraham corrections may not support the magnitude you attribute to it — flag it.
- **IV:** is the first stage strong and the exclusion restriction defended, or is it a convenience instrument? Weak-IV results carry less weight in your synthesis.
- **RDD:** density/manipulation checks, bandwidth robustness — a fragile RDD is a fragile data point.
- **Structural / calibration:** are the parameters identified and the counterfactual policy-invariant, or is it calibration presented as estimation?
- **Experiments:** pre-registration, balance, attrition, multiple-hypothesis adjustment, external validity.

You are not re-running these — you are **rating their credibility** in the evidence matrix so the review's conclusions track the *best* evidence, not the *loudest* paper.

## Weighing, not vote-counting

Conflicting results are reconciled by **credibility and by what each study estimates**, never by tallying "7 studies positive, 4 negative." Two estimates that disagree often measure different objects (different populations, estimands, time horizons); say so, and let the framework's cells carry the distinction. A pooled "consensus" across non-comparable designs manufactures false agreement that ARE's methodologically literate readers will catch.

## Comprehensiveness vs. selectivity: the ARE contract

A review must be **comprehensive in coverage** yet **selective in emphasis** — and stay accessible in ~25–40 pages. Tier the corpus:

| Tier | Treatment |
|------|-----------|
| **Foundational / field-defining** | discussed in text, with what they established and their limits |
| **Important contributions** | grouped and weighed within framework cells; cited with their finding |
| **Confirmatory / incremental** | cited in clusters ("see also …") to show coverage without bloating prose |
| **Tangential** | cited only where they bear on a specific claim |

Comprehensiveness is proven by the citation set + saturation log (`arecon-literature-synthesis`); selectivity is exercised in the prose.

## Fairness and the self-citation trap

ARE referees are frequently the surveyed authors themselves, so balance is strategic as well as ethical:

- **Steelman every camp.** State each school's strongest case in terms its proponents would accept *before* noting weaknesses.
- **Attribute ideas to originators**, not popularizers (a recurring referee complaint).
- **Handle live controversies without resolving by fiat.** Lay out the disagreement, what evidence would settle it, and where your own read sits — labelled as *your read*, not as consensus.
- **Audit self-citation.** Your own work appears at the tier its importance to the field warrants — no more; rivals get their strongest statement; a reader who does not know the author cannot tell from the emphasis.

## Checklist

- [ ] Each pivotal primary study carries a credibility appraisal (design, identification, robustness)
- [ ] Outdated or fragile designs flagged where the review leans on their magnitudes
- [ ] Conflicting findings reconciled by credibility + estimand, not vote-counting
- [ ] Corpus tiered; prose emphasis matches tier; coverage provable from the saturation log
- [ ] Every rival school stated at its strongest before critique (steelman)
- [ ] Idea attribution traces to originators
- [ ] Live controversies presented with what evidence would settle them; author's read labelled
- [ ] Self-citation audited: own work at warranted tier; emphasis is identity-blind

## Anti-patterns

- Citing a study's headline number without noting its identification is now known to be biased
- Vote-counting conflicting results instead of weighing credibility and estimand
- Pooling non-comparable estimates into one "the literature shows…" magnitude
- Comprehensiveness theatre: equal-length summaries of every paper (no editorial judgment)
- Strawmanning the camp the author disagrees with
- A review that doubles as the author's CV (the most-punished ARE balance failure)
- Declaring a live controversy "resolved" by assertion rather than the evidentiary state

## Output format

```text
【Credibility appraisal】pivotal studies rated (design/identification/robustness)? Y/N
【Conflict handling】reconciled by credibility + estimand (not vote-count)? Y/N
【Tiering】corpus split foundational/important/confirmatory/tangential? Y/N
【Comprehensiveness】saturation log supports "nothing important missing"? Y/N
【Steelman】each rival school stated at its strongest? Y/N
【Controversy】evidence-to-settle stated; author's read labelled? Y/N
【Self-citation audit】own work at warranted tier; emphasis identity-blind? Y/N
【Next step】→ arecon-tables-figures (who-found-what tables) → arecon-writing-style
```
