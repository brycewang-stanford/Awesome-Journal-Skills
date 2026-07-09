---
name: fse-writing-style
description: Use when revising an ESEC/FSE paper for a practitioner-grounded software-engineering contribution on the first page, research-question contracts, a threats-to-validity section that argues rather than recites, evidence proportional to the claim, double-anonymous wording, and disciplined use of the ACM-template page budget.
---

# FSE Writing Style

Use this when revising the main paper. FSE papers are PACMSE journal articles read by SE
empiricists, so they need a **software-engineering contribution stated in the first page** and
evidence a reviewer trusts. The failure this skill prevents is a technically fine paper that reads
like a systems demo or an ML result with an SE title glued on.

## Revision rules

- **Lead with the SE contribution:** the problem a practitioner recognizes, why the current state
  is inadequate, the contribution (technique and/or finding), the evidence, and what changes for
  software engineering.
- **State research questions as contracts.** Each RQ should name what is measured and how it will
  be judged; every RQ must be answered explicitly in the results, and no result should exist
  without an RQ it serves.
- **Pair every claim with proportional evidence** — real subjects, a fair baseline, a statistic
  with an effect size, or a qualitative code with agreement — not adjectives.
- **Argue threats to validity; do not recite them.** Name the construct, internal, external, and
  conclusion threats that actually bite *this* study, and say what you did to bound each. A
  boilerplate threats paragraph is a tell that the author has not stressed their own claims.
- **Respect the page budget as a design constraint,** not a formatting afterthought — the ACM
  template is generous but finite, and a study that only fits by shrinking threats or method is
  over-scoped.
- **Maintain heavy double-anonymity** in self-citations, tool names, acknowledgements, funding,
  and the data-availability wording.

## Empirical-SE paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Problem, inadequacy, contribution, evidence preview, SE payoff — first page | Leads with a technology trend, not a problem |
| Background/Motivation | Why a practitioner or the field needs this now | Motivation by assertion, no grounding |
| Approach / Study design | The technique or the RQs + protocol, reproducibly | Method described too thinly to re-run |
| Evaluation | Each RQ answered with proportional evidence | Metrics that proxy for the claim rather than test it |
| Threats to validity | The threats that bite, each bounded | Generic list untethered from this study |
| Related work | Delta-first positioning against SE literature | Catalog of citations with no contrast |

## Sentence-level rewrites

| Draft pattern | FSE-safe rewrite |
|---|---|
| "Our tool significantly improves..." | "detects X% more defects (95% CI ...) than <baseline> on <N real projects>" |
| "We evaluate on a large dataset." | "We evaluate on <N> projects sampled by <criterion>, listed in the artifact" |
| "Results show our approach works well." | "RQ2: developers acted on <fraction> of comments (effect size ...); threats in §5.2" |
| "State-of-the-art performance." | Claim scoped to the subjects, metrics, and regime actually tested |
| "The LLM understands the code." | "the model's output matched <criterion> in <fraction> of cases" |

## Threats-to-validity discipline

```text
[Construct]   does the metric measure the SE outcome you claim? (e.g. proxy for causation)
[Internal]    could something other than your technique explain the effect? (confounds, tuning)
[External]    to which projects/languages/teams does the finding generalize?
[Conclusion]  are the statistics appropriate; multiple comparisons corrected; variance reported?
-> for each that bites: state it, then state the mitigation, next to the affected result
```

## Vignette: compressing a three-RQ study

A draft with three RQs, nine figures, and a sprawling background: keep all three RQ answers, the
two figures that carry the headline findings, and a threats subsection per RQ; move secondary plots
and full protocol tables to the artifact with explicit forward references; cut background to what
the argument needs. The test of a good cut: a reviewer should be able to answer "what did each RQ
find, and what threatens it?" from the body alone.

## Output format

```text
[Writing diagnosis] clear / under-motivated / over-claimed / evidence-mismatched / over-scoped
[First-page fix] <new framing leading with the SE contribution>
[RQ audit] <RQ -> metric -> where answered -> proportional? yes/no>
[Threats fix] <threat that bites -> mitigation to add, placed by the result>
[Anonymity edits] <tool names / self-citations / links to rewrite>
```
