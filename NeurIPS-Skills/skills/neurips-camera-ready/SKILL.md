---
name: neurips-camera-ready
description: Use when preparing accepted NeurIPS papers for camera-ready upload, de-anonymization, final checklist, code/data release, OpenReview metadata, and post-acceptance obligations.
---

# NeurIPS Camera-Ready

Use this skill only after acceptance. Camera-ready work is not just formatting: it is where anonymous
review artifacts become public scientific records.

## Official items to reopen

- Current camera-ready instructions in OpenReview and the yearly NeurIPS handbook.
- Final template and style file.
- Final page, file-size, checklist, appendix, and upload rules.
- Proceedings license, author metadata, presenter/registration requirements, and any presentation
  or poster instructions.

## 2026 baseline facts

The 2026 handbook states that accepted papers get one additional content page for camera-ready and
that camera-ready upload happens through the OpenReview paper page by selecting the camera-ready
version. It also says the final PDF combines paper pages, references, text appendices, and the
paper checklist. Treat these as 2026 facts, not permanent rules.

## Camera-ready workflow

1. Resolve reviewer and AC issues that are allowed in camera-ready without changing the accepted
   contribution beyond recognition.
2. De-anonymize authors, acknowledgments, repositories, datasets, model cards, code comments, and
   supplementary artifacts.
3. Update the checklist so every answer reflects the final paper and public artifacts.
4. Replace anonymous review links with stable public links, preferably with archived code and
   persistent dataset identifiers where appropriate.
5. Verify that all figures, tables, citations, appendices, and artifact instructions match the
   final claims.
6. Run a final integrity pass for hallucinated citations, broken links, hidden author metadata, and
   accidental private data.

## Output format

```text
[Camera-ready status] Ready / Needs fixes
[Official instructions checked] <URLs or missing items>
[Allowed paper changes] <summary>
[Public artifact tasks] <code/data/model/repo/archive>
[Final integrity risks] <citation/anonymity/license/privacy/checklist>
```

