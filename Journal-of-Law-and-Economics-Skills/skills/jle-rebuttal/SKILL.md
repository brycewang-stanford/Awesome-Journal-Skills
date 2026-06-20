---
name: jle-rebuttal
description: Use when a The Journal of Law and Economics (JLE) decision letter arrives (R&R or conditional accept) and a response-to-referees letter plus a revision plan must be drafted. Plans and structures the response; it does not run the new analysis (jle-identification / jle-robustness) or the submission preflight (jle-submission).
---

# Rebuttal & Response Letter (jle-rebuttal)

## When to trigger

- A JLE **R&R** or **conditional acceptance** decision letter has arrived
- You need to triage referee comments into must-do / argue / defer
- You are drafting the response-to-referees document and revision plan
- A reject-and-resubmit invitation needs a strategy before re-engaging

## How to read a JLE decision

The handling editor's letter is the **priority signal**: it tells you which referee concerns are binding and which are optional. At JLE the binding asks are almost always about (1) **whether the legal institution is described correctly and the rule binds as claimed**, and (2) **the credibility of the legal identification** (the staggered-timing estimator, the parallel-trends story, the random-assignment defense), before exposition. Because review is **single-blind**, the editor and referees know who you are — a gracious, evidence-led, non-defensive tone is worth more than at a blinded journal, and self-citation should stay honest. Address the editor's stated priorities first and in full; the revision is judged on whether the **identification and institutional concerns are genuinely resolved**, not on the volume of new tables.

## Response-letter structure

1. **Opening summary** — thank the editor/referees; state the 3–5 substantive changes that define the revision (lead with the institutional and identification changes).
2. **Point-by-point** — quote each comment, then respond with what you did, where in the paper (section/table/page), and the result. Use a consistent format per point.
3. **Tone** — gracious, concrete, non-defensive. Concede valid points fully; where you disagree, argue with evidence, not assertion.
4. **Triage discipline** — every comment gets one of: **done** (changed + located), **partially done** (with reason), or **respectfully declined** (with an evidence-based argument). No comment is ignored.
5. **Highlight the decisive evidence** — if a referee doubted the legal identification, show the new heterogeneity-robust estimate / honest-DID bound / placebo on an uncovered legal area explicitly, with the new number and its SE.

## Triage table

| Referee ask | Default response |
|-------------|------------------|
| Institution misdescribed / rule didn't bind when claimed (binding per editor) | correct it fully; re-date or re-scope; show the corrected estimate |
| Core legal-identification doubt (binding) | do it in full; new heterogeneity-robust estimate + SE; update the paper |
| Robustness / inference (few states) | run it; report point-estimate stability; wild-cluster bootstrap |
| Cross-jurisdiction external validity / estimand | add a calibrated scope statement; do not overclaim |
| Additional outcome / jurisdiction | run with appropriate adjustment, or argue why out of scope |
| Mechanism (deterrence vs. incapacitation, price vs. quality) | add the channel-distinguishing test |
| Exposition / framing | revise; cheap, builds goodwill |
| Out-of-scope new paper | respectfully decline with a one-line reason |

## Checklist

- [ ] Editor's stated priorities identified and addressed first, in full
- [ ] Institutional/legal-description concerns corrected and re-verified
- [ ] Every referee comment answered: done / partial / declined — none ignored
- [ ] Each "done" response cites the exact section/table/page and the new result
- [ ] Decisive identification/robustness evidence quoted with numbers and SEs
- [ ] Tone gracious and concrete (especially given single-blind); disagreements argued with evidence
- [ ] Replication package updated to match the revised exhibits (`jle-replication-package`)
- [ ] A short cover note to the editor summarizing how the binding concerns were resolved

## Pacing a JLE revision

Law-and-economics revisions often hinge on one or two heavy lifts — re-coding the institution, re-estimating with a heterogeneity-robust estimator, or running the few-clusters inference — rather than many small ones. Plan the revision so the **decisive new evidence is done first** and the rest of the letter is built around it. Do not let cosmetic edits crowd out the binding identification work, and do not promise analysis you cannot deliver in the revision window; an honest "we did A and B in full; C we address with a bound and explain why a full treatment is infeasible" reads better than over-promising. Keep the editor's letter open beside the draft and check off each binding item explicitly.

## Worked vignette (illustrative)

Referee 2 says the staggered-DID estimate of a tort-reform effect is biased and the author misdated the reform to the statute's signing rather than its effective date; the editor flags both as binding. A weak response argues TWFE "should be fine." The JLE response: re-date treatment to each state's effective date, re-estimate with Callaway–Sant'Anna (new ATT −0.08, s.e. 0.03, vs. −0.10 under mis-dated TWFE), add event-study leads and a Bacon decomposition, and run an honest-DID bound. In the letter, quote the new number, cite the exact figure/table, and note the conclusion is unchanged but now correctly dated and robust. The editor sees both binding concerns resolved with evidence — and, since review is single-blind, the tone stays gracious and forthright.

## Handling the institutional-correction ask (distinctive at JLE)

A class of JLE referee comment has no analog at a generic econ journal: the referee, who knows the legal institution, says you have the *law* wrong — the rule did not bind when you claim, you mis-coded an exemption, a controlling case changed the regime mid-sample, or your market definition is not the antitrust-relevant one. These are usually **binding** and must be handled with care:

1. **Concede precisely and re-verify the institution** against primary legal sources (statute text, effective-date records, the docket), not secondary summaries.
2. **Re-run with the corrected coding** and report whether the estimate moves; if the correction shrinks the effect, say so and bound the implication.
3. **Thank the referee for the institutional expertise** — these comments improve the paper and a gracious concession reads well under single-blind.
4. If the referee is *mistaken* about the law, **document the correct institutional fact with a citation** and explain courteously; do not simply assert your reading.

## Anti-patterns

- Answering the referees but ignoring the editor's prioritization
- Conceding an institutional-correction point in words but never re-running with the corrected coding
- Defensive or dismissive tone — costlier under single-blind, where reviewers know the author
- Claiming a change without saying where in the paper it landed
- Adding a wall of new tables that dodges the actual institutional/identification concern
- Letting the replication package drift out of sync with the revised paper
- Over-promising analysis you cannot finish in the revision window instead of bounding it honestly
- Silently dropping a comment you found inconvenient

## Output format

```
【Decision type】R&R / conditional accept / reject-and-resubmit
【Editor priorities】[binding asks, in order]
【Institution fix】description/dating corrected? [Y/N/NA]
【Triage】done: [...] | partial: [...] | declined (with reason): [...]
【Decisive evidence】new identification/robustness result + number(SE) + location
【Tone check】gracious, concrete, evidence-based? [Y/N]
【Package sync】replication updated to match revision? [Y/N]
【Next step】jle-submission (resubmit) → re-enter jle-workflow if further rounds
```
