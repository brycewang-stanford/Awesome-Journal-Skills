---
name: ieee-transactions-on-robotics
description: Use when targeting IEEE Transactions on Robotics (T-RO) or deciding whether a robotics manuscript fits this venue. Encodes the journal's fit, the complete-and-experimentally-validated-contribution bar, real-robot evidence rigor, the T-RO-vs-IJRR routing, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Robotics (ieee-transactions-on-robotics)

## Journal positioning

IEEE Transactions on Robotics (T-RO), published jointly by the IEEE Robotics and
Automation Society and partnering societies, is a flagship archival venue for
**complete, rigorously validated robotics contributions**: manipulation,
locomotion, motion planning, control, perception-for-action, estimation, and
mechanism/system design. The defining expectation is a self-contained advance
demonstrated through **experiments on real robots or high-fidelity simulation**,
with quantitative evaluation — not a preliminary idea or a method shown only on a
toy. Compared with its sibling `the-international-journal-of-robotics-research`,
T-RO favors complete, well-validated results, while IJRR leans to longer,
conceptually framed archival treatments; route by depth-of-framing vs.
completeness-of-validation. This skill is a **fit / venue-selection / re-framing**
tool. It does not replace the journal's current official author information.
Before submitting, re-check the live IEEE T-RO author guidance and submission system.

## When to trigger

- The author names T-RO for a manipulation, locomotion, planning, control, or
  perception-for-action manuscript and wants a fit/framing check.
- A result must be re-framed from "a method that works in simulation" into a
  complete contribution with real-robot or high-fidelity experimental validation.
- The author is choosing between T-RO and `the-international-journal-of-robotics-research`,
  or between T-RO and a conference-paper extension.
- The author needs T-RO's experimental-validation bar and desk-reject heuristics.

## Scope & topic fit

- Manipulation and grasping: dexterous and contact-rich manipulation, planning and
  control of manipulators, tactile/force-based interaction.
- Legged, wheeled, aerial, and underwater locomotion: dynamics, gait, and control
  demonstrated on physical platforms or validated high-fidelity simulation.
- Motion and task planning: sampling-based, optimization-based, and learning-based
  planning with analysis and demonstrated performance.
- Robot control and estimation: whole-body control, state estimation, SLAM-for-control,
  and learning-based control with real-system evaluation.
- Perception for action: closing the loop from sensing to robot behavior, where the
  robotics contribution (not the vision algorithm alone) is central.
- Mechanism, actuator, and system design: novel robot designs validated by
  characterization and task demonstration.

## Method & evidence bar

- **Experiments on real robots** are the norm; high-fidelity simulation is
  acceptable when justified, but pure toy simulation rarely clears the bar.
- Evaluation must be quantitative and statistically meaningful: report trials,
  success rates, error metrics, and timing, with appropriate baselines.
- The contribution must be complete — formulation, method, analysis (where relevant),
  and a convincing experimental campaign — not a preliminary proof-of-concept.
- Compare against the closest robotics baselines under matched conditions; ablate to
  show which component drives the gain.
- For learning-based methods, address sim-to-real transfer, generalization, and
  robustness, not just one trained instance on one setup.
- Provide reproducibility detail: platform, parameters, and ideally a supplementary
  video and code/data per current policy.

## Structure & house style

- IEEE double-column format; T-RO publishes full-length **Papers** (substantial,
  archival) — match the contribution to that scope and re-check current article types
  and length policy on the live guide.
- The introduction frames the robotics problem and the gap, then states the complete
  contribution; conference-to-journal extensions must add substantial new content.
- Figures are load-bearing: system/method diagrams, experimental setups, result
  plots with error bars, and frames from the accompanying video.
- A thorough experimental-results section is central; tables summarize quantitative
  comparisons across baselines and conditions.
- A supplementary video is strongly expected for hardware results.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center
  anchors, then cite the current T-RO-specific page you checked.
- Search the live site for "IEEE Transactions on Robotics information for authors"
  and follow the current ScholarOne/IEEE version.
- Re-check article types, page/length limits and overlength policy, and the IEEE
  double-column template.
- Confirm video, code/data, and reproducibility submission requirements.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a complete robotics advance, not a preliminary idea or single toy demo.
- [ ] Validation is on real robots (or justified high-fidelity simulation) with quantitative metrics.
- [ ] Results report trials/success rates/errors with appropriate baselines and ablations.
- [ ] Learning-based claims address transfer, generalization, and robustness beyond one setup.
- [ ] Any conference precursor is substantially extended with new content.
- [ ] A supplementary video and reproducibility detail accompany hardware results; length fits current limits.

## Common desk-reject triggers

- Method shown only in toy simulation with no real-robot or high-fidelity validation.
- Preliminary proof-of-concept lacking a complete formulation, analysis, or convincing experiments.
- Incremental conference extension with little new content beyond the prior paper.
- A computer-vision or learning paper with a robot used only as a label, no robotics contribution.
- Quantitative evaluation without baselines, trials, or statistics; cherry-picked single runs.

## Re-routing decision

- Longer, conceptually framed, foundational archival robotics → `the-international-journal-of-robotics-research`.
- Control-theoretic result with guarantees as the core → `ieee-transactions-on-automatic-control` / `automatica`.
- Industrial robot deployment with hardware-system focus → `ieee-transactions-on-industrial-electronics`.
- Medical/surgical-robotics imaging contribution → `ieee-transactions-on-medical-imaging` / `ieee-transactions-on-biomedical-engineering`.
- Focused, timely result → a robotics letters venue or conference.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Robotics
[Topic tags] <2–3 closest robotics subtopics>
[Contribution] <the complete robotics advance in one line>
[Method/evidence] <does the real-robot / high-fidelity validation clear T-RO's completeness bar?>
[Top risk] <the single most likely reason for rejection>
[Article type] Paper
[Official items to re-check] <article type / length / template / video-code-data / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
