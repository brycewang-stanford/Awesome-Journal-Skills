> **Illustrative teaching example.** The paper, method, datasets, and every number in
> this file are **invented** to demonstrate UAI first-page craft. No real paper is
> paraphrased and no venue policy is stated here beyond what
> [`../official-source-map.md`](../official-source-map.md) verifies. Companion skills:
> [`uai-writing-style`](../../skills/uai-writing-style/SKILL.md),
> [`uai-topic-selection`](../../skills/uai-topic-selection/SKILL.md),
> [`uai-experiments`](../../skills/uai-experiments/SKILL.md).

# Worked Example: A UAI-Style Abstract + Introduction (before → after)

The exercise: take a first-draft opening for a causal-discovery-flavored paper and
rebuild it to the UAI bar — the probabilistic object named on page 1, the assumption
set labeled and honest, the guarantee stated with its regime, and every claim wired to
a proof or an experiment a reviewer can locate. The venue's four review criteria
(technical correctness, novelty, convincing backing, clarity) are the grading rubric
throughout.

**Fictional paper:** *"Anchor-Regularized Structure Learning under Soft Interventions
with Unknown Targets."* Invented method: a score-based discovery algorithm that uses a
small set of variables with known intervention status ("anchors") to identify causal
structure when most intervention targets are unknown.

---

## Before (a typical first draft)

> **Abstract.** Causal discovery is an important problem with many applications in
> science and industry. Existing methods struggle when interventions are imperfect. We
> propose Anchor-GES, a novel deep-learning-enhanced framework for learning causal
> graphs from mixed observational and interventional data. Extensive experiments show
> that Anchor-GES significantly outperforms state-of-the-art methods on synthetic and
> real datasets.
>
> **Introduction.** Understanding causality is a fundamental goal of science. In recent
> years, many methods have been proposed for causal discovery, including constraint-based,
> score-based, and continuous-optimization approaches. However, these methods often
> assume perfect interventions, which is unrealistic. Inspired by recent advances, we
> develop a new framework that combines score-based search with anchor information. Our
> contributions are threefold: (1) a novel algorithm; (2) theoretical analysis; (3)
> extensive experiments demonstrating superior performance.

**Why this fails the UAI rubric:**

- **No probabilistic object, no regime.** "Learning causal graphs from mixed data"
  never says which graph class, which intervention model, or what "identify" means —
  the deletion-test core is invisible (`uai-topic-selection`).
- **Assumptions hidden.** Nothing about faithfulness, target knowledge, or acyclicity;
  a UAI reviewer's first question ("identified under what?") has no answer on page 1
  (`uai-writing-style`).
- **"Theoretical analysis" as a contribution bullet** — a guarantee with no statement
  is a promise with no content; correctness cannot even be assessed.
- **Uncalibrated superlatives** ("significantly outperforms", "state-of-the-art") with
  no metric, no dispersion, no regime — fails the backing criterion in the abstract
  itself (`uai-experiments`).
- **Marketing vocabulary** ("deep-learning-enhanced framework") signals a different
  venue's genre; at UAI the estimator, not the framework, is the protagonist.

---

## After (rebuilt to the UAI bar)

> **Abstract.** We study structure identification from a mixture of observational data
> and soft interventions whose targets are unknown, except for a small **anchor set**
> of variables with known intervention status. We show that with *k* anchors
> satisfying a coverage condition (Assumption A3), the interventional Markov
> equivalence class is identified up to a strictly finer partition than from
> observational data alone (Theorem 1), and we give a score-based algorithm,
> **Anchor-GES**, whose output converges to this class as sample size grows
> (Theorem 2, under A1–A4). On synthetic ensembles where the true graph is known,
> Anchor-GES reduces structural Hamming distance relative to target-agnostic baselines,
> with the gain growing in anchor coverage exactly as Theorem 1 predicts (Fig. 2; mean
> ± sd over 25 graph draws). A stress study with violated coverage (A3 broken)
> localizes the failure to the uncovered blocks (Fig. 4). Code and graph generators
> are provided.
>
> **Introduction.** *(¶1 — object and regime.)* When interventions are soft and their
> targets unknown, what is identifiable about a causal DAG? We answer for the regime
> where a small anchor set has known intervention status — a setting arising in
> genomics screens where a minority of perturbations are validated. *(¶2 — gap, named
> per method family.)* Constraint-based methods with unknown targets recover only the
> observational equivalence class here; continuous-optimization methods presume known
> targets; unknown-target score methods treat all variables symmetrically and provably
> cannot exploit anchors (Prop. 1). *(¶3 — contribution, assumption-forward.)* Under
> faithfulness (A1), soft-intervention positivity (A2), anchor coverage (A3), and
> finite-degree (A4), we characterize the identified class and attain it
> algorithmically. Each assumption is discussed where stated; A3 is the novel and
> restrictive one, and Section 6 measures what breaks without it. *(¶4 — evidence
> map.)* Theorem 1 is proved in App. B; Theorem 2 in App. C; the exact-truth, stress,
> and real-data studies follow the three-regime design of Section 5, with seeds,
> generators, and diagnostics in the supplement. *(¶5 — scope.)* We claim nothing
> about cyclic models or hard interventions; extensions are outlined in App. F.

---

## What changed, criterion by criterion

| Rubric axis | Before | After |
|---|---|---|
| Correctness (assessable?) | "theoretical analysis" | Named theorems, labeled assumptions A1–A4, proof locations |
| Novelty | "novel framework" | The delta is a *regime* (anchors + unknown targets) plus an impossibility contrast (Prop. 1) |
| Backing | "significantly outperforms" | SHD with dispersion, gains tracking the theorem's prediction, stress study where A3 fails |
| Clarity | roadmap boilerplate | Object → regime → gap → assumptions → evidence map in five paragraphs |

Three transferable moves: (1) the **assumption with a confession** — flagging A3 as the
restrictive one and pointing at the experiment that breaks it disarms the strongest
review objection in advance; (2) the **theory-shaped experiment** — the headline plot
tracks the quantity the theorem says should matter (anchor coverage), converting a
benchmark into a test; (3) the **scope fence** — the final paragraph spends one
sentence disclaiming what is not proved, which is cheap insurance at a venue that
reads claims literally.

> Next: benchmark against the real, metadata-verified UAI papers in
> [`../exemplars/library.md`](../exemplars/library.md), and re-check current submission
> mechanics in [`../official-source-map.md`](../official-source-map.md) before acting.
