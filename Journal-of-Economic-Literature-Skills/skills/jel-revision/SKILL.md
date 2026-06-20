---
name: jel-revision
description: Use when responding to editor and referee feedback on a Journal of Economic Literature (JEL) survey — coverage gaps, balance complaints, framework/structure asks, and accessibility. Drafts the response letter and revision plan; it does not run the submission preflight (jel-submission) or redesign the spine from scratch (jel-organizing-framework).
---

# Revision & Response for a Survey (jel-revision)

## When to trigger

- An editor/referee letter on the survey arrived (revise-and-resubmit or major revision)
- Referees flagged missing literatures, imbalance, or "reads like a list"
- The editor asked to expand, cut, or rebalance coverage
- You need a point-by-point response letter for a survey, not a primary paper

## Categories of survey feedback (and how to answer each)

JEL revision asks cluster differently from primary-research asks. Triage every point into one bucket:

| Feedback type | Typical phrasing | Response move |
|---------------|------------------|---------------|
| **Coverage gap** | "you omit the X literature / author Y" | almost always *concede and integrate* — place the missing work in the right framework cell; re-run saturation (`jel-literature-synthesis`) |
| **Balance / fairness** | "this slights school Z / over-cites the author" | steelman the slighted side; re-audit self-citation (`jel-comprehensiveness-and-balance`) |
| **Framework / structure** | "this is an annotated bibliography" | strengthen or make explicit the spine (`jel-organizing-framework`); do not just reorder paragraphs |
| **Appraisal accuracy** | "you mischaracterize study W" | correct the characterization; surveyed authors often referee — fix precisely |
| **Accessibility** | "a non-specialist can't follow Section 4" | add intuition, define jargon (`jel-writing-style`) |
| **Scope** | "too broad / too narrow" | negotiate with the editor (`jel-editor-strategy`); rescope deliberately, not by random cuts |

## Writing the response letter

- **Point-by-point, quote-then-respond.** Reproduce each comment, then state the change and where it lives (section/page/table).
- **Coverage asks: concede gracefully and integrate.** A missing literature is a real defect in a survey of record; adding it strengthens the article. Resist defensiveness.
- **Balance asks: show the steelman.** Demonstrate the revised text states the other side at its strongest; this is what a fairness complaint actually demands.
- **Disagree rarely and respectfully.** If an ask would break the spine or expand scope unfinishably, explain the trade-off and propose an alternative, ideally pre-cleared with the editor.
- **Re-run the comprehensiveness audit** after integrating new material so additions do not unbalance the whole.
- **Keep the editor central.** On scope and conflicting referee asks, ask the editor to adjudicate rather than trying to satisfy mutually-incompatible referees.
- **Track every addition's ripple.** Adding a literature can shift the survey's center of gravity; after each integration, re-check that the framework cells, the summary tables, and the balance audit still hold, so a fix to one comment does not quietly break another.

## Checklist

- [ ] Every comment triaged into a bucket (coverage / balance / framework / appraisal / accessibility / scope)
- [ ] Coverage gaps conceded and integrated into the right framework cell; saturation re-run
- [ ] Balance complaints answered by demonstrable steelmanning + self-citation re-audit
- [ ] "Annotated bibliography" asks answered by a stronger/explicit spine, not reordering
- [ ] Mischaracterizations corrected precisely (surveyed authors may be the referees)
- [ ] Accessibility fixes add intuition / define jargon for the non-specialist
- [ ] Scope conflicts routed to the editor for adjudication
- [ ] Point-by-point letter: quote-then-respond, with section/page/table locations
- [ ] Comprehensiveness + balance re-audited after all additions

## Anti-patterns

- Defending an omission rather than adding the missing literature (a survey gap is a real defect)
- Answering a balance complaint with assertions of fairness instead of revised, steelmanned text
- "Fixing" an annotated-bibliography critique by shuffling paragraphs without imposing a spine
- Bloating scope to satisfy every "also cover…" until the survey no longer finishes
- Mischaracterizing or dismissing a surveyed author who is likely your referee
- Trying to satisfy two contradictory referees instead of asking the editor to decide

## Output format

```
【Triage】each comment bucketed (coverage/balance/framework/appraisal/accessibility/scope)? Y/N
【Coverage gaps】conceded + integrated into framework cells; saturation re-run? Y/N
【Balance】steelman shown in revised text; self-citation re-audited? Y/N
【Framework asks】spine strengthened/made explicit (not reordered)? Y/N
【Appraisal fixes】mischaracterizations corrected precisely? Y/N
【Scope conflicts】routed to editor? Y/N
【Letter】point-by-point, quote-then-respond, with locations? Y/N
【Next step】→ jel-submission (re-preflight the revised survey)
```
