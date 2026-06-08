> **Illustrative teaching example.** The paper, method, and every number below are **fictional** and
> exist only to demonstrate ICML house style. No real-paper facts are stated, and no policy claim is
> invented — policy lives in [`../official-source-map.md`](../official-source-map.md). Corresponding
> skills: [`icml-writing-style`](../../skills/icml-writing-style/SKILL.md),
> [`icml-topic-selection`](../../skills/icml-topic-selection/SKILL.md), and
> [`icml-experiments`](../../skills/icml-experiments/SKILL.md).

# Worked Example: An ICML-Style Abstract + Introduction (before → after)

This demonstrates the **ICML introduction shape** from `icml-writing-style`:
**define the ML problem precisely → state what prior methods/theory/evaluations fail to cover →
give the contribution in a reviewer-evaluable form (method, theorem, benchmark, empirical finding,
system, or analysis) → preview the evidence (proof, ablation, baseline, dataset, artifact) → bound
the claim and point to appendices only for support.** Critical evidence stays in the main 8-page
body; claims are written so they map to **soundness, originality, significance, and clarity**, with a
factual, proportionate impact statement.

**Illustrative paper (fictional):** *"Gradient-Aligned Dropout: A Drop-in Regularizer that Provably
Reduces Variance in Deep Net Training."* Fictional method: a dropout variant that masks units in the
direction of agreement across a minibatch's per-example gradients.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Deep learning has achieved great success in many domains. Regularization is an
> important topic. In this paper we propose a new regularization method based on dropout and
> gradients. We run experiments on several datasets and show that our method works well and often
> outperforms baselines. We hope this method will be useful to the community.
>
> **Introduction.** Neural networks are widely used and have been studied extensively. Dropout is a
> popular regularizer, and many variants exist. However, there are still problems. We propose
> Gradient-Aligned Dropout, which combines dropout with gradient information. We evaluate it and find
> it is effective. Section 2 reviews related work, Section 3 describes the method, Section 4 presents
> experiments, and Section 5 concludes. Additional results are in the appendix.

**What's wrong (against `icml-writing-style` / `icml-topic-selection` / `icml-experiments`):**

- **No precise ML problem.** "Regularization is an important topic" is throat-clearing, not a
  problem statement a reviewer can score for **significance**.
- **Contribution not in a reviewer-evaluable form.** "Works well," "often outperforms" — there is no
  named claim type (method? theorem? empirical finding?) and nothing maps to **soundness** or
  **originality**.
- **No gap.** It never says what prior dropout variants *fail* to cover, so **originality** is
  unscorable.
- **No previewed evidence.** No proof, ablation, baseline, or artifact is named, and the decisive
  evidence is deferred to "the appendix" — violating the rule that critical evidence lives in the
  main body.
- **Unbounded claim + missing impact framing.** "Outperforms baselines" with no conditions; no
  factual, proportionate impact statement.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (ICML shape — precise problem → gap → evaluable contribution → previewed evidence → bounded claim)

> **Abstract.** Dropout regularizes deep networks by masking units at random, but the mask ignores
> *how* the masked units affect the training signal, which can inflate minibatch gradient variance
> late in training. We introduce **Gradient-Aligned Dropout (GAD)**, a drop-in replacement that masks
> units in the direction along which per-example gradients in a minibatch agree. We prove that, under
> a bounded-curvature assumption, GAD yields a strictly smaller gradient-variance bound than standard
> dropout at the same expected mask rate (Thm. 1). Empirically, on three image and two text
> benchmarks with matched compute and five seeds, GAD lowers test error over standard dropout by
> 0.8–1.6 points and matches or beats four tuned regularizer baselines, with an ablation isolating
> the alignment term as the source of the gain. Code and exact commands are in the supplement.
> *(problem + gap + contribution type (method **and** theorem) + previewed evidence + reproducibility,
> in one paragraph.)*
>
> **Introduction.** Dropout masks hidden units independently of their effect on the loss, so the
> retained subnetwork's gradient can disagree sharply across examples in a minibatch; this variance
> is harmless early but slows convergence late in training. *(the ML problem, stated precisely.)*
> Existing dropout variants reweight or schedule the mask rate, but none align the mask with the
> minibatch gradient geometry, so they leave this specific variance source unaddressed. *(what prior
> methods fail to cover — the originality gap, relative to a named class of prior work.)*
>
> We make a **method** and a **theory** contribution that a reviewer can check directly. (i) We define
> **Gradient-Aligned Dropout**, which masks units in the subspace where per-example gradients agree,
> adding one hyperparameter and no extra backward pass. (ii) We prove (Thm. 1) that under bounded
> curvature GAD has a strictly smaller per-step gradient-variance bound than standard dropout at equal
> expected mask rate. *(contribution in reviewer-evaluable form — soundness via a stated theorem,
> originality via the named delta.)*
>
> We support the claim with evidence in the main body, not only the appendix: a controlled comparison
> against standard dropout and four tuned baselines on five benchmarks with matched compute and
> five-seed variance, plus an ablation that removes the alignment term and recovers ordinary dropout,
> isolating the mechanism. *(previewed evidence — baselines, variance, ablation, compute fairness, per
> `icml-experiments`.)*
>
> We bound the claim: the variance guarantee assumes bounded curvature and equal expected mask rate,
> and the empirical gains are measured at fixed compute; we do not claim improvements under heavy
> hyperparameter retuning of the baselines, which the appendix examines. *(claim bounded; appendix is
> support, not the main idea.)* GAD is a drop-in layer, so the **impact** is a modest, broadly
> applicable training improvement rather than a new capability; we state this proportionately and note
> no new data or human subjects are involved. *(factual, proportionate impact framing.)*

---

## Why the "after" meets the ICML bar

Mapped to the skill checklists:

- **Precise ML problem first** — the variance-inflation mechanism is stated concretely, not as "an
  important topic" (`icml-writing-style`: define the ML problem precisely).
- **Gap that establishes originality** — prior dropout variants "reweight or schedule the mask rate"
  but "none align the mask with the minibatch gradient geometry," a named delta a reviewer can score
  for **originality** (`icml-related-work`'s delta-paragraph posture, surfaced in the intro).
- **Contribution in a reviewer-evaluable form** — explicitly typed as **method + theorem**, the two
  forms `icml-topic-selection` lists, so **soundness** and **significance** are checkable.
- **Evidence previewed and kept in the main body** — baselines, five-seed variance, matched compute,
  and an ablation isolating the mechanism, exactly the `icml-experiments` audit items; the decisive
  table is not exiled to the appendix.
- **Claim bounded; appendix is support** — assumptions (bounded curvature, equal mask rate, fixed
  compute) are named, satisfying the rule that appendices support rather than carry the main idea.
- **Factual, proportionate impact statement** — a "drop-in, modest, broadly applicable" framing, not
  an overclaim, consistent with `icml-writing-style` and `icml-reproducibility`.
- **Reproducibility previewed** — "code and exact commands are in the supplement" matches the
  `icml-reproducibility` reviewer-facing sentence (anonymized package, exact commands).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified ICML
> papers** whose abstracts execute this shape, and
> [`../official-source-map.md`](../official-source-map.md) for the authoritative ICML policy facts
> (8-page body, anonymity, impact statement, supplement rules).
