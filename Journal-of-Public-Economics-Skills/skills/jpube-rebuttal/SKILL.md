---
name: jpube-rebuttal
description: Use when a Journal of Public Economics (JPubE) decision letter arrives (revision or reject) and a response strategy, response letter, or appeal decision is needed. Structures the revision and response for single-anonymized specialist review; it does not redo the analysis (route to the relevant jpube-* skill).
---

# Rebuttal & Revision (jpube-rebuttal)

## When to trigger

- A JPubE decision letter arrived: major/minor revision, or reject
- You have specialist referee reports and need a response strategy
- You are unsure how to prioritize conflicting public-finance referee demands
- You are weighing whether to use the single permitted appeal

## JPubE reality

JPubE uses **single anonymized review** with a minimum of two reviewers who **know your identity**, and the handling editor (under the Hendren–Kopczuk editorial leadership) synthesizes their reports through **Editorial Manager**. The **handling editor's letter is the contract**: it ranks which referee points are binding. Because referees are public-finance specialists, expect demands aimed at the *credibility of the policy parameter and its welfare mapping* — the counterfactual in a bunching design, the pre-trends in a reform DID, the sufficient-statistics assumptions, the external validity of a local elasticity.

## Triage protocol

1. **Decode the editor.** A point the editor underscores is binding; a single-referee point the editor passed over is lower priority (but still answer it).
2. **Classify every comment** as *fundamental* (needs new analysis), *clarification* (rewrite/explain), or *disagreement* (push back politely with evidence).
3. **Sequence the work.** Route fundamentals to `jpube-identification-strategy` / `jpube-data-analysis` (e.g., re-do the bunching counterfactual, add a modern DID estimator, propagate SEs into the MVPF), update exhibits, *then* write the letter.
4. **Settle with a check, not a fight.** If a robustness check resolves a referee concern, run it; reserve disagreement for where the referee is genuinely mistaken.

## Response-letter structure

- **Opening:** thank the editor and reviewers; summarize the main changes briefly.
- **Point-by-point:** quote each comment, then respond with what you did and exactly where it now appears (section/table/figure/page).
- **Disagreements:** state the point fairly, give the evidence-based reason you differ, and offer a compromise (e.g., an appendix robustness check).
- **Tone:** gracious, concrete, never defensive — and remember reviewers see your identity.

## Appeals (use sparingly)

Elsevier's Appeal Policy allows **one appeal per submission**. If a paper is rejected on a clear factual or procedural error, you may appeal once — calm, specific, evidence-based, addressed to the editor. Do not spend the single appeal relitigating a taste judgment.

## Checklist

- [ ] Editor's binding points decoded and used to rank responses
- [ ] Every referee comment classified (fundamental / clarification / disagreement)
- [ ] Fundamental requests resolved with actual new analysis, not promises
- [ ] Each response cites the exact location of the change
- [ ] Disagreements are evidence-based and offer a compromise
- [ ] Revised manuscript updated *before* the letter was written
- [ ] Appeal, if any, reserved for a clear error and used at most once

## Anti-patterns

- Writing the response letter before the manuscript reflects the changes
- Promising future work instead of doing the analysis this round
- Arguing where a quick robustness check (bunching counterfactual, DID estimator) would settle it
- Burning the single appeal on a taste disagreement
- A defensive tone — recall the specialist reviewers know who you are

## Referee pushback → venue-specific fix

The recurring public-finance objections and the move that resolves each. Do the analysis; do not argue.

| Referee says | Underlying worry | Fix this round |
|--------------|------------------|----------------|
| "Reduced-form effect, no welfare reading" | The estimate is not yet a contribution | Add the MVPF / sufficient-statistic mapping with propagated SEs |
| "Bunching identification leans on functional form" | Counterfactual chosen to inflate excess mass | Re-fit with alternative polynomial/excluded region; report sensitivity |
| "Policy endogeneity — the reform isn't exogenous" | Treatment timing correlates with shocks | Event-study pre-trends; placebo dates; modern staggered estimator |
| "Local elasticity sold as global" | External validity overstated | Restate scope; add a transportability discussion |

## Worked vignette: turning a fundamental into a settled point (illustrative)

A revision letter underscores one referee's charge that a kink-bunching elasticity (**e = 0.25**, illustrative) "rests on the chosen counterfactual." Rather than debating, the author re-estimates under three excluded-region widths and two polynomial orders; the elasticity moves within **0.22–0.28** (illustrative), and a new appendix figure shows the band. The point-by-point response quotes the comment, states the new robustness table location (App. Table A4), and notes the welfare conclusion is unchanged. A fundamental becomes a settled, cited fix — exactly what the editor's binding-points list rewards.

## Output format

```
【Decision】major / minor revision / reject
【Editor's binding points】[...]
【Classification】fundamental: [...] / clarification: [...] / disagreement: [...]
【Analysis routed to】jpube-identification-strategy / jpube-data-analysis (as needed)
【Letter status】point-by-point with locations? [Y/N]
【Appeal】warranted by a clear error? [Y/N — ≤1 allowed]
【Next step】resubmit via Editorial Manager (jpube-submission for file checks)
```
