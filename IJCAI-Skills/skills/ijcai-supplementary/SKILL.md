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

## Output format

```text
[Supplement status] Ready / Needs fixes / Not ready
[Files] <technical appendix / code-data zip / resubmission file>
[Deadline coupling] <same as full paper? source needed>
[Anonymity checks] <passed/issues>
[Reviewer dependency] <what breaks if supplement is ignored>
```
