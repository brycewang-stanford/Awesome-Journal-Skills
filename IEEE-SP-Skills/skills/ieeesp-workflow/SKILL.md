---
name: ieeesp-workflow
description: Use when planning an IEEE S&P (Oakland) submission calendar across the two-cycle year, including registration-versus-paper deadlines, the early-reject, rebuttal and interactive-rebuttal windows, the shepherd and camera-ready dates, the one-year embargo clock, and choosing which cycle a project can realistically hit.
---

# IEEE S&P Workflow

Use this to run a project against S&P's calendar. Unlike single-deadline ML
venues, each S&P symposium accepts papers through **multiple submission
cycles**, each a self-contained mini-conference with its own HotCRP site,
registration freeze, review rounds, and decision date. Planning means choosing
a cycle, not "the deadline."

## The S&P 2027 cycle map (re-verified 2026-11-24 on the live CFP)

| Milestone | Cycle 1 | Cycle 2 |
|---|---|---|
| Abstract registration (title/abstract/authors/ORCIDs frozen; 6-paper cap counted) | Jun 4, 2026 | Nov 10, 2026 |
| Full paper due | Jun 11, 2026 | Nov 17, 2026 |
| Early-reject notification | Jul 27, 2026 | Jan 18, 2027 |
| Reviews released to surviving papers | Aug 20, 2026 | Feb 11, 2027 |
| Rebuttal text due (750 words) | Aug 27, 2026 | Feb 16, 2027 |
| Interactive rebuttal + revised PDF (if assigned) | Aug 26 - Sep 3, 2026 | Feb 17 - 26, 2027 |
| Decision (Accept / Reject) | Sep 11, 2026 | Mar 5, 2027 |
| Submission to shepherd | Oct 2, 2026 | Mar 26, 2027 |
| Camera-ready | Oct 16, 2026 | Apr 8, 2027 |
| Symposium (Montreal, Canada) | May 17-19, 2027 | May 17-19, 2027 |

All deadlines are **23:59:59 AoE**; the HotCRP pages display the same instant
in US Eastern time (e.g., 7:59:59 AM EDT the next morning). Two planning
facts bite hardest. First, **both S&P 2027 cycles have closed** (the Cycle 2
paper deadline was November 17, 2026), and S&P 2028 had no published call on
2026-11-24 — the next door is S&P 2028 Cycle 1, expected around mid-2027 by
the 2027 pattern but not yet announced. Second, HotCRP's 24-hour rule: drafts
must be in a day early, and server failures in the final 24 hours earn no
extension.

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
T+~7-9w Early-reject notice; if surviving: reviews + 750-word rebuttal
        (+ ~1-week interactive period if assigned)
T+~13-16w Decision: Accept (shepherded camera-ready) / Reject
```

The item teams misplace is the ethics latency at T-8w: responsible-disclosure
clocks and IRB reviews run on other institutions' calendars, and the
registration-time Ethics Considerations field must describe work already done,
not intentions.

## Branch plans for the outcomes

- **Accept** — expect a draft meta-review plus a shepherd who checks concerns
  off as the camera-ready resolves them; budget real revision time, not a
  formatting pass (`ieeesp-camera-ready`).
- **Interactive rebuttal** (before the decision, if the PC assigns it) — the
  only chance to add requested results, with a revised PDF, inside about a
  week. Plan it as a project with an owner, not as "address comments"
  (`ieeesp-review-process`). There is no Revise outcome after the decision.
- **Reject** — the one-year embargo runs from the *original submission date*,
  and a very similar intellectual contribution counts as a resubmission
  however rewritten. The productive
  branch is usually a sibling venue whose deadline falls inside the embargo
  window.

## Choosing between cycles

- Pick the **later cycle** when the adaptive evaluation or disclosure process
  is incomplete — an early reject costs the venue for a year of that paper's
  life, and first-round reviewers do not see rebuttals.
- Pick the **earlier cycle** when the work is done: an accepted Cycle 1 paper
  is published open access within about a month of acceptance, months before
  the symposium.
- Never plan on submitting the same work to two S&P cycles back-to-back
  without checking the current CFP's resubmission wording — the embargo
  applies across cycles, not just across years.

## Standing risks to assign owners

| Risk | Owner action |
|---|---|
| Registration freeze missed | Calendar registration week, not paper week |
| Timezone misread (HotCRP EDT display vs CFP AoE) | Convert official time on day one; submit a draft 24 h early |
| Disclosure/IRB latency | Start at T-8w; log vendor contact dates |
| Embargo collision | Check prior S&P rejections before committing |
| Shepherd turnaround post-accept | Reserve author time in the decision month |

## Output format

```text
[Target] S&P <year>, Cycle <n> (registration <date>, paper <date>)
[Today→registration] <n> weeks; feasibility: on-track / tight / unrealistic
[Ethics latency] disclosure started? IRB determination? <status>
[Embargo] clear / blocked until <date>
[Branch plans] interactive rebuttal: <owner> · accept/shepherd: <owner> · reject: <next venue>
```
