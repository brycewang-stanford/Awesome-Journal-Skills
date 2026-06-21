---
name: ppsych-comprehensiveness-and-balance
description: Use when appraising the credibility of the studies a Perspectives on Psychological Science (PoPS) piece synthesizes and calibrating comprehensiveness, balance, and fair treatment of competing camps — including reform-minded but evidence-based critique. Weighs evidence and audits even-handedness; it does not design the spine (ppsych-organizing-framework) or run new analyses.
---

# Comprehensiveness & Balance (ppsych-comprehensiveness-and-balance)

## When to trigger

- The framework is set and you are filling cells with conflicting findings from different areas
- You must decide whether "the field finds X" is actually supported, or only loosely
- The topic has rival schools, a live controversy, or a replication/reform debate
- You are a contributor to this literature and worry the piece tilts toward your own work or your camp's reform agenda

## Appraising evidence you did not produce

A PoPS piece **runs no study of its own** (unless it is a meta-analysis with a superordinate message). You act as the field's **referee-of-record for cross-area readers**: judge how much weight each study can bear so the synthesis weighs evidence correctly. Make the appraisal explicit:

- **Power & sample.** Is the cited effect from an adequately powered design, or a small-N study likely to be inflated? Underpowered originals support weaker claims.
- **Replication status.** Has it replicated (direct or close)? A failed-to-replicate headline cannot anchor a "the field knows X" claim — flag it.
- **Preregistration & flexibility.** Was the analysis preregistered, or could researcher degrees of freedom explain it? Exploratory ≠ confirmatory.
- **Construct validity & generalizability.** Does the measure capture the construct, and does the sample (often WEIRD) support the breadth of the claim?
- **Publication bias.** Is the effect from a literature with funnel asymmetry / p-curve problems? Weight accordingly.

You are not re-running these — you are **rating their credibility** in the evidence matrix so the piece's conclusions track the *best* evidence, not the *loudest* finding.

## Weighing, not vote-counting

Conflicting results are reconciled by **credibility and by what each study measures**, never by tallying "9 studies positive, 4 null." Two effects that disagree often tap different constructs, populations, or moderators; say so, and let the framework's cells carry the distinction. A pooled "consensus" across non-comparable designs manufactures false agreement that PoPS's methodologically literate readers will catch.

## Comprehensiveness vs. selectivity: the PoPS contract

A PoPS piece must be **comprehensive in coverage** yet **selective in emphasis** — and stay concise. Tier the corpus:

| Tier | Treatment |
|------|-----------|
| **Foundational / field-defining** | discussed in text, with what they established and their limits |
| **Important contributions** | grouped and weighed within framework cells; cited with their finding |
| **Confirmatory / incremental** | cited in clusters ("see also …") to show coverage without bloating prose |
| **Tangential** | cited only where they bear on a specific claim |

Comprehensiveness is proven by the citation set + saturation log (`ppsych-literature-synthesis`); selectivity is exercised in the prose.

## Reform-minded but evidence-based

PoPS is a leading venue for **methodological reform and meta-science** — but the same standards apply to the reform argument itself. Being on the right side of open science does not license overclaiming:

- **Critique with calibrated strength.** Distinguish "this practice is demonstrably harmful" (with evidence) from "this practice is suboptimal" (an argument). Reform rhetoric without the prevalence data is exactly the overclaiming reform opposes.
- **Steelman the practice you criticize.** State why reasonable researchers adopted it before showing its costs.
- **Avoid the methodological-purity trap.** A reform piece that dismisses an entire literature on a single flaw is as one-sided as the inflation it critiques.

## Fairness and the self-citation trap

PoPS referees are frequently the surveyed authors or the camps being weighed, so balance is strategic as well as ethical:

- **Steelman every camp** in terms its proponents would accept *before* noting weaknesses.
- **Attribute ideas to originators**, not popularizers (a recurring referee complaint).
- **Handle live controversies without resolving by fiat.** Lay out the disagreement, what evidence would settle it, and where your read sits — labelled as *your read*.
- **Audit self-citation and self-camp.** Your work — and your reform faction — appears at the tier the evidence warrants, no more; a reader who does not know the author cannot tell from the emphasis.

## Checklist

- [ ] Each pivotal study carries a credibility appraisal (power, replication, preregistration, validity, bias)
- [ ] Failed-to-replicate or underpowered findings flagged where the piece leans on them
- [ ] Conflicting findings reconciled by credibility + construct, not vote-counting
- [ ] Corpus tiered; prose emphasis matches tier; coverage provable from the saturation log
- [ ] Reform claims calibrated to evidence; criticized practices steelmanned first
- [ ] Every rival school/camp stated at its strongest before critique
- [ ] Idea attribution traces to originators
- [ ] Live controversies presented with what evidence would settle them; author's read labelled
- [ ] Self-citation and self-camp audited: own work/faction at warranted tier; emphasis identity-blind

## Anti-patterns

- Citing a headline effect without noting it failed to replicate or was underpowered
- Vote-counting conflicting results instead of weighing credibility and construct
- Pooling non-comparable effects into one "the field shows…" magnitude
- Reform-as-rhetoric: sweeping methodological condemnation with no prevalence data
- Strawmanning the camp (or the "old guard") the author disagrees with
- A piece that doubles as the author's — or the reform movement's — CV
- Declaring a live controversy "resolved" by assertion rather than the evidentiary state

## Output format

```text
【Credibility appraisal】pivotal studies rated (power/replication/prereg/validity/bias)? Y/N
【Conflict handling】reconciled by credibility + construct (not vote-count)? Y/N
【Tiering】corpus split foundational/important/confirmatory/tangential? Y/N
【Comprehensiveness】saturation log supports "nothing important missing"? Y/N
【Reform calibration】claims matched to evidence; criticized practices steelmanned? Y/N
【Steelman】each rival camp stated at its strongest? Y/N
【Controversy】evidence-to-settle stated; author's read labelled? Y/N
【Self-citation/camp audit】own work + faction at warranted tier; emphasis identity-blind? Y/N
【Next step】→ ppsych-tables-figures (framework figure + summary/prevalence exhibits)
```
