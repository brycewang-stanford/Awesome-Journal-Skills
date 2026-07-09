---
name: percom-writing-style
description: Use when revising an IEEE PerCom paper for a pervasive-computing contribution on the first page, cross-subject claims stated precisely, a limitations section that argues rather than recites, evidence proportional to the claim, double-blind wording, and disciplined use of the tight IEEEtran 9-page budget.
---

# PerCom Writing Style

Use this when revising the main paper. PerCom papers are IEEE Xplore proceedings read by ubicomp
reviewers, so they need a **pervasive-computing contribution stated in the first page** and
evidence a reviewer trusts on **people they did not train on**. The failure this skill prevents is
a technically fine paper that reads like an ML result with a wearable title glued on, or a systems
demo with no human at its center.

## Revision rules

- **Lead with the ubicomp contribution:** the problem a real user or deployment faces, why current
  sensing is inadequate, the contribution (system and/or finding), the evidence, and what changes
  for pervasive computing.
- **State claims at the right granularity.** A recognition claim must say **cross-subject or
  within-subject**, on what population, with which metric. "97% accuracy" without a split or a class
  balance is a red flag to a PerCom reviewer, not a headline.
- **Pair every claim with proportional evidence** — real subjects, a fair baseline, F1 with
  confidence intervals on realistic class balance, deployment realism — not adjectives.
- **Argue limitations; do not recite them.** Name the external, construct, and generalization
  limits that actually bite *this* study (subject diversity, ground-truth quality, lab vs.
  free-living), and say what you did to bound each. A boilerplate limitations paragraph tells a
  reviewer you have not stressed your own claims.
- **Respect the 9-page budget as a design constraint,** not a formatting afterthought — IEEEtran
  two-column is tight, and a study that only fits by shrinking the evaluation or limitations is
  over-scoped. Recover space editorially, never by touching the template.
- **Maintain double-blindness** in self-citations (third person), testbed and system names, dataset
  links, acknowledgements, and funding.

## Ubicomp paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Problem, inadequacy, contribution, evidence preview, ubicomp payoff — first page | Leads with a technology trend, not a real-use problem |
| Background/Motivation | Why a user or deployment needs this now | Motivation by assertion, no grounding in practice |
| System / Study design | The technique or the study + sensing protocol, reproducibly | Method or sensor setup described too thinly to re-run |
| Evaluation | Each claim answered with **cross-subject**, proportional evidence | Within-subject or pooled-accuracy metrics that flatter the result |
| Limitations | The limits that bite, each bounded | Generic list untethered from this study's subjects/sensors |
| Related work | Delta-first positioning against the ubicomp literature | Catalog of citations with no contrast |

## Sentence-level rewrites

| Draft pattern | PerCom-safe rewrite |
|---|---|
| "Our system achieves 97% accuracy." | "leave-one-subject-out F1 of 0.xx (95% CI ...) on <N> participants" |
| "We evaluate on a large dataset." | "We evaluate on <N> participants over <duration> of free-living data, released as a dataset" |
| "Results show our approach works well." | "cross-subject F1 improves by X over <baseline>; per-subject variance in Fig. 3" |
| "State-of-the-art performance." | Claim scoped to the subjects, sensors, and setting actually tested |
| "The model recognizes activities." | "the recognizer reaches F1 0.xx on held-out subjects for <activity set>" |

## Cross-subject and metric discipline

```text
[Split]      state within-subject vs. leave-one-subject-out (or session-out); PerCom default is cross-subject
[Balance]    report class balance; on imbalanced activities use F1 (macro + per-class), not raw accuracy
[Event vs frame] say whether metrics are frame-level or event-level; they can differ sharply
[Realism]    lab vs. free-living; scripted vs. spontaneous behavior -- name which you tested
-> for each: state the choice next to the number so a reviewer is not left guessing
```

## Vignette: compressing an over-length study into 9 pages

A draft with three activity classes, nine figures, and a sprawling background: keep the
cross-subject headline result, the two figures that carry it, a per-class F1 table, and a
limitations subsection tied to subject diversity and ground truth; move per-subject breakdowns and
extra ablations to the dataset with explicit forward references; cut background to what the argument
needs. The test of a good cut: a reviewer should be able to answer "does it work on a new person,
and what threatens that?" from the body alone.

## Output format

```text
[Writing diagnosis] clear / under-motivated / over-claimed / within-subject-only / over-scoped
[First-page fix] <new framing leading with the pervasive-computing contribution>
[Claim audit] <claim -> split (LOSO?) -> metric (F1?) -> where answered -> proportional? yes/no>
[Limitations fix] <limit that bites -> bounding to add, placed by the result>
[Anonymity edits] <system names / self-citations / dataset links to rewrite>
```
