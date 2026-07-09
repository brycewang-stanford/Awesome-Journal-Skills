---
name: conext-reproducibility
description: Use when building the reproducibility story for an ACM CoNEXT paper — pinned traces and configs, a runnable artifact, an honest data-availability posture, and the one-page artifact description the CoNEXT reproducibility committee needs — remembering that the ACM badge opt-in is due before the submission deadline.
---

# CoNEXT Reproducibility

Build the reproducible-networking story alongside the experiments, not after acceptance. CoNEXT runs
a dedicated **reproducibility committee** that awards **optional ACM badges**, and the single most
missed rule is that **badge eligibility requires opting in before the paper submission deadline** —
you cannot bolt it on later. Even for authors who skip badging, a reproducible artifact strengthens
a double-anonymous, one-shot-revision review.

## The timing trap (read this first)

```text
[Before the submission deadline]  OPT IN for ACM badging (required for eligibility)
[At submission]                   anonymized, runnable artifact referenced from the paper
[Within ~1 week of acceptance]    send a ONE-PAGE artifact description to the reproducibility
                                  committee with pointers to code and other artifacts
[Camera-ready / post-accept]      committee evaluates for Available / Functional / Reusable /
                                  Reproduced badges (see conext-artifact-evaluation)
```

Miss the opt-in and the strongest artifact in the world cannot earn a badge this cycle.

## What "reproducible" means for a networking paper

Networking reproducibility is harder than "here is the code," because the result depends on an
environment:

- **Traces:** the exact captures, with vantage points, dates, and anonymization documented, plus the
  extraction scripts that turn raw captures into the paper's inputs.
- **Configs:** the exact parameters, topology, and settings used for each figure — not a
  representative example.
- **Environment:** hardware models, firmware, kernel/OS versions, link rates, and buffer depths for
  a testbed; container/VM images where feasible.
- **Pipeline:** a scripted path from raw data/trace to each table and figure, so the numbers
  regenerate rather than being hand-copied.

## Pin provenance at collection time

You cannot reconstruct provenance after the campaign ends:

- Record capture vantage points, timestamps, and anonymization method **as you collect**.
- Snapshot configs and firmware/OS versions **at run time**; a later "we think it was v2.1" is not
  reproducible.
- For ML-for-networking, pin model identifiers and dates and **cache raw model outputs** — a package
  that needs live API calls re-samples rather than reproduces.

## Honest data-availability posture

- If you can release traces/code, do — with a DOI-issuing archive (Zenodo/figshare/Software
  Heritage) and an open license.
- If operator agreements or privacy limits block release, **say so and why**, and release what you
  can (aggregate data, synthetic traces, the analysis pipeline). "Available upon request" reads as a
  scored weakness, not a neutral placeholder.
- Keep the availability statement **honest and matched** to what the artifact actually contains — a
  reviewer or the committee will check.

## Anonymity of the artifact (double-anonymous review)

- Re-host the artifact behind an **anonymizing service** before submission; scrub commit metadata,
  internal hostnames, and owner-identifying paths.
- Topology diagrams and configs can leak an operator or institution — sanitize AS numbers, hostnames,
  and IP ranges you own.
- The reproducibility material referenced at review time must not de-anonymize you.

## The one-page artifact description

After acceptance, the committee wants a **one-page** description that lets an evaluator start
quickly:

- What the artifact contains (code, traces, configs, testbed scripts) and pointers to each.
- The hardware/software the evaluator needs, and any hardware you must provide access to (some
  networking artifacts need specific switches/NICs — flag this early).
- A short "getting started" path and the claims the artifact supports.

## Pre-submission reproducibility audit

```text
[Opt-in]        badge opt-in done BEFORE the submission deadline? (if badging) yes/no
[Traces]        captures + vantage points + dates + extraction scripts present? yes/no
[Configs]       exact per-figure configs and topology recorded? yes/no
[Environment]   hardware/firmware/OS versions pinned; image where feasible? yes/no
[Pipeline]      raw -> figure regenerates by script? yes/no
[Availability]  honest statement; DOI archive or a documented reason not to release? yes/no
[Anonymity]     artifact re-hosted anonymously; metadata scrubbed? yes/no
```

## Output format

```text
[Reproducibility status] ready / gaps
[Badge intent] opt-in before submission? yes/no/n-a
[Provenance] traces/configs/environment pinned at collection time
[Availability] what is released, where (DOI), and any documented restriction
[Anonymity] artifact anonymized for double-anonymous review
[One-pager] artifact description drafted for the committee (post-accept)
```
