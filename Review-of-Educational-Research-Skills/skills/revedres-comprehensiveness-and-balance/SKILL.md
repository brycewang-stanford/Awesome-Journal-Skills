---
name: revedres-comprehensiveness-and-balance
description: Use when testing exhaustiveness, risk-of-bias, heterogeneity, and sensitivity for a Review of Educational Research (RER) review or meta-analysis. Hardens the synthesis against omission and fragility; it does not build the conceptual spine (revedres-organizing-framework) or settle coding reliability and open materials (revedres-transparency-and-reproducibility).
---

# Comprehensiveness & Balance (revedres-comprehensiveness-and-balance)

## When to trigger

- The corpus and framework exist, but you have not stress-tested coverage or robustness
- A pooled effect is reported without heterogeneity, bias, or sensitivity analysis
- You worry a reviewer will name an omitted study, school, or contradictory finding
- Conflicting studies are being tallied rather than weighed by design quality

## Comprehensiveness: prove there are no holes

RER asks for **comprehensive** reviews; the burden is on you to make exhaustiveness *provable*, not asserted.

1. **Saturation evidence.** Show that the search reached the point where new searches stopped yielding eligible studies (from `revedres-literature-synthesis`).
2. **Named-omission test.** Could an informed reviewer name an important study, research group, or adjacent literature you left out? If yes, include it or justify the boundary explicitly.
3. **Grey-literature & language reach.** Excluding dissertations, reports, or non-English work narrows scope and biases effects — acknowledge and, where feasible, widen.

## Balance: weigh evidence, never vote-count

The amateur move is **vote-counting** — tallying significant vs. null studies. The RER standard is to **weigh** evidence by what each study measures and how credibly.

1. **Risk-of-bias appraisal.** Apply the a-priori tool to every included study; let credibility, not count, drive emphasis. A handful of well-identified studies can outweigh many weak ones.
2. **Estimand discipline.** Reconcile conflicting findings by asking whether studies estimate the *same object* (population, construct, horizon, comparison). Apparent contradictions often dissolve.
3. **Steelman rival perspectives.** State each theoretical or methodological camp at its strongest before its limits; flag — and bracket — your own program so emphasis is identity-blind.

## Robustness (meta-analysis): make the number survive scrutiny

A pooled effect is a claim, not a fact, until you show it is not an artifact.

| Probe | What it guards against |
|---|---|
| **Heterogeneity** (Q, I², τ²) | reporting one number for a mix of different effects |
| **Moderator analysis** | masking real variation the framework should explain |
| **Publication-bias diagnostics** (funnel, Egger, trim-and-fill, p-curve/selection models) | an inflated effect from missing null results |
| **Sensitivity analysis** (leave-one-out, influence, alternative models) | a result driven by one study or one modeling choice |
| **Dependent-effects handling** (multilevel / robust variance) | false precision from multiple effects per sample |

For a narrative synthesis, the analogues are: confidence in the body of evidence (e.g. a GRADE-style judgment), explicit handling of conflicting findings, and a sensitivity check on which conclusions survive dropping the weakest studies.

## Checklist

- [ ] Saturation documented; no eligible study/database a reviewer could name as missing
- [ ] Grey-literature/language exclusions acknowledged with their bias implications
- [ ] Risk-of-bias appraised for every study; emphasis tracks credibility, not count
- [ ] Conflicting findings reconciled by estimand + design, not tallied
- [ ] Rival camps steelmanned; author's own work bracketed for identity-blind emphasis
- [ ] (Meta) heterogeneity, moderators, publication-bias, and sensitivity all reported
- [ ] (Meta) dependent effects modeled (multilevel / robust variance), not ignored
- [ ] (Narrative) strength-of-evidence judged and a drop-the-weakest sensitivity check run

## Anti-patterns

- Vote-counting significant vs. null studies as if each carries equal weight
- A single pooled effect with no I²/τ², no moderators, and no publication-bias check
- Ignoring dependent effect sizes, manufacturing false precision
- Excluding grey literature silently, then reporting an upward-biased effect
- Caricaturing the camp the author disagrees with instead of steelmanning it
- Treating "I found a lot of studies" as proof of comprehensiveness without saturation evidence

## Output format

```
【Saturation】documented? Y/N — named-omission test passed? Y/N
【Grey lit / language】exclusions + bias implication stated? Y/N
【Risk of bias】appraised for all studies; emphasis credibility-weighted? Y/N
【Conflict handling】reconciled by estimand/design (not vote-count)? Y/N
【Heterogeneity】I²/τ² + moderators reported? Y/N (meta) | strength-of-evidence judged (narrative)
【Publication bias】funnel/Egger/trim-fill/p-curve run? Y/N
【Sensitivity】leave-one-out / alt models / dependent-effects model? Y/N
【Next step】→ revedres-tables-figures (PRISMA flow, forest/funnel, coding tables)
```
