---
name: psychbull-rebuttal
description: Use when writing the response to a Psychological Bulletin revise-and-resubmit. A synthesis R&R often demands re-running the search, adding studies, or new bias/moderator analyses, so the response must satisfy every reviewer and the editor while keeping the meta-analysis internally consistent. Structures the response letter; it does not fabricate results.
---

# R&R Rebuttal (psychbull-rebuttal)

A Psychological Bulletin **R&R** on a synthesis is distinctive: reviewer requests often touch the
**search, eligibility, coding, model, or bias analyses** — any of which can ripple through every
downstream estimate, table, and figure. The response letter must convert each reviewer and keep the
editor confident **without breaking the synthesis's internal consistency** or its deposited package.

## When to trigger

- An R&R decision arrived and you are planning the revision + response letter
- A reviewer wants the search expanded, studies added, or eligibility changed
- A reviewer requests a different model, more moderators, or more bias diagnostics
- Reviewers disagree and you must reconcile their demands

## Strategy

1. **Read the editor's letter as the rubric.** The editor flags the decisive points; solve those first.
2. **One point-by-point response, every comment addressed.** Quote each comment, then respond; never
   skip one — silence reads as non-compliance.
3. **Propagate changes consistently.** If you **expand the search or change eligibility**, you must
   re-run **everything downstream** — pooled effect, heterogeneity, moderators, bias diagnostics,
   PRISMA counts, every table and figure — and keep them mutually consistent. State the new k.
4. **Concede or rebut with evidence.** Did what was asked (say where, with new numbers/exhibit numbers),
   or push back respectfully on methodological grounds (e.g., why an unplanned moderator stays
   exploratory, why a bias test is uninformative under high heterogeneity).
5. **Reconcile conflicting reviewers openly.** When one wants broader inclusion and another stricter,
   choose a principled rule, apply it, and explain the tradeoff to the editor.
6. **Protect the contribution.** Add robustness and clarification; resist changes that dilute the
   synthesis or over-claim beyond the evidence and heterogeneity.
7. **Keep it masked and update the package.** The revised manuscript stays masked; **update the
   deposited database, codebook, and scripts** so new estimates remain reproducible.

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree].
Change: [Section/page; new k; table/figure number; updated estimate].
```

Open with a short **summary of the main changes** to the editor (especially any change in study count
or model); group by reviewer; end each entry with the location of every change for quick verification.

## Anti-patterns

- Adding studies but leaving stale estimates/figures from the old pool (inconsistent synthesis)
- Ignoring or silently merging a comment
- Capitulating to a request that breaks eligibility logic just to please a reviewer
- Reporting a new bias test without acknowledging it changes the bottom line
- Letting the revised manuscript drift out of sync with the deposited package
- Reintroducing author clues while editing (breaks masking)

## Worked vignette — propagating an R&R through the synthesis

*Illustrative numbers only.* The self-affirmation synthesis returns with an R&R: Reviewer 1 wants the
search expanded to two more databases; Reviewer 2 calls the delivery-format moderator post-hoc;
Reviewer 3 wants a selection model added. Under this skill's rules the response propagates cleanly:

- **Search expansion** recovers 5 new trials, raising k from 42 to 47; *everything downstream is
  re-run* — pooled g shifts from 0.34 to 0.32 [0.23, 0.41], I² to 65%, and the PRISMA flow, forest plot,
  and summary table are regenerated to match.
- **Moderator challenge**: the response cites the OSF protocol showing delivery format was pre-specified,
  so it stays confirmatory.
- **New bias test**: the selection model lands g ≈ 0.24, consistent with the PET-PEESE bound; the letter
  states it nudges the bottom line toward "real but inflated."
- **Package**: the deposited database (now 47 studies), codebook, and scripts are updated; the
  manuscript stays masked.

## Reviewer pushback → response move (Bulletin-specific)

| Reviewer comment | Response move |
|------------------|---------------|
| "Search not exhaustive / PRISMA gaps" | Add databases, re-run downstream estimates, state the new k, regenerate the flow |
| "Moderators are post-hoc fishing" | Cite the registered protocol; keep pre-specified ones confirmatory, relabel any unplanned as exploratory |
| "Only one bias test" | Add converging diagnostics; report how the bottom line moves |
| "Reviewers disagree on inclusion" | Choose one principled rule, apply it, explain the tradeoff |
| "No integration beyond tallying" | Strengthen the contribution per `psychbull-theory-integration` |

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Re-run propagated】new k; all estimates/exhibits consistent? [Y/N]
【Concede vs rebut】each tagged with evidence + change location
【Reviewer conflicts】reconciled and explained? [Y/N]
【Masked + package updated】[Y/N]
【Next】resubmit via Editorial Manager
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — re-running the search/analysis; keeping the package in sync
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — masked review and transparency policy behind the response
