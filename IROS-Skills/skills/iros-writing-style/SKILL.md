---
name: iros-writing-style
description: Use when revising an IROS paper for a task-first opening, an integrated-system narrative, the references-counted-in page budget with no supplementary PDF, double-anonymous wording, demo-speak-to-numbers rewrites, and figure-first structure that carries the argument in the body for embodied-systems reviewers.
---

# IROS Writing Style

Use this when revising the main paper. An IROS paper has to make a reviewer picture the robot, the task,
and the physical constraint quickly, then trust that the system runs — all inside a page budget that
counts references and offers no appendix escape hatch.

## Revision rules

- Open with the **robot task and the embodiment constraint**, not with "robots are increasingly
  important." The first paragraph should name the platform, the task, and what makes it physically hard.
- Present the contribution as an **integrated system**: name the sensors, the interfaces between
  components, and the compute/latency budget, so the pipeline is reconstructable from the body.
- Treat the **body as the whole paper** — IROS has no supplementary PDF. Anything load-bearing (metric
  definition, protocol, key ablation) lives in the main text or it does not exist for the reviewer.
- Budget **references as content**; they count against the page limit, so a bloated bibliography costs
  real space.
- Convert **demo-speak to numbers**: "works robustly" becomes a trial count with a success interval and
  a failure taxonomy.
- Keep **double-anonymous** wording clean in self-citations, prior-platform references, acknowledgements,
  and figure/video captions.

## Figure-first discipline

- Robotics reviewers read figures before prose; a system diagram and a results figure should convey the
  contribution before a word is read.
- Make the hero figure a **system diagram with real interfaces**, not a clip-art robot — show what
  senses what and what commands what.
- Every plot of contact force, trajectory error, or success rate needs axis units and a stated trial
  count in the caption; a curve without n is decoration.
- Prefer vector figures: reviewers zoom into force and trajectory plots, and rasterized exports blur at
  400%.

## Sentence-level rewrites

| Draft pattern | IROS-safe rewrite |
|---|---|
| "Our system robustly opens doors." | "Succeeds on 108/120 trials across 15 unseen doors (Wilson 95% CI ...)." |
| "Real-time performance." | "Runs the full loop at 18 Hz within a 30 W onboard budget." |
| "Outperforms the baseline." | "Reduces trajectory error by X on the same platform and route." |
| "Works in the real world." | "Sim-to-real gap of Y points; failures categorized in Table II." |

## Vignette: compressing into the page budget

A draft with a sprawling related-work section, six figures, and a full appendix of derivations: keep the
system diagram and the two decision-critical results figures, fold related work into per-system
contrasts, and inline only the equations the reviewer must see — the rest is cut, not deferred, because
there is no appendix PDF. The test of a good cut: a reviewer reconstructs the system and believes the
evidence from the body alone.

```text
First-page checklist:
  [ ] robot + task + physical constraint stated in the first paragraph
  [ ] system diagram with real sensor/actuator interfaces as the hero figure
  [ ] each claim carries a number (Hz, watts, trials, error, gap)
  [ ] references budgeted inside the page limit
  [ ] no dependence on a non-existent supplement
  [ ] anonymity clean in text, figures, and video captions
```

## Output format

```text
[Writing diagnosis] task-clear / demo-speak / system-vague / over-budget
[First-page fix] <new task-and-constraint opening>
[Claim discipline] <claim -> number/figure/trial>
[Compression cuts] <cut, not deferred — no appendix>
[Anonymity edits] <phrases/figures/video to fix>
```
