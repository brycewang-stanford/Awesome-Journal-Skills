> **Illustrative teaching example.** The paper, robot, tasks, and every number below are
> **fictional**, invented only to demonstrate how an RSS first page differs from a demo
> write-up. No real-paper facts or venue policies are invented. Companion skills:
> [`rss-writing-style`](../../skills/rss-writing-style/SKILL.md),
> [`rss-experiments`](../../skills/rss-experiments/SKILL.md), and
> [`rss-topic-selection`](../../skills/rss-topic-selection/SKILL.md).

# Worked Example: From System Demo to RSS Science (before → after)

RSS asks a question most robotics venues do not press as hard: **what did we learn about
robotics, beyond the fact that this particular system works?** A submission whose honest
summary is "we built it and it succeeded" is fighting the venue's identity. The rewrite
below shows the same fictional project told twice — first as a demo report, then as a
scientific claim with a falsifiable structure.

**Fictional paper:** *"Contact Scheduling Is the Bottleneck: Decoupling When to Touch
from How to Move in Bimanual Cloth Manipulation."* Fictional finding: a planner that
chooses *contact timing* separately from arm motion doubles task reliability, and the
gain persists across grippers and cloth types — evidence that timing, not trajectory
quality, limits current systems.

---

## Before (a systems demo wearing a paper's clothes)

> **Abstract.** We present BiFold, a novel end-to-end system for bimanual cloth folding.
> BiFold integrates a state-of-the-art perception module, a learned grasp selector, and
> a whole-body motion planner on a dual-arm platform. In extensive experiments, BiFold
> successfully folds a variety of garments and outperforms baseline systems. Videos of
> our robot are available on our project page.
>
> **Introduction.** Cloth manipulation is a long-standing challenge in robotics. Recent
> advances in deep learning have enabled impressive progress. In this work we combine
> several components into a unified pipeline and demonstrate robust folding. Our system
> achieves a high success rate. We believe our results represent a step toward general
> household robots.

**Why an RSS reader bounces off this:**

- **No scientific claim.** The contribution is the *existence of a pipeline*. Nothing is
  hypothesized, isolated, or explained — the single most common RSS mismatch.
- **"Extensive experiments" is unaccountable.** No trial counts, no task distribution,
  no failure story; "a variety of garments" and "high success rate" cannot be audited.
- **The video does the arguing.** Links belong in the camera-ready at RSS 2026, not in
  the anonymous submission — and evidence reviewers can't inspect in the PDF is
  evidence they discount.
- **Superlatives without a comparator.** "State-of-the-art," "novel," and "impressive"
  are claims about the literature; none is tied to a named alternative.
- **The generality leap is unearned.** One platform, one lab, one wardrobe → "general
  household robots."

---

## After (the RSS arc: claim → mechanism → falsifiable evidence → scope)

> **Abstract.** Bimanual cloth manipulation systems typically plan *where* to grasp and
> *how* to move jointly. We give evidence that this coupling is the wrong bottleneck to
> optimize: across 600 folding trials, most failures trace to *when* contact is made and
> released, not to trajectory quality. We propose contact-schedule decoupling (CSD),
> which plans a discrete touch/release schedule first and fits arm motion to it. On a
> dual-arm platform, CSD raises task success from 41% to 83% (95% CIs over 100 trials
> per condition) on a five-garment distribution, and the improvement persists under a
> gripper swap and two unseen cloth stiffnesses. Ablating only the schedule while
> keeping motions fixed recovers most of the gain, supporting the bottleneck claim.
> Failure modes, protocol, and all trials are reported; code and logs accompany the
> supplement.
>
> **Introduction, ¶1 — the claim.** We argue that in bimanual cloth folding, *contact
> timing* — not motion quality — is the dominant failure source, and that planning it
> as a first-class discrete variable yields large, transferable reliability gains.
>
> **¶2 — why this is a scientific question.** Prior systems entangle timing with
> trajectory optimization, so their failures cannot be attributed: was the grasp early,
> or the path poor? We instrument failures into a four-way attribution (timing, path,
> perception, slip) and find timing dominates in our 600-trial corpus — a measurement
> any lab can repeat with the released protocol.
>
> **¶3 — mechanism.** CSD searches the small discrete space of touch/release orderings
> against a cloth-state predictor, then solves for motion under the fixed schedule.
> This inverts the usual hierarchy and is cheap: schedules are enumerable where
> trajectories are not.
>
> **¶4 — evidence sized to the claim.** Because the claim is *causal* (timing is the
> bottleneck) and *general* (not an artifact of one gripper), the evaluation includes
> a schedule-only ablation, a hardware swap, and unseen materials — each with per-
> condition trial counts, confidence intervals, and a failure taxonomy. What the claim
> does not cover — deformable objects beyond cloth, mobile bases — is stated as scope,
> not smuggled in.

---

## What changed, mapped to the skills

| Demo habit | RSS repair | Skill |
| --- | --- | --- |
| Pipeline as contribution | One falsifiable claim about robotics | `rss-topic-selection` |
| "Extensive experiments" | 600 trials, per-condition counts, CIs | `rss-experiments` |
| Video as argument | PDF self-contained; media as supplement | `rss-supplementary` |
| "Outperforms baselines" | Named ablation isolating the mechanism | `rss-experiments` |
| "Step toward general robots" | Explicit scope sentence | `rss-writing-style` |
| Project-page link in submission | Links deferred to camera-ready | `rss-submission` |

> Next: study real first pages that execute this arc in
> [`../exemplars/library.md`](../exemplars/library.md) — all free to read at
> roboticsproceedings.org — and confirm current policy in
> [`../official-source-map.md`](../official-source-map.md).
