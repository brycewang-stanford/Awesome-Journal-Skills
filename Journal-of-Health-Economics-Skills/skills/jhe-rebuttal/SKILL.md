---
name: jhe-rebuttal
description: Use when a Journal of Health Economics (JHE) decision letter arrives (R&R or reject-and-resubmit) and a response-to-referees letter plus revision plan must be drafted. Plans and structures the response; it does not run the new analysis (jhe-identification / jhe-robustness) or the submission preflight.
---

# Rebuttal and Response Letter (jhe-rebuttal)

## When to trigger

- A JHE **R&R** or reject-and-resubmit decision letter has arrived
- You need to triage referee comments into must-do / argue / defer
- You are drafting the response-to-referees document and the revision plan
- Two referees disagree and you need a strategy that satisfies the editor

## How to read a JHE decision

The **editor's letter is the priority signal**: it tells you which referee concerns are binding. At JHE the binding asks cluster around **design credibility** (selection, concurrent policy, staggered-DiD bias, inference) and **honest scope** (a coverage/utilization effect is not welfare) before exposition. Because review is single-anonymized and the referees are health economists, expect institution-specific pushback you must answer with evidence, not assertion. With ≥2 reviewers you will sometimes face **conflicting requests**; the editor's letter, not a majority vote, resolves them — address the editor's stated priorities first and in full.

## Response-letter structure

1. **Opening summary** — thank the editor and referees; state the 3–5 substantive changes that define the revision, leading with the identification/selection/scope changes.
2. **Point-by-point** — quote each comment, then respond with: what you did, where in the paper (section/table/page), and the result. Keep one consistent format per point.
3. **Tone** — gracious, concrete, non-defensive. Concede valid points fully; where you disagree, argue with evidence and institutional fact.
4. **Triage discipline** — every comment is **done** (changed + located), **partially done** (with reason), or **respectfully declined** (with an evidence-based argument). Nothing is silently dropped.
5. **Quote the decisive number.** If a referee doubted the design, show the heterogeneity-robust estimate / honest-DID bound / selection bound / placebo explicitly, with its SE and location.
6. **Reconcile conflicting referees** by naming the trade-off and the choice the editor's priorities imply.

## Triage table

| Referee ask | Default response |
|-------------|------------------|
| Selection / identification doubt (binding per editor) | do it in full; show the new estimate or bound + SE; update the paper |
| Concurrent-policy / institutional confound | add the placebo / timing argument in the institutional section |
| Staggered-DiD or inference fix | re-estimate with CS/SA; wild-cluster bootstrap; report stability |
| "Coverage effect ≠ welfare" | add the demand-and-cost model; rescope the claim honestly |
| Additional health outcome/subgroup | run with MHT; or argue out of scope with a reason |
| Exposition / institutional clarity | revise; cheap and builds goodwill |
| Out-of-scope new paper | respectfully decline with a one-line reason |

## Checklist

- [ ] Editor's stated priorities identified and addressed first, in full
- [ ] Every referee comment answered: done / partial / declined — none ignored
- [ ] Each "done" response cites the exact section/table/page and the new result
- [ ] Decisive identification/selection/robustness evidence quoted with numbers and SEs
- [ ] Conflicting referee requests reconciled by reference to the editor's priorities
- [ ] Scope claims rematched to the design where a referee flagged overreach
- [ ] Replication package and DAS updated to match the revised exhibits (`jhe-replication-package`)
- [ ] Tone gracious and concrete; disagreements argued with evidence and institutions

## Coordinating the rebuttal with the rest of the pack

A response letter is only as strong as the new evidence behind it. When a binding concern requires fresh analysis, route the work to the owning skill before drafting the point: `jhe-identification` for a design fix, `jhe-robustness` for a stability check, `jhe-theory-model` for a welfare rescope. Then update exhibits (`jhe-tables-figures`) and the package and Data Availability Statement (`jhe-replication-package`) so the revised paper, the letter, and the deposit all tell the same story. A letter that quotes a number the revised paper does not contain is the fastest way to lose editor trust.

## Anti-patterns

- Answering the referees but ignoring the editor's prioritization
- Defensive or dismissive tone; arguing by assertion instead of new evidence
- Claiming a change without saying where in the paper it landed
- A wall of new tables that dodges the actual selection/identification concern
- Splitting the difference between conflicting referees instead of following the editor
- Letting the replication package or DAS drift out of sync with the revised paper

## Timing and the resubmission cover note

Elsevier R&Rs do not run on a fixed clock the way some society journals do; do the work properly rather than rushing, but do not let a revision go stale — a multi-year gap invites a fresh referee pool and new objections. Open the resubmission with a **short cover note to the editor** (separate from the point-by-point) that lists, in three to five bullets, how each binding concern was resolved and where. Editors triage resubmissions from that note; make it carry the decisive numbers and locations so the editor can verify the binding asks were met without re-reading the whole letter.

## What "resolved" means at JHE

A JHE revision is judged on whether the **design and scope concerns are genuinely settled**, not on the count of new tables. "Resolved" means: the selection/identification doubt is answered with an estimate or bound (not more controls); the institutional confound is ruled out with a placebo or timing argument; and any welfare/scope overreach the referee flagged is rematched to what the design identifies. A revision that adds analysis but leaves the binding concern technically un-addressed will not clear, however thick it is.

## Worked vignette (illustrative)

Referee 1 calls the staggered Medicaid-expansion DiD biased and the parallel-trends story thin; Referee 2 wants more outcomes; the editor flags Referee 1 as binding. A weak response argues TWFE "should be fine." The JHE response: re-estimate with Callaway–Sant'Anna (new ATT 4.0pp, s.e. 1.1, vs. 4.6pp under TWFE), add event-study leads and a Goodman-Bacon decomposition, run an honest-DID bound, and rule out the concurrent marketplace launch with a placebo — then in the letter quote the new number, cite the exact figure/table, and note the conclusion is unchanged but now robust. Referee 2's extra outcomes are added with MHT where central and declined-with-reason where out of scope, explicitly subordinated to the editor's binding concern.

## Output format

```
【Decision type】R&R / reject-and-resubmit / conditional accept
【Editor priorities】[binding asks, in order]
【Triage】done: [...] | partial: [...] | declined (with reason): [...]
【Decisive evidence】new identification/selection result + number(SE) + location
【Conflicting referees】reconciled via editor priorities? [Y/N]
【Scope discipline】overclaim rescoped to design? [Y/N]
【Package sync】replication + DAS updated to match revision? [Y/N]
【Next step】jhe-submission (resubmit) → re-enter jhe-workflow if further rounds
```

## Handoff boundary

This skill plans and structures the response and the revision; it does not produce the new evidence (that is `jhe-identification` / `jhe-robustness` / `jhe-theory-model`) nor run the resubmission preflight (`jhe-submission`). When the letter is drafted and every binding concern has its evidence and location, hand off to `jhe-submission` to resubmit through Editorial Manager.
