---
name: psychbull-open-science-and-transparency
description: Use when planning and assembling the transparency package for a Psychological Bulletin submission — protocol preregistration (PROSPERO/OSF), TOP-compliant disclosure, and depositing the database, codebook, and analysis scripts. Covers transparency requirements; it does not run the analysis.
---

# Open Science & Transparency (psychbull-open-science-and-transparency)

Effective **February 1, 2022**, Psychological Bulletin requires **transparent reporting for empirical
work, including meta-analyses**, aligned with the **TOP Guidelines**. Authors who submit quantitative
analyses must **supply their database, codebook, and relevant scripts**, and must **state whether the
design/hypotheses were preregistered and where to access them**. Build this as you go — it is not a
last-minute add-on. (Verify the exact TOP level wording on the live page; see 待核实 in the source map.)

## When to trigger

- Before screening — to **preregister the protocol**
- Assembling the data/code/materials package for submission
- Answering the journal's transparency/availability statements
- A reviewer asks where the database, codebook, or scripts live

## Preregister the protocol (before screening)

- Register the **review protocol** on **PROSPERO** (the systematic-review registry) or **OSF
  Registries**: question, eligibility criteria, search plan, coding plan, and the **pre-specified
  analysis and moderators**.
- The manuscript must **state whether work was preregistered and where to access it**.
- **Masking note:** Bulletin submissions registered on PROSPERO may **attach registration details as
  an appendix, omitting author names and the registration number** so review stays masked.
- Clearly distinguish **pre-specified (confirmatory)** from **exploratory** analyses in the writeup.

## The transparency package (TOP)

1. **Database** — the coded effect-size dataset (one row per effect, with study identifiers and
   moderator codes), in an open format.
2. **Codebook** — variable definitions and decision rules (from `psychbull-inclusion-and-coding`).
3. **Analysis scripts** — code that reproduces every pooled estimate, moderator model, bias diagnostic,
   table, and figure.
4. **Materials** — search strings/logs, screening records, and the PRISMA-flow inputs.
5. Deposit to a **trusted repository** (OSF / institutional) with a **persistent identifier (DOI)**;
   complete the journal's **data-availability statement**, explaining any restricted data.

## Anti-patterns

- Preregistering *after* screening (defeats the purpose)
- "Available upon request" instead of a deposited, identifiable package
- A dataset no one else could re-run (no codebook, undocumented variables)
- Leaving the PROSPERO number / author names in an appendix during masked review
- Blurring confirmatory and exploratory analyses

## Output format

```
【Protocol】preregistered (PROSPERO/OSF) before screening? [Y/N] + where
【Masking】PROSPERO appendix anonymized (no number/names)? [Y/N]
【Database + codebook】deposited with DOI? [Y/N]
【Scripts】reproduce all estimates/exhibits? [Y/N]
【Availability statement】drafted; restricted data explained? [Y/N]
【Confirmatory vs exploratory】clearly separated? [Y/N]
【Next】psychbull-submission
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — PROSPERO, OSF, TOP, repositories, reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — TOP (Feb 1 2022), data/codebook/scripts, preregistration/PROSPERO policy
