---
name: ijcai-supplementary
description: Use when preparing IJCAI or IJCAI-ECAI supplementary material, technical appendices, ZIP files, proofs, derivations, data, source code, and resubmission files under deadline, format, size, anonymity, and reviewer-discretion constraints.
---

# IJCAI Supplementary

Use this when assembling or auditing IJCAI supplementary material. Reopen the current CFP and
FAQ because deadlines, file types, and size limits are cycle-specific.

## Supplement plan

- Separate the Technical Appendix from the Resubmission File. Do not mix prior-review
  material into the technical supplement.
- Keep the main paper self-contained; reviewers may choose not to read the appendix.
- Submit supplement and resubmission files by the full-paper deadline. IJCAI-ECAI 2026 did
  not use separate later deadlines for these files.
- Respect file type and size rules. IJCAI-ECAI 2026 allowed up to 50MB of supplementary
  material in PDF or ZIP format.
- Anonymize every file, archive name, directory name, path, metadata field, license header,
  screenshot, notebook output, and URL.
- Verify that ZIPs open, contain deterministic paths, and do not include cache files, hidden
  OS files, credentials, API keys, or large irrelevant artifacts.

## Placement decision: body, appendix, or ZIP

IJCAI reviewers may never open the supplement, so placement is a scoring decision. Sort each
artifact before assembling.

| Artifact | Where it belongs | Why |
| --- | --- | --- |
| Theorem statement, main result table | 7-page body | Load-bearing; reviewers must see it without the supplement |
| Full proof, extra derivations | Technical Appendix | Supports credibility but not required reading |
| Hyperparameter grids, full per-domain tables | Technical Appendix | Detail that would crowd the body |
| Runnable code, simulator, instance generator | Code/data ZIP | Reproducibility evidence reviewers may sample |
| Prior reviews and rejected version | Resubmission File only | Must stay out of the technical supplement |

## Worked vignette: a planning paper's split

A planning paper has a soundness theorem, a 40-domain coverage table, and a planner
implementation. Decision: the theorem statement and a condensed coverage summary stay in the
body; the proof and the full 40-domain table go to the Technical Appendix; the planner plus a
deterministic instance generator and seeds go in the ZIP; nothing from a prior IJCAI rejection
goes anywhere except the Resubmission File. This keeps the paper self-contained while giving a
skeptical search/planning reviewer a re-runnable artifact.

## Reviewer pushback and the venue-specific fix

- "Had to open the ZIP to understand the method." Move the missing protocol into the body; the
  appendix should deepen, not define, the contribution.
- "Appendix mixes in old reviews." Separate them into the Resubmission File; mixing risks an
  anonymity or policy flag.
- "Archive would not open or had absolute paths." Re-zip with relative deterministic paths and
  strip OS and cache files before the full-paper deadline, since there is no later upload.

## Output format

```text
[Supplement status] Ready / Needs fixes / Not ready
[Files] <technical appendix / code-data zip / resubmission file>
[Deadline coupling] <same as full paper? source needed>
[Anonymity checks] <passed/issues>
[Reviewer dependency] <what breaks if supplement is ignored>
```
