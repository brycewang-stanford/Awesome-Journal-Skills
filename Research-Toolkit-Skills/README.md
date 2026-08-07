# Research-Toolkit-Skills

**Cross-journal author workflow toolkit.** Where the per-journal depth packs answer *"how
do I clear THIS venue's bar?"*, this pack answers the cross-cutting questions that run
across venues — *which* venue, how to *run* the analysis, whether it's *ready*, what
referees will *attack*, how to *respond*, and how to ship the *replication package*.

[简体中文](README.zh-CN.md)

## The loop

```
paper-profile.yml     write the five signals down once; everything below reads it
rt-journal-match      pick the venue (743 indexed venues → reach/match/safe + ladder)
  → rt-ladder-ev           price the ladder in months and in P(ever placing)
  → rt-venue-integrity     verify a venue this index does not cover, before submitting
  → rt-venue-reframe       diff the paper from its old venue's framing to the new one
  → rt-execution-bridge    run the analysis via StatsPAI / Stata MCP (fitted + audited)
  → rt-submission-readiness self-check go/no-go on your own manuscript
  → rt-desk-reject-risk    score the draft against the venue's own desk-reject triggers
  → rt-simulated-referee    rehearse a calibrated AE + referee panel
  → rt-response-to-referees draft the point-by-point reply after an R&R
  → rt-replication-package  assemble + validate the Data-Editor package
rt-workflow            routes across all of the above
```

## Skills

| Skill | What it does |
|---|---|
| [`rt-workflow`](skills/rt-workflow/SKILL.md) | Router across the toolkit + the lifecycle |
| [`rt-journal-match`](skills/rt-journal-match/SKILL.md) | Abstract → ranked venue shortlist + resubmission ladder, via `tools/match_venues.py` |
| [`rt-ladder-ev`](skills/rt-ladder-ev/SKILL.md) | Cost a submission sequence: expected months, P(placed), P(ladder exhausted) |
| [`rt-venue-integrity`](skills/rt-venue-integrity/SKILL.md) | Source-by-source verification of a venue outside the index — indexing, publisher, board, fees |
| [`rt-venue-reframe`](skills/rt-venue-reframe/SKILL.md) | Venue A → venue B reframing diff across claim, arc, evidence, style, policy |
| [`rt-execution-bridge`](skills/rt-execution-bridge/SKILL.md) | Run DiD / IV / RDD / SCM / DML + audit via MCP |
| [`rt-submission-readiness`](skills/rt-submission-readiness/SKILL.md) | Venue-parameterized go/no-go on the manuscript |
| [`rt-desk-reject-risk`](skills/rt-desk-reject-risk/SKILL.md) | Ranked risk report against the target's documented desk-reject triggers |
| [`rt-simulated-referee`](skills/rt-simulated-referee/SKILL.md) | Calibrated AE + referee rehearsal |
| [`rt-response-to-referees`](skills/rt-response-to-referees/SKILL.md) | R&R → point-by-point reply + revision plan |
| [`rt-replication-package`](skills/rt-replication-package/SKILL.md) | Assemble + validate the Data-Editor package |

## Design

- **Venue-neutral.** The toolkit picks the venue, runs the analysis, and rehearses review;
  the **venue bar and all live facts** (fees, limits, acceptance, data policy, house style)
  come from the chosen pack's own skills and `resources/official-source-map.md`.
- **Backed by canonical capability docs** in
  [`shared-resources/`](../shared-resources/) (`journal-selection/`, `empirical-methods/`,
  `submission-readiness/`) — the skills are the triggerable entry points; the deep
  methodology + validated worked-examples (DiD / IV / RDD / SCM / DML, all real tool runs)
  live there once.
- **Measured, not asserted.** Venue shortlisting runs `tools/match_venues.py` over a
  generated index of 743 venues with an adjacency graph for the resubmission ladder, and
  **the evaluation scores that same code path** against a 1,738-paper gold set split into
  a tuning half and a held-out half — R@10 = 40.5% from a bare title, 51.3% with the
  discipline supplied
  ([`shared-resources/journal-selection/eval/`](../shared-resources/journal-selection/eval/README.md)).
  Retrieval produces a reading list; the recommendation still comes from the venue's own pack.
- **One profile, many skills.** The five signals about the paper are written once, as
  [`paper-profile.yml`](../shared-resources/journal-selection/paper-profile.md), instead
  of each skill re-deriving them from the manuscript and quietly disagreeing.
- **Run, don't claim.** Empirical steps execute through the StatsPAI / Stata MCP tools and
  report the actual number; citations only via `bibtex`.

## Install

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install research-toolkit-skills
/reload-plugins
```

Then: `用 rt-workflow 告诉我这份稿子下一步该投哪、怎么做实、能不能过审。`
