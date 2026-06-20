---
name: aeja-rebuttal
description: Use when an American Economic Journal: Applied Economics (AEJ: Applied) decision letter arrives (R&R or conditional accept) and a response-to-referees letter plus a revision plan must be drafted. Plans and structures the response; it does not run the new analysis (aeja-identification / aeja-robustness) or the submission preflight.
---

# Rebuttal & Response Letter (aeja-rebuttal)

## When to trigger

- An AEJ: Applied **R&R** or **conditional acceptance** decision letter has arrived
- You need to triage referee comments into must-do / argue / defer
- You are drafting the response-to-referees document and revision plan
- A reject-and-resubmit invitation needs a strategy before re-engaging

## How to read an AEJ: Applied decision

The editor's letter is the **priority signal**: it tells you which referee concerns are binding and which are optional. At AEJ: Applied the binding asks are almost always about **design credibility** (the identification, robustness, inference) before exposition. Address the editor's stated priorities first and in full; treat the referee reports as the menu the editor has already filtered. A revision is judged on whether the **identification concerns are genuinely resolved**, not on volume of new tables.

## Response-letter structure

1. **Opening summary** — thank the editor/referees; state the 3–5 substantive changes that define the revision (lead with the identification/robustness changes).
2. **Point-by-point** — quote each comment, then respond with: what you did, where in the paper (section/table/page), and the result. Use a consistent format per point.
3. **Tone** — gracious, concrete, non-defensive. Concede valid points fully; where you disagree, argue with evidence, not assertion.
4. **Triage discipline** — every comment gets one of: **done** (changed + located), **partially done** (with reason), or **respectfully declined** (with an evidence-based argument). No comment is ignored.
5. **Highlight the decisive evidence** — if a referee doubted the design, show the new heterogeneity-robust estimate / honest-DID bound / falsification result explicitly and quote the new number with its SE.

## Triage table

| Referee ask | Default response |
|-------------|------------------|
| Core identification doubt (binding per editor) | do it in full; show the new estimate + SE; update the paper |
| Robustness/inference request | run it; report stability of the point estimate |
| External-validity / estimand | add a calibrated scope statement; do not overclaim |
| Additional outcome/subgroup | run with MHT adjustment; or argue why it is out of scope |
| Exposition / framing | revise; cheap to do, builds goodwill |
| Out-of-scope new paper | respectfully decline with a one-line reason |

## Checklist

- [ ] Editor's stated priorities identified and addressed first, in full
- [ ] Every referee comment answered: done / partial / declined — none ignored
- [ ] Each "done" response cites the exact section/table/page and the new result
- [ ] Decisive identification/robustness evidence quoted with numbers and SEs
- [ ] Tone gracious and concrete; disagreements argued with evidence
- [ ] Replication package updated to match the revised exhibits (`aeja-replication-package`)
- [ ] A short cover note to the editor summarizing how the binding concerns were resolved

## Worked vignette (illustrative)

Referee 2 says the staggered-DID estimate is biased and the parallel-trends story is thin; the editor's
letter flags this as the binding concern. A weak response argues that TWFE "should be fine here." The
AEJ: Applied response: re-estimate with Callaway–Sant'Anna, report the new ATT of 3.1pp (s.e. 0.9, vs. 3.6pp
under TWFE), add the event-study leads and a Goodman-Bacon decomposition, and run an honest-DID bound — then
in the letter quote the new number, cite the exact figure/table, and note the conclusion is unchanged but now
robust. The editor sees the binding concern fully resolved with evidence, not assertion.

## Anti-patterns

- Answering the referees but ignoring the editor's prioritization
- Defensive or dismissive tone; arguing by assertion instead of new evidence
- Claiming a change without saying where in the paper it landed
- Adding a wall of new tables that dodges the actual identification concern
- Letting the replication package drift out of sync with the revised paper
- Silently dropping a comment you found inconvenient

## Output format

```
【Decision type】R&R / conditional accept / reject-and-resubmit
【Editor priorities】[binding asks, in order]
【Triage】done: [...] | partial: [...] | declined (with reason): [...]
【Decisive evidence】new identification/robustness result + number(SE) + location
【Tone check】gracious, concrete, evidence-based? [Y/N]
【Package sync】replication updated to match revision? [Y/N]
【Next step】aeja-submission (resubmit) → re-enter aeja-workflow if further rounds
```
