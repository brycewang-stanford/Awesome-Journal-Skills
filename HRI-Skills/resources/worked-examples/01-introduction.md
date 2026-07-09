> **Illustrative teaching example.** The paper, robot, study, and every number below are
> **fictional** and exist only to demonstrate HRI house style. No real-paper facts, participants, or
> results are stated, and no policy is invented. Corresponding skills:
> [`hri-writing-style`](../../skills/hri-writing-style/SKILL.md),
> [`hri-topic-selection`](../../skills/hri-topic-selection/SKILL.md), and
> [`hri-experiments`](../../skills/hri-experiments/SKILL.md).

# Worked Example: An HRI-Style Abstract + Introduction (before → after)

This demonstrates the **HRI first-page arc** from `hri-writing-style`:
**interaction problem → why we do not yet know the answer → contribution (a designed robot behavior
and/or a finding about people) → study of an embodied robot with real participants → what it means
for how we design robots that interact with people** — with the HRI expectations that there is a
**robot embodiment**, evidence is a **human-subjects study** proportional to the claim (design,
measures, effect sizes *and*/or qualitative rigor), and the **track** and its contribution type are
legible from the first page.

The framing also reflects `hri-topic-selection`: HRI is strongest when the lesson is about the
**interaction between a person and an embodied robot** — here, whether a robot admitting its own
uncertainty changes how much people rely on it — rather than a robot-autonomy result with no human
in the loop (which would route to ICRA/IROS) or a screen-only interface study with no robot (which
would route to CHI).

**Illustrative paper (fictional):** *"'I'm Not Sure': How a Delivery Robot's Expressed Uncertainty
Shapes Human Reliance and Blame."* Fictional robot: a wheeled indoor delivery robot that can either
state its confidence or stay silent. Fictional study: a between-subjects lab experiment in which
participants decide whether to accept the robot's route recommendations.

---

## Before (buries the interaction question — typical first-draft abstract + intro)

> **Abstract.** Robots are increasingly deployed in human environments. We build a delivery robot
> that expresses uncertainty using a state-of-the-art confidence-estimation module and a novel
> speech interface. Our system achieves high estimation accuracy and users rated it positively,
> showing the promise of transparent robots for human-robot interaction.
>
> **Introduction.** Human-robot interaction is important. Many robots now work alongside people. In
> this paper we add an uncertainty-expression capability to a delivery robot using a confidence
> module, and we evaluate it in a user study, showing users liked it. Section 2 covers related work,
> Section 3 our system, Section 4 the study, Section 5 results, and Section 6 concludes.

**What's wrong (against `hri-writing-style` / `hri-topic-selection` / `hri-experiments`):**

- **No interaction question on the first page** — it leads with "robots are important" and a systems
  win (estimation accuracy), not with a question about *what happens between the person and the
  robot*. HRI wants the human-robot contribution up front.
- **Wrong claim shape.** "High estimation accuracy" and "users rated it positively" are a component
  metric and a vague liking score; neither shows whether uncertainty expression changes **reliance**
  — the behavioral outcome that matters. The claim and the evidence do not match.
- **No design or hypotheses.** The reader cannot tell if this is between- or within-subjects, what
  was manipulated, what was measured, or what was predicted — so no reviewer can judge the study.
- **Track is illegible.** Is this a Systems paper (the capability), a User Studies paper (reliance),
  or a Technical paper (the estimator)? An HRI submission must enter one track and be judged by it.
- **Robot embodiment underdescribed and no video** — HRI reviewers need to see the robot and the
  interaction; a silent, screen-free description hides the very thing being studied.
- **Ethics invisible** — a study with participants and (implicitly) deception about robot competence
  needs an IRB/consent posture, absent here.

---

## After (HRI arc — interaction problem → gap → contribution → embodied study → design implication)

> **Abstract.** As mobile robots give people recommendations in everyday settings, a design choice
> recurs: should the robot **admit when it is unsure**? Transparency is widely assumed to be good,
> but expressed uncertainty could equally *reduce* appropriate reliance or shift **blame** onto the
> user when things go wrong — and we lack evidence about which. In a **between-subjects lab study
> (N = 96)**, participants followed route recommendations from a wheeled delivery robot that either
> **expressed its confidence verbally** or stayed silent, across trials where the robot was
> sometimes wrong. We measure **reliance** (whether people accept recommendations, and how
> appropriately given robot accuracy), **trust** (a validated scale), and **blame attribution**
> after a failure, reporting effect sizes and confidence intervals. We find that expressed
> uncertainty **calibrates** reliance — people follow good advice and reject bad advice more often —
> but also **shifts blame toward the robot** after failures. We contribute a **designed
> uncertainty-expression behavior**, an **empirical account of its effect on reliance and blame**,
> and design guidance for when transparency helps. A video shows the interaction; study materials and
> de-identified data are in the supplement. *(interaction problem → gap → contribution → embodied
> study → finding → design implication — all on the first page.)*
>
> **Introduction.** *(¶1 — the interaction problem, first breath.)* When a robot tells a person
> "take the left corridor," the person must decide whether to believe it. Designers increasingly
> want robots to be *transparent* about their own confidence — but it is not obvious that hearing
> "I'm not sure" makes a person rely on the robot **better**. It might make them ignore good advice,
> or it might change who they blame when the route is wrong. The interaction question is therefore
> not "can the robot estimate its confidence?" but **"how does a robot expressing uncertainty change
> a person's reliance on it, and their blame when it fails?"**
>
> *(¶2 — why we do not yet know.)* Prior work shows people form trust in robots quickly and that
> robot errors damage it, and transparency is often recommended. But most evidence measures *stated*
> trust on questionnaires rather than *behavioral reliance*, and rarely separates transparency's
> effect on **appropriate** reliance (following good advice, rejecting bad) from its effect on
> **blame**. We do not know whether expressed uncertainty helps people calibrate — or simply lowers
> confidence across the board.
>
> *(¶3 — contribution, stated for the track.)* This is a **User Studies** contribution. We make
> three: (a) a **designed uncertainty-expression behavior** for a mobile delivery robot, grounded in
> calibration theory; (b) an **experiment** isolating its causal effect on reliance and blame; and
> (c) **design guidance** on when to express uncertainty. Hypotheses: expressed uncertainty
> **improves reliance calibration** (H1) but **increases blame on the robot** after failure (H2).
>
> *(¶4 — the embodied study, each claim paired with evidence.)* We ran a between-subjects lab
> experiment (N = 96, IRB-approved, informed consent) with a real wheeled delivery robot; the
> uncertainty manipulation was controlled and logged. We measure reliance behaviorally (accept/
> reject decisions against ground-truth robot accuracy), trust with a validated scale, and blame
> with a post-failure attribution measure; analyses report effect sizes with confidence intervals
> and a pre-registered primary comparison. A manipulation check confirms participants noticed the
> uncertainty cues.
>
> *(¶5 — limitations posture and the design implication.)* We state the central limitation plainly:
> a controlled lab task with a single robot and short exposure bounds external validity, so we frame
> the result as a **calibration-vs-blame trade-off to test in the field**, not a universal law. The
> design payoff is concrete: transparency is not free — expressing uncertainty can help people rely
> appropriately while making the robot the target of blame, so designers should choose it where
> calibration matters more than perceived robot competence. Section 2 details the design; Section 3
> the study; limitations are argued alongside each result, not deferred. *(brief roadmap, no
> over-signposting.)*

---

## Why the "after" meets the HRI bar

Mapped to the skill checklists:

- **Interaction question on the first page** — the abstract and ¶1 pose a *human-robot* question
  (reliance, blame) before any module detail (`hri-writing-style`: "lead with the human-robot
  contribution, not the system").
- **Evidence proportional to the claim** — the claim is about *reliance and blame*, so the evidence
  is behavioral reliance data and a blame measure on real participants, with effect sizes — not
  estimation accuracy or a liking score (`hri-experiments`: match evidence to the claim, report
  effect sizes).
- **A real study with a visible design** — between-subjects, N stated, hypotheses, manipulation
  check, validated scale, pre-registered primary comparison; a reviewer can judge it
  (`hri-experiments`).
- **Right venue and track** — there is a robot embodiment and a human in the loop, so it is HRI not
  ICRA/IROS or CHI; and it enters the **User Studies** track and is written to that contribution
  type (`hri-topic-selection`).
- **Embodiment and video** — the robot is described and a video shows the interaction, matching how
  HRI reviewers read temporal, embodied behavior (`hri-supplementary`).
- **Ethics visible** — IRB approval and informed consent are stated, as HRI's human-participants
  obligations require (`hri-experiments`, `hri-submission`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified HRI
> conference papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for HRI-specific submission policy, the
> five tracks, and the two-phase review model.
