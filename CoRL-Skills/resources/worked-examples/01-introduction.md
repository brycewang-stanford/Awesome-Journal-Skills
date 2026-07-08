# Worked Example: Abstract and Introduction, Before → After

A fictional CoRL-target paper, rewritten to the standards in
`../../skills/corl-writing-style/SKILL.md` and `../../skills/corl-experiments/SKILL.md`.
The paper, its numbers, and its authors are invented; no venue policy is invented —
where the rewrite leans on a rule (mandatory Limitations, evidence-scale
statement), the rule is real and mapped in `../official-source-map.md`.

## The fictional project

A method ("LATCH") for learning contact-rich cabinet-opening and drawer-opening
from 400 teleoperated demonstrations, using a force-aware action representation.
Trained in simulation across procedurally generated furniture; deployed on one
real mobile manipulator.

---

## BEFORE (typical first draft)

> **Abstract.** Opening articulated furniture is a fundamental challenge for
> household robots. We propose LATCH, a novel force-aware imitation learning
> framework that seamlessly handles diverse articulated objects. Extensive
> experiments demonstrate that LATCH significantly outperforms state-of-the-art
> baselines and generalizes robustly to the real world. We believe LATCH is an
> important step toward general household manipulation.
>
> **Introduction (opening).** Recent years have witnessed remarkable progress in
> robot learning. However, contact-rich manipulation remains challenging. Existing
> methods either rely on accurate models or fail to generalize. In this paper, we
> present LATCH, which addresses these limitations through a novel architecture...

### Why this fails at CoRL

- **No evidence scale anywhere.** "Extensive," "significantly," "robustly" — a
  reviewer scoring against the rubric finds no tasks × seeds × episodes to anchor
  the claims; the abstract promises what the rebuttal will later have to retrofit.
- **"Seamlessly / novel / remarkable"** — demo adjectives the style skill bans;
  each will be tested against the video and the tables.
- **The learned/engineered boundary is invisible.** What is learned? What is the
  action space? Which parts are scripted? Both reviewer audiences are left
  guessing.
- **"Generalizes robustly to the real world"** — an unscoped sim-to-real claim,
  the single most attacked sentence shape at this venue.
- **A vision-statement ending** replaces the takeaway a reader could reuse.

---

## AFTER (CoRL-calibrated)

> **Abstract.** Opening cabinets, drawers, and appliance doors requires policies
> that regulate contact forces, not just positions: position-only imitation
> snaps handles and stalls on stiff hinges. We present LATCH, an imitation
> learner whose action representation couples end-effector motion targets with
> feedforward wrench profiles extracted automatically from 400 teleoperated
> demonstrations. Across 24 procedurally generated articulated-furniture tasks
> in simulation (5 seeds, 100 evaluation episodes each), LATCH reaches 81 ± 3%
> success versus 62 ± 4% for a diffusion-policy baseline given identical
> demonstrations. On a real mobile manipulator, the same checkpoints achieve
> 68% over 75 trials spanning 9 unseen furniture units — an average sim-to-real
> drop of 13 points, concentrated in high-stiffness hinges. Failure modes,
> protocol, and data are released; the policy runs at 20 Hz onboard.
>
> **Introduction (opening).** A robot that cannot open a cabinet cannot put
> anything in it. The specific difficulty is force: handles must be grasped,
> latches unseated, and hinges driven along constrained arcs where a few
> newtons separate success from hardware-stressing failure. We ask whether a
> force-aware action representation — motion targets paired with wrench
> profiles — lets ordinary behavioral cloning absorb this skill from
> demonstrations, without dynamics models or online adaptation. Everything
> upstream of the policy is deliberately standard (off-the-shelf grasp
> proposals, scripted approach); the contribution is the learned contact-phase
> policy and the evidence that its force channel, not extra data or capacity,
> produces the gains (ablation, §5.4)...

### What changed, mapped to pack standards

| Change | Skill standard it satisfies |
|---|---|
| Every claim carries tasks × seeds × episodes | `corl-experiments` two-layer randomness protocol |
| "Same checkpoints" sim → real, gap printed (13 points) | transfer claims need the identical-checkpoint pairing |
| Baseline named, given identical demonstrations | baseline-fairness norms |
| Learned vs engineered boundary drawn in the intro | `corl-writing-style` dual-audience rule |
| Failure location admitted (stiff hinges) up front | feeds the mandatory, counted Limitations section |
| "20 Hz onboard" replaces "real-time" | calibrated-claim table |
| Opening names the task and the physical difficulty | page-1 contract, question 1 |
| Contribution phrased as a testable question + ablation pointer | claims map to designated evidence |

### Residual work the rewrite still owes the paper

- The Limitations section must expand the stiff-hinge failure with numbers and a
  mechanism hypothesis, consistent with the supplementary video's failure clips.
- §4 must specify the real-robot protocol verbatim: reset procedure, success
  criterion, trial counts per furniture unit, and any excluded trials with cause.
- The 400-demonstration dataset needs a datasheet and a release tier declaration
  (`corl-artifact-evaluation`) before the claims about release are printed.
