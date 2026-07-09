---
name: hri-workflow
description: Use to plan an ACM/IEEE HRI campaign backward from the full-paper deadline through the abstract-then-paper two-step, the rebuttal, the program-committee meeting, camera-ready, and the March conference, coordinating the parallel alt.HRI, Late-Breaking Reports, video, and Student Design deadlines.
---

# HRI Workflow

HRI runs an **annual** cycle that lands the conference in **March**, with the full-paper deadline the
previous **early fall**. The trap is that the study — a human-subjects study of an embodied robot —
takes far longer than the writing, and IRB approval plus participant recruiting cannot be
compressed in the final weeks. Plan backward from the deadline and start the study early. Dates
below are the **HRI 2026** cycle (see `resources/official-source-map.md`); HRI 2027 (Santa Clara,
8-12 Mar 2027) is the live next target — reopen its call for exact dates.

## The cycle, backward from the deadline

- **Abstract deadline (HRI 2026: 22 Sep 2025, AoE)** — mandatory for *every* full paper, about a
  week before the paper. Locks title, authors, abstract, and track. No abstract → no paper slot.
- **Full-paper deadline (HRI 2026: 30 Sep 2025, AoE)** — the anonymized 8-page PDF plus supplement
  and video, via **PCS**.
- **Reviews + rebuttal (HRI 2026: rebuttal ~12 Nov 2025, AoE)** — you receive reviews from three
  externals (mediated by a 1AC/2AC) and write one rebuttal. See `hri-author-response`.
- **Discussion + PC meeting (Nov-Dec)** — reviewers discuss online; the program committee meets and
  makes decisions. Some venues use light shepherding/conditional acceptance (**待核实** per cycle).
- **Decisions (HRI 2026: December 2025)**.
- **Camera-ready (HRI 2026: ~9-12 Jan 2026)** — de-anonymize, complete ACM+IEEE metadata, finalize
  the video. See `hri-camera-ready`.
- **Conference (HRI 2026: 16-19 Mar 2026, Edinburgh)** — at least one author registers and presents.

Everything after the deadline is short and fixed; only the **pre-deadline study window** is yours to
manage — so protect it.

## Backward planning that actually matters

Count backward from the **paper deadline**, not the abstract:

| Work item | Start before deadline | Why it cannot be compressed |
| --- | --- | --- |
| IRB/ethics approval | 8-12+ weeks | Review boards have their own queues; no data collection without it |
| Study design + pilot | 8-10 weeks | A design flaw found after data collection is unfixable |
| Participant recruiting + running | 4-8 weeks | Recruiting real people to interact with a robot is slow; robots break |
| Analysis + effect sizes | 2-3 weeks | Pre-registered analysis, not p-hunting after the fact |
| Writing + video editing | 3-4 weeks | The video is a real artifact, not an afterthought |
| Anonymization sweep | final week | On the *final* PDF, data, and video — see `hri-submission` |

If IRB and recruiting will not finish in time, the honest move is **Late-Breaking Reports** this
cycle and a full paper next — not a rushed study.

## Parallel tracks and their own deadlines

HRI is a multi-track conference; the full paper is one lane. For the 2026 cycle:

- **alt.HRI (17 Oct 2025)** — bold/unconventional full-length work; separate call, companion
  proceedings.
- **Late-Breaking Reports (8 Dec 2025)** — 2-4 pages, early-stage; a good newcomer entry and a home
  for a study that is not yet full-paper-complete.
- **Interactivity / Videos & Demos (8 Dec 2025)** — a live demo or video of an interactive system.
- **Student Design Competition (8 Dec 2025)** — themed design challenge; at least one author
  registers.
- **Workshops & Tutorials + HRI Pioneers** — proposals and applications run on their own earlier
  timelines; Pioneers is a doctoral-consortium-style workshop held the first day.

Decide up front which lanes you are entering; a study can seed both a full paper (this cycle or
next) and a demo/video.

## Decision branches after notification

- **Accept** → `hri-camera-ready`; finalize video and ACM+IEEE metadata; register a presenter.
- **Accept with shepherding / conditional** (if the edition uses it) → make the required changes and
  clear them with the shepherd before camera-ready (**待核实** whether the cycle uses this).
- **Reject** → re-route with `hri-topic-selection` (RO-MAN, THRI, next HRI, or CHI), reuse the study,
  and mine the reviews for the resubmission. HRI has no in-cycle major-revision round — a reject is
  a reject for that edition.

## Reverify each cycle

- The exact dates, and whether the abstract-then-paper two-step and its one-week gap persist.
- Whether the edition uses shepherding/conditional acceptance.
- The short-track deadlines (they sometimes move independently of the full-paper date).
- The camera-ready date and whether separate ACM/IEEE author kits apply.

## Output format

```text
[Target edition] HRI <year> (<city>) — full-paper deadline <date>
[Abstract locked] title/authors/track by the earlier abstract deadline? yes/no
[Study readiness] IRB approved? data collected? analysis pre-registered?
[Critical path] <item blocking the deadline> — start-by date
[Parallel lanes] alt.HRI / LBR / video / Student Design — in or out
[Post-decision] camera-ready date · presenter registered · reroute plan if rejected
```
