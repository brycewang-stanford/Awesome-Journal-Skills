> **Illustrative teaching example.** The paper, method, datasets, and every number below are
> **fictional** and exist only to demonstrate NeurIPS house style. No real-paper facts, no NeurIPS
> policy, and no benchmark results are asserted. Corresponding skills:
> [`neurips-writing-style`](../../skills/neurips-writing-style/SKILL.md),
> [`neurips-topic-selection`](../../skills/neurips-topic-selection/SKILL.md),
> [`neurips-experiments`](../../skills/neurips-experiments/SKILL.md), and
> [`neurips-reproducibility`](../../skills/neurips-reproducibility/SKILL.md).

# Worked Example: A NeurIPS-Style Abstract + Introduction (before → after)

This demonstrates the **NeurIPS introduction pattern** from `neurips-writing-style`:
**name the problem and why current ML practice cannot solve it → identify the specific gap (method,
theory, data, evaluation, system, or understanding) → state the contribution type and why it fits
NeurIPS → preview the evidence → bound the claim with limitations** — under the style rules that every
headline result is tied to a baseline / dataset / theorem / ablation, claims are falsifiable rather than
adjectival, "we show" is used only when the paper demonstrates the claim, and limitations are stated
rather than buried.

**Illustrative paper (fictional):** *"Gradient-Free Routing: A Mixture-of-Experts Layer Trained by
Local Bandit Feedback."* Fictional method (a router trained without backpropagation through the gating
decision), fictional datasets, fictional numbers — used only to show the arc.

---

## Before (leaderboard-first draft — buries the science)

> Mixture-of-Experts (MoE) models have become very popular and have achieved impressive,
> state-of-the-art results on many tasks. In this paper we propose a novel and powerful new MoE routing
> method that significantly outperforms existing approaches. Our method is simple, effective, and
> general. We run extensive experiments on several benchmarks and show that our approach achieves the
> best accuracy. We also believe our method will be useful for many future applications. The results
> demonstrate the effectiveness of the proposed approach.

**What's wrong (against `neurips-writing-style`, `neurips-topic-selection`, `neurips-experiments`):**

- **No problem and no gap.** It never says *why current MoE practice fails*, so a reviewer outside the
  authors' exact subfield cannot locate the contribution (`neurips-writing-style`: make the contribution
  legible to reviewers outside the subfield; name the problem and the specific gap).
- **Adjectives instead of falsifiable claims** ("novel," "powerful," "significantly outperforms,"
  "best accuracy") with **no baseline, dataset, or metric named** (`neurips-writing-style`: prefer
  falsifiable claims; tie every headline result to a baseline/dataset/theorem/ablation).
- **"State-of-the-art" with no comparison set, metric, or time boundary** — a named anti-pattern.
- **Benchmark wins with no mechanism or explanation** — exactly the submission risk flagged in
  `neurips-experiments` and `neurips-submission` ("strong benchmark wins but weak scientific
  explanation is vulnerable").
- **No contribution type** (General / Theory / Use-Inspired / Concept & Feasibility / Negative Results),
  so reviewer expectations are unset (`neurips-topic-selection`).
- **Limitations buried entirely** — NeurIPS reviewers are instructed to reward honest limitation
  reporting (`neurips-writing-style`).

---

## After (NeurIPS arc — problem → gap → contribution type → evidence → limitation)

### Abstract

> Standard Mixture-of-Experts layers route tokens by backpropagating through a softmax gate, which
> couples the router to the experts and makes the routing distribution unstable under distribution
> shift. *(problem + why current practice is limited.)* We ask whether a router can instead be trained
> from **local bandit feedback** — each expert's downstream loss as a reward — so the gate never needs a
> differentiable path through expert selection. *(specific gap: a method/optimization question.)* We
> introduce **Gradient-Free Routing (GFR)**, a MoE gating layer trained with a per-token bandit
> objective, and give a regret bound showing the router converges to the loss-minimizing assignment
> under a bounded-drift assumption. *(contribution type: General method + Theory.)* On three fictional
> sequence benchmarks GFR matches a tuned top-2 softmax-gating baseline in accuracy while reducing
> router-induced loss variance under simulated distribution shift; an ablation isolates the bandit
> objective as the source of the stability gain. *(evidence anchored to baseline + ablation, no
> "SOTA".)* GFR assumes bounded reward drift and is evaluated only at small scale; we do not claim gains
> at frontier model sizes. *(limitation, stated up front.)* We release code, configs, seeds, and the
> checklist to support reproduction. *(reproducibility, matching the checklist answer.)*

### Introduction (first paragraphs)

> Mixture-of-Experts layers scale capacity by routing each token to a few experts, but the router is
> trained by backpropagating through a softmax over expert scores. This couples the gating decision to
> the experts being trained and, in our fictional setting, makes the routing distribution drift when the
> input distribution shifts at test time. *(Step 1 — name the problem and why current ML practice cannot
> solve it cleanly.)*
>
> The specific gap is whether the router needs a differentiable path through expert selection at all.
> Expert assignment is a discrete decision with an observable downstream loss — the structure of a
> contextual bandit, not of a quantity that must be differentiated. No prior MoE method, to our fictional
> knowledge, trains the gate purely from this bandit feedback. *(Step 2 — the specific gap in method /
> understanding.)*
>
> We contribute **Gradient-Free Routing (GFR)**, a general MoE gating method, together with a theory
> result: under a bounded-drift assumption we prove an O(√T) regret bound for the router relative to the
> oracle loss-minimizing assignment. This is a **General + Theory** contribution, which fits NeurIPS
> because it changes how the routing sub-problem is *posed*, not just its leaderboard number. *(Step 3 —
> contribution type and why it fits NeurIPS; ties to `neurips-topic-selection`.)*
>
> We preview three pieces of evidence: (i) on three fictional benchmarks GFR matches a tuned top-2
> softmax-gating baseline within reported error bars over five seeds; (ii) under simulated distribution
> shift GFR lowers router-induced loss variance relative to that baseline; and (iii) an ablation that
> removes the bandit objective recovers the baseline's instability, isolating the mechanism rather than a
> confound. *(Step 4 — preview the evidence, each anchored; ties to `neurips-experiments`.)*
>
> We bound the claim. The regret guarantee relies on bounded reward drift, which can fail under abrupt
> shift; all experiments are small-scale, and we make no claim about frontier-scale models or
> wall-clock training cost. *(Step 5 — limitations and failure modes, not buried; ties to
> `neurips-reproducibility`.)*

---

## Why the "after" meets the NeurIPS bar

Mapped to the skill checklists:

- **Problem → gap → contribution type → evidence → limitation**, in order — the exact five-step
  introduction pattern in `neurips-writing-style`.
- **Every headline claim is anchored** to a named baseline (tuned top-2 softmax gating), a theorem
  (the O(√T) regret bound), and an ablation that isolates the mechanism — satisfying both
  `neurips-writing-style` ("tie every headline result to a baseline, dataset, theorem, ablation") and
  the `neurips-experiments` audit (strong baseline, mechanism-isolating ablation, robustness under
  shift, multiple seeds).
- **No "state of the art."** Comparisons name the baseline, metric, and setting; claims are falsifiable.
- **Contribution type is explicit** (General + Theory), setting reviewer expectations as
  `neurips-topic-selection` requires — and the "why NeurIPS" sentence argues it reframes the routing
  sub-problem, not that it tops a leaderboard.
- **Limitations are stated in the abstract and the intro** (bounded-drift assumption, small scale, no
  frontier-scale or wall-clock claim) — the honest-limitation reporting `neurips-writing-style` says
  reviewers reward.
- **Reproducibility is promised concretely** (code, configs, seeds, checklist) and is consistent with
  what `neurips-reproducibility` calls a matching checklist answer — multiple seeds and error bars are
  named in the evidence preview, not left implicit.

> The rewrite-output template from `neurips-writing-style` applied to one claim:
>
> ```text
> [Claim before]            We propose a powerful new MoE router that achieves SOTA accuracy.
> [Claim after]             GFR matches a tuned top-2 softmax-gating baseline in accuracy (5 seeds)
>                           while reducing router-induced loss variance under simulated shift.
> [Evidence anchor]         baseline table + distribution-shift experiment + bandit-objective ablation
> [Limitation sentence]     Guarantee assumes bounded reward drift; evaluated only at small scale.
> [Reviewer concern reduced] significance + reproducibility (mechanism shown, claim not over-broad)
> ```

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified NeurIPS/NIPS
> papers** whose abstracts execute a version of this arc, and
> [`../official-source-map.md`](../official-source-map.md) for the verified NeurIPS submission, checklist,
> and reproducibility-track facts referenced above.
