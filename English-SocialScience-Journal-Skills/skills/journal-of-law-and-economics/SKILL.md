---
name: journal-of-law-and-economics
description: Use when targeting Journal of Law and Economics (JLE) or deciding whether an empirical or applied law-and-economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Law and Economics (journal-of-law-and-economics)

## Journal positioning

JLE is the foundational Chicago law-and-economics journal, publishing empirical and applied economic analysis of law, regulation, crime, antitrust, and institutions. It rewards papers that bring credible data and economic reasoning to legal and regulatory questions, in the price-theory and empirical tradition associated with Chicago. The readership is economists and law-and-economics scholars, so a paper must combine a real legal/regulatory question with sound empirical or applied economic analysis.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the journal/University of Chicago Press site and the editorial submission system.

## When to trigger

- The author names JLE as the target venue, or wants a Chicago-tradition law-and-economics home.
- An empirical paper studies the effects of law, regulation, crime, or antitrust with credible data.
- A regulation or institutions paper needs re-framing so the contribution reads as empirical law-and-economics, not legal doctrine or pure policy.
- The author needs JLE's desk-reject risks and a credible law-and-economics alternative list.

## Scope & topic fit

- The economics of law and regulation: effects of legal rules, enforcement, and regulatory regimes.
- Antitrust, competition, and industrial regulation analyzed empirically.
- Crime, deterrence, punishment, and the economics of the legal/criminal-justice system.
- Institutions, property rights, contracting, and the economic analysis of legal and regulatory change.

## Method & evidence bar

- Credible empirical analysis is the filter: identification (experiments, quasi-experiments, DiD, IV, RDD, or well-justified design) with threats pre-empted.
- Data quality and measurement of legal/regulatory variables (treatment timing, enforcement intensity) must be defensible.
- Modern estimators and correct inference are expected; applied price-theory reasoning should connect the law/regulation to the economic outcome.
- The contribution is a credible effect of a legal/regulatory feature with an economic mechanism, not a descriptive correlation.

## Structure & house style

- The introduction states the legal/regulatory question, the data, the identification, and the headline result early, and says why it matters for law, regulation, or institutions.
- Position against the relevant law-and-economics literature; "first to study legal change X" is not a contribution without an advance.
- Uses an unstructured abstract; an appendix carries robustness, institutional detail, and data construction.
- Exhibits report interpretable magnitudes and transparent identification, with the legal/regulatory variation clearly described.

## Official-submission checklist

- Search the live site for "Journal of Law and Economics submission guidelines / instructions for authors" and follow the current University of Chicago Press version.
- Re-check formatting, abstract requirements, anonymization, and figure/table standards on the submission system.
- Re-check the current data and code availability / replication policy and any legal-data disclosure requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this result matters for law, regulation, antitrust, or institutions.
- [ ] The contribution is stated as a credible effect of a legal/regulatory feature + mechanism, not as statistical significance.
- [ ] The introduction positions the paper against the current law-and-economics frontier on this question.
- [ ] Identification threats are addressed by design; legal/regulatory variation and measurement are defensible.
- [ ] Data, code, and institutional appendix are ready for the official policy.

## Common desk-reject triggers

- A descriptive correlation between a legal rule and an outcome with no credible identification.
- A legal-doctrine or pure-policy paper with no empirical or applied-economics contribution.
- Mismeasured or hand-waved legal/regulatory treatment with no institutional detail.
- "First to study regulation X" with no economic mechanism or methodological advance.

## Re-routing decision

- Law–economics–organization, positive political theory, contracts, and institutions framing → `journal-of-law-economics-and-organization`.
- Antitrust/regulation with an IO-theory or industry core → `rand-journal-of-economics`; crime/enforcement with a public-finance core → `journal-of-public-economics`.
- General-interest at the top → `american-economic-review`; broad general field → `european-economic-review`; technically heavy identification → `journal-of-applied-econometrics` or `international-economic-review`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Law and Economics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the empirical identification clear JLE's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / abstract / data-code policy / legal data / exhibits>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
