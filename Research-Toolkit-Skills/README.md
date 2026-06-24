# Research-Toolkit-Skills

**Cross-journal author workflow toolkit.** Where the per-journal depth packs answer *"how
do I clear THIS venue's bar?"*, this pack answers the cross-cutting questions that run
across venues — *which* venue, how to *run* the analysis, whether it's *ready*, what
referees will *attack*, how to *respond*, and how to ship the *replication package*.

[简体中文](README.zh-CN.md)

## The loop

```
rt-journal-match      pick the venue (185+ packs → reach/match/safe + resubmission ladder)
  → rt-execution-bridge    run the analysis via StatsPAI / Stata MCP (fitted + audited)
  → rt-submission-readiness self-check go/no-go on your own manuscript
  → rt-simulated-referee    rehearse a calibrated AE + referee panel
  → rt-response-to-referees draft the point-by-point reply after an R&R
  → rt-replication-package  assemble + validate the Data-Editor package
rt-workflow            routes across all of the above
```

## Skills

| Skill | What it does |
|---|---|
| [`rt-workflow`](skills/rt-workflow/SKILL.md) | Router across the toolkit + the lifecycle |
| [`rt-journal-match`](skills/rt-journal-match/SKILL.md) | Abstract → ranked venue shortlist + resubmission ladder |
| [`rt-execution-bridge`](skills/rt-execution-bridge/SKILL.md) | Run DiD / IV / RDD / SCM / DML + audit via MCP |
| [`rt-submission-readiness`](skills/rt-submission-readiness/SKILL.md) | Venue-parameterized go/no-go on the manuscript |
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
- **Run, don't claim.** Empirical steps execute through the StatsPAI / Stata MCP tools and
  report the actual number; citations only via `bibtex`.

## Install

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install research-toolkit-skills
/reload-plugins
```

Then: `用 rt-workflow 告诉我这份稿子下一步该投哪、怎么做实、能不能过审。`
