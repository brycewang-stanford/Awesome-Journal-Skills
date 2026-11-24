---
name: atc-workflow
description: Use when planning an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) campaign end to end — running the year backward from the 19 January 2027 deadline through the two review rounds, the 72-hour author response, conditional-acceptance shepherding, the post-acceptance artifact evaluation, and the ACM Open Access camera-ready for the June–July 2027 Rennes conference.
---

# ATC Workflow

Plan the campaign backward from the deadline. ATC — the **ACM SIGOPS** continuation of the retired
**USENIX ATC** — has changed its calendar twice in two years: ATC 2026 took papers on **10 June
2026** for a **November** meeting in Hong Kong, and **ATC 2027** takes them on **19 January 2027
(AoE, no extensions)** for **28 June – 1 July 2027 in Rennes, France**. The 2027 cycle (call
re-verified 2026-11-24) has **two review rounds** (the first reads the first two pages), a
**72-hour author response**, **conditional acceptance with shepherding**, a separate
**artifact-evaluation** track, and a **two-submissions-per-author** cap. Reopen the SIGOPS call
before committing to any of the offsets below.

## The arc (ATC 2027)

```text
[19 Jan 2027, AoE]      submission on atc27.hotcrp.com (no extensions; author list frozen)
[Round one]             first two pages read; out-of-scope / unmotivated / unclear / incremental /
                        poorly positioned / weakly evaluated papers cut
[Round two]             additional reviews for papers that advance
[3-5 Apr 2027]          72-hour author response: factual corrections and answers only
[27 Apr 2027]           notification: conditional accept / reject
[Shepherding]           a PC shepherd signs off required revisions before final acceptance
[Artifact evaluation]   separate post-acceptance AEC track (2027 call not yet published)
[28 May 2027]           camera-ready: de-anonymize, satisfy shepherd, ACM Open Access metadata
[28 Jun - 1 Jul 2027]   Rennes: oral and/or poster presentation; one author must attend
```

## Backward plan from the January deadline

- **T-10 to T-8 weeks (mid-November):** lock the system and freeze the experiments. On a systems
  paper the testbed and measurements are the long pole, and the December holidays eat two of the
  remaining weeks. Pin environments now (`atc-reproducibility`).
- **T-6 weeks:** full-paper draft complete against `atc-writing-style`; baselines and honest costs in
  place per `atc-experiments`; settle which **two** ATC submissions each author is on.
- **T-3 weeks:** stress-test the **first two pages** — the round-one decision surface. Have someone
  read *only* pages 1-2 and tell you the problem, idea, delta over prior work, positioning, and
  evidence. If they cannot, fix the opening.
- **T-2 weeks:** fit the 12/6-page budget **including any appendix**; build the anonymized,
  runnable artifact and the claim-to-experiment map.
- **T-1 week:** double-blind sweep on the final PDF and artifact; fill HotCRP fields, conflicts, and
  any resubmission change summary.
- **T-0:** upload; re-download and read cold.

## Between submission and decision

- **Round one is silent from your side** — the first two pages are your entire round-one argument.
- **Prepare the response before 3 April:** keep a running list of the clarifications a skeptical
  reviewer would ask for, each pointing to evidence already in the paper, so the 72-hour window is
  spent editing rather than drafting (`atc-author-response`). New experiments are not allowed in it.
- Meanwhile, start the artifact package — the post-acceptance AE deadline will be short.

## After a conditional accept (27 April 2027)

- Treat the **shepherd's required revisions as binding**. Make each change or explicitly justify
  declining it; the shepherd holds final acceptance until satisfied.
- Submit the **artifact** on the AEC's own schedule (`atc-artifact-evaluation`); archive it in a
  DOI-issuing repository for the Available badge.
- Prepare the **camera-ready** for **28 May 2027**: de-anonymize, fold in the shepherd's changes,
  complete **ACM Open Access** metadata, and settle any APC (authors outside ACM Open institutions;
  the ATC call quotes no rate) (`atc-camera-ready`).
- Plan travel to Rennes early: one author must attend, whether the paper gets an oral slot or a
  poster.

## Calendar reconnaissance

```text
[Deadline]     19 January 2027, AoE — confirm the HotCRP /deadlines clock once it is populated
[Conference]   Rennes, Le Couvent des Jacobins, 28 June - 1 July 2027
[Artifact]     find the AEC dates on the 2027 call for artifacts (待核实 — not yet published)
[Backup]       if rejected (27 April), line up OSDI/NSDI/EuroSys/FAST dates via atc-topic-selection
[History]      ATC 2026: 10 June 2026 deadline, Hong Kong 15-18 November 2026
```

## Reverify each cycle

- The deadline, response window, notification, and camera-ready dates (ATC has moved its calendar
  every year since the SIGOPS handover).
- Whether round one still reads two pages, whether appendices still count, and the author cap.
- Artifact-evaluation timing and the badge set (**待核实** for 2027).
- ACM Open Access / APC terms and waivers.

## Output format

```text
[ATC workflow stage] planning / drafting / opening-hardening / submitted / round two / author response / shepherding / artifact / camera-ready
[Critical path] the long-pole task (usually testbed + measurements, then the first two pages)
[Deadline set] submission (19 Jan 2027 AoE), response (3-5 Apr), notification (27 Apr), camera-ready (28 May)
[Next action] the single most schedule-critical step, with a date
[Risk] the item most likely to slip (provenance pinning / opening self-containment / author cap / shepherd changes)
```
