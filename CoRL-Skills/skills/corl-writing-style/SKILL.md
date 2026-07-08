---
name: corl-writing-style
description: Use when writing or revising a CoRL paper's prose — leading with the embodied task and the learned component, calibrating claims to evaluation scale, writing the mandatory Limitations section as a scored asset, fitting the argument into 8 pages, and satisfying a dual reviewer audience of ML and robotics readers.
---

# CoRL Writing Style

A CoRL paper is read by two audiences at once: reviewers fluent in learning
methods who will probe the algorithmic claim, and reviewers fluent in robots who
will probe the physical claim. Prose that serves only one of them loses the
other's score. The style guidance here is about keeping both readers oriented
inside 8 pages — with a mandatory Limitations section spending part of that
budget (CoRL 2026 instructions, corl.org, read 2026-07-08).

## The opening contract

By the end of page 1, both audiences should be able to answer four questions:

1. **What does the robot do** that it couldn't before? (task family, concrete)
2. **What is learned**, and what is engineered around it? (policy? reward?
   representation? data?)
3. **What is the evidence scale?** (tasks × seeds × episodes; sim, real, or both)
4. **Why does this generalize beyond the demo?** (the transferable insight)

A reliable abstract shape: task problem → why existing learning approaches fall
short → the idea in one sentence → headline evidence with its scale attached
("across 8 manipulation tasks, 5 seeds, 50 evaluation episodes each, on a real
UR5") → the takeaway for the field.

## Claim calibration — the venue's core stylistic norm

Robot-learning results are stochastic and setup-dependent; the writing must carry
those qualifiers without drowning in them. Calibrate at the sentence level:

| Overclaimed | Calibrated |
|---|---|
| "Our policy solves kitchen manipulation" | "Our policy reaches 76% mean success on the 6-task kitchen suite" |
| "Transfers seamlessly to the real world" | "Transfers with an 11-point average sim-to-real drop (Table 4)" |
| "Generalizes to unseen objects" | "Maintains 61% success on 10 held-out objects (vs 78% on training objects)" |
| "Runs in real time" | "Runs at 15 Hz on the onboard Orin" |
| "Robust to disturbances" | "Recovers from 8 of 12 scripted pushes (protocol in §5.3)" |

The pattern: attach the number, the scale, and the pointer. This is also rebuttal
insurance — precise claims are defensible in one page; vibes are not.

## The Limitations section: write it as an asset

CoRL makes Limitations mandatory and counts it inside the page limit, which
changes its rhetorical status: reviewers treat it as part of the argument, not
boilerplate. A strong one:

- Names *specific* failure modes observed ("fails on transparent objects; the
  depth camera returns holes"), matching what the supplementary video shows.
- States the *boundary of the claim* ("evaluated on a single embodiment; no
  cross-robot claim"), which preempts the corresponding review objection.
- Proposes concrete paths forward, not "future work will explore."

Weak versions — generic ("more experiments needed"), disguised advertising
("limited only by compute"), or contradicted by the video — actively cost points
with this reviewer pool.

## Structure for an 8-page body

```text
1  Introduction          1.00 pp   the four-question contract
2  Related work          0.75 pp   three-lane positioning (corl-related-work)
3  Method                2.00 pp   one architecture figure; learned vs engineered
                                   boundary drawn explicitly
4  Experimental setup    1.25 pp   tasks, robot/sim, data, baselines, protocol —
                                   the reproducibility spine lives HERE, not appendix
5  Results               2.25 pp   claims in subsection headers; per-axis analysis
6  Limitations           0.50 pp   mandatory; specific; video-consistent
7  Conclusion            0.25 pp   one paragraph
   (references + appendix follow, uncounted)
```

Adjust the split, but defend two invariants: the setup section is generous
(robotics readers judge rigor there), and Limitations is protected (it is
mandatory and cutting it to reclaim space is not an option).

## Serving the dual audience in the method section

- Open the method with the *interface*: observation space, action space, control
  frequency. ML readers get the problem formalized; robotics readers learn what
  the policy actually commands.
- Draw the learned/engineered boundary in one explicit paragraph ("grasp
  proposals are scripted; the insertion policy is learned"). Blurring this line
  is the most common honesty complaint in reviews of systems-flavored papers.
- Prefer one strong figure per idea: an execution filmstrip with per-frame
  annotations often communicates a robot result faster than any paragraph — but
  every figure claim needs its number in a table too; filmstrips are anecdotes.
- Keep notation light and standard (states, actions, observations, policy); a
  CoRL paper rarely needs custom operator symbols, and every nonstandard symbol
  taxes half your audience.

## Sentence-level habits that survive review

- Present tense for the method, past tense for the runs you did.
- "We find" for empirical observations, "we prove/show" reserved for what is
  actually established at that strength.
- Numbers with dispersion wherever a mean appears; captions state k seeds × n
  episodes so tables stand alone when skimmed.
- Kill demo adjectives ("impressive," "remarkable," "highly robust") — the video
  either shows it or it isn't so.
- Acronym hygiene: define at first use; the field's alphabet soup (BC, RL, VLA,
  MPC, SDF) is not universal across your two audiences.

## Revision pass checklist

```text
[ ] Page-1 contract: task, learned component, evidence scale, insight
[ ] Every abstract claim → number + scale + section pointer
[ ] Learned vs engineered boundary stated explicitly
[ ] Setup section carries protocol detail (not deferred to appendix)
[ ] Limitations: specific, video-consistent, claim-bounding
[ ] Captions self-contained with seeds × episodes
[ ] No demo adjectives; no uncalibrated robustness language
[ ] Both audiences can follow §3 (interface first, standard notation)
```

Style norms are community culture; recalibrate against recent accepted papers in
the newest PMLR volume (v305 for CoRL 2025) and the live author instructions at
corl.org each cycle.
