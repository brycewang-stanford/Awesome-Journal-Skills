---
name: jbf-rebuttal
description: Use when responding to a Journal of Banking & Finance revise-and-resubmit, including triaging referee reports, strengthening identification, adding robustness, preserving anonymity where needed, and drafting a point-by-point response letter.
---

# R&R Rebuttal (jbf-rebuttal)

## When to trigger

- JBF returns a major or minor revision decision
- Referees request more identification, robustness, data detail, or mechanism evidence
- You need a response letter that is firm, empirical, and concise

## Triage first

Classify every comment:

1. **Must-do**: editor requests, identification threats, data errors, missing
   robustness, unclear contribution.
2. **Should-do**: additional heterogeneity, mechanism tests, clearer exposition,
   appendix reorganization.
3. **Negotiate**: infeasible data, out-of-scope extensions, tests that would
   answer a different paper.
4. **Clarify**: misunderstandings caused by your writing.

## JBF-style response strategy

- Put the editor's main concern first.
- For identification comments, add the strongest feasible test and explain what
  it does and does not rule out.
- For robustness comments, add a table or appendix panel with exact line/table
  references.
- For data comments, document sources, merge rules, sample attrition, and
  proprietary-data limits.
- For scope comments, tie revisions back to banking/finance implications.

## Response paragraph pattern

```text
We thank the referee for raising this point. We now [change made]. The new
analysis appears in Table X / Appendix Table Y and shows [result]. We also revised
page Z to clarify [interpretation]. This addresses the concern because [logic].
```

## Anti-patterns

- Arguing instead of adding evidence where evidence is feasible
- Saying "space constraints" when the appendix can carry the work
- Hiding null or weaker robustness checks
- Changing the design without updating the contribution claim

## JBF comment-to-fix map

| Typical JBF referee ask | Standard fix | Where it goes |
| --- | --- | --- |
| "Plain TWFE is biased under staggered adoption" | Re-estimate with a heterogeneity-robust DID estimator; show both side by side | main table + event-study figure |
| "Results may be a crisis artifact" | Re-run excluding 2007–09 (and 2020 if in sample); report stability | appendix panel cited in the text |
| "Cluster at the policy level, not the bank" | Re-cluster; wild-cluster bootstrap if clusters are few | table notes + one robustness column |
| "Economic significance is unclear" | Convert to basis points / % of assets / capital-ratio points against a stated benchmark | results text + abstract |
| "The policy conclusion overreaches" | Bound the claim to the identified margin and treated population | conclusion rewrite, flagged in the letter |

## Worked response pass (illustrative)

Referee: "Your staggered-deregulation DID relies on TWFE, which recent econometrics shows can be badly weighted."

- Action: re-estimate with a robust estimator; suppose TWFE gives −1.8% and the robust estimator −2.4% (illustrative), with flat pre-event coefficients.
- Letter: report both numbers, note the conclusion is unchanged or strengthened, and point to the new event-study figure plus an estimator note.
- Manuscript: promote the robust estimate to the baseline; keep TWFE as a comparison column rather than deleting it.

## Negotiation lines that hold up at JBF

- Infeasible supervisory data: offer aggregate moments plus full code, citing the confidentiality regime, rather than a flat refusal.
- Out-of-scope structural-model request: offer a stylized mechanism subsection and bound the empirical claim instead.
- Sample extension beyond the data license: state vendor coverage limits and show stability on the overlapping window.

## Letter skeleton

```text
Dear Editor,
[1] One paragraph on what the revision does, led by the editor's own concern.
[2] Summary table: comment -> change -> location (table/page).
Referee 1
  R1.1 [restate the point fairly] / Response: [evidence, exact table and page]
  ...
Referee 2 ...
[Closing] remaining limitations stated plainly; no new unflagged claims.
```

## Evidence ledger

For the response letter, maintain a ledger:

```text
Comment | New evidence | Location | Effect on claim | Remaining limitation
```

Every must-do comment should have a new evidence row or a clearly justified infeasibility row. If a new
test weakens the headline result, state the narrower finance interpretation and update the introduction.
JBF rebuttals are strongest when the response letter, manuscript text, and appendix all tell the same
story about identification, data limits, and economic magnitude.

## Output format

```text
[Decision type] major / minor / conditional
[Editor priority] ...
[Comment matrix] must-do / should-do / negotiate / clarify
[New analyses] ...
[Response tone] grateful, precise, evidence-led
[Next step] revise manuscript + response letter
```
