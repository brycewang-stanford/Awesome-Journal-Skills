---
name: revedres-proposal-and-commissioning
description: Use when writing the protocol, fixing scope and eligibility, and (where applicable) preregistering a systematic review or meta-analysis before searching, for a Review of Educational Research (RER) manuscript. Produces the a-priori plan; it does not run the search (revedres-literature-synthesis) or impose the conceptual spine (revedres-organizing-framework).
---

# Protocol & Preregistration (revedres-proposal-and-commissioning)

## When to trigger

- Topic selection cleared the four RER fit tests and it is time to lock the plan
- You are about to search but have not written down inclusion/exclusion rules
- You want a PROSPERO / OSF registration so the search is demonstrably a-priori
- A reviewer is likely to ask "were these inclusion rules set before or after you saw the results?"

## RER is SUBMITTED, not commissioned — the protocol replaces the commission

Annual Reviews *invite* their authors; **RER reviews are submitted and peer-reviewed**, so no editor pre-blesses your scope. The credibility that an invitation would have signaled must instead come from a **transparent, a-priori protocol**. For a systematic review or meta-analysis this is not optional polish — it is the difference between a synthesis and a fishing expedition. (RER occasionally publishes *solicited* analytic reviews of special topics, but the default and the bar is a strong unsolicited submission — 检索于 2026-06；以官网为准.)

## The protocol: decisions to fix BEFORE you search

Write these down first; a reviewer who senses they were chosen after seeing results will distrust the whole review.

1. **Question in PICO/PICOS form.** Population (learners/settings), Intervention/exposure or construct, Comparison, Outcomes, Study designs. This *is* the scope.
2. **Eligibility criteria.** Inclusion and exclusion on population, constructs, designs, outcomes, language, publication type (peer-reviewed? grey literature? dissertations?), and date range — each with a reason.
3. **Information sources & search strategy.** Databases (ERIC, PsycINFO, Education Source, Web of Science, Scopus, ProQuest Dissertations), grey-literature sources, and at least one full search string to be reported verbatim.
4. **Screening procedure.** Two independent screeners at title/abstract and full-text; how disagreements are resolved; the reliability statistic you will report.
5. **Data extraction & coding scheme.** What you will code from each study (design, sample, measures, effect sizes, moderators, risk-of-bias) and the codebook.
6. **Synthesis plan.** Meta-analytic model (fixed/random/multilevel/robust variance), effect-size metric, planned moderator and sensitivity analyses, and publication-bias diagnostics — *or* the explicit qualitative/narrative synthesis method for a non-poolable literature.
7. **Risk-of-bias / quality appraisal tool** chosen in advance (e.g. a design-appropriate instrument).

## Preregistration: register the plan, then deviate transparently

- **Systematic reviews / meta-analyses:** register the protocol on **PROSPERO** (health-adjacent) or **OSF** before screening; cite the registration in the manuscript. Use **PRISMA-P** as the protocol-reporting checklist.
- A registration is a commitment, not a cage — you *may* change the plan, but you must **flag and justify every deviation** in the paper (planned vs. exploratory analyses kept distinct).
- Purely conceptual/critical syntheses are not "registered" the same way, but they still need an explicit, written scope and search logic that the paper reports.

## Why a-priori discipline pays off at RER specifically

A protocol is not bureaucratic overhead — it is what lets a *submitted* review be trusted the way an *invited* one is. Three concrete payoffs:

- **It pre-empts the "fishing expedition" objection.** A reviewer who sees that inclusion rules, the model, and the moderators were fixed before screening cannot claim they were chosen to produce a clean result.
- **It makes the PRISMA flow honest.** Counts flow from rules set in advance, so the diagram reports what the search found rather than what survived after-the-fact pruning.
- **It separates confirmatory from exploratory.** Anything not in the protocol is labeled exploratory in the paper — which protects the headline result and still lets you report interesting surprises.

A common failure is treating the protocol as a draft of the paper. It is not prose; it is a set of **decision rules** a stranger could execute and reach your corpus. Write it as rules, register it, then let the search run against it.

## Checklist

- [ ] Question in PICO/PICOS; scope bounded the same way the search will be
- [ ] Eligibility criteria written with a reason for each inclusion/exclusion rule
- [ ] Databases + grey-literature sources listed; at least one full search string drafted
- [ ] Dual independent screening defined; reliability statistic chosen
- [ ] Coding scheme / codebook drafted before extraction
- [ ] Synthesis plan fixed (meta-analytic model + moderators + bias diagnostics, or narrative method)
- [ ] Risk-of-bias tool chosen a-priori
- [ ] Registered on PROSPERO/OSF (or scope/search logic written for a conceptual synthesis)

## Anti-patterns

- Searching first, then writing inclusion rules to fit the studies you liked
- "Random-effects, REML" chosen after seeing heterogeneity rather than in advance
- No codebook — coders improvise, and reliability cannot be defended later
- Treating registration as a formality, then silently changing the question or outcomes
- Promising an exhaustive search but planning only one database

## Output format

```
【Question (PICOS)】<population / intervention-construct / comparison / outcomes / designs>
【Eligibility】<key inclusion + exclusion rules, each with a reason>
【Sources + search】<databases + grey lit; one full search string drafted? Y/N>
【Screening】dual independent? Y/N; reliability stat = <kappa/agreement>
【Coding scheme】codebook drafted before extraction? Y/N
【Synthesis plan】<meta-analytic model + moderators + bias diagnostics | narrative method>
【Risk-of-bias tool】<instrument, chosen a-priori>
【Registration】PROSPERO/OSF id or "conceptual synthesis — scope written"
【Next step】→ revedres-literature-synthesis (run the search to a PRISMA flow)
```
