---
name: jleo-referee-strategy
description: Use when anticipating the referee read on a Journal of Law, Economics, and Organization (JLEO) manuscript before submitting — modeling the institutional/organizational economist who will review it and pre-empting the objections that sink JLEO papers. Anticipates objections; it does not write the response to an actual report (jleo-rebuttal).
---

# Referee Strategy (jleo-referee-strategy)

## When to trigger

- The paper is near submission and you want to see it through a JLEO referee's eyes first
- You suspect a credibility gap (selection into governance, reform endogeneity, a decorative model) that a referee will find
- The contribution is real but might read as "applied micro with institutional labels" to a TCE/PPE reviewer
- You need to decide which weaknesses to fix now versus flag transparently in the cover letter
- The paper sits near a sibling boundary and a referee might say "this belongs at JLE / Org Science"

## Who reviews at JLEO and what they look for

JLEO referees are drawn from the institutional and organizational economics and PPE communities — people fluent in transaction-cost economics, contract theory, and the political economy of institutions. They are unusually attentive to two things generic economics referees are not: (1) whether the **institutional mechanism** is real and named, and (2) whether the empirical object — usually *chosen* by the agents — is credibly identified despite that choice. Model the reviewer, then pre-empt.

## The objections that recur at JLEO

| Likely referee objection | Pre-empt by |
|--------------------------|-------------|
| "This is applied micro dressed as institutional economics" | Make the institutional mechanism the headline; show the result speaks to a JLEO frontier (jleo-literature-positioning) |
| "Governance form is endogenous — you've measured selection" | Address selection head-on with IV / selection model / shock; bound it (jleo-identification, jleo-robustness) |
| "The model adds notation but no prediction the intuition lacked" | Make comparative statics the deliverable; flag the surprising one (jleo-theory-model) |
| "Reform timing is endogenous to the outcome" | Show timing exogeneity, anticipation tests, clean event-study leads |
| "Your institutional measure is not valid" | Validate the construct with alternative measures; document coding (jleo-replication-package) |
| "An alternative mechanism explains this" | Include a test only your mechanism predicts |
| "This belongs at JLE / Org Science" | State the organization/PPE payoff that makes it JLEO, not a sibling |

## Strategy moves

1. **Triage by severity.** Separate fatal objections (identification, contribution) from fixable ones (an extra robustness table). Fix the fatal ones before submitting; do not gamble that the referee will miss them.
2. **Pre-empt in the text, not just in your head.** For each anticipated objection, put the defense where the referee will look — a paragraph, a robustness table, a footnote — so the report can say "the authors already address this."
3. **Use the cover letter for honest limitations.** Flag a known limitation transparently rather than hoping it goes unnoticed; institutional referees respect candor and punish concealment.
4. **Suggest reviewers who know the tradition.** If the system allows suggestions, name scholars in the relevant TCE/PPE conversation who will read the mechanism charitably and competently — and note conflicts to avoid.
5. **Decide the sibling-boundary defense in advance.** Have a one-paragraph answer to "why JLEO and not JLE/Org Science" ready, because a referee may raise it as a desk-level concern.

## Checklist

- [ ] The institutional mechanism is unmistakable to a TCE/PPE referee on first read
- [ ] The endogeneity of the governance form / institution is addressed in the text, not just acknowledged
- [ ] The model's value-add (a prediction the intuition lacked) is visible
- [ ] Each anticipated objection has a defense placed where the referee will look
- [ ] The sibling-boundary answer (why JLEO) is written and ready
- [ ] Known limitations are flagged honestly, ideally in the cover letter

## Anti-patterns

- Hoping the referee misses the selection problem instead of confronting it
- A defense that lives only in your head, not in the manuscript where the referee reads
- Concealing a limitation that an institutional referee will find anyway
- Suggesting reviewers who are conflicted, or who work in a different (JLE/Org-Science) tradition
- No prepared answer to "why isn't this a JLE / Organization Science paper?"

## Worked vignette (illustrative)

A paper argues that delegating rule-making to an independent agency improves regulatory quality. Anticipating the JLEO referee: the fatal objection is endogeneity — legislatures delegate precisely where they expect quality gains, so the estimate may be selection. The author pre-empts by exploiting a constitutional change that forced delegation for a subset of policy areas regardless of expected gain, places the design in Section 3 where any referee looks first, and writes the cover-letter limitation that external validity is bounded to the affected areas. The second-order objection ("this is political science, not JLEO") gets a ready paragraph: the payoff is a PPE claim about the credible-commitment value of delegation — squarely the North–Weingast line — with formal comparative statics, making it JLEO and not QJPS.

## Output format

```text
【Top 3 anticipated objections】1) ___ 2) ___ 3) ___
【Severity】fatal (fix now) / fixable (table/footnote)
【Pre-empt location in MS】where each defense lives
【Sibling-boundary answer】why JLEO not JLE/Org Science (one paragraph ready)
【Cover-letter limitations】what to flag transparently
【Suggested reviewers】TCE/PPE scholars; conflicts noted
【Next skill】jleo-submission
```
