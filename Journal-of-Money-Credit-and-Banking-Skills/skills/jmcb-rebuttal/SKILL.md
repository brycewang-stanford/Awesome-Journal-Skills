---
name: jmcb-rebuttal
description: Use when a Journal of Money, Credit and Banking (JMCB) decision letter or referee report has arrived and you need a response-letter strategy and revision plan. Turns the reports into a prioritized, point-by-point rebuttal; it does not re-run the core analysis or re-write the paper.
---

# Rebuttal Strategy (jmcb-rebuttal)

## When to trigger

- A JMCB R&R or reject-and-resubmit letter arrived and you need a response plan
- Two referees disagree (e.g., one wants a structural model, the other wants reduced-form transparency) and you must reconcile them
- The editor's letter prioritizes some points over others and you need to honor that hierarchy
- A report demands analysis that touches identification or measurement and you must decide what is feasible

## Reading the JMCB decision letter

At JMCB the **editor's letter is the governing document** — it tells you which referee points are binding, which are advisory, and what the bar for the next round is. Read it first and let it set priorities; do not weight all referee comments equally. Note the decision type: an R&R asks for a revision under the same desk; a reject-and-resubmit (sometimes after a no-fee resubmission window) is a fresh start that still benefits from addressing the prior reports. Confirm the resubmission fee status (resubmissions of invited revisions are typically fee-exempt — 待核实).

## Building the response

1. **Open with a brief summary** of the main changes and the new evidence, so the editor sees the revision's shape before the point-by-point.
2. **Point-by-point, quoting each comment**, then: (a) what you changed, (b) where (section/table/figure number), (c) the result. Make it trivial for the referee to verify.
3. **Triage every comment** into: *fully addressed* (new analysis), *addressed in text* (argument/clarification), or *respectfully pushed back* (with evidence, never with attitude).
4. **Reconcile conflicting referees explicitly** — name the tension, explain the choice, and where possible satisfy both (e.g., keep the reduced-form headline *and* add the model in the appendix).
5. **For identification/measurement demands**, show the new diagnostic and report whether the headline moved; transparency about a small change is more persuasive than insisting nothing changed.
6. **Track magnitudes across the revision** — if a new specification shifts the elasticity, say by how much and why the conclusion survives.

## Handling the characteristic JMCB asks

- *"Your shock is contaminated."* → Add the info-robust re-identification (Jarociński–Karadi); show the IRF is similar; cite `jmcb-identification`.
- *"This is credit demand, not supply."* → Add firm×time fixed effects (or single-vs-multi-bank split); report the supply coefficient.
- *"What disciplines your parameters / is the counterfactual policy-invariant?"* → Add the parameter-to-moment map and the Lucas-critique argument.
- *"So what for policy?"* → Sharpen the policy lever in the intro and conclusion; benchmark the magnitude.
- *"It's too long."* → Move supporting material to the online appendix (see `jmcb-internet-appendix`); the 40-page recommendation excludes it.

## Tone and format that referees reward

- **Respect the hierarchy.** Address the editor's emphasized points first and most thoroughly; do not let a minor referee-3 stylistic note get equal airtime with a binding identification objection.
- **Quote-then-respond, every time.** Reproduce each comment verbatim in a distinct font/block, then respond beneath it. Referees skim for their own comments; make them findable.
- **Point to the manuscript by number.** "We now report this in Table 5, columns 3–4" lets a referee verify in seconds; "we have addressed this" forces a re-read of the whole paper.
- **Concede gracefully where right.** A referee who is correct should be thanked and accommodated; saved face costs you nothing and buys goodwill for the points where you push back.
- **Push back with evidence, never with attitude.** When a referee is wrong, show why with a result or citation, in measured language. Defensiveness reads as weakness.

## Deciding what is feasible

Not every demand is worth meeting. For each costly ask (a new structural model, restricted data you cannot obtain, a redesign), weigh: is it binding per the editor, how much does it strengthen the paper, and is it attainable? If a demand is infeasible (restricted data access denied) or misguided, say so plainly with the reason, and offer the closest feasible substitute (e.g., a public-data approximation, a bounding exercise). An honest "here is why we cannot do exactly that, and here is what we did instead" is more persuasive than silence or a half-measure dressed as compliance.

## Checklist

- [ ] Editor's letter read first; binding vs. advisory points separated and prioritized
- [ ] Response opens with a summary of the main changes
- [ ] Every comment quoted, with what changed, where (section/table), and the result
- [ ] Each comment triaged: fully addressed / addressed in text / respectful pushback with evidence
- [ ] Conflicting referees reconciled explicitly, satisfying both where feasible
- [ ] Identification/measurement asks answered with the diagnostic and honest magnitude movement
- [ ] Length asks handled by moving material to the online appendix, not by cutting evidence
- [ ] Resubmission fee/route status confirmed (待核实)

## Anti-patterns

- Treating all referee comments as equal weight, ignoring the editor's prioritization
- Pushing back on a binding point without new evidence — or with a defensive tone
- Claiming "no change to results" after re-identification without showing the new estimate
- Quietly dropping a referee's objection instead of addressing or respectfully declining it
- Letting two referees' contradictory demands stall the revision instead of reconciling them in writing
- Padding the main text back over 40 pages with material that belongs in the appendix

## Pace and the resubmission window

A JMCB R&R does not reward speed for its own sake — it rewards a revision that visibly closes the binding points. But a long silence risks reviewer turnover and a colder reread. Aim to return within the editor's expected window with every binding point demonstrably addressed; if a demanded analysis (restricted-data access, a new structural model) will take longer, it is worth a brief note to the editor rather than missing the window with a half-revision. Confirm the resubmission fee status before resubmitting (invited revisions are typically fee-exempt — 待核实) and re-run the `jmcb-submission` preflight, since page count and exhibits often drift during a revision.

## Worked vignette (illustrative)

A JMCB R&R has the editor flagging two binding points: shock contamination (referee 1) and demand contamination (referee 2). The response opens by summarizing both fixes, then, point-by-point, shows the info-robust IRF (peak −1.8% vs. −2.0% before, illustrative) and the firm×quarter-FE supply coefficient. Referee 3's request for a full structural model conflicts with referee 1's preference for transparency; the authors reconcile by keeping the reduced-form headline and adding a calibrated banking model in the appendix as corroboration. The letter makes every change verifiable by table number, and the small magnitude change is reported, not hidden.

## A response-letter structure that works

Open with a one-paragraph summary of the main changes and any new results, so the editor sees the revision's shape at a glance. Then take each referee in turn, reproducing every comment verbatim and answering beneath it with the change, the location by table/section number, and the result. Close each referee's section by noting any of their points you respectfully declined and why. Keep a parallel "changes to the manuscript" list if the editor requests one. The letter should let a busy editor confirm, in a single read, that every binding point is closed — that perception, as much as the analysis itself, drives the next decision.

## Output format

```text
【Journal】Journal of Money, Credit and Banking
【Skill】jmcb-rebuttal
【Decision type】R&R / reject-and-resubmit; editor's priority order
【Binding vs advisory】which referee points govern the next round
【Point-by-point】comment → change → location (section/table) → result
【Triage】fully addressed / addressed in text / respectful pushback
【Conflicts reconciled】how contradictory referee demands were squared
【Magnitude tracking】any headline movement reported honestly
【Next step】revise; re-run jmcb-submission preflight before resubmitting
```
