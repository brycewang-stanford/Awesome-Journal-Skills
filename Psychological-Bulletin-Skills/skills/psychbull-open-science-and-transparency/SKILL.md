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

## What transparency referees verify

As an APA flagship that adopted TOP-aligned reporting, Psychological Bulletin treats the transparency
package as a reviewable deliverable, not a courtesy. The bar reviewers apply:

| Transparency item | Pass | Reject / desk-return trigger |
|-------------------|------|------------------------------|
| Protocol timing | Preregistered before screening, location stated | Registered after coding, or "available on request" |
| Database deposited | One-row-per-effect file with a DOI | No data, or a spreadsheet no one else can run |
| Codebook deposited | Variable definitions and decision rules included | Undocumented columns; codes unexplained |
| Scripts deposited | Reproduce every estimate, table, and figure | Numbers in text that no script regenerates |
| Masking preserved | PROSPERO appendix stripped of number and names | Registration number visible during masked review |

## Worked vignette — assembling the package

*Illustrative figures only.* For the self-affirmation synthesis (k = 42, g = 0.34), the deposit under
this skill's rules:

- **Protocol** on OSF Registries timestamped before screening, listing eligibility, the search plan, and
  the delivery-format moderator as confirmatory.
- **Database**: 51 rows (42 studies, 9 contributing multiple effects), each with study ID, g, variance,
  and moderator codes, in an open CSV with a DOI.
- **Codebook** carried over from the inclusion-and-coding stage, defining all 23 variables.
- **Scripts**: one `metafor`/`robumeta` script regenerates the pooled 0.34, the meta-regression
  (R²-analog 0.22), every bias diagnostic, the forest and funnel plots, and the summary table.
- **Masking**: the PROSPERO/OSF appendix is anonymized, with the registration number and author names
  removed, so review stays masked.

## Referee pushback → venue-specific fix

- *"Was this preregistered, and where?"* → Add the registry link and the timestamp predating screening;
  state explicitly which analyses were confirmatory.
- *"'Data available on request' is insufficient."* → Deposit the database, codebook, and scripts to a
  trusted repository with a persistent DOI and complete the availability statement.
- *"Confirmatory and exploratory analyses are blurred."* → Separate them in both the manuscript and the
  deposited scripts so the distinction is auditable. (Confirm the exact TOP level on the live page.)

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
