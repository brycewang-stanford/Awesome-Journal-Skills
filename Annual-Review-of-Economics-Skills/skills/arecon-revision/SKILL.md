---
name: arecon-revision
description: Use when responding to Editorial Committee and referee feedback on an Annual Review of Economics (ARE) review — coverage gaps, balance/accuracy complaints, framework/structure asks, and accessibility. Drafts the response and revision plan; it does not run the delivery preflight (arecon-submission) or redesign the spine from scratch (arecon-organizing-framework).
---

# Revision & Response for a Review (arecon-revision)

## When to trigger

- A Committee/referee letter on the invited review arrived
- Referees flagged missing literatures, imbalance, mischaracterization, or "reads like a list"
- The editor asked to expand, cut, or rebalance coverage, or to make the framework explicit
- You need a point-by-point response for a review article, not a primary paper

## Categories of review feedback (and how to answer each)

ARE revision asks cluster differently from primary-research asks. Triage every point into one bucket:

| Feedback type | Typical phrasing | Response move |
|---------------|------------------|---------------|
| **Coverage gap** | "you omit the X literature / author Y" | almost always *concede and integrate* — place the missing work in the right framework cell; re-run saturation (`arecon-literature-synthesis`) |
| **Balance / fairness** | "this slights school Z / over-cites the author" | steelman the slighted side; re-audit self-citation (`arecon-evidence-standards`) |
| **Appraisal accuracy** | "you mischaracterize study W" | correct precisely; reviewed authors often referee — fix exactly |
| **Framework / structure** | "this is an annotated bibliography" | strengthen or make explicit the spine (`arecon-organizing-framework`); do not just reorder paragraphs |
| **Accessibility** | "a non-specialist can't follow Section 4" | add intuition, define jargon (`arecon-writing-style`) |
| **Scope** | "too broad / too narrow / overruns length" | negotiate with the editor (`arecon-editor-strategy`); rescope deliberately, within the page envelope |

## AREcon-specific revision ledger

Annual Review of Economics revisions should leave a clear economics review contract, not just a
longer bibliography. Maintain a ledger that tells the editor how each change sharpens what an
economist can learn from the review.

| Revision pressure | Evidence to add or rebalance | Where it should show up |
|-------------------|------------------------------|--------------------------|
| Theory/model spine is unclear | canonical model, mechanism, or comparative-static logic | opening framework figure/table, section road map |
| Empirical frontier is uneven | design map: data, identification, estimand, limitation | evidence table and "what we know" summary |
| Magnitudes are under-interpreted | elasticities, welfare-relevant units, or scale benchmarks | synthesis paragraphs, not just citations |
| Field boundary is disputed | adjacent JEL literatures and handbook/JEP-style anchors | boundary note explaining inclusion/exclusion |
| Policy or welfare stakes are vague | clarified mechanism-to-policy channel and uncertainty | conclusion/agenda, with caveats preserved |
| Adjacent economists cannot follow | intuition before notation, plain-language result labels | section openings and table captions |

Use the ledger to prevent a common AREcon failure mode: adding every requested citation while the
review's economic proposition becomes less visible.

## Writing the response letter

- **Point-by-point, quote-then-respond.** Reproduce each comment, then state the change and where it lives (section/page/table).
- **Coverage asks: concede and integrate.** A missing literature is a real defect in a review of record; adding it strengthens the article. Resist defensiveness — the omitting author may be the referee who named it.
- **Balance asks: show the steelman.** Demonstrate the revised text states the other side at its strongest; that is what a fairness complaint actually demands.
- **Accuracy asks: fix exactly.** Mischaracterizing a reviewed author who is your referee is the fastest route to a hostile second round; correct the wording precisely and, where helpful, quote their own framing.
- **Translate additions into economic learning.** When you add a literature, say whether it changes a
  mechanism, an estimand, a benchmark magnitude, or only the historical coverage.
- **Separate evidence classes.** Do not let theory, calibration, quasi-experiment, structural estimate,
  and descriptive trend evidence collapse into one "evidence says" paragraph.
- **Disagree rarely and respectfully.** If an ask would break the spine or overrun the page envelope, explain the trade-off and propose an alternative, ideally pre-cleared with the editor.
- **Keep the editor central.** On scope and conflicting referee asks, ask the Committee editor to adjudicate rather than satisfying mutually-incompatible referees.
- **Track every addition's ripple.** Adding a literature can shift the review's center of gravity; after each integration, re-check that the framework cells, the summary tables, and the balance audit still hold, and that the draft still fits the volume's length envelope.
- **Mind the volume clock.** Revisions run against a production deadline (`arecon-review-process`); plan the rework so the article stays in its volume.

## Checklist

- [ ] Every comment triaged into a bucket (coverage / balance / appraisal / framework / accessibility / scope)
- [ ] Coverage gaps conceded and integrated into the right framework cell; saturation re-run
- [ ] Balance complaints answered by demonstrable steelmanning + self-citation re-audit
- [ ] Mischaracterizations corrected precisely (reviewed authors may be the referees)
- [ ] "Annotated bibliography" asks answered by a stronger/explicit spine, not reordering
- [ ] Theory, identification, magnitude, boundary, and policy/welfare stakes separated in the revision ledger
- [ ] Accessibility fixes add intuition / define jargon for the adjacent economist
- [ ] Scope conflicts routed to the editor; rework fits the page envelope and the volume deadline
- [ ] Point-by-point letter: quote-then-respond, with section/page/table locations
- [ ] Comprehensiveness + balance re-audited after all additions

## Anti-patterns

- Defending an omission rather than adding the missing literature (a review gap is a real defect)
- Answering a balance complaint with assertions of fairness instead of revised, steelmanned text
- Dismissing or re-mischaracterizing a reviewed author who is likely your referee
- "Fixing" an annotated-bibliography critique by shuffling paragraphs without imposing a spine
- Treating theory, reduced-form evidence, structural estimates, and descriptive facts as interchangeable support
- Adding policy motivation without preserving the review's uncertainty and welfare-relevant caveats
- Bloating scope to satisfy every "also cover…" until the review overruns its length and slips the volume
- Trying to satisfy two contradictory referees instead of asking the editor to decide

## Output format

```text
【Triage】each comment bucketed (coverage/balance/appraisal/framework/accessibility/scope)? Y/N
【Coverage gaps】conceded + integrated into framework cells; saturation re-run? Y/N
【Balance】steelman shown in revised text; self-citation re-audited? Y/N
【Appraisal fixes】mischaracterizations corrected precisely? Y/N
【Framework asks】spine strengthened/made explicit (not reordered)? Y/N
【Economics ledger】theory/design/magnitude/boundary/policy stakes separated? Y/N
【Scope/length】fits page envelope + volume deadline? Y/N
【Letter】point-by-point, quote-then-respond, with locations? Y/N
【Next step】→ arecon-submission (re-deliver the revised review)
```
