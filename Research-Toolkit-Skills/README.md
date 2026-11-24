# Research-Toolkit-Skills

**Cross-journal author workflow toolkit.** Where the per-journal depth packs answer *"how
do I clear THIS venue's bar?"*, this pack answers the cross-cutting questions that run
across venues — *which* venue, how to *run* the analysis, whether it's *ready*, what
referees will *attack*, how to *respond*, and how to ship the *replication package*.

[简体中文](README.zh-CN.md)

## The loop

```
paper-profile.yml     write the five signals down once; everything below reads it
rt-journal-match      pick the venue (744 indexed venues → reach/match/safe + ladder)
  → rt-ladder-ev           price the ladder in months and in P(ever placing)
  → rt-venue-integrity     verify a venue this index does not cover, before submitting
  → rt-venue-reframe       diff the paper from its old venue's framing to the new one
  → rt-execution-bridge    run the analysis via StatsPAI / Stata MCP (fitted + audited)
  → rt-submission-readiness the pre-submission pipeline on your actual file:
                            preflight → scorecard → referee panel → polish → letter → re-run
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
| [`rt-submission-readiness`](skills/rt-submission-readiness/SKILL.md) | The pre-submission pipeline on the real file: deterministic preflight against the venue's verified rules, nine-dimension scorecard, referee panel, claim-to-evidence polish, cover letter + statements, re-run diff |
| [`rt-desk-reject-risk`](skills/rt-desk-reject-risk/SKILL.md) | Ranked risk report against the target's documented desk-reject triggers |
| [`rt-simulated-referee`](skills/rt-simulated-referee/SKILL.md) | AE desk-screen + independent referees on the venue family's real review form, verified and synthesized |
| [`rt-response-to-referees`](skills/rt-response-to-referees/SKILL.md) | R&R → point-by-point reply + revision plan |
| [`rt-replication-package`](skills/rt-replication-package/SKILL.md) | Assemble + validate the Data-Editor package |

## Pre-submission polishing (rt-submission-readiness)

The flagship workflow. Give it the manuscript file and the target venue:

```bash
python3 resources/preflight/preflight.py paper.pdf --venue "Journal of Finance"   # inside this pack
python3 tools/preflight.py paper.tex --venue icml --json                           # from a repo clone
python3 resources/preflight/preflight.py --list-venues                             # venues with verified rules
```

Stage 0 is deterministic: abstract/word/page limits, double-blind anonymization (names,
self-citations, acknowledgments, non-anonymous links, file metadata), every statement the
venue requires, citations ↔ references (optionally verified on Crossref), exhibit
numbering, cross-references and standard-error notes, abstract numbers traced to the
tables, placeholders and tracked changes. Venue limits come from a rules block in each
pack's `official-source-map.md`, re-verified against the official pages and kept
consistent with the prose by CI. The skill then runs the scorecard, a referee panel on
the venue family's real review form, a claim-to-evidence polish, and the cover letter
and statements the venue asks for — and re-runs after the author's fixes. Measured on a
seeded-defect benchmark:
[`showcase/presubmission-benchmark/`](https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/showcase/presubmission-benchmark/README.md).

## Design

- **Venue-neutral.** The toolkit picks the venue, runs the analysis, and rehearses review;
  the **venue bar and all live facts** (fees, limits, acceptance, data policy, house style)
  come from the chosen pack's own skills and `resources/official-source-map.md`.
- **Backed by canonical capability docs** in `shared-resources/` (`journal-selection/`,
  `empirical-methods/`, `submission-readiness/`), vendored into
  [`resources/shared/`](resources/shared/) so they resolve from a plugin install — the skills are the triggerable entry points; the deep
  methodology + validated worked-examples (DiD / IV / RDD / SCM / DML, all real tool runs)
  live there once.
- **Measured, not asserted.** Venue shortlisting runs `tools/match_venues.py` over a
  generated index of 744 venues with an adjacency graph for the resubmission ladder, and
  **the evaluation scores that same code path** against a gold set split into a tuning
  half and a held-out half — on the held-out half, R@10 = 65.7% from a bare title, 77.7%
  with the discipline supplied (2026-11-23)
  ([`shared-resources/journal-selection/eval/`](resources/shared/journal-selection/eval/README.md)).
  Retrieval produces a reading list; the recommendation still comes from the venue's own pack.
- **One profile, many skills.** The five signals about the paper are written once, as
  [`paper-profile.yml`](resources/shared/journal-selection/paper-profile.md), instead
  of each skill re-deriving them from the manuscript and quietly disagreeing.
- **Run, don't claim.** Empirical steps execute through the StatsPAI / Stata MCP tools and
  report the actual number; citations only via `bibtex`.

## Install

The pack is self-contained for pre-submission work (preflight + compiled venue rules +
the readiness docs ship inside it). `rt-journal-match` also needs the repository's venue
index; after `/plugin marketplace add` it is already on disk at
`~/.claude/plugins/marketplaces/awesome-journal-skills/` (the skill looks there first).

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install research-toolkit-skills
/reload-plugins
```

Then: `用 rt-workflow 告诉我这份稿子下一步该投哪、怎么做实、能不能过审。`
