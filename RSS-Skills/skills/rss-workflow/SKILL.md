---
name: rss-workflow
description: Use when planning an RSS (Robotics: Science and Systems) campaign end to end — the late-January abstract/paper/supplement cascade, the invited-rebuttal window, late-April decisions, July conference week — and when placing RSS inside the year-round ICRA/IROS/RSS/CoRL robotics deadline calendar.
---

# RSS Workflow

Project-manage an RSS submission against its real calendar. Anchor every date to the
current edition's pages; the 2026 dates below are a verified historical snapshot
(source map rows 1-3, checked 2026-07-08), not a promise about 2027.

## Where the cycle stands right now (as of 2026-07-08)

- RSS 2026 (22nd edition, Sydney: UTS + ICC) runs **July 13-17, 2026** — conference
  week starts in days. The submission funnel (abstract Jan 23 → paper Jan 30 →
  supplement Feb 6 → invited rebuttal Apr 3 → decisions Apr 27, all AoE) is closed.
- Accepted authors are in final-presentation mode: talk, poster, travel, and artifact
  release (`rss-camera-ready`, `rss-artifact-evaluation`).
- Everyone else is planning **RSS 2027**, whose site, dates, and deadlines were
  unposted at check time (待核实). The recent pattern — late-January deadline, July
  conference — is a planning hypothesis only.

## The robotics year, seen from RSS

RSS shares its authors with three siblings, so choosing RSS is also choosing a slot in
an annual rotation. Approximate recent geometry (verify each venue's live pages):

| Venue | Typical deadline | Typical event | What slipping past RSS costs |
|---|---|---|---|
| RSS | late January | July | Next comparable single-track slot is a full year away |
| IROS | ~March | ~October | Natural catch for a paper 6 weeks short of RSS-ready |
| CoRL | ~June | ~November | Right jury if the learning story dominates |
| ICRA | ~September | ~May/June | Broadest program; absorbs systems breadth |

The practical use: a project that misses the January bar honestly should aim at IROS
or CoRL rather than submit thin — RSS's selectivity makes weak submissions expensive
in reviewer goodwill.

## Backward plan to a late-January deadline

| Weeks out | Milestone for a claim-plus-hardware paper |
|---|---|
| 12+ | Scientific claim fixed in one sentence; evidence plan sized to it |
| 10 | Hardware trial campaign running; failure attribution logged from day one |
| 6 | Ablations that isolate the mechanism complete |
| 4 | Full draft; supplement storyboard; internal red-team read |
| 2 | Anonymity sweep of PDF and media; OpenReview metadata entered |
| 1 | Abstract registered; buffer for robot downtime already spent |
| 0 | Paper in; supplement due one week later — do not design it that week, only pack it |

The one-week paper→supplement gap (2026: Jan 30 → Feb 6) is packing time, not filming
time; footage shot after the deadline cannot support claims already frozen in the PDF.

## Conference-week execution (the stage that is live right now)

For teams presenting at the current edition, the final week has its own checklist:

- Confirm the talk slot, format, and timing against the official program page; a
  single-track schedule has no parallel-session slack for overruns.
- Load footage locally; conference-venue networks are not a playback plan.
- Push the public artifact release live *before* the talk — the single-track
  audience is the largest referral event the repository will ever get
  (`rss-artifact-evaluation`).
- Prepare the poster to carry the evidence detail (trial counts, failure
  distribution) that the talk compresses away.
- Assign one author to note every hallway objection; those are free previews of the
  journal-extension reviews.

## RSS 2027 monitoring plan

Nothing about 2027 was posted at check time. Watch these, in this order, starting
early autumn 2026:

1. https://roboticsconference.org/ — the banner rebinds to the new edition.
2. The RSS Foundation calendar page (roboticsfoundation.org).
3. The OpenReview venue namespace for a `RSS/2027` group appearing.
4. The CFP page for the new deadline cascade and any format change — the 8-page
   ceiling and the two-stage rebuttal are both cycle policies, not fixtures.

## Stage-specific traps

- **February-March silence:** first reviews are not public-scheduled; do not plan
  team availability assuming a known release date (待核实 each cycle).
- **The rebuttal is conditional:** only papers above a first-round threshold are
  invited to respond. Plan an April window in calendars *without* assuming it will be
  used (`rss-author-response`).
- **April 27 → July is short:** visa lead times for the host country can exceed the
  decision-to-conference gap; start paperwork at submission time for likely-accept
  projects.
- **No standing editors:** the Program Chair and Area Chairs rotate per edition (2026
  PC chair: Matei Ciocarlie, Columbia — verified 2026-07-08); never carry a name or a
  policy across cycles.

## Ownership map for a multi-person campaign

Robotics submissions fail at handoffs; name owners early:

| Workstream | Single owner for |
|---|---|
| Claim custody | The one-sentence claim; vetoes scope drift in any section |
| Trial campaign | Protocol document, ledger integrity, daily campaign log |
| Media | Footage banking from every session; the supplement cut |
| Anonymity | The sweep across PDF, video, archive, and OpenReview fields |
| Deadline mechanics | AoE conversions, form fields, upload confirmations |

Footage banking deserves emphasis: clips must be captured *during* the campaign,
because the supplement freezes one week after the paper and reshoots after the
paper deadline cannot support frozen claims.

## Output format

```text
[Cycle position] planning 2027 / drafting / submitted / rebuttal window / accepted / conference week
[Next hard date] <date + source URL, or 待核实>
[Critical path] <three tasks gating the next stage>
[Fallback venue] IROS / CoRL / ICRA + trigger condition
[Calendar risks] <robot downtime / visa / footage / rebuttal availability>
```
