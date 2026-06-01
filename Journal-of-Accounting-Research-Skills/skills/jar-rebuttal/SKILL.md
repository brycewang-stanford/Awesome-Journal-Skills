---
name: jar-rebuttal
description: Use after a Journal of Accounting Research (JAR) revise-and-resubmit to plan the revision and draft the point-by-point response — prioritizing the Senior Editor's first-order concerns (identification, the channel, measurement) and updating the required data-and-code package. Plans and drafts the response; it does not run the new analyses from scratch (jar-data-analysis) or re-run the submission preflight (jar-submission).
---

# R&R Revision & Response (jar-rebuttal)

## When to trigger

- You received a JAR **revise-and-resubmit** and must plan the revision
- You need to draft the point-by-point response to the Senior Editor and referees
- Referees disagree and you must triage which concerns are binding
- New analyses change tables and the data-and-code package needs updating

## Sequence: revise first, then write the response

Do the analytical work **before** drafting the letter. A JAR R&R turns on whether you have actually strengthened **identification, the economic channel, and measurement** — not on rhetorical skill. The Senior Editor's letter is the binding map: it tells you which referee points are **first-order** (and must be resolved) versus **second-order** (where a reasoned reply may suffice). Address the editor's priorities first.

## Triage the referee points

- **First-order (must resolve):** endogeneity/identification threats, an unidentified channel, fragile or invalid construct measurement, sample-construction concerns. These usually require **new analyses** (a cleaner setting, additional diagnostics, alternative proxies, falsification tests).
- **Second-order (resolve or reason):** additional robustness, exposition, framing, extra citations. Implement where cheap; otherwise explain clearly.
- **Conflicting referees:** do not whipsaw the paper. State the trade-off and follow the **Senior Editor's** steer; note where you sided with one referee and why.

## Draft the response letter

- **One point, one response.** Quote each comment, then give your response and **point to the exact change** (section, table number, new analysis).
- **Show the new evidence.** For identification/measurement concerns, present the new table or diagnostic in the letter (or a response appendix), not just a promise.
- **Be candid about limits.** Where a concern cannot be fully resolved, say what the design can and cannot identify and add the scope condition to the paper.
- **Respectful and specific.** Thank referees, concede valid points, and defend with evidence — never dismiss.

## Update the deliverables JAR requires

Re-run the **data-and-code package** so it regenerates **all** revised tables and figures from raw extracts; update the README for new screens, vintages, and analyses. Keep the manuscript double-anonymized and consistent (variable names, hypothesis labels, table numbers) after the revision. If this is a **Registered Report Stage 2**, confirm the analyses match the pre-approved Stage 1 protocol and explain any pre-specified deviations.

## Checklist

- [ ] Revision analyses completed **before** drafting the response
- [ ] Editor's first-order concerns identified and resolved
- [ ] Each referee comment quoted with a specific, change-anchored response
- [ ] New identification/measurement evidence shown, not promised
- [ ] Conflicting referees reconciled per the editor's steer
- [ ] Data-and-code package regenerates all revised exhibits; README updated
- [ ] Manuscript still anonymized and internally consistent
- [ ] (If RR Stage 2) analyses match the approved Stage 1 protocol

## Anti-patterns

- **Writing the letter before doing the work.**
- **Treating all referees equally** instead of following the editor's priorities.
- **Promising robustness** instead of showing it.
- **Cosmetic responses** to first-order identification concerns.
- **Letting the posted code drift** out of sync with the revised tables.

## Output format

```
【Editor first-order asks】[...] — resolved by ...
【Referee triage】R1/R2/R3 first-order vs second-order
【New analyses done】identification / measurement / falsification ...
【Response letter】per-point, change-anchored draft status
【Conflicts reconciled】editor's steer followed where ...
【Data-and-code】package regenerates revised exhibits? updated?
【Next step】resubmit via Research Exchange (jar-submission for preflight)
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JAR/Chicago Booth/Wiley URLs (accessed 2026-06-01)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — analysis and reproducibility tooling for revision work
