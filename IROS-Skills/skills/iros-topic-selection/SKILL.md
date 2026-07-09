---
name: iros-topic-selection
description: Use when deciding whether a project is a strong IROS fit, routing among ICRA, RSS, CoRL, RA-L, T-RO, HRI, and CASE from IROS's seat on the fall IEEE/RSJ calendar, identifying the integrated-system contribution and its embodiment constraint, and sharpening the intelligent-robots-and-systems framing before writing begins.
---

# IROS Topic Selection

Use this before writing. IROS is strongest for an **integrated intelligent system** — perception,
estimation, planning, learning, or control working together on a robot — validated under a real
embodiment constraint. The house question is not "is the idea novel?" but "does the system run, on
stated hardware, and is that demonstrably hard?"

## Fit test

- Prefer IROS when the contribution is a working system for perception-action integration, autonomy,
  navigation, manipulation, robot learning deployed on hardware, human-aware robotics, or fielded
  systems — and the embodiment (sensors, compute, power, latency) shapes the design.
- Route to **ICRA** when the work is a fine automation/robotics contribution whose natural slot is the
  spring cycle; IROS and ICRA overlap heavily, so timing and program fit often decide.
- Route to **RSS** when the contribution is a single, foundational, science-first claim that wants a
  single-track audience and a rebuttal, rather than deployed-system breadth.
- Route to **CoRL** when the learning method *is* the contribution and robots are the testbed, more than
  the system integration being the point.
- Route to **RA-L / T-RO** when the work wants journal review and revision, then optionally a conference
  presentation via the transfer window.
- Route to **HRI / RO-MAN** for interaction studies with human-subjects methodology, and to **CASE** for
  automation-science and factory-scale problems.

## Fit signal table

| Signal in the project | IROS reading |
|---|---|
| A system that runs on real hardware under a compute/power/latency budget | Core fit — the house genre |
| Perception + planning + control integrated and evaluated end to end | Core fit |
| A single foundational theorem or model, science-first, best with rebuttal | Better served at RSS |
| A learning algorithm whose novelty carries the paper, robot as testbed | Better served at CoRL |
| A polished demo with no trials, resets, or failure analysis | Not yet IROS-shaped — build evidence |
| Journal-length exposition or need for revision cycles | RA-L or T-RO, then transfer to present |

## Vignette: where a legged-locomotion project goes

A project delivers a controller that keeps a quadruped upright on loose gravel, on the robot, with trial
counts and a failure taxonomy. IROS reading: strong fit — an integrated system meeting a terrain
constraint with embodied evidence. Strip the hardware and keep only a simulation policy-learning result,
and it drifts toward CoRL; distill it to one provable stability claim wanting single-track scrutiny, and
RSS becomes the better home; grow it into a journal-length treatment with revisions, and RA-L or T-RO
fits, after which the transfer window can still put it on an IROS stage.

## Sharpening moves before committing

- Name the **embodiment constraint** the system respects — onboard compute, power budget, sensor noise,
  contact uncertainty, or real-time latency. If nothing physical constrains the design, the IROS framing
  is thin.
- Confirm the argument fits the **body alone**: IROS has no supplementary PDF, so a system that only
  makes sense with an appendix is mis-sized.
- Verify you can produce **embodied evidence** — real trials, resets, failures, and a stated sim-to-real
  gap — not just a curve or a single hero run.
- Robotics program emphasis drifts between cycles and cities; scan the current CFP topic list before
  final routing.

```text
Quick router:
  system on real hardware under a physical constraint? ---> IROS (or ICRA by season)
  single foundational science claim, wants rebuttal? ----> RSS
  the learning method is the contribution? -------------> CoRL
  wants journal review + revisions? --------------------> RA-L / T-RO (then transfer to present)
```

## Output format

```text
[Fit] strong IROS / possible IROS / better elsewhere
[Best venue] IROS / ICRA / RSS / CoRL / RA-L / T-RO / HRI / CASE / other
[System sentence] <one sentence naming the integrated system>
[Embodiment constraint] <compute / power / latency / contact / sensing>
[Top rejection risk] <evidence / integration / novelty / scope>
[Next action] <build evidence, reframe, or switch venue>
```
