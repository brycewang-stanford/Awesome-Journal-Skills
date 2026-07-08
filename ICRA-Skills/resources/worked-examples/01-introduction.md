> **Illustrative teaching example.** The robot, task, method, and every number below
> are **fictional**, constructed only to demonstrate ICRA house style. No real-paper
> facts are restated and no venue policy is invented. Companion skills:
> [`icra-writing-style`](../../skills/icra-writing-style/SKILL.md),
> [`icra-experiments`](../../skills/icra-experiments/SKILL.md), and
> [`icra-supplementary`](../../skills/icra-supplementary/SKILL.md).

# Worked Example: An ICRA-Style Abstract + Introduction (before → after)

The target shape is the ICRA first page: **robot task → physical difficulty →
mechanism → measured evidence → scope honesty**, written for a reviewer who will
watch the video attachment first and skim figures second. The fictional paper:
*"Slip-Reflex Regrasping for Torque-Controlled Manipulators."*

---

## Before (the demo write-up — typical robotics first draft)

> **Abstract.** Robotic manipulation is a key challenge for future automation.
> Recently, learning-based approaches have shown great promise. In this paper we
> present a novel framework for robust regrasping using deep learning. Extensive
> experiments demonstrate that our approach is robust and works in real time on a
> real robot, significantly outperforming baseline methods. A video demonstrates
> our system in action.
>
> **Introduction.** Manipulation has long been studied in robotics. Classical
> approaches use analytic grasp metrics, while modern methods leverage deep
> learning. However, existing methods struggle with dynamic effects. Motivated by
> this, we propose a novel end-to-end framework combining tactile sensing with
> learned recovery policies. Our contributions are: (1) a novel framework; (2) a
> new network architecture; (3) extensive real-world experiments. Experiments show
> our method is superior. The video shows our robot successfully completing many
> tasks.

**Why this fails the ICRA bar:**

- **No task, no physics.** "Robotic manipulation is a key challenge" tells the
  reviewer nothing about *what the robot does* or *what physical effect makes it
  hard* — the two facts an ICRA first paragraph must pin down.
- **Demo-speak throughout.** "Robust," "real time," "significantly outperforming,"
  "extensive" — six adjectives, zero measurements (`icra-writing-style` requires
  each converted to a number or deleted).
- **Contribution list is generic.** "A novel framework" could head any paper in
  the proceedings; nothing is falsifiable.
- **The video is used as marketing** ("in action," "many tasks") rather than as
  evidence cross-referenced to trials (`icra-supplementary`).
- **No trial counts, no failure modes, no baseline names** — the experimental
  promises are unauditable (`icra-experiments`).
- **No rebuttal exists at ICRA** to repair the vagueness later: what the reviewer
  misreads here is never corrected.

---

## After (the ICRA arc — task, physics, mechanism, numbers, honesty)

> **Abstract.** When a grasped tool slips, a torque-controlled arm leaves its
> planned contact state faster than vision-based pipelines can react. We present a
> slip-reflex layer that detects slip onset from joint-torque residuals — no added
> tactile hardware — within 12 ms of onset, and triggers a regrasp policy that
> recovers the object before task abort. On a 7-DOF arm across 5 tool geometries
> and 3 surface conditions, the reflex recovers 87% of 150 induced slip events
> (exact binomial 95% CI: 80-92%), versus 41% for a vision-triggered baseline and
> 23% for the nominal planner, with all trials, criteria, and failures reported.
> The reflex runs inside a 500 Hz impedance loop on the robot's stock sensors. All
> events, including the 19 failures, appear in the attached video and released
> logs. Limitations: rigid tools only; deformable objects defeat the residual
> model.
>
> **Introduction.** *(¶1 — task and physical difficulty.)* Tightening a bolt with
> a socket wrench fails differently on a robot than in simulation: the tool
> rotates in the gripper under reaction torque, and by the time an external camera
> confirms the slip, the contact state assumed by the planner no longer exists. We
> measured this window at 40-70 ms on our platform — beyond recovery by
> replanning. The task in this paper is regrasping mid-task after such slips, on
> stock joint-torque sensing.
>
> *(¶2 — why existing routes are insufficient, each with a named failure.)*
> Vision-triggered recovery reacts after visible displacement, which our
> measurements place past the recoverable window for the tool geometries tested.
> Tactile-array approaches detect slip earlier but require fingertip hardware
> absent from most deployed grippers. Grasp-quality re-optimization addresses
> *which* grasp to take, not *when* the current one is failing. *(three families,
> three specific failure modes — not "existing methods struggle.")*
>
> *(¶3 — mechanism, stated to be checkable.)* Our reflex layer monitors the
> residual between commanded and measured joint torques, classifies slip onset
> with a filter whose parameters are learned from 2,000 logged slip events, and
> interrupts the impedance controller with a regrasp primitive selected by
> current tool pose. Detection-to-reaction latency is 12 ms at the 500 Hz control
> rate. *(the reader can now predict what the ablations must be: the filter, the
> primitive selection, the latency budget.)*
>
> *(¶4 — evidence, scoped and auditable.)* We induce 150 slip events (10 per
> tool × surface cell) under a pre-registered protocol: success = tool secured
> within 2 s without workspace exit. The reflex recovers 87% (CI 80-92%);
> baselines: vision-triggered 41%, nominal planner 23%, identical trials. All 19
> failures are categorized (Table III: 11 late detections on low-friction glass,
> 5 primitive-in-collision, 3 hardware timeouts, disclosed) and shown at 1× speed
> in the video attachment. *(numbers, protocol, failure taxonomy, and the video
> as cross-referenced evidence.)*
>
> *(¶5 — scope honesty and contributions.)* The residual model assumes rigid
> tools; deformables violate it and are out of scope. Contributions: (i) a slip
> detector on stock torque sensing with measured 12 ms onset latency; (ii) a
> regrasp reflex integrated in a 500 Hz impedance loop; (iii) a 150-trial
> evaluation with full failure taxonomy and released logs. *(each contribution is
> falsifiable against a table, a latency measurement, or an artifact.)*

---

## What changed, mapped to the skills

| Fix | Where visible | Skill |
| --- | --- | --- |
| Task + physics open the paper | ¶1 wrench/slip window | `icra-writing-style` |
| Every adjective became a number | 12 ms, 500 Hz, 87%, CI | `icra-writing-style` |
| Prior work grouped by named failure | ¶2 three families | `icra-related-work` |
| Pre-registered protocol, n, criterion | ¶4 | `icra-experiments` |
| Failures counted, categorized, shown | ¶4, Table III reference | `icra-experiments` |
| Video cited as evidence, incl. failures | abstract + ¶4 | `icra-supplementary` |
| Scope limitation pre-answers the objection | ¶5 rigid-tools line | `icra-review-process` |

> Next: study real first pages in [`../exemplars/library.md`](../exemplars/library.md)
> (verified ICRA papers only), and check current-cycle rules in
> [`../official-source-map.md`](../official-source-map.md) before formatting.
