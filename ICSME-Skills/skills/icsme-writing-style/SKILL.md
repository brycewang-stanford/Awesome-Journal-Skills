---
name: icsme-writing-style
description: Use when revising an IEEE ICSME paper for a maintenance/evolution contribution stated on the first page, research-question contracts, a threats-to-validity section that argues rather than recites, evidence proportional to the claim, double-anonymous wording, and disciplined use of the IEEEtran two-column 10-page budget.
---

# ICSME Writing Style

Use this when revising the main paper. ICSME papers are read by maintenance and evolution
empiricists, so they need a **software-maintenance contribution stated on the first page** and
evidence a reviewer trusts. The failure this skill prevents is a technically fine paper that reads
like a greenfield systems demo or a generic ML result with a maintenance title glued on — the
`icsme-topic-selection` re-route signal.

## Revision rules

- **Lead with the maintenance/evolution problem:** the situation a maintainer recognizes (a system
  aging under change, debt accruing, a refactoring nobody trusts, comprehension lost over years),
  why the current state is inadequate, the contribution, the evidence, and what changes for people
  who maintain software.
- **State research questions as contracts.** Each RQ names what is measured and how it will be
  judged; every RQ is answered explicitly in the results, and no result exists without an RQ it
  serves.
- **Pair every claim with proportional evidence** — real evolving subject systems, a fair baseline,
  a statistic with an effect size, or a qualitative code with agreement — not adjectives.
- **Argue threats to validity; do not recite them.** Name the construct, internal, external, and
  conclusion threats that actually bite *this* maintenance study (mining confounds, survivorship in
  change history, one-ecosystem generalization) and say what you did to bound each.
- **Respect the 10-page budget as a design constraint.** The IEEEtran two-column limit counts
  figures, tables, and appendices; a study that only fits by shrinking threats or method is
  over-scoped for the venue.
- **Maintain double-anonymity** in self-citations, tool names, the choice of your own system as a
  subject, acknowledgements, funding, and data-availability wording.

## Maintenance/evolution paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Maintenance problem, inadequacy, contribution, evidence preview, payoff — first page | Leads with a technology trend, not a maintenance pain |
| Background/Motivation | Why a maintainer or the evolution literature needs this now | Motivation by assertion, no grounding in practice |
| Approach / Study design | The technique or the RQs + mining/analysis protocol, reproducibly | Method too thin to re-run on other histories |
| Evaluation | Each RQ answered with proportional evidence on real systems | Metrics that proxy for the maintenance outcome |
| Threats to validity | The threats that bite this history/corpus, each bounded | Generic list untethered from this study |
| Related work | Delta-first positioning against the evolution literature | Catalog of citations with no contrast |

## Sentence-level rewrites

| Draft pattern | ICSME-safe rewrite |
|---|---|
| "Our tool significantly improves maintainability." | "reduces change-impact set size by X% (95% CI ...) vs. <baseline> on <N evolving systems>" |
| "We study a large software corpus." | "We mine <N> projects sampled by <criterion> over <time window>, listed in the artifact" |
| "Results show our refactoring is safe." | "RQ2: behaviour-preservation held on <fraction> of applications; threats in §5.2" |
| "State-of-the-art performance." | Claim scoped to the systems, change history, and metrics actually studied |
| "Developers understood the code better." | "comprehension-task accuracy rose from X to Y (effect size ...) in the study" |

## Threats-to-validity discipline

```text
[Construct]   does the metric measure the maintenance outcome you claim? (e.g. churn as a proxy for effort)
[Internal]    could something other than your technique explain it? (confounds in change history, tuning)
[External]    to which systems/languages/domains/histories does the finding generalize?
[Conclusion]  are the statistics appropriate; survivorship handled; multiple comparisons corrected?
-> for each that bites: state it, then state the mitigation, next to the affected result
```

## Vignette: compressing a mining study into 10 pages

A draft with three RQs, nine figures, and a sprawling background on version-control internals: keep
all three RQ answers, the two figures that carry the headline evolution findings, and a threats
subsection per RQ; move the full per-project breakdown, the mining pipeline diagram, and secondary
plots to the artifact with explicit forward references; cut background to what the argument needs.
The test of a good cut: a reviewer should be able to answer "what did each RQ find about how this
software evolves, and what threatens it?" from the 10 pages alone.

## Output format

```text
[Writing diagnosis] clear / under-motivated / over-claimed / evidence-mismatched / over-scoped
[First-page fix] <new framing leading with the maintenance/evolution contribution>
[RQ audit] <RQ -> metric -> where answered -> proportional? yes/no>
[Threats fix] <threat that bites this history/corpus -> mitigation to add, placed by the result>
[Anonymity edits] <tool names / self-citations / own-system subject / links to rewrite>
```
