---
name: rt-response-to-referees
description: Use after an R&R (or the simulated rehearsal) to turn a referee report into a point-by-point response letter plus a revision plan — editor first, every comment answered, each empirical fix backed by a real re-run via the target pack's skill and the execution bridge. Defers the venue's response format to the pack + source-map.
---

# Response-to-Referees (rt-response-to-referees)

Draft the reply that decides the second round. Full method:
[`shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md).

## When to trigger

- An R&R letter has arrived and needs a point-by-point response + revision.
- You want to convert `rt-simulated-referee` output into a rehearsed reply.

## What it does

1. **Inventory every comment** (per referee + AE), tag major/minor, substantive/clarification.
2. **Editor first** — lead with the AE's decisive concerns.
3. **Classify each response** honestly: concede & fix / address partially / push back with
   evidence (rarely, and only when right).
4. **Back substantive fixes with a real re-run** — map each empirical comment to the pack
   skill + `rt-execution-bridge`; the number in the reply must be one you actually computed.
5. **Write the letter** — quote each comment, respond beneath it, point to the exact change.
6. **Summarize the changes** in a scannable table.

## Hard rules

1. **Editor first**, then referees.
2. **Every claimed fix corresponds to a real change/re-run**; empirical claims cite a number
   produced via the execution bridge.
3. **Answer every comment** — none silently dropped.
4. **Venue response format from the pack + source-map** (some cap length / want a structure).
5. It drafts a *reply*; the author owns final scientific sign-off.

## Output format

```
【Cover note to editor】how the decisive concerns were addressed
【Referee 1】R1.1 (quote) → concede&fix / partial / push-back · what changed · where · new number
【Referee 2】… 【AE】(decisive points first)
【Summary of changes】comment → change → location
【Open/declined】comments not fully addressed, with the honest reason
```

## Anti-patterns

- Silent omission; defensive tone / blanket push-back; "we addressed this" with no real
  edit; burying the AE's load-bearing concern.

Next: regenerate affected outputs in `rt-replication-package` so the package matches the revision.
