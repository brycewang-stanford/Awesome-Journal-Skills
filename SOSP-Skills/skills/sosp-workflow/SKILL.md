---
name: sosp-workflow
description: Use when planning a SOSP campaign across the annual cycle — back-scheduling from the spring abstract and paper deadlines, running the summer response and July notification, stacking the August camera-ready with artifact evaluation, and retargeting rejections across the SOSP/OSDI/EuroSys circuit.
---

# SOSP Workflow

Use this to place a project on the SOSP calendar and to decide what to do in the
current phase. SOSP has been **annual since 2024** (the SIGOPS announcement is at
`sigops.org/2023/sosp-is-going-annual/`), which changed campaign planning from a
two-year bet into a rolling circuit. All dates below were checked 2026-07-08.

## The 2026 cycle as the template

| Milestone (2026 cycle) | Date | Phase it opens |
|---|---|---|
| Abstract registration | March 27, 2026 (Apr 1 AoE window rendered in EDT on HotCRP) | Freeze title/authors/conflicts |
| Full paper deadline | April 2, 2026, 7:59:59 AM EDT | Review |
| Author response window | Announced with reviews, pre-PC-meeting | `sosp-author-response` |
| Notification | July 3, 2026 | Camera-ready + AE (accepted) or retarget (rejected) |
| Camera-ready | August 28, 2026 | Shepherded final version |
| Conference | Sep 29 - Oct 2, 2026, Prague, Czech Republic | Talk, posters, workshops |

As of **2026-07-08 the notification has just landed**: teams are either five days
into the acceptance track or five days into retargeting. SOSP 2027 dates are
unpublished (待核实 at `sigops.org` and `sosp.org`); the annual pattern implies a
spring 2027 deadline, but never back-schedule against an implied date — only
against a posted one.

## Accepted: three threads, two months

July 3 to August 28 runs three deadline-bound conversations in parallel, and the
standing failure is one person owning all three:

1. **Shepherd thread** — revision plan within days, agreed scope, 13th/14th page
   negotiation (see `sosp-camera-ready`). Owner A.
2. **Artifact thread** — sysartifacts registration opens days after notification;
   the evaluation window is interactive (see `sosp-artifact-evaluation`). Owner B.
3. **Logistics thread** — ACM rights form, registration, Czech-entry visas where
   needed, talk preparation. Owner C, earliest start wins on visas.

## Rejected: the retargeting circuit

Annual SOSP plus annual OSDI plus the EuroSys/ATC/NSDI ring means a systems paper
is rarely more than a few months from its next natural deadline. Retarget on a
decision tree, not on grief:

- Reviews attack **soundness** (evaluation holes, unisolated mechanisms): fix the
  evidence first; the next deadline is whichever one the new experiments make.
- Reviews attack **fit or significance** but concede soundness: the paper may be
  right for a sibling with a different center of gravity — networked-systems
  framing to NSDI, storage framing to FAST, deployment/practitioner framing to ATC.
- Reviews are **strong with one blocker**: an OSDI resubmission in the next window
  with a surgical fix and a cover-your-delta introduction paragraph is the highest
  expected-value move. Exact sibling deadlines shift every cycle (待核实 against
  each venue's current CFP before promising a date to co-authors).

## Back-scheduling the next submission

```text
T-9 months   problem locked; motivating measurement exists; skeleton design review
T-6 months   system runs end-to-end on one workload; claim list drafted
T-4 months   evaluation matrix frozen (sosp-experiments); baselines built and tuned
T-10 weeks   full experimental sweep begins; env capture automated (sosp-reproducibility)
T-6 weeks    complete draft; strict 15-minute read by an outside systems reader
T-3 weeks    evaluation freeze; figures one-command from logs
T-10 days    format compile, leak sweep, conflict list drafted (sosp-submission)
T-6 days     abstract registration
T-0          upload; verify the HotCRP-held PDF, not the local one
```

The two intervals teams misjudge: baselines (building and fairly tuning someone
else's system routinely costs a month) and the draft-to-freeze gap (a SOSP draft
that first exists three weeks before the deadline reads like it).

## Cadence discipline for a group

- Track the circuit in one shared calendar: SOSP, OSDI, EuroSys, ATC, NSDI, FAST,
  plus HotOS in odd rhythm for early-stage ideas — each with abstract and paper
  gates, refreshed from official CFPs each fall and spring.
- One project, one primary venue bet, one named fallback — deciding the fallback
  *before* notification removes the week of post-rejection drift.
- Never submit the same work to overlapping review cycles; systems venues share PC
  members and treat dual submission as an integrity violation.

## Output format

```text
[Phase] where this project sits on the cycle today
[Owners] shepherd / artifact / logistics threads assigned?
[If rejected] soundness vs fit diagnosis -> named next venue + posted deadline
[Back-schedule] T-milestones with dates against the next posted deadline
[Calendar risk] the interval currently underestimated
```
