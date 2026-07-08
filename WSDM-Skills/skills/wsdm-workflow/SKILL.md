---
name: wsdm-workflow
description: Use when planning the calendar for a WSDM submission - the single annual cycle from August abstract and paper deadlines through October notification to the February conference, backward milestone planning, the September short-paper fallback, alternate entrances (demos, WSDM Cup, doctoral consortium), and coordination with sibling-venue deadlines.
---

# WSDM Workflow

Plan a WSDM campaign around the venue's defining rhythm: one deadline a year,
in August, for a conference the following February - with no rebuttal stage
between them. Missing August costs twelve months, and nothing after August can
improve the outcome. Every date below is a 2026-cycle anchor (abstract
2025-08-07, paper 2025-08-14, notification 2025-10-23, conference 2026-02-22
to 26, Boise); the 2027 edition (20th, Hong Kong, February 15-19, 2027) had
not published verified deadlines at this pack's check date - confirm them at
wsdm-conference.org/2027 before committing the plan.

## The annual clock

```text
        T-26w  fit decision (wsdm-topic-selection) + evidence plan
        T-20w  datasets locked, split manifests written, baselines running
        T-12w  main results stable; ablation matrix complete
        T-8w   full draft; adversarial read #1 -> objection inventory
        T-4w   artifact repo review-ready; ethics section drafted
        T-1w   abstract registered (bidding-quality title+abstract)
  Aug   T=0    paper deadline, AoE     <- everything ends here
  Oct   ~T+10w notification            <- no interaction in between
  Nov+         camera-ready + ACM production (dates from acceptance email)
  Feb          single-track conference (talk/poster, registration, travel)
```

The unusual constraints, made explicit:

- **Front-load quality.** Venues with rebuttals let you defend a rushed
  evaluation; WSDM does not. The T-8w adversarial read is the highest-leverage
  meeting of the campaign - schedule it like a deadline.
- **The August-to-October silence** is planning time, not waiting time: prepare
  the camera-ready artifact conversion and, in parallel, the rejection fork
  (below), so either outcome executes immediately.
- **February logistics are real work**: winter travel, visas for the host
  country (Hong Kong in 2027), industry disclosure approvals for the final
  version - start each at notification, not in January.

## The September pressure valve

Since 2026 the series runs a short-paper track with deadlines about a month
after the long-paper deadline (2026 anchor: announced September 11/18, with
registry evidence of an extension to September 18/25 - verify the current
year's dates directly). Plan uses:

- A long paper that is honestly two results and a wish can be split in July:
  the strong, focused result targets the short track; the broader project waits
  a year and arrives with more evidence.
- A near-miss at the long deadline (evaluation incomplete) degrades gracefully
  to the short track instead of slipping twelve months.
- Do not treat "short" as "unfinished": the 2026 call asked for solid,
  empirically validated contributions, capped submissions at 10 per author,
  and desk-rejected placeholder abstracts.

## Alternate entrances to the same room

| Entrance | Typical timing (verify per edition) | What it earns |
|---|---|---|
| Long paper | August deadline | Archival full paper + single-track talk |
| Short paper | ~September deadline (since 2026) | Archival concise paper |
| Demonstration | Autumn deadline; 4-page cap in 2026 | Archival demo paper + demo floor |
| WSDM Cup | Task-specific autumn schedule | Challenge standing + workshop-style exposure |
| Doctoral consortium | Autumn deadline | Mentoring + community entry for PhD students |
| Industry Day talk | CFP per edition (2026 theme: LLMs and agentic AI in industry) | Non-archival visibility with the practitioner half of the venue |

A lab shipping a system can rationally take two entrances in one year (e.g.,
short paper + demo) - check the current calls' dual-submission language first.

## Coordinating with the sibling calendar

WSDM's August deadline sits inside a lattice of neighbors (all timings
approximate and cycle-volatile - verify each): SIGIR around January/February,
TheWebConf around October, CIKM around May, RecSys in spring, KDD's two cycles
around August and February. Two standard plays:

- **Forward chain:** a paper rejected from SIGIR (decisions in spring) has a
  natural summer revision window before WSDM's August deadline - the reviews
  arrive in time to act on them.
- **Backward chain:** a WSDM rejection in October reaches SIGIR or KDD Cycle 2
  in winter with fixes applied. Map the chain *before* submitting, so the
  October decision triggers execution instead of deliberation.

Never dual-submit along the chain: these are archival venues with standard
concurrent-submission prohibitions; the chain is sequential by definition.

## Contingencies

- **Deadline extension announced:** treat extra days as validation time, not
  new-experiment time; late-added results are the least-reviewed and
  most-attacked parts of a paper at a no-rebuttal venue.
- **A competing preprint appears in July:** do not race it with rushed
  experiments. Add the contrast citation, sharpen the delta sentence, and let
  the August version be correct rather than first-and-fragile.
- **Key experiment breaks at T-2w:** invoke the valve - descope the claim to
  what stands, or pivot to the short track - rather than shipping a table you
  cannot defend to reviewers you cannot answer.
- **Chair announcement contradicts the CFP:** newest official instruction
  wins; log both with dates (precedence order in
  `../../resources/external_tools.md`).

## Team operating rules

1. One owner for the EasyChair record: account, abstract text, author order,
   conflicts, final PDF upload.
2. The objection inventory (started at T-8w) is a living document with named
   owners per objection; unresolved rows at T-1w force claim reductions.
3. The artifact repo freezes at T-1w except README fixes - late code churn
   breaks the numbers-match-paper invariant more often than it helps.
4. Log every date-fact with its source URL the day you verify it; August
   deadline drift (extensions happen) is checked weekly in the final month
   against the official site, not social media.

## Output format

```text
[Cycle] target edition + verified deadlines (source + check date)
[Milestones] T-26w..T-0 with owners; current slack per milestone
[Valve decision] long / long+short split / short / defer, with reason
[Alternate entrances] pursued this year: <list or none>
[Chain map] pre-WSDM source venue / post-WSDM destination, with dates
[Logistics] visa / registration / disclosure lead items and start dates
```
