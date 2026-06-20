---
name: jpam-review-process
description: Use when anticipating how a Journal of Policy Analysis and Management (JPAM) manuscript will be evaluated — desk screening, double-blind peer review, the article types and which are not peer-reviewed, decision categories, and what JPAM referees reward and punish. Sets expectations; it does not write the paper or the rebuttal.
---

# Review Process (jpam-review-process)

Knowing how JPAM judges papers lets you pre-empt the objections that sink them. JPAM is an APPAM /
Wiley journal with an anonymized-review preflight and a stated right to **desk-reject without review**.
The reviewer pool is cross-disciplinary, so a paper must satisfy an economist's identification standard
*and* a policy reader's relevance standard at once. (Verify volatile specifics on the author page:
检索于 2026-06；以官网为准.)

## When to trigger

- Before submission, to stress-test against likely referee objections
- Deciding which article type to target and whether it is peer-reviewed
- Interpreting a decision letter and planning next steps
- Understanding the desk-screen so you avoid an avoidable desk reject

## How JPAM evaluates (the working model)

1. **Desk screen.** Editors may **desk-reject without review** for fit (not a credible policy
   evaluation / out of scope), inadequate identification, or insufficient significance. The submission
   must also satisfy the membership-or-fee requirement before it is considered (see `jpam-submission`).
2. **Anonymized review preparation.** Prepare an anonymized manuscript plus a separate title page; follow
   the live Research Exchange file labels and anonymity prompts. Anonymize self-references.
3. **Cross-disciplinary referees.** Expect at least one identification-focused reviewer and one
   policy/field reviewer. Both must be satisfied — strong design, real relevance.
4. **Decision categories.** Reject / major or minor revision (R&R) / accept (exact category labels vary;
   confirm on the live page). R&R is the common path to publication for promising papers.

## Article types and peer review

| Type | Peer-reviewed? | Note |
|------|----------------|------|
| Feature Research Article | Yes | the main research format |
| Methods for Policy Analysis | Yes | methodological advances for analysts |
| Policy Retrospective | Typically (confirm) | reflective look-back |
| Point/Counterpoint | **No** (invited) | short scholarly debate |
| Policy Insights | **No** (invited; ≤ 3,000 words) | rapid, timely take |
| Book Reviews | No (invited/edited) | — |

## What JPAM referees reward / punish

- **Reward:** credible identification, a clear policy implication calibrated to the design, cost-benefit
  and distributional attention, cross-field relevance, and a reproducible package.
- **Punish:** overclaiming beyond the estimand, selection-on-observables dressed up as causal, naive
  TWFE on staggered policies, no policy takeaway, ignoring who bears the costs, and irreproducible code.

## Checklist

- [ ] Manuscript survives a self-administered desk screen (fit, identification, significance)
- [ ] Correct article type chosen; peer-review status understood
- [ ] Double-blind anonymization done (text + self-cites + metadata)
- [ ] Design pre-tested against the reviewer-objection checklist
- [ ] Both an identification reviewer and a policy reviewer would be satisfied
- [ ] Replication package staged so it is not a late surprise

## Anti-patterns

- Submitting a paper that an editor will desk-reject for obvious fit/identification gaps
- Pitching a full research paper into the non-reviewed Point/Counterpoint or Policy Insights slots
- Satisfying the identification reviewer while ignoring the policy reviewer (or vice versa)
- Leaving anonymization, fee/membership, or the data package to the last moment

## Output format

```
【Desk-screen risk】fit / identification / significance — clear? [Y/N]
【Article type】+ peer-reviewed? [Y/N]
【Anonymization】text + self-cites + metadata clean? [Y/N]
【Referee coverage】identification + policy reviewers both satisfied? [Y/N]
【Package staged】replication materials ready? [Y/N]
【Next】jpam-submission
```

## Supplementary resources

- [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md) — objections by identification strategy
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review model, article types, decision-category guardrails
