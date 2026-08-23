# Paper profile — the five signals, written down once

Step 1 of [`journal-match.md`](journal-match.md) asks for five things: discipline,
method, contribution type, setting, ambition. Every other cross-journal skill needs the
same five, and each was re-deriving them from scratch — `rt-desk-reject-risk` re-read the
manuscript to learn its design, `rt-venue-reframe` re-decided its contribution type,
`rt-ladder-ev` re-guessed its ambition. Three readings of one paper produce three
slightly different papers, and the disagreement surfaces as advice that contradicts
itself across a single session.

So write the profile **once**, keep it in the working directory, and pass it along.

```yaml
# paper-profile.yml
title: "Minimum wages and local labour markets: evidence from a staggered rollout"
discipline: economics/labor          # a value from `match_venues.py --list-disciplines`
adjacent: [economics, economics/public]   # optional; the matcher widens to these anyway
method: DiD                          # DiD | IV | RDD | structural | lab-experiment
                                     # | survey-SEM | qualitative | theory | meta-analysis
lane: empirical                      # empirical | theory | review | qualitative
contribution: new-fact               # new-fact | new-mechanism | new-method
                                     # | new-theory | replication | policy-evaluation
setting:
  region: international              # international | china  (matches the index column)
  country: US
  data: administrative payroll records, 2005-2019
  proprietary: false                 # drives the data-and-code policy check
ambition: field                      # general-interest | field | specialist
                                     # be honest: this calibrates reach vs safe
constraints:
  clock: "job market, decision needed by March"   # or empty
  budget_apc: none                   # what the author can actually pay
  anonymisable: true                 # can the paper be blinded if the venue requires it
history: []                          # venue_ids that have already rejected it
```

## Who reads which field

| Field | Used by | For |
|---|---|---|
| `title`, abstract text | `rt-journal-match` | the query passed to `tools/match_venues.py` |
| `discipline`, `adjacent` | `rt-journal-match` | the discipline prior (Step 2) |
| `lane` | `rt-journal-match` | dropping venues that publish no work of this kind |
| `method`, `contribution` | `rt-journal-match`, `rt-venue-reframe` | fit judgement (Step 3), the reframing diff |
| `setting.region`, `setting.proprietary` | `rt-journal-match`, `rt-desk-reject-risk` | region filter; data-and-code policy feasibility |
| `ambition` | `rt-journal-match`, `rt-ladder-ev` | the reach / match / safe split, and the ladder's odds |
| `constraints.clock`, `constraints.budget_apc` | `rt-ladder-ev` | which ladder is affordable in time and money |
| `constraints.anonymisable` | `rt-desk-reject-risk` | anonymity triggers |
| `history` | `rt-journal-match`, `rt-ladder-ev` | `--exclude`; where the ladder starts |

## Rules

1. **The profile holds judgements about the paper, never facts about venues.** No fees,
   acceptance rates, turnaround or page limits — those are read live from each pack's
   `resources/official-source-map.md` at the moment they are used.
2. **`ambition` is the field authors get wrong.** It is a claim about how general the
   result is, not about how much work went into it. Over-stating it produces a shortlist
   of reaches and a year of desk rejects.
3. **Update it, don't fork it.** After a reject, append to `history` and revisit
   `ambition`; do not start a second profile.
4. **An absent field is absent, not false.** If the author has not said what they can
   pay, leave `budget_apc` empty and ask before recommending a venue with an APC.

---
*Part of [`journal-selection/`](README.md). Produced in Step 1 of
[`journal-match.md`](journal-match.md); consumed across
[`Research-Toolkit-Skills`](../../Research-Toolkit-Skills/README.md).*
