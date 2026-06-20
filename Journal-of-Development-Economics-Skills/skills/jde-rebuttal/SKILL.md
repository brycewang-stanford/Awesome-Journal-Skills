---
name: jde-rebuttal
description: Use when responding to a Journal of Development Economics (JDE) decision — drafting the response letter and revision plan for a single-anonymized R&R, including the short-paper track's limited-revision structure. Strategy for the response; it does not rewrite the manuscript.
---

# Rebuttal & R&R Strategy (jde-rebuttal)

## When to trigger

- A JDE R&R or revise decision arrived and you need a response-letter strategy
- Referee reports conflict and you must triage which changes to make
- You are on the short-paper track and have a single, time-boxed revision round
- You need to decide what to concede, what to defend, and what to add

## Read the decision first

JDE review is **single-anonymized** (referees know your identity), so responses are professional and direct; there is no anonymity to preserve on your side. Map the editor's letter against the referee reports: the **editor's priorities** are binding even when a referee raised a point in passing. Identify the two or three concerns that actually gate acceptance — typically **identification credibility, robustness, and the development contribution** — and lead with those.

## Track-specific timing

- **Full-length R&R:** standard multi-round revision; referees usually see the resubmission. Expect to satisfy the editor across rounds, so address every point even if briefly.
- **Short-paper (limited-revision) track:** you get a **single revision round of 4 weeks**, and **resubmissions are not returned to referees** — the editor decides. This is decisive: the revision must fully resolve the editor's conditions in one pass, because there is no second bite and no referee re-review. Do not defer fixes "for a later round" that will not exist.

## Response-letter structure

- **Cover summary**: thank the editor and referees; state the 2-3 substantive changes that most improve the paper; flag where you respectfully disagree and why.
- **Point-by-point**: quote each comment, then respond. For each: what you changed, where (section/table/figure), and the new result — or a reasoned, evidence-backed defense if you did not change it.
- **New analyses**: add the robustness, heterogeneity, attrition, or identification checks referees requested; if a check is infeasible (restricted data, power), say so transparently with an alternative.
- **Replication**: note that the data/code package reflects every new result — JDE can request it, so keep it in sync (see jde-replication-and-data-policy).

## Tactics

- Concede cheap, defensible points quickly to build credibility for the points you defend.
- For identification objections, add falsification/placebo evidence rather than rhetoric.
- Keep claims calibrated; development referees reward honest scope and punish overreach.
- Track the **submission cap** (three per 12 months) so a resubmission does not collide with other submissions.

## Common JDE referee objections and the venue-specific fix

| Referee objection                                         | The fix that lands at JDE                                              |
|-----------------------------------------------------------|-----------------------------------------------------------------------|
| "External validity — this is one context, one program"    | State the LATE/population precisely; show what travels via mechanism, not bravado |
| "Spillovers contaminate your control group"               | Add a SUTVA/spillover check (distance rings, treated-neighbor share), bound the bias |
| "PAP deviations are not flagged"                          | Add a deviation table: pre-specified vs realized, with reasons        |
| "SEs ignore clustered randomization"                      | Re-cluster at the randomization level; few clusters → wild-cluster bootstrap or RI |
| "Subgroup result looks mined"                             | Re-run as pre-specified-only, apply Romano–Wolf, demote the rest to exploratory |
| "Attrition is differential and unaddressed"               | Report attrition by arm, add Lee bounds, show robustness to the bound |

## Worked micro-example (illustrative)

Hypothetical: a full-length R&R on a cluster-randomized agricultural-extension trial. Editor's letter flags three gates — clustering, spillovers, and a heterogeneity claim.

- **Concede + fix (cheap):** re-cluster at the village level; the ITT moves from +0.21 to +0.19 SD and the CI widens but stays positive (*illustrative*) — concede the original SEs, show the result survives.
- **Defend with evidence:** for spillovers, add a treated-neighbor-share regression showing near-zero leakage; defend the control group rather than just asserting SUTVA.
- **Demote:** move the gender-interaction claim to "exploratory, MHT-adjusted," conceding it was not pre-registered.
- **Letter line:** "Comment 2 (clustering): re-estimated at the randomization level (Table 3, col. 2); ITT = 0.19 SD, 95% CI 0.05–0.33; the package reflects this change." Numbers *illustrative*.

## Anti-patterns

- Defending everything and conceding nothing — reads as defensive
- On the short-paper track, leaving a gap "for the next round" that does not exist
- Adding prose where a referee asked for a robustness check
- A response letter that does not point to the exact revised location of each change
- Letting the replication package drift out of sync with new results

## Output format

```
【Decision type】full-length R&R / short-paper limited revision / reject-with-encouragement
【Editor's gating concerns】[top 2-3]
【Concede】[points + fix]
【Defend (with evidence)】[points + argument]
【New analyses】[robustness/heterogeneity/identification added]
【Replication in sync?】[Y/N]
【Round constraint】limited-revision short-paper route? [Y/N]
```
