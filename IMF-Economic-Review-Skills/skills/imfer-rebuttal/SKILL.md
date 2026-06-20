---
name: imfer-rebuttal
description: Use when an IMF Economic Review (IMFER) R&R or decision letter arrived and you need a response-letter strategy for a dual academic/policy referee panel. Plans and drafts the response; it returns to imfer-submission for the resubmission preflight and does not re-run the original identification (imfer-identification).
---

# Rebuttal Strategy (imfer-rebuttal)

## When to trigger

- An IMFER R&R (major or minor) arrived and you must turn referee reports into a revision plan
- The editor's letter prioritizes some points over others and you must read the signal
- A referee asks for a new identification check, a country-composition test, or a stronger policy framing
- Two referees disagree — one academic-leaning, one policy-leaning — and you must satisfy both
- You need to decide what to concede, what to push back on, and what to defer
- A referee requests a major redesign and you must decide whether to comply, push back, or withdraw

## How to read an IMFER decision letter

IMFER R&Rs usually carry the **dual signature** of the pool: an academic referee pressing on identification and frontier novelty, and a reader pressing on **policy relevance and program realism**. Start from the **editor's letter** — it ranks the points and signals which are deal-breakers. The classic IMFER revision arc is: shore up the cross-country design, add the composition/common-shock checks the referees expect, and **sharpen (or appropriately bound) the policy implication** without overreaching. Treat the academic and policy concerns as two tracks that must both be closed.

| Referee ask | Response move |
|-------------|---------------|
| "Re-do with a heterogeneity-robust estimator" | re-estimate; show the headline barely moves; report the event-study leads |
| "Show it is not driven by a few countries" | add leave-one-country-out / drop-dominant to the main paper, not just the appendix |
| "This is the global financial cycle" | add the global-cycle / US-shock control; show the result survives |
| "Policy is endogenous to the crisis" | add the instrument / narrative-timing defense; bound the causal reading |
| "The policy implication is overreached" | re-scope the implication to exactly what the design supports |
| "Inference is too narrow" | switch to Driscoll–Kraay / wild-cluster; report the new CIs |
| Two referees disagree | let the editor's ranking arbitrate; address both, flag the tension transparently |
| "Make it reproducible" | finalize the package with restricted-data access instructions |
| "Extend to more countries / a longer sample" | extend if feasible and report; if data-constrained, say so and bound external validity |

### Reading the decision verdict
IMFER decisions, like most economics journals, carry a verdict the letter's tone encodes: a **major R&R** invites real engagement and usually signals the editor wants the paper if the design and policy claim can be shored up; a **minor R&R** means the contribution is accepted and the asks are executable; a **reject-and-resubmit** (rarer) means a fundamental redesign before it can re-enter. Calibrate effort to the verdict — do not under-respond to a major R&R by treating it as cosmetic, and do not over-engineer a minor R&R into a new paper the editor did not ask for. The editor's framing of the contribution, not the referee word count, is the signal.

## Rebuttal craft

1. **Lead with a summary of changes** keyed to the editor's priorities, then a point-by-point reply.
2. **Quote each comment, then answer** with what changed, where (section/table/page), and the result — show the number, do not just assert.
3. **Concede gracefully and push back precisely.** Where a referee is wrong, disagree with evidence and courtesy; do not stonewall the policy referee on relevance.
4. **Satisfy both tracks.** Close the academic identification asks *and* the policy-relevance asks; a revision that fixes one and ignores the other stalls.
5. **Bound, do not inflate, the policy claim.** Re-scoping an overreached implication is usually safer than defending it.
6. **Show robustness moved little.** The persuasive object is that new checks leave the headline stable.

## Checklist

- [ ] Effort calibrated to the verdict (major vs. minor R&R vs. reject-and-resubmit)
- [ ] Summary-of-changes table keyed to the editor's ranked priorities
- [ ] Every referee point quoted and answered with section/table reference and the result
- [ ] New identification / composition / common-shock checks run and reported
- [ ] Policy implication re-scoped or sharpened to what the evidence supports
- [ ] Both the academic and the policy referee's concerns are closed
- [ ] Disagreements handled with evidence, not stonewalling; tensions flagged for the editor
- [ ] A polite, point-by-point tone maintained even where the referee is wrong
- [ ] Resubmission re-runs the double-blind preflight (`imfer-submission`)

## Anti-patterns

- A response letter that argues instead of revising — refusing the obvious requested checks
- Closing the academic asks while ignoring the policy referee (or vice versa)
- Re-defending an overreached policy claim instead of bounding it
- Asserting "we added robustness" without showing the new numbers
- Ignoring the editor's signaled priorities and treating all comments as equal
- Forgetting to re-anonymize the revised main file for the next double-blind round
- Letting two conflicting referees pull the paper apart instead of using the editor's ranking to arbitrate
- A response document so long the editor cannot find what changed — lead with the changes table
- Silently dropping a result a referee questioned instead of addressing the concern openly

## Worked vignette (illustrative)

The R&R: Referee 1 (academic) wants Callaway–Sant'Anna and a leave-one-country-out; Referee 2 (policy) thinks the CFM welfare claim is overreached; the editor flags identification as the deal-breaker. The response leads with a changes table keyed to that ranking: the headline moves from −0.82 to −0.79 under the new estimator (shown), leave-one-country-out stays in [−0.9, −0.7] (new appendix table referenced), and the welfare claim is re-scoped from "CFMs are optimal" to "CFMs reduce the outflow by roughly half in the regime we study, with the optimal tax bounded at 1–3%." Both referees' tracks close; the editor's priority is addressed first.

## Referee pushback mapped to the rebuttal move

- *"You did not actually run the requested estimator."* → Run it, report the new headline, and show it barely moved — assertion is not enough.
- *"The policy claim is still too strong."* → Re-scope explicitly to the regime and magnitude the design supports; do not re-defend the original.
- *"The two referees contradict each other."* → Quote the editor's ranking, address both, and flag the tension transparently for the editor to adjudicate.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-rebuttal
【Editor priorities】ranked deal-breakers: ___
【Point-by-point】[comment → change → location → result] for each
【New analyses】estimator / composition / common-shock checks run: ___
【Policy claim】re-scoped / sharpened to the evidence: ___
【Both tracks closed】academic ___ | policy ___
【Next step】imfer-submission (re-run double-blind preflight for resubmission)
```
