---
name: aaai-camera-ready
description: Use when preparing an accepted AAAI paper for camera-ready source submission to AAAI Press, including proceedings page limits, two-column template compliance, copyright transfer, purchased extra technical pages, deanonymization, registration, oral or poster presentation, and final public artifact release.
---

# AAAI Camera Ready

Use this after AAAI acceptance. Reopen the current camera-ready email, publication/attendance page,
author kit, copyright instructions, and proceedings source-file requirements.

## Camera-ready checklist

- Apply the current AAAI proceedings template and page rules. AAAI-26 accepted main-track papers
  used 7 proceedings pages plus pages solely for references and acknowledgments, with an option to
  purchase up to two additional technical-content pages.
- Prepare source files as required: LaTeX or Word source, figures, bibliography, style files, and a
  high-resolution PDF.
- Add author names, affiliations, acknowledgments, funding, and ethical disclosures where required.
- Keep all references from the submitted paper unless superseded, and explain major citation updates
  conservatively.
- Resolve reviewer-facing clarity issues without changing the scientific identity of the paper.
- Complete copyright transfer and any AAAI Digital Library metadata.
- Ensure at least one author registers and presents the paper, unless current exceptional-circumstance
  procedures apply.

## AAAI Press production gotchas

AAAI Press compiles the proceedings from your source, so a PDF that looks fine locally can still be
kicked back. The two-column AAAI style is strict about a few things that trip up authors arriving
from single-column or NeurIPS-style submissions:

- Do not alter margins, font sizes, or column gap; AAAI explicitly forbids style hacks to gain space.
  If you need room, purchase technical pages instead of shrinking the template.
- Disable `\pdfoutput` overrides and embed all fonts; non-embedded fonts are a common rejection.
- Move references and acknowledgments into the pages that do not count against the technical limit,
  per the current rule, rather than padding the main body.
- Restore author block, funding, and ethics statements that were stripped for double-blind review.

## Deanonymization sweep

Acceptance reverses the anonymity discipline: now identity must be present and correct, while stale
blind-mode placeholders must go. Walk the paper, supplement, and code for "Anonymous", redacted
citations to your own prior work, and `\\if-blind` toggles still set to blind.

## Worked vignette

A knowledge-representation paper lands at 7.5 technical pages after restoring the author block and an
ethics statement. Decision: it cannot shrink the template, so the author buys one extra technical
page (within the current cap), keeps references on the non-counting pages, and re-runs the
deanonymization sweep before uploading source to AAAI Press.

## Release plan

- Replace anonymous code/data links with durable public repositories or archives.
- Publish a project page only if it is stable, accurate, and does not overclaim beyond the paper.
- Preserve a copy of the submitted PDF, reviews, rebuttal, accepted PDF, source package, and artifact
  release for future journal extensions.

## Output format

```text
[Camera-ready state] Ready / Needs fixes / Blocked
[Proceedings files] <PDF/source/bib/figures/supplement>
[Page status] within limit / extra pages needed / over limit
[Publication obligations] copyright / registration / presentation / metadata
[Final fixes] <ordered list before upload>
```

