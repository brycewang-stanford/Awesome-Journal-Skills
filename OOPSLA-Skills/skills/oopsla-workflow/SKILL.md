---
name: oopsla-workflow
description: Use when planning an OOPSLA campaign on the two-round clock — choosing October vs April entry, budgeting for Minor or Major Revision paths, mapping acceptance to the OOPSLA1 or OOPSLA2 PACMPL issue, scheduling artifact evaluation, and landing the SPLASH talk, with dates re-anchored to the live cycle.
---

# OOPSLA Workflow

OOPSLA gives a paper *two doors per year* into the same PACMPL volume — for
2027, October 14, 2026 (Round 1 → Issue OOPSLA1, published no earlier than
April 1, 2027) and April 7, 2027 (Round 2 → Issue OOPSLA2, no earlier than
October 1, 2027), with all outcomes presented in person at SPLASH 2027
(Prague, October 10–15, 2027). Planning an OOPSLA campaign is therefore a
routing problem over rounds and revision outcomes, not a countdown to a
single deadline. As of 2026-11-24 Round 1 has closed (author response
December 1–5, 2026; notification December 18, 2026; revisions due January
22, 2027) and the next open door is **Round 2, April 7, 2027** (author
response June 15–19, notification July 2, revisions July 30, final
notification August 13, camera-ready August 27, 2027) — re-anchor every
date below to live pages.

## Door choice: October vs April

| Factor | Favors the October round | Favors the April round |
| --- | --- | --- |
| Revision insurance | Major Revision lands in April, **same volume** | Major Revision waits ~6 months for next volume's R1 |
| Publication timing | April issue; citable before the conference | October issue; publishes near conference time |
| Evidence maturity | Requires the evaluation done by early fall | Buys a winter of experiments |
| Team calendar | Summer build, fall write | Fall build, winter write |
| Talk lead time | Long runway to SPLASH | Acceptance close to travel booking |

Default heuristic: enter the earliest round where the *evidence* (not the
prose) is complete — the revision insurance of the early round compounds,
because the most likely non-accept outcome for solid work is a revision, and
same-volume revision is the cheapest one available anywhere in the SIGPLAN
family.

## Campaign state machine

```text
PLAN ──> ROUND N SUBMITTED ──> RESPONSE WINDOW ──> outcome?
  Accept ─────────────► CAMERA-READY ► ARTIFACT ► ISSUE ► SPLASH TALK
  Minor Revision ─────► execute list by the round's revision deadline
                        (or wait for the next round) ► (as Accept)
  Major Revision ─────► revise against expectations ► ROUND N+1 (same
                        reviewers where possible)
  Reject ─────────────► diagnose ► re-route (oopsla-topic-selection)
                        or rebuild ► next volume (an R1 reject may
                        not re-enter R2 of the same volume)
Each transition has an owner and a date pulled from the live track page.
```

## Backward plan from a target round (T = deadline)

- **T-12 to T-8 weeks** — freeze claim list; run `oopsla-experiments`
  routing; start the demand matrix and reproducibility ledger.
- **T-8 to T-4** — full draft in the 23-page frame; related-work family
  sweep (`oopsla-related-work`); internal red-team read using the four
  SIGPLAN pillars.
- **T-4 to T-1** — style pass (`oopsla-writing-style`); appendix layering
  (`oopsla-supplementary`); Data-Availability Statement drafted from the
  ledger.
- **Final 72 hours** — the filing-day sequence in `oopsla-submission`.
- **Post-submission** — pre-write response scaffolding: the concerns you
  already know about, with PDF pointers ready for the round's response window.

## Revision-path budgeting

Reserve capacity *after* submission: the two most probable outcomes for
competent work — Minor and Major Revision — both demand engineering time on
a fixed clock. A team that disbands to other projects the week after the
deadline systematically converts Minor Revisions into missed opportunities.
Rule of thumb: hold 20% of the build team's time in reserve until the
outcome letter, then re-plan against the actual expectation list.

## Post-acceptance rail

Camera-ready reconciliation (`oopsla-camera-ready`) → artifact kick-the-tires
and badges (`oopsla-artifact-evaluation`) → Zenodo DOI into the final
statement → issue publication → SPLASH registration, talk, and optional
poster. The talk lands months after OOPSLA1 publication — plan it as a
presentation of known work, and budget travel to the SPLASH city early.

## Output format

```text
[Cycle anchor] current volume + next open round (live URL + date checked)
[Door choice] round + rationale from the table
[State] position in the state machine
[Reserve] revision capacity held + expiry
[Next transition] owner, date, blocking items
```
