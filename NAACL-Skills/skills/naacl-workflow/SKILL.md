---
name: naacl-workflow
description: Use when planning a research project's calendar toward NAACL — handling the chapter's skipped-year rhythm, choosing an ARR cycle when the edition's feeding cycles are not yet announced, backward-planning data and annotation work, and keeping a decision tree for commit-versus-wait-versus-reroute moments.
---

# NAACL Workflow

Project management for NAACL differs from every annual venue in one blunt
way: the conference might not exist next year. The chapter historically
skips editions when the ACL main meeting is hosted in the Americas — no
NAACL 2023, no NAACL 2026 — so a NAACL plan is really a plan for entering
the *ACL Rolling Review machine at a moment that leaves a NAACL commitment
open, with named fallbacks for when the calendar shifts under you.

## The calendar reality (as of 2026-07-08)

- Most recent editions: NAACL 2024 (Mexico City, June 16-21, 2024) and
  NAACL 2025 (Albuquerque, April 29 - May 4, 2025).
- Next edition: NAACL 2027 — site registered, but dates, venue, feeding
  cycles, and commitment deadline all 待核实 at planning time.
- Reference shape from 2025: ARR upload mid-October, reviews mid-December,
  commitment around the turn of the year, final versions early February,
  conference late April. A spring NAACL implies an autumn ARR deadline —
  plan provisionally on that shape, verify the moment the CFP lands.

```text
Provisional backward plan for a spring NAACL (verify every date):
  T-0   conference (spring)
  T-11w final versions due
  T-16w commitment deadline           <- reviews must exist by here
  T-26w ARR cycle submission          <- the real deadline
  T-30w evidence freeze: data, annotation, main runs complete
  T-38w annotation campaign starts (if collecting new data)
  T-46w pilot studies + guideline drafting
```

## Milestones with owners

| Milestone | Owner | Exit criterion |
|---|---|---|
| Venue decision review | Whole team | NAACL still the target? (rerun quarterly — see decision tree) |
| Data/annotation freeze | Data lead | Agreement scores computed; splits published internally |
| Main-results freeze | Experiments lead | Ledger complete; variance reported |
| Paper freeze | Writing lead | Content pages self-contained; Limitations drafted |
| Compliance pass | One named person | Checklist, anonymity, template, citations verified |
| ARR upload | Corresponding author | Confirmation email archived |
| Response window | All authors on call | Every review answered per triage |
| Commitment decision | Senior author | Decision logged with rationale |

Annotation campaigns deserve the earliest slot they can get. Recruiting
annotators for Guaraní or Haitian Creole is not a two-week task, and
community partnerships — common for Americas-language projects — move at
partnership speed, not deadline speed.

## The commit-versus-wait decision tree

Reviews arrive; now the genuinely NAACL-specific decision:

1. **Strong package, NAACL window open** → commit to NAACL.
2. **Strong package, no NAACL window soon** → commit to the nearest
   fitting sibling (EMNLP, EACL, AACL, or ACL) rather than letting reviews
   age a year; NAACL loyalty is not worth a stale paper.
3. **Fixable weaknesses** → revise and resubmit to a later ARR cycle with a
   change summary, timed so the *new* reviews land before the NAACL
   commitment deadline.
4. **Field moving fast under the paper** → prefer earlier venues over
   waiting; a skipped-year gap is long enough for your baselines to become
   historical artifacts.

Log the decision and the date; teams that skip the log relitigate the same
choice monthly.

## Monitoring routine between editions

Between the decision to target NAACL and the edition's CFP, run a light
monthly watch instead of a panicked scramble later:

- ARR dates page: has any cycle acquired a NAACL assignment?
- Chapter site and the edition placeholder (`{year}.naacl.org`): dates,
  venue, or organizing-committee announcements.
- The chapter's announcement channels and the ACL Member Portal, where
  cycle-to-conference mappings are often posted first.
- On any hit: update the backward plan the same week, and rerun the
  decision tree with the real dates.

Assign the watch to one named person; a "we all sort of watch" arrangement
reliably discovers CFPs three weeks late, which on a ten-week cycle is
fatal.

## Standing risks on a NAACL path

- **Announcement risk:** feeding cycles for a new edition can be announced
  with little slack; subscribe to the chapter's channels and recheck the
  ARR dates page monthly once an edition is expected.
- **Pool-depth risk:** post-gap commitment pools are deep; a borderline
  package should strengthen or reroute, not hope.
- **Single-point compliance risk:** desk rejects (template, Limitations,
  checklist) burn the whole cycle — ten weeks lost, not ten days.
- **Deadline convention risk:** all ARR clocks run AoE (UTC-12); a team
  spread across the Americas' time zones still gets exactly one cutoff.

## Output format

```text
[Target edition] <NAACL year, or "unannounced — provisional plan">
[Cycle chosen] <ARR month/year + verification date>
[Backward plan] <milestone -> date -> owner>
[Decision-tree state] commit / wait / revise / reroute (+ rationale)
[Top calendar risk] <one line>
```
