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
- [ ] The letter opens with a one-page summary of major changes
- [ ] Every response carries a verifiable pointer (section/table/page) the AE can check

## Worked move: converting a contested request into a resolved concern (illustrative)

A referee demands an instrument you do not have. Arguing "no valid instrument exists" reads as a dodge. The resolving move triangulates: add the within-unit/quasi-experimental evidence you *can* produce, run a selection-sensitivity analysis showing how large unobserved confounding would have to be to overturn the result, and state plainly the residual limitation in the discussion. You did not give the referee the exact tool requested, but you addressed the underlying worry — endogeneity — with evidence, and you let the AE see that the concern is now bounded rather than ignored. That is what "resolved, not just answered" means in an EIC-led process.

## Anti-patterns

- A defensive letter that argues with referees instead of resolving concerns
- Answering robustness asks while leaving the contribution doubt untouched
- Silently following one referee against another without explaining the reconciliation
- "We have addressed this" with no pointer to the change or new evidence
- Letting added analyses push the paper past 50 pages or break anonymization
- A response the AE cannot verify against the manuscript without hunting for the change
- Answering a contested request literally instead of resolving the underlying concern with available evidence
- Reintroducing identifying details in the revision letter or revised manuscript

## Structure the response document for fast adjudication

The EIC and AE adjudicate faster when the letter is built for scanning. Open with a one-page **summary of major changes** that states how the contribution is now sharper and lists the three or four biggest revisions. Then take each reviewer in turn, quoting every comment verbatim in a distinct font or block, followed by your response in plain text with an explicit pointer ("see revised Section 4.2, Table 3, p. 18") and the new result stated inline. Where the same concern came from multiple reviewers, answer it once and cross-reference, so the AE sees consistency rather than contradictions. Close each reviewer's section by inviting them to the specific changed passages. A response that the AE can verify against the manuscript without hunting is itself evidence that you took the review seriously.

## Route the underlying work, then write the letter

The response letter documents fixes; it does not perform them. Before drafting, send each substantive concern to the skill that owns the real change — identification and measurement to `jmis-data-analysis`, contribution doubts to `jmis-contribution-framing`, exhibit problems to `jmis-tables-figures` — and complete those revisions in the manuscript first. Then write the letter against the finished revision, so every "we have done X" points to a change that already exists. A letter written ahead of the work invariably overpromises and underdelivers.

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
