---
name: finman-rebuttal
description: Use when a Financial Management (FM) decision letter arrives (R&R or conditional accept) and a response-to-referees letter plus a revision plan must be drafted. Plans and structures the response; it does not run the new analysis (finman-identification / finman-robustness) or the resubmission preflight (finman-submission).
---

# Rebuttal & Response Letter (finman-rebuttal)

## When to trigger

- An FM **R&R** or **conditional acceptance** decision letter has arrived
- You need to triage referee comments into must-do / argue / defer
- You are drafting the response-to-referees document and the revision plan
- A reject-with-encouragement note needs a strategy before any re-engagement

## How to read an FM decision

The editor's letter is the **priority signal**: it tells you which referee concerns are binding and which are optional. Given FM's criteria, the binding asks usually concern **credibility (identification/inference)** and **whether the contribution is interesting and general enough**, rather than robustness volume — FM **under-weights trivial robustness**, so an R&R rarely turns on "run ten more checks." Address the editor's stated priorities first and in full; treat the referee reports as the menu the editor has already filtered. Because FM values papers "people actually read," a revision that also **sharpens the framing and the so-what** — not just the econometrics — reads as responsive to the journal's taste. A revision is judged on whether the binding concerns are genuinely resolved and the paper is now more interesting, not on the number of new tables.

## Response-letter structure

1. **Opening summary** — thank the editor and referees; state the 3–5 substantive changes that define the revision, leading with the credibility and framing changes the editor flagged.
2. **Point-by-point** — quote each comment, then respond with what you did, where in the paper (section/table/page), and the result. One consistent format per point.
3. **Tone** — gracious, concrete, non-defensive. Concede valid points fully; where you disagree, argue with evidence, not assertion.
4. **Triage discipline** — every comment gets one of: **done** (changed + located), **partially done** (with reason), or **respectfully declined** (with an evidence-based argument). No comment is silently dropped.
5. **Highlight the decisive evidence** — if a referee doubted the design, quote the new heterogeneity-robust estimate / sensitivity bound / falsification result with its SE and say where it now lives.

## Triage table

| Referee ask | Default response |
|-------------|------------------|
| Core identification/inference doubt (binding per editor) | do it in full; show the new estimate + SE; update the paper |
| "Not interesting / too narrow" (binding per editor) | sharpen the general-interest framing and the so-what; do not just add tables |
| "Belongs in a specialist journal" | strengthen the substitution answer in the intro |
| Trivial robustness request | run it if cheap, but lead with stability of the point estimate; resist a robustness wall FM discounts |
| Additional outcome / subsample | run with appropriate inference, or argue why it is out of scope |
| Exposition / framing | revise; cheap, builds goodwill, and serves FM's readability brand |
| Out-of-scope new paper | respectfully decline with a one-line reason |

## Checklist

- [ ] The editor's stated priorities are identified and addressed first, in full
- [ ] Every referee comment is answered: done / partial / declined — none ignored
- [ ] Each "done" response cites the exact section/table/page and the new result
- [ ] Decisive credibility evidence is quoted with numbers and SEs
- [ ] The framing/so-what is sharpened where "not interesting enough" was raised
- [ ] Tone is gracious and concrete; disagreements are argued with evidence
- [ ] Internet appendix and any data/code are updated to match the revised exhibits

## Anti-patterns

- Answering the referees but ignoring the editor's prioritization
- Responding to "this isn't interesting" with more robustness tables instead of better framing
- Defensive or dismissive tone; arguing by assertion rather than new evidence
- Claiming a change without saying where in the paper it landed
- Adding a wall of new tables that dodges the actual credibility concern
- Letting the internet appendix or data/code drift out of sync with the revision

## The FM-specific revision instinct

Two reflexes serve an FM revision better than the generic "do everything the referees asked":

- **When a referee says "not interesting," resist the table reflex.** The fix is almost always *framing* — a sharper general-interest hook, a clearer so-what, a magnitude in managerial units — not more econometrics. Adding tables to answer an interest objection reads as not understanding the journal.
- **Lead the response letter with the contribution, restated.** Open by reminding the editor what the paper shows and why it matters, then walk the binding concerns. Editors handling a fast-turnaround journal appreciate a letter that re-establishes the value before diving into point-by-point detail.
- **Keep the revision proportionate.** FM under-weights trivial robustness, so a revision that triples the table count to look responsive can backfire; a tight revision that resolves the binding concerns and improves readability fits the journal's taste.

## Worked vignette (illustrative)

The editor's letter says the staggered-DID estimate needs a modern estimator and the paper "doesn't yet feel general-interest." A weak response argues TWFE "should be fine" and adds five robustness tables. The FM response: re-estimate with Sun–Abraham, report the new ATT of 3.1pp (s.e. 0.9 vs. 3.6pp under TWFE), add the event-study leads, and — addressing the second binding concern — rewrite the abstract and intro around the general managerial implication and the debate the finding furthers. The letter quotes the new number, cites the exact figure, and shows the framing change. Both binding concerns are resolved; no robustness wall is built.

## Handling a reject-with-encouragement

FM's explanatory feedback sometimes amounts to a reject that signals the paper could return in different form. Read it carefully:

- **Distinguish fit from execution.** If the note says the contribution is not general-interest enough, the issue is fit — reframe or re-target rather than re-running analysis. If it flags credibility, the issue is execution — fix and consider resubmission only if the editor invited it.
- **Do not resubmit a cosmetically changed paper.** A second submission that ignores the first round's substance burns a fee and goodwill; FM editors remember.
- **Use the feedback to choose the next venue honestly** — sometimes the right move is a specialist sibling where the contribution lands better.
- **Quote the editor's own language back** if you do resubmit on invitation, to show the binding concerns were taken seriously rather than reinterpreted.

## Output format

```
【Decision type】R&R / conditional accept / reject-with-encouragement
【Editor priorities】[binding asks, in order]
【Triage】done: [...] | partial: [...] | declined (with reason): [...]
【Decisive evidence】new credibility result + number(SE) + location
【Framing fix】so-what / general-interest sharpened where flagged? [Y/N]
【Tone check】gracious, concrete, evidence-based? [Y/N]
【Package sync】internet appendix + data/code updated? [Y/N]
【Next step】finman-submission (resubmit) → re-enter finman-workflow if further rounds
```
