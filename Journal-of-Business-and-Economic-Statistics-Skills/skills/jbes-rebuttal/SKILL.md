---
name: jbes-rebuttal
description: Use when a Journal of Business & Economic Statistics (JBES) decision letter arrives (R&R or major revision) and a response strategy and letter are needed for a methods paper. Structures the revision and response; it does not redo the analysis (route to the relevant jbes-* skill).
---

# Rebuttal & Revision (jbes-rebuttal)

## When to trigger

- A JBES decision letter arrived: revise-and-resubmit or major revision
- You have method-expert referee reports and need a response strategy
- You are unsure how to prioritize conflicting referee demands
- The revised manuscript exists and you need to draft the response letter

## JBES reality: the handling Co-Editor's letter is the contract

JBES is run by a panel of **Co-Editors / Joint Editors**, and the **handling Co-Editor's letter sets priorities** — read it first and let it rank the referees' points. Because JBES referees are **method experts**, their objections cluster on three axes: **statistical validity** (assumptions, asymptotics, inference), **empirical relevance** (the application, whether the method truly helps it), and **reproducibility** (can the simulation and empirical results be regenerated). Treat an R&R as a near-final opportunity: resolve everything substantive in this round.

## Triage protocol

1. **Decode the Co-Editor.** A point the handling editor underscores is binding; a point only one referee raised and the editor did not flag is lower priority (but still answer it).
2. **Classify every comment.** Tag each: *fundamental* (needs new theory/simulation/application work), *clarification* (rewrite/explain), or *disagreement* (push back politely, with evidence — often a decisive Monte Carlo).
3. **Sequence the work.** Route fundamentals: validity → `jbes-identification-strategy`; simulations/application → `jbes-data-analysis`; reproducibility → `jbes-replication-and-data-policy`; exposition → `jbes-writing-style`. Do the work, update exhibits, *then* write the letter.
4. **Settle it with a simulation when you can.** At a methods journal, a referee dispute about validity is often resolved by an additional, well-designed Monte Carlo — run it rather than arguing.

## Response-letter structure

- **Opening**: thank the Co-Editor and referees; summarize the main changes in a short paragraph.
- **Point-by-point**: quote each comment, then respond with what you did and exactly where (section/theorem/table/figure/page) it now appears.
- **Disagreements**: state the referee's point fairly, give evidence (often a new simulation), and offer a compromise (e.g., an added robustness table) where possible.
- **Tone**: gracious, concrete, never defensive.

## Checklist

- [ ] Handling Co-Editor's priorities decoded and used to rank responses
- [ ] Every comment classified (fundamental / clarification / disagreement)
- [ ] All fundamental requests resolved with actual new theory/simulation/application work
- [ ] Each response cites the exact location of the change in the revised paper
- [ ] Validity disputes settled with new Monte Carlo evidence where possible
- [ ] Reproducibility comments addressed in the supplement
- [ ] Revised manuscript updated *before* the letter was written

## Anti-patterns

- Writing the response letter before the manuscript reflects the changes
- Arguing a validity point a clean Monte Carlo would settle
- Promising future work instead of doing the analysis this round
- Defensive or curt tone; treating method referees' reports as attacks
- Vague responses ("we have addressed this") with no location in the paper

## Worked vignette: triaging a method-paper R&R

A hypothetical JBES R&R on a new spectral test for structural breaks in volatility draws three reports (numbers **illustrative**). The handling Co-Editor's letter underscores Referee 1's validity point and flags the application as thin. Triage: Referee 1 ("the null limiting distribution assumes no leverage effect") is *fundamental* — route to `jbes-identification-strategy`, then settle it with a new Monte Carlo showing an illustrative size of 5.1% under a leverage DGP. Referee 2 ("compare to the CUSUM-of-squares benchmark") is *fundamental* on evidence — route to `jbes-data-analysis` and add the benchmark in the same tables. Referee 3 ("dense notation") is *clarification* — route to `jbes-writing-style`. The reproducibility comment goes to `jbes-replication-and-data-policy`. The manuscript is updated first; only then is the letter written, each response citing the exact theorem/table/page.

## Referee-pushback patterns in revision (venue-specific fixes)

| JBES report objection | Fix this skill enforces |
|----|----|
| "The validity claim is still unproven." | Settle it with a decisive new Monte Carlo rather than prose argument |
| "You promised this for future work." | Do the theory/simulation/application this round; an R&R is near-final |
| "Where in the paper did you change this?" | Cite the exact section/theorem/table/figure/page in each response |

Calibration anchor (hedged): the handling Co-Editor's letter is the contract — a point the editor
underscores is binding, one only a single referee raised and the editor did not flag is lower priority
(still answered). For the number and scope of revision rounds, follow the decision letter's own
instructions.

## Output format

```
【Decision】R&R / major revision
【Co-Editor's binding points】[...]
【Classification】fundamental: [...] / clarification: [...] / disagreement: [...]
【Routed to】jbes-identification-strategy / jbes-data-analysis / jbes-replication-and-data-policy (as needed)
【Letter status】point-by-point with locations? [Y/N]
【Tone check】gracious + concrete? [Y/N]
【Next step】resubmit via the JBES portal (jbes-submission for file checks)
```
