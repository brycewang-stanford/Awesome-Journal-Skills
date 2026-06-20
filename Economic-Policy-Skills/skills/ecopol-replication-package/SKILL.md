---
name: ecopol-replication-package
description: Use when assembling the data, code, and verification materials for an Economic Policy (EP) manuscript so results are accessible and replicable to the journal's standard. Builds the verification-ready package; it does not invent evidence or citations.
---

# Replication Package (ecopol-replication-package)

## When to trigger

- Empirical, experimental, or simulation results need to be made accessible and replicable
- Code is scattered across machines with hard-coded paths and no master script
- Data are restricted/proprietary and you need a verification plan that still works
- The Managing Editor / production process will ask for the datasets and programs underlying the figures
- You want the package ready before the conference so a discussant can probe a number on the spot

## EP's data standard: accessible and replicable, verified by the journal

EP's guidance is that **"all empirical, experimental and simulation results should, where possible, be accessible and replicable,"** and authors submit the datasets, programs, and sources for the journal to verify and publish alongside the article (检索于 2026-06；以官网为准). EP does not (as of this writing) run the AEA-style mandatory pre-acceptance Data Editor audit that AEJ:EP / QE use, so the bar is "where possible" rather than universal — but a paper feeding a policy recommendation lives or dies on whether its central number can be reproduced. Build the package as if a skeptical discussant will re-run it. Confirm the exact deposit location, README format, and any embargo rules in the live guidelines (待核实).

## What goes in the package

| Component | Requirement |
|-----------|-------------|
| Raw / source data | included if licensing allows; otherwise a precise acquisition guide |
| Cleaning code | from raw to analysis dataset, one master script, no manual steps |
| Analysis code | reproduces **every** number, table, and figure in the paper |
| Master script | runs end-to-end with one command; relative paths only |
| README | data sources, software + versions, run instructions, expected runtime |
| Data citations | each dataset cited with provider, version, access date |
| Mapping | exhibit → script → output (so a discussant can find any number fast) |

## Handling restricted policy data

EP papers often use confidential administrative or central-bank data. When you cannot deposit the raw data:

- Provide the **full code** plus a synthetic or simulated dataset with the same structure so the pipeline runs end-to-end.
- Document the **exact access procedure** (the agency, the application route, the version) so a determined replicator can obtain it.
- Offer the journal a **verification path** (e.g., code run on-site, or output verified against a secure enclave) rather than nothing.
- State the restriction openly in the data section — silence reads as evasion to a discussant.

## Craft moves

- **One-command reproducibility.** A reviewer should clone, run `master`, and get your exhibits. Hard-coded `/Users/yourname/` paths are the most common failure.
- **Pin software versions.** "Stata 18.0", "R 4.4.1 with fixest 0.12" — not "recent version".
- **Map every headline number** to the line of code that produces it; the conference is live and you may be asked to show provenance.
- **Seed every simulation / bootstrap** and report the seed.
- **Keep the package legible**, not just runnable — a clear folder structure signals the same care the policy audience expects of the analysis.

## Checklist

- [ ] Master script runs end-to-end with one command, relative paths only
- [ ] Every table/figure/number in the paper is reproduced by the code
- [ ] README lists data sources, software + exact versions, run instructions, runtime
- [ ] Restricted data handled: synthetic data + access guide + verification path
- [ ] Each dataset formally cited (provider, version, access date)
- [ ] Exhibit → script → output mapping included
- [ ] Simulations/bootstraps seeded and the seed reported
- [ ] Deposit location / README format confirmed against live guidelines (待核实)

## Anti-patterns

- Hard-coded absolute paths that break on any other machine
- "Data available on request" with no code and no access procedure
- A package that produces some but not all of the paper's numbers
- Unpinned software versions, so the pipeline silently breaks on a newer release
- Treating replication as a post-acceptance afterthought when a discussant may probe it at the conference

## Output format

```text
【Journal】Economic Policy (EP)
【Skill】ecopol-replication-package
【One-command run】master reproduces all exhibits? Y/N
【Coverage】every number/table/figure reproduced? Y/N
【Restricted data plan】synthetic data + access guide + verification path
【Versions pinned】software + package versions listed? Y/N
【Exhibit→code map】present? Y/N
【Deposit spec】confirmed / 待核实
【Next skill】ecopol-referee-strategy
```
