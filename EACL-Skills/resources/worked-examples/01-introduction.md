> **Illustrative teaching example.** The paper, task, system, and every number below are **fictional** and
> exist only to demonstrate EACL house style. No real-paper facts, datasets, or results are stated, and no
> policy is invented. Corresponding skills:
> [`eacl-writing-style`](../../skills/eacl-writing-style/SKILL.md),
> [`eacl-topic-selection`](../../skills/eacl-topic-selection/SKILL.md), and
> [`eacl-experiments`](../../skills/eacl-experiments/SKILL.md).

# Worked Example: An EACL-Style Abstract + Introduction (before → after)

This demonstrates the **EACL first-page arc** from `eacl-writing-style`:
**task → why current methods fall short → what we do → measured result → honest scope** — with the *ACL
conventions that the contribution is legible on the first page, that claims are quantified rather than
asserted, and that the paper's limits are named rather than hidden (the mandatory **Limitations** section
sits at the end, outside the page budget).

The framing also reflects `eacl-topic-selection`: EACL is strongest for a **well-scoped NLP question
answered with careful, often multilingual evidence** — here, an evaluation-integrity finding for
lower-resourced languages, not a leaderboard win (which might route to a systems-heavy track elsewhere).

**Illustrative paper (fictional):** *"When the Test Set Speaks Your Model's Language: Measuring
Translationese Leakage in Multilingual QA Benchmarks."* Fictional finding: machine-translated evaluation
sets inflate cross-lingual scores for lower-resourced languages.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Multilingual NLP has made great progress in recent years. In this paper we study question
> answering across many languages, which is an important and challenging problem. We propose a new approach
> and evaluate it on several multilingual benchmarks, achieving strong results and outperforming prior
> systems in most languages. Our findings have important implications for the community.
>
> **Introduction.** Question answering has been widely studied. With the rise of large language models,
> multilingual QA has become increasingly popular. Many datasets exist, and many models have been proposed.
> In this paper, we investigate multilingual QA and present new results. We evaluate on standard benchmarks
> and show that our method works well across languages. Section 2 reviews related work, Section 3 describes
> our approach, Section 4 presents experiments, and Section 5 concludes.

**What's wrong (against `eacl-writing-style` / `eacl-topic-selection` / `eacl-experiments`):**

- **No task or finding on the first page** — leads with "great progress," not with the specific question
  or the result. EACL reviewers want the contribution in the first breath.
- **Overclaims** ("strong results," "outperforming in most languages," "works well") with **no numbers,
  baselines, or variance** — the exact pattern `eacl-experiments` flags.
- **No claim → evidence pairing**: nothing ties a stated result to a table, a test, or a controlled
  comparison.
- **Scope hidden** — no mention of *which* languages, *how* the test sets were built, or where the method
  fails; the Limitations section is treated as an afterthought rather than shaping the claim.
- **Vague significance** ("important implications") standing in for a concrete takeaway.
- **Over-signposted roadmap** substituting for an argument.

---

## After (EACL arc — task → gap → what we measure → result → honest scope)

> **Abstract.** Cross-lingual question-answering benchmarks for lower-resourced languages are often built
> by **machine-translating an English test set**, and reported cross-lingual gains may reflect this
> **translationese** rather than genuine understanding. We introduce a controlled protocol that pairs each
> machine-translated evaluation item with a **human-authored counterpart** in the same language, across six
> lower-resourced European and Mediterranean languages. Measuring five multilingual models on both, we find
> that scores on machine-translated items are **systematically higher** than on human-authored items at
> matched difficulty, and that the gap **grows as language resources shrink**. We report exact-match and F1
> with 95% confidence intervals over five seeds, release both evaluation halves, and show that a simple
> translationese filter narrows but does not close the gap. *(task → gap → protocol → measured result →
> honest residual — all on the first page.)*
>
> **Introduction.** *(¶1 — task + finding, first breath.)* A multilingual QA benchmark is only trustworthy
> if a high score means the model understood the question in that language — not that it recognised
> **translated English phrasing**. We show that for lower-resourced languages, where test sets are usually
> machine-translated, this distinction is not academic: models score measurably higher on translated items
> than on human-authored items of matched difficulty, so published cross-lingual gains are **partly an
> artifact of how the test set was made**.
>
> *(¶2 — gap: why current practice is insufficient, each reason specific.)* Existing multilingual QA
> evaluations are insufficient for nameable reasons. Translate-test and translate-train pipelines
> **import English syntactic patterns** that models trained on parallel data recognise cheaply. Aggregate
> cross-lingual scores **average over languages of very different resource levels**, hiding where the
> problem concentrates. And prior audits report overall accuracy without a **human-authored control**, so
> a translationese effect and a genuine-competence effect are **confounded**. *(each prior line gets a
> specific failure, not a generic "prior work is limited.")*
>
> *(¶3 — what we do + the explicit design choice.)* We build a **paired evaluation set**: for six
> lower-resourced languages, every machine-translated item has a human-authored sibling calibrated to the
> same answer type and difficulty. The **only** structural assumption is that the two halves are matched on
> difficulty, which we validate with human annotators; we make no claim about languages outside this set.
>
> *(¶4 — result + evidence, each claim paired.)* Across five multilingual models, machine-translated items
> yield higher exact-match and F1 than human-authored items (Table 1), the gap **correlates with a
> resource-availability index** (Fig. 1), and a translationese classifier used as a filter reduces the gap
> by a measured but partial amount (Table 2). **All numbers carry 95% confidence intervals over five
> seeds**, and the annotation protocol, difficulty-matching procedure, and inter-annotator agreement are in
> the appendix. *(every claim → table, figure, or reproducibility location.)*
>
> *(¶5 — why it matters + honest scope + brief roadmap.)* The contribution is a **measurement and a
> protocol**: cross-lingual QA scores for lower-resourced languages should be read against a human-authored
> control, and we provide one. We are explicit in the **Limitations** section that six languages cannot
> speak for all lower-resourced settings and that our difficulty matching is imperfect. Section 2 details
> the paired-set construction, Section 3 the models and metrics, and Section 4 the results.
> *(brief roadmap, scope named, not buried.)*

---

## Why the "after" meets the EACL bar

Mapped to the skill checklists:

- **Contribution on the first page** — the abstract and ¶1 state the task, the gap, the protocol, and the
  finding before any system detail (`eacl-writing-style`: "put the task and the result in the first
  page").
- **Claims are measured, not asserted** — "systematically higher," "gap grows as resources shrink," each
  tied to a table or figure with **confidence intervals over five seeds** (`eacl-experiments`: significance
  and variance floors; avoid overclaiming).
- **Every claim paired with evidence** — translationese gap → Table 1; resource correlation → Fig. 1;
  filter effect → Table 2; protocol → appendix.
- **Scope named honestly** — six languages, imperfect difficulty matching, and a *residual* gap the filter
  does not close, all surfaced rather than hidden; the **Limitations** section is planned into the claim,
  not bolted on (`eacl-submission`: Limitations is mandatory and read).
- **Contamination / evaluation-integrity framing** — the paper measures a benchmark artifact and re-reads
  results through it, the discipline in `eacl-reproducibility`.
- **Right venue** — a well-scoped multilingual evaluation finding with careful controls is a strong EACL
  fit rather than a systems-leaderboard submission (`eacl-topic-selection`).
- **8-page discipline** — the paired-set construction and full protocol live in the appendix while the
  body carries the argument (`eacl-writing-style`: content pages carry the claim, appendix carries the
  detail).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, Anthology-verified EACL
> papers** whose first pages execute this arc, and [`../official-source-map.md`](../official-source-map.md)
> for EACL-specific submission and commitment policy.
