---
name: the-international-journal-of-robotics-research
description: Use when targeting The International Journal of Robotics Research (IJRR) or deciding whether a robotics manuscript fits this venue. Encodes the journal's fit, the longer-form conceptually-framed-and-general contribution bar, depth-and-generality rigor, the IJRR-vs-T-RO routing, house style, official-submission re-check, and desk-reject heuristics.
---

# The International Journal of Robotics Research (the-international-journal-of-robotics-research)

## Journal positioning

The International Journal of Robotics Research (IJRR), published by SAGE, is a
flagship archival venue for **longer-form, conceptually framed robotics research**:
foundational methods, extended treatments, and contributions whose value rests on
**generality and depth** rather than a single working demonstration. The defining
expectation is an idea developed thoroughly — formalized, analyzed, and evaluated
across conditions — that advances how the field thinks about a problem, not only a
system that performs one task. Compared with its sibling
`ieee-transactions-on-robotics`, IJRR favors the deeper, more general, more
conceptual treatment, while T-RO favors complete and tightly validated results;
route by whether the strength is generality-of-idea or completeness-of-validation.
This skill is a **fit / venue-selection / re-framing** tool. It does not replace
the journal's current official author guidelines. Before submitting, re-check the
live IJRR/SAGE author information.

## When to trigger

- The author names IJRR for a robotics manuscript with a foundational or
  conceptually general contribution and wants a fit/framing check.
- A result must be re-framed from "our system does X" into a general method or
  principle, developed and analyzed beyond a single demonstration.
- The author is choosing between IJRR and `ieee-transactions-on-robotics` by
  depth-and-generality vs. completeness-of-validation.
- The author needs IJRR's depth/generality bar and desk-reject heuristics.

## Scope & topic fit

- Foundational methods in planning, control, estimation, learning, and perception
  for robots, presented with generality and analysis.
- Manipulation, locomotion, and navigation when the contribution is a principle or
  framework that transfers beyond one platform or task.
- Algorithmic and theoretical robotics: complexity, guarantees, representations, and
  formal treatments grounded in robotic problems.
- Extended treatments that consolidate, generalize, or deepen a line of work into an
  archival reference.
- System and architecture contributions when the design embodies a generalizable
  concept, evaluated across conditions, not a one-off demo.

## Method & evidence bar

- The central object is a **general, well-developed idea**: a formalization, method,
  or framework whose scope and limits are characterized, not a single tuned result.
- Evaluation should probe generality — across tasks, platforms, parameters, or
  conditions — and may combine analysis, simulation, and real-robot experiments.
- Analysis (assumptions, guarantees, complexity, failure modes) is expected where the
  contribution is methodological, supporting the claim of generality.
- Experiments matter, but a single impressive demonstration is not sufficient if the
  conceptual generality is not established and tested.
- Position the work in the broader arc of the field; the contribution should change
  how a problem is approached, not just report a better number.
- Reproducibility: enough detail (and ideally code/data and video) to let others
  build on the framework, per current policy.

## Structure & house style

- SAGE long-form archival article; IJRR accommodates fuller development than a
  letters/short format — match the depth to that scope and re-check current article
  types and length policy on the live guide.
- The introduction frames the conceptual problem and the field-level gap, then states
  the general contribution; it situates the work in a broad intellectual context.
- The development is thorough: clear formalization, analysis, and a discussion of
  scope, assumptions, and limitations.
- Figures and tables support both the concept and its multi-condition evaluation;
  a supplementary video supports any hardware demonstration.
- Related work is substantive, reflecting the archival, reference-quality positioning.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the SAGE anchors, then cite
  the current IJRR author-guidelines page you checked.
- Search the live site for "International Journal of Robotics Research submission
  guidelines" and follow the current SAGE/manuscript-system version.
- Re-check article types, length expectations, and the IJRR/SAGE manuscript format.
- Confirm data/code-availability, video, and reproducibility expectations.
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure
  requirements, and open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a general, well-developed idea or framework, not a single tuned demonstration.
- [ ] Generality is established and tested across tasks/platforms/conditions, not asserted.
- [ ] Methodological claims are supported by analysis (assumptions, guarantees, complexity, failure modes).
- [ ] The work is situated in the broad arc of the field and changes how the problem is approached.
- [ ] Development depth and length fit IJRR's long-form archival format.
- [ ] Reproducibility detail (and ideally code/data/video) lets others build on the framework.

## Common desk-reject triggers

- A single working system or demo with no generalization, analysis, or conceptual framing.
- Incremental result better suited to a shorter, tightly validated format than long-form archival.
- Method asserted to be general but evaluated on one task/platform only.
- Application paper where the robotics idea is incidental and not developed.
- Thin related work and shallow analysis inconsistent with reference-quality positioning.

## Re-routing decision

- Complete, tightly validated single contribution → `ieee-transactions-on-robotics`.
- Control-theoretic result with guarantees as the core → `ieee-transactions-on-automatic-control` / `automatica`.
- Industrial-robot deployment with hardware-system focus → `ieee-transactions-on-industrial-electronics`.
- Medical/surgical-robotics imaging contribution → `ieee-transactions-on-medical-imaging`.
- Focused, timely result → a robotics letters venue or conference.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The International Journal of Robotics Research
[Topic tags] <2–3 closest robotics subtopics>
[Conceptual contribution] <the general idea/framework in one line>
[Method/evidence] <is generality established and tested, clearing IJRR's depth bar?>
[Top risk] <the single most likely reason for rejection>
[Article type] Long-form archival article
[Official items to re-check] <article type / length / format / data-code-video / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
