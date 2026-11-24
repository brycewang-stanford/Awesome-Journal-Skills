---
name: uist-workflow
description: Use when planning a UIST cycle end to end — the spring abstract, paper and materials deadlines, the ten-week build-freeze before video production, the rebuttal window, conditional acceptance, the end-of-July camera-ready, adjunct-track parallel lanes, and the November conference — with owners and risk buffers.
---

# UIST Workflow

A UIST year is engineered backwards from two fixed points: the paper deadline in late
March and the conference in the fall. Between them sits a pipeline with almost no
slack for hardware failures, video production, or study scheduling. This skill turns
the cycle into a managed project. All dates below are the UIST 2026 numbers
(re-verified 2026-11-24 against the live CFP); reopen `uist.acm.org/<year>/cfp/` before
committing a calendar.

## The 2026 reference calendar

| Date (2026) | Event | Author obligation |
|---|---|---|
| Mar 24 | Abstract deadline (AoE) | Title, abstract, authors, track metadata in PCS |
| Mar 31 | Paper deadline (AoE) | Anonymous paper PDF (< 20 MB) |
| Apr 9 | Materials deadline (AoE) | Video figure, supplementary files, alt text, video subtitles (< 300 MB total) |
| May 28 - Jun 5 | Reviews out → rebuttal due | 5,000-character self-contained response |
| Jun 27 | Notification | Decisions are conditional on rebuttal-promised changes |
| Jul 3 | Final reviews | Full reviews, possibly revised after the PC meeting |
| Jul 10 | Adjunct deadlines | Demos, Posters, Doctoral Symposium, Workshops, Visions |
| Jul 31 | Camera-ready upload (PCS + TAPS) | TAPS source, alt text, final video, +10% page allowance |
| Aug 7 | Final acceptance decision | 1AC has checked the promised changes |
| Aug 14 | Video preview | Mandatory 30-second preview |
| Nov 2 | Workshops + Doctoral Symposium (in person) | Separate tracks, separate deadlines |
| Nov 2-5 | Conference, Detroit | Talk + (typically) live demo of the system |

As of 2026-11-24 the whole 2026 cycle is closed (the conference met November 2-5).
New submissions target **UIST 2027 — Vienna, Austria, October 26-29, 2027** — whose
home page announces Papers deadlines of abstract **March 31**, full paper **April 7**
and supplementary materials **April 9** (2027). The UIST 2027 CFP and Author Guide are
not yet published, so page limits, adjunct-track dates and the review calendar are
still unknown.

## Backwards plan for a systems paper

Work in reverse from the paper deadline; the ordering below is where UIST projects
actually fail, not a generic writing schedule:

1. **T minus 0-1 weeks — submission mechanics.** PCS uploads, anonymity sweeps,
   abstract-field consistency (see `uist-submission`).
2. **T minus 1-3 weeks — video figure production.** Scripting, capture, edit,
   captions, anonymization. The video cannot be shot until the system is stable, and
   it competes with the writing for the same people (see `uist-supplementary`).
3. **T minus 3-6 weeks — evaluation.** Technical benchmarks and any user study; IRB
   approval must predate this window, so file it in the fall.
4. **T minus 6-10 weeks — feature freeze.** Everything demonstrated in the paper
   must exist by here. Features added after freeze belong to the next paper.
5. **T minus 10+ weeks — build.** Include one full hardware re-spin or one major
   refactor in the estimate, because there will be one.

## Owners and risk register

Assign names, not roles, and write the mitigation before the risk fires:

```text
RISK                              OWNER      MITIGATION
Hardware breaks in video week     <name>     Build two units; film B-roll early
Study participants no-show        <name>     Over-recruit 30%; pilot in freeze week
Video render/caption pipeline     <name>     Dry-run export at T-3w with dummy edit
Page-limit overflow (10pp body)   <name>     Appendix plan agreed at T-4w
Rebuttal week hits a holiday      <name>     Pre-draft objection playbook (uist-author-response)
Camera-ready owner on vacation    <name>     TAPS + alt-text buddy named at notification
```

## The two parallel lanes

UIST is one conference with two archival containers, and a healthy group uses both:

- **Papers lane** (main proceedings): the full pipeline above.
- **Adjunct lane** (Demos, Posters — separate chairs, separate deadlines, adjunct
  proceedings): a rejected paper's system can still appear at the conference as a
  demo; early-stage work can test community reaction as a poster; the same work must
  not be submitted to both Demos and Posters (the 2026 rule converts it to a demo and
  drops the poster). Decide the fallback lane on notification day, not after the
  adjunct deadlines pass.

## Planning UIST 2027 from a late-2026 vantage

For teams reading this after UIST 2026, the next Papers deadline is about four and a
half months out: the UIST 2027 home page (checked 2026-11-24) lists abstract March 31,
full paper April 7 and supplementary materials April 9, with the conference in Vienna,
October 26-29, 2027. The full CFP is not yet out. Planning rules that survive cycle
drift:

- Anchor the feature-freeze ten weeks before **April 7, 2027** (late January) and the
  abstract a week earlier; the 2027 deadlines sit a week later than 2026's, but do not
  assume the rest of the 2026 calendar shifts with them.
- Anything involving **human subjects** needs ethics approval filed by roughly
  December; anything involving **custom hardware** needs its final revision ordered
  by January (fab and shipping queues do not respect AoE).
- Book **video-production capacity** — the person, the rig, the edit suite — for
  the two pre-deadline weeks now; it is the least substitutable resource in the
  pipeline.
- Draft the **contribution list before the spring**: if you cannot write three
  capability claims in January, the project is a 2028 paper wearing a 2027 badge.

## The month-by-month cadence (generic UIST year)

| Months before deadline | Focus |
|---|---|
| 9-7 | Routing decision, system architecture, ethics filing |
| 7-4 | Core build; related-work sweep running in parallel |
| 4-2.5 | Feature freeze; evaluation harness and pilots |
| 2.5-1 | Studies and technical characterization; paper skeleton |
| 1-0.5 | Video production; full drafts circulating |
| 0.5-0 | Submission mechanics only — nothing new enters the paper |

## Between cycles

- File a post-mortem within two weeks of notification while reviews are fresh:
  which review criticism was predictable at freeze time?
- Convert the submission's infrastructure — build scripts, benchmark harnesses,
  capture rigs — into reusable lab property; UIST groups compound or burn out on
  exactly this.
- Watch the next edition's site from its first announcement: dates shift by weeks
  between editions and the length rules have changed across recent cycles.

## Output format

```text
[Cycle target] UIST <year> papers / demos / posters / DS
[Today's phase] build / freeze / evaluation / video / submission / review / rebuttal / camera-ready / conference prep
[Critical path] <the single task that moves the finish date>
[Risk register] top three, each with named owner
[Next fixed date] <date + obligation>
```
