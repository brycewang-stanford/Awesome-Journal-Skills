---
name: ase-reproducibility
description: Use when building the open-science and reproducibility story for an ASE (IEEE/ACM Automated Software Engineering) submission, covering the mandatory Data Availability Statement, anonymized-but-runnable tools, tool and subject-system provenance pinning, cached LLM outputs, and staging for the ACM Available/Reusable artifact badges.
---

# ASE Reproducibility

Build the reproducibility story at data-collection time, not at submission. ASE requires a
**mandatory Data Availability Statement** in the paper and expects an **anonymized, runnable**
artifact at review time; automated-SE artifacts are usually *tools*, so "runnable" means a reviewer
can actually execute the automation on stated subjects. What is not pinned when you collect it
cannot be reconstructed later.

## The mandatory Data Availability Statement

- **Required**, placed **after the Conclusions** and **inside the 10-page limit** (it is not free
  appendix space).
- State what exists — the tool, the dataset, the subject systems, the scripts, the logs — and
  **where it will live** after acceptance (an archival DOI target).
- Provide an **anonymized** link or upload now; "available upon request" reads as a scored weakness,
  not a neutral placeholder.
- Match the statement to what the archive actually contains — an overclaiming statement is worse
  than a modest, honest one.

## Anonymized-but-runnable tools

- Re-host the tool and dataset behind an **anonymizing service**; strip repository owner, commit
  author metadata, and any path revealing your identity (`/home/<you>/`, institutional URLs).
- Include a **minimal run path**: exact commands, expected inputs, and a small sample so a reviewer
  can execute the automation without your machine.
- Pin the environment: dependencies with versions, a container or lockfile, and the exact tool
  commit — automated-SE tools rot fast against moving toolchains.

## Provenance pinning (do this at collection time)

For the tool:
- Exact **commit SHA**, build instructions, dependency versions, and configuration/flags used in the
  experiments (including seeds for randomized components).

For subject systems and datasets:
- **Names, versions, and SHAs** of every subject; the corpus **extraction date**; query/filter
  criteria; and any manual **labeling protocol** with inter-rater agreement.
- A regeneration script and a versioned snapshot — live scraping re-samples a moving target.

For LLM-based components:
- **Model identifiers and dates**, prompts, decoding settings, and **cached raw outputs** so the
  artifact reproduces rather than calls a live, drifting API.

## Reproducibility failure modes (ASE-specific)

| Failure | Consequence | Prevention |
|---|---|---|
| Tool needs your exact machine | Reviewers cannot run it; artifact fails | Container/lockfile + minimal run path |
| Subjects unpinned (branch, not SHA) | Numbers cannot be reproduced | Record SHAs + extraction date at collection |
| LLM outputs uncached | Re-runs drift; comparison invalid | Cache outputs; record model IDs/dates |
| Data Availability outside the 10 pages | Policy violation | Place it after Conclusions, inside the budget |
| Identity leak in artifact | Anonymity violation | Scrub owner/metadata; re-host anonymized |

## From submission to the ACM badges

The submission-time artifact and the post-acceptance badge artifact are the *same package* matured.
ASE offers **Artifacts Available** and **Artifacts Reusable** badges (ACM scheme); staging for them
now avoids a scramble later (see `ase-artifact-evaluation`):

- **Available** — deposit in a DOI-issuing archive (Zenodo / figshare / Software Heritage) with an
  open license.
- **Reusable** — documentation, a clear run path, and structure that lets a stranger reuse the tool
  beyond reproducing your tables.

## Output format

```text
[Data Availability] present, after Conclusions, inside 10pp? matches the archive?
[Tool] commit pinned, deps versioned, container/lockfile, minimal run path?
[Subjects/data] SHAs + extraction date + selection/labeling protocol recorded?
[LLM] model IDs/dates, prompts, cached outputs?
[Anonymity] owner/metadata scrubbed; anonymized re-host?
[Badge readiness] Available (DOI+license) / Reusable (docs+run path) staged?
```
