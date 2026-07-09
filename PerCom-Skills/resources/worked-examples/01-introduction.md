> **Illustrative teaching example.** The paper, dataset, system, and every number below are
> **fictional** and exist only to demonstrate PerCom house style. No real-paper facts, projects, or
> results are stated, and no policy is invented. Corresponding skills:
> [`percom-writing-style`](../../skills/percom-writing-style/SKILL.md),
> [`percom-topic-selection`](../../skills/percom-topic-selection/SKILL.md), and
> [`percom-experiments`](../../skills/percom-experiments/SKILL.md).

# Worked Example: A PerCom-Style Abstract + Introduction (before → after)

This demonstrates the **PerCom first-page arc** from `percom-writing-style`:
**pervasive-computing problem in real human use → why current sensing is inadequate → contribution
(system and/or finding) → evidence on real subjects with cross-subject evaluation → what changes
for pervasive computing** — with the PerCom expectations that the contribution is a *ubicomp*
contribution, evidence is **proportional to the claim** (real people, real sensors, generalization
across subjects), and a **deployment-realism / limitations** posture is visible from the start,
not bolted on.

The framing also reflects `percom-topic-selection`: PerCom is strongest when the lesson is about
how people are **sensed, modeled, and served in everyday environments** — here, whether a wrist
wearable can recognize eating episodes across people it has never seen — rather than a pure
networking result (which would route to a networked-sensor-systems venue) or a modeling result
whose ubicomp consequence is incidental (which might route to a journal like IMWUT).

**Illustrative paper (fictional):** *"EatWatch: Cross-Subject Recognition of Eating Episodes from a
Commodity Smartwatch."* Fictional artifact: a wrist-IMU pipeline plus a released, de-identified
multi-subject dataset of daily-living eating episodes.

---

## Before (buries the ubicomp contribution — typical first-draft abstract + intro)

> **Abstract.** Wearables are transforming health. We build a deep model that recognizes eating
> from smartwatch motion data using a novel neural architecture. Our approach achieves 97%
> accuracy on our dataset and outperforms baselines, showing the promise of AI for dietary
> monitoring.
>
> **Introduction.** Diet matters for health. Many wearables now track activity. In this paper we
> use a deep network on accelerometer data to detect eating, and we evaluate it on a dataset we
> collected, showing strong results. Section 2 covers related work, Section 3 our model, Section 4
> experiments, Section 5 limitations, and Section 6 concludes.

**What's wrong (against `percom-writing-style` / `percom-topic-selection` / `percom-experiments`):**

- **No pervasive-computing question on the first page** — it leads with "wearables transform
  health" and a model win, not with a problem a real deployment faces. PerCom wants the ubicomp
  contribution up front.
- **Wrong claim shape.** "97% accuracy" on a pooled dataset hides the question PerCom reviewers ask
  first: does it work **on a person the model never trained on**? Within-subject accuracy is not
  evidence of a deployable recognizer.
- **No cross-subject evaluation and no class imbalance handling** — eating is rare in a day of
  data, so raw accuracy is inflated; F1 or event-level metrics are missing.
- **Model-as-contribution.** If the architecture were swapped, no ubicomp lesson would remain — the
  `percom-topic-selection` re-route signal that this is an ML paper wearing a wearable title.
- **No dataset-release or ethics posture** — no mention of subjects, IRB, privacy, or a shareable
  dataset, which a PerCom reviewer looks for immediately.
- **Limitations quarantined in Section 5** as boilerplate, so deployment realism is never engaged
  where it matters.

---

## After (PerCom arc — problem → inadequacy → contribution → cross-subject evidence → what changes)

> **Abstract.** Automatic diet monitoring could transform preventive health, but wrist wearables
> that recognize eating are trained and tested on the **same** people and collapse on new users and
> in free-living conditions. We study eating recognition on a **commodity smartwatch across 32
> participants over 3 weeks of daily living** and show that a within-subject model's apparent
> accuracy drops sharply under **leave-one-subject-out** evaluation, especially for short snacking
> episodes. We present **EatWatch**, a recognition pipeline that combines motion primitives with a
> personalization step requiring under a minute of user data, and evaluate it with **event-level F1
> on held-out subjects**, reporting confidence intervals, a per-subject breakdown, and a
> false-positive analysis under non-eating activities (typing, brushing). We release a de-identified
> dataset and code. *(problem → inadequacy → finding → system → cross-subject evidence →
> limitations posture — all on the first page.)*
>
> **Introduction.** *(¶1 — the pervasive-computing problem, first breath.)* A wearable that could
> quietly log *when* someone eats would unlock dietary feedback without food diaries. The
> engineering question is not "can a model separate eating from not-eating in a curated set?" but
> **"can a commodity smartwatch recognize eating episodes for a person it has never seen, during
> ordinary daily life?"**
>
> *(¶2 — why the current state is inadequate.)* Prior eating-recognition results are largely
> **within-subject and in-lab**: the same participants and scripted meals appear in train and test,
> and metrics are pooled accuracy on class-balanced windows. Real wrists differ, real days are
> mostly non-eating, and short snacks look like other hand-to-mouth motions — so a headline
> accuracy tells a reviewer nothing about a fresh user in the wild.
>
> *(¶3 — contribution, stated as ubicomp claims.)* We make two contributions. First, an **empirical
> characterization** of how eating-recognition performance degrades across subjects and from lab to
> free-living, on 32 participants over 3 weeks. Second, **EatWatch**, a pipeline with a
> under-a-minute personalization step that recovers cross-subject event-level F1 without per-user
> retraining, released as a de-identified dataset and open code.
>
> *(¶4 — evidence on real subjects, each claim paired.)* We tie every claim to evidence: the
> degradation result uses **leave-one-subject-out** splits with bootstrap confidence intervals
> (Table 1); EatWatch's gain is reported as **event-level F1 on held-out subjects** with a
> per-subject distribution (Fig. 3); false positives are measured against confounding non-eating
> activities (Table 4); and the personalization budget is reported in seconds of user data, not
> epochs. The dataset, extraction scripts, and trained models are in the artifact.
>
> *(¶5 — limitations posture and what changes for pervasive computing.)* We state the central
> limits plainly: 32 mostly-younger participants bound external validity, and the ground truth is
> self-report-confirmed rather than instrumented, which we treat as a construct threat and audit on
> a subsample. The payoff for ubicomp is concrete: dietary sensing can move off curated benchmarks
> toward users a system meets for the first time. Section 2 details the study; Section 3 EatWatch;
> Section 4 the cross-subject evaluation; limitations are argued alongside each result, not
> deferred. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the PerCom bar

Mapped to the skill checklists:

- **Ubicomp contribution on the first page** — the abstract and ¶1 pose an everyday-sensing problem
  and a deployment-level question before any model detail (`percom-writing-style`: "lead with the
  pervasive-computing contribution").
- **Evidence proportional to the claim** — the claim is about *a new user in daily life*, so the
  evidence is **leave-one-subject-out, free-living, event-level F1** with intervals, not pooled
  accuracy (`percom-experiments`: match the evidence to the claim shape; cross-subject is the
  default, not a bonus).
- **Limitations engaged where they live** — external validity (32 participants) and construct
  validity (self-report ground truth) are named in ¶5 and bounded, reported *with* results rather
  than quarantined (`percom-writing-style`).
- **Right venue, model-swap test passes** — the lesson (within-subject metrics mislead; cheap
  personalization recovers cross-subject performance) survives swapping the architecture, so it is
  a PerCom contribution, not an ML re-route (`percom-topic-selection`).
- **Open data by default, ethically** — a de-identified dataset, code, and an IRB/privacy note
  match PerCom's dataset-sharing expectations (`percom-reproducibility`).
- **Deployment-realistic evaluation** — held-out subjects, free-living data, and a false-positive
  analysis against confounding activities pre-empt the reviewer's first three objections
  (`percom-experiments`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified PerCom
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for PerCom-specific submission policy and
> the double-blind rebuttal cycle.
