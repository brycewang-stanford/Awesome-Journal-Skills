---
name: hri-topic-selection
description: Use when deciding whether a human-robot-interaction project belongs at the ACM/IEEE HRI conference versus CHI, ICRA/IROS, RO-MAN, CoRL, HAI, or the THRI/JHRI journals, and then which of HRI's five full-paper tracks (User Studies, Technical, Design, Theory and Methods, Systems) it should enter, using the robot-embodiment and human-in-the-loop tests and the HRI calendar.
---

# HRI Topic Selection

Two decisions precede everything else: **is this an HRI paper at all**, and **which of the five
tracks** does it enter. HRI is the flagship *interdisciplinary* venue for human-robot interaction —
it uniquely rewards work that sits *between* robotics, HCI, psychology, and design. Getting the
venue and track right is the highest-leverage move an author makes, because HRI judges each paper
by the contribution type of its chosen track. Facts below were read from the HRI 2026/2027 calls on
2026-07-09 (see `resources/official-source-map.md`); reopen the live call before deciding.

## The two gating tests

Apply both. HRI wants **a person and a robot interacting**.

1. **Robot-embodiment test.** Is there a robot — a physical or virtual *embodied* agent — that is
   central to the study? If the "robot" is really a chatbot, a screen widget, or a disembodied voice
   assistant with no embodiment, the interaction lessons usually belong at **CHI** or a dialogue
   venue, not HRI.
2. **Human-in-the-loop test.** Is a *person* interacting with the robot, and is the paper's claim
   about that interaction? If the contribution is autonomy, control, perception, or learning
   evaluated **without a human** (benchmarks, trajectories, success rates), it belongs at
   **ICRA/IROS/CoRL**, even if the long-term motivation is human-facing.

Pass both and you are plausibly at HRI. Fail the first → CHI (or a design/AI venue). Fail the
second → a robotics/learning venue. Pass both but the human is incidental → reconsider whether the
human study is real or decorative.

## Route among the siblings

| If the core contribution is... | Prefer | Why not HRI |
| --- | --- | --- |
| Interaction with an embodied robot, evaluated with people | **HRI** | — |
| A general HCI/UI interaction with no robot embodiment | **CHI** | No robot; HRI requires embodiment |
| Robot autonomy/control/perception/learning, no human study | **ICRA / IROS / CoRL** | No human-in-the-loop; HRI wants the interaction |
| Robot-and-human *communication* with an engineering-comms framing | **RO-MAN** | RO-MAN overlaps; HRI is more selective and study-centric — a judgment call, decide by community fit |
| Human-*agent* interaction where the agent is not a robot | **HAI** | Embodiment/robot focus is weaker |
| A mature, extended study or synthesis better as an archival article | **THRI** (journal) | HRI is an 8-page conference paper, not a journal article |
| Early-stage result or new idea, not yet a full study | **HRI Late-Breaking Reports** | Full papers need a complete, defensible study |
| Bold, provocative, or unconventional work / methods | **HRI alt.HRI** | The main track expects standard rigor; alt.HRI invites the unorthodox |

The **RO-MAN vs HRI** and **CHI vs HRI** calls are the frequent ones. Decide RO-MAN/HRI by
selectivity and evidence culture (HRI leans harder on study design and effect sizes); decide
CHI/HRI by whether the robot's *embodiment* is doing real work in the interaction.

## Then pick the track (this is HRI-specific)

Full papers enter **exactly one** of five tracks, and are reviewed by the subcommittee matched to
that contribution type. Choose by **what your primary contribution is**, not by your topic:

- **User Studies** — new knowledge about human-robot interaction from a **study involving people**.
  The default home for empirical/behavioral work. Reproducibility studies also go here. Typically
  the largest track (and may be split into multiple subcommittees).
- **Technical** — the primary contribution is an **algorithm, model, or method**, best judged by
  component-level testing rather than a full system evaluation (e.g., a perception or behavior-
  generation method for interaction).
- **Design** — the contribution is a **designed interaction, artifact, or interface** for HRI, with
  design insight demonstrated (often with people, but the contribution is the design).
- **Theory and Methods** — the contribution advances the **conceptual foundations** of HRI or the
  **methods** by which we do HRI research (frameworks, measures, methodology).
- **Systems** — the contribution is an **integrated robotic system** achieving new interactive
  capability, evaluated at the **system level**.

Mismatch is costly: a design contribution shoved into User Studies will be marked down for a weak
study it never claimed to be. If two tracks fit, pick the one matching the contribution you most
want judged, and make that contribution unmistakable on the first page.

## The re-label test (does it survive as an HRI paper?)

Ask: *if I removed the robot, would the contribution survive?* If yes, it is probably a CHI/ML/
psychology paper wearing a robot costume. And: *if I removed the human study, would the contribution
survive?* If yes, it is probably an ICRA/IROS systems paper. An HRI paper is one where **both the
robot and the human interaction are load-bearing**.

## Calendar as a routing input

HRI runs an **annual** cycle with an early-fall full-paper deadline. For the 2026 cycle: **abstract
22 Sep 2025**, **paper 30 Sep 2025** (AoE); **alt.HRI 17 Oct 2025**; **LBR / video / Student Design
8 Dec 2025**; conference March. If the study will not be *complete and defensible* by the
full-paper deadline, the honest routes are **LBR** (early-stage) now and a full paper next cycle, or
a different venue — not a thin full-paper submission that a User Studies subcommittee will see
through.

## Output format

```text
[Venue decision] HRI / CHI / ICRA-IROS-CoRL / RO-MAN / HAI / THRI / other
[Both gating tests] robot embodiment: yes/no · human-in-the-loop: yes/no
[Re-label test] survives without robot? without human study? (both should be "no")
[Track] User Studies / Technical / Design / Theory and Methods / Systems — why
[If not HRI] recommended venue + reason
[Calendar fit] complete by the full-paper deadline? else LBR/alt.HRI/next cycle
```
