# HRI Exemplars Library (contribution shape × track × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** (`db/conf/hri`) and the **ACM Digital Library / IEEE Xplore** to confirm it appeared at
> the **ACM/IEEE International Conference on Human-Robot Interaction (HRI)** — matching title,
> author list, year, and venue string — rather than at a sibling conference (CHI, ICRA, IROS,
> RO-MAN, HAI) or in a journal (**THRI**, **JHRI**, **IJSR**). Papers that could not be cleanly
> confirmed as an HRI *conference* placement were **omitted and documented below**. It is
> deliberately a short, verified list (4 verified > 15 guessed).
>
> **Sibling-confusion guard:** HRI (the conference) is **not** CHI, **not** ICRA/IROS, **not**
> RO-MAN, and **not** the THRI/JHRI/IJSR journals. Several canonical HRI *ideas* were published in
> those journals, not in the conference proceedings (see omissions). A famous robot, a familiar
> scale, or a well-known author does **not** prove an HRI-conference placement.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, effect sizes, or table numbers — read the original on ACM DL / IEEE
> Xplore before citing anything. For HRI-specific policy, tracks, and the review model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × track × method** is closest to yours, then study how
that paper (1) poses a **human-robot-interaction question a broad, interdisciplinary audience
recognizes**, (2) backs it with a **defensible study of an embodied robot** whose evidence is
proportional to the claim, and (3) is honest about its **limitations and generality** — the HRI
bar (see [`../../skills/hri-writing-style/SKILL.md`](../../skills/hri-writing-style/SKILL.md),
[`../../skills/hri-topic-selection/SKILL.md`](../../skills/hri-topic-selection/SKILL.md), and
[`../../skills/hri-experiments/SKILL.md`](../../skills/hri-experiments/SKILL.md)). For each, ask the
self-check question before claiming your paper is "HRI-shaped," and note which of the five tracks
(User Studies / Technical / Design / Theory and Methods / Systems) it would enter.

Two rows are HRI **Best Paper** honorees, so they also model what "the community's highest bar"
looks like at this venue.

---

## By contribution shape

### User study — trust / safety (User Studies track)

- **Robinette, Li, Allen, Howard & Wagner, "Overtrust of Robots in Emergency Evacuation
  Scenarios," HRI 2016 (11th ACM/IEEE HRI).** Verified: dblp `rec/conf/hri/RobinetteLAHW16`;
  widely recognized as an HRI 2016 Best Paper. A controlled study in which participants chose
  whether to follow a robot's guidance during a simulated emergency, including after seeing the
  robot perform poorly.
  - **Why it is an exemplar:** it asks a crisp behavioral question — *do people over-trust a robot
    when it matters?* — and answers it with a **staged, embodied study** and a real behavioral
    outcome (following vs. not), not a questionnaire proxy. The finding travels beyond one robot.
  - **Self-check:** does your study measure what a person actually *does* with the robot (behavior),
    with a design that isolates the manipulation, rather than only what they *say* on a scale?

### User study — social interaction / proxemics (User Studies track)

- **Mumm & Mutlu, "Human-Robot Proxemics: Physical and Psychological Distancing in Human-Robot
  Interaction," HRI 2011 (6th ACM/IEEE HRI).** Verified: HRI 2011 Best Paper (official 2011
  best-paper listing) / dblp. A controlled study of how a robot's gaze and likability shape the
  physical and psychological distance people keep from it.
  - **Why it is an exemplar:** it operationalizes a **theory-grounded construct** (proxemics) into
    measurable robot manipulations and human responses, connecting a social-science idea to an
    embodied HRI design — exactly the interdisciplinary move HRI prizes.
  - **Self-check:** is your independent variable a manipulation of the *robot's behavior*, and are
    your dependent variables measures a psychologist would recognize as valid?

### Technique + behavioral evaluation — designed robot behavior (Technical track)

- **Mutlu, Shiwa, Kanda, Ishiguro & Hagita, "Footing in Human-Robot Conversations: How Robots Might
  Shape Participant Roles Using Gaze Cues," HRI 2009 (4th ACM/IEEE HRI), pp. 61-68.** Verified:
  dblp / ACM DL (Proc. 4th ACM/IEEE HRI). Designs robot **gaze behaviors** grounded in Goffman's
  footing and evaluates whether they shape people's conversational roles.
  - **Why it is an exemplar:** the contribution is a **designed, generative behavior** (gaze cues
    that assign participant roles) *plus* a study showing it works on people — a technical/
    behavioral contribution whose value is demonstrated through human response, not component
    metrics alone.
  - **Self-check:** is your robot behavior derived from a principle (not ad hoc), and does the
    evaluation show its *effect on people*, so the lesson survives a change of platform?

### Interaction design — fluent collaboration (Design track)

- **Cakmak, Srinivasa, Lee, Kiesler & Forlizzi, "Using Spatial and Temporal Contrast for Fluent
  Robot-Human Hand-overs," HRI 2011 (6th ACM/IEEE HRI).** Verified: dblp / ACM DL. Studies how a
  robot should present an object so a person takes it fluently, combining design insight with
  human evaluation.
  - **Why it is an exemplar:** it treats **the interaction itself as the design object** — the
    handover — and shows, with people, which spatial/temporal cues make it fluent. A design-track
    contribution that is empirical without being a bare user study.
  - **Self-check:** is your contribution a *designed interaction* whose merit is demonstrated in
    how smoothly real people engage with it, and would a video make the improvement legible?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Track | Verified HRI exemplar | Edition |
| --- | --- | --- | --- |
| Behavioral user study (trust) | User Studies | Robinette et al., "Overtrust of Robots..." | HRI 2016 |
| Social user study (proxemics) | User Studies | Mumm & Mutlu, "Human-Robot Proxemics" | HRI 2011 |
| Designed behavior + evaluation | Technical | Mutlu et al., "Footing in Human-Robot Conversations" | HRI 2009 |
| Fluent interaction design | Design | Cakmak et al., "...Fluent Robot-Human Hand-overs" | HRI 2011 |

> Four verified papers across three of the five tracks. **Theory and Methods** and **Systems** are
> intentionally left without a placeholder row: rather than guess, find your own verified exemplar
> with the recipe below (a Theory/Methods exemplar reframes how the field measures or conceptualizes
> HRI; a Systems exemplar integrates components into a robot that achieves a new interactive
> capability, evaluated at the system level).

---

## Omitted for lack of clean HRI-*conference* verification (do not attribute to HRI without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the journal-vs-conference confusions the header warns about:

- **Riek, "Wizard of Oz Studies in HRI: A Systematic Review and New Reporting Guidelines"** —
  verified to be the **Journal of Human-Robot Interaction (JHRI)**, *not* the HRI conference. A
  methodological touchstone this pack cites in `hri-experiments`, but as a **journal** work.
- **Bartneck et al., the "Godspeed" questionnaire series** — published in the **International
  Journal of Social Robotics (IJSR)**, not the HRI conference. Widely used *at* HRI, but not an
  HRI-proceedings paper.
- **Strabala et al., "Toward Seamless Human-Robot Handovers"** — appeared in **JHRI (2013)**, a
  journal; do not conflate it with conference handover papers such as Cakmak et al. (HRI 2011).
- **Salem et al., "To Err is Human(-like)..."** — appeared in **IJSR**, a journal, not the HRI
  conference. A direct journal-vs-conference trap; listed only as a guardrail.

Before adding any paper, confirm it on **dblp** (`db/conf/hri`) and **ACM DL / IEEE Xplore** by
matching the venue string to an **HRI conference edition** (not CHI, ICRA, IROS, RO-MAN, HAI, or a
THRI/JHRI/IJSR journal), then record authors, year, and DOI/pages, note the likely track, and
update the access-date header. When in doubt, omit. If web search is unavailable, add the row as
**待核实 / TO VERIFY** with **no attribution**.
