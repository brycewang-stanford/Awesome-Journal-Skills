---
name: webconf-author-response
description: Use when drafting the Web Conference (WWW) rebuttal inside its one-week window, triaging reviews from the venue's mixed systems/mining/social-science reviewer pool, answering misread-track objections, protecting anonymity, and deciding what can honestly be promised for the camera-ready versus what needs new evidence.
---

# Web Conference Author Response

The 2026 rebuttal window ran November 24 - December 1, 2025 — seven days, scheduled
over a major holiday week in North America, between the October 7 paper deadline and
the January 13 notification. Plan writing capacity for that specific week the moment
the paper goes in. Exact mechanics (length caps, per-review vs. single response,
revised-PDF permission) were not published in the sources this pack could verify;
confirm them in the review platform the day reviews arrive, before drafting.

## Read the packet as a track artifact

Web Conference reviews come from a track-scoped pool, and the venue's defining
property is that neighboring tracks read the same paper differently. A
recommendation paper reviewed in "User modeling, personalization and recommendation"
gets offline-metric and baseline questions; the same paper in "Social networks and
social media" gets construct-validity and user-harm questions. Before answering
anything, classify each review:

| Reviewer stance | Diagnostic signal | Response strategy |
|---|---|---|
| In-track expert | Names specific baselines/datasets you skipped | Concede or supply numbers; never hand-wave |
| Adjacent-track lens | Questions assume a different evidence standard | Restate the track's contribution type, then answer on their terms |
| Web-fit skeptic | "Why is this a WWW paper?" | Point to the web-native element: platform data, web-scale constraint, user behavior |
| Feasibility doubter | "Would this survive real traffic / real crawls?" | Cite the appendix's systems details by section number |

The "why is this a WWW paper" objection is the venue's signature rejection reason
and deserves its own paragraph in almost every rebuttal: name the property of the
Web (openness, adversarial content, platform incentives, hyperlink structure, live
user feedback) without which the contribution would not exist.

## Evidence rules inside the window

- New numbers are credible only if small and directly responsive: one extra
  baseline, one ablation cell, one robustness split. A brand-new experiment campaign
  announced in a rebuttal reads as an admission the paper was premature.
- Anything already in the submission beats anything new. Cite by page, section, and
  line number (the `review` class option prints line numbers for exactly this).
- Keep anonymity intact: no links to freshly pushed repositories or dashboards whose
  accounts identify you, no "as we showed at <company>."
- Never promise the camera-ready something the 12-page proceedings budget cannot
  hold. "We will add a full new user study" is a promise reviewers know is either
  false or destined for an appendix nobody must read.

## Rebuttal skeleton

```text
[Common thread]  (2-4 sentences shared across reviewers)
  All reviewers asked about X; the short answer is Y (Sec 4.2, lines 512-530).

[R1 - in-track]
  Q: missing baseline B.  A: added; B underperforms ours by <delta> on the same
  split (protocol identical to Table 2). Will appear in Table 2.
  Q: dataset freshness.   A: crawl window and snapshot date are in App. A; we will
  surface them in Sec 3.1.

[R2 - adjacent track]
  Your reading applies the <other-track> bar of <standard>. Our claim is a
  <contribution type> claim; under the track's CFP scope, the evidence in Sec 5
  addresses it because <reason>. On your specific concern: <direct answer>.

[R3 - web-fit skeptic]
  The method exploits <web-native property>; without it, <what breaks>. Non-web
  analogues (e.g., <venue>) do not face <constraint>.
```

One discipline per answer: quote the reviewer's actual sentence, answer it in the
first line, then justify. Reviewers reread rebuttals in minutes, not hours.

## Triage when everything cannot be answered

1. Answer every factual error, however small — uncorrected errors become
   meta-review facts.
2. Answer the objection most repeated across reviews with the common-thread block.
3. Answer the lowest-scoring reviewer's *strongest* point, not their longest one.
4. Concede real limitations explicitly and say what the camera-ready will state.
   At this venue, a clean concession on scope routinely outperforms a defensive
   paragraph, because track chairs read rebuttals for calibration as much as content.

## Micro-example: the same objection, answered twice

Reviewer sentence: *"The improvements may come from the larger embedding table
rather than the proposed crawl-time signal."*

Weak answer (defensive, unfalsifiable):

> We respectfully disagree. Our method is fundamentally different from simply
> increasing capacity, as explained in Section 4. The crawl-time signal is a key
> novel contribution and the results clearly demonstrate its effectiveness.

Strong answer (evidence-anchored, one new number, page-cited):

> Table 3 row 4 already controls for this: the parameter-matched ablation
> (identical embedding budget, signal removed) loses 3.8 points (p. 7, lines
> 689-702). We add one cell for completeness: doubling the baseline's embedding
> table recovers only 0.4 of those points. We will fold this cell into Table 3
> and state the parameter counts in the caption.

The differences that matter: the strong answer names the existing evidence by
coordinates, adds the *smallest* experiment that decides the question, and ends
with a concrete, budget-compatible camera-ready commitment. It also never uses
"novel," "fundamentally," or "clearly" — calibration words that track chairs
discount automatically.

## After the window

Nothing can be added between December 1 and the January 13 notification; do not
email chairs with supplements. If the outcome is rejection, the same cycle still
offered later routes in 2026 — short papers (November deadlines) closed before
notification, but the next edition's research tracks and the current edition's
workshop calls remain; route via `webconf-workflow`.

## Output format

```text
[Rebuttal plan] <n> reviews: <in-track/adjacent/web-fit/feasibility counts>
[Common thread] <the one issue answered once for everyone>
[New evidence] <small additions only, with source of numbers>
[Concessions] <what is admitted and how the camera-ready will phrase it>
[Anonymity check] pass / fail
[Unverified mechanics] <length cap / format items confirmed in-platform>
```
