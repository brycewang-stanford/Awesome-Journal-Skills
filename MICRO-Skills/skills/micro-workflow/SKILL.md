---
name: micro-workflow
description: Use when planning a MICRO campaign end to end — the April-to-Athens 2026 cycle clock, the four-venue architecture calendar (MICRO/ISCA/HPCA/ASPLOS) seen from MICRO's October seat, resubmission lattices after each outcome, and starting the MICRO 2027 evaluation stack early enough to matter.
---

# MICRO Workflow

MICRO owns the **autumn slot** of computer architecture's four-venue year: an early
April deadline feeding an end-of-October symposium. Because the four sibling venues
interleave, a MICRO plan is really a lattice plan — every outcome has a next move
within roughly four months. Dates below verified 2026-07-08; every one is a
single-cycle snapshot.

## The 2026 cycle clock (59th edition, Athens)

```text
2026-03-31  abstract registration       11:59 PM EDT   hard gate
2026-04-07  full paper                  11:59 PM EDT   micro2026.hotcrp.com
2026-06-03 → 06-17  rebuttal/revision   two-week window (micro-author-response)
2026-07-07  notification
2026-09-11  camera-ready               (AE runs in parallel; micro-camera-ready)
2026-10-31 → 11-04  symposium, Athens, Greece
```

As of this pack's check date (2026-07-08), the 2026 cycle had **just issued
decisions** — the live work is camera-ready + AE for accepts, and lattice routing
for rejects. The next MICRO submission opportunity is the 2027 cycle, expected in
the same early-April position (待核实 when `microarch.org` posts it).

## The four-venue calendar from MICRO's seat

| Venue | Deadline (verified for cycle shown) | Conference | Use it when |
|---|---|---|---|
| **MICRO 2026** | Apr 7, 2026 (closed) | Oct 31–Nov 4, 2026, Athens | Mechanism-centric core work |
| HPCA 2027 | **July 24, 2026** | March 2027, Salt Lake City | Fastest next slot after a MICRO reject — 17 days after notification |
| ASPLOS 2027 | Sept 9, 2026 (2nd of two; Apr 15 passed) | April 2027, Crete | Reviews said "the interesting part is the software interaction" |
| ISCA 2027 | abstracts Nov 10 / papers **Nov 17, 2026** | June 2027, Atlanta | Four months of repair headroom; broadest architecture audience |
| MICRO 2027 | ~April 2027, 待核实 | autumn 2027 | Full-year rework or a new project |

The rhythm to internalize: **architecture deadlines cluster in April
(MICRO, ASPLOS-1st), July (HPCA), September (ASPLOS-2nd), and November (ISCA)** —
one submission window roughly every quarter. A healthy lab pipeline drafts against
the next two windows simultaneously.

## Backward plan for a MICRO 2027 submission

Working back from an assumed early-April 2027 deadline (verify the real date):

| When | Milestone | Owner risk |
|---|---|---|
| Aug–Sep 2026 | Mechanism sketch + `micro-topic-selection` gate; infrastructure choice (simulator, workloads) | Wrong venue discovered late |
| Oct–Nov 2026 | Baseline validated against published configs; characterization study done | Untuned baseline poisons all later data |
| Dec 2026 | Mechanism implemented in simulator; first end-to-end numbers | "It simulates" ≠ "it is modeled correctly" |
| Jan 2027 | Ablations + sensitivity sweeps; power/area modeling attached | Sweeps are compute-bound — queue early |
| Feb 2027 | Full draft; internal red-team review against `micro-writing-style` | Cost accounting missing |
| Mar 2027 | Freeze evaluation; `micro-reproducibility` manifests complete; format pass | Late "one more feature" restarts sweeps |
| T-7 days | Abstract registered in HotCRP | Missing the registration gate ends everything |
| T-0 | Upload (EDT arithmetic!) | See `micro-submission` |

The structural insight: in microarchitecture the **evaluation stack is the
schedule**. Simulator bring-up, trace generation, and multi-week sweep queues
dominate; prose is the cheap part. Any plan that allocates most of its calendar to
writing is mis-costed.

## Risk register for the compute-bound schedule

| Risk | Early symptom | Mitigation |
|---|---|---|
| Sweep queue starvation | Cluster contention in Feb–Mar (everyone's MICRO crunch) | Reserve allocation in January; keep `key`-tier configs that finish overnight |
| Baseline invalidated late | A simulator bugfix changes baseline IPC | Freeze simulator commit by January; batch fixes into one revalidation |
| Trace regeneration cascade | New compiler/flags after traces cut | Version traces; treat regeneration as a one-week line item, not a checkbox |
| Writing squeezed to two weeks | "Evaluation almost done" through February | Draft intro + mechanism sections in parallel with sweeps — they do not depend on final numbers |
| Deadline-week format panic | First full format pass happens at T-2 | Run the `micro-submission` gate table at T-14 and T-1 |

## Standing weekly cadence during a campaign

```text
Mon   queue review: sweeps finished / stalled / mis-configured; ledger updated
Wed   claims meeting: does yesterday's data still support the paper's sentences?
Fri   risk register walk (table above) + one live-page re-verification
      (deadline, CFP, HotCRP) logged with date — rules change between visits
```

## Outcome branches (July 7 has happened)

- **Accepted:** run `micro-camera-ready` and `micro-artifact-evaluation` as
  parallel tracks converging on September 11; book Athens logistics once
  attendance rules are confirmed (待核实 on `micro59/attend/`).
- **Rejected, methodology wounds:** the HPCA July 24 window is realistically only
  for papers whose fixes are textual; simulation repairs point at ISCA Nov 17.
- **Rejected, "not microarchitectural enough":** ASPLOS Sept 9 with a cross-layer
  reframe — see `micro-topic-selection` routing table.
- **Any branch:** archive reviews, update the results ledger, and file rebuttal
  promises as the next version's spec.

## Multi-paper pipelines and self-competition

Labs running more than one submission per cycle share one sweep queue and one set
of senior readers — schedule both explicitly:

- Stagger internal red-team reviews (`micro-writing-style` checklist) so the same
  professor is not reading two full drafts in deadline week.
- Deconflict topics in HotCRP if two submissions are adjacent; two papers from
  one lab splitting the same reviewer pool can drag each other down in
  double-blind bidding without anyone noticing until the reviews land.
- After notification, the lattice branches diverge per paper — keep one shared
  calendar of the four venues' gates (table above) so a July HPCA sprint for
  paper A does not silently consume the cluster paper B needs for its ISCA
  repairs.

## Output format

```text
[Today] <date> → position in cycle: <phase>
[Active gate] <next deadline, venue, days remaining, timezone stated>
[Lattice] plan A <venue+date> · plan B <venue+date> · trigger condition between them
[Evaluation-stack status] simulator / baseline / traces / sweeps: ready-blocked each
[Backward plan] next 3 milestones with dates and owners
[待核实] <dates assumed but not yet posted on live pages>
```
