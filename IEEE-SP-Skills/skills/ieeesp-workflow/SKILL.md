---
name: ieeesp-workflow
description: Use when planning an IEEE S&P (Oakland) submission calendar across the two-cycle year, including registration-versus-paper deadlines, the early-reject and rebuttal windows, Revise resubmission timing, the one-year embargo clock, and choosing which cycle a project can realistically hit.
---

# IEEE S&P Workflow

Use this to run a project against S&P's calendar. Unlike single-deadline ML
venues, each S&P symposium accepts papers through **multiple submission
cycles**, each a self-contained mini-conference with its own HotCRP site,
registration freeze, review rounds, and decision date. Planning means choosing
a cycle, not "the deadline."

## The S&P 2027 cycle map (checked 2026-07-08, all dates 待核实 before use)

| Milestone | Cycle 1 | Cycle 2 |
|---|---|---|
| Abstract registration (title/abstract/authors/ORCIDs frozen) | Jun 5, 2026, 7:59:59 AM EDT | Nov 10, 2026 |
| Full paper due | Jun 12, 2026 | Nov 17, 2026 |
| Early-reject notification | 待核实 | Jan 18, 2027 |
| Reviews released to surviving papers | 待核实 | Feb 11, 2027 |
| Rebuttal due | 待核实 | Feb 16, 2027 |
| Decision (Accept / Revise / Reject) | 待核实 | Mar 5, 2027 |
| Symposium (Montreal, Canada) | May 2027 | May 2027 |

Two planning facts bite hardest. First, **Cycle 1 for 2027 closed on June 12,
2026** — as of this pack's check date the open path is Cycle 2. Second, S&P
states deadlines in a fixed clock time (7:59:59 AM EDT for Cycle 1), **not
AoE**; a team assuming Anywhere-on-Earth loses most of a day.

## Registration week is the real deadline

At S&P, the registration deadline is substantive: the final title, complete
abstract, full author list with ORCIDs, and declared conflicts are locked on
HotCRP one week before the paper is due, and none of it may change afterwards.
ORCID records must match HotCRP names and emails or the paper is desk
rejected. Treat registration week as the week author-list politics, ORCID
housekeeping, and conflict declarations get resolved — not deadline night.

## Backward schedule from a cycle

```text
T-16w  Threat model + evidence plan frozen (ieeesp-topic-selection)
T-12w  Core exploit / adaptive evaluation / measurement running
T-8w   Ethics work: disclosure sent to vendors, IRB determination
       in hand — these have external latency you cannot compress
T-4w   Full draft; internal adversarial read by a non-author
T-1w   REGISTRATION: title, abstract, authors+ORCIDs, conflicts,
       Ethics Considerations field on HotCRP — then frozen
T-0    Paper upload (13 pages + ≤5 refs/appendix, compsoc template)
T+~9w  Early-reject notice; if surviving: reviews + 5-day rebuttal
T+~16w Decision: Accept (shepherded camera-ready) / Revise / Reject
```

The item teams misplace is the ethics latency at T-8w: responsible-disclosure
clocks and IRB reviews run on other institutions' calendars, and the
registration-time Ethics Considerations field must describe work already done,
not intentions.

## Branch plans for the three outcomes

- **Accept** — expect a draft meta-review plus a shepherd who checks concerns
  off as the camera-ready resolves them; budget real revision time, not a
  formatting pass (`ieeesp-camera-ready`).
- **Revise** — a structured major revision with a summary of expectations;
  this is the venue's signature second chance. Plan it as a project with an
  owner and a deadline, not as "address comments" (`ieeesp-review-process`).
- **Reject** — the one-year embargo runs from the *original submission date*,
  and anything ≥~40% overlapping counts as a resubmission. The productive
  branch is usually a sibling venue whose deadline falls inside the embargo
  window.

## Choosing between cycles

- Pick the **later cycle** when the adaptive evaluation or disclosure process
  is incomplete — an early reject costs the venue for a year of that paper's
  life, and first-round reviewers do not see rebuttals.
- Pick the **earlier cycle** when the work is done and a Revise outcome would
  still land the paper in the same symposium year.
- Never plan on submitting the same work to two S&P cycles back-to-back
  without checking the current CFP's resubmission wording — the embargo
  applies across cycles, not just across years.

## Standing risks to assign owners

| Risk | Owner action |
|---|---|
| Registration freeze missed | Calendar registration week, not paper week |
| Timezone misread (EDT vs AoE) | Convert official time on day one |
| Disclosure/IRB latency | Start at T-8w; log vendor contact dates |
| Embargo collision | Check prior S&P rejections before committing |
| Shepherd turnaround post-accept | Reserve author time in the decision month |

## Output format

```text
[Target] S&P <year>, Cycle <n> (registration <date>, paper <date>)
[Today→registration] <n> weeks; feasibility: on-track / tight / unrealistic
[Ethics latency] disclosure started? IRB determination? <status>
[Embargo] clear / blocked until <date>
[Branch plans] accept: <owner> · revise: <owner> · reject: <next venue>
```
