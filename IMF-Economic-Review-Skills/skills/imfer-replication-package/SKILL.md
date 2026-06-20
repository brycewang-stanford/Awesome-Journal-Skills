---
name: imfer-replication-package
description: Use when an IMF Economic Review (IMFER) manuscript's data and code must be packaged for reproducibility — including restricted IMF/central-bank data paths, cross-country source lineage, and a runnable environment. Builds the package; it does not produce the exhibits (imfer-tables-figures) or run the submission preflight (imfer-submission).
---

# Replication Package (imfer-replication-package)

## When to trigger

- The analysis is settled and the data/code package must be assembled before submission or at acceptance
- Some inputs are **restricted** (IMF program data, central-bank micro data, proprietary flows) and cannot be redistributed
- A cross-country dataset stitches many sources (IFS, BOP, WEO, BIS, EPFR, national accounts) and the lineage is undocumented
- A referee or editor asks for a reproducibility check or a data-availability statement
- Code runs only on one machine; seeds, versions, and the build order are not pinned

## The IMFER reproducibility reality

IMFER work leans on **international-macro data that is often partly restricted** — IMF surveillance data, central-bank confidential series, commercial flow data (EPFR), or program-specific files. The package must make everything **reproducible in principle even when some inputs cannot be shipped**: provide the build scripts, the exact source and vintage of each series, and clear instructions for obtaining the restricted inputs, so a replicator with access can rebuild the analysis dataset and regenerate every exhibit. Confirm the journal's current data-availability and deposit requirements on the official pages (检索于 2026-06；以官网为准).

| Package element | What it must contain |
|-----------------|----------------------|
| Data-availability statement | for each input: public vs. restricted; source; vintage; how a replicator obtains it |
| Source-to-analysis lineage | raw downloads → cleaning → analysis dataset, scripted and ordered |
| Restricted-data handling | the build script + access instructions; never ship confidential micro data |
| Code | numbered, run-in-order scripts that regenerate every table and figure |
| Environment | language versions and packages pinned (lockfile / sessionInfo / `requirements`) |
| Codebook / data dictionary | variable definitions, country codes, units, currency conventions, transformations |
| Seeds & determinism | seeds set and reported for any simulation / bootstrap / estimation |
| README | one-command (or clearly stepped) path from inputs to all exhibits |
| Mapping table | each table/figure → the script and line that produces it |

### The restricted-data spectrum (classify each input)
International-macro inputs are rarely all-public or all-secret; classify each on a spectrum and document accordingly. **Fully public** (IFS, WEO, BIS statistics, World Bank): ship the pull scripts and vintage. **Public-but-licensed** (Bloomberg, Refinitiv, EPFR, Datastream): ship cleaning code plus the license/access route, not the raw series. **Restricted-by-agreement** (central-bank confidential micro data, IMF surveillance files): ship the build script plus contact/access instructions and any aggregate that the agreement permits. **Author-constructed** (a hand-coded narrative classification, an event list): ship it in full with the coding rules. The data-availability statement is just this classification made explicit, input by input.

## Packaging craft

1. **Map every series to a source and vintage.** Cross-country panels silently mix vintages (a WEO release, an IFS pull); record exactly which, because revisions change results.
2. **Separate public from restricted up front.** Write the data-availability statement first; it dictates what ships and what needs access instructions.
3. **Script the build, do not hand-edit.** Every transformation from raw to analysis dataset must be in code, so a replicator with the restricted input can reconstruct your sample.
4. **Pin the environment.** International-macro pipelines often span Stata, R, and Python; lock each so results do not drift with package updates.
5. **Regenerate exhibits from scratch** in a clean environment before submission — the most common failure is a figure that no longer matches the script.
6. **Document country and currency conventions** in the codebook; a replicator must know your USD/local, gross/net, deflator choices.

## Checklist

- [ ] Data-availability statement: each input classified public/restricted with source, vintage, access path
- [ ] Restricted inputs never shipped; access instructions + build script provided instead
- [ ] Raw-to-analysis lineage fully scripted and ordered
- [ ] Numbered code regenerates every table and figure
- [ ] Environment pinned (versions + packages) across all languages used
- [ ] Codebook covers variables, country codes, units, currency/deflator/gross-net conventions
- [ ] Exhibit-to-script mapping table provided (every table/figure traceable to its code)
- [ ] Seeds set and reported for simulation/bootstrap/estimation
- [ ] Clean-environment rebuild verified; exhibits match the scripts
- [ ] Current deposit / data-availability rules confirmed on official pages or marked 待核实

## Anti-patterns

- Shipping confidential IMF/central-bank micro data instead of access instructions
- A panel with no record of which data vintage was used (results not reconstructable after revisions)
- Hand-edited intermediate files that no script can reproduce
- Unpinned environment, so a referee's rerun drifts from the paper
- A README that assumes the author's exact machine and paths
- Treating reproducibility as an acceptance-time afterthought rather than building it in
- A data-availability statement that says "available on request" for inputs that have a real public source or access route

## Worked vignette (illustrative)

A capital-flows paper merges EPFR fund flows (commercial, licensed), IFS balance-of-payments (public), and a central bank's confidential intervention log (restricted). The package ships the public IFS pulls and all build scripts, but for EPFR and the intervention log it ships only the *cleaning code plus access instructions* (how to license EPFR, whom to contact at the central bank). The data-availability statement classifies each input, records the IFS vintage (2024 Q1 release) and the EPFR pull date, and the README runs the public-data portions end to end. A replicator with the licenses can rebuild the full analysis dataset and regenerate every exhibit — reproducible in principle without redistributing restricted data.

## Referee/editor pushback mapped to the package fix

- *"Some inputs are restricted — is this reproducible?"* → Provide build scripts plus access instructions for the restricted inputs; never ship them.
- *"Which data vintage produced these numbers?"* → Record source and vintage for every series in the data-availability statement and codebook.
- *"Your rerun gives different numbers."* → Pin the environment across Stata/R/Python and verify a clean-environment rebuild before submission.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-replication-package
【Data-availability】public vs restricted, with sources + vintages: ___
【Restricted handling】access instructions + build script (not shipped): ___
【Lineage】raw→analysis fully scripted? [Y/N]
【Code】numbered, regenerates all exhibits? [Y/N]
【Environment】versions/packages pinned across languages? [Y/N]
【Codebook】variables, country codes, currency/gross-net conventions? [Y/N]
【Clean rebuild】exhibits match scripts? [Y/N]
【Next skill】imfer-referee-strategy
```
