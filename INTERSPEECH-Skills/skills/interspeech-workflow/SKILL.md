---
name: interspeech-workflow
description: Use when managing an INTERSPEECH project across the annual ISCA cycle — backward-planning from the late-February deadline through the update window, spring review, June notification, camera-ready and registration coupling, and the September–October conference, including what to do in the current post-decision phase and 2027 planning.
---

# INTERSPEECH Workflow

Interspeech runs one cycle per year with an unforgiving rhythm: a winter deadline,
a silent spring, a June verdict, and a Northern-autumn conference. This skill is
the project-management layer; every date below is the verified 2026 (Sydney)
calendar and must be swapped for the live one each cycle.

## The 2026 reference clock

| Date (2026) | Event | Owner's job |
|---|---|---|
| 17 Jan | CMT portal opens | metadata drafted, area chosen |
| 25 Feb | Paper deadline | PDF + frozen metadata in |
| 4 Mar | Paper-update close | sanctioned typo/figure pass done |
| ~24 Apr – 1 May | Rebuttal window (reported, 待核实) | response team on call |
| 5 Jun | Notification | triage meeting same week |
| 19 Jun | Camera-ready close | de-anonymized PDF + metadata |
| 15 Jul | Early-bird registration closes | author registration secured |
| 16 Aug | Standard registration closes | stragglers covered |
| 27 Sep – 1 Oct | Conference, Sydney | talk/poster + audio fallback ready |

## Where the cycle stands today (2026-07-08)

Mid-cycle, post-decision. Accepted teams: camera-ready is behind you; **early-bird
registration closes in one week** — that is the live deadline — then presentation
prep, artifact publication (`interspeech-camera-ready`,
`interspeech-artifact-evaluation`), and travel/visa for Sydney. Rejected or
unsubmitted teams: the 2027 cycle (São Paulo, 29 Aug – 2 Sep 2027) is the target;
expect a deadline in the same late-winter region but **treat the 2027 dates as
unpublished until the São Paulo site posts them**.

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
- **T**: submit half a day early; CMT queues at AoE cutoffs.
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
- **Rebuttal watcher** — has CMT credentials, watches the reported window, owns
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
`resources/official-source-map.md` (checked 2026-07-08). ISCA rotates organizing
committees per edition — the Sydney team's choices (tracks, rebuttal shape,
attachment rules) do not bind São Paulo.
