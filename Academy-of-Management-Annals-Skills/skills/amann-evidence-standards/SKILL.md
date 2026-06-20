---
name: amann-evidence-standards
description: Use when appraising the cumulative evidence and ensuring balance in an Academy of Management Annals (Annals) review — weighing conflicting findings by credibility, steelmanning rival schools, and handling the author's own work even-handedly. Audits evidence quality and fairness; it does not design the framework (amann-organizing-framework) or build exhibits (amann-tables-figures).
---

# Evidence Standards — Appraisal & Balance (amann-evidence-standards)

## When to trigger

- The framework is set and you are filling cells with the literature
- The field has rival schools, a live controversy, or conflicting empirical results
- You must decide whether to cite *everything* or curate, and how to weigh disagreeing studies
- You are a contributor to this literature and worry the review tilts toward your own work

## At Annals you are the field's reviewer-of-record

An Annals review carries no estimates of its own — but it is not therefore neutral. The "attitude" is **disciplined critical appraisal**: you judge how good the cumulative evidence is, reconcile conflicts by credibility, and state where the field's confidence is and is not warranted. This is the review-craft replacement for primary-research robustness checks: you are appraising *other people's* designs, not defending your own.

## Completeness vs. selectivity: the Annals contract

A review must be **comprehensive in coverage** yet **selective in emphasis** — long (~50 pages) but not an inventory. Resolve the tension by **tiering** the corpus:

| Tier | Treatment |
|------|-----------|
| **Foundational / field-defining** | discussed in text — what it established and its limits |
| **Important contributions** | grouped and weighed within the framework's cells; cited with their finding |
| **Confirmatory / incremental** | cited in clusters ("see also …") to show coverage without bloating prose |
| **Tangential** | cited only where it bears on a specific claim |

Comprehensiveness is proven by the *citation set* (the saturation log from `amann-literature-synthesis`); selectivity is exercised in the *prose*. Equal-length summaries of every paper abdicate the editorial judgment that is the review's value.

## Weighing conflicting evidence (not vote-counting)

Management findings conflict constantly. Reconcile them by **why they differ**, never by tally:

- **Weigh by credibility.** Design strength (causal vs. correlational), sample, measurement validity, replication, and publication-bias risk — not "9 studies positive, 4 negative."
- **Separate by construct and context.** Studies often disagree because they measure different constructs or run in different settings; surface that rather than forcing a false consensus.
- **Flag the cumulative-evidence quality.** State plainly where the evidence is strong, mixed, or thin — and where apparent consensus rests on a few non-independent studies.
- **Name what would settle it.** For a live debate, specify the study design that would resolve it (this seeds the agenda).

## Fairness across schools and the self-citation trap

Annals is the **review-of-the-field**: its account of a debate becomes the field's shared reference, and **the surveyed authors often referee the review**. Balance is therefore both ethical and strategic.

- **Steelman every camp.** State each school's strongest case in terms its proponents would accept *before* critiquing it. Refute positions at their best.
- **Attribute ideas to originators**, not popularizers — a recurring referee complaint.
- **Audit self-citation.** Your own work is cited at the tier its *importance to the field* warrants — no more. Rivals get their strongest statement. A reader who does not know who wrote the review cannot tell from the emphasis.
- **Label your read as your read.** Where you take a provocative position (the "attitude"), mark it as the author's judgment, not as settled consensus.

## Checklist

- [ ] Corpus tiered (foundational / important / confirmatory / tangential); prose emphasis matches tier
- [ ] Comprehensiveness provable from the citation set + saturation log
- [ ] Conflicting findings reconciled by credibility, construct, and context — not vote-counting
- [ ] Cumulative-evidence quality stated (strong / mixed / thin) per claim
- [ ] Every rival school stated at its strongest before critique (steelman)
- [ ] Idea attribution traces to originators
- [ ] Self-citation audited: own work at field-warranted tier; emphasis identity-blind
- [ ] Provocative positions labelled as the author's read; what-would-settle-it named for live debates
- [ ] No important author/school an informed referee could say was slighted or omitted

## Anti-patterns

- Comprehensiveness theatre: equal-length summaries of every paper (no editorial judgment)
- Vote-counting conflicting results instead of weighing credibility, construct, and context
- Treating all findings as equally credible regardless of design quality
- Strawmanning the camp the author disagrees with (the referee may be that camp)
- A review that doubles as the author's CV (the most-punished balance failure)
- Declaring a live controversy "resolved" by assertion rather than by laying out the evidentiary state

## Output format

```text
【Tiering】corpus split foundational/important/confirmatory/tangential? Y/N
【Comprehensiveness evidence】saturation log + citation set support "nothing important missing"? Y/N
【Conflict handling】reconciled by credibility + construct + context (not vote-count)? Y/N
【Evidence quality】strong/mixed/thin stated per claim? Y/N
【Steelman】each rival school stated at its strongest? Y/N
【Self-citation audit】own work at warranted tier; emphasis identity-blind? Y/N
【Attitude labelled】provocative reads marked as author's judgment? Y/N
【Next skill】→ amann-tables-figures (who-found-what tables + framework figure)
```
