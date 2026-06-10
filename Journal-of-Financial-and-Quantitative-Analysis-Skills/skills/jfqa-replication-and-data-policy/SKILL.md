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

## Pseudo-data recipe for licensed finance sources

CRSP, Compustat, TAQ, IBES, and OptionMetrics extracts cannot be redistributed, so the pseudo dataset carries the verification load:

1. Preserve the exact schema — variable names, types, and panel keys (permno/gvkey/date) — so merges run unchanged.
2. Simulate or scramble enough rows (say, 500 firms over 120 months; scale to your design) to exercise every merge, filter, and edge case: missing delisting returns, duplicate links, zero-volume days, fiscal-year changes.
3. Run the full pipeline on the pseudo data and confirm every program completes and every exhibit is produced in well-formed (not numerically identical) form.
4. In the read-me, state plainly that pseudo-data numbers will not match the paper, and specify the exact licensed extracts a verifier needs (data vendor, library/table names, variable list, query date range) to reproduce the real ones.

## Archive layout and dry-run protocol

```
jfqa-archive/
  README.md            # software + versions, data inventory, execution roadmap
  run_all.sh           # one-button rebuild of every table and figure
  code/                # numbered: 01_build_sample, 02_main_tables, ...
  data/raw/  or  data/pseudo/
  output/tables/  output/figures/
```

- Fresh-machine test: copy the archive to a clean directory (ideally a colleague's machine), run `run_all`, and diff the regenerated exhibits against the manuscript.
- Confirm the read-me reflects the academic-research-only license and the requirement that users acknowledge the code's origin.
- Because verification may be performed by an external service on randomly selected papers, write the read-me for a stranger with no context, not for your coauthors.

## Exception decision aid

| Data situation | Archive move | Exception at initial submission? |
|---|---|---|
| Standard WRDS sources (CRSP/Compustat/TAQ) | pseudo dataset + full code | no |
| Proprietary data under NDA (broker, exchange, bank) | pseudo dataset + request delayed/limited sharing | yes — request it now, not at acceptance |
| Hand-collected data from public filings | deposit the raw data itself | no |
| Commercial data with negotiable terms | ask the vendor early; default to pseudo data | only if sharing truly cannot occur |

## Output format

```
【Code】reproduces all tables/figures from raw data? [Y/N]
【Data】raw OR pseudo dataset that runs end-to-end? [which]
【Read-me】software/versions + execution roadmap? [Y/N]
【Deposit】JFQA Dataverse (Harvard), academic-use license? [Y/N]
【Exception】needed? if so, requested at INITIAL submission? [Y/N/NA]
【Next step】jfqa-submission
```
