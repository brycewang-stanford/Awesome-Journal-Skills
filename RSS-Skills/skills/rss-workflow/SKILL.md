---
name: rss-workflow
description: Use when planning an RSS (Robotics: Science and Systems) campaign end to end — the RSS 2027 two-stage calendar (December Extended Abstract, February rebuttal and Extension Charter, April final paper and decisions), July conference week — and when placing RSS inside the year-round ICRA/IROS/RSS/CoRL robotics deadline calendar.
---

# RSS Workflow

Project-manage an RSS submission against its real calendar. Anchor every date to the
current edition's pages; the dates below are the RSS 2027 calendar (source map rows 1-4,
read directly on 2026-11-24), with RSS 2026 kept only as labelled history.

## Where the cycle stands right now (as of 2026-11-24)

- **RSS 2027** (23rd edition, Athens, Greece: Megaron Athens International Conference
  Centre) runs **July 6–11, 2027**. Its call is out and the first gate is close: the
  **Stage 1 Extended Abstract is due December 4, 2026** (11:59pm AoE).
- RSS 2026 (Sydney, July 13-17, 2026) has met; its single-deadline cycle (abstract
  Jan 23 → paper Jan 30 → supplement Feb 6 → invited rebuttal Apr 3 → decisions
  Apr 27, 2026) is history, not a template for 2027.

## The RSS 2027 two-stage calendar

| Date (11:59pm AoE) | Event | Skill |
|---|---|---|
| December 4, 2026 | Stage 1 Extended Abstract (5 + 1 pages) | `rss-submission` |
| February 5, 2027 | Stage 1 decision: reject or invitation to rebuttal (with Metareview) | `rss-review-process` |
| February 12, 2027 | Rebuttal | `rss-author-response` |
| February 26, 2027 | Stage 2 decision: reject or Extension Charter | `rss-review-process` |
| April 16, 2027 | Final paper (8 pages excluding references), Charter executed | `rss-submission`, `rss-experiments` |
| April 19, 2027 | Supplementary material (zip, 100MB max) | `rss-supplementary` |
| April 30, 2027 | Acceptance notification | — |
| May 14, 2027 | Camera-ready | `rss-camera-ready` |
| July 6–11, 2027 | Conference, Athens | `rss-camera-ready`, `rss-artifact-evaluation` |

## The robotics year, seen from RSS

RSS shares its authors with three siblings, so choosing RSS is also choosing a slot in
an annual rotation. Approximate recent geometry (verify each venue's live pages):

| Venue | Typical deadline | Typical event | What slipping past RSS costs |
|---|---|---|---|
| RSS | early December (2027 Stage 1; late January through 2026) | July | Next comparable single-track slot is a full year away |
| IROS | ~March | ~October | Natural catch for a paper not ready for RSS |
| CoRL | ~May/June | ~November | Right jury if the learning story dominates |
| ICRA | ~September | ~May/June | Broadest program; absorbs systems breadth |

The practical use: Stage 1 asks for a sharp hypothesis and methodology, not finished
results, so RSS 2027 is reachable earlier in a project than before — but the Extension
Charter then demands execution between late February and mid-April. A project that
cannot staff that window should aim at IROS or CoRL instead.

## Backward plan to the December 4 Stage 1 gate

| Weeks out | Milestone for a hypothesis-plus-hardware paper |
|---|---|
| 8+ | Hypothesis fixed in one testable sentence; methodology designed to confirm or falsify it |
| 6 | Pilot trials that show the method is feasible; failure attribution logged from day one |
| 3 | 5-page draft: problem, hypotheses, method, key preliminary evidence; 1 page of references |
| 2 | Internal red-team read against the review form (value of hypothesis, feasibility) |
| 1 | Anonymity sweep; every citation resolved against a real record; OpenReview profiles complete |
| 0 | Submit; then keep the robot and pipeline ready for a possible Extension Charter |

## Stage 2 execution window (February 26 → April 16, 2027)

Seven weeks to run whatever the Charter requires — possibly new or different
experiments. Reserve hardware time, people, and compute before February 5; the
supplement (zip, 100MB) follows three days after the final paper and is packing time,
not filming time.

## Conference-week execution

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

## Stage-specific traps

- **The December gate is earlier than habit:** teams used to a late-January RSS
  deadline lose the holiday weeks they planned around.
- **Dual submission is strict:** a paper still under review elsewhere (e.g., ICLR) on
  December 4 must be withdrawn there first — no overlap, even for days.
- **The rebuttal is conditional:** only papers invited at Stage 1 respond (February
  5-12). Plan the window without assuming it will be used (`rss-author-response`).
- **Authors are frozen at Stage 1:** adding a collaborator for Charter experiments needs
  Program Chair approval and must be justified by the Charter.
- **April 30 → July is short:** visa lead times for Greece can exceed the
  decision-to-conference gap; start paperwork early for likely-accept projects.
- **No standing editors:** the Program Chair and Area Chairs rotate per edition (2027
  Program Chair: Amanda Prorok, Cambridge; 2026: Matei Ciocarlie, now General Chair);
  never carry a name or a policy across cycles.

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
because the Stage 2 supplement freezes three days after the final paper and reshoots
after the paper deadline cannot support frozen claims.

## Output format

```text
[Cycle position] drafting stage 1 / stage 1 submitted / rebuttal window / executing charter / final submitted / accepted / conference week
[Next hard date] <date + source URL, or 待核实>
[Critical path] <three tasks gating the next stage>
[Fallback venue] IROS / CoRL / ICRA + trigger condition
[Calendar risks] <robot downtime / visa / footage / rebuttal availability>
```
