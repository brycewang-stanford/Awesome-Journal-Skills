# Clinical Medicine Journal Skills

<p align="center">
  <img src="assets/cover.svg" alt="Clinical Medicine Journal Skills — 30 flagship specialty clinical-medicine journals" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Index](https://img.shields.io/badge/index-JAMA%20%C2%B7%20Lancet%20%C2%B7%20Radiology%20%C2%B7%20Brain-1f6feb)](#)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

An opinionated agent skill stack for **30 flagship English-language specialty clinical-medicine journals** — deepening the clinical-medicine category beyond the general big-four (NEJM, Lancet, JAMA, BMJ) and the broad-specialty venues already covered by the natural-science bundle. It covers the JAMA Network specialty journals (Internal Medicine, Oncology, Cardiology, Neurology, Pediatrics, Psychiatry, Surgery), the Lancet specialty titles (Respiratory Medicine, Diabetes & Endocrinology, Public Health, Psychiatry), and the leading society/specialty flagships across oncology, respiratory/critical care, nephrology, endocrinology, hepatology/GI, allergy/immunology, rheumatology, neurology, radiology, anesthesiology, obstetrics/gynecology, and urology.

This is the specialty-clinical sibling of [`English-NaturalScience-Journal-Skills`](../English-NaturalScience-Journal-Skills/) (which holds the general big-four and broad-specialty clinical flagships). Like the other bundles, it ships **one self-contained fit-and-house-style skill per journal**, plus `en-clinmed-journal-workflow` for routing. Each journal skill helps answer: *is my study on-target for this specialty venue, how should it be framed, what clinical evidence and reporting standard does it expect, and what official submission details (article type, reporting checklist, trial registration, ethics, disclosures) must be re-checked?*

> These skills are **venue-fit and house-style aids only**. They are not clinical, diagnostic, or regulatory advice.

## Coverage

| Group | Count |
|---|--:|
| JAMA Network specialty journals | 7 |
| The Lancet specialty titles | 4 |
| Oncology · respiratory/critical care · nephrology · endocrinology | 8 |
| Hepatology/GI · allergy/immunology · rheumatology · neurology | 6 |
| Radiology · anesthesiology · ob-gyn · urology | 5 |
| **Total journal skills** | **30** |
| Routing workflow (`en-clinmed-journal-workflow`) | 1 |

## How to use

1. **Route first.** Start from `en-clinmed-journal-workflow` to classify your study by
   specialty, study design (RCT / observational / diagnostic-accuracy / review), and
   evidence strength, and get a ranked shortlist of candidate venues.
2. **Fit second.** Open the single-journal skill for your top candidate to test scope
   fit, framing, the clinical-evidence bar, house style, and likely desk-reject triggers.
3. **Re-check official rules last.** Every skill ends with an official-submission
   checklist. Before submitting, open the journal's current instructions for authors
   (see `resources/official-source-map.md`), confirm the applicable reporting guideline
   (CONSORT/PRISMA/STROBE/STARD) and trial registration — the live page always wins.

## Design rules (shared with the sibling bundles)

- **No volatile facts.** No impact factors, acceptance rates, ISSNs, exact limits, APC
  amounts, or editor names.
- **No fabricated citations.** Literatures are referred to generically.
- **No clinical advice.** These are venue-fit and house-style tools.
- **Stable conventions only.** Durable structural facts (structured abstracts, the
  evidence hierarchy, ICMJE trial-registration and authorship rules, the EQUATOR
  reporting guidelines, society affiliations) are used where they help fit.
- **Official page wins.** If a live instruction conflicts with a skill, follow the
  official instruction.

## License

MIT © 2026 Bryce Wang. See [LICENSE](LICENSE).
