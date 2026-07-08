---
name: chi-workflow
description: Use when planning an ACM CHI submission cycle end to end — the single September deadline, two-round review with a five-week revise-and-resubmit window, December decisions, the TAPS and publication-ready chain, and the May conference — with owners and risk buffers for each stage.
---

# CHI Workflow

CHI is a one-shot annual venue with a two-round review inside the cycle. The dates
below are the CHI 2027 calendar as posted on `chi2027.acm.org` and read on 2026-07-08
via search renderings (the site refuses direct automated fetches); treat them as this
cycle's plan and reverify on the live page at each stage.

## The CHI 2027 calendar

| Date | Stage | Who must act |
|---|---|---|
| 2026-07-30 | PCS submission site opens | Submitting author sets up the record early |
| 2026-09-10 (Thu) | **Full papers due — including videos and supplementary** | Everyone; no separate abstract deadline was posted |
| ~late Oct / early Nov 2026 (待核实) | Round-1 outcome: revise-and-resubmit invitation or reject | 1AC/2AC verdict arrives; clear your calendar if invited |
| 2026-12-03 | Revised paper + author response due (≈5 weeks after round-1) | Whole author team, on a fixed clock |
| 2026-12-17 | Final notification after round 2 / PC meeting | — |
| 2027-01-14 | Camera-ready source due in ACM TAPS | Paper lead + whoever owns LaTeX/Word source |
| 2027-02-18 | Publication-ready deadline on PCS (final materials, supplemental, optional video preview) | Paper lead |
| 2027-03-04 | Registration deadline + video presentation deadline | Presenting author + grant admin |
| 2027-05-10 – 05-14 | CHI 2027, Pittsburgh, Pennsylvania, USA | Presenter |

Two structural facts drive all planning: **everything is due on September 10** — CHI
gives no later supplement or video slot — and **the December 3 revision window is only
five weeks long**, landing across November holidays for much of the community.

## Working backwards from September 10

- **T−16 weeks (mid-May):** study data collection finished. A CHI paper whose study is
  still running in July will submit an under-analyzed paper.
- **T−10 weeks:** analysis locked; contribution type and subcommittee choices drafted
  (`chi-topic-selection`); skeleton of the paper written.
- **T−6 weeks:** full draft exists; video figure storyboarded. Video production,
  captioning, and consent checks for footage reliably take three weeks.
- **T−3 weeks:** internal "mock 1AC" read by someone outside the project; fix the
  contribution statement before polishing prose.
- **T−1 week:** run the `chi-submission` audit; upload a complete package to PCS and
  re-download it. PCS accepts revisions until the deadline, so upload early and
  overwrite.

## Pre-positioning for the five-week revision

The revise-and-resubmit window cannot be extended, so buy time before it opens:

```text
Before round-1 results arrive (October):
[ ] Keep the study environment alive — do not archive the analysis pipeline,
    delete participant contact channels, or let IRB approval lapse; a small
    follow-up analysis is the most common revision request you can predict.
[ ] Pre-agree author availability for the five weeks around Nov-Dec.
[ ] Set up the tracked-changes toolchain now (latexdiff or Word tracking)
    so day 1 of the window is spent revising, not configuring.
[ ] Draft the response-letter template with one section per reviewer.
```

If invited, treat it as a real second round, not a formality: at CHI as much as half
of revised papers can still be rejected at the PC meeting (the posted process warns up
to 50%; at CHI 2026, 65.5% of resubmissions were accepted). See `chi-author-response`.

## The post-acceptance chain is longer than at most venues

Acceptance in December starts a four-deadline pipeline — TAPS source (January),
publication-ready PCS package with accessibility metadata (February), registration and
the presentation video (March), then the conference (May). Each has a different owner
and a different failure mode; assign names in December, not February. Details in
`chi-camera-ready`.

## Risk register for the cycle

| Risk | Window | Mitigation |
|---|---|---|
| Study slips past May | Spring | Cut scope to a short paper rather than submit thin data |
| Video figure unfinished at deadline | September | Storyboard at T−6 weeks; captions are mandatory work, not polish |
| Round-1 invite lands during travel/holidays | Oct–Dec | Availability pact signed in October |
| Requested analysis impossible (data deleted, IRB lapsed) | Nov | Keep the pipeline warm until December 17 |
| TAPS rejects source formatting | January | Compile on the ACM class early; do not hand-hack the PDF |
| Missing alt text blocks publication-ready sign-off | February | Write figure descriptions during drafting, not after acceptance |
| Nobody registered by March 4 | March | Registration owner named at acceptance |

## If the December answer is no

Rejected CHI papers have a well-worn afterlife: the reviews map cleanly onto CSCW
(different deadline rhythm), DIS, IUI, or a TOCHI journal submission where length
limits will not pinch. Do the re-route triage within two weeks of the decision while
the reviews are fresh — see the venue table in `chi-topic-selection` — and log which
criticisms were CHI-specific versus substantive.

## Output format

```text
[Cycle] CHI 2027 (papers due 2026-09-10; verified 2026-07-08, reverify live)
[Today → next gate] <stage name, days remaining>
[Stage owners] submission: <name> / revision: <name> / TAPS: <name> / registration: <name>
[Top calendar risk] <risk + mitigation from the register>
[Fallback venue] <where this goes if December says no>
```
