> **Illustrative teaching example.** The system, hardware, numbers, and citations below are
> **fictional**, invented only to demonstrate UIST house style; no real-paper facts or venue
> policies are asserted here. Corresponding skills:
> [`uist-writing-style`](../../skills/uist-writing-style/SKILL.md),
> [`uist-topic-selection`](../../skills/uist-topic-selection/SKILL.md),
> [`uist-experiments`](../../skills/uist-experiments/SKILL.md), and
> [`uist-supplementary`](../../skills/uist-supplementary/SKILL.md).

# Worked Example: A UIST-Style Abstract + Introduction (before → after)

The exercise: the same fictional project — a self-calibrating electrotactile display woven
into an off-the-shelf glove — written first as the kind of draft UIST reviewers reject
without malice, then rewritten to the venue's systems rhetoric: **artifact on page one,
capability claims with measurement conditions, mechanism named early, evaluation matched to
claim, and a video the text is synchronized with**.

**Fictional paper:** *"WeftHaptics: Self-Calibrating Electrotactile Feedback in Unmodified
Textile Gloves."*

---

## Before (reads like a motivation essay — typical UIST reject shape)

> **Abstract.** Haptic feedback is increasingly important for virtual reality and wearable
> computing. However, existing haptic devices are often bulky, expensive, or uncomfortable.
> In this paper, we explore how textile-based interfaces can provide rich tactile
> sensations. We present a novel glove-based system and report on a user study showing that
> participants found the sensations realistic and enjoyable. Our findings have implications
> for the design of future wearable haptic interfaces.
>
> **Introduction.** Touch is one of the most important human senses. Researchers have long
> sought to recreate tactile sensations... [three paragraphs on the history of haptics]
> ...To address these challenges, we designed a glove that can display tactile sensations.
> We conducted a study with 12 participants who rated the experience positively. In the
> following sections we review related work, describe our design process, present our
> study, and discuss implications for design.

**Why this fails the UIST read** (the diagnosis, per skill):

- **No artifact until late, and no mechanism ever** — "explore," "novel glove-based
  system," "designed a glove": a reviewer cannot say what was built or why it required
  invention (`uist-writing-style`: artifact-first pass fails on page 1).
- **No capability claim** — nothing states what becomes possible that was not; the
  artifact-subtraction test leaves a preference study, which routes to CHI
  (`uist-topic-selection`).
- **Evaluation mismatched** — "rated the experience positively" is a ritual study; the
  claim a haptics *device* must carry is psychophysical and technical
  (`uist-experiments`).
- **No numbers with conditions** — bulky/expensive/uncomfortable are asserted about prior
  work without a comparison dimension; nothing about the new system is measured.
- **Implications-for-design ending** — an empirical-venue cadence, telling UIST reviewers
  the authors wrote for the wrong jury.

---

## After (UIST arc: capability → mechanism → numbers → breadth)

> **Abstract.** Electrotactile displays can render texture and contact cues without motors,
> but they require per-user, per-session calibration by an experimenter, which has kept
> them out of consumer form factors. We present **WeftHaptics**, an electrotactile display
> that runs in an **unmodified conductive-thread glove** and **calibrates itself**: a
> 40 ms impedance sweep at don time sets per-electrode current limits, and a closed-loop
> controller re-fits them continuously as skin conditions drift. The system renders
> 3 mm-resolution tactile patterns across the palmar surface using the glove's existing
> weave as the electrode array. Self-calibration matches experimenter calibration within
> 8% on perceived-intensity constancy (n = 16, magnitude estimation), and sensation
> quality holds across a 45-minute session as hands warm and sweat (drift study, n = 12).
> We demonstrate breadth with three applications — VR object handoff, non-visual
> navigation, and a texture-authoring tool — and release firmware, controller, and the
> calibration protocol.
>
> **Introduction.** *(¶1 — the capability gap, stated as engineering.)* Electrotactile
> stimulation renders tactile cues with no moving parts, yet forty years after its first
> demonstrations it still ships nowhere. The blocker is calibration: comfortable and
> perceivable current bands vary per user, per electrode site, and per minute as skin
> impedance drifts, so existing systems park an experimenter in the loop. A textile
> electrotactile display that **calibrates itself** would remove the last human from that
> loop — that is the artifact this paper contributes.
>
> *(¶2 — the mechanism, named immediately.)* WeftHaptics treats the glove's conductive
> weave as both display and sensor. At don time, a 40 ms sweep measures the impedance of
> all 42 thread-crossing electrodes; a per-site model maps impedance to safe, perceivable
> current bands. During use, the controller interleaves 1 kHz stimulation frames with
> sensing frames, re-fitting the model as impedance drifts — calibration becomes a
> property of the drive electronics rather than a procedure.
>
> *(¶3 — claims, each with its evidence address.)* We claim three things. First,
> self-calibration is as good as the human it replaces: within 8% of
> experimenter-calibrated perceived-intensity constancy in a 16-participant magnitude
> estimation study (Sec 7.1). Second, it holds up over time: sensation quality is stable
> across 45-minute sessions under thermal and moisture drift (Sec 7.2), where a
> fixed-calibration baseline degrades measurably. Third, the approach fits unmodified
> commodity gloves: we characterize rendering resolution and latency (3 mm; 11 ms
> frame-to-skin, Sec 6.3) on two off-the-shelf glove models.
>
> *(¶4 — breadth and reuse.)* Three applications exercise the design space — bimanual
> object handoff in VR, eyes-free pedestrian navigation, and an authoring tool with which
> two tactile designers built novel textures in under an hour (Sec 8). Firmware, the
> controller, and the calibration protocol are released for replication (Sec 9; video
> figure shows all three applications running live).
>
> *(¶5 — one-sentence roadmap, no tour.)* Section 2 positions WeftHaptics against
> motor-based wearables and prior electrotactile arrays; Sections 4-6 give the design,
> hardware, and controller; Sections 7-8 evaluate and demonstrate.

---

## What changed, mapped to the skills

| Move | Before | After | Skill |
| --- | --- | --- | --- |
| Artifact on page one | "we explore textile interfaces" | Named system + form factor + mechanism in the abstract | `uist-writing-style` |
| Capability framing | "rich tactile sensations" | "removes the experimenter from the calibration loop" | `uist-topic-selection` |
| Evidence match | 12 people "rated positively" | Psychophysics vs the replaced human + drift study + technical characterization | `uist-experiments` |
| Numbers carry conditions | none | 8% constancy (n = 16, magnitude estimation); 11 ms frame-to-skin | `uist-writing-style` |
| Breadth as evidence | absent | Three applications + authoring-tool session | `uist-experiments` |
| Video synchronization | video unmentioned | Text points at the video's live demonstrations | `uist-supplementary` |
| Reuse posture | "implications for design" | Firmware + protocol released for replication | `uist-artifact-evaluation` |

> Next: benchmark this arc against the real, DL-verified papers in
> [`../exemplars/library.md`](../exemplars/library.md) — every Lasting Impact winner there
> executes the capability → mechanism → evidence ladder on its first page — and check
> current cycle rules in [`../official-source-map.md`](../official-source-map.md).
