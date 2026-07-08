---
name: interspeech-review-process
description: Use when reasoning about how INTERSPEECH review actually works — area-based assignment inside ISCA's scientific program, multi-reviewer scoring and meta-review on CMT, what the rebuttal can and cannot move, oral/poster allocation, ISCA best student paper selection, and reading a decision letter for next-cycle strategy.
---

# INTERSPEECH Review Process

Interspeech reviews several thousand submissions a year through an area-structured
technical program committee, on a compressed spring schedule, with a single
decision date. Understanding the machine explains both the review you got and the
leverage you have. Mechanics are re-tuned annually by that year's Technical
Program Chairs — the 2026 shape below is a snapshot, not a constitution.

## The pipeline, 2026 shape

| Stage | 2026 anchor | Author-visible? |
|---|---|---|
| Submission + update window | 25 Feb / update to 4 Mar | yes |
| Area chairs assign reviewers within the chosen scientific area | Mar–Apr | no |
| Independent reviews written (typically 3+) | Apr | at release |
| Author rebuttal window | reported 24 Apr – 1 May (待核实) | yes |
| Meta-review / area consolidation | May | in decision |
| TPC acceptance meeting; program packing (oral vs poster) | May | no |
| Notification | 5 Jun | yes |
| Camera-ready | 19 Jun | yes |

The **area** is the unit of everything: your reviewers, your meta-reviewer, and
your competition for slots all come from the scientific area you selected at
submission. That is why area choice is a strategy decision, not a form field.

## What reviewers are scored on

ISCA-style review forms ask for judgments along familiar axes — novelty/relevance,
technical correctness, quality of evaluation, clarity, and reference coverage —
plus a listen to any audio. Exact form wording per cycle is 待核实; what is stable
is the community's calibration:

- "Not convincing" (evaluation too thin, no significance, wrong baseline) is the
  modal complaint — more than "not novel."
- Speech reviewers reward *scoped* claims verified carefully over broad claims
  verified loosely.
- Reference coverage includes the ISCA Archive lineage; missing the standard prior
  system from two Interspeechs ago is read as not knowing the field.

## What the rebuttal moves (and what it cannot)

Interspeech's rebuttal is young (introduced in recent cycles) and short. It
reliably fixes: factual misreadings, missed content in the dense 4 pages, and
protocol misunderstandings. It rarely fixes: taste, scope objections, or a
reviewer's judgment that the evidence bar was missed. Write for the meta-reviewer
who will arbitrate (see `interspeech-author-response`).

## Decisions and what they encode

- **Accept**: mode (oral/poster) arrives with scheduling, not with the decision;
  poster is a packing outcome, not a demotion — award-winning papers present as
  posters at this venue.
- **Reject**: the letter usually aggregates review themes. Decode for next cycle:
  evidence gap → fixable by `interspeech-experiments`; fit complaint → re-run
  `interspeech-topic-selection`; density complaint → the 4 pages were overstuffed,
  consider the Long Paper track or a journal.
- There is no conditional-accept limbo; the accept is real and the camera-ready
  window is administrative.

## Awards, for calibration not planning

ISCA confers **three Best Student Paper awards** at each Interspeech (selection
combines reviewing and on-site presentation; the first author must be a student —
verify current criteria), and the **ISCA Medal for Scientific Achievement** opens
the conference. Award papers are useful exemplars of the venue's taste — see
`resources/exemplars/library.md` — but optimizing a submission for awards is noise.

## Confidentiality and conduct

Reviews, scores, and CMT discussion are confidential; quoting them publicly
violates community norms. Reviewer duty flows the other way too — Interspeech
recruits heavily from the author pool, and reviewing a few papers well is how the
4-page machine stays alive.

## Reading your reviews: a 20-minute protocol

```text
1. Strip scores; list every distinct claim reviewers make about the paper.
2. Tag each: misreading / evidence gap / scope-taste / writing density.
3. Count how many trace to compression (answer existed but was crushed
   out of the 4 pages) — that fraction is your writing problem, not your
   research problem.
4. Identify what the meta-reviewer will likely weight: points echoed by
   2+ reviewers, or by the most expert one.
5. Choose the lane: rebut (this cycle) / revise (next cycle) / reroute.
```

## Calibrating expectations by phase

- **March–April (silence)**: normal. Reviewer assignment and writing are
  underway; there is nothing to check and nobody to email.
- **Late April (reviews/rebuttal, if run)**: the one author-input point of the
  spring. Missing a one-week window because nobody watched CMT is a wholly
  preventable failure — name the watcher at submission time.
- **May (silence again)**: meta-review and TPC consolidation; score changes here
  are invisible to you.
- **Early June**: decision. The same-week triage meeting matters because the
  camera-ready window is two weeks and registration pricing tiers are ticking.

## Scale, honestly stated

Interspeech operates at thousands-of-submissions scale with a large volunteer
reviewer pool, which explains the texture of the process: short reviews,
area-local calibration, no negotiation rounds, and a program committee that
packs a five-day, many-parallel-session program. Publicly posted acceptance
rates vary by edition and are not restated here (待核实 per cycle) — but the
planning implication is stable: the process is one-shot per year, so the
February version of the paper is the paper.

## Output format

```text
[Stage now] where in the pipeline, next visible event + date
[Review map] per-reviewer objection tags
[Meta-review prediction] <the consolidated one-liner you must change>
[Leverage] rebuttal-movable vs immovable points
[If rejected] revise-for-2027 / Long Paper / journal / reroute + rationale
```

2026 anchors were checked 2026-07-08 (rebuttal dates from secondary sources —
待核实); see `resources/official-source-map.md` for the trail.
