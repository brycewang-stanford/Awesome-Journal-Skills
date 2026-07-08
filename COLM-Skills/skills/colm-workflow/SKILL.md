---
name: colm-workflow
description: Use when planning a COLM submission campaign across the calendar — working backward from the late-March abstract and paper deadlines through the May-June rebuttal, July decisions, August camera-ready, and October conference, coordinating co-authors, compute, and reciprocal-reviewing duties, and slotting COLM into a multi-venue LM-research pipeline.
---

# COLM Workflow

COLM gives you exactly one shot per year: one deadline (late March in 2026), one
rebuttal, one decision (early July), one October stage. Campaign planning is
therefore mostly *backward induction from March* — and, because LM projects burn
compute and involve many hands, the critical path is usually GPUs and co-author
availability, not writing.

## The 2026 cycle as a template (all dates verified 2026-07-08)

| Date (2026) | Event | What must already be true |
|---|---|---|
| February | OpenReview opens | Profiles current for every author |
| March 26 | Abstract deadline | Real abstract; reciprocal reviewer chosen |
| March 31 | Full paper deadline | Frozen claims, pinned evidence, anonymized package |
| May 22 | Reviews released | Response owners pre-assigned; cache warm |
| May 22 - June 8 | Rebuttal | ~18 days; plan in `colm-author-response` |
| July 8 | Decisions | Both branches pre-planned |
| August 7 | Camera-ready | Public artifacts ready to ship simultaneously |
| October 6-9 | Conference, San Francisco | Presenter, visa, poster all handled |

**Live-phase note:** on this pack's access date — 2026-07-08 — the 2026 cycle is at
decision day. If that is you, jump to `colm-camera-ready` or the reject branch in
`colm-review-process`. If you are planning fresh work, you are planning **COLM
2027**: dates unannounced (待核实), with late March the reasonable working
assumption to be corrected the moment `colmweb.org` posts the real calendar.

## Backward plan from a March deadline

```text
T-20w (Nov)  route the project (colm-topic-selection); if COLM, freeze the
             one-sentence finding and the evaluation design — contamination
             handling decided NOW, not retrofitted (colm-experiments)
T-16w (Dec)  compute budget locked: training runs, eval sweeps, API spend;
             book cluster time — March demand is when everyone else trains too
T-12w (Jan)  main experiments running; pinning discipline live from day one
             (colm-reproducibility); related-work lanes assigned (colm-related-work)
T-8w  (Feb)  full draft v1; internal red-team review against the four attacks;
             OpenReview profiles + reciprocal-reviewer map done when the venue opens
T-4w  (Mar)  freeze claims; kill or hedge anything unverified; build the
             anonymized package (colm-supplementary)
T-1w         abstract in (Mar 26); mechanical sweeps; co-author policy items
T-0   (Mar 31) upload; re-download; read cold
```

Two LM-specific scheduling truths: **evaluation takes as long as training** once
you include prompt-sensitivity runs, multiple families, and CI-grade sampling —
budget it explicitly; and **the February cluster crunch is real** — every LM group
targets the same spring deadlines, so compute reserved in December is worth double
compute begged for in March.

## Coordination artifacts for a multi-author LM paper

- **A claims ledger** — every claim, its owner, its evidence status
  (verified / running / at-risk). The T-4w freeze operates on this ledger.
- **A reciprocal-reviewing map** — who is nominated for which submission across
  the *whole group's* March portfolio; the same person cannot cover two papers,
  and anyone on 4+ submissions is drafted into the pool regardless.
- **A policy checklist per co-author** — OpenReview profile, Code of Ethics
  acknowledgment, LLM-usage disclosure input. These are the tasks only their
  owners can do, which is what makes them deadline risks.
- **A decision-tree memo** written before July: if accept → who runs camera-ready
  and the artifact release in the August-vacation month; if reject → target venue
  (autumn ICLR? next NeurIPS? COLM 2027?) and which review criticisms gate the
  resubmission.

## Slotting COLM into the venue year

COLM's March deadline sits after the ICLR decision (winter) and before the NeurIPS
deadline (spring), which creates the standard LM-group rotation: ICLR reject →
strengthen → COLM; COLM reject (July) → strengthen → ICLR (autumn). Use the
rotation deliberately, with `colm-topic-selection` as the gate each time — a paper
bouncing between venues unchanged is not a strategy, it is a queue.

## The small-lab variant

The plan above assumes a group; a two-person or advisor-student team runs the same
calendar with different bottlenecks:

| Constraint | Adaptation |
|---|---|
| No compute reserve | Anchor claims on open-weight models small enough to rerun; design the paper so API spend is evaluation-only and capped |
| One person does everything | The T-4w claim freeze becomes T-6w; the last month is writing and packaging only |
| No internal red team | Trade cold reads with a neighboring group in February — the four-attacks review (`colm-experiments`) does not require seniority, only distance |
| Advisor bandwidth | Book the advisor's full-draft read for a named week in February; "when it's ready" means March 29 |
| Single submission | Reciprocal-reviewing is simpler (one nominee) but the 4+ auto-draft rule may still catch a prolific advisor — check |

The compensating advantage: small teams pivot. If January experiments kill the
framing, a two-person team can re-route to a workshop or the autumn cycle without
a committee meeting — take that exit deliberately rather than limping to March.

## Failure patterns this calendar produces

- Evaluation designed after training finishes → contamination handling becomes an
  apology instead of a design (start it at T-20w).
- Abstract stub on March 26 → bad reviewer matching that no rebuttal can fix.
- Rebuttal window discovered at review-release → the 18 days start with three days
  of panic; pre-assign owners in March.
- August camera-ready month colliding with vacations → name the owner in July.

## Workshop track as a parallel lane

COLM's workshop day (October 9 in 2026) runs its own later calendar — in 2026,
workshop proposals were due April 14, and contributed workshop papers had a
suggested June 23 deadline with mandatory notification by July 24. For work that
misses March or is not archival-ready, the workshop lane keeps the project inside
the COLM community's October gathering without burning the main-track shot — and a
workshop audience in October is the best red team a March 2027 main-track version
will ever get. Check each workshop's own pages; their deadlines and archival
status vary (待核实 per workshop).

## Output format

```text
[Target cycle] COLM 202X — deadline <confirmed / working assumption 待核实>
[Phase now] <planning / experiments / freeze / submitted / rebuttal / decision / camera-ready>
[Critical path] <compute / evaluation / writing / co-author policy items>
[Ledger health] claims verified <k>/<n>; at-risk: <items>
[Group constraints] reciprocal map ▢  4+-submission authors: <names>
[Next milestone] <date — what must be true>
```
