---
name: jcf-rebuttal
description: Use when preparing a revise-and-resubmit response for the Journal of Corporate Finance (JCF) — a point-by-point reply to two-or-more single-anonymized reviewers and the handling editor, reconciling divergent demands without over-claiming. It structures the response letter and revision plan; it does not run new analysis on its own.
---

# R&R Rebuttal (jcf-rebuttal)

## When to trigger

- You received an R&R from JCF and must write the response letter
- Two or more reviewers asked for **different or conflicting** things
- You need to map each comment to a concrete revision

## How JCF R&R works

JCF review is **single anonymized** with a **minimum of two reviewers**, so you typically face **two independent sets of demands** plus the editor's priorities. Reviewers see your identity; the editor decides whether the revision clears the bar. Address every point, but prioritize the editor's framing.

## Response-letter structure

1. **Cover note to the editor**: thank them, summarize the **main changes**, and state how the revision resolves the core concern. Flag any request you respectfully decline and why.
2. **Per-reviewer sections**: restate each comment **verbatim**, then your response, then the **exact change** (section/table/page).
3. **Reconcile conflicts**: when reviewers disagree, state the trade-off, choose a defensible path, and show both robustness results where feasible.

## Revision discipline

- [ ] Every comment has a numbered, traceable response
- [ ] New analyses are added as **robustness**, not a redesign that contradicts the paper
- [ ] Identification concerns answered with diagnostics/placebos, not rhetoric (see jcf-identification-strategy)
- [ ] No new **over-claiming**; scope still matches the design
- [ ] Updated Option C data-availability statement / archive if the empirics changed
- [ ] Abstract still ≤ 250 words; references still consistent (see jcf-writing-style)

## Reviewer-conflict table

Use this when reviewers push in different directions:

```text
Issue | Reviewer A asks | Reviewer B asks | Editor signal | Chosen response | Evidence added
```

The chosen response should protect the corporate-finance mechanism and the identification design. If a
requested analysis would answer a different paper, acknowledge the point, add the closest feasible
diagnostic, and state why the manuscript keeps its original scope. Do not let an R&R turn a clean shorter
format paper into an unfocused full-length paper.

## Comment-type playbook for JCF reviews

```text
Comment type      | Typical JCF ask                              | Response move
Identification    | Modern DID estimator; selection discussion   | New diagnostic + estimator table, not rhetoric
Magnitude         | "Is this economically big?"                  | Convert to % of mean / 1-SD; add a magnitudes row
Sample            | Filters, financials exclusion, survivorship  | Reconstruction table; result on the alternate sample
Mechanism         | "Why does this happen?"                      | Cross-sectional splits the channel predicts
Generalizability  | One shock, one country                       | Bound the claim; add an external-validity paragraph
Framing / fit     | "Is this corporate finance?"                 | Reframe the headline on the firm decision
```

## Worked reply: the staggered-DID demand

Hypothetical, numbers illustrative: Reviewer 1 writes "TWFE on staggered adoption is biased; use Callaway–Sant'Anna." The reply that works at JCF: (1) restate the comment verbatim; (2) report the new estimate — TWFE 0.024 versus CS 0.015, both significant — in a new table promoted to the main text; (3) move the Bacon decomposition showing where TWFE weight sat into the appendix; (4) one sentence in the letter: "The headline estimate is now the heterogeneity-robust one; conclusions are unchanged in sign, economically smaller, and the text now reports the smaller magnitude." No defensiveness, and no claim that the old estimator was fine.

## Routing new material in the revision

Common practice for JCF revisions (confirm against the journal's current author guidelines): the main text absorbs analyses that change the headline or defend identification; bulk robustness moves to an appendix or a separately uploaded internet appendix referenced by exhibit number. In the letter, point to exact locations — "now Table 6, Panel B; Internet Appendix Table IA.4" — so two independent reviewers can verify changes without re-reading the full paper. If reviewers demanded conflicting estimators, run both, table both, and let the letter state which one the text features and why.

## Anti-patterns

- A response that argues without changing the paper.
- Silently ignoring a point the editor cares about.
- Caving to one reviewer in a way that breaks the other's concern.
- Letting the revision quietly over-claim beyond the design.

## Output

```
【Editor note】main changes + core concern resolved? [Y/N]
【Per-reviewer】each comment → response → exact change? [Y/N]
【Conflicts】reconciled with trade-off stated? [Y/N]
【Integrity】no new over-claim; ID diagnostics added? [Y/N]
```
