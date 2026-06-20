---
name: jmis-rebuttal
description: Use when planning and drafting the response to a Journal of Management Information Systems (JMIS) major/minor revision — a point-by-point reply to the EIC, Associate Editor, and double-anonymized referees that resolves identification, measurement, contribution, and robustness concerns. Plans and drafts the response; revisit earlier jmis-* skills to execute the underlying fixes.
---

# Rebuttal Strategy (jmis-rebuttal)

## When to trigger

- A JMIS major- or minor-revision letter arrived and you need a response plan
- Referee and AE comments conflict and you must decide whom to follow
- A reviewer asks for analysis you have not run, or challenges the contribution's IS relevance
- You need a point-by-point response letter that the EIC and AE can adjudicate quickly

## Triage before you draft

JMIS revisions come back through an **EIC-led, double-anonymized** process: the EIC and Associate Editor weigh the referees, so your response is read by people deciding whether you have *resolved* concerns, not merely answered them. Triage every comment:

1. **Fit / contribution concerns first.** If the AE or EIC doubts the IS-management contribution, no robustness check rescues it — re-run `jmis-contribution-framing` and lead the letter with the reframe.
2. **Identification / measurement / robustness.** Classify each as a real fix (new analysis), a clarification (already in the paper, surface it), or a defensible decline (explain why the request is not appropriate, with evidence).
3. **Cosmetic / clarity.** Batch and resolve quickly.

## Weight the AE over a divergent referee, but answer everyone

When referees conflict, the **AE's letter is the decision signal** — prioritize the concerns the AE foregrounds, and where two referees disagree, say how you reconciled them and why. Never silently side with one referee against another; make the resolution explicit so the AE can see your reasoning. Answer every comment, even the ones you decline.

## Draft the point-by-point response

- **Lead with a summary** of the major changes and how the contribution is now sharper for IS management.
- **Quote each comment, then respond** with what you changed, where (section/table/page), and the result. Show, do not assert: paste the new estimate, the new validity figure, the new robustness column.
- **Where you decline,** give a reasoned, evidence-backed explanation — politely and without defensiveness.
- **Keep the revised paper inside ≤50 pages** even after additions; if new analyses crowd the body, move support to the online appendix rather than overrunning the limit.
- **Maintain anonymization** in the revised manuscript and respect the numbered-reference style throughout.

## Match the fix to the right skill

| Referee concern | Where the real fix happens |
|-----------------|----------------------------|
| Contribution unclear / incremental | `jmis-contribution-framing` (+ `jmis-literature-positioning`) |
| Endogeneity / weak identification | `jmis-data-analysis` (+ `jmis-methods`) |
| Construct validity / common-method bias | `jmis-data-analysis` |
| Not robust / not generalizable | `jmis-data-analysis` |
| Exhibits unclear | `jmis-tables-figures` |
| Prose / abstract / framing | `jmis-writing-style` |

## Checklist

- [ ] Every comment is triaged: real fix / clarification / reasoned decline
- [ ] Fit/contribution concerns are addressed first and lead the letter
- [ ] AE's emphasis is prioritized; conflicting referees explicitly reconciled
- [ ] Each response names the change, its location, and the result (with new numbers)
- [ ] Declines are justified with evidence, not asserted
- [ ] Revised manuscript stays ≤50pp, anonymized, with numbered references

## Anti-patterns

- A defensive letter that argues with referees instead of resolving concerns
- Answering robustness asks while leaving the contribution doubt untouched
- Silently following one referee against another without explaining the reconciliation
- "We have addressed this" with no pointer to the change or new evidence
- Letting added analyses push the paper past 50 pages or break anonymization

## Output format

```text
【Decision type】major / minor revision
【Lead change】how the IS-management contribution is now sharper
【Comment triage】#fixes / #clarifications / #reasoned-declines
【AE emphasis】the concerns prioritized; conflicts reconciled
【Response letter】point-by-point, each with location + new result
【Constraints kept】≤50pp / anonymized / numbered refs
【Underlying fixes routed to】jmis-data-analysis / jmis-contribution-framing / jmis-tables-figures / …
```
