---
name: jfqa-replication-and-data-policy
description: Use when building the code and data archive required by the Journal of Financial and Quantitative Analysis (JFQA) Code Sharing Policy — source code reproducing all findings, raw or pseudo datasets, and a read-me with an execution roadmap, deposited in the JFQA Dataverse at the Harvard University Dataverse. Use to prepare the mandatory archive for accepted post-2024 submissions and to request any exception at initial submission.
---

# JFQA Replication & Data Policy (jfqa-replication-and-data-policy)

Use this skill to satisfy the **JFQA Code Sharing Policy**. It is **mandatory** for submissions made **on or after January 1, 2024** if the paper is accepted (voluntary for earlier submissions). Materials are posted **at acceptance, before online publication**. Re-verify the live policy before final packaging.

## What you must deposit

1. **Source code** that reproduces **all reported findings from the raw data** — every table and figure.
2. **The raw datasets**, OR — if restricted by copyright/confidentiality (common with CRSP, Compustat, TAQ, etc.) — a **pseudo dataset** with enough observations that all programs **execute successfully**.
3. A **"read me" file** documenting the software, languages, and data formats, plus a **roadmap of the program execution order** when there are multiple programs.

## Where it goes

- Archived in the **JFQA Dataverse**, hosted at the **Harvard University Dataverse**, as supplemental materials.
- Code is licensed for **academic research only**; users must **acknowledge the code's origin**.

## Exceptions (timing matters)

- Any **exception** — e.g., delayed code sharing — must be requested **on the initial submission**, not later. The handling editor decides; an **approved exception is noted in the published paper**.

## Verification

- JFQA may use **external verification services** to validate code for **randomly selected** publications. Build the package so a third party can run it end-to-end from the (raw or pseudo) data.

## Build discipline

- One **master script** (`run_all`) regenerating every exhibit from the deposited data.
- **Pin** software/package versions; **set and report seeds** for any bootstrap/simulation.
- Keep paths relative; ensure the pseudo dataset triggers every code path.

## Output format

```
【Code】reproduces all tables/figures from raw data? [Y/N]
【Data】raw OR pseudo dataset that runs end-to-end? [which]
【Read-me】software/versions + execution roadmap? [Y/N]
【Deposit】JFQA Dataverse (Harvard), academic-use license? [Y/N]
【Exception】needed? if so, requested at INITIAL submission? [Y/N/NA]
【Next step】jfqa-submission
```
