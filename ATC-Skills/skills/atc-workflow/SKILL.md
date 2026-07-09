---
name: atc-workflow
description: Use when planning an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) campaign end to end — running the year backward from the early-June deadline through the two review rounds, the rebuttal, conditional-acceptance shepherding, the post-acceptance artifact evaluation, and the ACM Open Access camera-ready for the November Hong Kong conference.
---

# ATC Workflow

Plan the campaign backward from the deadline. ATC 2026 — the first **ACM SIGOPS** edition of the
former **USENIX ATC** — runs on a calendar and a review structure that both changed in the
transition: an **early-June 2026** submission deadline (AoE; 1 vs. 10 June unresolved across
renderings — 待核实), a **two-round, extended-abstract** review, **conditional acceptance with
shepherding**, a separate **artifact-evaluation** track, and the conference in **Hong Kong, 15-18
November 2026**. Reopen the SIGOPS call for the exact dates before committing to any of the offsets
below.

## The arc (backward from the deadline)

```text
[T-0    Submission]      paired upload: 2-page extended abstract + full paper on atc26.hotcrp.com
[Round one]             two reviewers judge each extended abstract; below-bar papers cut early
[Round two]             3-4 reviewers read the full paper of survivors
[Rebuttal]              ~1 page: correct factual misreadings; note prior-submission changes if any
[Decision]              conditional accept / reject
[Shepherding]           a PC shepherd signs off required revisions before final acceptance
[Artifact evaluation]   separate post-acceptance AEC track -> Available / Functional / Reproduced
[Camera-ready]          de-anonymize, satisfy shepherd, ACM Open Access metadata + production checks
[Nov 15-18]             present at the Hong Kong conference; talk video/slides per the venue norm
```

## Backward plan from the June deadline

- **T-10 to T-8 weeks:** lock the system and freeze the experiments. On a systems paper the testbed
  and measurements are the long pole; leave prose churn for later. Pin environments now
  (`atc-reproducibility`) — provenance cannot be reconstructed at the deadline.
- **T-6 weeks:** full-paper draft complete against `atc-writing-style`; baselines and honest costs
  in place per `atc-experiments`.
- **T-3 weeks:** write and stress-test the **two-page extended abstract** — the round-one decision
  surface. Have someone read *only* the abstract and tell you the problem, contribution, testbed,
  and result. If they cannot, fix it.
- **T-2 weeks:** build the anonymized, runnable artifact and the claim-to-experiment map.
- **T-1 week:** double-blind sweep on the final PDF, abstract, and artifact; fill HotCRP fields and
  conflicts; confirm the exact AoE deadline day.
- **T-0:** upload both the extended abstract and the paper; re-download and read cold.

## Between submission and decision

- **Round one is silent from your side** — there is no action between upload and the round-one cut;
  the abstract is your entire round-one argument. Do not start major new experiments hoping to swap
  in a stronger paper mid-cycle.
- **If you advance to round two,** prepare for the rebuttal: keep a running list of the measurements
  and clarifications a skeptical reviewer would ask for, so the ~1-page window is spent well
  (`atc-author-response`).

## After a conditional accept

- Treat the **shepherd's required revisions as binding**. Make each change or explicitly justify
  declining it; the shepherd holds final acceptance until satisfied.
- Start the **artifact-evaluation** package immediately: the AEC track has its **own post-acceptance
  deadline**, independent of the camera-ready (`atc-artifact-evaluation`). De-anonymize and archive
  the artifact in a DOI-issuing repository for the Available badge.
- Prepare the **camera-ready**: de-anonymize the paper, fold in the shepherd's changes, and complete
  **ACM Open Access** metadata (`atc-camera-ready`). Budget for the transition **APC**
  (subsidized for 2026; exact figure per the ACM/SIGOPS terms).

## Calendar reconnaissance

```text
[Deadline]     confirm the exact early-June AoE day on the SIGOPS call (1 vs 10 June — 待核实)
[Conference]   Hong Kong (Hyatt, Shatin), Nov 15-18, 2026 — plan travel/visa early for HK
[Rotation]     under SIGOPS, ATC rotates Asia/Europe/North America; next-year location differs
[Artifact]     find the AEC submission date on the call for artifacts (separate from camera-ready)
[Backup]       if rejected, line up OSDI/NSDI/EuroSys/FAST dates via atc-topic-selection
```

## Reverify each cycle

- The exact deadline day, notification/rebuttal dates, and camera-ready date.
- Whether the two-round extended-abstract model and the reviewer counts persist.
- Artifact-evaluation timing and the badge set; the Deployed Systems lane (**待核实**).
- ACM Open Access / APC terms; template file (USENIX vs. ACM) (**待核实**).

## Output format

```text
[ATC workflow stage] planning / drafting / abstract-hardening / submitted / round two / rebuttal / shepherding / artifact / camera-ready
[Critical path] the long-pole task (usually testbed + measurements, then the extended abstract)
[Deadline set] submission (early June AoE), rebuttal, shepherd sign-off, artifact, camera-ready
[Next action] the single most schedule-critical step, with a date
[Risk] the item most likely to slip (provenance pinning / abstract self-containment / shepherd changes)
```
