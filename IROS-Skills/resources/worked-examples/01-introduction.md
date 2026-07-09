> **Illustrative teaching example.** The system, robot, task, and every number below are
> **fictional** and exist only to demonstrate IROS house style. No real-paper facts, datasets, or
> results are stated, and no policy is invented. Corresponding skills:
> [`iros-writing-style`](../../skills/iros-writing-style/SKILL.md),
> [`iros-topic-selection`](../../skills/iros-topic-selection/SKILL.md), and
> [`iros-experiments`](../../skills/iros-experiments/SKILL.md).

# Worked Example: An IROS-Style Abstract + Introduction (before → after)

This demonstrates the **IROS first-page arc** from `iros-writing-style`:
**robot task and embodiment constraint → why current systems fail on it → the integrated system →
embodied evidence (trials, resets, failures, transfer) → why it belongs at IROS** — with the IROS
reality that there is **no supplementary PDF**, so everything load-bearing lives in the body, and that
reviewers read the **60-second video** before the text.

The framing also reflects `iros-topic-selection`: IROS is strongest when **a working system meets a
real embodiment constraint**, not when a learning curve is the whole story (which might route to CoRL)
or when a single foundational claim carries the paper (which might route to RSS).

**Illustrative paper (fictional):** *"Reliable Opening of Unseen Spring-Loaded Doors with a Mobile
Manipulator under a 30-Watt Onboard Compute Budget."* Fictional system: a wheeled arm that senses hinge
side and spring resistance from contact, and re-plans its base and grasp on the fly.

---

## Before (buries the system — typical first-draft abstract + intro)

> **Abstract.** Robots are increasingly deployed in human environments. Opening doors is an important
> capability for service robots. We propose a novel deep learning approach that combines perception and
> control to open doors. Our method achieves strong performance and outperforms baselines in extensive
> experiments, demonstrating the effectiveness of our approach.
>
> **Introduction.** Door opening has been studied for many years. Many approaches exist, including
> classical planning and learning-based methods. In this paper, we present an end-to-end system that
> uses a neural network to open doors. We evaluate our system and show that it works well. Section II
> reviews related work, Section III describes our method, Section IV presents experiments, and Section V
> concludes.

**What's wrong (against `iros-writing-style` / `iros-topic-selection` / `iros-experiments`):**

- **No robot task or embodiment constraint on the first page** — "robots are deployed in human
  environments" is a slogan, not a problem statement. IROS wants the specific task, platform, and
  physical constraint up front.
- **The system is invisible.** "Combines perception and control" names no interface, no sensor, no
  compute budget — a reviewer cannot picture the robot.
- **Overclaims** ("strong performance," "outperforms baselines," "works well") with **no trial counts,
  no success criterion, and no failure analysis** — the exact evidence IROS reviewers open the video to
  check.
- **No sim-to-real or reliability framing** — nothing says how many real doors, how many resets, or how
  it fails.
- **Venue-misfit framing** — pitched as "a novel deep learning approach," which invites the question of
  whether this is a learning paper (CoRL) rather than a systems-under-constraint paper (IROS).
- **Roadmap-as-argument** — the Section II-V recital stands in for a contribution.

---

## After (IROS arc — task/constraint → gap → system → embodied evidence → why it matters)

> **Abstract.** Service robots must open **spring-loaded** doors they have never seen, but a mobile
> manipulator cannot know the hinge side or the spring stiffness until it makes contact, and onboard
> planners that could search these unknowns exceed a battery-powered robot's compute budget. We present
> a mobile-manipulation system that **infers hinge side and spring resistance from the first 2 seconds
> of contact wrench** and re-plans the base pose and grasp online within a **30 W onboard budget**, with
> no offboard compute. On **120 trials across 15 previously unseen doors** (fictional), the system
> completes the open-and-pass-through task in **89% (fictional)** of trials; we report the full failure
> taxonomy — mis-inferred hinge side, slip at the handle, and base-arm reach conflicts — and the
> reset protocol. A physics-simulation study sweeps spring stiffness to show where contact inference
> degrades, and the real-robot gap is **7 points (fictional)**. The 60-second video shows three
> uncut successful trials and two labeled failures.
>
> **Introduction.** *(¶1 — task, platform, constraint, first breath.)* A robot that opens only the doors
> it was trained on is not useful in a building. We target **spring-loaded** doors — the kind that push
> back — opened by a **wheeled manipulator** that must decide, at contact, which way the door swings and
> how hard it resists, all **within a 30 W onboard compute budget** so the robot stays untethered.
>
> *(¶2 — gap: why current systems fail this specific task.)* Existing approaches fail here for concrete,
> nameable reasons. Vision-only hinge detection **cannot see spring stiffness**, which only reveals
> itself under load. Learned end-to-end policies **assume the door's swing direction is fixed** or
> known, and mis-commit on the first push. Full online planning over hinge and stiffness **exceeds the
> power budget** of a battery-powered base. *(each prior line gets a specific failure, not "prior work
> is limited.")*
>
> *(¶3 — the system and its interfaces.)* Our system reads the **contact wrench** during a brief probing
> push, estimates hinge side and a spring-stiffness bracket, and feeds those to a **base-and-grasp
> re-planner** that fits the 30 W budget by searching a discretized, pre-cached motion library rather
> than optimizing from scratch. We state the sensor, the estimator's inputs and outputs, the planner's
> action set, and the compute measurement method so the pipeline is reconstructable from the body alone.
>
> *(¶4 — embodied evidence, each claim grounded.)* We run **120 trials across 15 unseen doors**
> (fictional), define success as **latched-open plus base pass-through**, and report **success rate with
> a Wilson interval**, not a bare mean. We publish the **failure taxonomy** and the **reset procedure**
> between trials, because unreported resets inflate reliability. A **simulation sweep over spring
> stiffness** maps where contact inference breaks, and we quantify the **sim-to-real gap** rather than
> implying it is zero. *(every claim → trial count, interval, failure class, or transfer number.)*
>
> *(¶5 — why it belongs at IROS + roadmap.)* The contribution is an **integrated system that turns an
> unobservable physical property into an online decision under a hard power budget** — perception,
> estimation, and planning working together on a real robot, which is the IROS center of gravity.
> Section II positions against door-opening and contact-estimation systems; Section III details the
> pipeline; Section IV reports the trials, failures, and transfer study. *(brief roadmap, no
> over-signposting.)*

---

## Why the "after" meets the IROS bar

Mapped to the skill checklists:

- **Task and embodiment on the first page** — the abstract and ¶1 name the door type, the platform, and
  the 30 W budget before any method detail (`iros-writing-style`: "lead with the robot task and the
  physical constraint").
- **The gap is specific** — three prior approaches each get a named physical failure
  (`iros-related-work`: distinguish, don't dismiss).
- **Every claim is grounded in embodied evidence** — success → 120 trials with an interval; reliability →
  failure taxonomy and reset protocol; transfer → a stated sim-to-real gap (`iros-experiments`:
  claim-to-evidence ladder).
- **No overclaiming** — "89% across 15 unseen doors" with a reported interval and failures, not
  "outperforms baselines" (`iros-experiments`: report reliability, not best-case).
- **Video as evidence, not decoration** — uncut successes plus labeled failures in 60 seconds
  (`iros-supplementary`: the video is a first-class artifact, and IROS caps it tighter than ICRA).
- **Right venue** — a system meeting an embodiment constraint, not a pure learning result (CoRL) or a
  single foundational claim (RSS), so it is a strong IROS fit (`iros-topic-selection`).
- **No-supplement discipline** — the sensor, estimator, planner, metric, and protocol all live in the
  body, because IROS has no supplementary PDF to hide them in (`iros-writing-style`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, DOI-verified IROS papers**
> whose first pages execute this arc, and [`../official-source-map.md`](../official-source-map.md) for
> IROS-specific submission policy.
