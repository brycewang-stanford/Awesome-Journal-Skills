---
name: interspeech-workflow
description: Use when managing an INTERSPEECH project across the annual ISCA cycle — backward-planning from the February deadline (9 February 2027) through the update window, April rebuttal, June notification, camera-ready and registration coupling, and the late-summer conference (São Paulo, 29 August – 2 September 2027).
---

# INTERSPEECH Workflow

Interspeech runs one cycle per year with an unforgiving rhythm: a winter deadline,
a silent spring, a June verdict, and a Northern-autumn conference. This skill is
the project-management layer; every date below is the Interspeech 2027 (São Paulo)
calendar read on the official call on 2026-11-24, and must be swapped for the live
one each cycle.

## The 2027 reference clock

| Date (2027) | Event | Owner's job |
|---|---|---|
| 19 Jan | Submission portal opens | metadata drafted, area chosen |
| 9 Feb | Paper deadline | PDF + frozen metadata in |
| 16 Feb | Paper-update close | sanctioned typo/figure pass done |
| 13–20 Apr | Rebuttal period | response team on call |
| 2 Jun | Notification | triage meeting same week |
| 9 Jun | Camera-ready close | de-anonymized PDF + metadata |
| (待核实) | Registration tiers | author registration secured |
| 29 Aug – 2 Sep | Conference, São Paulo | talk/poster + audio fallback ready |

The 2026 (Sydney) clock for comparison: portal 17 Jan, deadline 25 Feb, update 4 Mar,
rebuttal 24 Apr – 1 May, notification 5 Jun, camera-ready 19 Jun, early-bird
registration 15 Jul, conference 27 Sep – 1 Oct 2026.

## Where the cycle stands today (2026-11-24)

Between cycles. Interspeech 2026 (Sydney) has met. The Interspeech 2027 call is
published: **the paper deadline is 9 February 2027, about eleven weeks away**, and
the deadline is two weeks earlier than 2026's. The paper kit and submission page were
still "available soon" — watch interspeech2027.org for them, and plan for an
August–September conference in Brazil (visa lead times).

## Backward plan from any Interspeech deadline

Offsets that have survived contact with real teams; anchor them to live dates:

- **T−10 weeks**: claims frozen; corpus/split/licensing decisions final.
- **T−6 weeks**: main results table filled with *some* number in every cell — the
  quality improves later, the design cannot.
- **T−4 weeks**: draft exists in the official paper kit (not a one-column doc —
  the 4-page reality only shows in the template).
- **T−2 weeks**: internal review by one speech scientist *and* one engineer,
  mirroring the reviewer mix; significance tests run.
- **T−1 week**: compression pass (`interspeech-writing-style`), anonymity sweep,
  demo page frozen.
- **T**: submit half a day early; submission portals queue at AoE cutoffs.
- **T+1 week**: proofread the submitted PDF; use the update window for repairs
  only.

## Failure patterns by phase

- **Winter**: discovering at T−1 that the paper is 5.5 pages — compression is a
  week of work, not a night (see the compression order in
  `interspeech-writing-style`).
- **Spring silence**: team disbands; nobody owns the rebuttal when it lands.
  Assign the response owner at submission time.
- **June**: acceptance euphoria eats the two-week camera-ready window; the
  registration coupling (no registered author → no proceedings entry) surfaces in
  August as a crisis.
- **September**: audio demos that only ever ran on the lab machine meet a
  conference-hall AV chain. Rehearse playback; carry spectrogram fallbacks.

## Parallel-track decisions

- **Interspeech vs ICASSP double rhythm**: the sibling deadline (typically autumn
  for ICASSP) means a rejected February idea has a fall retry — decide in June
  whether reviews point to "fix and ICASSP" or "grow and Interspeech 2027".
- **Challenge alignment**: many Interspeech papers ride a challenge (CHiME,
  VoxSRC, ASVspoof…); challenge timelines are their own clocks, published by each
  organizer, and system-description papers have separate rules — verify per
  challenge.
- **Journal extension**: an accepted 4-pager with leftover material has a
  standard afterlife at TASLP / Computer Speech & Language / Speech Communication;
  start the extension outline while the reviews are fresh.

## Standing owner map

Assign at kickoff, not at crisis:

- **Paper owner** — format, compression, the submitted PDF, the update-window
  proofread.
- **Evidence owner** — experiment matrix, seeds, significance, scoring scripts.
- **Compliance owner** — anonymity sweep (PDF + demo page + repo), license
  chain, policy checkboxes.
- **Rebuttal watcher** — has portal credentials, watches the 13–20 April window, owns
  the response draft calendar.
- **Logistics owner** — registration before the tier cutoffs, visa timelines,
  AV rehearsal for the talk or poster QR codes.

One person can hold two hats; no hat may be unassigned. Every 2026 failure
pattern above maps to exactly one vacant hat.

## Minimal milestone ledger

```text
[frozen]   claims / corpus / splits ........ T-10w   owner: evidence
[in-kit]   draft in official template ...... T-4w    owner: paper
[reviewed] internal science+eng pass ....... T-2w    owner: paper
[swept]    anonymity + demo page frozen .... T-1w    owner: compliance
[in]       CMT submission confirmed ........ T       owner: paper
[patched]  update-window proofread ......... T+1w    owner: paper
[watched]  rebuttal window covered ......... spring  owner: watcher
[final]    camera-ready + registration ..... June    owner: logistics
```

## Output format

```text
[Phase] pre-deadline / update-window / silent-spring / rebuttal /
        post-decision / conference-run-up / post-conference
[Live deadline] <date + what it gates + source URL>
[Owner map] paper / rebuttal / camera-ready+registration / artifacts / talk
[Backward plan] next three offsets with dates
[Parallel tracks] ICASSP retry? challenge clock? journal extension?
[Risk now] <single most time-critical item>
```

Verified anchors and the 待核实 list live in
`resources/official-source-map.md` (re-verified 2026-11-24). ISCA rotates organizing
committees per edition — the Sydney team's choices (tracks, rebuttal shape,
attachment rules) did not bind São Paulo, and São Paulo's will not bind San Antonio.
