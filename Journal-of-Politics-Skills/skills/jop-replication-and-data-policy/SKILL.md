---
name: jop-replication-and-data-policy
description: Use when preparing the replication / data-access materials for a The Journal of Politics (JOP) manuscript. JOP makes acceptance contingent on replicability — a JOP replication analyst assigned at conditional acceptance assesses the package you deposit in the JOP Dataverse (Harvard Dataverse), and non-replicable manuscripts are rejected. Prepares the package; it does not waive the requirement.
---

# Replication & Data Policy (jop-replication-and-data-policy)

This is JOP's signature skill. JOP does not merely request a deposit — **acceptance is contingent on
replicability**. A **JOP replication analyst**, assigned at **conditional acceptance**, assesses your
materials before publication, and **manuscripts that are not replicable are rejected**. Build the package
**as you analyze**, not at acceptance.

## When to trigger

- Building the replication / data-access package (start during analysis)
- A manuscript reached **conditional acceptance** and a replication analyst was assigned
- Data cannot be fully shared (privacy, ethics, legal/provider restrictions) and you need the path
- Any empirical, simulation-based, or formal-theoretical paper headed for JOP

## What JOP requires (verify current wording on the policy page)

1. **Replicability-contingent acceptance.** It is JOP policy to publish a paper only if the data are
   **accessible**, the analyses **fully documented**, and the empirical findings **reproducible**. The
   conditional accept is *conditional* on passing this check.
2. **The JOP replication analyst.** At conditional acceptance, a JOP analyst is assigned and **initially
   assesses replicability**. This is an in-house JOP check — distinct from APSR's editorial-office
   reproduction and AJPS's external third-party verifier. Treat it as a real gate.
3. **Deposit to the JOP Dataverse.** Materials are uploaded to **The Journal of Politics Dataverse on
   Harvard Dataverse** as a **single .zip file**, with permanent DOIs, and made **publicly available at
   the time of publication**.
4. **The four required items.** A **readme** (lists/describes every file, plus operating system and
   software version), the **dataset(s)** (all variables used to produce every figure, table, and
   quantitative result), a **codebook** (names and defines every variable), and the **code**.

## When data cannot be shared (access path)

- **Explain why** the data cannot be shared (ethics, privacy, or provider/legal restriction).
- Give **README instructions on exactly how others can obtain the data** (access process, contact).
- Where possible, **provide synthetic or simulated data** so the code can be exercised end-to-end.

## Build-as-you-go checklist

- [ ] One **master script** regenerates **every** table, figure, and reported number from raw/constructed data
- [ ] **readme** documents every file, the OS, and exact **software/package versions**
- [ ] **Codebook** names and defines every variable used in the analysis
- [ ] **Seeds** set and reported for every stochastic step
- [ ] Exhibit/number-in-text values **match** the package output exactly
- [ ] Everything bundled as a **single .zip** ready for the JOP Dataverse
- [ ] Restricted data: explanation + access instructions + synthetic data where feasible

## Anti-patterns

- Treating the deposit as a post-acceptance afterthought (it gates publication; the analyst re-checks)
- Depositing code that does not reproduce the printed tables/figures (non-replicable → rejected)
- A personal URL or generic cloud link instead of the JOP Dataverse
- Missing the codebook or version/OS info the readme must contain
- Claiming data are restricted without an access path or synthetic substitute

## What the analyst checks (failure-mode table)

The JOP analyst's re-run is mechanical: it either regenerates your printed numbers or it does not. Close
each common failure before conditional acceptance.

| Failure the analyst will hit | Close it before deposit |
|------------------------------|--------------------------|
| Script errors on a clean machine | Master script, relative paths, fresh-clone test |
| Numbers drift from the printed table | Regenerate every exhibit from code; re-run end to end |
| Stochastic result will not reproduce | Set and report a seed for every random step |

## Worked micro-example (illustrative)

The AVR-turnout author reaches conditional acceptance and the analyst runs the .zip. On a fresh clone the
master script fails because the working directory was hard-coded — tested only on the author's machine.
After a relative-path fix it runs, but the turnout estimate prints as +1.79 against the paper's +1.8, a
rounding mismatch. The author aligns the table to the script's value, confirms the seed reproduces the
bootstrap CI, and the re-run matches the printed page.

## Analyst pushback patterns and the JOP fix

- *"Your code does not run on my machine."* Test from a fresh clone with no local state, use relative
  paths, and pin software and package versions in the readme.
- *"Confirm the data are restricted as claimed."* Confirm the journal's current sharing expectations
  against the policy page before relying on a restricted-data path.

## Output format

```
【Repository】JOP Dataverse (Harvard) — single .zip staged? [Y/N]
【Reproduces everything?】master script re-runs all results locally? [Y/N]
【Four items】readme + dataset(s) + codebook + code present? [Y/N]
【Versions + seeds】OS/software recorded, seeds set? [Y/N]
【Restricted data?】explanation + access path + synthetic data?
【Next】jop-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and qualitative-transparency options (QDR)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JOP data-replication policy, replication analyst, JOP Dataverse
